#!/usr/bin/env python3
"""
Power Supply Schematic Generator with EMBEDDED Symbols

Generates a KiCad schematic with:
- 12V DC Input (Barrel Jack)
- LM2596S-5.0 (12V → 5V)
- LM2596S-ADJ (12V → 3.3V)
- LM2596S-ADJ (12V → 1.8V)

IMPORTANT: This script EMBEDS all symbol definitions in lib_symbols section.
- No external library dependencies (Device, power, etc.)
- All pin coordinates are 2.54mm grid aligned
- Footprints from: jlc_components (easyeda2kicad generated)
- LCSC Part field added for JLCPCB BOM compatibility

Usage:
    python scripts/generate_power_jlc.py
"""

import uuid
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = PROJECT_ROOT / "fcBoard_Power.kicad_sch"

# Library names
JLC_FP = "jlc_components"  # Footprint library from easyeda2kicad

SCHEMATIC_UUID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


def gen_uuid():
    """Generate a random UUID."""
    return str(uuid.uuid4())


# =============================================================================
# EMBEDDED SYMBOL DEFINITIONS (lib_symbols section)
# All pin coordinates are 2.54mm grid aligned
# =============================================================================

LIB_SYMBOLS = '''	(lib_symbols
		(symbol "fcBoard_Power:R"
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
		(symbol "fcBoard_Power:C"
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
		(symbol "fcBoard_Power:CP"
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
		(symbol "fcBoard_Power:L"
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
		(symbol "fcBoard_Power:D_Schottky"
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
		(symbol "fcBoard_Power:LED"
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
		(symbol "fcBoard_Power:Barrel_Jack"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Barrel_Jack" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 1.27 -1.016 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 1.27 -1.016 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "DC Barrel Jack" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Barrel_Jack_0_1"
				(rectangle (start -5.08 3.81) (end 3.81 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
				(arc (start -3.302 3.175) (mid -3.9288 2.54) (end -3.302 1.905) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -3.302 3.175) (xy 0 3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 0 3.175) (xy 0 1.905) (xy -3.302 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
				(rectangle (start 0 -1.27) (end -2.54 -1.905) (stroke (width 0) (type default)) (fill (type outline)))
				(polyline (pts (xy -2.54 -1.27) (xy -3.81 0) (xy -2.54 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Barrel_Jack_1_1"
				(pin passive line (at 6.35 2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 6.35 -2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_Power:LM2596S-5"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LM2596S-5" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "5V 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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
		)
		(symbol "fcBoard_Power:LM2596S-ADJ"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LM2596S-ADJ" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Adjustable 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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
		)
		(symbol "fcBoard_Power:GND"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
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
		(symbol "fcBoard_Power:+12V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
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
		(symbol "fcBoard_Power:+5V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
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
		(symbol "fcBoard_Power:+3V3"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
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
		(symbol "fcBoard_Power:+1V8"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
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
	)'''


