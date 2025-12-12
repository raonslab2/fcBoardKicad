#!/usr/bin/env python3
"""
Peripherals Subsystem Schematic Generator with EMBEDDED Symbols

Generates a KiCad schematic with:
- RS485 Transceivers (2x MAX485)
- User LEDs (4x)
- User Buttons (2x)
- GPIO Headers
- UART (CP2102N USB-UART)

All symbols are embedded in lib_symbols section.
No external library dependencies.

Usage:
    python scripts/generate_peripherals_embedded.py
"""

import uuid
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = PROJECT_ROOT / "fcBoard_Peripherals.kicad_sch"

JLC_FP = "jlc_components"
SCHEMATIC_UUID = "e5f6a7b8-c9d0-1234-ef01-567890123456"


def gen_uuid():
    return str(uuid.uuid4())


# =============================================================================
# EMBEDDED SYMBOL DEFINITIONS
# =============================================================================

LIB_SYMBOLS = '''	(lib_symbols
		(symbol "fcBoard_PERIPH:MAX485"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
			(property "Value" "MAX485" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "RS485 Transceiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "MAX485_0_1"
				(rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "MAX485_1_1"
				(pin output line (at -10.16 2.54 0) (length 2.54) (name "RO" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 0 0) (length 2.54) (name "~{RE}" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 -5.08 0) (length 2.54) (name "DI" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "A" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "B" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_PERIPH:CP2102N"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "CP2102N" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB to UART Bridge" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "CP2102N_0_1"
				(rectangle (start -10.16 11.43) (end 10.16 -11.43) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "CP2102N_1_1"
				(pin power_in line (at -12.7 7.62 0) (length 2.54) (name "VDD" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -12.7 5.08 0) (length 2.54) (name "REGIN" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -12.7 0 0) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -13.97 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin output line (at 12.7 7.62 180) (length 2.54) (name "TXD" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 5.08 180) (length 2.54) (name "RXD" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin output line (at 12.7 0 180) (length 2.54) (name "RTS" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 -2.54 180) (length 2.54) (name "CTS" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 -7.62 180) (length 2.54) (name "~{RST}" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_PERIPH:USB_B_Micro"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_B_Micro" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB Micro-B Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB_B_Micro_0_1"
				(rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB_B_Micro_1_1"
				(pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -5.08 180) (length 2.54) (name "ID" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_PERIPH:LED"
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
			)
			(symbol "LED_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_PERIPH:SW_Push"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "SW" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "SW_Push" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Push Button" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "SW_Push_0_1"
				(circle (center -2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
				(circle (center 2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -2.54 1.27) (xy 2.54 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "SW_Push_1_1"
				(pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_PERIPH:Conn_01x04"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x04" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "4-pin Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Conn_01x04_0_1"
				(rectangle (start -2.54 3.81) (end 2.54 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Conn_01x04_1_1"
				(pin passive line (at -5.08 2.54 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -5.08 0 0) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -5.08 -2.54 0) (length 2.54) (name "3" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -5.08 -5.08 0) (length 2.54) (name "4" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_PERIPH:Conn_02x10"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_02x10" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "2x10 Pin Header" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Conn_02x10_0_1"
				(rectangle (start -5.08 11.43) (end 5.08 -13.97) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Conn_02x10_1_1"
				(pin passive line (at -7.62 10.16 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 10.16 180) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 7.62 0) (length 2.54) (name "3" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 7.62 180) (length 2.54) (name "4" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 5.08 0) (length 2.54) (name "5" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 5.08 180) (length 2.54) (name "6" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 2.54 0) (length 2.54) (name "7" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 2.54 180) (length 2.54) (name "8" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 0 0) (length 2.54) (name "9" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 0 180) (length 2.54) (name "10" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -2.54 0) (length 2.54) (name "11" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -2.54 180) (length 2.54) (name "12" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -5.08 0) (length 2.54) (name "13" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -5.08 180) (length 2.54) (name "14" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -7.62 0) (length 2.54) (name "15" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -7.62 180) (length 2.54) (name "16" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -10.16 0) (length 2.54) (name "17" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -10.16 180) (length 2.54) (name "18" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -12.7 0) (length 2.54) (name "19" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -12.7 180) (length 2.54) (name "20" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_PERIPH:R"
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
		(symbol "fcBoard_PERIPH:C"
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
		(symbol "fcBoard_PERIPH:GND"
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
		(symbol "fcBoard_PERIPH:+3V3"
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
		(symbol "fcBoard_PERIPH:+5V"
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
	)'''


