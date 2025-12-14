#!/usr/bin/env python3
"""
전원 회로도 재생성 스크립트
- 파워 심벌 기반 연결 (긴 배선 없이)
- +12V_IN, +5V, +3V3, +1V8, GND 사용
"""

import uuid
import os

PROJECT_DIR = r"D:\git2\fcBoardKicad"

def gen_uuid():
    return str(uuid.uuid4())

def create_power_schematic():
    """깔끔한 전원 회로도 생성"""

    content = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "Power Supply - Clean Design")
		(date "2024-12-01")
		(rev "0.2")
		(company "fcBoard Project")
		(comment 1 "12V Input, 5V/3.3V/1.8V DC-DC Outputs")
		(comment 2 "Power Symbol Based Connections")
	)
	(lib_symbols
'''

    # Barrel Jack Symbol
    content += '''		(symbol "Connector:Barrel_Jack_Switch"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Barrel_Jack" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Connector_BarrelJack:BarrelJack_Horizontal" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "DC Barrel Jack with Switch" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Barrel_Jack_Switch_0_1"
				(rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Barrel_Jack_Switch_1_1"
				(pin passive line (at 7.62 2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 7.62 -2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # LM2596S-5 Symbol
    content += '''		(symbol "Regulator_Switching:LM2596S-5"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at -7.62 6.35 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "LM2596S-5" (at 2.54 6.35 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "5V 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "LM2596S-5_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "LM2596S-5_1_1"
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin output line (at 10.16 2.54 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # LM2596S-ADJ Symbol
    content += '''		(symbol "Regulator_Switching:LM2596S-ADJ"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at -7.62 6.35 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "LM2596S-ADJ" (at 2.54 6.35 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Adjustable 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "LM2596S-ADJ_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "LM2596S-ADJ_1_1"
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin output line (at 10.16 2.54 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # Capacitor Symbol
    content += '''		(symbol "Device:C"
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
'''

    # LED Symbol
    content += '''		(symbol "Device:LED"
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
'''

    # Resistor Symbol
    content += '''		(symbol "Device:R"
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
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # Inductor Symbol
    content += '''		(symbol "Device:L"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
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
				(pin passive line (at 0 3.81 270) (length 1.27) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # Diode Symbol
    content += '''		(symbol "Device:D_Schottky"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Schottky Diode" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "D_Schottky_0_1"
				(polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.27 1.27) (xy -1.27 -1.27) (xy -0.762 -1.27) (xy -0.762 -1.016)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "D_Schottky_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    # Power Symbols
    content += '''		(symbol "power:+12V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+12V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+12V_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+12V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+12V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard:+12V_IN"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+12V_IN" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "12V Input Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+12V_IN_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+12V_IN_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+12V_IN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:+5V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+5V_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+5V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:+3V3"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+3V3_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+3V3_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:+1V8"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+1V8" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+1V8_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+1V8_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "+1V8" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "power:GND"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "GND_0_1"
				(polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "GND_1_1"
				(pin power_in line (at 0 0 270) (length 0) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
'''

    content += '''	)
'''

    # ========== INSTANCES ==========
    # 위치 정의
    # Section 1: Input (50, 50) - DC Jack
    # Section 2: +5V Regulator (50, 100)
    # Section 3: +3.3V Regulator (150, 100)
    # Section 4: +1.8V Regulator (250, 100)

    # Title Text
    content += f'''
	(text "Power Supply - Clean Design\\nPower Symbol Based Connections\\n\\n+12V_IN → +5V → +3V3 → +1V8"
		(exclude_from_sim no)
		(at 30 25 0)
		(effects (font (size 2.54 2.54)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== DC Input Section =====
    content += f'''
	(text "=== DC 12V Input ==="
		(exclude_from_sim no)
		(at 30 50 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # J16 - DC Barrel Jack
    j16_uuid = gen_uuid()
    content += f'''
	(symbol
		(lib_id "Connector:Barrel_Jack_Switch")
		(at 50 60 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{j16_uuid}")
		(property "Reference" "J16"
			(at 50 50.8 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "DC_12V"
			(at 50 68.58 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Connector_BarrelJack:BarrelJack_Horizontal"
			(at 51.27 61.27 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 51.27 61.27 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 50 60 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1"
			(uuid "{gen_uuid()}")
		)
		(pin "2"
			(uuid "{gen_uuid()}")
		)
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "J16")
					(unit 1)
				)
			)
		)
	)
'''

    # +12V_IN power symbol at DC Jack output
    content += f'''
	(symbol
		(lib_id "fcBoard:+12V_IN")
		(at 65 57.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR01"
			(at 65 53.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+12V_IN"
			(at 65 53.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 65 57.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 65 57.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 65 57.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1"
			(uuid "{gen_uuid()}")
		)
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR01")
					(unit 1)
				)
			)
		)
	)
'''

    # GND at DC Jack
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 65 62.54 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR02"
			(at 65 68.89 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 65 66.35 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 65 62.54 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 65 62.54 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 65 62.54 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1"
			(uuid "{gen_uuid()}")
		)
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR02")
					(unit 1)
				)
			)
		)
	)
'''

    # Wire: J16 pin1 to +12V_IN
    content += f'''
	(wire
		(pts (xy 57.62 57.46) (xy 65 57.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 57.62 62.54) (xy 65 62.54))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== +5V Regulator Section =====
    content += f'''
	(text "=== +5V Regulator (U28) ==="
		(exclude_from_sim no)
		(at 30 85 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # U28 - LM2596S-5
    content += f'''
	(symbol
		(lib_id "Regulator_Switching:LM2596S-5")
		(at 60 100 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U28"
			(at 52.38 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Value" "LM2596S-5"
			(at 62.54 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3"
			(at 60 112.7 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 60 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 60 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(pin "5" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "U28")
					(unit 1)
				)
			)
		)
	)
'''

    # +12V_IN at U28 VIN
    content += f'''
	(symbol
		(lib_id "fcBoard:+12V_IN")
		(at 45 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR03"
			(at 45 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+12V_IN"
			(at 45 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 45 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 45 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 45 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR03")
					(unit 1)
				)
			)
		)
	)
'''

    # +5V at U28 OUT
    content += f'''
	(symbol
		(lib_id "power:+5V")
		(at 75 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR04"
			(at 75 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+5V"
			(at 75 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 75 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 75 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 75 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR04")
					(unit 1)
				)
			)
		)
	)
'''

    # GND at U28
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 60 110 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR05"
			(at 60 116.35 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 60 113.81 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 60 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 60 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 60 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR05")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for U28
    content += f'''
	(wire
		(pts (xy 45 97.46) (xy 49.84 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 70.16 97.46) (xy 75 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 60 107.62) (xy 60 110))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== +3.3V Regulator Section =====
    content += f'''
	(text "=== +3.3V Regulator (U26) ==="
		(exclude_from_sim no)
		(at 130 85 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # U26 - LM2596S-ADJ for 3.3V
    content += f'''
	(symbol
		(lib_id "Regulator_Switching:LM2596S-ADJ")
		(at 160 100 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U26"
			(at 152.38 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Value" "LM2596S-ADJ"
			(at 162.54 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3"
			(at 160 112.7 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 160 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 160 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(pin "5" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "U26")
					(unit 1)
				)
			)
		)
	)
'''

    # +12V_IN at U26 VIN
    content += f'''
	(symbol
		(lib_id "fcBoard:+12V_IN")
		(at 145 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR06"
			(at 145 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+12V_IN"
			(at 145 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 145 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 145 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 145 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR06")
					(unit 1)
				)
			)
		)
	)
'''

    # +3V3 at U26 OUT
    content += f'''
	(symbol
		(lib_id "power:+3V3")
		(at 175 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR07"
			(at 175 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+3V3"
			(at 175 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 175 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 175 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 175 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR07")
					(unit 1)
				)
			)
		)
	)
'''

    # GND at U26
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 160 110 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR08"
			(at 160 116.35 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 160 113.81 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 160 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 160 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 160 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR08")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for U26
    content += f'''
	(wire
		(pts (xy 145 97.46) (xy 149.84 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 170.16 97.46) (xy 175 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 160 107.62) (xy 160 110))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== +1.8V Regulator Section =====
    content += f'''
	(text "=== +1.8V Regulator (U27) ==="
		(exclude_from_sim no)
		(at 230 85 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # U27 - LM2596S-ADJ for 1.8V
    content += f'''
	(symbol
		(lib_id "Regulator_Switching:LM2596S-ADJ")
		(at 260 100 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "U27"
			(at 252.38 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Value" "LM2596S-ADJ"
			(at 262.54 93.65 0)
			(effects (font (size 1.27 1.27)) (justify left))
		)
		(property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3"
			(at 260 112.7 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 260 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 260 100 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(pin "3" (uuid "{gen_uuid()}"))
		(pin "4" (uuid "{gen_uuid()}"))
		(pin "5" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "U27")
					(unit 1)
				)
			)
		)
	)
'''

    # +12V_IN at U27 VIN
    content += f'''
	(symbol
		(lib_id "fcBoard:+12V_IN")
		(at 245 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR09"
			(at 245 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+12V_IN"
			(at 245 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 245 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 245 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 245 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR09")
					(unit 1)
				)
			)
		)
	)
'''

    # +1V8 at U27 OUT
    content += f'''
	(symbol
		(lib_id "power:+1V8")
		(at 275 97.46 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR10"
			(at 275 93.65 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+1V8"
			(at 275 93.34 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 275 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 275 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 275 97.46 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR10")
					(unit 1)
				)
			)
		)
	)
'''

    # GND at U27
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 260 110 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR11"
			(at 260 116.35 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 260 113.81 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 260 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 260 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 260 110 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR11")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for U27
    content += f'''
	(wire
		(pts (xy 245 97.46) (xy 249.84 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 270.16 97.46) (xy 275 97.46))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 260 107.62) (xy 260 110))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== LED Indicators Section =====
    content += f'''
	(text "=== Power LED Indicators ==="
		(exclude_from_sim no)
		(at 30 140 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
'''

    # +5V LED (D12)
    content += f'''
	(symbol
		(lib_id "Device:LED")
		(at 60 155 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "D12"
			(at 60 149 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "LED_5V"
			(at 60 161 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "LED_SMD:LED_0603_1608Metric"
			(at 60 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 60 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 60 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "D12")
					(unit 1)
				)
			)
		)
	)
'''

    # R21 for D12
    content += f'''
	(symbol
		(lib_id "Device:R")
		(at 75 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "R21"
			(at 75 150 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "1K"
			(at 75 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Resistor_SMD:R_0402_1005Metric"
			(at 75 156.778 90)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 75 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 75 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "R21")
					(unit 1)
				)
			)
		)
	)
'''

    # +5V for LED
    content += f'''
	(symbol
		(lib_id "power:+5V")
		(at 50 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR12"
			(at 53.81 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+5V"
			(at 46.44 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 50 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 50 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 50 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR12")
					(unit 1)
				)
			)
		)
	)
'''

    # GND for LED
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 85 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR13"
			(at 91.35 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 88.81 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 85 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 85 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 85 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR13")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for 5V LED
    content += f'''
	(wire
		(pts (xy 50 155) (xy 56.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 63.81 155) (xy 71.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 78.81 155) (xy 85 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # +3V3 LED (D15)
    content += f'''
	(symbol
		(lib_id "Device:LED")
		(at 160 155 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "D15"
			(at 160 149 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "LED_3V3"
			(at 160 161 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "LED_SMD:LED_0603_1608Metric"
			(at 160 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 160 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 160 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "D15")
					(unit 1)
				)
			)
		)
	)
'''

    # R18 for D15
    content += f'''
	(symbol
		(lib_id "Device:R")
		(at 175 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "R18"
			(at 175 150 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "470"
			(at 175 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Resistor_SMD:R_0402_1005Metric"
			(at 175 156.778 90)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 175 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 175 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "R18")
					(unit 1)
				)
			)
		)
	)
'''

    # +3V3 for LED
    content += f'''
	(symbol
		(lib_id "power:+3V3")
		(at 150 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR14"
			(at 153.81 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+3V3"
			(at 146.44 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 150 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 150 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 150 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR14")
					(unit 1)
				)
			)
		)
	)
'''

    # GND for 3V3 LED
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 185 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR15"
			(at 191.35 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 188.81 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 185 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 185 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 185 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR15")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for 3V3 LED
    content += f'''
	(wire
		(pts (xy 150 155) (xy 156.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 163.81 155) (xy 171.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 178.81 155) (xy 185 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # +1V8 LED (D16)
    content += f'''
	(symbol
		(lib_id "Device:LED")
		(at 260 155 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "D16"
			(at 260 149 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "LED_1V8"
			(at 260 161 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "LED_SMD:LED_0603_1608Metric"
			(at 260 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 260 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 260 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "D16")
					(unit 1)
				)
			)
		)
	)
'''

    # R19 for D16
    content += f'''
	(symbol
		(lib_id "Device:R")
		(at 275 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "R19"
			(at 275 150 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "100"
			(at 275 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "Resistor_SMD:R_0402_1005Metric"
			(at 275 156.778 90)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 275 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 275 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(pin "2" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "R19")
					(unit 1)
				)
			)
		)
	)
'''

    # +1V8 for LED
    content += f'''
	(symbol
		(lib_id "power:+1V8")
		(at 250 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR16"
			(at 253.81 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "+1V8"
			(at 246.44 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 250 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 250 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 250 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR16")
					(unit 1)
				)
			)
		)
	)
'''

    # GND for 1V8 LED
    content += f'''
	(symbol
		(lib_id "power:GND")
		(at 285 155 90)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR17"
			(at 291.35 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Value" "GND"
			(at 288.81 155 90)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" ""
			(at 285 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Datasheet" ""
			(at 285 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(property "Description" ""
			(at 285 155 0)
			(effects (font (size 1.27 1.27)) hide)
		)
		(pin "1" (uuid "{gen_uuid()}"))
		(instances
			(project "fcBoard"
				(path "/e63e39d7-6ac0-4ffd-8aa3-1841a4541b55/b1a2c3d4-0001-0001-0001-000000000001"
					(reference "#PWR17")
					(unit 1)
				)
			)
		)
	)
'''

    # Wires for 1V8 LED
    content += f'''
	(wire
		(pts (xy 250 155) (xy 256.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 263.81 155) (xy 271.19 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
	(wire
		(pts (xy 278.81 155) (xy 285 155))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
'''

    # ===== Hierarchical Labels =====
    content += f'''
	(hierarchical_label "+12V_IN"
		(shape output)
		(at 30 180 180)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "+5V"
		(shape output)
		(at 30 185 180)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "+3V3"
		(shape output)
		(at 30 190 180)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "+1V8"
		(shape output)
		(at 30 195 180)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
	(hierarchical_label "GND"
		(shape passive)
		(at 30 200 180)
		(effects (font (size 1.27 1.27)) (justify right))
		(uuid "{gen_uuid()}")
	)
'''

    # Close schematic
    content += '''
	(sheet_instances
		(path "/"
			(page "2")
		)
	)
)
'''

    return content


def main():
    output_path = os.path.join(PROJECT_DIR, "fcBoard_Power_Clean.kicad_sch")

    print("Generating clean power schematic...")
    content = create_power_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {output_path}")
    print("Done!")


if __name__ == "__main__":
    main()
