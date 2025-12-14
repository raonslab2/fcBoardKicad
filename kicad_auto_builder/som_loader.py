"""
SoM Loader - SoM 커넥터 핀맵 CSV 파싱 및 심볼 생성 모듈

ACU5EV SoM 등 대형 커넥터(120핀)를 위한:
- CSV 핀맵 파싱
- 동적 심볼 생성 (좌우 분할 레이아웃)
"""

import csv
import logging
import re
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def sanitize_signal_name(signal: str) -> str:
    """KiCad netlabel에 안전한 문자열로 정규화합니다.

    Args:
        signal: 원본 신호 이름

    Returns:
        정규화된 신호 이름
    """
    if not signal or signal.strip() == "":
        return "NC"

    # 공백을 언더스코어로
    result = signal.strip().replace(" ", "_")

    # 특수문자 처리: /, \, [], (), +, - 등
    result = result.replace("/", "_")
    result = result.replace("\\", "_")
    result = result.replace("[", "_")
    result = result.replace("]", "_")
    result = result.replace("(", "_")
    result = result.replace(")", "_")
    result = result.replace("+", "P")  # + -> P (Positive)
    result = result.replace("-", "N")  # - -> N (Negative)  단, 단독 - 제외

    # 연속 언더스코어 제거
    result = re.sub(r'_+', '_', result)

    # 앞뒤 언더스코어 제거
    result = result.strip("_")

    # 빈 문자열이면 NC
    if not result:
        return "NC"

    return result


@dataclass
class PinSpec:
    """핀 명세."""
    number: int                        # 핀 번호 (1~120)
    signal: str                        # 신호 이름 (B65_L1_P, GND 등)
    pin_type: str                      # 핀 타입 (I/O, PWR, NC 등)
    bank: str = ""                     # FPGA 뱅크 (BANK65, PS 등)
    fpga_pin: str = ""                 # FPGA 핀 번호 (Y8 등)
    description: str = ""              # 설명
    carrier_use: str = ""              # 캐리어 보드 용도


@dataclass
class SoMConnectorSpec:
    """SoM 커넥터 명세."""
    ref: str                           # Reference (J29, J30 등)
    pins_csv: str                      # CSV 파일 경로
    pins: list = field(default_factory=list)  # PinSpec 리스트


@dataclass
class SoMSpec:
    """SoM 전체 명세."""
    name: str                          # SoM 이름 (ACU5EV)
    connectors: list = field(default_factory=list)  # SoMConnectorSpec 리스트


@dataclass
class PCBSpec:
    """PCB 생성 명세."""
    board_width: float = 150.0         # 보드 너비 (mm)
    board_height: float = 100.0        # 보드 높이 (mm)
    mounting_holes: int = 4            # 마운팅 홀 개수
    connectors: dict = field(default_factory=dict)  # 커넥터별 좌표 {ref: {x, y}}


def load_pinmap_csv(csv_path: str | Path, base_dir: Optional[Path] = None) -> list[PinSpec]:
    """CSV 파일에서 핀맵을 로드합니다.

    Args:
        csv_path: CSV 파일 경로
        base_dir: 기준 디렉토리 (상대 경로 해석용)

    Returns:
        PinSpec 리스트
    """
    path = Path(csv_path)
    if base_dir and not path.is_absolute():
        path = base_dir / path

    if not path.exists():
        raise FileNotFoundError(f"핀맵 CSV 파일을 찾을 수 없습니다: {path}")

    pins = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pin = PinSpec(
                number=int(row.get('Pin', 0)),
                signal=row.get('Signal', ''),
                pin_type=row.get('Type', 'I/O'),
                bank=row.get('Bank', ''),
                fpga_pin=row.get('FPGA_Pin', ''),
                description=row.get('Description', ''),
                carrier_use=row.get('Carrier_Use', ''),
            )
            pins.append(pin)

    logger.info(f"핀맵 로드: {path.name} ({len(pins)}핀)")
    return pins


