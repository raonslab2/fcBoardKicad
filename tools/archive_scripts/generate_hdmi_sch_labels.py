#!/usr/bin/env python3
"""
KiCad HDMI In/Out 회로도 생성 스크립트
IT6801FN (HDMI RX) + IT66121FN (HDMI TX)
"""

import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def create_hdmi_schematic():
    """HDMI 회로도 생성"""

    sch = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{main_uuid}")
  (paper "A3")
  (title_block
    (title "HDMI In/Out")
    (date "2024-11-30")
    (rev "0.1")
    (company "fcBoard Project")
    (comment 1 "IT6801FN HDMI Receiver + IT66121FN HDMI Transmitter")
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
    (symbol "Video:IT6801" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 31.75 0) (effects (font (size 1.27 1.27))))
      (property "Value" "IT6801FN" (at 0 29.21 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "IT6801_0_1"
        (rectangle (start -17.78 27.94) (end 17.78 -27.94) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "IT6801_1_1"
        (pin power_in line (at -20.32 25.4 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 22.86 0) (length 2.54) (name "VDD18" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 -25.4 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 15.24 0) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 12.7 0) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 10.16 0) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 7.62 0) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 5.08 0) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 2.54 0) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 0 0) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 -2.54 0) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -7.62 0) (length 2.54) (name "CEC" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin output line (at -20.32 -10.16 0) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -15.24 0) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -17.78 0) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 25.4 180) (length 2.54) (name "PCLK" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 22.86 180) (length 2.54) (name "DE" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 20.32 180) (length 2.54) (name "HSYNC" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 17.78 180) (length 2.54) (name "VSYNC" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 12.7 180) (length 2.54) (name "R[7:0]" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 10.16 180) (length 2.54) (name "G[7:0]" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 7.62 180) (length 2.54) (name "B[7:0]" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -20.32 180) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -22.86 180) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Video:IT66121" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 31.75 0) (effects (font (size 1.27 1.27))))
      (property "Value" "IT66121FN" (at 0 29.21 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "IT66121_0_1"
        (rectangle (start -17.78 27.94) (end 17.78 -27.94) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "IT66121_1_1"
        (pin power_in line (at -20.32 25.4 0) (length 2.54) (name "VDD33" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 22.86 0) (length 2.54) (name "VDD18" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 20.32 0) (length 2.54) (name "VDD12" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 -25.4 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 12.7 0) (length 2.54) (name "PCLK" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 10.16 0) (length 2.54) (name "DE" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 7.62 0) (length 2.54) (name "HSYNC" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 5.08 0) (length 2.54) (name "VSYNC" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 0 0) (length 2.54) (name "R[7:0]" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 -2.54 0) (length 2.54) (name "G[7:0]" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 -5.08 0) (length 2.54) (name "B[7:0]" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -12.7 0) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -20.32 -15.24 0) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 15.24 180) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 12.7 180) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 10.16 180) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 7.62 180) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 5.08 180) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 2.54 180) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 0 180) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -2.54 180) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 20.32 -7.62 180) (length 2.54) (name "CEC" (effects (font (size 1.27 1.27)))) (number "22" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -10.16 180) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "23" (effects (font (size 1.27 1.27)))))
        (pin input line (at 20.32 -20.32 180) (length 2.54) (name "XTALIN" (effects (font (size 1.27 1.27)))) (number "24" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -22.86 180) (length 2.54) (name "XTALOUT" (effects (font (size 1.27 1.27)))) (number "25" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Connector:HDMI_A" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 17.78 0) (effects (font (size 1.27 1.27))))
      (property "Value" "HDMI_A" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_HDMI:HDMI_A_Molex_47151-0001_Horizontal" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "HDMI_A_0_1"
        (rectangle (start -7.62 12.7) (end 7.62 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "HDMI_A_1_1"
        (pin bidirectional line (at -10.16 10.16 0) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 7.62 0) (length 2.54) (name "TMDS_D2_SH" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 0 0) (length 2.54) (name "TMDS_D1_SH" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -10.16 -7.62 0) (length 2.54) (name "TMDS_D0_SH" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -10.16 0) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 10.16 180) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 7.62 180) (length 2.54) (name "TMDS_CLK_SH" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 5.08 180) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "CEC" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin no_connect line (at 10.16 0 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 -7.62 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 -10.16 180) (length 2.54) (name "+5V" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin input line (at 10.16 -12.7 180) (length 2.54) (name "HPD" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Interface:TXB0108" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TXB0108" (at 0 11.43 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TXB0108_0_1"
        (rectangle (start -7.62 10.16) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "TXB0108_1_1"
        (pin power_in line (at -10.16 7.62 0) (length 2.54) (name "VCCA" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "A1" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "A2" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 0 0) (length 2.54) (name "A3" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "A4" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "A5" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "A6" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 10.16 7.62 180) (length 2.54) (name "VCCB" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 5.08 180) (length 2.54) (name "B1" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "B2" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 0 180) (length 2.54) (name "B3" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "B4" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "B5" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 10.16 -7.62 180) (length 2.54) (name "B6" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -10.16 0) (length 2.54) (name "OE" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
      )
    )

    (symbol "Power_Protection:TPD12S016" (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPD12S016" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPD12S016_0_1"
        (rectangle (start -10.16 12.7) (end 10.16 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "TPD12S016_1_1"
        (pin bidirectional line (at -12.7 10.16 0) (length 2.54) (name "D2+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "D2-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 5.08 0) (length 2.54) (name "D1+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "D1-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 0 0) (length 2.54) (name "D0+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "D0-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 -5.08 0) (length 2.54) (name "CLK+" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at -12.7 -7.62 0) (length 2.54) (name "CLK-" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -12.7 -10.16 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 10.16 180) (length 2.54) (name "D2+_O" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 7.62 180) (length 2.54) (name "D2-_O" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 5.08 180) (length 2.54) (name "D1+_O" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 2.54 180) (length 2.54) (name "D1-_O" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 0 180) (length 2.54) (name "D0+_O" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "D0-_O" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 -5.08 180) (length 2.54) (name "CLK+_O" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin bidirectional line (at 12.7 -7.62 180) (length 2.54) (name "CLK-_O" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
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
    """컴포넌트 배치"""

    components = f'''
  (symbol
    (lib_id "Video:IT6801")
    (at 88.9 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U1" (at 88.9 41.91 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT6801FN" (at 88.9 44.45 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 88.9 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Video:IT66121")
    (at 88.9 175.26 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U2" (at 88.9 140.97 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT66121FN" (at 88.9 143.51 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 88.9 175.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 88.9 175.26 0) (effects (font (size 1.27 1.27)) hide))
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
  )

  (symbol
    (lib_id "Connector:HDMI_A")
    (at 35.56 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J7" (at 35.56 55.88 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HDMI_IN" (at 35.56 58.42 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_HDMI:HDMI_A_Molex_47151-0001_Horizontal" (at 35.56 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 35.56 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Connector:HDMI_A")
    (at 157.48 175.26 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J8" (at 157.48 154.94 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HDMI_OUT" (at 157.48 157.48 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_HDMI:HDMI_A_Molex_47151-0001_Horizontal" (at 157.48 175.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 157.48 175.26 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Interface:TXB0108")
    (at 177.8 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U3" (at 177.8 60.96 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TXB0108" (at 177.8 63.5 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" (at 177.8 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 177.8 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
  )

  (symbol
    (lib_id "Power_Protection:TPD12S016")
    (at 55.88 76.2 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U4" (at 55.88 57.15 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD12S016" (at 55.88 59.69 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 55.88 76.2 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 55.88 76.2 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Power_Protection:TPD12S016")
    (at 137.16 175.26 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U5" (at 137.16 156.21 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD12S016" (at 137.16 158.75 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 137.16 175.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 137.16 175.26 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Device:Crystal")
    (at 124.46 99.06 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "Y1" (at 124.46 93.98 0) (effects (font (size 1.27 1.27))))
    (property "Value" "27MHz" (at 124.46 104.14 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 124.46 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 99.06 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:Crystal")
    (at 124.46 198.12 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "Y2" (at 124.46 193.04 0) (effects (font (size 1.27 1.27))))
    (property "Value" "27MHz" (at 124.46 203.2 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm" (at 124.46 198.12 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 198.12 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 60.96 50.8 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C1" (at 63.5 49.53 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 63.5 52.07 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 61.9252 54.61 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 50.8 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:C")
    (at 60.96 149.86 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "C2" (at 63.5 148.59 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100nF" (at 63.5 151.13 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at 61.9252 153.67 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 149.86 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "Device:R")
    (at 53.34 96.52 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "R1" (at 55.88 95.25 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "10K" (at 55.88 97.79 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "Resistor_SMD:R_0402_1005Metric" (at 51.562 96.52 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 53.34 96.52 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
    (pin "2" (uuid "{gen_uuid()}"))
  )
'''
    return components

def generate_wires():
    """와이어 연결"""

    wires = f'''
  (wire
    (pts (xy 45.72 66.04) (xy 43.18 66.04))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 45.72 71.12) (xy 43.18 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 45.72 78.74) (xy 43.18 78.74))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 45.72 81.28) (xy 43.18 81.28))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 66.04) (xy 68.58 60.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 68.58 60.96) (xy 68.58 61.0))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 50.8) (xy 130.81 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 53.34) (xy 130.81 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 55.88) (xy 130.81 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 58.42) (xy 130.81 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 63.5) (xy 130.81 63.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 66.04) (xy 130.81 66.04))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 68.58) (xy 130.81 68.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 55.88) (xy 109.22 96.52))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 109.22 96.52) (xy 121.92 96.52))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 96.52) (xy 121.92 99.06))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 53.34) (xy 111.76 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 111.76 53.34) (xy 111.76 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 111.76 101.6) (xy 127 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 127 99.06) (xy 127 101.6))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 130.81 50.8) (xy 167.64 50.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 167.64 50.8) (xy 167.64 68.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 130.81 53.34) (xy 165.1 53.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 165.1 53.34) (xy 165.1 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 165.1 71.12) (xy 167.64 71.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 130.81 55.88) (xy 162.56 55.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 162.56 55.88) (xy 162.56 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 162.56 73.66) (xy 167.64 73.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 130.81 58.42) (xy 160.02 58.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 58.42) (xy 160.02 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 160.02 76.2) (xy 167.64 76.2))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 190.5) (xy 109.22 195.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 109.22 195.58) (xy 121.92 195.58))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 195.58) (xy 121.92 198.12))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 152.4) (xy 111.76 152.4))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 111.76 152.4) (xy 111.76 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 111.76 200.66) (xy 127 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 127 198.12) (xy 127 200.66))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 190.5) (xy 124.46 190.5))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 190.5) (xy 124.46 172.72))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 172.72) (xy 124.46 165.1))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 187.96) (xy 121.92 187.96))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 187.96) (xy 121.92 177.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 177.8) (xy 124.46 177.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 185.42) (xy 119.38 185.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 185.42) (xy 119.38 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 119.38 180.34) (xy 124.46 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 182.88) (xy 116.84 182.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 116.84 182.88) (xy 116.84 182.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 116.84 182.88) (xy 124.46 182.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 180.34) (xy 114.3 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 114.3 180.34) (xy 114.3 185.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 114.3 185.42) (xy 124.46 185.42))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 175.26) (xy 124.46 175.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 124.46 175.26) (xy 124.46 170.18))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 109.22 172.72) (xy 121.92 172.72))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 172.72) (xy 121.92 167.64))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
  (wire
    (pts (xy 121.92 167.64) (xy 124.46 167.64))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 165.1) (xy 147.32 165.1))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 167.64) (xy 147.32 167.64))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 170.18) (xy 147.32 170.18))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 172.72) (xy 147.32 172.72))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 175.26) (xy 147.32 175.26))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 177.8) (xy 147.32 177.8))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 180.34) (xy 147.32 180.34))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )

  (wire
    (pts (xy 149.86 182.88) (xy 147.32 182.88))
    (stroke (width 0) (type default))
    (uuid "{gen_uuid()}")
  )
'''
    return wires

def generate_labels():
    """라벨 및 계층 라벨"""

    labels = f'''
  (label "HDMI_IN_D2P"
    (at 43.18 66.04 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "HDMI_IN_D2N"
    (at 43.18 71.12 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "HDMI_IN_D1P"
    (at 43.18 78.74 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "HDMI_IN_D1N"
    (at 43.18 81.28 180)
    (effects (font (size 1.27 1.27)) (justify right bottom))
    (uuid "{gen_uuid()}")
  )

  (label "PCLK_RX"
    (at 130.81 50.8 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "DE_RX"
    (at 130.81 53.34 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "HSYNC_RX"
    (at 130.81 55.88 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "VSYNC_RX"
    (at 130.81 58.42 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "R_RX[7:0]"
    (at 130.81 63.5 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "G_RX[7:0]"
    (at 130.81 66.04 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (label "B_RX[7:0]"
    (at 130.81 68.58 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_RX_PCLK"
    (shape output)
    (at 200.66 68.58 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_RX_DE"
    (shape output)
    (at 200.66 71.12 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_RX_HSYNC"
    (shape output)
    (at 200.66 73.66 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_RX_VSYNC"
    (shape output)
    (at 200.66 76.2 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_RX_DATA[23:0]"
    (shape output)
    (at 200.66 81.28 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_TX_PCLK"
    (shape input)
    (at 50.8 149.86 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_TX_DE"
    (shape input)
    (at 50.8 152.4 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_TX_HSYNC"
    (shape input)
    (at 50.8 154.94 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_TX_VSYNC"
    (shape input)
    (at 50.8 157.48 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

  (hierarchical_label "HDMI_TX_DATA[23:0]"
    (shape input)
    (at 50.8 162.56 180)
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
    (at 60.96 44.45 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR02" (at 60.96 48.26 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 60.96 40.64 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 44.45 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 44.45 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 60.96 143.51 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR03" (at 60.96 147.32 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 60.96 139.7 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 143.51 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 143.51 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+3V3")
    (at 187.96 68.58 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR04" (at 187.96 72.39 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 187.96 64.77 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 187.96 68.58 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 187.96 68.58 0) (effects (font (size 1.27 1.27)) hide))
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
    (property "Reference" "#PWR05" (at 27.94 46.99 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 27.94 39.37 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 27.94 43.18 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:+1V8")
    (at 167.64 68.58 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR06" (at 167.64 72.39 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+1V8" (at 167.64 64.77 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 167.64 68.58 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 167.64 68.58 0) (effects (font (size 1.27 1.27)) hide))
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
    (at 60.96 54.61 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR08" (at 60.96 60.96 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 60.96 58.42 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 54.61 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 54.61 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 60.96 153.67 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR09" (at 60.96 160.02 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 60.96 157.48 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 60.96 153.67 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60.96 153.67 0) (effects (font (size 1.27 1.27)) hide))
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
    (at 68.58 200.66 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR011" (at 68.58 207.01 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 68.58 204.47 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 68.58 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 68.58 200.66 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 124.46 106.68 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR012" (at 124.46 113.03 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 124.46 110.49 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 124.46 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 106.68 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 124.46 205.74 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR013" (at 124.46 212.09 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 124.46 209.55 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 124.46 205.74 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 124.46 205.74 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 177.8 88.9 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR014" (at 177.8 95.25 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 177.8 92.71 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 177.8 88.9 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 177.8 88.9 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )

  (symbol
    (lib_id "power:GND")
    (at 167.64 182.88 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "#PWR015" (at 167.64 189.23 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 167.64 186.69 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 167.64 182.88 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 167.64 182.88 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{gen_uuid()}"))
  )
'''
    return power

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_path = os.path.join(project_dir, "fcBoard_HDMI.kicad_sch")

    content = create_hdmi_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"HDMI schematic generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    main()
