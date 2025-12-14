"""
Part Resolver - 부품 → 심볼/풋프린트 매핑 v1.4

easyeda2kicad를 통해 LCSC 부품의 심볼/풋프린트를 자동으로 가져옵니다.
v1.1: footprint_override 지원 추가
v1.4: 에러 처리 강화, 캐시 무결성 검증
"""

import hashlib
import json
import logging
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from .config_loader import PartSpec
from .exceptions import (
    PartResolveError,
    EasyEDAError,
    NetworkError,
    CacheError,
    SymbolParseError,
)

logger = logging.getLogger(__name__)

# 캐시 메타 버전 (구조 변경 시 증가)
CACHE_META_VERSION = 2


@dataclass
class ResolvedPart:
    """리졸브된 부품 정보."""
    ref: str                          # Reference designator
    role: str                         # 역할
    symbol_lib: Optional[Path] = None # 심볼 라이브러리 파일 경로
    symbol_name: str = ""             # 심볼 이름
    footprint_lib: Optional[Path] = None  # 풋프린트 라이브러리 경로
    footprint_name: str = ""          # 풋프린트 이름
    footprint_override: str = ""      # 사용자 지정 풋프린트 (우선 적용)
    value: str = ""                   # 값
    lcsc: str = ""                    # LCSC 부품번호
    manufacturer: str = ""            # 제조사
    description: str = ""             # 설명
    nets: dict = field(default_factory=dict)  # 핀-넷 매핑
    pins: list = field(default_factory=list)  # 핀 목록 [{name, number, type}]
    # v1.3 BOM 고도화 필드
    mpn: str = ""                     # Manufacturer Part Number
    dnp: bool = False                 # Do Not Populate

    @property
    def footprint_full(self) -> str:
        """풋프린트 전체 경로 (LibName:FootprintName).

        우선순위:
        1. footprint_override가 있으면 사용
           - 콜론이 없고 footprint_lib가 있으면 lib:footprint 형식으로 보정
        2. footprint_lib + footprint_name 조합
        """
        # 1. override가 있으면 우선 사용
        if self.footprint_override:
            # 콜론이 있으면 그대로 사용
            if ":" in self.footprint_override:
                return self.footprint_override
            # 콜론이 없고 footprint_lib가 있으면 lib:override 형식
            if self.footprint_lib:
                lib_name = self.footprint_lib.stem
                return f"{lib_name}:{self.footprint_override}"
            # 그 외에는 그대로 반환
            return self.footprint_override

        # 2. 기본 로직
        if self.footprint_lib and self.footprint_name:
            lib_name = self.footprint_lib.stem
            return f"{lib_name}:{self.footprint_name}"
        return ""


