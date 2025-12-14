#!/usr/bin/env python3
"""
HDMI Subsystem Schematic Generator with EMBEDDED Symbols

Generates a KiCad schematic with:
- IT6801FN HDMI Input Receiver
- IT66121FN HDMI Output Transmitter
- 2x HDMI Type-A Connectors
- ESD Protection

All symbols are embedded in lib_symbols section.
No external library dependencies.

Usage:
    python scripts/generate_hdmi_embedded.py
"""

import uuid
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = PROJECT_ROOT / "fcBoard_HDMI.kicad_sch"

JLC_FP = "jlc_components"
SCHEMATIC_UUID = "d4e5f6a7-b8c9-0123-def0-456789012345"


def gen_uuid():
    return str(uuid.uuid4())


# =============================================================================
# EMBEDDED SYMBOL DEFINITIONS
# =============================================================================

LIB_SYMBOLS = '''	(lib_symbols
		(symbol "fcBoard_HDMI:IT6801FN"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Value" "IT6801FN" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI 1.4 Receiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "IT6801FN_0_1"
				(rectangle (start -15.24 24.13) (end 15.24 -24.13) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "IT6801FN_1_1"
				(pin power_in line (at -17.78 20.32 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -17.78 17.78 0) (length 2.54) (name "DVDD" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 12.7 0) (length 2.54) (name "HDMI_RX0+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 10.16 0) (length 2.54) (name "HDMI_RX0-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 7.62 0) (length 2.54) (name "HDMI_RX1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 5.08 0) (length 2.54) (name "HDMI_RX1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 2.54 0) (length 2.54) (name "HDMI_RX2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 0 0) (length 2.54) (name "HDMI_RX2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -5.08 0) (length 2.54) (name "HDMI_RX_CLK+" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -7.62 0) (length 2.54) (name "HDMI_RX_CLK-" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -12.7 0) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -17.78 0) (length 2.54) (name "DDC_SCL" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -20.32 0) (length 2.54) (name "DDC_SDA" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -26.67 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 20.32 180) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 17.78 180) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 15.24 180) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 12.7 180) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 7.62 180) (length 2.54) (name "D[23:0]" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -5.08 180) (length 2.54) (name "I2C_SCL" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -7.62 180) (length 2.54) (name "I2C_SDA" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
				(pin input line (at 17.78 -12.7 180) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 -17.78 180) (length 2.54) (name "INT_N" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_HDMI:IT66121FN"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Value" "IT66121FN" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI 1.4 Transmitter" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "IT66121FN_0_1"
				(rectangle (start -15.24 24.13) (end 15.24 -24.13) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "IT66121FN_1_1"
				(pin power_in line (at -17.78 20.32 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -17.78 17.78 0) (length 2.54) (name "DVDD" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 12.7 0) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 10.16 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 7.62 0) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 5.08 0) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 0 0) (length 2.54) (name "D[23:0]" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -7.62 0) (length 2.54) (name "I2C_SCL" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -10.16 0) (length 2.54) (name "I2C_SDA" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -15.24 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin output line (at -17.78 -20.32 0) (length 2.54) (name "INT_N" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -26.67 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 12.7 180) (length 2.54) (name "HDMI_TX0+" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 10.16 180) (length 2.54) (name "HDMI_TX0-" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 7.62 180) (length 2.54) (name "HDMI_TX1+" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 5.08 180) (length 2.54) (name "HDMI_TX1-" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 2.54 180) (length 2.54) (name "HDMI_TX2+" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 0 180) (length 2.54) (name "HDMI_TX2-" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 -5.08 180) (length 2.54) (name "HDMI_TX_CLK+" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin output line (at 17.78 -7.62 180) (length 2.54) (name "HDMI_TX_CLK-" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
				(pin input line (at 17.78 -12.7 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -17.78 180) (length 2.54) (name "DDC_SCL" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -20.32 180) (length 2.54) (name "DDC_SDA" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_HDMI:HDMI_A"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 17.78 0) (effects (font (size 1.27 1.27))))
			(property "Value" "HDMI_A" (at 0 -17.78 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI Type-A Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "HDMI_A_0_1"
				(rectangle (start -7.62 15.24) (end 7.62 -15.24) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "HDMI_A_1_1"
				(pin bidirectional line (at -10.16 12.7 0) (length 2.54) (name "D2+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 10.16 0) (length 2.54) (name "D2_S" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "D2-" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "D1+" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "D1_S" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "D0+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 -5.08 0) (length 2.54) (name "D0_S" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "D0-" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 12.7 180) (length 2.54) (name "CLK+" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 10.16 10.16 180) (length 2.54) (name "CLK_S" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 7.62 180) (length 2.54) (name "CLK-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin no_connect line (at 10.16 5.08 180) (length 2.54) (name "CEC" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin no_connect line (at 10.16 2.54 180) (length 2.54) (name "NC" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 10.16 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin power_out line (at 10.16 -7.62 180) (length 2.54) (name "+5V" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin input line (at 10.16 -10.16 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_HDMI:C"
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
		(symbol "fcBoard_HDMI:R"
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
		(symbol "fcBoard_HDMI:GND"
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
		(symbol "fcBoard_HDMI:+3V3"
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
		(symbol "fcBoard_HDMI:+5V"
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
		(title "HDMI Input/Output Subsystem")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "IT6801FN HDMI Input + IT66121FN HDMI Output")
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

    # ==================== HDMI INPUT (IT6801FN) ====================
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:IT6801FN",
        ref="U1", value="IT6801FN",
        x=101.6, y=76.2,
        footprint="Package_QFP:LQFP-64_10x10mm_P0.5mm",
        lcsc=""
    ))

    # HDMI Input Connector
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:HDMI_A",
        ref="J1", value="HDMI_IN",
        x=40.64, y=76.2,
        footprint="Connector_HDMI:HDMI-A_Molex_46765-0x01",
        lcsc=""
    ))

    # Decoupling capacitors for IT6801
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:C",
        ref="C1", value="100nF",
        x=76.2, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:C",
        ref="C2", value="100nF",
        x=81.28, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Power symbols for HDMI Input section
    instances.append(create_power_symbol("fcBoard_HDMI:+3V3", 76.2, 50.8))
    instances.append(create_power_symbol("fcBoard_HDMI:+3V3", 81.28, 50.8))
    instances.append(create_power_symbol("fcBoard_HDMI:GND", 101.6, 106.68))
    instances.append(create_power_symbol("fcBoard_HDMI:+5V", 55.88, 63.5))
    instances.append(create_power_symbol("fcBoard_HDMI:GND", 55.88, 96.52))

    # ==================== HDMI OUTPUT (IT66121FN) ====================
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:IT66121FN",
        ref="U2", value="IT66121FN",
        x=203.2, y=76.2,
        footprint="Package_QFP:LQFP-64_10x10mm_P0.5mm",
        lcsc=""
    ))

    # HDMI Output Connector
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:HDMI_A",
        ref="J2", value="HDMI_OUT",
        x=264.16, y=76.2,
        footprint="Connector_HDMI:HDMI-A_Molex_46765-0x01",
        lcsc=""
    ))

    # Decoupling capacitors for IT66121
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:C",
        ref="C3", value="100nF",
        x=177.8, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_HDMI:C",
        ref="C4", value="100nF",
        x=182.88, y=60.96,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # Power symbols for HDMI Output section
    instances.append(create_power_symbol("fcBoard_HDMI:+3V3", 177.8, 50.8))
    instances.append(create_power_symbol("fcBoard_HDMI:+3V3", 182.88, 50.8))
    instances.append(create_power_symbol("fcBoard_HDMI:GND", 203.2, 106.68))
    instances.append(create_power_symbol("fcBoard_HDMI:+5V", 279.4, 63.5))
    instances.append(create_power_symbol("fcBoard_HDMI:GND", 279.4, 96.52))

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

    # HDMI Input (IT6801) to FPGA
    hdmi_in_signals = [
        ("HDMI_RX_PCLK", 127.0, 96.52),
        ("HDMI_RX_DE", 127.0, 93.98),
        ("HDMI_RX_HSYNC", 127.0, 91.44),
        ("HDMI_RX_VSYNC", 127.0, 88.9),
        ("HDMI_RX_D[23:0]", 127.0, 83.82),
        ("HDMI_RX_I2C_SCL", 127.0, 71.12),
        ("HDMI_RX_I2C_SDA", 127.0, 68.58),
        ("HDMI_RX_RESET_N", 127.0, 63.5),
        ("HDMI_RX_INT_N", 127.0, 58.42),
    ]
    for name, x, y in hdmi_in_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    # HDMI Output (IT66121) from FPGA
    hdmi_out_signals = [
        ("HDMI_TX_PCLK", 177.8, 88.9),
        ("HDMI_TX_DE", 177.8, 86.36),
        ("HDMI_TX_HSYNC", 177.8, 83.82),
        ("HDMI_TX_VSYNC", 177.8, 81.28),
        ("HDMI_TX_D[23:0]", 177.8, 76.2),
        ("HDMI_TX_I2C_SCL", 177.8, 68.58),
        ("HDMI_TX_I2C_SDA", 177.8, 66.04),
        ("HDMI_TX_RESET_N", 177.8, 60.96),
        ("HDMI_TX_INT_N", 177.8, 55.88),
    ]
    for name, x, y in hdmi_out_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

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
    return f'''	(text "HDMI Input Receiver\\nIT6801FN - 1080p@60Hz"
		(exclude_from_sim no)
		(at 101.6 40.64 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "HDMI Output Transmitter\\nIT66121FN - 1080p@60Hz"
		(exclude_from_sim no)
		(at 203.2 40.64 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)'''


def main():
    print("=" * 60)
    print("HDMI Subsystem Schematic Generator (Embedded Symbols)")
    print("=" * 60)

    schematic = generate_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {OUTPUT_FILE}")
    print()
    print("Components:")
    print("  - U1: IT6801FN (HDMI 1.4 Receiver)")
    print("  - U2: IT66121FN (HDMI 1.4 Transmitter)")
    print("  - J1: HDMI Type-A Input Connector")
    print("  - J2: HDMI Type-A Output Connector")
    print("  - C1-C4: Decoupling Capacitors")
    print()
    print("[NOTE] All symbols embedded - no external library needed.")


if __name__ == "__main__":
    main()
