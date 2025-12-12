"""
Config Loader - YAML/JSON 설정 파일 파서 v1.3

YAML 파일에서 프로젝트 설정과 부품 목록을 로드합니다.
v1.2: sheets 지원 추가 (계층 시트 생성)
v1.3: BOM 고도화, title_block 옵션, ports 확장
"""

import logging
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional, Union

import yaml

logger = logging.getLogger(__name__)


@dataclass
class PartSpec:
    """부품 명세."""
    ref: str                          # Reference designator (U1, R1, etc.)
    role: str                         # 역할 (buck_5v, input_conn, etc.)
    lcsc: Optional[str] = None        # LCSC 부품번호 (C12345)
    value: Optional[str] = None       # 값 (10k, 100nF, etc.)
    footprint: Optional[str] = None   # 대체 풋프린트
    nets: dict = field(default_factory=dict)  # 핀-넷 매핑
    optional: bool = False            # 선택적 부품 여부
    # v1.3 BOM 고도화 필드
    mpn: Optional[str] = None         # Manufacturer Part Number
    manufacturer: Optional[str] = None  # 제조사
    dnp: bool = False                 # Do Not Populate
    description: Optional[str] = None  # 부품 설명


@dataclass
class PortSpec:
    """포트 명세 (v1.3)."""
    name: str                         # 포트 이름
    shape: str = "passive"            # input/output/bidirectional/passive
    side: str = "left"                # left/right (시트 심볼에서 핀 배치 방향)


@dataclass
class SheetSpec:
    """시트 명세 (v1.2)."""
    name: str                         # 시트 이름 (Power, USB, etc.)
    filename: str = ""                # 시트 파일명 (자동 생성)
    parts: list = field(default_factory=list)  # 이 시트의 부품 목록 (PartSpec)
    ports: list = field(default_factory=list)  # 포트 목록 (PortSpec)

    def __post_init__(self):
        if not self.filename:
            self.filename = f"{self.name}.kicad_sch"


@dataclass
class TitleBlockSpec:
    """타이틀 블록 명세 (v1.3)."""
    rev: str = "1.0"                  # 리비전
    company: str = "Auto Generated"   # 회사명
    date: str = "auto"                # "auto" 또는 "YYYY-MM-DD"
    comment1: str = ""                # 코멘트 1
    comment2: str = ""                # 코멘트 2

    def get_date(self) -> str:
        """실제 날짜 문자열 반환."""
        if self.date == "auto":
            return date.today().strftime("%Y-%m-%d")
        return self.date


@dataclass
class ProjectConfig:
    """프로젝트 설정."""
    name: str                         # 프로젝트 이름
    kicad_version: int = 8            # KiCad 버전
    out_dir: str = "out"              # 출력 디렉토리
    net_presets: dict = field(default_factory=dict)  # 네트 프리셋
    parts: list = field(default_factory=list)        # 부품 목록 (PartSpec) - 단일 시트 모드
    sheets: list = field(default_factory=list)       # 시트 목록 (SheetSpec) - v1.2

    # v1.3: 타이틀 블록 옵션
    title_block: TitleBlockSpec = field(default_factory=TitleBlockSpec)

    # 추가 옵션
    cache_dir: str = "cache"          # easyeda2kicad 캐시 디렉토리
    prefer_kicad_lib: bool = False    # KiCad 기본 라이브러리 우선

    @property
    def is_hierarchical(self) -> bool:
        """계층 시트 모드인지 확인."""
        return len(self.sheets) > 0

    @property
    def all_parts(self) -> list:
        """모든 부품 목록 (단일/계층 모드 통합)."""
        if self.is_hierarchical:
            all_p = []
            for sheet in self.sheets:
                all_p.extend(sheet.parts)
            return all_p
        return self.parts

    @property
    def output_path(self) -> Path:
        """출력 디렉토리 경로."""
        return Path(self.out_dir)

    @property
    def lib_path(self) -> Path:
        """라이브러리 출력 경로."""
        return self.output_path / "lib"

    @property
    def schematic_filename(self) -> str:
        """회로도 파일명."""
        return f"{self.name}.kicad_sch"


def parse_ports(ports_data: list) -> list[PortSpec]:
    """포트 목록을 파싱합니다.

    두 형식 모두 지원:
    A) 문자열: ["+5V", "GND"]
    B) 객체: [{"name": "+5V", "shape": "passive", "side": "left"}, ...]

    Args:
        ports_data: 포트 데이터 리스트

    Returns:
        PortSpec 객체 리스트
    """
    ports = []
    for p in ports_data:
        if isinstance(p, str):
            # 문자열 형식 → 기본값으로 PortSpec 생성
            ports.append(PortSpec(name=p))
        elif isinstance(p, dict):
            # 객체 형식
            if not p.get("name"):
                raise ValueError(f"포트에 name이 없습니다: {p}")
            ports.append(PortSpec(
                name=p["name"],
                shape=p.get("shape", "passive"),
                side=p.get("side", "left"),
            ))
        else:
            raise ValueError(f"잘못된 포트 형식: {p}")
    return ports


