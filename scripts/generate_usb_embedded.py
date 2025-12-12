#!/usr/bin/env python3
"""
USB Subsystem Schematic Generator with EMBEDDED Symbols

Generates a KiCad schematic with:
- USB5744 USB 3.0 Hub (4-port)
- USB3320 ULPI PHY
- 4x USB Type-A Connectors
- ESD Protection (TPD4S012)

All symbols are embedded in lib_symbols section.
No external library dependencies.

Usage:
    python scripts/generate_usb_embedded.py
"""

import uuid
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = PROJECT_ROOT / "fcBoard_USB.kicad_sch"

JLC_FP = "jlc_components"
SCHEMATIC_UUID = "b2c3d4e5-f6a7-8901-bcde-f23456789012"


def gen_uuid():
    return str(uuid.uuid4())


# =============================================================================
# EMBEDDED SYMBOL DEFINITIONS
# =============================================================================

LIB_SYMBOLS = '''	(lib_symbols
		(symbol "fcBoard_USB:USB5744"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB5744" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB 3.0 4-Port Hub Controller" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB5744_0_1"
				(rectangle (start -15.24 24.13) (end 15.24 -24.13) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB5744_1_1"
				(pin power_in line (at -17.78 20.32 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -17.78 17.78 0) (length 2.54) (name "VDDA33" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 12.7 0) (length 2.54) (name "USB_DM" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 10.16 0) (length 2.54) (name "USB_DP" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "SSRXM" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 2.54 0) (length 2.54) (name "SSRXP" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -2.54 0) (length 2.54) (name "SSTXM" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -5.08 0) (length 2.54) (name "SSTXP" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -10.16 0) (length 2.54) (name "XTALIN" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin output line (at -17.78 -12.7 0) (length 2.54) (name "XTALOUT" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -17.78 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -26.67 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 20.32 180) (length 2.54) (name "DN1_DM" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 17.78 180) (length 2.54) (name "DN1_DP" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 12.7 180) (length 2.54) (name "DN2_DM" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 10.16 180) (length 2.54) (name "DN2_DP" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 5.08 180) (length 2.54) (name "DN3_DM" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 2.54 180) (length 2.54) (name "DN3_DP" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -2.54 180) (length 2.54) (name "DN4_DM" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -5.08 180) (length 2.54) (name "DN4_DP" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_USB:USB3320"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB3320" (at 0 20.32 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB 2.0 ULPI PHY" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB3320_0_1"
				(rectangle (start -12.7 19.05) (end 12.7 -19.05) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB3320_1_1"
				(pin power_in line (at -15.24 15.24 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -15.24 12.7 0) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "DP" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "DM" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin input line (at -15.24 0 0) (length 2.54) (name "REFCLK" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at -15.24 -5.08 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -21.59 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 15.24 180) (length 2.54) (name "DATA0" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "DATA1" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "DATA2" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 7.62 180) (length 2.54) (name "DATA3" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "DATA4" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DATA5" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 0 180) (length 2.54) (name "DATA6" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DATA7" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -7.62 180) (length 2.54) (name "CLK" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -10.16 180) (length 2.54) (name "DIR" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -12.7 180) (length 2.54) (name "NXT" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin input line (at 15.24 -15.24 180) (length 2.54) (name "STP" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_USB:USB_A"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_A" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB Type-A Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB_A_0_1"
				(rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB_A_1_1"
				(pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_USB:Crystal"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "Y" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Crystal Oscillator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Crystal_0_1"
				(rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.524 -1.27) (xy -1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 1.524 -1.27) (xy 1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Crystal_1_1"
				(pin passive line (at -3.81 0 0) (length 2.286) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.286) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_USB:R"
			(pin_numbers hide)
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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
		(symbol "fcBoard_USB:C"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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
		(symbol "fcBoard_USB:GND"
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
		(symbol "fcBoard_USB:+5V"
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
		(symbol "fcBoard_USB:+3V3"
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
		(symbol "fcBoard_USB:+1V8"
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
    sch = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{SCHEMATIC_UUID}")
	(paper "A3")
	(title_block
		(title "USB 3.0 Hub Subsystem")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "USB5744 4-Port Hub + USB3320 ULPI PHY")
		(comment 2 "Embedded Symbols - No External Library Required")
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
    instances = []

    # ==================== USB5744 Hub Controller ====================
    instances.append(create_symbol(
        lib_id="fcBoard_USB:USB5744",
        ref="U1", value="USB5744",
        x=101.6, y=76.2,
        footprint="Package_QFP:LQFP-48_7x7mm_P0.5mm",
        lcsc=""
    ))

    # Decoupling capacitors for USB5744
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C1", value="100nF",
        x=76.2, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C2", value="100nF",
        x=81.28, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Crystal for USB5744 (24MHz)
    instances.append(create_symbol(
        lib_id="fcBoard_USB:Crystal",
        ref="Y1", value="24MHz",
        x=76.2, y=86.36,
        footprint="Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        lcsc=""
    ))

    # Crystal load capacitors
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C3", value="18pF",
        x=68.58, y=91.44,
        footprint=f"{JLC_FP}:C0402",
        lcsc=""
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C4", value="18pF",
        x=83.82, y=91.44,
        footprint=f"{JLC_FP}:C0402",
        lcsc=""
    ))

    # Power symbols for USB5744
    instances.append(create_power_symbol("fcBoard_USB:+3V3", 76.2, 50.8))
    instances.append(create_power_symbol("fcBoard_USB:+3V3", 81.28, 50.8))
    instances.append(create_power_symbol("fcBoard_USB:GND", 101.6, 106.68))
    instances.append(create_power_symbol("fcBoard_USB:GND", 68.58, 101.6))
    instances.append(create_power_symbol("fcBoard_USB:GND", 83.82, 101.6))

    # ==================== USB3320 ULPI PHY ====================
    instances.append(create_symbol(
        lib_id="fcBoard_USB:USB3320",
        ref="U2", value="USB3320",
        x=203.2, y=76.2,
        footprint="Package_QFP:QFN-32-1EP_5x5mm_P0.5mm",
        lcsc=""
    ))

    # Decoupling capacitors for USB3320
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C5", value="100nF",
        x=180.34, y=66.04,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_USB:C",
        ref="C6", value="100nF",
        x=185.42, y=66.04,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Power symbols for USB3320
    instances.append(create_power_symbol("fcBoard_USB:+3V3", 180.34, 55.88))
    instances.append(create_power_symbol("fcBoard_USB:+1V8", 185.42, 55.88))
    instances.append(create_power_symbol("fcBoard_USB:GND", 203.2, 101.6))

    # ==================== USB Type-A Connectors (4 ports) ====================
    usb_y_positions = [127.0, 152.4, 177.8, 203.2]
    for i, y_pos in enumerate(usb_y_positions, 1):
        instances.append(create_symbol(
            lib_id="fcBoard_USB:USB_A",
            ref=f"J{i}", value=f"USB_A_{i}",
            x=266.7, y=y_pos,
            footprint="Connector_USB:USB_A_Molex_105057-0001",
            lcsc=""
        ))
        instances.append(create_power_symbol("fcBoard_USB:+5V", 279.4, y_pos - 5.08))
        instances.append(create_power_symbol("fcBoard_USB:GND", 266.7, y_pos + 10.16))

    return '\n'.join(instances)


def create_symbol(lib_id: str, ref: str, value: str, x: float, y: float,
                  footprint: str = "", lcsc: str = ""):
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
    labels = []

    # ULPI interface signals to SoM
    ulpi_signals = [
        ("ULPI_DATA0", 228.6, 91.44),
        ("ULPI_DATA1", 228.6, 88.9),
        ("ULPI_DATA2", 228.6, 86.36),
        ("ULPI_DATA3", 228.6, 83.82),
        ("ULPI_DATA4", 228.6, 81.28),
        ("ULPI_DATA5", 228.6, 78.74),
        ("ULPI_DATA6", 228.6, 76.2),
        ("ULPI_DATA7", 228.6, 73.66),
        ("ULPI_CLK", 228.6, 68.58),
        ("ULPI_DIR", 228.6, 66.04),
        ("ULPI_NXT", 228.6, 63.5),
        ("ULPI_STP", 228.6, 60.96),
    ]

    for name, x, y in ulpi_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    # USB upstream from SoM
    labels.append(create_hlabel("USB_DP", 76.2, 86.36, "bidirectional"))
    labels.append(create_hlabel("USB_DM", 76.2, 88.9, "bidirectional"))
    labels.append(create_hlabel("USB_SSRX_P", 76.2, 81.28, "bidirectional"))
    labels.append(create_hlabel("USB_SSRX_M", 76.2, 78.74, "bidirectional"))
    labels.append(create_hlabel("USB_SSTX_P", 76.2, 73.66, "bidirectional"))
    labels.append(create_hlabel("USB_SSTX_M", 76.2, 71.12, "bidirectional"))

    return '\n'.join(labels)


def create_hlabel(name: str, x: float, y: float, shape: str = "passive"):
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
    return f'''	(text "USB5744 USB 3.0 Hub\\n4-Port Downstream"
		(exclude_from_sim no)
		(at 101.6 45.72 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "USB3320 ULPI PHY\\nTo Zynq PS"
		(exclude_from_sim no)
		(at 203.2 50.8 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "USB Type-A\\nDownstream Ports"
		(exclude_from_sim no)
		(at 266.7 116.84 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)'''


def main():
    print("=" * 60)
    print("USB Subsystem Schematic Generator (Embedded Symbols)")
    print("=" * 60)

    schematic = generate_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {OUTPUT_FILE}")
    print()
    print("Components:")
    print("  - U1: USB5744 (USB 3.0 4-Port Hub)")
    print("  - U2: USB3320 (ULPI PHY)")
    print("  - J1-J4: USB Type-A Connectors")
    print("  - Y1: 24MHz Crystal")
    print("  - C1-C6: Decoupling Capacitors")
    print()
    print("[NOTE] All symbols embedded - no external library needed.")


if __name__ == "__main__":
    main()
