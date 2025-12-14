"""
Symbol Base - 심볼 정의 데이터클래스

심볼 메타데이터와 핀 정보를 정의합니다.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class SymbolCategory(Enum):
    """심볼 카테고리."""
    PASSIVE = "passive"
    POWER = "power"
    REGULATOR = "regulator"
    CONNECTOR = "connector"
    INTERFACE = "interface"
    DIODE = "diode"
    TRANSISTOR = "transistor"
    OPAMP = "opamp"
    MCU = "mcu"
    SWITCH = "switch"
    MISC = "misc"


class PinType(Enum):
    """KiCad 핀 타입."""
    INPUT = "input"
    OUTPUT = "output"
    BIDIRECTIONAL = "bidirectional"
    PASSIVE = "passive"
    POWER_IN = "power_in"
    POWER_OUT = "power_out"
    OPEN_COLLECTOR = "open_collector"
    OPEN_EMITTER = "open_emitter"
    NO_CONNECT = "no_connect"
    UNSPECIFIED = "unspecified"


@dataclass
class PinDefinition:
    """핀 정의."""
    number: str               # 핀 번호
    name: str                 # 핀 이름
    pin_type: str = "passive" # 핀 타입 (input, output, passive, power_in, etc.)
    x: float = 0              # 핀 X 위치 (심볼 기준)
    y: float = 0              # 핀 Y 위치
    length: float = 2.54      # 핀 길이
    rotation: int = 0         # 핀 회전 (0, 90, 180, 270)


@dataclass
class SymbolDefinition:
    """심볼 정의 메타데이터."""
    name: str                                    # 심볼 이름 (R, LM2596S-5 등)
    category: SymbolCategory                     # 카테고리
    reference_prefix: str                        # Reference 접두사 (R, C, U, J 등)
    kicad_symbol: str                            # KiCad 심볼 정의 문자열
    description: str = ""                        # 설명
    pins: list[PinDefinition] = field(default_factory=list)  # 핀 목록
    default_footprint: str = ""                  # 기본 footprint 힌트
    keywords: list[str] = field(default_factory=list)        # 검색 키워드
    datasheet_url: str = ""                      # 데이터시트 링크
    value: str = ""                              # 기본값

    def get_pin_names(self) -> list[str]:
        """핀 이름 목록 반환."""
        return [p.name for p in self.pins]

    def get_pin_by_name(self, name: str) -> Optional[PinDefinition]:
        """이름으로 핀 찾기."""
        for pin in self.pins:
            if pin.name == name:
                return pin
        return None

    def get_pin_by_number(self, number: str) -> Optional[PinDefinition]:
        """번호로 핀 찾기."""
        for pin in self.pins:
            if pin.number == number:
                return pin
        return None
