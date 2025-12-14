"""
Connector Symbols - 커넥터 심볼

Barrel_Jack, USB, 핀헤더 등 커넥터 심볼
"""

from ..base import SymbolCategory

# 커넥터 심볼 정의 (KiCad 8 포맷)
CONNECTOR_SYMBOLS = {
    "Barrel_Jack": '''(symbol "Barrel_Jack"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Barrel_Jack" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Barrel_Jack_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
        (arc (start -3.302 3.81) (mid -4.064 3.048) (end -3.302 2.286) (stroke (width 0.254) (type default)) (fill (type none)))
        (arc (start -3.302 -2.286) (mid -4.064 -3.048) (end -3.302 -3.81) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 3.81) (xy 1.778 3.81)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 2.286) (xy -0.762 2.286) (xy -0.762 -2.286) (xy -3.302 -2.286)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 -3.81) (xy 1.778 -3.81)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.778 3.81) (xy 1.778 4.572) (xy 3.048 4.572) (xy 3.048 -4.572) (xy 1.778 -4.572) (xy 1.778 -3.81)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Barrel_Jack_1_1"
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 0 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "USB_A": '''(symbol "USB_A"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 0 -8.89 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 1.27 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 1.27 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB_A_0_1"
        (rectangle (start -5.08 7.62) (end 5.08 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB_A_1_1"
        (pin power_in line (at 7.62 5.08 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 2.54 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 7.62 -2.54 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -5.08 180) (length 2.54) (name "Shield" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)''',

    "USB_C": '''(symbol "USB_C"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_C" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB_C_0_1"
        (rectangle (start -7.62 13.97) (end 7.62 -13.97) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB_C_1_1"
        (pin power_in line (at 10.16 11.43 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "A4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 8.89 180) (length 2.54) (name "CC1" (effects (font (size 1.27 1.27)))) (number "A5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 6.35 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "A6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 3.81 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "A7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 1.27 180) (length 2.54) (name "SBU1" (effects (font (size 1.27 1.27)))) (number "A8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -1.27 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "A1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -3.81 180) (length 2.54) (name "TX1+" (effects (font (size 1.27 1.27)))) (number "A2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -6.35 180) (length 2.54) (name "TX1-" (effects (font (size 1.27 1.27)))) (number "A3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -8.89 180) (length 2.54) (name "RX1+" (effects (font (size 1.27 1.27)))) (number "B11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -11.43 180) (length 2.54) (name "RX1-" (effects (font (size 1.27 1.27)))) (number "B10" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -16.51 90) (length 2.54) (name "Shield" (effects (font (size 1.27 1.27)))) (number "S1" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Conn_01x02": '''(symbol "Conn_01x02"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Conn_01x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Conn_01x02_1_1"
        (rectangle (start -1.27 -2.413) (end 0 -2.667) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 0.127) (end 0 -0.127) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 1.27) (end 1.27 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Conn_01x03": '''(symbol "Conn_01x03"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Conn_01x03" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Conn_01x03_1_1"
        (rectangle (start -1.27 -2.413) (end 0 -2.667) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 0.127) (end 0 -0.127) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 2.667) (end 0 2.413) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 3.81) (end 1.27 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -5.08 2.54 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Conn_01x04": '''(symbol "Conn_01x04"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Conn_01x04" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Conn_01x04_1_1"
        (rectangle (start -1.27 -4.953) (end 0 -5.207) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 -2.413) (end 0 -2.667) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 0.127) (end 0 -0.127) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 2.667) (end 0 2.413) (stroke (width 0.1524) (type default)) (fill (type none)))
        (rectangle (start -1.27 3.81) (end 1.27 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -5.08 2.54 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -5.08 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Conn_01x06": '''(symbol "Conn_01x06"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Conn_01x06" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Conn_01x06_1_1"
        (rectangle (start -1.27 6.35) (end 1.27 -8.89) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -5.08 5.08 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 2.54 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -5.08 0) (length 3.81) (name "Pin_5" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -7.62 0) (length 3.81) (name "Pin_6" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Screw_Terminal_01x02": '''(symbol "Screw_Terminal_01x02"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Screw_Terminal_01x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Screw_Terminal_01x02_1_1"
        (rectangle (start -1.27 1.27) (end 1.27 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
        (circle (center 0 -2.54) (radius 0.635) (stroke (width 0.1524) (type default)) (fill (type none)))
        (circle (center 0 0) (radius 0.635) (stroke (width 0.1524) (type default)) (fill (type none)))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Screw_Terminal_01x03": '''(symbol "Screw_Terminal_01x03"
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Screw_Terminal_01x03" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Screw_Terminal_01x03_1_1"
        (rectangle (start -1.27 3.81) (end 1.27 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
        (circle (center 0 -2.54) (radius 0.635) (stroke (width 0.1524) (type default)) (fill (type none)))
        (circle (center 0 0) (radius 0.635) (stroke (width 0.1524) (type default)) (fill (type none)))
        (circle (center 0 2.54) (radius 0.635) (stroke (width 0.1524) (type default)) (fill (type none)))
        (pin passive line (at -5.08 2.54 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',
}


def register_symbols(registry):
    """커넥터 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in CONNECTOR_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.CONNECTOR,
            reference_prefix="J",
        )
