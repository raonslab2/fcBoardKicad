#!/usr/bin/env python3
"""
KiCad USB 3.0 Hub 회로도 생성 스크립트
USB5744 4-Port Hub + USB3320 ULPI PHY
"""

import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def create_usb_schematic():
    """USB 회로도 생성"""

    sch = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{main_uuid}")
  (paper "A3")
  (title_block
    (title "USB 3.0 Hub")
    (date "2024-11-30")
    (rev "0.1")
    (company "fcBoard Project")
    (comment 1 "USB5744 4-Port USB 3.0 Hub + USB3320 ULPI PHY")
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

    lib_symbols = generate_lib_symbols()
    components = generate_components()
    wires = generate_wires()
    labels = generate_labels()
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
    (symbol "Interface_USB:USB5744" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 26.67 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB5744" (at 0 24.13 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.microchip.com/USB5744" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB5744_0_1"
        (rectangle (start -15.24 22.86) (end 15.24 -22.86) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "USB5744_1_1"
        (pin input line (at -17.78 20.32 0) (length 2.54) (name "VBUS_DET" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -17.78 17.78 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 12.7 0) (length 2.54) (name "USB_DN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 10.16 0) (length 2.54) (name "USB_DP" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "SS_RX_N" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 2.54 0) (length 2.54) (name "SS_RX_P" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 -2.54 0) (length 2.54) (name "SS_TX_N" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -17.78 -5.08 0) (length 2.54) (name "SS_TX_P" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -17.78 -10.16 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 20.32 180) (length 2.54) (name "DN1_DN" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 17.78 180) (length 2.54) (name "DN1_DP" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 12.7 180) (length 2.54) (name "DN2_DN" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 10.16 180) (length 2.54) (name "DN2_DP" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 5.08 180) (length 2.54) (name "DN3_DN" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 2.54 180) (length 2.54) (name "DN3_DP" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 -2.54 180) (length 2.54) (name "DN4_DN" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 -5.08 180) (length 2.54) (name "DN4_DP" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin input line (at 17.78 -10.16 180) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 -12.7 180) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Interface_USB:USB3320" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 21.59 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB3320" (at 0 19.05 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.microchip.com/USB3320" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB3320_0_1"
        (rectangle (start -12.7 17.78) (end 12.7 -17.78) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "USB3320_1_1"
        (pin power_in line (at -15.24 15.24 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 12.7 0) (length 2.54) (name "VDD18" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "DP" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "DM" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 -15.24 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 15.24 180) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 12.7 180) (length 2.54) (name "DIR" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 10.16 180) (length 2.54) (name "STP" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 7.62 180) (length 2.54) (name "NXT" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DATA0" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 0 180) (length 2.54) (name "DATA1" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DATA2" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -5.08 180) (length 2.54) (name "DATA3" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -7.62 180) (length 2.54) (name "DATA4" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -10.16 180) (length 2.54) (name "DATA5" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -12.7 180) (length 2.54) (name "DATA6" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -15.24 180) (length 2.54) (name "DATA7" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Connector:USB_A" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB_A" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB_A_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "USB_A_1_1"
        (pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 7.62 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Power_Protection:TPD4S012" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPD4S012" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.ti.com/lit/ds/symlink/tpd4s012.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPD4S012_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "TPD4S012_1_1"
        (pin passive line (at -7.62 2.54 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -7.62 0 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "D+_OUT" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 0 180) (length 2.54) (name "D-_OUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Power_Management:TPS2041" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPS2041" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.ti.com/lit/ds/symlink/tps2041.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPS2041_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "TPS2041_1_1"
        (pin power_in line (at -7.62 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -7.62 0 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 7.62 -2.54 180) (length 2.54) (name "OC" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:Crystal" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "Y" (at 0 3.175 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Crystal_0_1"
        (rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.524 -1.778) (xy -1.524 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.524 -1.778) (xy 1.524 1.778)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "Crystal_1_1"
        (pin passive line (at -2.54 0 0) (length 1.016) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 0 180) (length 1.016) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
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
'''
    return symbols

def generate_components():
    """컴포넌트 배치 - USB3320 ULPI PHY, USB5744 Hub, USB Connectors, ESD Protection"""

    components = f'''
  (symbol
    (lib_id "Interface_USB:USB3320")
    (at 63.5 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U2" (at 63.5 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB3320" (at 63.5 54.61 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm" (at 63.5 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 63.5 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
  )

  (symbol
    (lib_id "Interface_USB:USB5744")
    (at 165.1 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U1" (at 165.1 46.99 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB5744" (at 165.1 49.53 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm" (at 165.1 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 165.1 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
  )

  (symbol
    (lib_id "Device:Crystal")
    (at 195.58 91.44 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "Y1" (at 195.58 86.36 0) (effects (font (size 1.27 1.27))))
    (property "Value" "24MHz" (at 195.58 96.52 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 195.58 91.44 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 91.44 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:USB_A")
    (at 266.7 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J1" (at 266.7 45.72 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 266.7 48.26 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal" (at 266.7 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 266.7 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:USB_A")
    (at 266.7 83.82 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J2" (at 266.7 73.66 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 266.7 76.2 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal" (at 266.7 83.82 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 266.7 83.82 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:USB_A")
    (at 266.7 111.76 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J3" (at 266.7 101.6 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 266.7 104.14 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal" (at 266.7 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 266.7 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:USB_A")
    (at 266.7 139.7 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J4" (at 266.7 129.54 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_A" (at 266.7 132.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_A_Molex_105057_Horizontal" (at 266.7 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 266.7 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Management:TPS2041")
    (at 228.6 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U3" (at 228.6 44.45 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPS2041" (at 228.6 46.99 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 228.6 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 228.6 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Management:TPS2041")
    (at 228.6 83.82 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U4" (at 228.6 72.39 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPS2041" (at 228.6 74.93 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 228.6 83.82 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 228.6 83.82 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Management:TPS2041")
    (at 228.6 111.76 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U5" (at 228.6 100.33 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPS2041" (at 228.6 102.87 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 228.6 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 228.6 111.76 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Management:TPS2041")
    (at 228.6 139.7 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U6" (at 228.6 128.27 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPS2041" (at 228.6 130.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 228.6 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 228.6 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Protection:TPD4S012")
    (at 246.38 58.42 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U7" (at 246.38 46.99 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD4S012" (at 246.38 49.53 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm" (at 246.38 58.42 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 246.38 58.42 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Protection:TPD4S012")
    (at 246.38 86.36 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U8" (at 246.38 74.93 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD4S012" (at 246.38 77.47 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm" (at 246.38 86.36 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 246.38 86.36 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Protection:TPD4S012")
    (at 246.38 114.3 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U9" (at 246.38 102.87 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD4S012" (at 246.38 105.41 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm" (at 246.38 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 246.38 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Power_Protection:TPD4S012")
    (at 246.38 142.24 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U10" (at 246.38 130.81 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD4S012" (at 246.38 133.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SON:USON-10_2.5x1mm_P0.5mm" (at 246.38 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 246.38 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 45.72 63.5 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C1" (at 48.26 62.23 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 48.26 64.77 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 46.6852 67.31 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 45.72 63.5 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 45.72 73.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C2" (at 48.26 72.39 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "10uF" (at 48.26 74.93 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0805_2012Metric" (at 46.6852 77.47 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 45.72 73.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 139.7 63.5 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C3" (at 142.24 62.23 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 142.24 64.77 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 140.6652 67.31 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 63.5 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 139.7 73.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C4" (at 142.24 72.39 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "10uF" (at 142.24 74.93 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0805_2012Metric" (at 140.6652 77.47 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 73.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 190.5 99.06 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C5" (at 193.04 97.79 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 193.04 100.33 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 191.4652 102.87 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 190.5 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 200.66 99.06 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C6" (at 203.2 97.79 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 203.2 100.33 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 201.6252 102.87 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 200.66 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )
'''
    return components

def generate_wires():
    """와이어 연결"""

    wires = f'''
  (wire
    (pts (xy 78.74 60.96) (xy 88.9 60.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 88.9 60.96) (xy 88.9 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 63.5) (xy 91.44 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 68.58) (xy 91.44 68.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 73.66) (xy 91.44 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 76.2) (xy 91.44 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 78.74) (xy 91.44 78.74))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 81.28) (xy 91.44 81.28))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 83.82) (xy 91.44 83.82))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 86.36) (xy 91.44 86.36))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 88.9) (xy 91.44 88.9))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 78.74 91.44) (xy 91.44 91.44))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 147.32 55.88) (xy 139.7 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 139.7 55.88) (xy 139.7 59.69))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 147.32 63.5) (xy 127 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 127 63.5) (xy 127 68.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 147.32 66.04) (xy 124.46 66.04))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 66.04) (xy 124.46 83.82))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 55.88) (xy 190.5 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 190.5 55.88) (xy 190.5 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 58.42) (xy 195.58 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 63.5) (xy 200.66 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 66.04) (xy 205.74 66.04))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 71.12) (xy 210.82 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 73.66) (xy 210.82 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 78.74) (xy 210.82 78.74))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 81.28) (xy 210.82 81.28))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 86.36) (xy 193.04 86.36))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 193.04 86.36) (xy 193.04 91.44))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 88.9) (xy 198.12 88.9))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 198.12 88.9) (xy 198.12 91.44))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 236.22 53.34) (xy 238.76 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 238.76 53.34) (xy 238.76 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 55.88) (xy 259.08 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 58.42) (xy 259.08 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 236.22 81.28) (xy 238.76 81.28))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 238.76 81.28) (xy 238.76 83.82))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 83.82) (xy 259.08 83.82))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 86.36) (xy 259.08 86.36))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 236.22 109.22) (xy 238.76 109.22))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 238.76 109.22) (xy 238.76 111.76))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 111.76) (xy 259.08 111.76))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 114.3) (xy 259.08 114.3))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 236.22 137.16) (xy 238.76 137.16))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 238.76 137.16) (xy 238.76 139.7))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 139.7) (xy 259.08 139.7))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 253.96 142.24) (xy 259.08 142.24))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