# 내부 역할 → 기본 심볼 매핑 테이블
ROLE_MAPPING = {
    # ============================================================
    # 전원 IC - DC-DC 컨버터
    # ============================================================
    "buck_5v": {"symbol": "LM2596S-5", "value": "5V"},
    "buck_3v3": {"symbol": "LM2596S-ADJ", "value": "3.3V"},
    "buck_1v8": {"symbol": "LM2596S-ADJ", "value": "1.8V"},
    "buck_adj": {"symbol": "LM2596S-ADJ", "value": "ADJ"},
    "buck_xl1509": {"symbol": "XL1509-5.0", "value": "5V"},

    # ============================================================
    # 전원 IC - LDO 레귤레이터
    # ============================================================
    "ldo_3v3": {"symbol": "AMS1117-3.3", "value": "3.3V"},
    "ldo_5v": {"symbol": "AMS1117-5.0", "value": "5V"},
    "ldo_1v8": {"symbol": "AMS1117-1.8", "value": "1.8V"},
    "ldo_ap2112": {"symbol": "AP2112K-3.3", "value": "3.3V"},

    # ============================================================
    # 전원 IC - 리니어 레귤레이터
    # ============================================================
    "reg_7805": {"symbol": "LM7805", "value": "5V"},
    "reg_7812": {"symbol": "LM7812", "value": "12V"},
    "reg_317": {"symbol": "LM317", "value": "ADJ"},

    # ============================================================
    # 커넥터 - 전원
    # ============================================================
    "input_conn": {"symbol": "Barrel_Jack", "value": "DC Jack"},
    "barrel_jack": {"symbol": "Barrel_Jack", "value": "DC Jack"},
    "screw_2p": {"symbol": "Screw_Terminal_01x02", "value": "Screw 2P"},
    "screw_3p": {"symbol": "Screw_Terminal_01x03", "value": "Screw 3P"},

    # ============================================================
    # 커넥터 - USB
    # ============================================================
    "usb_a": {"symbol": "USB_A", "value": "USB-A"},
    "usb_c": {"symbol": "USB_C", "value": "USB-C"},

    # ============================================================
    # 커넥터 - 핀헤더
    # ============================================================
    "conn_2p": {"symbol": "Conn_01x02", "value": "2P"},
    "conn_3p": {"symbol": "Conn_01x03", "value": "3P"},
    "conn_4p": {"symbol": "Conn_01x04", "value": "4P"},
    "conn_6p": {"symbol": "Conn_01x06", "value": "6P"},

    # ============================================================
    # 커넥터 - 기타
    # ============================================================
    "rj45": {"symbol": "RJ45_Magjack", "value": "RJ45"},
    "hdmi": {"symbol": "HDMI_A", "value": "HDMI"},

    # ============================================================
    # 인터페이스 IC - USB
    # ============================================================
    "usb_hub": {"symbol": "USB5744", "value": "USB5744"},
    "usb_phy": {"symbol": "USB3320", "value": "USB3320"},

    # ============================================================
    # 인터페이스 IC - UART/USB 변환
    # ============================================================
    "usb_uart": {"symbol": "CH340G", "value": "CH340G"},
    "ch340": {"symbol": "CH340G", "value": "CH340G"},
    "cp2102": {"symbol": "CP2102", "value": "CP2102"},
    "ft232": {"symbol": "FT232RL", "value": "FT232RL"},

    # ============================================================
    # 인터페이스 IC - RS232
    # ============================================================
    "rs232": {"symbol": "MAX232", "value": "MAX232"},
    "max232": {"symbol": "MAX232", "value": "MAX232"},

    # ============================================================
    # 인터페이스 IC - CAN
    # ============================================================
    "can_transceiver": {"symbol": "SN65HVD230", "value": "CAN"},
    "can_controller": {"symbol": "MCP2515", "value": "MCP2515"},

    # ============================================================
    # 패시브 소자 - 저항/커패시터
    # ============================================================
    "resistor": {"symbol": "R", "value": "R"},
    "capacitor": {"symbol": "C", "value": "C"},
    "capacitor_pol": {"symbol": "CP", "value": "CP"},
    "inductor": {"symbol": "L", "value": "L"},
    "ferrite": {"symbol": "Ferrite_Bead", "value": "FB"},
    "fuse": {"symbol": "Fuse", "value": "F"},

    # ============================================================
    # 패시브 소자 - 다이오드/LED
    # ============================================================
    "led": {"symbol": "LED", "value": "LED"},
    "diode": {"symbol": "D", "value": "D"},
    "schottky": {"symbol": "D_Schottky", "value": "D"},
    "zener": {"symbol": "Zener", "value": "Zener"},
    "tvs": {"symbol": "TVS", "value": "TVS"},

    # ============================================================
    # 트랜지스터
    # ============================================================
    "nmos": {"symbol": "Q_NMOS_GSD", "value": "NMOS"},
    "pmos": {"symbol": "Q_PMOS_GSD", "value": "PMOS"},
    "nmos_dgs": {"symbol": "Q_NMOS_DGS", "value": "NMOS"},
    "pmos_dgs": {"symbol": "Q_PMOS_DGS", "value": "PMOS"},
    "npn": {"symbol": "Q_NPN_BCE", "value": "NPN"},
    "pnp": {"symbol": "Q_PNP_BCE", "value": "PNP"},

    # ============================================================
    # 연산 증폭기/비교기
    # ============================================================
    "opamp": {"symbol": "Opamp_Generic", "value": "OpAmp"},
    "opamp_dual": {"symbol": "LM358", "value": "LM358"},
    "opamp_quad": {"symbol": "LM324", "value": "LM324"},
    "comparator": {"symbol": "LM393", "value": "LM393"},
    "tl072": {"symbol": "TL072", "value": "TL072"},
    "ne5532": {"symbol": "NE5532", "value": "NE5532"},

    # ============================================================
    # 기타
    # ============================================================
    "crystal": {"symbol": "Crystal", "value": "Crystal"},
    "button": {"symbol": "SW_Push", "value": "SW"},
    "testpoint": {"symbol": "TestPoint", "value": "TP"},
}


