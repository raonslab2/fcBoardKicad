"""
KiCad Auto Builder - LCSC/JLC 연동 자동 회로도 생성기 v1.4

YAML 설정 파일 하나로:
- LCSC 부품 검색 → 심볼/풋프린트 자동 확보
- .kicad_sym / .kicad_mod 라이브러리 생성
- .kicad_sch 회로도 자동 생성
- BOM CSV 생성

v1.4 변경사항:
- 안정성 개선: 상세 예외 클래스, YAML 스키마 검증, 캐시 무결성
- 심볼 시스템 리팩토링: 카테고리별 분리, SymbolRegistry 싱글톤
- 새 심볼 추가: LDO, MOSFET, OpAmp, 인터페이스 IC 등
- ROLE_MAPPING 확장: 60+ 역할 지원
- 레이아웃 개선: 기능 그룹별 배치, 전원 심볼 인접 배치

Usage:
    python -m kicad_auto_builder.cli build power_board.yaml
    python -m kicad_auto_builder.cli validate power_board.yaml
"""

__version__ = "1.4.0"

from .config_loader import load_config, ProjectConfig, PartSpec
from .part_resolver import PartResolver, ResolvedPart, ROLE_MAPPING
from .kicad_builder import KicadBuilder
from .exceptions import (
    KicadAutoBuilderError,
    ConfigError,
    ConfigValidationError,
    PartResolveError,
    EasyEDAError,
    NetworkError,
    CacheError,
    SymbolParseError,
    BuildError,
)

__all__ = [
    "__version__",
    # Config
    "load_config",
    "ProjectConfig",
    "PartSpec",
    # Resolver
    "PartResolver",
    "ResolvedPart",
    "ROLE_MAPPING",
    # Builder
    "KicadBuilder",
    # Exceptions
    "KicadAutoBuilderError",
    "ConfigError",
    "ConfigValidationError",
    "PartResolveError",
    "EasyEDAError",
    "NetworkError",
    "CacheError",
    "SymbolParseError",
    "BuildError",
]