'''
    return wires

def generate_labels():
    """라벨 및 계층 라벨"""

    labels = f'''
  (label "USB_CLK"
    (at 88.9 60.96 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DIR"
    (at 88.9 63.5 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_STP"
    (at 88.9 68.58 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_NXT"
    (at 88.9 73.66 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA0"
    (at 88.9 76.2 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA1"
    (at 88.9 78.74 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA2"
    (at 88.9 81.28 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA3"
    (at 88.9 83.82 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA4"
    (at 88.9 86.36 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA5"
    (at 88.9 88.9 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "USB_DATA6"
    (at 88.9 91.44 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USB_CLK"
    (shape output)
    (at 27.94 60.96 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USB_DIR"
    (shape output)
    (at 27.94 63.5 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USB_STP"
    (shape input)
    (at 27.94 68.58 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USB_NXT"
    (shape output)
    (at 27.94 73.66 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USB_DATA[0..7]"
    (shape bidirectional)
    (at 27.94 78.74 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+5V"
    (shape input)
    (at 27.94 38.1 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+3V3"
    (shape input)
    (at 27.94 43.18 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GND"
    (shape passive)
    (at 27.94 48.26 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )
'''
    return labels

def generate_power_symbols():
    """전원 심볼"""

    power = f'''
  (symbol
    (lib_id "power:+5V")
    (at 27.94 38.1 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR01" (at 27.94 41.91 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 27.94 34.29 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 38.1 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 38.1 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+5V")
    (at 220.98 53.34 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 220.98 57.15 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 220.98 49.53 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 53.34 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 53.34 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+5V")
    (at 220.98 81.28 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 220.98 85.09 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 220.98 77.47 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+5V")
    (at 220.98 109.22 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 220.98 113.03 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 220.98 105.41 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 109.22 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 109.22 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+5V")
    (at 220.98 137.16 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR05" (at 220.98 140.97 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 220.98 133.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 137.16 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 137.16 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 27.94 43.18 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR06" (at 27.94 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 27.94 39.37 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 45.72 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR07" (at 45.72 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 45.72 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 45.72 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 45.72 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 139.7 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR08" (at 139.7 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 139.7 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 139.7 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 27.94 48.26 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR09" (at 27.94 54.61 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 27.94 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 45.72 81.28 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR010" (at 45.72 87.63 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 45.72 85.09 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 45.72 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 45.72 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 139.7 81.28 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR011" (at 139.7 87.63 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 139.7 85.09 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 139.7 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 195.58 106.68 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR012" (at 195.58 113.03 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 195.58 110.49 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 195.58 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 220.98 58.42 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR013" (at 220.98 64.77 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220.98 62.23 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 58.42 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 58.42 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 220.98 86.36 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR014" (at 220.98 92.71 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220.98 90.17 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 86.36 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 86.36 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 220.98 114.3 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR015" (at 220.98 120.65 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220.98 118.11 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 220.98 142.24 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR016" (at 220.98 148.59 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220.98 146.05 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 220.98 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220.98 142.24 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 274.32 60.96 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR017" (at 274.32 67.31 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 274.32 64.77 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 274.32 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 274.32 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 274.32 88.9 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR018" (at 274.32 95.25 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 274.32 92.71 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 274.32 88.9 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 274.32 88.9 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 274.32 116.84 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR019" (at 274.32 123.19 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 274.32 120.65 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 274.32 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 274.32 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 274.32 144.78 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR020" (at 274.32 151.13 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 274.32 148.59 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 274.32 144.78 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 274.32 144.78 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )
'''
    return power

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_path = os.path.join(project_dir, "fcBoard_USB.kicad_sch")

    content = create_usb_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"USB schematic generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    main()
