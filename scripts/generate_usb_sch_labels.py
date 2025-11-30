#!/usr/bin/env python3
"""
Generate USB schematic with label-based connections
Clean layout with symbols properly spaced, using labels instead of long wires
"""

import uuid

def gen_uuid():
    return str(uuid.uuid4())

def create_usb_schematic():
    """Create USB schematic with label connections"""

    # Header
    content = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "''' + gen_uuid() + '''")
  (paper "A3")
  (title_block
    (title "USB Subsystem")
    (company "fcBoard")
  )

  (lib_symbols
'''

    # USB3320 symbol definition
    content += '''    (symbol "USB3320" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB3320" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm" (at 0 -24.13 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB3320_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -22.86) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "USB3320_1_1"
        (pin bidirectional line (at -12.7 10.16 0) (length 2.54) (name "DATA0" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "DATA1" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 5.08 0) (length 2.54) (name "DATA2" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "DATA3" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 0 0) (length 2.54) (name "DATA4" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "DATA5" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -5.08 0) (length 2.54) (name "DATA6" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -7.62 0) (length 2.54) (name "DATA7" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 10.16 180) (length 2.54) (name "CLK" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 7.62 180) (length 2.54) (name "DIR" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 5.08 180) (length 2.54) (name "NXT" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin input line (at 12.7 2.54 180) (length 2.54) (name "STP" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "DP" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -5.08 180) (length 2.54) (name "DN" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -25.4 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -5.08 15.24 270) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 15.24 270) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 -12.7 0) (length 2.54) (name "REFCLK" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # USB5744 symbol definition
    content += '''    (symbol "USB5744" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 26.67 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB5744" (at 0 24.13 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm" (at 0 -30.48 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB5744_0_1"
        (rectangle (start -12.7 22.86) (end 12.7 -27.94) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "USB5744_1_1"
        (pin input line (at -15.24 20.32 0) (length 2.54) (name "CLK" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -15.24 17.78 0) (length 2.54) (name "DIR" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -15.24 15.24 0) (length 2.54) (name "NXT" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin output line (at -15.24 12.7 0) (length 2.54) (name "STP" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "DATA0" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "DATA1" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 2.54 0) (length 2.54) (name "DATA2" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 0 0) (length 2.54) (name "DATA3" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 -2.54 0) (length 2.54) (name "DATA4" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 -5.08 0) (length 2.54) (name "DATA5" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 -7.62 0) (length 2.54) (name "DATA6" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -15.24 -10.16 0) (length 2.54) (name "DATA7" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 20.32 180) (length 2.54) (name "DN1_DP" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 17.78 180) (length 2.54) (name "DN1_DN" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "DN2_DP" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "DN2_DN" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "DN3_DP" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DN3_DN" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DN4_DP" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 15.24 -5.08 180) (length 2.54) (name "DN4_DN" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -30.48 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -5.08 25.4 270) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 25.4 270) (length 2.54) (name "VDD12" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # TPD4S012 symbol definition
    content += '''    (symbol "TPD4S012" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPD4S012" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:UQFN-10_1.4x1.8mm_P0.4mm" (at 0 -10.16 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPD4S012_0_1"
        (rectangle (start -6.35 5.08) (end 6.35 -7.62) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "TPD4S012_1_1"
        (pin bidirectional line (at -8.89 2.54 0) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -8.89 0 0) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 8.89 2.54 180) (length 2.54) (name "D+_OUT" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 8.89 0 180) (length 2.54) (name "D-_OUT" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 7.62 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # TPS2041B symbol definition
    content += '''    (symbol "TPS2041B" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPS2041B" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 0 -10.16 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPS2041B_0_1"
        (rectangle (start -6.35 5.08) (end 6.35 -7.62) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "TPS2041B_1_1"
        (pin power_in line (at -8.89 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin power_out line (at 8.89 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -8.89 -2.54 0) (length 2.54) (name "EN" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin output line (at 8.89 -2.54 180) (length 2.54) (name "FAULT" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # USB_A symbol definition
    content += '''    (symbol "USB_A" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB_A" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_USB:USB_A_Stewart_SS-52100-001_Horizontal" (at 0 -10.16 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB_A_0_1"
        (rectangle (start -6.35 5.08) (end 6.35 -7.62) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "USB_A_1_1"
        (pin power_in line (at -8.89 2.54 0) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -8.89 0 0) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -8.89 -2.54 0) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 8.89 0 180) (length 2.54) (name "SHIELD" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
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
    (symbol "power:+5V" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (symbol "+5V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none))))
      (symbol "+5V_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
    (symbol "power:+1V8" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+1V8" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (symbol "+1V8_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none))))
      (symbol "+1V8_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide (name "+1V8" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
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
    # Layout: Left to right with good spacing
    # Row 1: USB3320 (x=50) -> USB5744 (x=130)
    # Row 2-5: TPD4S012 (x=220) -> TPS2041B (x=300) -> USB_A (x=380)

    # USB3320 at (50, 80)
    content += f'''  (symbol
    (lib_id "USB3320")
    (at 50 80 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U6" (at 50 61 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB3320" (at 50 63.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm" (at 50 104.13 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "13" (uuid "{gen_uuid()}"))
    (pin "14" (uuid "{gen_uuid()}"))
    (pin "15" (uuid "{gen_uuid()}"))
    (pin "16" (uuid "{gen_uuid()}"))
    (pin "17" (uuid "{gen_uuid()}"))
    (pin "18" (uuid "{gen_uuid()}"))
  )

'''

    # USB5744 at (130, 80)
    content += f'''  (symbol
    (lib_id "USB5744")
    (at 130 80 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U7" (at 130 51 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB5744" (at 130 53.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm" (at 130 110.48 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "13" (uuid "{gen_uuid()}"))
    (pin "14" (uuid "{gen_uuid()}"))
    (pin "15" (uuid "{gen_uuid()}"))
    (pin "16" (uuid "{gen_uuid()}"))
    (pin "17" (uuid "{gen_uuid()}"))
    (pin "18" (uuid "{gen_uuid()}"))
    (pin "19" (uuid "{gen_uuid()}"))
    (pin "20" (uuid "{gen_uuid()}"))
    (pin "21" (uuid "{gen_uuid()}"))
    (pin "22" (uuid "{gen_uuid()}"))
    (pin "23" (uuid "{gen_uuid()}"))
  )

'''

    # 4 downstream ports - TPD4S012, TPS2041B, USB_A
    port_y_positions = [50, 90, 130, 170]
    tpd_refs = ["U4", "U8", "U10", "U12"]
    tps_refs = ["U5", "U9", "U11", "U13"]
    usb_refs = ["J2", "J3", "J4", "J5"]

    for i, y in enumerate(port_y_positions):
        port_num = i + 1

        # TPD4S012 at x=220
        content += f'''  (symbol
    (lib_id "TPD4S012")
    (at 220 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{tpd_refs[i]}" (at 220 {y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD4S012" (at 220 {y-9.5} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:UQFN-10_1.4x1.8mm_P0.4mm" (at 220 {y+10.16} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
  )

'''

        # TPS2041B at x=300
        content += f'''  (symbol
    (lib_id "TPS2041B")
    (at 300 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{tps_refs[i]}" (at 300 {y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPS2041B" (at 300 {y-9.5} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 300 {y+10.16} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

'''

        # USB_A at x=380
        content += f'''  (symbol
    (lib_id "USB_A")
    (at 380 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{usb_refs[i]}" (at 380 {y-12} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 380 {y-9.5} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_A_Stewart_SS-52100-001_Horizontal" (at 380 {y+10.16} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

'''

    # ============ POWER SYMBOLS ============
    # +3V3 for USB3320
    content += f'''  (symbol
    (lib_id "power:+3V3")
    (at 45 62 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR01" (at 45 66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 45 58 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # +1V8 for USB3320
    content += f'''  (symbol
    (lib_id "power:+1V8")
    (at 55 62 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 55 66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 55 58 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # GND for USB3320
    content += f'''  (symbol
    (lib_id "power:GND")
    (at 50 108 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 50 114 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 50 112 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # +3V3 for USB5744
    content += f'''  (symbol
    (lib_id "power:+3V3")
    (at 125 52 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 125 56 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 125 48 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # GND for USB5744
    content += f'''  (symbol
    (lib_id "power:GND")
    (at 130 113 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR05" (at 130 119 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 130 117 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # Power symbols for each port
    pwr_idx = 6
    for i, y in enumerate(port_y_positions):
        # +3V3 for TPD
        content += f'''  (symbol
    (lib_id "power:+3V3")
    (at 220 {y-10} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{pwr_idx:02d}" (at 220 {y-6} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 220 {y-14} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''
        pwr_idx += 1

        # GND for TPD
        content += f'''  (symbol
    (lib_id "power:GND")
    (at 220 {y+12} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{pwr_idx:02d}" (at 220 {y+18} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220 {y+16} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''
        pwr_idx += 1

        # +5V for TPS input
        content += f'''  (symbol
    (lib_id "power:+5V")
    (at 289 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{pwr_idx:02d}" (at 289 {y+4} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 289 {y-4} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''
        pwr_idx += 1

        # GND for TPS
        content += f'''  (symbol
    (lib_id "power:GND")
    (at 300 {y+12} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{pwr_idx:02d}" (at 300 {y+18} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 300 {y+16} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''
        pwr_idx += 1

        # GND for USB_A
        content += f'''  (symbol
    (lib_id "power:GND")
    (at 380 {y+12} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{pwr_idx:02d}" (at 380 {y+18} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 380 {y+16} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''
        pwr_idx += 1

    # ============ LABELS ============
    # ULPI signals between USB3320 and USB5744
    ulpi_signals = ["ULPI_CLK", "ULPI_DIR", "ULPI_NXT", "ULPI_STP",
                    "ULPI_D0", "ULPI_D1", "ULPI_D2", "ULPI_D3",
                    "ULPI_D4", "ULPI_D5", "ULPI_D6", "ULPI_D7"]

    # USB3320 output side (right side)
    ulpi_usb3320_y = [69.84, 72.38, 74.92, 77.46]  # CLK, DIR, NXT, STP at pins 9-12
    for i, sig in enumerate(["ULPI_CLK", "ULPI_DIR", "ULPI_NXT", "ULPI_STP"]):
        content += f'''  (label "{sig}"
    (at 65 {ulpi_usb3320_y[i]} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

    # DATA0-7 on USB3320 left side
    ulpi_data_y = [69.84, 72.38, 74.92, 77.46, 80, 82.54, 85.08, 87.62]
    for i in range(8):
        content += f'''  (label "ULPI_D{i}"
    (at 35 {ulpi_data_y[i]} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # USB5744 input side (left side)
    usb5744_ulpi_y = [59.68, 62.22, 64.76, 67.3]  # CLK, DIR, NXT, STP
    for i, sig in enumerate(["ULPI_CLK", "ULPI_DIR", "ULPI_NXT", "ULPI_STP"]):
        content += f'''  (label "{sig}"
    (at 112 {usb5744_ulpi_y[i]} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # DATA0-7 on USB5744 left side
    usb5744_data_y = [72.38, 74.92, 77.46, 80, 82.54, 85.08, 87.62, 90.16]
    for i in range(8):
        content += f'''  (label "ULPI_D{i}"
    (at 112 {usb5744_data_y[i]} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # Downstream port signals - USB5744 to TPD4S012
    dn_y_offset = [59.68, 62.22, 67.3, 69.84, 74.92, 77.46, 82.54, 85.08]  # DN1_DP, DN1_DN, DN2_DP...
    for port in range(1, 5):
        dp_label = f"DN{port}_DP"
        dn_label = f"DN{port}_DN"

        # USB5744 output side
        content += f'''  (label "{dp_label}"
    (at 148 {dn_y_offset[(port-1)*2]} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "{dn_label}"
    (at 148 {dn_y_offset[(port-1)*2+1]} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

        # TPD4S012 input side
        tpd_y = port_y_positions[port-1]
        content += f'''  (label "{dp_label}"
    (at 208 {tpd_y-2.54} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "{dn_label}"
    (at 208 {tpd_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # TPD4S012 to USB_A (through TPS2041B for power)
    for port in range(1, 5):
        tpd_y = port_y_positions[port-1]
        dp_out_label = f"USB{port}_DP"
        dn_out_label = f"USB{port}_DN"
        vbus_label = f"USB{port}_VBUS"

        # TPD4S012 output side
        content += f'''  (label "{dp_out_label}"
    (at 232 {tpd_y-2.54} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "{dn_out_label}"
    (at 232 {tpd_y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

        # TPS2041B output (VBUS)
        content += f'''  (label "{vbus_label}"
    (at 312 {tpd_y-2.54} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

        # USB_A connector input side
        content += f'''  (label "{vbus_label}"
    (at 368 {tpd_y-2.54} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "{dn_out_label}"
    (at 368 {tpd_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "{dp_out_label}"
    (at 368 {tpd_y+2.54} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ SHORT WIRES FOR POWER ============
    # Wire from +3V3 to USB3320 VDD33
    content += f'''  (wire
    (pts (xy 45 62) (xy 45 64.76))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # Wire from +1V8 to USB3320 VDD18
    content += f'''  (wire
    (pts (xy 55 62) (xy 55 64.76))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # Wire from USB3320 GND
    content += f'''  (wire
    (pts (xy 50 105.4) (xy 50 108))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # Wire from +3V3 to USB5744 VDD33
    content += f'''  (wire
    (pts (xy 125 52) (xy 125 54.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # Wire from USB5744 GND
    content += f'''  (wire
    (pts (xy 130 110.48) (xy 130 113))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # Power wires for each port
    for i, y in enumerate(port_y_positions):
        # TPD VCC wire
        content += f'''  (wire
    (pts (xy 220 {y-7.62}) (xy 220 {y-10}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # TPD GND wire
        content += f'''  (wire
    (pts (xy 220 {y+10.16}) (xy 220 {y+12}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # TPS VIN wire
        content += f'''  (wire
    (pts (xy 289 {y}) (xy 291.11 {y-2.54}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # TPS GND wire
        content += f'''  (wire
    (pts (xy 300 {y+10.16}) (xy 300 {y+12}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # USB_A GND wire
        content += f'''  (wire
    (pts (xy 380 {y+10.16}) (xy 380 {y+12}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ HIERARCHICAL LABELS ============
    # ULPI interface to SoM
    hlabels = [
        ("ULPI_CLK", 25, 70, "input"),
        ("ULPI_DIR", 25, 73, "input"),
        ("ULPI_NXT", 25, 76, "input"),
        ("ULPI_STP", 25, 79, "output"),
        ("ULPI_D0", 25, 85, "bidirectional"),
        ("ULPI_D1", 25, 88, "bidirectional"),
        ("ULPI_D2", 25, 91, "bidirectional"),
        ("ULPI_D3", 25, 94, "bidirectional"),
        ("ULPI_D4", 25, 97, "bidirectional"),
        ("ULPI_D5", 25, 100, "bidirectional"),
        ("ULPI_D6", 25, 103, "bidirectional"),
        ("ULPI_D7", 25, 106, "bidirectional"),
    ]

    for name, x, y, shape in hlabels:
        content += f'''  (hierarchical_label "{name}"
    (shape {shape})
    (at {x} {y} 180)
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
    output_path = r"D:\git2\fcBoardKicad\fcBoard_USB.kicad_sch"

    content = create_usb_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {output_path}")
    print("USB schematic with label-based connections created!")
