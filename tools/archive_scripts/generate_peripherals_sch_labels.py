#!/usr/bin/env python3
"""
Generate Peripherals schematic with label-based connections
CAN, RS485, MicroSD, Debug USB, User LEDs, Buttons
"""

import uuid

def gen_uuid():
    return str(uuid.uuid4())

def create_peripherals_schematic():
    """Create Peripherals schematic with label connections"""

    content = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "''' + gen_uuid() + '''")
  (paper "A3")
  (title_block
    (title "Peripherals - CAN, RS485, MicroSD, Debug")
    (company "fcBoard")
  )

  (lib_symbols
'''

    # SN65HVD230 CAN transceiver
    content += '''    (symbol "SN65HVD230" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SN65HVD230" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "SN65HVD230_0_1"
        (rectangle (start -7.62 6.35) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "SN65HVD230_1_1"
        (pin input line (at -10.16 3.81 0) (length 2.54) (name "TXD" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin output line (at -10.16 1.27 0) (length 2.54) (name "RXD" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin no_connect line (at 10.16 -5.08 180) (length 2.54) (name "NC" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 3.81 180) (length 2.54) (name "CANL" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 1.27 180) (length 2.54) (name "CANH" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -5.08 0) (length 2.54) (name "RS" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # MAX485 RS485 transceiver
    content += '''    (symbol "MAX485" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
      (property "Value" "MAX485" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -12.7 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "MAX485_0_1"
        (rectangle (start -7.62 6.35) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "MAX485_1_1"
        (pin output line (at -10.16 3.81 0) (length 2.54) (name "RO" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 1.27 0) (length 2.54) (name "~{RE}" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -1.27 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -3.81 0) (length 2.54) (name "DI" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 -1.27 180) (length 2.54) (name "A" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 1.27 180) (length 2.54) (name "B" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # CP2102N USB-UART
    content += '''    (symbol "CP2102N" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "CP2102N" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 0 -20.32 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CP2102N_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -17.78) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "CP2102N_1_1"
        (pin bidirectional line (at -12.7 10.16 0) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -12.7 2.54 0) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 10.16 180) (length 2.54) (name "TXD" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin input line (at 12.7 7.62 180) (length 2.54) (name "RXD" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "RTS" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin input line (at 12.7 0 180) (length 2.54) (name "CTS" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 -5.08 180) (length 2.54) (name "DTR" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin input line (at 12.7 -7.62 180) (length 2.54) (name "DSR" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin power_out line (at -5.08 15.24 270) (length 2.54) (name "VDD" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 15.24 270) (length 2.54) (name "REGIN" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # MicroSD connector
    content += '''    (symbol "MicroSD" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Value" "MicroSD" (at 0 11.43 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_Card:microSD_HC_Wuerth_693072010801" (at 0 -15.24 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "MicroSD_0_1"
        (rectangle (start -7.62 10.16) (end 7.62 -12.7) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "MicroSD_1_1"
        (pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "DAT2" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "DAT3/CD" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 2.54 0) (length 2.54) (name "CMD" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 12.7 270) (length 2.54) (name "VDD" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "CLK" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -15.24 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "DAT0" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "DAT1" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin output line (at 10.16 0 180) (length 2.54) (name "CD" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # Pin header 1x02
    content += '''    (symbol "PinHeader_1x02" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Value" "PinHeader_1x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "PinHeader_1x02_0_1"
        (rectangle (start -2.54 3.81) (end 2.54 -3.81) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "PinHeader_1x02_1_1"
        (pin passive line (at -5.08 1.27 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -5.08 -1.27 0) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # LED
    content += '''    (symbol "LED" (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LED" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 1.27) (xy -1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0)) (stroke (width 0.254) (type default)) (fill (type outline))))
      (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "A" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "K" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # Resistor
    content += '''    (symbol "R" (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254) (type default)) (fill (type none))))
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # Button
    content += '''    (symbol "SW_Push" (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SW_Push" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Button_Switch_SMD:SW_SPST_TL3342" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "SW_Push_0_1"
        (circle (center -2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 0) (xy -2.032 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.032 0) (xy 2.54 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -1.524 1.27) (xy 1.524 1.27)) (stroke (width 0) (type default)) (fill (type none))))
      (symbol "SW_Push_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # Power symbols
    content += '''    (symbol "power:+3V3" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (symbol "+3V3_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none))))
      (symbol "+3V3_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
    (symbol "power:GND" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none))))
      (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) hide (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
'''

    content += '''  )

'''

    # ============ SYMBOL INSTANCES ============

    # CAN section - y=50
    can_y = 50

    # CAN0: SN65HVD230 (U22) at x=80
    content += f'''  (symbol
    (lib_id "SN65HVD230")
    (at 80 {can_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U22" (at 80 {can_y-15} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN65HVD230" (at 80 {can_y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 80 {can_y+12.7} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

'''

    # CAN0 connector (J12) at x=150
    content += f'''  (symbol
    (lib_id "PinHeader_1x02")
    (at 150 {can_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J12" (at 150 {can_y-8} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CAN0" (at 150 {can_y+8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 150 {can_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # CAN1: SN65HVD230 (U24) at x=80, y+40
    can1_y = can_y + 40
    content += f'''  (symbol
    (lib_id "SN65HVD230")
    (at 80 {can1_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U24" (at 80 {can1_y-15} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN65HVD230" (at 80 {can1_y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 80 {can1_y+12.7} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

'''

    # CAN1 connector (J14) at x=150
    content += f'''  (symbol
    (lib_id "PinHeader_1x02")
    (at 150 {can1_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J14" (at 150 {can1_y-8} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CAN1" (at 150 {can1_y+8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 150 {can1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # RS485 section - y=140
    rs485_y = 140

    # RS485_0: MAX485 (U23) at x=80
    content += f'''  (symbol
    (lib_id "MAX485")
    (at 80 {rs485_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U23" (at 80 {rs485_y-15} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX485" (at 80 {rs485_y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 80 {rs485_y+12.7} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

'''

    # RS485_0 connector (J13) at x=150
    content += f'''  (symbol
    (lib_id "PinHeader_1x02")
    (at 150 {rs485_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J13" (at 150 {rs485_y-8} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RS485_0" (at 150 {rs485_y+8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 150 {rs485_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # RS485_1: MAX485 (U25) at x=80, y+40
    rs485_1_y = rs485_y + 40
    content += f'''  (symbol
    (lib_id "MAX485")
    (at 80 {rs485_1_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U25" (at 80 {rs485_1_y-15} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX485" (at 80 {rs485_1_y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 80 {rs485_1_y+12.7} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

'''

    # RS485_1 connector (J15) at x=150
    content += f'''  (symbol
    (lib_id "PinHeader_1x02")
    (at 150 {rs485_1_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J15" (at 150 {rs485_1_y-8} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RS485_1" (at 150 {rs485_1_y+8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 150 {rs485_1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # Debug USB section - x=220, y=70
    debug_y = 70
    content += f'''  (symbol
    (lib_id "CP2102N")
    (at 220 {debug_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U21" (at 220 {debug_y-20} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CP2102N" (at 220 {debug_y-17} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 220 {debug_y+20.32} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
    (pin "9" (uuid "{gen_uuid()}"))
    (pin "10" (uuid "{gen_uuid()}"))
    (pin "11" (uuid "{gen_uuid()}"))
    (pin "12" (uuid "{gen_uuid()}"))
  )

'''

    # USB Debug connector (J11)
    content += f'''  (symbol
    (lib_id "PinHeader_1x02")
    (at 290 {debug_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J11" (at 290 {debug_y-8} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_Debug" (at 290 {debug_y+8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" (at 290 {debug_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # MicroSD section - x=220, y=140
    sd_y = 140
    content += f'''  (symbol
    (lib_id "MicroSD")
    (at 220 {sd_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J10" (at 220 {sd_y-17} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MicroSD" (at 220 {sd_y-14} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_Card:microSD_HC_Wuerth_693072010801" (at 220 {sd_y+15.24} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
    (pin "9" (uuid "{gen_uuid()}"))
  )

'''

    # User LEDs section - x=320, y=50
    led_y = 50
    led_refs = ["D7", "D8", "D9", "D10"]
    led_values = ["LED_USER0", "LED_USER1", "LED_USER2", "LED_USER3"]
    res_refs = ["R11", "R12", "R13", "R14"]

    for i in range(4):
        y_offset = led_y + i * 15

        # LED
        content += f'''  (symbol
    (lib_id "LED")
    (at 330 {y_offset} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{led_refs[i]}" (at 330 {y_offset-7} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{led_values[i]}" (at 330 {y_offset+7} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 330 {y_offset} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

        # Resistor
        content += f'''  (symbol
    (lib_id "R")
    (at 310 {y_offset} 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{res_refs[i]}" (at 310 {y_offset-5} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "470R" (at 310 {y_offset+5} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 310 {y_offset} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # User buttons - x=320, y=120
    btn_y = 120
    btn_refs = ["SW1", "SW2"]
    btn_values = ["BTN0", "BTN1"]

    for i in range(2):
        y_offset = btn_y + i * 20

        content += f'''  (symbol
    (lib_id "SW_Push")
    (at 330 {y_offset} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{btn_refs[i]}" (at 330 {y_offset-7} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{btn_values[i]}" (at 330 {y_offset+7} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Button_Switch_SMD:SW_SPST_TL3342" (at 330 {y_offset} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

    # ============ LABELS ============

    # CAN0 labels
    can_labels = [
        ("CAN0_TX", can_y - 3.81, 67),
        ("CAN0_RX", can_y - 1.27, 67),
        ("CAN0_H", can_y - 1.27, 93),
        ("CAN0_L", can_y - 3.81, 93),
    ]

    for name, y, x in can_labels:
        if x < 80:
            justify = "right"
            angle = 180
        else:
            justify = "left"
            angle = 0

        content += f'''  (label "{name}"
    (at {x} {y} {angle})
    (effects (font (size 1.27 1.27)) (justify {justify}))
    (uuid "{gen_uuid()}")
  )

'''

    # CAN0 connector labels
    content += f'''  (label "CAN0_H"
    (at 142 {can_y-1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN0_L"
    (at 142 {can_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # CAN1 labels
    content += f'''  (label "CAN1_TX"
    (at 67 {can1_y-3.81} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN1_RX"
    (at 67 {can1_y-1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN1_H"
    (at 93 {can1_y-1.27} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN1_L"
    (at 93 {can1_y-3.81} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN1_H"
    (at 142 {can1_y-1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "CAN1_L"
    (at 142 {can1_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # RS485 labels
    content += f'''  (label "RS485_0_RO"
    (at 67 {rs485_y-3.81} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_DI"
    (at 67 {rs485_y+3.81} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_DE"
    (at 67 {rs485_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_A"
    (at 93 {rs485_y+1.27} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_B"
    (at 93 {rs485_y-1.27} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_A"
    (at 142 {rs485_y-1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_0_B"
    (at 142 {rs485_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # RS485_1 labels
    content += f'''  (label "RS485_1_RO"
    (at 67 {rs485_1_y-3.81} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_DI"
    (at 67 {rs485_1_y+3.81} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_DE"
    (at 67 {rs485_1_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_A"
    (at 93 {rs485_1_y+1.27} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_B"
    (at 93 {rs485_1_y-1.27} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_A"
    (at 142 {rs485_1_y-1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "RS485_1_B"
    (at 142 {rs485_1_y+1.27} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # Debug UART labels
    content += f'''  (label "DEBUG_TXD"
    (at 235 {debug_y-10.16} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
    content += f'''  (label "DEBUG_RXD"
    (at 235 {debug_y-7.62} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

    # MicroSD labels
    sd_labels = [
        ("SD_DAT2", sd_y - 7.62),
        ("SD_DAT3", sd_y - 5.08),
        ("SD_CMD", sd_y - 2.54),
        ("SD_CLK", sd_y + 2.54),
        ("SD_DAT0", sd_y + 5.08),
        ("SD_DAT1", sd_y + 7.62),
    ]

    for name, y in sd_labels:
        content += f'''  (label "{name}"
    (at 207 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # User LED labels
    for i in range(4):
        y_offset = led_y + i * 15
        content += f'''  (label "USER_LED{i}"
    (at 303 {y_offset} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # Button labels
    for i in range(2):
        y_offset = btn_y + i * 20
        content += f'''  (label "USER_BTN{i}"
    (at 322 {y_offset} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ HIERARCHICAL LABELS ============
    hlabels = [
        # CAN
        ("CAN0_TX", 40),
        ("CAN0_RX", 43),
        ("CAN1_TX", 50),
        ("CAN1_RX", 53),
        # RS485
        ("RS485_0_RO", 60),
        ("RS485_0_DI", 63),
        ("RS485_0_DE", 66),
        ("RS485_1_RO", 73),
        ("RS485_1_DI", 76),
        ("RS485_1_DE", 79),
        # Debug UART
        ("DEBUG_TXD", 90),
        ("DEBUG_RXD", 93),
        # MicroSD
        ("SD_CMD", 100),
        ("SD_CLK", 103),
        ("SD_DAT0", 106),
        ("SD_DAT1", 109),
        ("SD_DAT2", 112),
        ("SD_DAT3", 115),
        # LEDs
        ("USER_LED0", 125),
        ("USER_LED1", 128),
        ("USER_LED2", 131),
        ("USER_LED3", 134),
        # Buttons
        ("USER_BTN0", 140),
        ("USER_BTN1", 143),
    ]

    for name, y in hlabels:
        content += f'''  (hierarchical_label "{name}"
    (shape bidirectional)
    (at 25 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # Close schematic
    content += '''  (symbol_instances
  )
)
'''

    return content


if __name__ == "__main__":
    output_path = r"D:\git2\fcBoardKicad\fcBoard_Peripherals.kicad_sch"

    content = create_peripherals_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {output_path}")
    print("Peripherals schematic with label-based connections created!")
