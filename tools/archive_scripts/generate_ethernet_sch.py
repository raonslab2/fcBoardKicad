#!/usr/bin/env python3
"""
KiCad Gigabit Ethernet 회로도 생성 스크립트
RTL8211F-CG x2 (PS GEM3 + PL RGMII)
"""

import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def create_ethernet_schematic():
    """Ethernet 회로도 생성"""

    sch = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{main_uuid}")
  (paper "A3")
  (title_block
    (title "Gigabit Ethernet")
    (date "2024-11-30")
    (rev "0.1")
    (company "fcBoard Project")
    (comment 1 "Dual Port - RTL8211F-CG x2 (PS GEM3 + PL RGMII)")
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
    (symbol "Interface_Ethernet:RTL8211F" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 31.75 0) (effects (font (size 1.27 1.27))))
      (property "Value" "RTL8211F-CG" (at 0 29.21 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.realtek.com/en/component/zoo/category/rtl8211f-cg" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RTL8211F_0_1"
        (rectangle (start -17.78 27.94) (end 17.78 -27.94) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "RTL8211F_1_1"
        (pin power_in line (at -20.32 25.4 0) (length 2.54) (name "AVDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 22.86 0) (length 2.54) (name "DVDD33" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 20.32 0) (length 2.54) (name "DVDD10" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 -25.4 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 12.7 0) (length 2.54) (name "TXD0" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 10.16 0) (length 2.54) (name "TXD1" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 7.62 0) (length 2.54) (name "TXD2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 5.08 0) (length 2.54) (name "TXD3" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 0 0) (length 2.54) (name "TX_CLK" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 -5.08 0) (length 2.54) (name "TX_CTL" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 12.7 180) (length 2.54) (name "RXD0" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 10.16 180) (length 2.54) (name "RXD1" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 7.62 180) (length 2.54) (name "RXD2" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 5.08 180) (length 2.54) (name "RXD3" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 0 180) (length 2.54) (name "RX_CLK" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -5.08 180) (length 2.54) (name "RX_CTL" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 20.32 -12.7 180) (length 2.54) (name "MDIO" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -15.24 180) (length 2.54) (name "MDC" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -20.32 180) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -22.86 180) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -12.7 0) (length 2.54) (name "TXP" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -15.24 0) (length 2.54) (name "TXN" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -17.78 0) (length 2.54) (name "RXP" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -20.32 0) (length 2.54) (name "RXN" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Connector:RJ45_MagJack" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
      (property "Value" "RJ45_MagJack" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_RJ:RJ45_Pulse_JXD1-1000NL_Horizontal" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RJ45_MagJack_0_1"
        (rectangle (start -7.62 7.62) (end 7.62 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "RJ45_MagJack_1_1"
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "TX+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "TX-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 0 0) (length 2.54) (name "RX+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "RX-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 5.08 180) (length 2.54) (name "LED_G+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 2.54 180) (length 2.54) (name "LED_G-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 0 180) (length 2.54) (name "LED_Y+" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 -2.54 180) (length 2.54) (name "LED_Y-" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
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

    (symbol "Device:Ferrite_Bead" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "FB" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Ferrite_Bead" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.016 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Ferrite_Bead_0_1"
        (polyline (pts (xy -1.27 1.27) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (rectangle (start -1.016 -1.778) (end 1.016 1.778) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "Ferrite_Bead_1_1"
        (pin passive line (at 0 3.81 270) (length 2.032) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.032) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
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
    """컴포넌트 배치 - 2x RTL8211F PHY, 2x RJ45, Crystals"""

    components = f'''
  (symbol
    (lib_id "Interface_Ethernet:RTL8211F")
    (at 88.9 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U1" (at 88.9 41.91 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RTL8211F-CG" (at 88.9 44.45 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm" (at 88.9 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 88.9 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "24" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Interface_Ethernet:RTL8211F")
    (at 88.9 165.1 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U2" (at 88.9 130.81 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RTL8211F-CG" (at 88.9 133.35 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm" (at 88.9 165.1 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 88.9 165.1 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "24" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:RJ45_MagJack")
    (at 185.42 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J5" (at 185.42 60.96 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RJ45_MagJack" (at 185.42 63.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_RJ:RJ45_Pulse_JXD1-1000NL_Horizontal" (at 185.42 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 185.42 76.2 0) (effects (font (size 1.27 1.27)) hide))
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

  (symbol
    (lib_id "Connector:RJ45_MagJack")
    (at 185.42 165.1 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J6" (at 185.42 149.86 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RJ45_MagJack" (at 185.42 152.4 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_RJ:RJ45_Pulse_JXD1-1000NL_Horizontal" (at 185.42 165.1 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 185.42 165.1 0) (effects (font (size 1.27 1.27)) hide))
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

  (symbol
    (lib_id "Device:Crystal")
    (at 124.46 99.06 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "Y1" (at 124.46 93.98 0) (effects (font (size 1.27 1.27))))
    (property "Value" "25MHz" (at 124.46 104.14 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 124.46 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:Crystal")
    (at 124.46 187.96 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "Y2" (at 124.46 182.88 0) (effects (font (size 1.27 1.27))))
    (property "Value" "25MHz" (at 124.46 193.04 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 124.46 187.96 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 187.96 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 60.96 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C1" (at 63.5 54.61 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 63.5 57.15 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 61.9252 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 60.96 144.78 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C2" (at 63.5 143.51 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 63.5 146.05 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 61.9252 148.59 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 144.78 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 119.38 106.68 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C3" (at 121.92 105.41 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 121.92 107.95 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 120.3452 110.49 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 119.38 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 129.54 106.68 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C4" (at 132.08 105.41 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 132.08 107.95 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 130.5052 110.49 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 129.54 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 119.38 195.58 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C5" (at 121.92 194.31 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 121.92 196.85 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 120.3452 199.39 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 119.38 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 129.54 195.58 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C6" (at 132.08 194.31 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "22pF" (at 132.08 196.85 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 130.5052 199.39 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 129.54 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 116.84 63.5 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R1" (at 119.38 62.23 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "4.7K" (at 119.38 64.77 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 115.062 63.5 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 116.84 63.5 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 116.84 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R2" (at 119.38 151.13 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "4.7K" (at 119.38 153.67 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 115.062 152.4 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 116.84 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:Ferrite_Bead")
    (at 53.34 50.8 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "FB1" (at 55.88 49.53 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "600R@100MHz" (at 55.88 52.07 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Inductor_SMD:L_0402_1005Metric" (at 52.324 50.8 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:Ferrite_Bead")
    (at 53.34 139.7 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "FB2" (at 55.88 138.43 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "600R@100MHz" (at 55.88 140.97 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Inductor_SMD:L_0402_1005Metric" (at 52.324 139.7 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )
'''
    return components

def generate_wires():
    """와이어 연결"""

    wires = f'''
  (wire
    (pts (xy 68.58 50.8) (xy 60.96 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 60.96 50.8) (xy 60.96 52.07))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 53.34) (xy 60.96 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 60.96 53.34) (xy 60.96 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 63.5) (xy 50.8 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 66.04) (xy 50.8 66.04))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 68.58) (xy 50.8 68.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 71.12) (xy 50.8 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 76.2) (xy 50.8 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 81.28) (xy 50.8 81.28))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 63.5) (xy 116.84 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 116.84 63.5) (xy 116.84 59.69))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 60.96) (xy 124.46 60.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 55.88) (xy 124.46 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 55.88) (xy 124.46 96.52))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 109.22 53.34) (xy 127 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 127 53.34) (xy 127 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 121.92 99.06) (xy 119.38 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 99.06) (xy 119.38 102.87))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 127 99.06) (xy 129.54 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 129.54 99.06) (xy 129.54 102.87))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 63.5) (xy 68.58 88.9))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 68.58 88.9) (xy 156.21 88.9))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 156.21 88.9) (xy 156.21 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 156.21 71.12) (xy 175.26 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 66.04) (xy 68.58 91.44))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 68.58 91.44) (xy 158.75 91.44))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 158.75 91.44) (xy 158.75 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 158.75 73.66) (xy 175.26 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 93.98) (xy 161.29 93.98))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 161.29 93.98) (xy 161.29 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 161.29 76.2) (xy 175.26 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 96.52) (xy 163.83 96.52))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 163.83 96.52) (xy 163.83 78.74))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 163.83 78.74) (xy 175.26 78.74))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 139.7) (xy 60.96 139.7))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 60.96 139.7) (xy 60.96 140.97))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 142.24) (xy 60.96 142.24))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 60.96 142.24) (xy 60.96 139.7))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 152.4) (xy 50.8 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 154.94) (xy 50.8 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 157.48) (xy 50.8 157.48))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 160.02) (xy 50.8 160.02))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 165.1) (xy 50.8 165.1))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 170.18) (xy 50.8 170.18))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 152.4) (xy 116.84 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 116.84 152.4) (xy 116.84 148.59))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 149.86) (xy 124.46 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 144.78) (xy 124.46 144.78))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 144.78) (xy 124.46 185.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 109.22 142.24) (xy 127 142.24))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 127 142.24) (xy 127 187.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 121.92 187.96) (xy 119.38 187.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 187.96) (xy 119.38 191.77))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 127 187.96) (xy 129.54 187.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 129.54 187.96) (xy 129.54 191.77))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 152.4) (xy 68.58 177.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 68.58 177.8) (xy 156.21 177.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 156.21 177.8) (xy 156.21 160.02))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 156.21 160.02) (xy 175.26 160.02))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 154.94) (xy 68.58 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 68.58 180.34) (xy 158.75 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 158.75 180.34) (xy 158.75 162.56))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 158.75 162.56) (xy 175.26 162.56))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 182.88) (xy 161.29 182.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 161.29 182.88) (xy 161.29 165.1))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 161.29 165.1) (xy 175.26 165.1))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 185.42) (xy 163.83 185.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 163.83 185.42) (xy 163.83 167.64))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 163.83 167.64) (xy 175.26 167.64))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
'''
    return wires

def generate_labels():
    """라벨 및 계층 라벨"""

    labels = f'''
  (label "ETH1_TXD0"
    (at 50.8 63.5 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_TXD1"
    (at 50.8 66.04 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_TXD2"
    (at 50.8 68.58 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_TXD3"
    (at 50.8 71.12 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_TX_CLK"
    (at 50.8 76.2 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_TX_CTL"
    (at 50.8 81.28 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_MDIO"
    (at 124.46 60.96 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH1_MDC"
    (at 124.46 63.5 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TXD0"
    (at 50.8 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TXD1"
    (at 50.8 154.94 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TXD2"
    (at 50.8 157.48 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TXD3"
    (at 50.8 160.02 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TX_CLK"
    (at 50.8 165.1 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_TX_CTL"
    (at 50.8 170.18 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_MDIO"
    (at 124.46 149.86 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "ETH2_MDC"
    (at 124.46 152.4 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GEM3_TXD[0..3]"
    (shape output)
    (at 27.94 63.5 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GEM3_TX_CLK"
    (shape output)
    (at 27.94 76.2 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GEM3_MDIO"
    (shape bidirectional)
    (at 27.94 83.82 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GEM3_MDC"
    (shape output)
    (at 27.94 86.36 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "PL_ETH_TXD[0..3]"
    (shape output)
    (at 27.94 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "PL_ETH_TX_CLK"
    (shape output)
    (at 27.94 165.1 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "PL_ETH_MDIO"
    (shape bidirectional)
    (at 27.94 172.72 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "PL_ETH_MDC"
    (shape output)
    (at 27.94 175.26 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+3V3"
    (shape input)
    (at 27.94 38.1 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+1V8"
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
    (lib_id "power:+3V3")
    (at 27.94 38.1 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR01" (at 27.94 41.91 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 27.94 34.29 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 38.1 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 38.1 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 53.34 46.99 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 53.34 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 53.34 43.18 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 53.34 135.89 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 53.34 139.7 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 53.34 132.08 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 135.89 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 135.89 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 116.84 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 116.84 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 116.84 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 116.84 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 116.84 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 116.84 144.78 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR05" (at 116.84 148.59 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 116.84 140.97 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 116.84 144.78 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 116.84 144.78 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+1V8")
    (at 27.94 43.18 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR06" (at 27.94 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 27.94 39.37 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
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
    (property "Reference" "#PWR07" (at 27.94 54.61 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 27.94 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 60.96 59.69 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR08" (at 60.96 66.04 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 60.96 63.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 60.96 148.59 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR09" (at 60.96 154.94 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 60.96 152.4 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 148.59 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 148.59 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 68.58 101.6 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR010" (at 68.58 107.95 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 68.58 105.41 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 68.58 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 68.58 101.6 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 68.58 190.5 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR011" (at 68.58 196.85 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 68.58 194.31 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 68.58 190.5 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 68.58 190.5 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 124.46 114.3 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR012" (at 124.46 120.65 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 124.46 118.11 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 124.46 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 114.3 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 124.46 203.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR013" (at 124.46 209.55 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 124.46 207.01 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 124.46 203.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 203.2 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 195.58 81.28 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR014" (at 195.58 87.63 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 195.58 85.09 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 195.58 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 81.28 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 195.58 170.18 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR015" (at 195.58 176.53 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 195.58 173.99 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 195.58 170.18 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 170.18 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )
'''
    return power

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_path = os.path.join(project_dir, "fcBoard_Ethernet.kicad_sch")

    content = create_ethernet_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Ethernet schematic generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    main()
