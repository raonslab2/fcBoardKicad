"""
Passive Symbols - 패시브 부품 심볼

R, C, L, LED, 다이오드, 크리스탈, 스위치, 테스트포인트 등
"""

from ..base import SymbolCategory

# 패시브 심볼 정의 (KiCad 8 포맷)
PASSIVE_SYMBOLS = {
    "R": '''(symbol "R"
    (pin_numbers hide)
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
    (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "R_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "C": '''(symbol "C"
    (pin_numbers hide)
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
    )
    (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "CP": '''(symbol "CP"
    (pin_numbers hide)
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "CP" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "CP_0_1"
        (rectangle (start -2.286 0.508) (end 2.286 1.016) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 2.286) (xy -0.762 2.286)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 1.778) (xy -1.27 2.794)) (stroke (width 0) (type default)) (fill (type none)))
        (rectangle (start 2.286 -0.508) (end -2.286 -1.016) (stroke (width 0) (type default)) (fill (type outline)))
    )
    (symbol "CP_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "L": '''(symbol "L"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "L" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
    (property "Value" "L" (at 1.905 0 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "L_0_1"
        (arc (start 0 -2.54) (mid 0.6323 -1.905) (end 0 -1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 -1.27) (mid 0.6323 -0.635) (end 0 0) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 0) (mid 0.6323 0.635) (end 0 1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 1.27) (mid 0.6323 1.905) (end 0 2.54) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "L_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "LED": '''(symbol "LED"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "D_Schottky": '''(symbol "D_Schottky"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "D_Schottky_0_1"
        (polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "D_Schottky_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "D": '''(symbol "D"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "D" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "D_0_1"
        (polyline (pts (xy -1.27 1.27) (xy -1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "D_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Zener": '''(symbol "Zener"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Zener" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Zener_0_1"
        (polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27) (xy -0.762 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Zener_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "TVS": '''(symbol "TVS"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TVS" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "TVS_0_1"
        (polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -0.508 1.27) (xy -0.508 -1.27) (xy -1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.508 -1.27) (xy 0.508 1.27) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -0.508 0) (xy 0.508 1.27) (xy 0.508 -1.27) (xy -0.508 0)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "TVS_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Crystal": '''(symbol "Crystal"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Y" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Crystal_0_1"
        (rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 -1.778) (xy -1.778 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.778 -1.778) (xy 1.778 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Crystal_1_1"
        (pin passive line (at -5.08 0 0) (length 3.302) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 3.302) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "SW_Push": '''(symbol "SW_Push"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "SW" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SW_Push" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "SW_Push_0_1"
        (circle (center -2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 1.27) (xy 0 3.048)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 1.27) (xy 2.54 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "SW_Push_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "TestPoint": '''(symbol "TestPoint"
    (pin_numbers hide)
    (pin_names (offset 0.762) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "TP" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TestPoint" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "TestPoint_0_1"
        (circle (center 0 0) (radius 0.762) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "TestPoint_1_1"
        (pin passive line (at 0 -2.54 90) (length 1.778) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Ferrite_Bead": '''(symbol "Ferrite_Bead"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "FB" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Ferrite_Bead" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Ferrite_Bead_0_1"
        (rectangle (start -2.54 1.016) (end 2.54 -1.016) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 -0.508) (xy 2.54 -0.508)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "Ferrite_Bead_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Fuse": '''(symbol "Fuse"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "F" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Fuse" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Fuse_0_1"
        (rectangle (start -2.54 1.016) (end 2.54 -1.016) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 0) (xy 2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "Fuse_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)''',
}

# 레퍼런스 접두사 매핑
REFERENCE_PREFIX = {
    "R": "R",
    "C": "C",
    "CP": "C",
    "L": "L",
    "LED": "D",
    "D_Schottky": "D",
    "D": "D",
    "Zener": "D",
    "TVS": "D",
    "Crystal": "Y",
    "SW_Push": "SW",
    "TestPoint": "TP",
    "Ferrite_Bead": "FB",
    "Fuse": "F",
}


def register_symbols(registry):
    """패시브 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in PASSIVE_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.PASSIVE,
            reference_prefix=REFERENCE_PREFIX.get(name, "U"),
        )
