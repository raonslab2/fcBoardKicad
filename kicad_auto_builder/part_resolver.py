"""
Part Resolver - 부품 → 심볼/풋프린트 매핑 v1.1

easyeda2kicad를 통해 LCSC 부품의 심볼/풋프린트를 자동으로 가져옵니다.
footprint_override 지원 추가.
"""

import json
import logging
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .config_loader import PartSpec

logger = logging.getLogger(__name__)


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
    # 전원 IC
    "buck_5v": {"symbol": "LM2596S-5", "value": "5V"},
    "buck_3v3": {"symbol": "LM2596S-ADJ", "value": "3.3V"},
    "buck_1v8": {"symbol": "LM2596S-ADJ", "value": "1.8V"},
    "ldo_3v3": {"symbol": "AMS1117-3.3", "value": "3.3V"},
    "ldo_1v8": {"symbol": "AMS1117-1.8", "value": "1.8V"},

    # 커넥터
    "input_conn": {"symbol": "Barrel_Jack", "value": "DC Jack"},
    "usb_a": {"symbol": "USB_A", "value": "USB-A"},
    "usb_c": {"symbol": "USB_C", "value": "USB-C"},
    "rj45": {"symbol": "RJ45_Magjack", "value": "RJ45"},
    "hdmi": {"symbol": "HDMI_A", "value": "HDMI"},

    # USB IC
    "usb_hub": {"symbol": "USB5744", "value": "USB5744"},
    "usb_phy": {"symbol": "USB3320", "value": "USB3320"},

    # 패시브
    "resistor": {"symbol": "R", "value": "R"},
    "capacitor": {"symbol": "C", "value": "C"},
    "capacitor_pol": {"symbol": "CP", "value": "CP"},
    "inductor": {"symbol": "L", "value": "L"},
    "led": {"symbol": "LED", "value": "LED"},
    "diode": {"symbol": "D_Schottky", "value": "D"},

    # 기타
    "crystal": {"symbol": "Crystal", "value": "Crystal"},
    "button": {"symbol": "SW_Push", "value": "SW"},
    "testpoint": {"symbol": "TestPoint", "value": "TP"},
}


class PartResolver:
    """부품 리졸버 - LCSC/내부매핑으로 심볼/풋프린트 획득."""

    def __init__(self, cache_dir: str = "cache", prefer_kicad_lib: bool = False):
        """초기화.

        Args:
            cache_dir: easyeda2kicad 캐시 디렉토리
            prefer_kicad_lib: KiCad 기본 라이브러리 우선 사용 여부
        """
        self.cache_dir = Path(cache_dir)
        self.prefer_kicad_lib = prefer_kicad_lib
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
        # 캐시 확인
        cache_path = self.cache_dir / lcsc_id
        meta_file = cache_path / "meta.json"

        if meta_file.exists():
            logger.debug(f"  캐시 사용: {cache_path}")
            self._load_from_cache(cache_path, resolved)
            return

        # easyeda2kicad 호출
        logger.info(f"  easyeda2kicad 호출: {lcsc_id}")
        cache_path.mkdir(parents=True, exist_ok=True)

        try:
            result = subprocess.run(
                ["easyeda2kicad", "--lcsc_id", lcsc_id, "--output", str(cache_path)],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode != 0:
                raise RuntimeError(f"easyeda2kicad 실패: {result.stderr}")

            # 생성된 파일 파싱
            self._parse_easyeda_output(cache_path, lcsc_id, resolved)

            # 메타 정보 저장
            meta = {
                "lcsc": lcsc_id,
                "symbol_name": resolved.symbol_name,
                "footprint_name": resolved.footprint_name,
                "value": resolved.value,
            }
            with open(meta_file, 'w') as f:
                json.dump(meta, f)

        except subprocess.TimeoutExpired:
            raise RuntimeError(f"easyeda2kicad 타임아웃: {lcsc_id}")

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
        content = sym_file.read_text(encoding='utf-8')

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

        return pins
