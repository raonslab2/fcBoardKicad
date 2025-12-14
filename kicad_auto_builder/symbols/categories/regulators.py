"""
Regulator Symbols - 전압 레귤레이터 심볼

LDO, DC-DC 컨버터 등 전압 레귤레이터 심볼
"""

from ..base import SymbolCategory

# 레귤레이터 심볼 정의 (KiCad 8 포맷)
REGULATOR_SYMBOLS = {
    "LM2596S-5": '''(symbol "LM2596S-5"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-5" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM2596S-5_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM2596S-5_1_1"
        (pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM2596S-ADJ": '''(symbol "LM2596S-ADJ"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-ADJ" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM2596S-ADJ_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM2596S-ADJ_1_1"
        (pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)''',

    "AMS1117-3.3": '''(symbol "AMS1117-3.3"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-3.3" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "AMS1117-3.3_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "AMS1117-3.3_1_1"
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "AMS1117-5.0": '''(symbol "AMS1117-5.0"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-5.0" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "AMS1117-5.0_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "AMS1117-5.0_1_1"
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "AMS1117-1.8": '''(symbol "AMS1117-1.8"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-1.8" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "AMS1117-1.8_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "AMS1117-1.8_1_1"
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM7805": '''(symbol "LM7805"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM7805" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM7805_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM7805_1_1"
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM7812": '''(symbol "LM7812"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM7812" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM7812_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM7812_1_1"
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LM317": '''(symbol "LM317"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM317" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM317_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM317_1_1"
        (pin input line (at 0 -7.62 90) (length 2.54) (name "ADJ" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 0 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "AP2112K-3.3": '''(symbol "AP2112K-3.3"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AP2112K-3.3" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "AP2112K-3.3_0_1"
        (rectangle (start -6.35 3.81) (end 6.35 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "AP2112K-3.3_1_1"
        (pin power_in line (at -8.89 1.27 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -6.35 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -8.89 -1.27 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 8.89 -1.27 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 8.89 1.27 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)''',

    "XL1509-5.0": '''(symbol "XL1509-5.0"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Value" "XL1509-5.0" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOP-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "XL1509-5.0_0_1"
        (rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "XL1509-5.0_1_1"
        (pin power_in line (at -10.16 3.81 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -1.27 0) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 1.27 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 3.81 180) (length 2.54) (name "SW" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 1.27 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 -1.27 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 -3.81 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',
}


def register_symbols(registry):
    """레귤레이터 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in REGULATOR_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.REGULATOR,
            reference_prefix="U",
        )
