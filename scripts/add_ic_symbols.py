#!/usr/bin/env python3
"""
Add IC Symbols to fcBoard.kicad_sym Library

Adds LM2596S-5, LM2596S-ADJ, USB5744, USB3320, RTL8211F,
IT6801FN, IT66121FN, MAX485, CP2102N IC symbols.
"""

from pathlib import Path

IC_SYMBOLS = '''
(symbol "LM2596S-5"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-5.0" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "5V 3A Step-Down Voltage Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM2596S-5_0_1"
        (rectangle (start -7.62 7.62) (end 7.62 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM2596S-5_1_1"
        (pin power_in line (at -10.16 5.08 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 5.08 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin output line (at 10.16 0 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 0 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "LM2596S-ADJ"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596S-ADJ" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Adjustable 3A Step-Down Voltage Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "LM2596S-ADJ_0_1"
        (rectangle (start -7.62 7.62) (end 7.62 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "LM2596S-ADJ_1_1"
        (pin power_in line (at -10.16 5.08 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 5.08 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 0 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 0 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "USB5744"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 33.02 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB5744" (at 0 -33.02 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB 3.0 4-Port Hub Controller" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB5744_0_1"
        (rectangle (start -12.7 30.48) (end 12.7 -30.48) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB5744_1_1"
        (pin power_in line (at -15.24 27.94 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 22.86 0) (length 2.54) (name "USB_DM_UP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 20.32 0) (length 2.54) (name "USB_DP_UP" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 15.24 0) (length 2.54) (name "SSRXM_UP" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 12.7 0) (length 2.54) (name "SSRXP_UP" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "SSTXM_UP" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "SSTXP_UP" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 0 0) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin output line (at -15.24 -2.54 0) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 -7.62 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 27.94 180) (length 2.54) (name "USB_DM_DN1" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 25.4 180) (length 2.54) (name "USB_DP_DN1" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 20.32 180) (length 2.54) (name "SSRXM_DN1" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 17.78 180) (length 2.54) (name "SSRXP_DN1" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "SSTXM_DN1" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "SSTXP_DN1" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "USB_DM_DN2" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "USB_DP_DN2" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "USB_DM_DN3" (effects (font (size 1.27 1.27)))) (number "31" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -5.08 180) (length 2.54) (name "USB_DP_DN3" (effects (font (size 1.27 1.27)))) (number "32" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -10.16 180) (length 2.54) (name "USB_DM_DN4" (effects (font (size 1.27 1.27)))) (number "41" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -12.7 180) (length 2.54) (name "USB_DP_DN4" (effects (font (size 1.27 1.27)))) (number "42" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -33.02 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "USB3320"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 20.32 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB3320" (at 0 -20.32 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB 2.0 Hi-Speed ULPI Transceiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "USB3320_0_1"
        (rectangle (start -10.16 17.78) (end 10.16 -17.78) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "USB3320_1_1"
        (pin power_in line (at -12.7 15.24 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 10.16 0) (length 2.54) (name "DP" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "DM" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 2.54 0) (length 2.54) (name "REFCLK" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -2.54 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 15.24 180) (length 2.54) (name "DATA0" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 12.7 180) (length 2.54) (name "DATA1" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 10.16 180) (length 2.54) (name "DATA2" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 7.62 180) (length 2.54) (name "DATA3" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 5.08 180) (length 2.54) (name "DATA4" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 2.54 180) (length 2.54) (name "DATA5" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 0 180) (length 2.54) (name "DATA6" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "DATA7" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -7.62 180) (length 2.54) (name "DIR" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -10.16 180) (length 2.54) (name "NXT" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -12.7 180) (length 2.54) (name "STP" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -15.24 180) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -20.32 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "RTL8211F"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 33.02 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RTL8211F-CG" (at 0 -33.02 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.3x5.3mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "Gigabit Ethernet PHY with RGMII" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "RTL8211F_0_1"
        (rectangle (start -12.7 30.48) (end 12.7 -30.48) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "RTL8211F_1_1"
        (pin power_in line (at -15.24 27.94 0) (length 2.54) (name "AVDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 22.86 0) (length 2.54) (name "TXD0" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 20.32 0) (length 2.54) (name "TXD1" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 17.78 0) (length 2.54) (name "TXD2" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 15.24 0) (length 2.54) (name "TXD3" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 10.16 0) (length 2.54) (name "TXCLK" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 7.62 0) (length 2.54) (name "TXCTL" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 27.94 180) (length 2.54) (name "RXD0" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 25.4 180) (length 2.54) (name "RXD1" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 22.86 180) (length 2.54) (name "RXD2" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 20.32 180) (length 2.54) (name "RXD3" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 15.24 180) (length 2.54) (name "RXCLK" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 12.7 180) (length 2.54) (name "RXCTL" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 7.62 180) (length 2.54) (name "MDC" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "MDIO" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 0 0) (length 2.54) (name "TX+" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -2.54 0) (length 2.54) (name "TX-" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -7.62 0) (length 2.54) (name "RX+" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -10.16 0) (length 2.54) (name "RX-" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 0 180) (length 2.54) (name "XTAL_IN" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -2.54 180) (length 2.54) (name "XTAL_OUT" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 -7.62 180) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -10.16 180) (length 2.54) (name "INT_N" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -33.02 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "IT6801FN"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT6801FN" (at 0 -30.48 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-100_14x14mm_P0.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "HDMI 1.4 Receiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "IT6801FN_0_1"
        (rectangle (start -12.7 27.94) (end 12.7 -27.94) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "IT6801FN_1_1"
        (pin power_in line (at -15.24 25.4 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 20.32 0) (length 2.54) (name "HDMI_D2+" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 17.78 0) (length 2.54) (name "HDMI_D2-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 12.7 0) (length 2.54) (name "HDMI_D1+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 10.16 0) (length 2.54) (name "HDMI_D1-" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "HDMI_D0+" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 2.54 0) (length 2.54) (name "HDMI_D0-" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -2.54 0) (length 2.54) (name "HDMI_CLK+" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -5.08 0) (length 2.54) (name "HDMI_CLK-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 25.4 180) (length 2.54) (name "VIDEO_D0" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 22.86 180) (length 2.54) (name "VIDEO_D1" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 5.08 180) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 0 180) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -5.08 180) (length 2.54) (name "INT_N" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -30.48 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "IT66121FN"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT66121FN" (at 0 -30.48 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-100_14x14mm_P0.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "HDMI 1.4 Transmitter" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "IT66121FN_0_1"
        (rectangle (start -12.7 27.94) (end 12.7 -27.94) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "IT66121FN_1_1"
        (pin power_in line (at -15.24 25.4 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 20.32 0) (length 2.54) (name "VIDEO_D0" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 17.78 0) (length 2.54) (name "VIDEO_D1" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 25.4 180) (length 2.54) (name "HDMI_D2+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 22.86 180) (length 2.54) (name "HDMI_D2-" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 17.78 180) (length 2.54) (name "HDMI_D1+" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 15.24 180) (length 2.54) (name "HDMI_D1-" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "HDMI_D0+" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 7.62 180) (length 2.54) (name "HDMI_D0-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "HDMI_CLK+" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 0 180) (length 2.54) (name "HDMI_CLK-" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 10.16 0) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -5.08 180) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 0 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin output line (at -15.24 -5.08 0) (length 2.54) (name "INT_N" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -30.48 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "MAX485"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX485" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "RS485 Transceiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "MAX485_0_1"
        (rectangle (start -7.62 7.62) (end 7.62 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "MAX485_1_1"
        (pin output line (at -10.16 5.08 0) (length 2.54) (name "RO" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 2.54 0) (length 2.54) (name "RE" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 0 0) (length 2.54) (name "DE" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "DI" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -10.16 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "B" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 10.16 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)

(symbol "CP2102N"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CP2102N" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Description" "USB to UART Bridge" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "CP2102N_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "CP2102N_1_1"
        (pin power_in line (at -12.7 10.16 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 5.08 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at -12.7 -2.54 0) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -7.62 0) (length 2.54) (name "RESET_N" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 10.16 180) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 7.62 180) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "RTS" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 0 180) (length 2.54) (name "CTS" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -2.54 180) (length 2.54) (name "DTR" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -5.08 180) (length 2.54) (name "DSR" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -15.24 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "GND" (effects (font (size 1.27 1.27)))))
    )
)
'''


