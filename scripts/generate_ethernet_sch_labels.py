#!/usr/bin/env python3
"""
Generate Ethernet schematic with label-based connections
Clean layout with RTL8211F PHYs and RJ45 MagJack connectors
"""

import uuid

def gen_uuid():
    return str(uuid.uuid4())

def create_ethernet_schematic():
    """Create Ethernet schematic with label connections"""

    content = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "''' + gen_uuid() + '''")
  (paper "A3")
  (title_block
    (title "Dual Gigabit Ethernet")
    (company "fcBoard")
  )

  (lib_symbols
'''

    # RTL8211F-CG symbol definition
    content += '''    (symbol "RTL8211F-CG" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 31.75 0) (effects (font (size 1.27 1.27))))
      (property "Value" "RTL8211F-CG" (at 0 29.21 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm" (at 0 -35.56 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RTL8211F-CG_0_1"
        (rectangle (start -15.24 27.94) (end 15.24 -33.02) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "RTL8211F-CG_1_1"
        (pin bidirectional line (at -17.78 25.4 0) (length 2.54) (name "TXD0" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 22.86 0) (length 2.54) (name "TXD1" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 20.32 0) (length 2.54) (name "TXD2" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 17.78 0) (length 2.54) (name "TXD3" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin output line (at -17.78 12.7 0) (length 2.54) (name "TX_CLK" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 10.16 0) (length 2.54) (name "TX_EN" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "RXD0" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 2.54 0) (length 2.54) (name "RXD1" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 0 0) (length 2.54) (name "RXD2" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 -2.54 0) (length 2.54) (name "RXD3" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin output line (at -17.78 -7.62 0) (length 2.54) (name "RX_CLK" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin output line (at -17.78 -10.16 0) (length 2.54) (name "RX_DV" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 -15.24 0) (length 2.54) (name "MDC" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 -17.78 0) (length 2.54) (name "MDIO" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 25.4 180) (length 2.54) (name "TXP_A" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 22.86 180) (length 2.54) (name "TXN_A" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 17.78 180) (length 2.54) (name "TXP_B" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 15.24 180) (length 2.54) (name "TXN_B" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 10.16 180) (length 2.54) (name "TXP_C" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 7.62 180) (length 2.54) (name "TXN_C" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 2.54 180) (length 2.54) (name "TXP_D" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 0 180) (length 2.54) (name "TXN_D" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 -22.86 0) (length 2.54) (name "REFCLK" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -35.56 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "24" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -5.08 30.48 270) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "25" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 30.48 270) (length 2.54) (name "VDD10" (effects (font (size 1.016 1.016)))) (number "26" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # RJ45_MagJack symbol definition
    content += '''    (symbol "RJ45_MagJack" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "RJ45_MagJack" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_RJ:RJ45_Amphenol_RJHSE538X_Horizontal" (at 0 -20.32 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RJ45_MagJack_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -17.78) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "RJ45_MagJack_1_1"
        (pin input line (at -12.7 10.16 0) (length 2.54) (name "TXP_A" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 7.62 0) (length 2.54) (name "TXN_A" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 5.08 0) (length 2.54) (name "TXP_B" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 2.54 0) (length 2.54) (name "TXN_B" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 0 0) (length 2.54) (name "TXP_C" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 -2.54 0) (length 2.54) (name "TXN_C" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 -5.08 0) (length 2.54) (name "TXP_D" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin input line (at -12.7 -7.62 0) (length 2.54) (name "TXN_D" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 5.08 180) (length 2.54) (name "LED_G+" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "LED_G-" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 -2.54 180) (length 2.54) (name "LED_Y+" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 -5.08 180) (length 2.54) (name "LED_Y-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # Crystal symbol
    content += '''    (symbol "Crystal" (in_bom yes) (on_board yes)
      (property "Reference" "Y" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Value" "25MHz" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 0 -7.62 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Crystal_0_1"
        (rectangle (start -1.27 2.54) (end 1.27 -2.54) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.54 -1.27) (xy -2.54 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 -1.27) (xy 2.54 1.27)) (stroke (width 0.254) (type default)) (fill (type none))))
      (symbol "Crystal_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016))))))
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
    # Layout: Two rows for two Ethernet ports
    # ETH1: RTL8211F (x=80) -> RJ45 (x=220)
    # ETH2: RTL8211F (x=80, y+80) -> RJ45 (x=220, y+80)

    eth_y = [70, 150]  # Two Ethernet ports

    for i, y in enumerate(eth_y):
        eth_num = i + 1
        phy_ref = f"U{14 + i}"
        rj45_ref = f"J{6 + i}"
        crystal_ref = f"Y{i + 1}"

        # RTL8211F-CG
        content += f'''  (symbol
    (lib_id "RTL8211F-CG")
    (at 80 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{phy_ref}" (at 80 {y-35} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RTL8211F-CG" (at 80 {y-32} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm" (at 80 {y+35.56} 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "25" (uuid "{gen_uuid()}"))
    (pin "26" (uuid "{gen_uuid()}"))
  )

'''

        # RJ45_MagJack
        content += f'''  (symbol
    (lib_id "RJ45_MagJack")
    (at 220 {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{rj45_ref}" (at 220 {y-20} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RJ45_MagJack" (at 220 {y-17} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_RJ:RJ45_Amphenol_RJHSE538X_Horizontal" (at 220 {y+20.32} 0) (effects (font (size 1.27 1.27)) hide))
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
  )

'''

        # Crystal 25MHz
        content += f'''  (symbol
    (lib_id "Crystal")
    (at 50 {y+30} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "{crystal_ref}" (at 50 {y+23} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "25MHz" (at 50 {y+37} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 50 {y+37.62} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

'''

        # Power symbols
        # +3V3 for RTL8211F
        content += f'''  (symbol
    (lib_id "power:+3V3")
    (at 75 {y-33} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{i*4+1:02d}" (at 75 {y-29} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 75 {y-37} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

        # GND for RTL8211F
        content += f'''  (symbol
    (lib_id "power:GND")
    (at 80 {y+38} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{i*4+2:02d}" (at 80 {y+44} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 80 {y+42} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

        # GND for RJ45
        content += f'''  (symbol
    (lib_id "power:GND")
    (at 220 {y+23} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR{i*4+3:02d}" (at 220 {y+29} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 220 {y+27} 0) (effects (font (size 1.27 1.27))))
    (pin "1" (uuid "{gen_uuid()}"))
  )

'''

    # ============ LABELS ============
    # RGMII interface labels for each Ethernet port
    for i, y in enumerate(eth_y):
        eth_num = i + 1

        # RGMII TX signals (left side of RTL8211F - going to SoM)
        rgmii_tx_labels = [
            (f"ETH{eth_num}_TXD0", y - 25.4),
            (f"ETH{eth_num}_TXD1", y - 22.86),
            (f"ETH{eth_num}_TXD2", y - 20.32),
            (f"ETH{eth_num}_TXD3", y - 17.78),
            (f"ETH{eth_num}_TX_CLK", y - 12.7),
            (f"ETH{eth_num}_TX_EN", y - 10.16),
        ]

        for label_name, label_y in rgmii_tx_labels:
            content += f'''  (label "{label_name}"
    (at 60 {label_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

        # RGMII RX signals
        rgmii_rx_labels = [
            (f"ETH{eth_num}_RXD0", y - 5.08),
            (f"ETH{eth_num}_RXD1", y - 2.54),
            (f"ETH{eth_num}_RXD2", y),
            (f"ETH{eth_num}_RXD3", y + 2.54),
            (f"ETH{eth_num}_RX_CLK", y + 7.62),
            (f"ETH{eth_num}_RX_DV", y + 10.16),
        ]

        for label_name, label_y in rgmii_rx_labels:
            content += f'''  (label "{label_name}"
    (at 60 {label_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

        # MDC/MDIO
        content += f'''  (label "ETH{eth_num}_MDC"
    (at 60 {y + 15.24} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''
        content += f'''  (label "ETH{eth_num}_MDIO"
    (at 60 {y + 17.78} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

        # MDI signals (right side of RTL8211F to RJ45)
        mdi_pairs = ["A", "B", "C", "D"]
        mdi_y_offsets = [(-25.4, -22.86), (-17.78, -15.24), (-10.16, -7.62), (-2.54, 0)]

        for j, pair in enumerate(mdi_pairs):
            txp_y = y + mdi_y_offsets[j][0]
            txn_y = y + mdi_y_offsets[j][1]

            # RTL8211F output side
            content += f'''  (label "ETH{eth_num}_MDI{pair}P"
    (at 100 {txp_y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
            content += f'''  (label "ETH{eth_num}_MDI{pair}N"
    (at 100 {txn_y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

        # RJ45 input side
        rj45_y_offsets = [10.16, 7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]
        mdi_signals = ["MDIAP", "MDIAN", "MDIBP", "MDIBN", "MDICP", "MDICN", "MDIDP", "MDIDN"]

        for j, sig in enumerate(mdi_signals):
            label_y = y - rj45_y_offsets[j]
            content += f'''  (label "ETH{eth_num}_{sig}"
    (at 205 {label_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ HIERARCHICAL LABELS ============
    for i, y in enumerate(eth_y):
        eth_num = i + 1
        hlabel_y = y - 30

        hlabels = [
            (f"ETH{eth_num}_TXD0", hlabel_y),
            (f"ETH{eth_num}_TXD1", hlabel_y + 3),
            (f"ETH{eth_num}_TXD2", hlabel_y + 6),
            (f"ETH{eth_num}_TXD3", hlabel_y + 9),
            (f"ETH{eth_num}_TX_CLK", hlabel_y + 14),
            (f"ETH{eth_num}_TX_EN", hlabel_y + 17),
            (f"ETH{eth_num}_RXD0", hlabel_y + 22),
            (f"ETH{eth_num}_RXD1", hlabel_y + 25),
            (f"ETH{eth_num}_RXD2", hlabel_y + 28),
            (f"ETH{eth_num}_RXD3", hlabel_y + 31),
            (f"ETH{eth_num}_RX_CLK", hlabel_y + 36),
            (f"ETH{eth_num}_RX_DV", hlabel_y + 39),
            (f"ETH{eth_num}_MDC", hlabel_y + 44),
            (f"ETH{eth_num}_MDIO", hlabel_y + 47),
        ]

        for name, label_y in hlabels:
            content += f'''  (hierarchical_label "{name}"
    (shape bidirectional)
    (at 30 {label_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ POWER WIRES ============
    for i, y in enumerate(eth_y):
        # +3V3 to RTL8211F VDD33
        content += f'''  (wire
    (pts (xy 75 {y-33}) (xy 75 {y-30.48}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # GND for RTL8211F
        content += f'''  (wire
    (pts (xy 80 {y+35.56}) (xy 80 {y+38}))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

'''
        # GND for RJ45
        content += f'''  (wire
    (pts (xy 220 {y+20.32}) (xy 220 {y+23}))
    (stroke (width 0) (type default))
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
    output_path = r"D:\git2\fcBoardKicad\fcBoard_Ethernet.kicad_sch"

    content = create_ethernet_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {output_path}")
    print("Ethernet schematic with label-based connections created!")