def generate_schematic():
    sch = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{SCHEMATIC_UUID}")
	(paper "A3")
	(title_block
		(title "Peripherals Subsystem")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "RS485, LEDs, Buttons, GPIO, UART")
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

    # ==================== RS485 SECTION ====================
    # RS485 #1
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:MAX485",
        ref="U1", value="MAX485",
        x=76.2, y=50.8,
        footprint="Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        lcsc=""
    ))

    # RS485 #1 Connector
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:Conn_01x04",
        ref="J1", value="RS485_1",
        x=111.76, y=50.8,
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
        lcsc=""
    ))

    # RS485 #2
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:MAX485",
        ref="U2", value="MAX485",
        x=76.2, y=88.9,
        footprint="Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        lcsc=""
    ))

    # RS485 #2 Connector
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:Conn_01x04",
        ref="J2", value="RS485_2",
        x=111.76, y=88.9,
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
        lcsc=""
    ))

    # Power for RS485
    instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 76.2, 38.1))
    instances.append(create_power_symbol("fcBoard_PERIPH:GND", 76.2, 63.5))
    instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 76.2, 76.2))
    instances.append(create_power_symbol("fcBoard_PERIPH:GND", 76.2, 101.6))

    # ==================== USB-UART SECTION ====================
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:CP2102N",
        ref="U3", value="CP2102N",
        x=203.2, y=50.8,
        footprint="Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm",
        lcsc=""
    ))

    # USB Micro-B Connector
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:USB_B_Micro",
        ref="J3", value="USB_UART",
        x=157.48, y=50.8,
        footprint="Connector_USB:USB_Micro-B_Molex_47346-0001",
        lcsc=""
    ))

    # Decoupling
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:C",
        ref="C1", value="100nF",
        x=182.88, y=40.64,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Power for UART
    instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 182.88, 30.48))
    instances.append(create_power_symbol("fcBoard_PERIPH:GND", 203.2, 68.58))
    instances.append(create_power_symbol("fcBoard_PERIPH:GND", 157.48, 63.5))

    # ==================== USER LEDs SECTION ====================
    led_x = 254.0
    for i, y in enumerate([50.8, 60.96, 71.12, 81.28], 1):
        instances.append(create_symbol(
            lib_id="fcBoard_PERIPH:LED",
            ref=f"D{i}", value=f"LED{i}",
            x=led_x, y=y,
            footprint=f"{JLC_FP}:LED0603-RD",
            lcsc="C2286"
        ))
        instances.append(create_symbol(
            lib_id="fcBoard_PERIPH:R",
            ref=f"R{i}", value="330R",
            x=led_x + 15.24, y=y,
            footprint=f"{JLC_FP}:R0402",
            lcsc="C72038"
        ))
        instances.append(create_power_symbol("fcBoard_PERIPH:GND", led_x - 7.62, y))

    instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 274.32, 40.64))

    # ==================== USER BUTTONS SECTION ====================
    for i, y in enumerate([127.0, 139.7], 1):
        instances.append(create_symbol(
            lib_id="fcBoard_PERIPH:SW_Push",
            ref=f"SW{i}", value=f"BTN{i}",
            x=254.0, y=y,
            footprint="Button_Switch_SMD:SW_SPST_TL3342",
            lcsc=""
        ))
        instances.append(create_symbol(
            lib_id="fcBoard_PERIPH:R",
            ref=f"R{i+4}", value="10k",
            x=269.24, y=y - 7.62,
            footprint=f"{JLC_FP}:R0402",
            lcsc=""
        ))
        instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 269.24, y - 15.24))
        instances.append(create_power_symbol("fcBoard_PERIPH:GND", 246.38, y))

    # ==================== GPIO HEADER ====================
    instances.append(create_symbol(
        lib_id="fcBoard_PERIPH:Conn_02x10",
        ref="J4", value="GPIO_HDR",
        x=76.2, y=160.02,
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical",
        lcsc=""
    ))

    instances.append(create_power_symbol("fcBoard_PERIPH:+3V3", 68.58, 142.24))
    instances.append(create_power_symbol("fcBoard_PERIPH:GND", 83.82, 142.24))

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

    # RS485 signals
    rs485_signals = [
        ("RS485_1_TX", 58.42, 48.26), ("RS485_1_RX", 58.42, 53.34),
        ("RS485_1_DE", 58.42, 50.8),
        ("RS485_2_TX", 58.42, 86.36), ("RS485_2_RX", 58.42, 91.44),
        ("RS485_2_DE", 58.42, 88.9),
    ]
    for name, x, y in rs485_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    # UART signals
    uart_signals = [
        ("UART_TX", 223.52, 58.42), ("UART_RX", 223.52, 55.88),
        ("UART_RTS", 223.52, 50.8), ("UART_CTS", 223.52, 48.26),
    ]
    for name, x, y in uart_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    # LED signals
    for i in range(1, 5):
        labels.append(create_hlabel(f"LED{i}", 276.86, 40.64 + (i-1)*10.16, "input"))

    # Button signals
    labels.append(create_hlabel("BTN1", 261.62, 127.0, "output"))
    labels.append(create_hlabel("BTN2", 261.62, 139.7, "output"))

    # GPIO signals
    for i in range(1, 21):
        x = 60.96 if i % 2 == 1 else 91.44
        y = 170.18 - ((i-1) // 2) * 2.54
        labels.append(create_hlabel(f"GPIO{i}", x, y, "bidirectional"))

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
    return f'''	(text "RS485 Transceivers\\n2x Half-Duplex"
		(exclude_from_sim no)
		(at 76.2 30.48 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "USB-UART Bridge\\nCP2102N Debug Port"
		(exclude_from_sim no)
		(at 180.34 25.4 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "User LEDs"
		(exclude_from_sim no)
		(at 254.0 38.1 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "User Buttons"
		(exclude_from_sim no)
		(at 254.0 114.3 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "GPIO Header\\n2x10 Pin"
		(exclude_from_sim no)
		(at 76.2 132.08 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)'''


def main():
    print("=" * 60)
    print("Peripherals Subsystem Schematic Generator (Embedded Symbols)")
    print("=" * 60)

    schematic = generate_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {OUTPUT_FILE}")
    print()
    print("Components:")
    print("  - U1, U2: MAX485 (RS485 Transceivers)")
    print("  - U3: CP2102N (USB-UART Bridge)")
    print("  - J1, J2: RS485 Connectors")
    print("  - J3: USB Micro-B (Debug UART)")
    print("  - J4: GPIO Header (2x10)")
    print("  - D1-D4: User LEDs")
    print("  - SW1, SW2: User Buttons")
    print()
    print("[NOTE] All symbols embedded - no external library needed.")


if __name__ == "__main__":
    main()
