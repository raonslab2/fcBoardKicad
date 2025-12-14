#!/usr/bin/env python3
"""
Generate USB 3.0 Hub schematic with proper connections
USB5744 → TPD4S012 (ESD) → TPS2041 (Power Switch) → USB_A Connector
"""

import uuid

OUTPUT_FILE = r"D:\git2\fcBoardKicad\fcBoard_USB.kicad_sch"

def gen_uuid():
    return str(uuid.uuid4())

def create_schematic():
    # UUIDs for components
    uuids = {f'uuid_{i}': gen_uuid() for i in range(200)}

    schematic = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "USB 3.0 Hub")
		(date "2024-12-01")
		(rev "0.2")
		(company "fcBoard Project")
		(comment 1 "USB5744 4-Port USB 3.0 Hub + USB3320 ULPI PHY")
		(comment 2 "Signal flow: USB5744 -> TPD4S012 (ESD) -> TPS2041 (Power) -> USB_A")
	)
	(lib_symbols
		(symbol "Interface_USB:USB5744"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U"
				(at 0 31.75 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "USB5744"
				(at 0 29.21 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" "Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm"
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "USB5744_0_1"
				(rectangle (start -15.24 27.94) (end 15.24 -27.94)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "USB5744_1_1"
				(pin power_in line (at -17.78 25.4 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -17.78 20.32 0) (length 2.54) (name "USBUP_DP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -17.78 17.78 0) (length 2.54) (name "USBUP_DM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 25.4 180) (length 2.54) (name "USBDN1_DP" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 22.86 180) (length 2.54) (name "USBDN1_DM" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 17.78 180) (length 2.54) (name "USBDN2_DP" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 15.24 180) (length 2.54) (name "USBDN2_DM" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 10.16 180) (length 2.54) (name "USBDN3_DP" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 7.62 180) (length 2.54) (name "USBDN3_DM" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 2.54 180) (length 2.54) (name "USBDN4_DP" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 0 180) (length 2.54) (name "USBDN4_DM" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -30.48 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "EP" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -5.08 0) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "30" (effects (font (size 1.27 1.27)))))
				(pin output line (at -17.78 -7.62 0) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "31" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -12.7 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "40" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -17.78 -20.32 0) (length 2.54) (name "VBUS_DET" (effects (font (size 1.27 1.27)))) (number "50" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Interface_USB:USB3320"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U"
				(at 0 21.59 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "USB3320"
				(at 0 19.05 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm"
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "USB3320_0_1"
				(rectangle (start -12.7 17.78) (end 12.7 -17.78)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "USB3320_1_1"
				(pin power_in line (at -15.24 15.24 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 10.16 0) (length 2.54) (name "DP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "DM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin output line (at 15.24 15.24 180) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin output line (at 15.24 12.7 180) (length 2.54) (name "DIR" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin output line (at 15.24 10.16 180) (length 2.54) (name "NXT" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
				(pin input line (at 15.24 7.62 180) (length 2.54) (name "STP" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DATA0" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 0 180) (length 2.54) (name "DATA1" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DATA2" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -5.08 180) (length 2.54) (name "DATA3" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -7.62 180) (length 2.54) (name "DATA4" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -10.16 180) (length 2.54) (name "DATA5" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -12.7 180) (length 2.54) (name "DATA6" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -15.24 180) (length 2.54) (name "DATA7" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "EP" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Power_Management:TPS2041B"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U"
				(at 0 8.89 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "TPS2041B"
				(at 0 6.35 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" "Package_TO_SOT_SMD:SOT-23-5"
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "TPS2041B_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "TPS2041B_1_1"
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin open_collector line (at 10.16 -2.54 180) (length 2.54) (name "OC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Power_Protection:TPD4S012"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U"
				(at 0 10.16 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "TPD4S012"
				(at 0 7.62 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm"
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "TPD4S012_0_1"
				(rectangle (start -7.62 6.35) (end 7.62 -6.35)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "TPD4S012_1_1"
				(pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "D1_IN" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "D1_OUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "D2_IN" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "D2_OUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Connector:USB_A"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J"
				(at 0 7.62 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "USB_A"
				(at 0 -7.62 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal"
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "USB_A_0_1"
				(rectangle (start -5.08 5.08) (end 5.08 -5.08)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "USB_A_1_1"
				(pin power_in line (at -7.62 2.54 0) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -7.62 0 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -7.62 -2.54 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -7.62 -5.08 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:Crystal"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "Y"
				(at 0 3.81 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "Crystal"
				(at 0 -3.81 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "Crystal_0_1"
				(rectangle (start -1.27 2.54) (end 1.27 -2.54)
					(stroke (width 0) (type default))
					(fill (type none))
				)
				(polyline (pts (xy -2.54 -2.54) (xy -2.54 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 2.54 -2.54) (xy 2.54 2.54)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "Crystal_1_1"
				(pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:C"
			(pin_numbers (hide yes))
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C"
				(at 0.635 2.54 0)
				(effects (font (size 1.27 1.27)) (justify left))
			)
			(property "Value" "C"
				(at 0.635 -2.54 0)
				(effects (font (size 1.27 1.27)) (justify left))
			)
			(property "Footprint" ""
				(at 0.9652 -3.81 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "C_0_1"
				(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
			)
			(symbol "C_1_1"
				(pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:R"
			(pin_numbers (hide yes))
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R"
				(at 2.032 0 90)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "R"
				(at 0 0 90)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" ""
				(at -1.778 0 90)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "R_0_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54)
					(stroke (width 0.254) (type default))
					(fill (type none))
				)
			)
			(symbol "R_1_1"
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:+3V3"
			(power)
			(pin_numbers (hide yes))
			(pin_names (offset 0) (hide yes))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR"
				(at 0 -3.81 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Value" "+3V3"
				(at 0 3.556 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "+3V3_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+3V3_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:+5V"
			(power)
			(pin_numbers (hide yes))
			(pin_names (offset 0) (hide yes))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR"
				(at 0 -3.81 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Value" "+5V"
				(at 0 3.556 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "+5V_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+5V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:GND"
			(power)
			(pin_numbers (hide yes))
			(pin_names (offset 0) (hide yes))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR"
				(at 0 -6.35 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Value" "GND"
				(at 0 -3.81 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Footprint" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(property "Datasheet" ""
				(at 0 0 0)
				(effects (font (size 1.27 1.27)) (hide yes))
			)
			(symbol "GND_0_1"
				(polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27))
					(stroke (width 0) (type default)) (fill (type none))
				)
			)
			(symbol "GND_1_1"
				(pin power_in line (at 0 0 270) (length 0) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
	)
'''

    # ==================== USB3320 ULPI PHY (Upstream to SoM) ====================
    # Position: Left side of schematic
    usb3320_x, usb3320_y = 60, 80

    schematic += f'''
	(symbol
		(lib_id "Interface_USB:USB3320")
		(at {usb3320_x} {usb3320_y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U1"
			(at {usb3320_x} {usb3320_y - 25} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB3320"
			(at {usb3320_x} {usb3320_y - 23} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm"
			(at {usb3320_x} {usb3320_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb3320_x} {usb3320_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "10" (uuid "{gen_uuid()}"))
		(pin "11" (uuid "{gen_uuid()}"))
		(pin "12" (uuid "{gen_uuid()}"))
		(pin "13" (uuid "{gen_uuid()}"))
		(pin "14" (uuid "{gen_uuid()}"))
		(pin "15" (uuid "{gen_uuid()}"))
		(pin "16" (uuid "{gen_uuid()}"))
		(pin "17" (uuid "{gen_uuid()}"))
		(pin "18" (uuid "{gen_uuid()}"))
		(pin "19" (uuid "{gen_uuid()}"))
		(pin "20" (uuid "{gen_uuid()}"))
		(pin "21" (uuid "{gen_uuid()}"))
		(pin "EP" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "U1")
					(unit 1)
				)
			)
		)
	)
'''

    # ==================== USB5744 Hub IC ====================
    # Position: Center of schematic
    usb5744_x, usb5744_y = 150, 80

    schematic += f'''
	(symbol
		(lib_id "Interface_USB:USB5744")
		(at {usb5744_x} {usb5744_y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U2"
			(at {usb5744_x} {usb5744_y - 35} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB5744"
			(at {usb5744_x} {usb5744_y - 33} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm"
			(at {usb5744_x} {usb5744_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb5744_x} {usb5744_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "10" (uuid "{gen_uuid()}"))
		(pin "11" (uuid "{gen_uuid()}"))
		(pin "14" (uuid "{gen_uuid()}"))
		(pin "15" (uuid "{gen_uuid()}"))
		(pin "18" (uuid "{gen_uuid()}"))
		(pin "19" (uuid "{gen_uuid()}"))
		(pin "22" (uuid "{gen_uuid()}"))
		(pin "23" (uuid "{gen_uuid()}"))
		(pin "30" (uuid "{gen_uuid()}"))
		(pin "31" (uuid "{gen_uuid()}"))
		(pin "40" (uuid "{gen_uuid()}"))
		(pin "50" (uuid "{gen_uuid()}"))
		(pin "EP" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "U2")
					(unit 1)
				)
			)
		)
	)
'''

    # ==================== 4x Downstream Ports ====================
    # Each port: TPD4S012 (ESD) -> TPS2041 (Power) -> USB_A Connector

    port_configs = [
        {'num': 1, 'y_offset': 0,   'dn_dp': 'USBDN1_DP', 'dn_dm': 'USBDN1_DM'},
        {'num': 2, 'y_offset': 50,  'dn_dp': 'USBDN2_DP', 'dn_dm': 'USBDN2_DM'},
        {'num': 3, 'y_offset': 100, 'dn_dp': 'USBDN3_DP', 'dn_dm': 'USBDN3_DM'},
        {'num': 4, 'y_offset': 150, 'dn_dp': 'USBDN4_DP', 'dn_dm': 'USBDN4_DM'},
    ]

    base_x = 200
    base_y = 50

    for port in port_configs:
        n = port['num']
        y = base_y + port['y_offset']

        # TPD4S012 ESD Protection
        tpd_x = base_x
        tpd_y = y
        schematic += f'''
	(symbol
		(lib_id "Power_Protection:TPD4S012")
		(at {tpd_x} {tpd_y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U{2 + n}"
			(at {tpd_x} {tpd_y - 12} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "TPD4S012"
			(at {tpd_x} {tpd_y - 10} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm"
			(at {tpd_x} {tpd_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tpd_x} {tpd_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(pin "5" (uuid "{gen_uuid()}"))
		(pin "6" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "U{2 + n}")
					(unit 1)
				)
			)
		)
	)
'''

        # TPS2041 Power Switch
        tps_x = base_x + 40
        tps_y = y
        schematic += f'''
	(symbol
		(lib_id "Power_Management:TPS2041B")
		(at {tps_x} {tps_y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U{6 + n}"
			(at {tps_x} {tps_y - 12} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "TPS2041B"
			(at {tps_x} {tps_y - 10} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_TO_SOT_SMD:SOT-23-5"
			(at {tps_x} {tps_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x} {tps_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(pin "5" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "U{6 + n}")
					(unit 1)
				)
			)
		)
	)
'''

        # USB_A Connector
        usb_x = base_x + 80
        usb_y = y
        schematic += f'''
	(symbol
		(lib_id "Connector:USB_A")
		(at {usb_x} {usb_y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "J{n}"
			(at {usb_x} {usb_y - 10} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB_A"
			(at {usb_x} {usb_y + 10} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal"
			(at {usb_x} {usb_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb_x} {usb_y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "J{n}")
					(unit 1)
				)
			)
		)
	)
'''

        # ==================== WIRES for this port ====================
        # USB5744 DN -> TPD4S012 input
        hub_out_x = usb5744_x + 17.78
        hub_dp_y = usb5744_y + 25.4 - (n - 1) * 7.62
        hub_dm_y = hub_dp_y - 2.54

        # Wire from USB5744 to TPD4S012
        schematic += f'''
	(wire
		(pts (xy {hub_out_x} {hub_dp_y}) (xy {tpd_x - 10.16} {tpd_y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {hub_out_x} {hub_dm_y}) (xy {tpd_x - 10.16} {tpd_y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # Wire from TPD4S012 output to USB_A connector
        schematic += f'''
	(wire
		(pts (xy {tpd_x + 10.16} {tpd_y + 2.54}) (xy {usb_x - 7.62} {usb_y - 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {tpd_x + 10.16} {tpd_y}) (xy {usb_x - 7.62} {usb_y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # Wire from TPS2041 VOUT to USB_A VBUS
        schematic += f'''
	(wire
		(pts (xy {tps_x + 10.16} {tps_y + 2.54}) (xy {usb_x - 7.62} {usb_y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # +5V to TPS2041 VIN
        schematic += f'''
	(symbol
		(lib_id "power:+5V")
		(at {tps_x - 15} {tps_y + 2.54} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{10 + n}"
			(at {tps_x - 19} {tps_y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+5V"
			(at {tps_x - 17} {tps_y + 2.54} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tps_x - 15} {tps_y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x - 15} {tps_y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{10 + n}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tps_x - 15} {tps_y + 2.54}) (xy {tps_x - 10.16} {tps_y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # GND for TPS2041
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {tps_x} {tps_y + 12} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{20 + n}"
			(at {tps_x} {tps_y + 18} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {tps_x} {tps_y + 16} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tps_x} {tps_y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x} {tps_y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{20 + n}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tps_x} {tps_y + 7.62}) (xy {tps_x} {tps_y + 12}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # GND for TPD4S012
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {tpd_x} {tpd_y + 14} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{30 + n}"
			(at {tpd_x} {tpd_y + 20} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {tpd_x} {tpd_y + 18} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tpd_x} {tpd_y + 14} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tpd_x} {tpd_y + 14} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{30 + n}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tpd_x} {tpd_y + 8.89}) (xy {tpd_x} {tpd_y + 14}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

        # GND for USB connector
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {usb_x - 12} {usb_y - 5.08} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{40 + n}"
			(at {usb_x - 18} {usb_y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {usb_x - 15} {usb_y - 5.08} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb_x - 12} {usb_y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb_x - 12} {usb_y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{40 + n}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb_x - 12} {usb_y - 5.08}) (xy {usb_x - 7.62} {usb_y - 5.08}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ==================== USB3320 to USB5744 upstream connection ====================
    # Wire from USB3320 DP/DM to USB5744 upstream
    schematic += f'''
	(wire
		(pts (xy {usb3320_x - 15.24} {usb3320_y + 10.16}) (xy {usb5744_x - 17.78} {usb5744_y + 20.32}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {usb3320_x - 15.24} {usb3320_y + 7.62}) (xy {usb5744_x - 17.78} {usb5744_y + 17.78}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ==================== Power for USB5744 ====================
    schematic += f'''
	(symbol
		(lib_id "power:+3V3")
		(at {usb5744_x - 22} {usb5744_y + 25.4} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR01"
			(at {usb5744_x - 26} {usb5744_y + 25.4} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+3V3"
			(at {usb5744_x - 24} {usb5744_y + 25.4} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb5744_x - 22} {usb5744_y + 25.4} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb5744_x - 22} {usb5744_y + 25.4} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR01")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb5744_x - 22} {usb5744_y + 25.4}) (xy {usb5744_x - 17.78} {usb5744_y + 25.4}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # GND for USB5744
    schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {usb5744_x} {usb5744_y + 35} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR02"
			(at {usb5744_x} {usb5744_y + 41} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {usb5744_x} {usb5744_y + 39} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb5744_x} {usb5744_y + 35} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb5744_x} {usb5744_y + 35} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR02")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb5744_x} {usb5744_y + 30.48}) (xy {usb5744_x} {usb5744_y + 35}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ==================== Power for USB3320 ====================
    schematic += f'''
	(symbol
		(lib_id "power:+3V3")
		(at {usb3320_x - 20} {usb3320_y + 15.24} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR03"
			(at {usb3320_x - 24} {usb3320_y + 15.24} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+3V3"
			(at {usb3320_x - 22} {usb3320_y + 15.24} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb3320_x - 20} {usb3320_y + 15.24} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb3320_x - 20} {usb3320_y + 15.24} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR03")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb3320_x - 20} {usb3320_y + 15.24}) (xy {usb3320_x - 15.24} {usb3320_y + 15.24}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # GND for USB3320
    schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {usb3320_x} {usb3320_y + 25} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR04"
			(at {usb3320_x} {usb3320_y + 31} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {usb3320_x} {usb3320_y + 29} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb3320_x} {usb3320_y + 25} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb3320_x} {usb3320_y + 25} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR04")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb3320_x} {usb3320_y + 20.32}) (xy {usb3320_x} {usb3320_y + 25}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ==================== Hierarchical Labels for ULPI interface ====================
    ulpi_labels = [
        ('USB_CLK', usb3320_x + 15.24, usb3320_y + 15.24),
        ('USB_DIR', usb3320_x + 15.24, usb3320_y + 12.7),
        ('USB_NXT', usb3320_x + 15.24, usb3320_y + 10.16),
        ('USB_STP', usb3320_x + 15.24, usb3320_y + 7.62),
        ('USB_DATA0', usb3320_x + 15.24, usb3320_y + 2.54),
        ('USB_DATA1', usb3320_x + 15.24, usb3320_y),
        ('USB_DATA2', usb3320_x + 15.24, usb3320_y - 2.54),
        ('USB_DATA3', usb3320_x + 15.24, usb3320_y - 5.08),
        ('USB_DATA4', usb3320_x + 15.24, usb3320_y - 7.62),
        ('USB_DATA5', usb3320_x + 15.24, usb3320_y - 10.16),
        ('USB_DATA6', usb3320_x + 15.24, usb3320_y - 12.7),
        ('USB_DATA7', usb3320_x + 15.24, usb3320_y - 15.24),
    ]

    for name, x, y in ulpi_labels:
        schematic += f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at {x + 10} {y} 0)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {x} {y}) (xy {x + 10} {y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # Power hierarchical labels
    schematic += f'''
	(hierarchical_label "+5V"
		(shape input)
		(at 30 40 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "+3V3"
		(shape input)
		(at 30 45 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "GND"
		(shape passive)
		(at 30 50 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
'''

    # Close schematic
    schematic += '''
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
'''

    return schematic


def main():
    content = create_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"USB schematic generated: {OUTPUT_FILE}")
    print(f"File size: {len(content)} bytes")


if __name__ == "__main__":
    main()
