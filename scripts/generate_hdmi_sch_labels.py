#!/usr/bin/env python3
"""
Generate HDMI schematic with label-based connections
IT6801FN (HDMI RX) and IT66121FN (HDMI TX) with TPD12S016 ESD protection
"""

import uuid

def gen_uuid():
    return str(uuid.uuid4())

def create_hdmi_schematic():
    """Create HDMI schematic with label connections"""

    content = '''(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "''' + gen_uuid() + '''")
  (paper "A3")
  (title_block
    (title "HDMI Input/Output")
    (company "fcBoard")
  )

  (lib_symbols
'''

    # IT6801FN HDMI Receiver symbol
    content += '''    (symbol "IT6801FN" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 36.83 0) (effects (font (size 1.27 1.27))))
      (property "Value" "IT6801FN" (at 0 34.29 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 0 -40.64 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "IT6801FN_0_1"
        (rectangle (start -15.24 33.02) (end 15.24 -38.1) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "IT6801FN_1_1"
        (pin input line (at -17.78 30.48 0) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 27.94 0) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 22.86 0) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 20.32 0) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 15.24 0) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 12.7 0) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 7.62 0) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 5.08 0) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 30.48 180) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 25.4 180) (length 2.54) (name "D0" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 22.86 180) (length 2.54) (name "D1" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 20.32 180) (length 2.54) (name "D2" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 17.78 180) (length 2.54) (name "D3" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 15.24 180) (length 2.54) (name "D4" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 12.7 180) (length 2.54) (name "D5" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 10.16 180) (length 2.54) (name "D6" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 7.62 180) (length 2.54) (name "D7" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 2.54 180) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 0 180) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 -2.54 180) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 -5.08 0) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 -7.62 0) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 -12.7 0) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 -10.16 180) (length 2.54) (name "INT" (effects (font (size 1.016 1.016)))) (number "24" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -40.64 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "25" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -5.08 35.56 270) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "26" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 35.56 270) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "27" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # IT66121FN HDMI Transmitter symbol
    content += '''    (symbol "IT66121FN" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 36.83 0) (effects (font (size 1.27 1.27))))
      (property "Value" "IT66121FN" (at 0 34.29 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 0 -40.64 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "IT66121FN_0_1"
        (rectangle (start -15.24 33.02) (end 15.24 -38.1) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "IT66121FN_1_1"
        (pin input line (at -17.78 30.48 0) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 25.4 0) (length 2.54) (name "D0" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 22.86 0) (length 2.54) (name "D1" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 20.32 0) (length 2.54) (name "D2" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 17.78 0) (length 2.54) (name "D3" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 15.24 0) (length 2.54) (name "D4" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 12.7 0) (length 2.54) (name "D5" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 10.16 0) (length 2.54) (name "D6" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 7.62 0) (length 2.54) (name "D7" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 2.54 0) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 0 0) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 -2.54 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 30.48 180) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 27.94 180) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 22.86 180) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 20.32 180) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 15.24 180) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 12.7 180) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 7.62 180) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 5.08 180) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -17.78 -7.62 0) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
        (pin input line (at -17.78 -10.16 0) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 -5.08 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
        (pin output line (at 17.78 -10.16 180) (length 2.54) (name "INT" (effects (font (size 1.016 1.016)))) (number "24" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -40.64 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "25" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -5.08 35.56 270) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "26" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 5.08 35.56 270) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "27" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # TPD12S016 HDMI ESD symbol
    content += '''    (symbol "TPD12S016" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 21.59 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TPD12S016" (at 0 19.05 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 0 -22.86 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TPD12S016_0_1"
        (rectangle (start -10.16 17.78) (end 10.16 -20.32) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "TPD12S016_1_1"
        (pin bidirectional line (at -12.7 15.24 0) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 12.7 0) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 5.08 0) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 0 0) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -2.54 0) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -7.62 0) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -10.16 0) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 15.24 180) (length 2.54) (name "TMDS_CLK+_OUT" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 12.7 180) (length 2.54) (name "TMDS_CLK-_OUT" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 7.62 180) (length 2.54) (name "TMDS_D0+_OUT" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 5.08 180) (length 2.54) (name "TMDS_D0-_OUT" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 0 180) (length 2.54) (name "TMDS_D1+_OUT" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -2.54 180) (length 2.54) (name "TMDS_D1-_OUT" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -7.62 180) (length 2.54) (name "TMDS_D2+_OUT" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -10.16 180) (length 2.54) (name "TMDS_D2-_OUT" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -15.24 0) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 -15.24 180) (length 2.54) (name "HPD_OUT" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -22.86 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 20.32 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # HDMI connector symbol
    content += '''    (symbol "HDMI_A" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 21.59 0) (effects (font (size 1.27 1.27))))
      (property "Value" "HDMI_A" (at 0 19.05 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal" (at 0 -22.86 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "HDMI_A_0_1"
        (rectangle (start -10.16 17.78) (end 10.16 -20.32) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "HDMI_A_1_1"
        (pin bidirectional line (at -12.7 15.24 0) (length 2.54) (name "TMDS_D2+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -12.7 12.7 0) (length 2.54) (name "TMDS_D2_SH" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 10.16 0) (length 2.54) (name "TMDS_D2-" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 7.62 0) (length 2.54) (name "TMDS_D1+" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -12.7 5.08 0) (length 2.54) (name "TMDS_D1_SH" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "TMDS_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 0 0) (length 2.54) (name "TMDS_D0+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -12.7 -2.54 0) (length 2.54) (name "TMDS_D0_SH" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -5.08 0) (length 2.54) (name "TMDS_D0-" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -7.62 0) (length 2.54) (name "TMDS_CLK+" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin passive line (at -12.7 -10.16 0) (length 2.54) (name "TMDS_CLK_SH" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -12.7 -12.7 0) (length 2.54) (name "TMDS_CLK-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 12.7 7.62 180) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin input line (at 12.7 5.08 180) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin output line (at 12.7 0 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 12.7 -7.62 180) (length 2.54) (name "+5V" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -22.86 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
      )
    )
'''

    # TXB0108 level shifter
    content += '''    (symbol "TXB0108" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 16.51 0) (effects (font (size 1.27 1.27))))
      (property "Value" "TXB0108" (at 0 13.97 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" (at 0 -17.78 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "TXB0108_0_1"
        (rectangle (start -7.62 12.7) (end 7.62 -15.24) (stroke (width 0.254) (type default)) (fill (type background))))
      (symbol "TXB0108_1_1"
        (pin bidirectional line (at -10.16 10.16 0) (length 2.54) (name "A1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "A2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "A3" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "A4" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 0 0) (length 2.54) (name "A5" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "A6" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "A7" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "A8" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 10.16 180) (length 2.54) (name "B1" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 7.62 180) (length 2.54) (name "B2" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 5.08 180) (length 2.54) (name "B3" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "B4" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 0 180) (length 2.54) (name "B5" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "B6" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "B7" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
        (pin bidirectional line (at 10.16 -7.62 180) (length 2.54) (name "B8" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at -2.54 15.24 270) (length 2.54) (name "VCCA" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 2.54 15.24 270) (length 2.54) (name "VCCB" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
        (pin power_in line (at 0 -17.78 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -12.7 0) (length 2.54) (name "OE" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
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
    # HDMI IN section: HDMI_A (J8) -> TPD12S016 (U16) -> IT6801FN (U17)
    # HDMI OUT section: IT66121FN (U19) -> TPD12S016 (U20) -> HDMI_A (J9)
    # TXB0108 (U18) for level shifting

    # HDMI IN - Row at y=70
    hdmi_in_y = 70

    # HDMI_A connector (HDMI IN) at x=50
    content += f'''  (symbol
    (lib_id "HDMI_A")
    (at 50 {hdmi_in_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J8" (at 50 {hdmi_in_y-25} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HDMI_IN" (at 50 {hdmi_in_y-22} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal" (at 50 {hdmi_in_y+22.86} 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "15" (uuid "{gen_uuid()}"))
    (pin "16" (uuid "{gen_uuid()}"))
    (pin "17" (uuid "{gen_uuid()}"))
    (pin "18" (uuid "{gen_uuid()}"))
    (pin "19" (uuid "{gen_uuid()}"))
  )

'''

    # TPD12S016 for HDMI IN at x=130
    content += f'''  (symbol
    (lib_id "TPD12S016")
    (at 130 {hdmi_in_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U16" (at 130 {hdmi_in_y-25} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD12S016" (at 130 {hdmi_in_y-22} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 130 {hdmi_in_y+22.86} 0) (effects (font (size 1.27 1.27)) hide))
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
  )

'''

    # IT6801FN HDMI Receiver at x=220
    content += f'''  (symbol
    (lib_id "IT6801FN")
    (at 220 {hdmi_in_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U17" (at 220 {hdmi_in_y-40} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT6801FN" (at 220 {hdmi_in_y-37} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 220 {hdmi_in_y+40.64} 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "27" (uuid "{gen_uuid()}"))
  )

'''

    # HDMI OUT section - Row at y=170
    hdmi_out_y = 170

    # IT66121FN HDMI Transmitter at x=80
    content += f'''  (symbol
    (lib_id "IT66121FN")
    (at 80 {hdmi_out_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U19" (at 80 {hdmi_out_y-40} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IT66121FN" (at 80 {hdmi_out_y-37} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_QFP:LQFP-64_10x10mm_P0.5mm" (at 80 {hdmi_out_y+40.64} 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "27" (uuid "{gen_uuid()}"))
  )

'''

    # TPD12S016 for HDMI OUT at x=170
    content += f'''  (symbol
    (lib_id "TPD12S016")
    (at 170 {hdmi_out_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U20" (at 170 {hdmi_out_y-25} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TPD12S016" (at 170 {hdmi_out_y-22} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 170 {hdmi_out_y+22.86} 0) (effects (font (size 1.27 1.27)) hide))
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
  )

'''

    # HDMI_A connector (HDMI OUT) at x=250
    content += f'''  (symbol
    (lib_id "HDMI_A")
    (at 250 {hdmi_out_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "J9" (at 250 {hdmi_out_y-25} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HDMI_OUT" (at 250 {hdmi_out_y-22} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal" (at 250 {hdmi_out_y+22.86} 0) (effects (font (size 1.27 1.27)) hide))
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
    (pin "15" (uuid "{gen_uuid()}"))
    (pin "16" (uuid "{gen_uuid()}"))
    (pin "17" (uuid "{gen_uuid()}"))
    (pin "18" (uuid "{gen_uuid()}"))
    (pin "19" (uuid "{gen_uuid()}"))
  )

'''

    # TXB0108 level shifter at x=300, y=120
    content += f'''  (symbol
    (lib_id "TXB0108")
    (at 300 120 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid "{gen_uuid()}")
    (property "Reference" "U18" (at 300 100 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TXB0108" (at 300 103 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" (at 300 137.78 0) (effects (font (size 1.27 1.27)) hide))
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
  )

'''

    # ============ LABELS ============
    # HDMI IN TMDS signals (J8 to TPD16)
    hdmi_in_tmds = [
        ("HDMI_IN_TMDS_D2P", hdmi_in_y - 15.24),
        ("HDMI_IN_TMDS_D2N", hdmi_in_y - 10.16),
        ("HDMI_IN_TMDS_D1P", hdmi_in_y - 7.62),
        ("HDMI_IN_TMDS_D1N", hdmi_in_y - 2.54),
        ("HDMI_IN_TMDS_D0P", hdmi_in_y),
        ("HDMI_IN_TMDS_D0N", hdmi_in_y + 5.08),
        ("HDMI_IN_TMDS_CLKP", hdmi_in_y + 7.62),
        ("HDMI_IN_TMDS_CLKN", hdmi_in_y + 12.7),
    ]

    for name, y in hdmi_in_tmds:
        # At HDMI connector output
        content += f'''  (label "{name}"
    (at 65 {y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        # At TPD12S016 input
        content += f'''  (label "{name}"
    (at 115 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # TPD16 to IT6801FN
    tpd_to_rx = [
        ("HDMI_IN_CLK_P", hdmi_in_y - 15.24),
        ("HDMI_IN_CLK_N", hdmi_in_y - 12.7),
        ("HDMI_IN_D0_P", hdmi_in_y - 7.62),
        ("HDMI_IN_D0_N", hdmi_in_y - 5.08),
        ("HDMI_IN_D1_P", hdmi_in_y),
        ("HDMI_IN_D1_N", hdmi_in_y + 2.54),
        ("HDMI_IN_D2_P", hdmi_in_y + 7.62),
        ("HDMI_IN_D2_N", hdmi_in_y + 10.16),
    ]

    for name, y in tpd_to_rx:
        # TPD output
        content += f'''  (label "{name}"
    (at 145 {y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        # IT6801FN input
        content += f'''  (label "{name}"
    (at 200 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # IT6801FN parallel output to SoM
    rx_output = [
        ("HDMI_RX_PCLK", hdmi_in_y - 30.48),
        ("HDMI_RX_D0", hdmi_in_y - 25.4),
        ("HDMI_RX_D1", hdmi_in_y - 22.86),
        ("HDMI_RX_D2", hdmi_in_y - 20.32),
        ("HDMI_RX_D3", hdmi_in_y - 17.78),
        ("HDMI_RX_D4", hdmi_in_y - 15.24),
        ("HDMI_RX_D5", hdmi_in_y - 12.7),
        ("HDMI_RX_D6", hdmi_in_y - 10.16),
        ("HDMI_RX_D7", hdmi_in_y - 7.62),
        ("HDMI_RX_HSYNC", hdmi_in_y - 2.54),
        ("HDMI_RX_VSYNC", hdmi_in_y),
        ("HDMI_RX_DE", hdmi_in_y + 2.54),
    ]

    for name, y in rx_output:
        content += f'''  (label "{name}"
    (at 240 {y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''

    # HDMI OUT parallel input from SoM
    tx_input = [
        ("HDMI_TX_PCLK", hdmi_out_y - 30.48),
        ("HDMI_TX_D0", hdmi_out_y - 25.4),
        ("HDMI_TX_D1", hdmi_out_y - 22.86),
        ("HDMI_TX_D2", hdmi_out_y - 20.32),
        ("HDMI_TX_D3", hdmi_out_y - 17.78),
        ("HDMI_TX_D4", hdmi_out_y - 15.24),
        ("HDMI_TX_D5", hdmi_out_y - 12.7),
        ("HDMI_TX_D6", hdmi_out_y - 10.16),
        ("HDMI_TX_D7", hdmi_out_y - 7.62),
        ("HDMI_TX_HSYNC", hdmi_out_y - 2.54),
        ("HDMI_TX_VSYNC", hdmi_out_y),
        ("HDMI_TX_DE", hdmi_out_y + 2.54),
    ]

    for name, y in tx_input:
        content += f'''  (label "{name}"
    (at 60 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # IT66121FN to TPD20
    tx_to_tpd = [
        ("HDMI_OUT_CLK_P", hdmi_out_y - 30.48),
        ("HDMI_OUT_CLK_N", hdmi_out_y - 27.94),
        ("HDMI_OUT_D0_P", hdmi_out_y - 22.86),
        ("HDMI_OUT_D0_N", hdmi_out_y - 20.32),
        ("HDMI_OUT_D1_P", hdmi_out_y - 15.24),
        ("HDMI_OUT_D1_N", hdmi_out_y - 12.7),
        ("HDMI_OUT_D2_P", hdmi_out_y - 7.62),
        ("HDMI_OUT_D2_N", hdmi_out_y - 5.08),
    ]

    for name, y in tx_to_tpd:
        # IT66121FN output
        content += f'''  (label "{name}"
    (at 100 {y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        # TPD input
        content += f'''  (label "{name}"
    (at 155 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # TPD20 to HDMI OUT connector
    tpd_to_hdmi_out = [
        ("HDMI_OUT_TMDS_CLKP", hdmi_out_y - 15.24),
        ("HDMI_OUT_TMDS_CLKN", hdmi_out_y - 12.7),
        ("HDMI_OUT_TMDS_D0P", hdmi_out_y - 7.62),
        ("HDMI_OUT_TMDS_D0N", hdmi_out_y - 5.08),
        ("HDMI_OUT_TMDS_D1P", hdmi_out_y),
        ("HDMI_OUT_TMDS_D1N", hdmi_out_y + 2.54),
        ("HDMI_OUT_TMDS_D2P", hdmi_out_y + 7.62),
        ("HDMI_OUT_TMDS_D2N", hdmi_out_y + 10.16),
    ]

    for name, y in tpd_to_hdmi_out:
        # TPD output
        content += f'''  (label "{name}"
    (at 185 {y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid "{gen_uuid()}")
  )

'''
        # HDMI connector input
        content += f'''  (label "{name}"
    (at 235 {y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid "{gen_uuid()}")
  )

'''

    # ============ HIERARCHICAL LABELS ============
    hlabels = []

    # HDMI RX parallel output
    for i, (name, _) in enumerate(rx_output):
        hlabels.append((name, 35 + i * 3))

    # HDMI TX parallel input
    for i, (name, _) in enumerate(tx_input):
        hlabels.append((name, 80 + i * 3))

    # I2C and control signals
    hlabels.extend([
        ("HDMI_RX_SDA", 125),
        ("HDMI_RX_SCL", 128),
        ("HDMI_RX_HPD", 131),
        ("HDMI_RX_INT", 134),
        ("HDMI_TX_SDA", 140),
        ("HDMI_TX_SCL", 143),
        ("HDMI_TX_HPD", 146),
        ("HDMI_TX_INT", 149),
    ])

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
    output_path = r"D:\git2\fcBoardKicad\fcBoard_HDMI.kicad_sch"

    content = create_hdmi_schematic()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {output_path}")
    print("HDMI schematic with label-based connections created!")
