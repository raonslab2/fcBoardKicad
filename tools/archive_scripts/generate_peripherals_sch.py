#!/usr/bin/env python3
"""
KiCad Peripherals 회로도 생성 스크립트
SD Card, Debug UART, CAN x2, RS485 x2, GPIO, etc.
"""

import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def create_peripherals_schematic():
    """Peripherals 회로도 생성"""

    sch = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{main_uuid}")
  (paper "A3")
  (title_block
    (title "Peripherals")
    (date "2024-11-30")
    (rev "0.1")
    (company "fcBoard Project")
    (comment 1 "SD Card, UART, CAN x2, RS485 x2, GPIO")
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
    (symbol "Connector:MicroSD_Card" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
      (property "Value" "MicroSD_Card" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_Card:microSD_HC_Wuerth_693072010801" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "MicroSD_Card_0_1"
        (rectangle (start -7.62 10.16) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "MicroSD_Card_1_1"
        (pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "DAT2" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "DAT3/CD" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "CMD" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 0 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "CLK" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 -5.08 0) (length 2.54) (name "VSS" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "DAT0" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 7.62 180) (length 2.54) (name "DAT1" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -7.62 180) (length 2.54) (name "CD" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Interface_USB:CP2102N" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "CP2102N" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CP2102N_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "CP2102N_1_1"
        (pin power_in line (at -12.7 10.16 0) (length 2.54) (name "VDD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 5.08 0) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -12.7 -10.16 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 10.16 180) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 7.62 180) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 2.54 180) (length 2.54) (name "RTS" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 0 180) (length 2.54) (name "CTS" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 -5.08 180) (length 2.54) (name "DTR" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at 12.7 -7.62 180) (length 2.54) (name "DSR" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Interface_CAN_LIN:SN65HVD230" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SN65HVD230" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "http://www.ti.com/lit/ds/symlink/sn65hvd230.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "SN65HVD230_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "SN65HVD230_1_1"
        (pin input line (at -10.16 2.54 0) (length 2.54) (name "TXD" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 -2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 2.54 180) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin output line (at -10.16 0 0) (length 2.54) (name "RXD" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 0 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "CANL" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "CANH" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -5.08 0) (length 2.54) (name "Rs" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Interface_UART:MAX485" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
      (property "Value" "MAX485" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://datasheets.maximintegrated.com/en/ds/MAX1487-MAX491.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "MAX485_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "MAX485_1_1"
        (pin output line (at -10.16 2.54 0) (length 2.54) (name "RO" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 0 0) (length 2.54) (name "~{RE}" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "DE" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -5.08 0) (length 2.54) (name "DI" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -5.08 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 0 180) (length 2.54) (name "B" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 2.54 180) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Connector:USB_B_Micro" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "USB_B_Micro" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_USB:USB_Micro-B_Molex_47346-0001" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "USB_B_Micro_0_1"
        (rectangle (start -5.08 2.54) (end 5.08 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "USB_B_Micro_1_1"
        (pin power_out line (at 7.62 0 180) (length 2.54) (name "VBUS" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 7.62 -5.08 180) (length 2.54) (name "D+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -7.62 -2.54 0) (length 2.54) (name "ID" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -7.62 -5.08 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Connector:Screw_Terminal_01x03" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Screw_Terminal_01x03" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Screw_Terminal_01x03_0_1"
        (rectangle (start -2.54 2.54) (end 2.54 -2.54) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "Screw_Terminal_01x03_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Device:LED" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 3.175 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LED" (at 0 -3.175 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -0.508 -1.778) (xy 0.762 -3.048)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 -1.778) (xy 1.524 -3.048)) (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
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

    (symbol "Switch:SW_Push" (pin_numbers hide) (pin_names (offset 1.016) hide) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at 1.27 6.35 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "SW_Push" (at 0 -1.524 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 5.08 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "SW_Push_0_1"
        (circle (center -2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0 1.27) (xy 0 3.048)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 2.54 1.27) (xy -2.54 1.27)) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
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
    """컴포넌트 배치"""

    components = f'''
  (symbol
    (lib_id "Connector:MicroSD_Card")
    (at 63.5 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J9" (at 63.5 38.1 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MicroSD" (at 63.5 40.64 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_Card:microSD_HC_Wuerth_693072010801" (at 63.5 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 63.5 55.88 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Connector:USB_B_Micro")
    (at 165.1 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J10" (at 165.1 46.99 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_Debug" (at 165.1 49.53 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_Micro-B_Molex_47346-0001" (at 165.1 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 165.1 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Interface_USB:CP2102N")
    (at 213.36 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U1" (at 213.36 36.83 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CP2102N" (at 213.36 39.37 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm" (at 213.36 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 213.36 55.88 0) (effects (font (size 1.27 1.27)) hide))
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
  )

  (symbol
    (lib_id "Interface_CAN_LIN:SN65HVD230")
    (at 63.5 119.38 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U2" (at 63.5 106.68 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN65HVD230" (at 63.5 109.22 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 63.5 119.38 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 63.5 119.38 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Interface_CAN_LIN:SN65HVD230")
    (at 63.5 154.94 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U3" (at 63.5 142.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SN65HVD230" (at 63.5 144.78 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 63.5 154.94 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 63.5 154.94 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Interface_UART:MAX485")
    (at 165.1 119.38 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U4" (at 165.1 106.68 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX485" (at 165.1 109.22 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 165.1 119.38 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 165.1 119.38 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Interface_UART:MAX485")
    (at 165.1 154.94 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U5" (at 165.1 142.24 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX485" (at 165.1 144.78 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 165.1 154.94 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 165.1 154.94 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
    (pin "4" (uuid "{gen_uuid()}"))
    (pin "5" (uuid "{gen_uuid()}"))
    (pin "6" (uuid "{gen_uuid()}"))
    (pin "7" (uuid "{gen_uuid()}"))
    (pin "8" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x03")
    (at 101.6 116.84 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J11" (at 101.6 109.22 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CAN0" (at 101.6 111.76 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 101.6 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x03")
    (at 101.6 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J12" (at 101.6 144.78 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CAN1" (at 101.6 147.32 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 101.6 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x03")
    (at 203.2 116.84 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J13" (at 203.2 109.22 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RS485_0" (at 203.2 111.76 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 203.2 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 203.2 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x03")
    (at 203.2 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J14" (at 203.2 144.78 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RS485_1" (at 203.2 147.32 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 203.2 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 203.2 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
    (pin "3" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:LED")
    (at 63.5 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D1" (at 63.5 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_USER0" (at 63.5 205.74 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 63.5 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 63.5 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:LED")
    (at 88.9 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D2" (at 88.9 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_USER1" (at 88.9 205.74 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 88.9 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 88.9 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:LED")
    (at 114.3 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D3" (at 114.3 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_USER2" (at 114.3 205.74 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 114.3 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 114.3 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:LED")
    (at 139.7 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "D4" (at 139.7 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_USER3" (at 139.7 205.74 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_0603_1608Metric" (at 139.7 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 139.7 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 50.8 200.66 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R1" (at 50.8 198.12 90) (effects (font (size 1.27 1.27))))
    (property "Value" "470R" (at 50.8 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 50.8 202.438 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 50.8 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 76.2 200.66 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R2" (at 76.2 198.12 90) (effects (font (size 1.27 1.27))))
    (property "Value" "470R" (at 76.2 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 76.2 202.438 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 76.2 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 101.6 200.66 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R3" (at 101.6 198.12 90) (effects (font (size 1.27 1.27))))
    (property "Value" "470R" (at 101.6 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 101.6 202.438 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 127 200.66 90)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R4" (at 127 198.12 90) (effects (font (size 1.27 1.27))))
    (property "Value" "470R" (at 127 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 127 202.438 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 127 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Switch:SW_Push")
    (at 180.34 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "SW1" (at 180.34 193.04 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BTN0" (at 180.34 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm" (at 180.34 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 180.34 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Switch:SW_Push")
    (at 213.36 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "SW2" (at 213.36 193.04 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BTN1" (at 213.36 195.58 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm" (at 213.36 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 213.36 195.58 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 195.58 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C1" (at 198.12 54.61 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 198.12 57.15 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 196.5452 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )
'''
    return components

def generate_wires():
    """와이어 연결"""

    wires = f'''
  (wire
    (pts (xy 53.34 48.26) (xy 40.64 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 50.8) (xy 40.64 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 53.34) (xy 40.64 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 58.42) (xy 40.64 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 63.5) (xy 40.64 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 73.66 48.26) (xy 86.36 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 172.72 55.88) (xy 182.88 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 182.88 55.88) (xy 182.88 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 182.88 53.34) (xy 200.66 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 172.72 58.42) (xy 185.42 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 185.42 58.42) (xy 185.42 60.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 185.42 60.96) (xy 200.66 60.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 225.98 45.72) (xy 241.3 45.72))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 225.98 48.26) (xy 241.3 48.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 116.84) (xy 40.64 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 119.38) (xy 40.64 119.38))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 73.62 116.84) (xy 83.82 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 83.82 116.84) (xy 96.52 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 73.62 114.3) (xy 83.82 114.3))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 83.82 114.3) (xy 83.82 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 152.4) (xy 40.64 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 53.34 154.94) (xy 40.64 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 73.62 152.4) (xy 83.82 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 83.82 152.4) (xy 96.52 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 73.62 149.86) (xy 83.82 149.86))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 83.82 149.86) (xy 83.82 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 116.84) (xy 142.24 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 119.38) (xy 142.24 119.38))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 121.92) (xy 142.24 121.92))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 124.46) (xy 142.24 124.46))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 175.26 116.84) (xy 187.96 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 187.96 116.84) (xy 198.12 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 175.26 119.38) (xy 187.96 119.38))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 187.96 119.38) (xy 187.96 116.84))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 152.4) (xy 142.24 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 154.94) (xy 142.24 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 157.48) (xy 142.24 157.48))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 154.94 160.02) (xy 142.24 160.02))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 175.26 152.4) (xy 187.96 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 187.96 152.4) (xy 198.12 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 175.26 154.94) (xy 187.96 154.94))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 187.96 154.94) (xy 187.96 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 54.61 200.66) (xy 59.69 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 80.01 200.66) (xy 85.09 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 105.41 200.66) (xy 110.49 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 130.81 200.66) (xy 135.89 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 67.31 200.66) (xy 72.39 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 92.71 200.66) (xy 97.79 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 118.11 200.66) (xy 123.19 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 143.51 200.66) (xy 152.4 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 175.26 200.66) (xy 170.18 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 185.42 200.66) (xy 193.04 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 208.28 200.66) (xy 203.2 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 218.44 200.66) (xy 226.06 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
'''
    return wires

def generate_labels():
    """라벨 및 계층 라벨"""

    labels = f'''
  (label "SDIO_DAT2"
    (at 40.64 48.26 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "SDIO_DAT3"
    (at 40.64 50.8 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "SDIO_CMD"
    (at 40.64 53.34 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "SDIO_CLK"
    (at 40.64 58.42 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "SDIO_DAT0"
    (at 40.64 63.5 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "SDIO_DAT1"
    (at 86.36 48.26 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "UART_TXD"
    (at 241.3 45.72 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "UART_RXD"
    (at 241.3 48.26 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "CAN0_TX"
    (at 40.64 116.84 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "CAN0_RX"
    (at 40.64 119.38 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "CAN1_TX"
    (at 40.64 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "CAN1_RX"
    (at 40.64 154.94 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_0_RX"
    (at 142.24 116.84 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_0_RE"
    (at 142.24 119.38 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_0_DE"
    (at 142.24 121.92 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_0_TX"
    (at 142.24 124.46 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_1_RX"
    (at 142.24 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_1_RE"
    (at 142.24 154.94 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_1_DE"
    (at 142.24 157.48 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "RS485_1_TX"
    (at 142.24 160.02 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "LED0"
    (at 46.99 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "LED1"
    (at 72.39 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "LED2"
    (at 97.79 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "LED3"
    (at 123.19 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "BTN0"
    (at 170.18 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "BTN1"
    (at 203.2 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "SDIO_DATA[0..3]"
    (shape bidirectional)
    (at 27.94 48.26 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "SDIO_CMD"
    (shape bidirectional)
    (at 27.94 53.34 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "SDIO_CLK"
    (shape output)
    (at 27.94 58.42 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "UART0_TX"
    (shape output)
    (at 254 45.72 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "UART0_RX"
    (shape input)
    (at 254 48.26 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "CAN0_TX"
    (shape output)
    (at 27.94 116.84 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "CAN0_RX"
    (shape input)
    (at 27.94 119.38 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "CAN1_TX"
    (shape output)
    (at 27.94 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "CAN1_RX"
    (shape input)
    (at 27.94 154.94 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USER_LED[0..3]"
    (shape input)
    (at 27.94 200.66 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "USER_BTN[0..1]"
    (shape output)
    (at 236.22 200.66 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+5V"
    (shape input)
    (at 27.94 30.48 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "+3V3"
    (shape input)
    (at 27.94 35.56 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "GND"
    (shape passive)
    (at 27.94 40.64 180)
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
    (at 27.94 30.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR01" (at 27.94 34.29 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 27.94 26.67 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 30.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 30.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 27.94 35.56 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 27.94 39.37 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 27.94 31.75 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 35.56 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 35.56 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 53.34 55.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 53.34 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 53.34 52.07 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 55.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 73.62 116.84 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 73.62 120.65 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 73.62 113.03 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 73.62 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 73.62 116.84 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 73.62 152.4 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR05" (at 73.62 156.21 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 73.62 148.59 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 73.62 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 73.62 152.4 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 175.26 121.92 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR06" (at 175.26 125.73 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 175.26 118.11 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 175.26 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175.26 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 175.26 157.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR07" (at 175.26 161.29 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 175.26 153.67 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 175.26 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175.26 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 195.58 49.53 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR08" (at 195.58 53.34 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 195.58 45.72 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 195.58 49.53 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 49.53 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 152.4 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR09" (at 152.4 204.47 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 152.4 196.85 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 152.4 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 152.4 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 27.94 40.64 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR010" (at 27.94 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 27.94 44.45 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 40.64 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 53.34 60.96 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR011" (at 53.34 67.31 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 53.34 64.77 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 53.34 121.92 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR012" (at 53.34 128.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 53.34 125.73 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 53.34 157.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR013" (at 53.34 163.83 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 53.34 161.29 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 53.34 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 175.26 124.46 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR014" (at 175.26 130.81 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 175.26 128.27 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 175.26 124.46 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175.26 124.46 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 175.26 160.02 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR015" (at 175.26 166.37 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 175.26 163.83 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 175.26 160.02 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175.26 160.02 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 195.58 59.69 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR016" (at 195.58 66.04 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 195.58 63.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 195.58 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 195.58 59.69 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 200.66 66.04 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR017" (at 200.66 72.39 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 200.66 69.85 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 200.66 66.04 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 200.66 66.04 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 193.04 200.66 270)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR018" (at 186.69 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 189.23 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 193.04 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 193.04 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 226.06 200.66 270)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR019" (at 219.71 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 222.25 200.66 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 226.06 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 226.06 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 101.6 121.92 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR020" (at 101.6 128.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 101.6 125.73 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 101.6 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 101.6 157.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR021" (at 101.6 163.83 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 101.6 161.29 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 101.6 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 101.6 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 203.2 121.92 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR022" (at 203.2 128.27 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 203.2 125.73 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 203.2 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 203.2 121.92 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 203.2 157.48 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR023" (at 203.2 163.83 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 203.2 161.29 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 203.2 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 203.2 157.48 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )
'''
    return power

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_path = os.path.join(project_dir, "fcBoard_Peripherals.kicad_sch")

    content = create_peripherals_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Peripherals schematic generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    main()
