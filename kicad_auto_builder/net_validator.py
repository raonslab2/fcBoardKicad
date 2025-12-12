"""
Net Validator - 핀-넷 매칭 검증 v1.1

YAML에서 지정한 nets의 핀 이름이 실제 심볼의 핀과 매칭되는지 검사합니다.
핀 정보 소스: ResolvedPart.pins > 내장 심볼 파싱 > 검증 스킵
"""

import logging
import re
from typing import Optional

from .part_resolver import ResolvedPart
from .templates.symbol import SymbolTemplate, BUILTIN_SYMBOLS

logger = logging.getLogger(__name__)


def parse_pins_from_symbol(symbol_text: str) -> list[dict]:
    """심볼 텍스트에서 핀 정보를 파싱합니다.

    Args:
        symbol_text: KiCad 심볼 정의 텍스트

    Returns:
        [{"name": str, "number": str, "type": str}, ...]
    """
    pins = []

    # KiCad 심볼 핀 형식:
    # (pin TYPE STYLE (at ...) (length ...) (name "NAME" (effects...)) (number "NUM" (effects...)))
    # 중첩 괄호가 있으므로 name/number 값만 추출
    pin_pattern = re.compile(
        r'\(pin\s+(\w+)\s+\w+\s+'   # (pin TYPE STYLE
        r'.*?'                       # 중간 내용 (at, length 등)
        r'\(name\s+"([^"]*)"'        # (name "NAME" - 값만 추출
        r'.*?'                       # effects 등
        r'\(number\s+"([^"]*)"',     # (number "NUM" - 값만 추출
        re.DOTALL
    )

    for match in pin_pattern.finditer(symbol_text):
        pins.append({
            "type": match.group(1),
            "name": match.group(2),
            "number": match.group(3),
        })

    return pins


def get_symbol_pins(part: ResolvedPart) -> tuple[list[dict], str]:
    """부품의 핀 목록을 가져옵니다.

    우선순위:
    1. part.pins (LCSC에서 파싱된 경우)
    2. 내장 심볼에서 regex로 파싱
    3. 빈 리스트

    Returns:
        (pins_list, source_description)
    """
    # 1. ResolvedPart.pins가 있으면 사용
    if part.pins:
        return part.pins, "resolved"

    # 2. 내장 심볼에서 파싱
    builtin_text = SymbolTemplate.get_builtin_symbol(part.symbol_name)
    if builtin_text:
        pins = parse_pins_from_symbol(builtin_text)
        if pins:
            return pins, "builtin"

    # 3. 둘 다 없음
    return [], "none"


def match_pin(pin_key, pins: list[dict]) -> Optional[dict]:
    """핀 키가 핀 목록과 매칭되는지 확인합니다.

    매칭 규칙 (우선순위):
    1. pin_key == pin.name (exact)
    2. pin_key == pin.number (exact)
    3. pin_key.lower() == pin.name.lower() (case-insensitive)

    Args:
        pin_key: YAML에서 지정한 핀 이름 (str 또는 int)
        pins: 심볼의 핀 목록 [{name, number, type}, ...]

    Returns:
        매칭된 핀 정보 또는 None
    """
    if not pins:
        return None

    # YAML에서 숫자로 파싱될 수 있으므로 문자열 변환
    pin_key = str(pin_key)

    # 1. name exact match
    for pin in pins:
        if pin.get("name") == pin_key:
            return pin

    # 2. number exact match
    for pin in pins:
        if pin.get("number") == pin_key:
            return pin

    # 3. name case-insensitive match
    pin_key_lower = pin_key.lower()
    for pin in pins:
        if pin.get("name", "").lower() == pin_key_lower:
            return pin

    return None


def validate_nets(
    resolved_parts: list[ResolvedPart],
    config_parts: list = None
) -> tuple[list[str], list[str]]:
    """모든 부품의 핀-넷 매칭을 검증합니다.

    Args:
        resolved_parts: 리졸브된 부품 목록
        config_parts: 원본 PartSpec 목록 (optional 플래그 확인용)

    Returns:
        (errors, warnings) 튜플
        - errors: 필수 부품의 매칭 실패 메시지 리스트
        - warnings: 선택 부품의 매칭 실패 또는 핀정보 없음 메시지 리스트
    """
    errors = []
    warnings = []

    # optional 플래그 매핑 (ref -> optional)
    optional_map = {}
    if config_parts:
        for p in config_parts:
            optional_map[p.ref] = getattr(p, 'optional', False)

    for part in resolved_parts:
        if not part.nets:
            continue

        is_optional = optional_map.get(part.ref, False)
        pins, source = get_symbol_pins(part)

        # 핀 정보가 없는 경우
        if not pins:
            if part.nets:
                msg = (
                    f"핀정보 없음, 검증 스킵: {part.ref} ({part.role}) "
                    f"symbol={part.symbol_name}"
                )
                warnings.append(msg)
            continue

        # 핀 이름/번호 목록 (에러 메시지용)
        available = []
        for p in pins[:10]:
            name = p.get("name", "")
            number = p.get("number", "")
            if name and name != number:
                available.append(f"{name}({number})")
            else:
                available.append(name or number)
        if len(pins) > 10:
            available.append(f"... (+{len(pins) - 10} more)")

        # 각 net의 pin_key 검증
        for pin_key, net_name in part.nets.items():
            matched = match_pin(pin_key, pins)

            if matched is None:
                msg = (
                    f"Pin mismatch: {part.ref} ({part.role}) "
                    f"symbol={part.symbol_name} pin='{pin_key}' not found. "
                    f"Available: {available}"
                )

                if is_optional:
                    warnings.append(msg)
                else:
                    errors.append(msg)

    return errors, warnings
