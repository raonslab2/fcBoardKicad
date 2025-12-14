"""
OpAmp Symbols - 연산 증폭기 심볼

LM358, LM324, LM393 등 연산 증폭기/비교기 심볼
"""

from ..base import SymbolCategory

# 연산 증폭기 심볼 정의 (KiCad 8 포맷)
OPAMP_SYMBOLS = {
    "Opamp_Generic": '''(symbol "Opamp_Generic"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Opamp_Generic" (at 0 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Opamp_Generic_0_1"
        (polyline (pts (xy -5.08 5.08) (xy -5.08 -5.08) (xy 5.08 0) (xy -5.08 5.08)) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -3.81 -1.27) (xy -3.81 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -4.445 1.905) (xy -3.175 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.81 1.27) (xy -3.81 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Opamp_Generic_1_1"
        (pin output line (at 7.62 0 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "V-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "V+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM358": '''(symbol "LM358"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "LM358" (at 0 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM358_0_1"
        (polyline (pts (xy -5.08 5.08) (xy -5.08 -5.08) (xy 5.08 0) (xy -5.08 5.08)) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -3.81 -1.27) (xy -3.81 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -4.445 1.905) (xy -3.175 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.81 1.27) (xy -3.81 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "LM358_1_1"
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN1-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN2+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN2-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM324": '''(symbol "LM324"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 7.62 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "LM324" (at 0 -7.62 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM324_0_1"
        (rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM324_1_1"
        (pin output line (at 10.16 3.81 180) (length 2.54) (name "OUT1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 3.81 0) (length 2.54) (name "IN1-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 1.27 0) (length 2.54) (name "IN1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -1.27 0) (length 2.54) (name "IN2+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -3.81 0) (length 2.54) (name "IN2-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 1.27 180) (length 2.54) (name "OUT2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -1.27 180) (length 2.54) (name "OUT3" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -3.81 0) (length 2.54) (name "IN3-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -1.27 0) (length 2.54) (name "IN3+" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 1.27 0) (length 2.54) (name "IN4+" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 3.81 0) (length 2.54) (name "IN4-" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -3.81 180) (length 2.54) (name "OUT4" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM393": '''(symbol "LM393"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "LM393" (at 0 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM393_0_1"
        (polyline (pts (xy -5.08 5.08) (xy -5.08 -5.08) (xy 5.08 0) (xy -5.08 5.08)) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -3.81 -1.27) (xy -3.81 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -4.445 1.905) (xy -3.175 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.81 1.27) (xy -3.81 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "LM393_1_1"
        (pin open_collector line (at 7.62 0 180) (length 2.54) (name "OUT1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN1-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN2+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN2-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin open_collector line (at 7.62 0 180) (length 2.54) (name "OUT2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',

    "TL072": '''(symbol "TL072"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "TL072" (at 0 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "TL072_0_1"
        (polyline (pts (xy -5.08 5.08) (xy -5.08 -5.08) (xy 5.08 0) (xy -5.08 5.08)) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -3.81 -1.27) (xy -3.81 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -4.445 1.905) (xy -3.175 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.81 1.27) (xy -3.81 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "TL072_1_1"
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN1-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "V-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN2+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN2-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "V+" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',

    "NE5532": '''(symbol "NE5532"
    (pin_names (offset 0.127))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "NE5532" (at 0 -5.08 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "NE5532_0_1"
        (polyline (pts (xy -5.08 5.08) (xy -5.08 -5.08) (xy 5.08 0) (xy -5.08 5.08)) (stroke (width 0.254) (type default)) (fill (type background)))
        (polyline (pts (xy -3.81 -1.27) (xy -3.81 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -4.445 1.905) (xy -3.175 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.81 1.27) (xy -3.81 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "NE5532_1_1"
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN1-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "V-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 2.54 0) (length 2.54) (name "IN2+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 -2.54 0) (length 2.54) (name "IN2-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 7.62 0 180) (length 2.54) (name "OUT2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "V+" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',
}


def register_symbols(registry):
    """연산 증폭기 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in OPAMP_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.OPAMP,
            reference_prefix="U",
        )