def main():
    """Add IC symbols to fcBoard.kicad_sym library."""
    print("=" * 60)
    print("Adding IC Symbols to fcBoard.kicad_sym")
    print("=" * 60)

    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    lib_file = project_root / "libraries" / "fcBoard.kicad_sym"

    if not lib_file.exists():
        print(f"[ERROR] Library file not found: {lib_file}")
        return

    # Read current content
    content = lib_file.read_text(encoding='utf-8')

    # Check if symbols already exist
    if '"LM2596S-5"' in content and '"MAX485"' in content:
        print("[INFO] IC symbols already exist in library")
        return

    # Find the position before the final closing parenthesis
    content = content.rstrip()
    if content.endswith(')'):
        insert_pos = content.rfind(')')
        new_content = content[:insert_pos] + IC_SYMBOLS + "\n)"
    else:
        print("[ERROR] Unexpected file format")
        return

    # Write back
    lib_file.write_text(new_content, encoding='utf-8')

    print(f"[OK] Updated: {lib_file}")
    print()
    print("Added IC symbols:")
    print("  - Power: LM2596S-5, LM2596S-ADJ")
    print("  - USB: USB5744, USB3320, CP2102N")
    print("  - Ethernet: RTL8211F")
    print("  - HDMI: IT6801FN, IT66121FN")
    print("  - Interface: MAX485")


if __name__ == "__main__":
    main()