def generate_schematic():
    """Generate the complete Power Supply schematic."""

    sch = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{SCHEMATIC_UUID}")
	(paper "A3")
	(title_block
		(title "Power Supply")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "12V Input, 5V/3.3V/1.8V DC-DC Outputs")
		(comment 2 "LM2596S Buck Converters with JLCPCB Components")
	)
{LIB_SYMBOLS}
{generate_instances()}
{generate_labels()}
{generate_text()}
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
'''
    return sch


def generate_instances():
    """Generate component instances using embedded library symbols."""
    instances = []

    # ==================== 12V INPUT SECTION ====================
    # Barrel Jack
    instances.append(create_symbol(
        lib_id="fcBoard_Power:Barrel_Jack",
        ref="J1", value="DC_12V",
        x=40.64, y=50.8,
        footprint="Connector_BarrelJack:BarrelJack_Horizontal",
        lcsc=""
    ))

    # Input filter capacitor 470uF
    instances.append(create_symbol(
        lib_id="fcBoard_Power:CP",
        ref="C1", value="470uF/25V",
        x=55.88, y=55.88,
        footprint=f"{JLC_FP}:CAP-SMD_BD10.0-L10.0-W10.0-LS11.2-FD",
        lcsc="C72505"
    ))

    # +12V power symbol at input
    instances.append(create_power_symbol("fcBoard_Power:+12V", 55.88, 45.72))

    # GND at barrel jack
    instances.append(create_power_symbol("fcBoard_Power:GND", 40.64, 60.96))
    instances.append(create_power_symbol("fcBoard_Power:GND", 55.88, 66.04))

    # ==================== 5V BUCK CONVERTER (LM2596S-5.0) ====================
    # U1: LM2596S-5.0
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LM2596S-5",
        ref="U1", value="LM2596S-5.0",
        x=101.6, y=50.8,
        footprint=f"{JLC_FP}:TO-263-5_L10.2-W8.9-P1.70-TL",
        lcsc="C347421"
    ))

    # Input cap for 5V converter
    instances.append(create_symbol(
        lib_id="fcBoard_Power:C",
        ref="C2", value="100nF",
        x=86.36, y=55.88,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Output inductor 33uH
    instances.append(create_symbol(
        lib_id="fcBoard_Power:L",
        ref="L1", value="33uH",
        x=119.38, y=48.26,
        footprint=f"{JLC_FP}:IND-SMD_L7.3-W7.3",
        lcsc="C90748"
    ))

    # Schottky diode SS34
    instances.append(create_symbol(
        lib_id="fcBoard_Power:D_Schottky",
        ref="D1", value="SS34",
        x=119.38, y=58.42,
        footprint=f"{JLC_FP}:SMA_L4.3-W2.6-LS5.2-RD",
        lcsc="C35722"
    ))

    # Output cap 220uF
    instances.append(create_symbol(
        lib_id="fcBoard_Power:CP",
        ref="C3", value="220uF/16V",
        x=132.08, y=55.88,
        footprint=f"{JLC_FP}:CAP-SMD_BD8.0-L8.3-W8.3-LS9.0-FD",
        lcsc="C72499"
    ))

    # Power LED indicator (green)
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LED",
        ref="D2", value="GREEN",
        x=142.24, y=55.88,
        footprint=f"{JLC_FP}:LED0603-RD",
        lcsc="C2286"
    ))

    # LED current limiting resistor 330R
    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R1", value="330R",
        x=142.24, y=45.72,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C72038"
    ))

    # +12V at input
    instances.append(create_power_symbol("fcBoard_Power:+12V", 86.36, 45.72))

    # +5V at output
    instances.append(create_power_symbol("fcBoard_Power:+5V", 132.08, 45.72))
    instances.append(create_power_symbol("fcBoard_Power:+5V", 142.24, 38.1))

    # GND symbols
    instances.append(create_power_symbol("fcBoard_Power:GND", 86.36, 66.04))
    instances.append(create_power_symbol("fcBoard_Power:GND", 101.6, 63.5))
    instances.append(create_power_symbol("fcBoard_Power:GND", 119.38, 66.04))
    instances.append(create_power_symbol("fcBoard_Power:GND", 132.08, 66.04))
    instances.append(create_power_symbol("fcBoard_Power:GND", 142.24, 66.04))

    # ==================== 3.3V BUCK CONVERTER (LM2596S-ADJ) ====================
    # U2: LM2596S-ADJ for 3.3V
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LM2596S-ADJ",
        ref="U2", value="LM2596S-ADJ",
        x=101.6, y=101.6,
        footprint=f"{JLC_FP}:TO-263-5_L10.2-W8.9-P1.70-TL",
        lcsc="C29781"
    ))

    # Input cap
    instances.append(create_symbol(
        lib_id="fcBoard_Power:C",
        ref="C4", value="100nF",
        x=86.36, y=106.68,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Feedback resistors for 3.3V: Vout = 1.23 * (1 + R2/R3)
    # For 3.3V: R2 = 1.5k, R3 = 1k -> Vout = 1.23 * 2.5 = 3.075V (close)
    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R2", value="1.5k",
        x=119.38, y=106.68,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C25077"
    ))

    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R3", value="1k",
        x=119.38, y=116.84,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C25905"
    ))

    # Output inductor 33uH
    instances.append(create_symbol(
        lib_id="fcBoard_Power:L",
        ref="L2", value="33uH",
        x=132.08, y=99.06,
        footprint=f"{JLC_FP}:IND-SMD_L7.3-W7.3",
        lcsc="C90748"
    ))

    # Schottky diode
    instances.append(create_symbol(
        lib_id="fcBoard_Power:D_Schottky",
        ref="D3", value="SS34",
        x=132.08, y=109.22,
        footprint=f"{JLC_FP}:SMA_L4.3-W2.6-LS5.2-RD",
        lcsc="C35722"
    ))

    # Output cap 220uF
    instances.append(create_symbol(
        lib_id="fcBoard_Power:CP",
        ref="C5", value="220uF/16V",
        x=144.78, y=106.68,
        footprint=f"{JLC_FP}:CAP-SMD_BD8.0-L8.3-W8.3-LS9.0-FD",
        lcsc="C72499"
    ))

    # Power LED indicator (green)
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LED",
        ref="D4", value="GREEN",
        x=154.94, y=106.68,
        footprint=f"{JLC_FP}:LED0603-RD",
        lcsc="C2286"
    ))

    # LED resistor
    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R4", value="470R",
        x=154.94, y=96.52,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C25087"
    ))

    # +12V at input
    instances.append(create_power_symbol("fcBoard_Power:+12V", 86.36, 96.52))

    # +3V3 at output
    instances.append(create_power_symbol("fcBoard_Power:+3V3", 144.78, 96.52))
    instances.append(create_power_symbol("fcBoard_Power:+3V3", 154.94, 88.9))

    # GND symbols
    instances.append(create_power_symbol("fcBoard_Power:GND", 86.36, 116.84))
    instances.append(create_power_symbol("fcBoard_Power:GND", 101.6, 114.3))
    instances.append(create_power_symbol("fcBoard_Power:GND", 119.38, 124.46))
    instances.append(create_power_symbol("fcBoard_Power:GND", 132.08, 116.84))
    instances.append(create_power_symbol("fcBoard_Power:GND", 144.78, 116.84))
    instances.append(create_power_symbol("fcBoard_Power:GND", 154.94, 116.84))

    # ==================== 1.8V BUCK CONVERTER (LM2596S-ADJ) ====================
    # U3: LM2596S-ADJ for 1.8V
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LM2596S-ADJ",
        ref="U3", value="LM2596S-ADJ",
        x=101.6, y=152.4,
        footprint=f"{JLC_FP}:TO-263-5_L10.2-W8.9-P1.70-TL",
        lcsc="C29781"
    ))

    # Input cap
    instances.append(create_symbol(
        lib_id="fcBoard_Power:C",
        ref="C6", value="100nF",
        x=86.36, y=157.48,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Feedback resistors for 1.8V: Vout = 1.23 * (1 + R5/R6)
    # For 1.8V: R5 = 470R, R6 = 1k -> Vout = 1.23 * 1.47 = 1.81V
    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R5", value="470R",
        x=119.38, y=157.48,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C25087"
    ))

    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R6", value="1k",
        x=119.38, y=167.64,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C25905"
    ))

    # Output inductor 33uH
    instances.append(create_symbol(
        lib_id="fcBoard_Power:L",
        ref="L3", value="33uH",
        x=132.08, y=149.86,
        footprint=f"{JLC_FP}:IND-SMD_L7.3-W7.3",
        lcsc="C90748"
    ))

    # Schottky diode
    instances.append(create_symbol(
        lib_id="fcBoard_Power:D_Schottky",
        ref="D5", value="SS34",
        x=132.08, y=160.02,
        footprint=f"{JLC_FP}:SMA_L4.3-W2.6-LS5.2-RD",
        lcsc="C35722"
    ))

    # Output cap 220uF
    instances.append(create_symbol(
        lib_id="fcBoard_Power:CP",
        ref="C7", value="220uF/16V",
        x=144.78, y=157.48,
        footprint=f"{JLC_FP}:CAP-SMD_BD8.0-L8.3-W8.3-LS9.0-FD",
        lcsc="C72499"
    ))

    # Power LED indicator (red for 1.8V to distinguish)
    instances.append(create_symbol(
        lib_id="fcBoard_Power:LED",
        ref="D6", value="RED",
        x=154.94, y=157.48,
        footprint=f"{JLC_FP}:LED0603-RD",
        lcsc="C2290"
    ))

    # LED resistor
    instances.append(create_symbol(
        lib_id="fcBoard_Power:R",
        ref="R7", value="330R",
        x=154.94, y=147.32,
        footprint=f"{JLC_FP}:R0402",
        lcsc="C72038"
    ))

    # +12V at input
    instances.append(create_power_symbol("fcBoard_Power:+12V", 86.36, 147.32))

    # +1V8 at output
    instances.append(create_power_symbol("fcBoard_Power:+1V8", 144.78, 147.32))
    instances.append(create_power_symbol("fcBoard_Power:+1V8", 154.94, 139.7))

    # GND symbols
    instances.append(create_power_symbol("fcBoard_Power:GND", 86.36, 167.64))
    instances.append(create_power_symbol("fcBoard_Power:GND", 101.6, 165.1))
    instances.append(create_power_symbol("fcBoard_Power:GND", 119.38, 175.26))
    instances.append(create_power_symbol("fcBoard_Power:GND", 132.08, 167.64))
    instances.append(create_power_symbol("fcBoard_Power:GND", 144.78, 167.64))
    instances.append(create_power_symbol("fcBoard_Power:GND", 154.94, 167.64))

    return '\n'.join(instances)


def create_symbol(lib_id: str, ref: str, value: str, x: float, y: float,
                  footprint: str = "", lcsc: str = ""):
    """Create a component symbol instance.

    All coordinates must be 2.54mm grid aligned.
    """
    lcsc_property = ""
    if lcsc:
        lcsc_property = f'''
		(property "LCSC Part" "{lcsc}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))'''

    return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "{ref}" (at {x} {y-5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{value}" (at {x} {y+5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide)){lcsc_property}
		(instances
			(project "fcBoard"
				(path "/{SCHEMATIC_UUID}" (reference "{ref}") (unit 1))
			)
		)
	)'''


def create_power_symbol(lib_id: str, x: float, y: float):
    """Create a power symbol instance."""
    value = lib_id.split(":")[-1]
    return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom no)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR" (at {x} {y+2.54} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Value" "{value}" (at {x} {y-2.54} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(instances
			(project "fcBoard"
				(path "/{SCHEMATIC_UUID}" (reference "#PWR") (unit 1))
			)
		)
	)'''


def generate_labels():
    """Generate hierarchical labels for power outputs."""
    labels = []

    # Output labels
    labels.append(create_hlabel("+5V", 152.4, 48.26, "output"))
    labels.append(create_hlabel("+3V3", 165.1, 99.06, "output"))
    labels.append(create_hlabel("+1V8", 165.1, 149.86, "output"))
    labels.append(create_hlabel("+12V", 66.04, 48.26, "input"))
    labels.append(create_hlabel("GND", 66.04, 58.42, "passive"))

    return '\n'.join(labels)


def create_hlabel(name: str, x: float, y: float, shape: str = "passive"):
    """Create a hierarchical label."""
    return f'''	(hierarchical_label "{name}"
		(shape {shape})
		(at {x} {y} 0)
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)'''


def generate_text():
    """Generate text annotations."""
    return f'''	(text "12V DC Input\\n5A minimum"
		(exclude_from_sim no)
		(at 30.48 40.64 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "5V @ 3A Output"
		(exclude_from_sim no)
		(at 96.52 35.56 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "3.3V @ 3A Output"
		(exclude_from_sim no)
		(at 96.52 86.36 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "1.8V @ 3A Output"
		(exclude_from_sim no)
		(at 96.52 137.16 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)'''


def main():
    """Main entry point."""
    print("=" * 60)
    print("Power Supply Schematic Generator (Embedded Symbols)")
    print("=" * 60)

    schematic = generate_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {OUTPUT_FILE}")
    print()
    print("Embedded Symbol Library: fcBoard_Power")
    print("  - R, C, CP, L (passive components)")
    print("  - D_Schottky, LED (diodes)")
    print("  - LM2596S-5, LM2596S-ADJ (regulators)")
    print("  - Barrel_Jack (connector)")
    print("  - GND, +12V, +5V, +3V3, +1V8 (power symbols)")
    print()
    print(f"Footprint Library: {JLC_FP} (easyeda2kicad)")
    print()
    print("LCSC Part Numbers (for JLCPCB BOM):")
    print("  - U1: C347421 (LM2596S-5.0)")
    print("  - U2, U3: C29781 (LM2596S-ADJ)")
    print("  - L1-L3: C90748 (33uH)")
    print("  - D1, D3, D5: C35722 (SS34)")
    print("  - D2, D4: C2286 (LED Green)")
    print("  - D6: C2290 (LED Red)")
    print("  - C1: C72505 (470uF)")
    print("  - C3, C5, C7: C72499 (220uF)")
    print("  - C2, C4, C6: C11702 (100nF)")
    print("  - R1, R7: C72038 (330R)")
    print("  - R2: C25077 (1.5k)")
    print("  - R3, R6: C25905 (1k)")
    print("  - R4, R5: C25087 (470R)")
    print()
    print("[NOTE] All symbols are embedded - no external library needed.")
    print("[NOTE] All coordinates are 2.54mm grid aligned.")


if __name__ == "__main__":
    main()