def _get_kicad_pin_type(pin_type: str) -> str:
    """CSV 핀 타입을 KiCad 핀 타입으로 변환."""
    mapping = {
        'I/O': 'bidirectional',
        'I': 'input',
        'O': 'output',
        'PWR': 'power_in',
        'NC': 'no_connect',
        'GND': 'power_in',
    }
    return mapping.get(pin_type, 'bidirectional')


def generate_connector_symbol(ref: str, pins: list[PinSpec],
                               symbol_name: Optional[str] = None) -> str:
    """대형 커넥터 심볼을 동적 생성합니다.

    120핀을 좌우 60핀씩 분할 배치합니다.

    Args:
        ref: Reference designator (J29 등)
        pins: PinSpec 리스트
        symbol_name: 심볼 이름 (기본: SoM_Connector_{ref})

    Returns:
        KiCad 심볼 S-expression 문자열
    """
    if not symbol_name:
        symbol_name = f"SoM_Connector_{ref}"

    pin_count = len(pins)
    pins_per_side = (pin_count + 1) // 2  # 좌우 분할

    # 심볼 크기 계산
    pin_spacing = 2.54  # mm
    symbol_height = (pins_per_side + 2) * pin_spacing
    symbol_width = 20.0  # 커넥터 본체 너비

    # 핀 위치 계산 (좌측: 1~60, 우측: 61~120)
    pin_lines = []

    for i, pin in enumerate(pins):
        pin_num = pin.number
        # 신호 이름 정규화
        raw_signal = pin.signal if pin.signal else ""
        pin_name = sanitize_signal_name(raw_signal)
        kicad_type = _get_kicad_pin_type(pin.pin_type)

        if i < pins_per_side:
            # 좌측 핀 (왼쪽에서 오른쪽으로)
            x = -symbol_width / 2 - 2.54
            y = symbol_height / 2 - (i + 1) * pin_spacing
            rotation = 0
        else:
            # 우측 핀 (오른쪽에서 왼쪽으로)
            x = symbol_width / 2 + 2.54
            y = symbol_height / 2 - (i - pins_per_side + 1) * pin_spacing
            rotation = 180

        # NC 핀 처리: 고유한 이름 부여
        if pin_name == 'NC' or pin.pin_type == 'NC':
            pin_name = f"NC_{pin_num}"

        # 핀 이름 특수문자 이스케이프 (sanitize 후에도 안전하게)
        escaped_name = pin_name.replace('"', '\\"')

        pin_line = f'''      (pin {kicad_type} line
        (at {x:.2f} {y:.2f} {rotation})
        (length 2.54)
        (name "{escaped_name}"
          (effects (font (size 1.0 1.0)))
        )
        (number "{pin_num}"
          (effects (font (size 1.0 1.0)))
        )
      )'''
        pin_lines.append(pin_line)

    pins_str = "\n".join(pin_lines)

    # 심볼 본체 생성
    symbol = f'''  (symbol "{symbol_name}"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "{ref}"
      (at 0 {symbol_height/2 + 2:.2f} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{symbol_name}"
      (at 0 {-symbol_height/2 - 2:.2f} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" ""
      (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" ""
      (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "{symbol_name}_0_1"
      (rectangle
        (start {-symbol_width/2:.2f} {symbol_height/2:.2f})
        (end {symbol_width/2:.2f} {-symbol_height/2:.2f})
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "{symbol_name}_1_1"
{pins_str}
    )
  )'''

    return symbol


def generate_connector_library(som_spec: SoMSpec, base_dir: Path) -> str:
    """SoM 커넥터 심볼 라이브러리를 생성합니다.

    Args:
        som_spec: SoM 명세
        base_dir: 기준 디렉토리 (CSV 경로 해석용)

    Returns:
        KiCad 심볼 라이브러리 S-expression
    """
    symbols = []

    for conn in som_spec.connectors:
        # CSV에서 핀맵 로드
        pins = load_pinmap_csv(conn.pins_csv, base_dir)
        conn.pins = pins

        # 심볼 생성
        symbol = generate_connector_symbol(conn.ref, pins)
        symbols.append(symbol)

    symbols_str = "\n".join(symbols)

    library = f'''(kicad_symbol_lib
  (version 20231120)
  (generator "kicad_auto_builder")
  (generator_version "1.5")
{symbols_str}
)'''

    return library
