"""
Transistor Symbols - 트랜지스터 심볼

MOSFET, BJT 등 트랜지스터 심볼
"""

from ..base import SymbolCategory

# 트랜지스터 심볼 정의 (KiCad 8 포맷)
TRANSISTOR_SYMBOLS = {
    "Q_NMOS_GSD": '''(symbol "Q_NMOS_GSD"
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_NMOS_GSD" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_NMOS_GSD_0_1"
        (polyline (pts (xy 0.254 0) (xy -2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 1.905) (xy 0.254 -1.905) (xy 0.254 -1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.27) (xy 0.762 -2.286)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 0.508) (xy 0.762 -0.508)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 2.286) (xy 0.762 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 2.54) (xy 2.54 1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -2.54) (xy 2.54 0) (xy 0.762 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.778) (xy 2.54 -1.778) (xy 2.54 1.778) (xy 0.762 1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.016 0) (xy 2.032 0.381) (xy 2.032 -0.381) (xy 1.016 0)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.651 0) (radius 2.794) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_NMOS_GSD_1_1"
        (pin input line (at -5.08 0 0) (length 2.54) (name "G" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Q_PMOS_GSD": '''(symbol "Q_PMOS_GSD"
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_PMOS_GSD" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_PMOS_GSD_0_1"
        (polyline (pts (xy 0.254 0) (xy -2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 1.905) (xy 0.254 -1.905) (xy 0.254 -1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.27) (xy 0.762 -2.286)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 0.508) (xy 0.762 -0.508)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 2.286) (xy 0.762 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -2.54) (xy 2.54 -1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 2.54) (xy 2.54 0) (xy 0.762 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 1.778) (xy 2.54 1.778) (xy 2.54 -1.778) (xy 0.762 -1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.286 0) (xy 1.27 0.381) (xy 1.27 -0.381) (xy 2.286 0)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.651 0) (radius 2.794) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_PMOS_GSD_1_1"
        (pin input line (at -5.08 0 0) (length 2.54) (name "G" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Q_NPN_BCE": '''(symbol "Q_NPN_BCE"
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_NPN_BCE" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_NPN_BCE_0_1"
        (polyline (pts (xy 0.635 0.635) (xy 2.54 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.635 -0.635) (xy 2.54 -2.54) (xy 2.54 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.635 1.905) (xy 0.635 -1.905) (xy 0.635 -1.905)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.778) (xy 1.778 -1.27) (xy 2.286 -2.286) (xy 1.27 -1.778) (xy 1.27 -1.778)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.27 0) (radius 2.8194) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_NPN_BCE_1_1"
        (pin input line (at -5.08 0 0) (length 5.715) (name "B" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "C" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "E" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Q_PNP_BCE": '''(symbol "Q_PNP_BCE"
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_PNP_BCE" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_PNP_BCE_0_1"
        (polyline (pts (xy 0.635 0.635) (xy 2.54 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.635 -0.635) (xy 2.54 -2.54) (xy 2.54 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.635 1.905) (xy 0.635 -1.905) (xy 0.635 -1.905)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy 1.651 0.635) (xy 0.889 1.143) (xy 1.143 1.905) (xy 1.651 0.635) (xy 1.651 0.635)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.27 0) (radius 2.8194) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_PNP_BCE_1_1"
        (pin input line (at -5.08 0 0) (length 5.715) (name "B" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "C" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "E" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Q_NMOS_DGS": '''(symbol "Q_NMOS_DGS"
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_NMOS_DGS" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_NMOS_DGS_0_1"
        (polyline (pts (xy 0.254 0) (xy -2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 1.905) (xy 0.254 -1.905) (xy 0.254 -1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.27) (xy 0.762 -2.286)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 0.508) (xy 0.762 -0.508)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 2.286) (xy 0.762 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 2.54) (xy 2.54 1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -2.54) (xy 2.54 0) (xy 0.762 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.778) (xy 2.54 -1.778) (xy 2.54 1.778) (xy 0.762 1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.016 0) (xy 2.032 0.381) (xy 2.032 -0.381) (xy 1.016 0)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.651 0) (radius 2.794) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_NMOS_DGS_1_1"
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -5.08 0 0) (length 2.54) (name "G" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',

    "Q_PMOS_DGS": '''(symbol "Q_PMOS_DGS"
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Q" (at 5.08 1.905 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "Q_PMOS_DGS" (at 5.08 0 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 5.08 2.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Q_PMOS_DGS_0_1"
        (polyline (pts (xy 0.254 0) (xy -2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 1.905) (xy 0.254 -1.905) (xy 0.254 -1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 -1.27) (xy 0.762 -2.286)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 0.508) (xy 0.762 -0.508)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 2.286) (xy 0.762 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -2.54) (xy 2.54 -1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 2.54) (xy 2.54 0) (xy 0.762 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.762 1.778) (xy 2.54 1.778) (xy 2.54 -1.778) (xy 0.762 -1.778)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.286 0) (xy 1.27 0.381) (xy 1.27 -0.381) (xy 2.286 0)) (stroke (width 0) (type default)) (fill (type outline)))
        (circle (center 1.651 0) (radius 2.794) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Q_PMOS_DGS_1_1"
        (pin passive line (at 2.54 -5.08 90) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -5.08 0 0) (length 2.54) (name "G" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 5.08 270) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
    )
)''',
}


def register_symbols(registry):
    """트랜지스터 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in TRANSISTOR_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.TRANSISTOR,
            reference_prefix="Q",
        )
