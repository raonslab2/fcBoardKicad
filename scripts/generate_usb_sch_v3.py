#!/usr/bin/env python3
"""
Generate USB 3.0 Hub schematic - Clean layout v3
Layout: USB3320 (left) -> USB5744 (center) -> TPD4S012 -> TPS2041B -> USB_A (right)
4 downstream ports arranged vertically
"""

import uuid

OUTPUT_FILE = r"D:\git2\fcBoardKicad\fcBoard_USB.kicad_sch"

def gen_uuid():
    return str(uuid.uuid4())

def create_schematic():
    schematic = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "USB 3.0 Hub")
		(date "2024-12-01")
		(rev "0.3")
		(company "fcBoard Project")
		(comment 1 "USB5744 4-Port USB 3.0 Hub + USB3320 ULPI PHY")
		(comment 2 "Signal: SoM -> USB3320 -> USB5744 -> TPD4S012 -> TPS2041B -> USB_A")
	)
'''

    # ============== LIB_SYMBOLS ==============
    schematic += '''
	(lib_symbols
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
				(pin power_in line (at 0 20.32 270) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "DP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "DM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin output line (at -15.24 12.7 0) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin output line (at -15.24 10.16 0) (length 2.54) (name "DIR" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin output line (at -15.24 7.62 0) (length 2.54) (name "NXT" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 5.08 0) (length 2.54) (name "STP" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 0 0) (length 2.54) (name "DATA0" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -2.54 0) (length 2.54) (name "DATA1" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -5.08 0) (length 2.54) (name "DATA2" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -7.62 0) (length 2.54) (name "DATA3" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -10.16 0) (length 2.54) (name "DATA4" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -12.7 0) (length 2.54) (name "DATA5" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 -15.24 0) (length 2.54) (name "DATA6" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -15.24 180) (length 2.54) (name "DATA7" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "EP" (effects (font (size 1.27 1.27)))))
			)
		)
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
				(rectangle (start -12.7 27.94) (end 12.7 -27.94)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "USB5744_1_1"
				(pin power_in line (at 0 30.48 270) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 20.32 0) (length 2.54) (name "USBUP_DP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -15.24 17.78 0) (length 2.54) (name "USBUP_DM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 20.32 180) (length 2.54) (name "DN1_DP" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 17.78 180) (length 2.54) (name "DN1_DM" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "DN2_DP" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "DN2_DM" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "DN3_DP" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DN3_DM" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DN4_DP" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 -5.08 180) (length 2.54) (name "DN4_DM" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 -10.16 0) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "30" (effects (font (size 1.27 1.27)))))
				(pin output line (at -15.24 -12.7 0) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "31" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 -17.78 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "40" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -15.24 -22.86 0) (length 2.54) (name "VBUS_DET" (effects (font (size 1.27 1.27)))) (number "50" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -30.48 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "EP" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Power_Protection:TPD4S012"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U"
				(at 0 8.89 0)
				(effects (font (size 1.27 1.27)))
			)
			(property "Value" "TPD4S012"
				(at 0 6.35 0)
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
				(rectangle (start -7.62 5.08) (end 7.62 -5.08)
					(stroke (width 0.254) (type default))
					(fill (type background))
				)
			)
			(symbol "TPD4S012_1_1"
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "D+_IN" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "D+_OUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "D-_IN" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "D-_OUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 7.62 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
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
				(pin input line (at -10.16 0 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin open_collector line (at 10.16 0 180) (length 2.54) (name "OC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
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
				(at 0 -10.16 0)
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
				(rectangle (start -5.08 5.08) (end 5.08 -7.62)
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
				(rectangle (start -1.27 2.54) (end 1.27 -2.54) (stroke (width 0) (type default)) (fill (type none)))
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
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
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

    # ============== COMPONENT PLACEMENT ==============
    # Coordinates (in mm)
    # USB3320: x=60, y=100
    # USB5744: x=130, y=100
    # Port 1: TPD@200, TPS@240, USB_A@290, y=60
    # Port 2: TPD@200, TPS@240, USB_A@290, y=100
    # Port 3: TPD@200, TPS@240, USB_A@290, y=140
    # Port 4: TPD@200, TPS@240, USB_A@290, y=180

    usb3320_x, usb3320_y = 60, 100
    usb5744_x, usb5744_y = 130, 100

    port_y = [60, 100, 140, 180]  # Y positions for 4 ports
    tpd_x = 200
    tps_x = 245
    usb_x = 300

    # ===== USB3320 (ULPI PHY) =====
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
			(at {usb3320_x} {usb3320_y - 23} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB3320"
			(at {usb3320_x} {usb3320_y - 21} 0)
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

    # ===== USB5744 (Hub) =====
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
			(at {usb5744_x} {usb5744_y - 33} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB5744"
			(at {usb5744_x} {usb5744_y - 31} 0)
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

    # ===== 4 Downstream Ports =====
    for i, y in enumerate(port_y):
        port_num = i + 1

        # TPD4S012 (ESD)
        schematic += f'''
	(symbol
		(lib_id "Power_Protection:TPD4S012")
		(at {tpd_x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U{2 + port_num}"
			(at {tpd_x} {y - 11} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "TPD4S012"
			(at {tpd_x} {y - 9} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm"
			(at {tpd_x} {y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tpd_x} {y} 0)
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
					(reference "U{2 + port_num}")
					(unit 1)
				)
			)
		)
	)
'''

        # TPS2041B (Power Switch)
        schematic += f'''
	(symbol
		(lib_id "Power_Management:TPS2041B")
		(at {tps_x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U{6 + port_num}"
			(at {tps_x} {y - 11} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "TPS2041B"
			(at {tps_x} {y - 9} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Package_TO_SOT_SMD:SOT-23-5"
			(at {tps_x} {y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x} {y} 0)
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
					(reference "U{6 + port_num}")
					(unit 1)
				)
			)
		)
	)
'''

        # USB_A Connector
        schematic += f'''
	(symbol
		(lib_id "Connector:USB_A")
		(at {usb_x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "J{port_num}"
			(at {usb_x} {y - 12} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "USB_A"
			(at {usb_x} {y + 12} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal"
			(at {usb_x} {y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb_x} {y} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "J{port_num}")
					(unit 1)
				)
			)
		)
	)
'''

    # ============== WIRES ==============

    # USB3320 DP/DM -> USB5744 upstream
    schematic += f'''
	(wire
		(pts (xy {usb3320_x + 15.24} {usb3320_y + 12.7}) (xy {usb5744_x - 15.24} {usb5744_y + 20.32}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {usb3320_x + 15.24} {usb3320_y + 10.16}) (xy {usb5744_x - 15.24} {usb5744_y + 17.78}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # USB5744 downstream -> TPD4S012 -> USB_A for each port
    hub_dn_y = [usb5744_y + 20.32, usb5744_y + 12.7, usb5744_y + 5.08, usb5744_y - 2.54]
    hub_dn_dm_y = [usb5744_y + 17.78, usb5744_y + 10.16, usb5744_y + 2.54, usb5744_y - 5.08]

    for i, y in enumerate(port_y):
        # Hub DN_DP -> horizontal -> down -> TPD D+_IN
        mid_x = usb5744_x + 15.24 + 10 + i * 5  # Stagger to avoid overlap
        schematic += f'''
	(wire
		(pts (xy {usb5744_x + 15.24} {hub_dn_y[i]}) (xy {mid_x} {hub_dn_y[i]}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {mid_x} {hub_dn_y[i]}) (xy {mid_x} {y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {mid_x} {y + 2.54}) (xy {tpd_x - 10.16} {y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        # Hub DN_DM -> TPD D-_IN
        mid_x2 = mid_x + 3
        schematic += f'''
	(wire
		(pts (xy {usb5744_x + 15.24} {hub_dn_dm_y[i]}) (xy {mid_x2} {hub_dn_dm_y[i]}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {mid_x2} {hub_dn_dm_y[i]}) (xy {mid_x2} {y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy {mid_x2} {y}) (xy {tpd_x - 10.16} {y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        # TPD D+_OUT -> USB_A D+
        schematic += f'''
	(wire
		(pts (xy {tpd_x + 10.16} {y + 2.54}) (xy {usb_x - 7.62} {y - 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        # TPD D-_OUT -> USB_A D-
        schematic += f'''
	(wire
		(pts (xy {tpd_x + 10.16} {y}) (xy {usb_x - 7.62} {y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        # TPS VOUT -> USB_A VBUS
        schematic += f'''
	(wire
		(pts (xy {tps_x + 10.16} {y + 2.54}) (xy {usb_x - 7.62} {y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ============== POWER SYMBOLS ==============

    # +3V3 for USB3320
    schematic += f'''
	(symbol
		(lib_id "power:+3V3")
		(at {usb3320_x} {usb3320_y - 25} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR01"
			(at {usb3320_x} {usb3320_y - 29} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+3V3"
			(at {usb3320_x} {usb3320_y - 27} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb3320_x} {usb3320_y - 25} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb3320_x} {usb3320_y - 25} 0)
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
		(pts (xy {usb3320_x} {usb3320_y - 25}) (xy {usb3320_x} {usb3320_y - 20.32}))
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
		(property "Reference" "#PWR02"
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
					(reference "#PWR02")
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

    # +3V3 for USB5744
    schematic += f'''
	(symbol
		(lib_id "power:+3V3")
		(at {usb5744_x} {usb5744_y - 35} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR03"
			(at {usb5744_x} {usb5744_y - 39} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+3V3"
			(at {usb5744_x} {usb5744_y - 37} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb5744_x} {usb5744_y - 35} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb5744_x} {usb5744_y - 35} 0)
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
		(pts (xy {usb5744_x} {usb5744_y - 35}) (xy {usb5744_x} {usb5744_y - 30.48}))
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
		(property "Reference" "#PWR04"
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
					(reference "#PWR04")
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

    # Power for each downstream port
    pwr_num = 5
    for i, y in enumerate(port_y):
        # +5V for TPS2041B VIN
        schematic += f'''
	(symbol
		(lib_id "power:+5V")
		(at {tps_x - 15} {y + 2.54} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{pwr_num}"
			(at {tps_x - 19} {y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "+5V"
			(at {tps_x - 17} {y + 2.54} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tps_x - 15} {y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x - 15} {y + 2.54} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{pwr_num}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tps_x - 15} {y + 2.54}) (xy {tps_x - 10.16} {y + 2.54}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        pwr_num += 1

        # GND for TPS2041B
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {tps_x} {y + 12} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{pwr_num}"
			(at {tps_x} {y + 18} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {tps_x} {y + 16} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tps_x} {y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tps_x} {y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{pwr_num}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tps_x} {y + 7.62}) (xy {tps_x} {y + 12}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        pwr_num += 1

        # GND for TPD4S012
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {tpd_x} {y + 12} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{pwr_num}"
			(at {tpd_x} {y + 18} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {tpd_x} {y + 16} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {tpd_x} {y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {tpd_x} {y + 12} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{pwr_num}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {tpd_x} {y + 7.62}) (xy {tpd_x} {y + 12}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        pwr_num += 1

        # GND for USB_A
        schematic += f'''
	(symbol
		(lib_id "power:GND")
		(at {usb_x - 12} {y - 5.08} 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR0{pwr_num}"
			(at {usb_x - 18} {y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Value" "GND"
			(at {usb_x - 15} {y - 5.08} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at {usb_x - 12} {y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at {usb_x - 12} {y - 5.08} 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0002-0002-0002-000000000002"
					(reference "#PWR0{pwr_num}")
					(unit 1)
				)
			)
		)
	)
	(wire
		(pts (xy {usb_x - 12} {y - 5.08}) (xy {usb_x - 7.62} {y - 5.08}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''
        pwr_num += 1

    # ============== HIERARCHICAL LABELS ==============
    # ULPI signals from USB3320 to SoM
    ulpi_y_start = usb3320_y + 12.7
    ulpi_signals = ['USB_CLK', 'USB_DIR', 'USB_NXT', 'USB_STP', 'USB_DATA0', 'USB_DATA1',
                    'USB_DATA2', 'USB_DATA3', 'USB_DATA4', 'USB_DATA5', 'USB_DATA6', 'USB_DATA7']

    for i, sig in enumerate(ulpi_signals):
        if i < 4:
            sig_y = ulpi_y_start - i * 2.54
        else:
            sig_y = usb3320_y - (i - 4) * 2.54

        schematic += f'''
	(hierarchical_label "{sig}"
		(shape bidirectional)
		(at 30 {sig_y} 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 30 {sig_y}) (xy {usb3320_x - 15.24} {sig_y}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # Power hierarchical labels
    schematic += f'''
	(hierarchical_label "+5V"
		(shape input)
		(at 30 200 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "+3V3"
		(shape input)
		(at 30 205 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "GND"
		(shape passive)
		(at 30 210 180)
		(fields_autoplaced yes)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
'''

    # ============== SHEET INSTANCES ==============
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
    print("\nLayout:")
    print("  USB3320 (60, 100) -> USB5744 (130, 100)")
    print("  Port 1: TPD(200, 60) -> TPS(245, 60) -> USB_A(300, 60)")
    print("  Port 2: TPD(200, 100) -> TPS(245, 100) -> USB_A(300, 100)")
    print("  Port 3: TPD(200, 140) -> TPS(245, 140) -> USB_A(300, 140)")
    print("  Port 4: TPD(200, 180) -> TPS(245, 180) -> USB_A(300, 180)")


if __name__ == "__main__":
    main()
