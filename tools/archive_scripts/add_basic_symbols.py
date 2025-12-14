#!/usr/bin/env python3
"""
Add Basic Symbols to fcBoard.kicad_sym Library

Adds R, C, CP, L, LED, D_Schottky, Crystal, Ferrite_Bead, Fuse,
GND, +12V, +5V, +3V3, +1V8, +2V5, VBUS, and connector symbols
to the fcBoard symbol library.

This allows schematic to reference fcBoard:R, fcBoard:GND, etc.
"""

import re
from pathlib import Path

# Basic symbols in KiCad 9.0 format
BASIC_SYMBOLS = '''
(symbol "R"
    (pin_numbers hide)
    (pin_names (offset 0))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
    (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Resistor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "R_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "C"
    (pin_numbers hide)
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Capacitor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
    )
    (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "CP"
    (pin_numbers hide)
    (pin_names (offset 0.254))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "CP" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Polarized Capacitor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "CP_0_1"
        (rectangle (start -2.286 0.508) (end 2.286 1.016) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 2.286) (xy -0.762 2.286)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 1.778) (xy -1.27 2.794)) (stroke (width 0) (type default)) (fill (type none)))
        (rectangle (start 2.286 -0.508) (end -2.286 -1.016) (stroke (width 0) (type default)) (fill (type outline)))
    )
    (symbol "CP_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "L"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "L" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
    (property "Value" "L" (at 1.905 0 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Inductor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "L_0_1"
        (arc (start 0 -2.54) (mid 0.6323 -1.905) (end 0 -1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 -1.27) (mid 0.6323 -0.635) (end 0 0) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 0) (mid 0.6323 0.635) (end 0 1.27) (stroke (width 0) (type default)) (fill (type none)))
        (arc (start 0 1.27) (mid 0.6323 1.905) (end 0 2.54) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "L_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "LED"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "LED" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.048 -1.524) (xy -1.27 -3.302)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 -1.524) (xy 0 -3.302)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 -2.794) (xy -1.27 -3.556) (xy -1.778 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -0.762 -2.794) (xy 0 -3.556) (xy -0.508 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "D_Schottky"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Schottky diode" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "D_Schottky_0_1"
        (polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.905 0.635) (xy -1.905 1.27) (xy -1.27 1.27) (xy -1.27 -1.27) (xy -0.635 -1.27) (xy -0.635 -0.635)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "D_Schottky_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "Crystal"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "Y" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Crystal oscillator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Crystal_0_1"
        (rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 -1.778) (xy -1.778 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.778 -1.778) (xy 1.778 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Crystal_1_1"
        (pin passive line (at -5.08 0 0) (length 3.302) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 3.302) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "Ferrite_Bead"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "FB" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Ferrite_Bead" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Ferrite bead" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Ferrite_Bead_0_1"
        (rectangle (start -2.54 1.016) (end 2.54 -1.016) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 -0.508) (xy 2.54 0.508)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Ferrite_Bead_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "Fuse"
    (pin_numbers hide)
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "F" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Fuse" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Fuse" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Fuse_0_1"
        (rectangle (start -2.54 1.016) (end 2.54 -1.016) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 0) (xy 2.54 0)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Fuse_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "GND"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Power Ground" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "+12V"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+12V" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "+12V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "+12V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "+12V_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "+5V"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "+5V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "+5V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "+5V_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "+3V3"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "+3.3V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "+3V3_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "+3V3_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "+1V8"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "+1.8V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "+1V8_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "+1V8_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "+2V5"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+2V5" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "+2.5V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "+2V5_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "+2V5_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "VBUS"
    (power)
    (pin_numbers hide)
    (pin_names (offset 0) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "VBUS" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB VBUS Power" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "VBUS_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "VBUS_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "Barrel_Jack"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Barrel_Jack" (at 0 -6.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "DC Power Jack" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Barrel_Jack_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
        (arc (start -3.302 3.175) (mid -4.1271 2.54) (end -3.302 1.905) (stroke (width 0.254) (type default)) (fill (type none)))
        (arc (start -3.302 -1.905) (mid -4.1271 -2.54) (end -3.302 -3.175) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 3.175) (xy 0 3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0 3.175) (xy 0 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0 1.905) (xy -3.302 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 -1.905) (xy 2.54 -1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -1.905) (xy 2.54 -3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -3.175) (xy -3.302 -3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
    )
    (symbol "Barrel_Jack_1_1"
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "USB_A"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 0 -8.89 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 2.54 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 2.54 -1.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB Type-A Receptacle" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB_A_0_1"
        (rectangle (start -5.08 7.62) (end 5.08 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB_A_1_1"
        (pin power_out line (at 7.62 5.08 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 2.54 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 7.62 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "SHIELD" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "USB_C"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_C" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB Type-C Receptacle" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB_C_0_1"
        (rectangle (start -5.08 13.97) (end 5.08 -13.97) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB_C_1_1"
        (pin power_out line (at 7.62 12.7 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "A4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 7.62 180) (length 2.54) (name "CC1" (effects (font (size 1.27 1.27)))) (number "A5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 2.54 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "A6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "A7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "SBU1" (effects (font (size 1.27 1.27)))) (number "A8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -5.08 180) (length 2.54) (name "CC2" (effects (font (size 1.27 1.27)))) (number "B5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -7.62 180) (length 2.54) (name "SBU2" (effects (font (size 1.27 1.27)))) (number "B8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 7.62 -12.7 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "A1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -10.16 180) (length 2.54) (name "SHIELD" (effects (font (size 1.27 1.27)))) (number "S1" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "RJ45_Magjack"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RJ45_Magjack" (at 0 -16.51 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "RJ45 with integrated magnetics" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "RJ45_Magjack_0_1"
        (rectangle (start -7.62 15.24) (end 7.62 -15.24) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "RJ45_Magjack_1_1"
        (pin bidirectional line (at 10.16 12.7 180) (length 2.54) (name "TX+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 10.16 180) (length 2.54) (name "TX-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 5.08 180) (length 2.54) (name "RX+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "RX-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -2.54 180) (length 2.54) (name "LED_G+" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -5.08 180) (length 2.54) (name "LED_G-" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -7.62 180) (length 2.54) (name "LED_Y+" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -10.16 180) (length 2.54) (name "LED_Y-" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -12.7 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 7.62 180) (length 2.54) (name "CT" (effects (font (size 1.27 1.27)))) (number "CT" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "HDMI_A"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 26.67 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HDMI_A" (at 0 -26.67 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 2.54 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "HDMI Type-A Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "HDMI_A_0_1"
        (rectangle (start -7.62 25.4) (end 7.62 -25.4) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "HDMI_A_1_1"
        (pin bidirectional line (at 10.16 22.86 180) (length 2.54) (name "D2+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 20.32 180) (length 2.54) (name "D2_SH" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 17.78 180) (length 2.54) (name "D2-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 15.24 180) (length 2.54) (name "D1+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 12.7 180) (length 2.54) (name "D1_SH" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 10.16 180) (length 2.54) (name "D1-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 7.62 180) (length 2.54) (name "D0+" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 5.08 180) (length 2.54) (name "D0_SH" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "D0-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 0 180) (length 2.54) (name "CLK+" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 -2.54 180) (length 2.54) (name "CLK_SH" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "CLK-" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -7.62 180) (length 2.54) (name "CEC" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 -10.16 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -12.7 180) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -15.24 180) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -17.78 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 -20.32 180) (length 2.54) (name "+5V" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -22.86 180) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 -25.4 180) (length 2.54) (name "SHIELD" (effects (font (size 1.27 1.27)))) (number "SH" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "Conn_2x10"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "J" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Conn_2x10" (at 0 -13.97 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "2x10 Pin Header" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "Conn_2x10_0_1"
        (rectangle (start -3.81 12.7) (end 3.81 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "Conn_2x10_1_1"
        (pin passive line (at -6.35 10.16 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 10.16 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 7.62 0) (length 2.54) (name "3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 7.62 180) (length 2.54) (name "4" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 5.08 0) (length 2.54) (name "5" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 5.08 180) (length 2.54) (name "6" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 2.54 0) (length 2.54) (name "7" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 2.54 180) (length 2.54) (name "8" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 0 0) (length 2.54) (name "9" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 0 180) (length 2.54) (name "10" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 -2.54 0) (length 2.54) (name "11" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 -2.54 180) (length 2.54) (name "12" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 -5.08 0) (length 2.54) (name "13" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 -5.08 180) (length 2.54) (name "14" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 -7.62 0) (length 2.54) (name "15" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 -7.62 180) (length 2.54) (name "16" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 -10.16 0) (length 2.54) (name "17" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 -10.16 180) (length 2.54) (name "18" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -6.35 -12.7 0) (length 2.54) (name "19" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 6.35 -12.7 180) (length 2.54) (name "20" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "SW_Push"
    (pin_numbers hide)
    (pin_names (offset 1.016) hide)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "SW" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SW_Push" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Push button switch" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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
)

(symbol "TestPoint"
    (pin_numbers hide)
    (pin_names (offset 0.762) hide)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (property "Reference" "TP" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TestPoint" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Test point" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "TestPoint_0_1"
        (circle (center 0 0) (radius 0.762) (stroke (width 0) (type default)) (fill (type none)))
    )
    (symbol "TestPoint_1_1"
        (pin passive line (at 0 -2.54 90) (length 1.778) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
    )
)
'''


