"""
Interface Symbols - 인터페이스 IC 심볼

USB 허브, UART-USB 변환기, 이더넷 PHY 등 인터페이스 IC 심볼
"""

from ..base import SymbolCategory

# 인터페이스 IC 심볼 정의 (KiCad 8 포맷)
INTERFACE_SYMBOLS = {
    "CH340G": '''(symbol "CH340G"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CH340G" (at 0 11.43 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOP-16_3.9x9.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "CH340G_0_1"
        (rectangle (start -10.16 10.16) (end 10.16 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "CH340G_1_1"
        (pin power_in line (at -12.7 7.62 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 7.62 180) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 5.08 180) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "V3" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "UD+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 0 0) (length 2.54) (name "UD-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -5.08 0) (length 2.54) (name "XI" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at -12.7 -7.62 0) (length 2.54) (name "XO" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "CTS" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 0 180) (length 2.54) (name "DSR" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -2.54 180) (length 2.54) (name "RI" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -5.08 180) (length 2.54) (name "DCD" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -7.62 180) (length 2.54) (name "DTR" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -10.16 180) (length 2.54) (name "RTS" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at -12.7 5.08 0) (length 2.54) (name "R232" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 12.7 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
    )
)''',

    "CP2102": '''(symbol "CP2102"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 17.78 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CP2102" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "CP2102_0_1"
        (rectangle (start -10.16 13.97) (end 10.16 -13.97) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "CP2102_1_1"
        (pin power_in line (at -12.7 11.43 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -12.7 8.89 0) (length 2.54) (name "REGIN" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at -12.7 6.35 0) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 3.81 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 1.27 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -16.51 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 11.43 180) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 8.89 180) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 6.35 180) (length 2.54) (name "RTS" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 3.81 180) (length 2.54) (name "CTS" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 1.27 180) (length 2.54) (name "DTR" (effects (font (size 1.27 1.27)))) (number "27" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -1.27 180) (length 2.54) (name "DSR" (effects (font (size 1.27 1.27)))) (number "26" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -1.27 0) (length 2.54) (name "RST" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -3.81 0) (length 2.54) (name "SUSPEND" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at -12.7 -6.35 0) (length 2.54) (name "SUSPENDBAR" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
    )
)''',

    "FT232RL": '''(symbol "FT232RL"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
    (property "Value" "FT232RL" (at 0 20.32 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SSOP-28_5.3x10.2mm_P0.65mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "FT232RL_0_1"
        (rectangle (start -12.7 19.05) (end 12.7 -19.05) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "FT232RL_1_1"
        (pin output line (at 15.24 16.51 180) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 13.97 180) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 11.43 180) (length 2.54) (name "RTS" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 8.89 180) (length 2.54) (name "CTS" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 6.35 180) (length 2.54) (name "DTR" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 3.81 180) (length 2.54) (name "DSR" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 1.27 180) (length 2.54) (name "DCD" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 -1.27 180) (length 2.54) (name "RI" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 16.51 0) (length 2.54) (name "USBDP" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 13.97 0) (length 2.54) (name "USBDM" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 11.43 0) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 8.89 0) (length 2.54) (name "VCCIO" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at -15.24 6.35 0) (length 2.54) (name "3V3OUT" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -21.59 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 1.27 0) (length 2.54) (name "RESET" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin output line (at -15.24 -1.27 0) (length 2.54) (name "OSCO" (effects (font (size 1.27 1.27)))) (number "27" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 -3.81 0) (length 2.54) (name "OSCI" (effects (font (size 1.27 1.27)))) (number "28" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -3.81 180) (length 2.54) (name "TXLED" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -6.35 180) (length 2.54) (name "RXLED" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -8.89 180) (length 2.54) (name "PWREN" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -11.43 180) (length 2.54) (name "TXDEN" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -13.97 180) (length 2.54) (name "SLEEP" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at -15.24 -6.35 0) (length 2.54) (name "TEST" (effects (font (size 1.27 1.27)))) (number "26" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 15.24 -16.51 180) (length 2.54) (name "CBUS0" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -8.89 0) (length 2.54) (name "CBUS1" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -11.43 0) (length 2.54) (name "CBUS2" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -13.97 0) (length 2.54) (name "CBUS3" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -15.24 -16.51 0) (length 2.54) (name "CBUS4" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
    )
)''',

    "MAX232": '''(symbol "MAX232"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX232" (at 0 11.43 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "MAX232_0_1"
        (rectangle (start -10.16 10.16) (end 10.16 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "MAX232_1_1"
        (pin passive line (at -12.7 7.62 0) (length 2.54) (name "C1+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at -12.7 5.08 0) (length 2.54) (name "VS+" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -12.7 2.54 0) (length 2.54) (name "C1-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -12.7 0 0) (length 2.54) (name "C2+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -12.7 -2.54 0) (length 2.54) (name "C2-" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at -12.7 -5.08 0) (length 2.54) (name "VS-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 7.62 180) (length 2.54) (name "T2OUT" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 5.08 180) (length 2.54) (name "R2IN" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "R2OUT" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 0 180) (length 2.54) (name "T2IN" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -2.54 180) (length 2.54) (name "T1IN" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -5.08 180) (length 2.54) (name "R1OUT" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -7.62 180) (length 2.54) (name "R1IN" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -10.16 180) (length 2.54) (name "T1OUT" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 12.7 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
    )
)''',

    "SN65HVD230": '''(symbol "SN65HVD230"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN65HVD230" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "SN65HVD230_0_1"
        (rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "SN65HVD230_1_1"
        (pin input line (at -10.16 3.81 0) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin output line (at -10.16 1.27 0) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -1.27 0) (length 2.54) (name "RS" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 1.27 180) (length 2.54) (name "CANL" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 3.81 180) (length 2.54) (name "CANH" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -3.81 0) (length 2.54) (name "Vref" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
    )
)''',

    "MCP2515": '''(symbol "MCP2515"
    (pin_names (offset 1.016))
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (property "Reference" "U" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MCP2515" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
    (symbol "MCP2515_0_1"
        (rectangle (start -10.16 11.43) (end 10.16 -11.43) (stroke (width 0.254) (type default)) (fill (type background)))
    )
    (symbol "MCP2515_1_1"
        (pin output line (at 12.7 8.89 180) (length 2.54) (name "TXCAN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 6.35 180) (length 2.54) (name "RXCAN" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 8.89 0) (length 2.54) (name "CLKOUT/SOF" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 6.35 0) (length 2.54) (name "TX0RTS" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 3.81 0) (length 2.54) (name "TX1RTS" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 1.27 0) (length 2.54) (name "TX2RTS" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -1.27 0) (length 2.54) (name "OSC2" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at -12.7 -3.81 0) (length 2.54) (name "OSC1" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -13.97 90) (length 2.54) (name "VSS" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 3.81 180) (length 2.54) (name "RX0BF" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 1.27 180) (length 2.54) (name "RX1BF" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -1.27 180) (length 2.54) (name "INT" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -3.81 180) (length 2.54) (name "SCK" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -6.35 180) (length 2.54) (name "SI" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -8.89 180) (length 2.54) (name "SO" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -6.35 0) (length 2.54) (name "CS" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin input line (at -12.7 -8.89 0) (length 2.54) (name "RESET" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 13.97 270) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
    )
)''',
}


def register_symbols(registry):
    """인터페이스 IC 심볼을 레지스트리에 등록합니다."""
    for name, kicad_symbol in INTERFACE_SYMBOLS.items():
        registry.register_raw(
            name=name,
            kicad_symbol=kicad_symbol,
            category=SymbolCategory.INTERFACE,
            reference_prefix="U",
        )