class PartResolver:
    """부품 리졸버 - LCSC/내부매핑으로 심볼/풋프린트 획득."""

    def __init__(
        self,
        cache_dir: str = "cache",
        prefer_kicad_lib: bool = False,
        timeout: int = 60,
    ):
        """초기화.

        Args:
            cache_dir: easyeda2kicad 캐시 디렉토리
            prefer_kicad_lib: KiCad 기본 라이브러리 우선 사용 여부
            timeout: easyeda2kicad 타임아웃 (초)
        """
        self.cache_dir = Path(cache_dir)
        self.prefer_kicad_lib = prefer_kicad_lib
        self.timeout = timeout
        self._easyeda2kicad_available = None

    @property
    def easyeda2kicad_available(self) -> bool:
        """easyeda2kicad 사용 가능 여부."""
        if self._easyeda2kicad_available is None:
            self._easyeda2kicad_available = shutil.which("easyeda2kicad") is not None
        return self._easyeda2kicad_available

    def resolve(self, part: PartSpec) -> ResolvedPart:
        """부품 명세를 리졸브합니다.

        Args:
            part: 부품 명세

        Returns:
            리졸브된 부품 정보

        Raises:
            ValueError: 필수 부품 리졸브 실패 시
        """
        logger.info(f"부품 리졸브: {part.ref} (role={part.role}, lcsc={part.lcsc})")

        resolved = ResolvedPart(
            ref=part.ref,
            role=part.role,
            nets=part.nets,
            lcsc=part.lcsc or "",
        )

        # 1순위: LCSC ID가 있으면 easyeda2kicad 시도
        if part.lcsc and self.easyeda2kicad_available:
            try:
                self._resolve_from_lcsc(part.lcsc, resolved)
                logger.info(f"  → LCSC에서 리졸브 성공: {resolved.symbol_name}")
            except Exception as e:
                logger.warning(f"  → LCSC 리졸브 실패: {e}")
                # 실패해도 계속 진행 (내부 매핑으로 폴백)

        # 2순위: 내부 매핑 테이블 (symbol_name이 없을 때만)
        if not resolved.symbol_name and part.role in ROLE_MAPPING:
            mapping = ROLE_MAPPING[part.role]
            resolved.symbol_name = mapping["symbol"]
            if not resolved.value:
                resolved.value = mapping.get("value", "")
            logger.info(f"  → 내부 매핑 사용: {resolved.symbol_name}")

        # 3순위: role 이름을 심볼 이름으로 사용
        if not resolved.symbol_name:
            resolved.symbol_name = part.role
            if not resolved.value:
                resolved.value = part.role
            logger.warning(f"  → 매핑 없음, role을 심볼로 사용: {resolved.symbol_name}")

        # Override 적용: LCSC/내부매핑 결과와 무관하게 part.value, part.footprint 우선
        if part.value:
            resolved.value = part.value
        if part.footprint:
            resolved.footprint_override = part.footprint

        # v1.3: BOM 필드 복사
        if part.mpn:
            resolved.mpn = part.mpn
        if part.manufacturer:
            resolved.manufacturer = part.manufacturer
        if part.description:
            resolved.description = part.description
        resolved.dnp = part.dnp

        # 필수 부품인데 리졸브 실패
        if not part.optional and not resolved.symbol_name:
            raise ValueError(f"필수 부품 리졸브 실패: {part.ref}")

        return resolved

    def resolve_all(self, parts: list[PartSpec]) -> list[ResolvedPart]:
        """여러 부품을 리졸브합니다.

        Args:
            parts: 부품 명세 목록

        Returns:
            리졸브된 부품 목록
        """
        resolved = []
        errors = []

        for part in parts:
            try:
                r = self.resolve(part)
                resolved.append(r)
            except ValueError as e:
                errors.append(str(e))

        if errors:
            raise ValueError(f"부품 리졸브 실패:\n" + "\n".join(errors))

        return resolved

    def _resolve_from_lcsc(self, lcsc_id: str, resolved: ResolvedPart):
        """LCSC ID로 easyeda2kicad를 통해 심볼/풋프린트를 가져옵니다."""
        cache_path = self.cache_dir / lcsc_id
        meta_file = cache_path / "meta.json"

        # 캐시 확인 (무결성 검증 포함)
        if meta_file.exists():
            try:
                if self._validate_cache(cache_path):
                    logger.debug(f"  캐시 사용: {cache_path}")
                    self._load_from_cache(cache_path, resolved)
                    return
            except CacheError as e:
                logger.warning(f"  캐시 손상 감지, 재다운로드: {e}")
                self._cleanup_cache(cache_path)

        # easyeda2kicad 호출
        logger.info(f"  easyeda2kicad 호출: {lcsc_id}")
        cache_path.mkdir(parents=True, exist_ok=True)

        try:
            result = subprocess.run(
                ["easyeda2kicad", "--lcsc_id", lcsc_id, "--output", str(cache_path)],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

            if result.returncode != 0:
                error_msg = result.stderr.strip() or result.stdout.strip()
                self._cleanup_cache(cache_path)

                # 에러 유형 분류
                error_lower = error_msg.lower()
                if "not found" in error_lower or "404" in error_msg:
                    raise EasyEDAError(
                        "부품을 찾을 수 없습니다",
                        lcsc_id=lcsc_id,
                        error_code="LCSC_NOT_FOUND",
                    )
                elif "rate limit" in error_lower or "429" in error_msg:
                    raise NetworkError(
                        "API 호출 제한 초과",
                        lcsc_id=lcsc_id,
                        error_code="RATE_LIMITED",
                    )
                elif "connection" in error_lower or "network" in error_lower:
                    raise NetworkError(
                        "네트워크 연결 실패",
                        lcsc_id=lcsc_id,
                        error_code="NETWORK_ERROR",
                    )
                else:
                    raise EasyEDAError(
                        f"다운로드 실패: {error_msg}",
                        lcsc_id=lcsc_id,
                        error_code="EASYEDA_FAILED",
                    )

            # 생성된 파일 검증
            if not self._validate_easyeda_output(cache_path):
                self._cleanup_cache(cache_path)
                raise EasyEDAError(
                    "다운로드된 파일이 없거나 손상됨",
                    lcsc_id=lcsc_id,
                    error_code="PARSE_ERROR",
                )

            # 파싱
            self._parse_easyeda_output(cache_path, lcsc_id, resolved)

            # 메타 정보 저장 (무결성 해시 포함)
            self._save_cache_meta(meta_file, resolved, cache_path)

        except subprocess.TimeoutExpired:
            self._cleanup_cache(cache_path)
            raise EasyEDAError(
                f"타임아웃 ({self.timeout}초)",
                lcsc_id=lcsc_id,
                error_code="TIMEOUT",
            )
        except FileNotFoundError:
            raise EasyEDAError(
                "easyeda2kicad가 설치되지 않았습니다",
                lcsc_id=lcsc_id,
                error_code="NOT_INSTALLED",
            )

    def _load_from_cache(self, cache_path: Path, resolved: ResolvedPart):
        """캐시에서 부품 정보를 로드합니다."""
        meta_file = cache_path / "meta.json"

        with open(meta_file, 'r') as f:
            meta = json.load(f)

        resolved.symbol_name = meta.get("symbol_name", "")
        resolved.footprint_name = meta.get("footprint_name", "")
        if not resolved.value:
            resolved.value = meta.get("value", "")

        # 심볼/풋프린트 파일 경로
        sym_files = list(cache_path.glob("*.kicad_sym"))
        if sym_files:
            resolved.symbol_lib = sym_files[0]

        fp_files = list(cache_path.glob("*.kicad_mod"))
        if fp_files:
            resolved.footprint_lib = fp_files[0]

        # 핀 정보 파싱
        if resolved.symbol_lib:
            resolved.pins = self._parse_symbol_pins(resolved.symbol_lib)

    def _parse_easyeda_output(self, cache_path: Path, lcsc_id: str, resolved: ResolvedPart):
        """easyeda2kicad 출력 파일을 파싱합니다."""
        # 심볼 파일 찾기
        sym_files = list(cache_path.glob("*.kicad_sym"))
        if sym_files:
            resolved.symbol_lib = sym_files[0]
            # 심볼 이름 추출
            resolved.symbol_name = self._extract_symbol_name(sym_files[0])
            resolved.pins = self._parse_symbol_pins(sym_files[0])

        # 풋프린트 파일 찾기
        fp_files = list(cache_path.glob("*.kicad_mod"))
        if fp_files:
            resolved.footprint_lib = fp_files[0]
            resolved.footprint_name = fp_files[0].stem

        # 값 설정
        if not resolved.value:
            resolved.value = resolved.symbol_name or lcsc_id

    def _extract_symbol_name(self, sym_file: Path) -> str:
        """심볼 파일에서 심볼 이름을 추출합니다."""
        content = sym_file.read_text(encoding='utf-8')
        # (symbol "NAME" ... ) 패턴 찾기
        match = re.search(r'\(symbol\s+"([^"]+)"', content)
        if match:
            return match.group(1)
        return sym_file.stem

    def _parse_symbol_pins(self, sym_file: Path) -> list[dict]:
        """심볼 파일에서 핀 정보를 추출합니다."""
        pins = []

        try:
            content = sym_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                content = sym_file.read_text(encoding='latin-1')
                logger.warning(f"심볼 파일 인코딩 문제 (latin-1 사용): {sym_file}")
            except Exception as e:
                logger.error(f"심볼 파일 읽기 실패: {sym_file}: {e}")
                return []

        try:
            # (pin TYPE STYLE (at X Y ANGLE) (length LEN) (name "NAME" ...) (number "NUM" ...))
            pin_pattern = re.compile(
                r'\(pin\s+(\w+)\s+\w+\s+'
                r'.*?\(name\s+"([^"]+)".*?\)\s*'
                r'\(number\s+"([^"]+)".*?\)',
                re.DOTALL
            )

            for match in pin_pattern.finditer(content):
                pins.append({
                    "type": match.group(1),
                    "name": match.group(2),
                    "number": match.group(3),
                })
        except re.error as e:
            logger.error(f"핀 파싱 정규식 에러: {e}")
            return []

        if not pins:
            logger.warning(f"핀 정보를 찾을 수 없음: {sym_file}")

        return pins

    # ========== 캐시 관리 함수 (v1.4) ==========

    def _compute_file_hash(self, file_path: Path) -> str:
        """파일의 SHA256 해시를 계산합니다."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def _validate_cache(self, cache_path: Path) -> bool:
        """캐시 무결성을 검증합니다.

        Args:
            cache_path: 캐시 디렉토리 경로

        Returns:
            True if valid

        Raises:
            CacheError: 캐시 손상 시
        """
        meta_file = cache_path / "meta.json"

        try:
            with open(meta_file, 'r', encoding='utf-8') as f:
                meta = json.load(f)
        except json.JSONDecodeError as e:
            raise CacheError(f"메타 파일 손상: {e}", cache_path=str(cache_path))
        except IOError as e:
            raise CacheError(f"메타 파일 읽기 실패: {e}", cache_path=str(cache_path))

        # 필수 필드 확인
        if "symbol_name" not in meta:
            raise CacheError("메타 파일에 symbol_name 없음", cache_path=str(cache_path))

        # 파일 해시 검증 (v2 이상 메타만)
        if meta.get("version", 1) >= CACHE_META_VERSION and "files" in meta:
            for filename, expected_hash in meta["files"].items():
                file_path = cache_path / filename
                if not file_path.exists():
                    raise CacheError(f"캐시 파일 누락: {filename}", cache_path=str(cache_path))

                actual_hash = self._compute_file_hash(file_path)
                if actual_hash != expected_hash:
                    raise CacheError(f"캐시 파일 손상: {filename}", cache_path=str(cache_path))

        return True

    def _validate_easyeda_output(self, cache_path: Path) -> bool:
        """easyeda2kicad 출력 파일이 유효한지 검증합니다.

        Args:
            cache_path: 캐시 디렉토리 경로

        Returns:
            True if valid output exists
        """
        sym_files = list(cache_path.glob("*.kicad_sym"))
        if not sym_files:
            return False

        # 심볼 파일이 비어있지 않은지 확인
        for sym_file in sym_files:
            if sym_file.stat().st_size < 100:  # 최소 크기 체크
                return False

        return True

    def _save_cache_meta(self, meta_file: Path, resolved: ResolvedPart, cache_path: Path):
        """캐시 메타 정보를 저장합니다 (무결성 해시 포함)."""
        meta = {
            "version": CACHE_META_VERSION,
            "lcsc": resolved.lcsc,
            "symbol_name": resolved.symbol_name,
            "footprint_name": resolved.footprint_name,
            "value": resolved.value,
            "created_at": datetime.now().isoformat(),
            "files": {},
        }

        # 파일별 해시 저장
        for f in cache_path.glob("*.kicad_*"):
            meta["files"][f.name] = self._compute_file_hash(f)

        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

    def _cleanup_cache(self, cache_path: Path):
        """손상된 캐시를 정리합니다."""
        if cache_path.exists():
            logger.warning(f"캐시 삭제: {cache_path}")
            shutil.rmtree(cache_path, ignore_errors=True)