def main():
    """Add basic symbols to fcBoard.kicad_sym library."""
    print("=" * 60)
    print("Adding Basic Symbols to fcBoard.kicad_sym")
    print("=" * 60)

    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    lib_file = project_root / "libraries" / "fcBoard.kicad_sym"

    if not lib_file.exists():
        print(f"[ERROR] Library file not found: {lib_file}")
        return

    # Read current content
    content = lib_file.read_text(encoding='utf-8')

    # Check if symbols already exist
    if '"R"' in content and '"GND"' in content and '"C"' in content:
        print("[INFO] Basic symbols already exist in library")
        return

    # Find the position before the final closing parenthesis
    # The file should end with "\n)\n" or ")\n"
    content = content.rstrip()
    if content.endswith(')'):
        # Insert before the last )
        insert_pos = content.rfind(')')
        new_content = content[:insert_pos] + BASIC_SYMBOLS + "\n)"
    else:
        print("[ERROR] Unexpected file format")
        return

    # Write back
    lib_file.write_text(new_content, encoding='utf-8')

    print(f"[OK] Updated: {lib_file}")
    print()
    print("Added symbols:")
    print("  - Common: R, C, CP, L, LED, D_Schottky, Crystal, Ferrite_Bead, Fuse")
    print("  - Power: GND, +12V, +5V, +3V3, +1V8, +2V5, VBUS")
    print("  - Connectors: Barrel_Jack, USB_A, USB_C, RJ45_Magjack, HDMI_A")
    print("  - Other: Conn_2x10, SW_Push, TestPoint")


if __name__ == "__main__":
    main()
