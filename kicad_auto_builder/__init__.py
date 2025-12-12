"""
KiCad Auto Builder - LCSC/JLC 연동 자동 회로도 생성기

YAML 설정 파일 하나로:
- LCSC 부품 검색 → 심볼/풋프린트 자동 확보
- .kicad_sym / .kicad_mod 라이브러리 생성
- .kicad_sch 회로도 자동 생성
- BOM CSV 생성

Usage:
    python -m kicad_auto_builder.cli build power_board.yaml
    python -m kicad_auto_builder.cli validate power_board.yaml
"""

__version__ = "1.3.0"

from .config_loader import load_config, ProjectConfig, PartSpec
from .part_resolver import PartResolver, ResolvedPart
from .kicad_builder import KicadBuilder

__all__ = [
    "__version__",
    "load_config",
    "ProjectConfig",
    "PartSpec",
    "PartResolver",
    "ResolvedPart",
    "KicadBuilder",
]