def load_config(config_path: str | Path) -> ProjectConfig:
    """YAML 설정 파일을 로드합니다.

    Args:
        config_path: 설정 파일 경로

    Returns:
        ProjectConfig 객체

    Raises:
        FileNotFoundError: 파일이 없을 때
        ValueError: 설정이 잘못되었을 때
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {config_path}")

    logger.info(f"설정 파일 로드: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data:
        raise ValueError("설정 파일이 비어있습니다")

    # 프로젝트 설정 파싱
    project_data = data.get('project', {})
    if not project_data.get('name'):
        raise ValueError("project.name은 필수입니다")

    # v1.3: 타이틀 블록 파싱
    title_data = project_data.get('title_block', {})
    title_block = TitleBlockSpec(
        rev=title_data.get('rev', '1.0'),
        company=title_data.get('company', 'Auto Generated'),
        date=title_data.get('date', 'auto'),
        comment1=title_data.get('comment1', ''),
        comment2=title_data.get('comment2', ''),
    )

    # 부품 목록 파싱 헬퍼
    def parse_parts(parts_data: list) -> list[PartSpec]:
        parts = []
        for part_data in parts_data:
            if not part_data.get('ref'):
                raise ValueError(f"부품에 ref가 없습니다: {part_data}")
            if not part_data.get('role'):
                raise ValueError(f"부품에 role이 없습니다: {part_data}")

            part = PartSpec(
                ref=part_data['ref'],
                role=part_data['role'],
                lcsc=part_data.get('lcsc'),
                value=part_data.get('value'),
                footprint=part_data.get('footprint'),
                nets=part_data.get('nets', {}),
                optional=part_data.get('optional', False),
                # v1.3 필드
                mpn=part_data.get('mpn'),
                manufacturer=part_data.get('manufacturer'),
                dnp=part_data.get('dnp', False),
                description=part_data.get('description'),
            )
            parts.append(part)
        return parts

    # 단일 시트 모드: parts 키 사용
    parts = parse_parts(data.get('parts', []))

    # 계층 시트 모드: sheets 키 사용 (v1.2)
    sheets = []
    for sheet_data in data.get('sheets', []):
        if not sheet_data.get('name'):
            raise ValueError(f"시트에 name이 없습니다: {sheet_data}")

        sheet = SheetSpec(
            name=sheet_data['name'],
            filename=sheet_data.get('filename', ''),
            parts=parse_parts(sheet_data.get('parts', [])),
            ports=parse_ports(sheet_data.get('ports', [])),
        )
        sheets.append(sheet)

    # sheets와 parts 동시 사용 검증
    if sheets and parts:
        logger.warning("sheets와 parts가 동시 정의됨. sheets 모드로 동작합니다.")
        parts = []  # sheets 우선

    config = ProjectConfig(
        name=project_data['name'],
        kicad_version=project_data.get('kicad_version', 8),
        out_dir=project_data.get('out_dir', 'out'),
        net_presets=data.get('net_presets', {}),
        parts=parts,
        sheets=sheets,
        title_block=title_block,
        cache_dir=project_data.get('cache_dir', 'cache'),
        prefer_kicad_lib=project_data.get('prefer_kicad_lib', False),
    )

    logger.info(f"프로젝트: {config.name}")
    logger.info(f"부품 수: {len(config.parts)}")

    return config


def validate_config(config: ProjectConfig) -> list[str]:
    """설정 유효성 검사.

    Args:
        config: 검사할 설정

    Returns:
        경고 메시지 목록 (빈 리스트면 정상)
    """
    warnings = []

    # all_parts 사용 (단일/계층 모드 통합)
    all_parts = config.all_parts

    # 중복 reference 체크
    refs = [p.ref for p in all_parts]
    duplicates = set([r for r in refs if refs.count(r) > 1])
    if duplicates:
        warnings.append(f"중복된 reference: {duplicates}")

    # LCSC 없는 부품 체크
    no_lcsc = [p.ref for p in all_parts if not p.lcsc and not p.optional]
    if no_lcsc:
        warnings.append(f"LCSC 번호 없는 필수 부품: {no_lcsc}")

    # nets 비어있는 부품 체크
    no_nets = [p.ref for p in all_parts if not p.nets]
    if no_nets:
        warnings.append(f"nets 정의 없는 부품: {no_nets}")

    # 계층 모드 추가 검증
    if config.is_hierarchical:
        # 시트 이름 중복 체크
        sheet_names = [s.name for s in config.sheets]
        dup_sheets = set([n for n in sheet_names if sheet_names.count(n) > 1])
        if dup_sheets:
            warnings.append(f"중복된 시트 이름: {dup_sheets}")

    return warnings
