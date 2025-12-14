#!/usr/bin/env python3
"""
KiCad 전원부 회로도 생성 스크립트
S-expression 형식으로 직접 생성
"""

import uuid
import os

def gen_uuid():
    """UUID 생성"""
    return str(uuid.uuid4())

def create_power_schematic():
    """전원부 회로도 생성"""

    sch = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{main_uuid}")
  (paper "A3")
  (title_block
    (title "Power Supply")
    (date "2024-11-30")
    (rev "0.1")
    (company "fcBoard Project")
    (comment 1 "12V Input, 5V/3.3V/1.8V DC-DC Outputs")
  )

  (lib_symbols
    {lib_symbols}
  )

  {components}

  {wires}

  {labels}

  {power_symbols}
)
'''

    # 라이브러리 심볼 정의
    lib_symbols = generate_lib_symbols()

    # 컴포넌트 배치
    components = generate_components()

    # 와이어 연결
    wires = generate_wires()

    # 라벨
    labels = generate_labels()

    # 전원 심볼
    power_symbols = generate_power_symbols()

    result = sch.format(
        main_uuid=gen_uuid(),
        lib_symbols=lib_symbols,
        components=components,
        wires=wires,
        labels=labels,
        power_symbols=power_symbols
    )

    return result

def generate_lib_symbols():
    """라이브러리 심볼 정의"""

    symbols = '''
    (symbol "Connector:Barrel_Jack_Switch" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Barrel_Jack" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Barrel_Jack_Switch_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
        (arc (start -3.302 3.175) (mid -4.127 2.54) (end -3.302 1.905) (stroke (width 0.254) (type default)) (fill (type none)))
        (arc (start -3.302 -1.905) (mid -4.127 -2.54) (end -3.302 -3.175) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 3.175) (xy -3.302 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.302 -1.905) (xy -3.302 -3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 2.54) (xy 1.27 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 2.54) (xy 1.27 -2.54) (xy -1.27 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "Barrel_Jack_Switch_1_1"
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:C" (pin_numbers hide) (pin_names (offset 0.254)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
      )
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:CP" (pin_numbers hide) (pin_names (offset 0.254)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "CP" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CP_0_1"
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -1.524 -0.762) (xy 1.524 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -1.524 1.27) (xy -1.524 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 1.524) (xy -1.27 1.524)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "CP_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:L" (pin_numbers hide) (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)
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
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:D_Schottky" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
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

    (symbol "Device:LED" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LED" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -3.048 -1.524) (xy -1.778 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.778 -1.524) (xy -0.508 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 -2.794) (xy -1.778 -2.794) (xy -1.778 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -0.762 -2.794) (xy -0.508 -2.794) (xy -0.508 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Regulator_Switching:LM2596S-5" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LM2596S-5" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 -10.16 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LM2596S-5_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "LM2596S-5_1_1"
        (pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 2.54 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "~{ON}/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Regulator_Switching:LM2596S-ADJ" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LM2596S-ADJ" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 -10.16 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LM2596S-ADJ_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "LM2596S-ADJ_1_1"
        (pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 2.54 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "~{ON}/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "power:GND" (power) (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "power:+12V" (power) (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+12V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+12V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+12V_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "+12V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "power:+5V" (power) (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+5V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+5V_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "power:+3V3" (power) (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+3V3_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+3V3_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "power:+1V8" (power) (pin_numbers hide) (pin_names (offset 0) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+1V8" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+1V8_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "+1V8_1_1"
        (pin power_in line (at 0 0 90) (length 0) (name "+1V8" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
      )
    )
'''
    return symbols


def generate_components():
    """컴포넌트 인스턴스 생성"""

    components = []

    # === 12V 입력부 (왼쪽 상단) ===
    # DC Jack J1
    components.append(f'''
  (symbol
    (lib_id "Connector:Barrel_Jack_Switch")
    (at 38.1 50.8 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J1" (at 38.1 40.64 0) (effects (font (size 1.27 1.27))))
    (property "Value" "DC_12V" (at 38.1 43.18 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_BarrelJack:BarrelJack_Horizontal" (at 39.37 49.53 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 39.37 49.53 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # 입력 전해 캐패시터 C1 (470uF)
    components.append(f'''
  (symbol
    (lib_id "Device:CP")
    (at 58.42 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C1" (at 62.23 54.61 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "470uF" (at 62.23 57.15 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" (at 59.3852 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 58.42 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # === 5V 레귤레이터 (상단 중앙) ===
    # U1: LM2596S-5 (5V 고정)
    components.append(f'''
  (symbol
    (lib_id "Regulator_Switching:LM2596S-5")
    (at 101.6 50.8 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U1" (at 101.6 40.64 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-5" (at 101.6 43.18 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 101.6 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )''')

    # L1: 5V 인덕터 (33uH)
    components.append(f'''
  (symbol
    (lib_id "Device:L")
    (at 127 48.26 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "L1" (at 127 45.72 90) (effects (font (size 1.27 1.27))))
    (property "Value" "33uH" (at 127 50.8 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Inductor_SMD:L_12x12mm_H8mm" (at 127 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 127 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # D1: 5V 쇼트키 다이오드
    components.append(f'''
  (symbol
    (lib_id "Device:D_Schottky")
    (at 119.38 55.88 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D1" (at 123.19 54.61 90) (effects (font (size 1.27 1.27))))
    (property "Value" "SS34" (at 123.19 57.15 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Diode_SMD:D_SMA" (at 119.38 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 119.38 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # C2: 5V 출력 캐패시터 (220uF)
    components.append(f'''
  (symbol
    (lib_id "Device:CP")
    (at 139.7 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C2" (at 143.51 54.61 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "220uF" (at 143.51 57.15 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" (at 140.6652 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # === 3.3V 레귤레이터 (중앙) ===
    # U2: LM2596S-ADJ (3.3V)
    components.append(f'''
  (symbol
    (lib_id "Regulator_Switching:LM2596S-ADJ")
    (at 101.6 101.6 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U2" (at 101.6 91.44 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-ADJ" (at 101.6 93.98 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 101.6 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )''')

    # L2: 3.3V 인덕터 (33uH)
    components.append(f'''
  (symbol
    (lib_id "Device:L")
    (at 127 99.06 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "L2" (at 127 96.52 90) (effects (font (size 1.27 1.27))))
    (property "Value" "33uH" (at 127 101.6 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Inductor_SMD:L_12x12mm_H8mm" (at 127 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 127 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # D2: 3.3V 쇼트키 다이오드
    components.append(f'''
  (symbol
    (lib_id "Device:D_Schottky")
    (at 119.38 106.68 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D2" (at 123.19 105.41 90) (effects (font (size 1.27 1.27))))
    (property "Value" "SS34" (at 123.19 107.95 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Diode_SMD:D_SMA" (at 119.38 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 119.38 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # C3: 3.3V 출력 캐패시터 (220uF)
    components.append(f'''
  (symbol
    (lib_id "Device:CP")
    (at 139.7 106.68 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C3" (at 143.51 105.41 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "220uF" (at 143.51 107.95 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" (at 140.6652 110.49 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # R1, R2: 3.3V 피드백 저항
    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 147.32 99.06 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R1" (at 149.86 97.79 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "3.3K" (at 149.86 100.33 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 145.542 99.06 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 147.32 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 147.32 111.76 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R2" (at 149.86 110.49 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "1.5K" (at 149.86 113.03 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 145.542 111.76 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 147.32 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # === 1.8V 레귤레이터 (하단) ===
    # U3: LM2596S-ADJ (1.8V)
    components.append(f'''
  (symbol
    (lib_id "Regulator_Switching:LM2596S-ADJ")
    (at 101.6 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U3" (at 101.6 142.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-ADJ" (at 101.6 144.78 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 101.6 162.56 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )''')

    # L3: 1.8V 인덕터 (33uH)
    components.append(f'''
  (symbol
    (lib_id "Device:L")
    (at 127 149.86 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "L3" (at 127 147.32 90) (effects (font (size 1.27 1.27))))
    (property "Value" "33uH" (at 127 152.4 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Inductor_SMD:L_12x12mm_H8mm" (at 127 149.86 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 127 149.86 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # D3: 1.8V 쇼트키 다이오드
    components.append(f'''
  (symbol
    (lib_id "Device:D_Schottky")
    (at 119.38 157.48 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D3" (at 123.19 156.21 90) (effects (font (size 1.27 1.27))))
    (property "Value" "SS34" (at 123.19 158.75 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Diode_SMD:D_SMA" (at 119.38 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 119.38 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # C4: 1.8V 출력 캐패시터 (220uF)
    components.append(f'''
  (symbol
    (lib_id "Device:CP")
    (at 139.7 157.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C4" (at 143.51 156.21 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "220uF" (at 143.51 158.75 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" (at 140.6652 161.29 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # R3, R4: 1.8V 피드백 저항
    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 147.32 149.86 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R3" (at 149.86 148.59 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "1K" (at 149.86 151.13 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 145.542 149.86 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 147.32 149.86 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 147.32 162.56 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R4" (at 149.86 161.29 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "1.5K" (at 149.86 163.83 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 145.542 162.56 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 147.32 162.56 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # === LED 인디케이터 (오른쪽) ===
    # LED1: 5V (Green)
    components.append(f'''
  (symbol
    (lib_id "Device:LED")
    (at 177.8 50.8 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D4" (at 177.8 44.45 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_5V" (at 177.8 46.99 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 177.8 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 177.8 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 190.5 50.8 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R5" (at 190.5 48.26 90) (effects (font (size 1.27 1.27))))
    (property "Value" "1K" (at 190.5 53.34 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 190.5 52.578 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 190.5 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # LED2: 3.3V (Green)
    components.append(f'''
  (symbol
    (lib_id "Device:LED")
    (at 177.8 101.6 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D5" (at 177.8 95.25 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_3V3" (at 177.8 97.79 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 177.8 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 177.8 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 190.5 101.6 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R6" (at 190.5 99.06 90) (effects (font (size 1.27 1.27))))
    (property "Value" "470" (at 190.5 104.14 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 190.5 103.378 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 190.5 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    # LED3: 1.8V (Green)
    components.append(f'''
  (symbol
    (lib_id "Device:LED")
    (at 177.8 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D6" (at 177.8 146.05 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_1V8" (at 177.8 148.59 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 177.8 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 177.8 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    components.append(f'''
  (symbol
    (lib_id "Device:R")
    (at 190.5 152.4 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R7" (at 190.5 149.86 90) (effects (font (size 1.27 1.27))))
    (property "Value" "100" (at 190.5 154.94 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 190.5 154.178 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 190.5 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )''')

    return '\n'.join(components)


def generate_wires():
    """와이어 연결 생성"""

    wires = []

    # === 12V 입력부 연결 ===
    # J1 출력 -> C1 입력
    wires.append(f'''
  (wire
    (pts (xy 45.72 48.26) (xy 58.42 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 58.42 48.26) (xy 58.42 52.07))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # 12V 버스 (입력에서 각 레귤레이터로)
    wires.append(f'''
  (wire
    (pts (xy 58.42 48.26) (xy 76.2 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 76.2 48.26) (xy 91.44 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 76.2 48.26) (xy 76.2 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 76.2 99.06) (xy 91.44 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 76.2 99.06) (xy 76.2 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 76.2 149.86) (xy 91.44 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # === 5V 출력 연결 ===
    wires.append(f'''
  (wire
    (pts (xy 111.76 48.26) (xy 119.38 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 48.26) (xy 119.38 52.07))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 48.26) (xy 123.19 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 130.81 48.26) (xy 139.7 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 48.26) (xy 139.7 52.07))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 48.26) (xy 160.02 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 48.26) (xy 160.02 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 50.8) (xy 173.99 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 181.61 50.8) (xy 186.69 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # === 3.3V 출력 연결 ===
    wires.append(f'''
  (wire
    (pts (xy 111.76 99.06) (xy 119.38 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 99.06) (xy 119.38 102.87))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 99.06) (xy 123.19 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 130.81 99.06) (xy 139.7 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 99.06) (xy 139.7 102.87))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 99.06) (xy 147.32 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 95.25) (xy 147.32 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 99.06) (xy 160.02 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 99.06) (xy 160.02 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 101.6) (xy 173.99 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 181.61 101.6) (xy 186.69 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # 피드백 연결
    wires.append(f'''
  (wire
    (pts (xy 147.32 102.87) (xy 147.32 104.14))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 104.14) (xy 111.76 104.14))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 107.95) (xy 147.32 104.14))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # === 1.8V 출력 연결 ===
    wires.append(f'''
  (wire
    (pts (xy 111.76 149.86) (xy 119.38 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 149.86) (xy 119.38 153.67))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 149.86) (xy 123.19 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 130.81 149.86) (xy 139.7 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 149.86) (xy 139.7 153.67))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 149.86) (xy 147.32 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 146.05) (xy 147.32 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 149.86) (xy 160.02 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 149.86) (xy 160.02 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 152.4) (xy 173.99 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 181.61 152.4) (xy 186.69 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    # 피드백 연결
    wires.append(f'''
  (wire
    (pts (xy 147.32 153.67) (xy 147.32 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 154.94) (xy 111.76 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 147.32 158.75) (xy 147.32 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )''')

    return '\n'.join(wires)


def generate_labels():
    """전원 라벨 생성"""

    labels = []

    # 출력 라벨
    labels.append(f'''
  (label "+5V_OUT"
    (at 160.02 48.26 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (label "+3V3_OUT"
    (at 160.02 99.06 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (label "+1V8_OUT"
    (at 160.02 149.86 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )''')

    # Hierarchical labels for sheet connections
    labels.append(f'''
  (hierarchical_label "+12V"
    (shape input)
    (at 58.42 40.64 90)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (hierarchical_label "+5V"
    (shape output)
    (at 160.02 40.64 90)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (hierarchical_label "+3V3"
    (shape output)
    (at 160.02 91.44 90)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (hierarchical_label "+1V8"
    (shape output)
    (at 160.02 142.24 90)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )''')

    labels.append(f'''
  (hierarchical_label "GND"
    (shape passive)
    (at 101.6 175.26 270)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )''')

    return '\n'.join(labels)


def generate_power_symbols():
    """전원 심볼 인스턴스 생성"""

    power = []

    # +12V 심볼
    power.append(f'''
  (symbol
    (lib_id "power:+12V")
    (at 58.42 40.64 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR01" (at 58.42 44.45 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+12V" (at 58.42 36.83 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 58.42 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 58.42 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )''')

    # +5V 심볼
    power.append(f'''
  (symbol
    (lib_id "power:+5V")
    (at 160.02 40.64 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 160.02 44.45 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 160.02 36.83 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 160.02 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 160.02 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )''')

    # +3V3 심볼
    power.append(f'''
  (symbol
    (lib_id "power:+3V3")
    (at 160.02 91.44 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 160.02 95.25 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 160.02 87.63 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 160.02 91.44 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 160.02 91.44 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )''')

    # +1V8 심볼
    power.append(f'''
  (symbol
    (lib_id "power:+1V8")
    (at 160.02 142.24 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 160.02 146.05 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 160.02 138.43 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 160.02 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 160.02 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )''')

    # GND 심볼들
    gnd_positions = [
        (58.42, 59.69),   # C1
        (45.72, 53.34),   # J1 GND
        (101.6, 58.42),   # U1 GND
        (119.38, 59.69),  # D1
        (139.7, 59.69),   # C2
        (101.6, 109.22),  # U2 GND
        (119.38, 110.49), # D2
        (139.7, 110.49),  # C3
        (147.32, 115.57), # R2
        (101.6, 160.02),  # U3 GND
        (119.38, 161.29), # D3
        (139.7, 161.29),  # C4
        (147.32, 166.37), # R4
        (194.31, 50.8),   # R5 (LED)
        (194.31, 101.6),  # R6 (LED)
        (194.31, 152.4),  # R7 (LED)
    ]

    for i, (x, y) in enumerate(gnd_positions):
        power.append(f'''
  (symbol
    (lib_id "power:GND")
    (at {x} {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{i+10:02d}" (at {x} {y+6.35} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at {x} {y+3.81} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )''')

    return '\n'.join(power)


if __name__ == "__main__":
    output_path = r"D:\git2\fcBoardKicad\fcBoard_Power.kicad_sch"

    # 회로도 생성
    schematic = create_power_schematic()

    # 파일 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"Power schematic generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")
