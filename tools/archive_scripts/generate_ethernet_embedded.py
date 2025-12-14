#!/usr/bin/env python3
"""
Ethernet Subsystem Schematic Generator with EMBEDDED Symbols

Generates a KiCad schematic with:
- 2x RTL8211F-CG Gigabit Ethernet PHY
- 2x RJ45 Connectors with Magnetics
- RGMII Interface to SoM

All symbols are embedded in lib_symbols section.
No external library dependencies.

Usage:
    python scripts/generate_ethernet_embedded.py
"""

import uuid
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = PROJECT_ROOT / "fcBoard_Ethernet.kicad_sch"

JLC_FP = "jlc_components"
SCHEMATIC_UUID = "c3d4e5f6-a7b8-9012-cdef-345678901234"


def gen_uuid():
    return str(uuid.uuid4())


# =============================================================================
# EMBEDDED SYMBOL DEFINITIONS
# =============================================================================

LIB_SYMBOLS = '''	(lib_symbols
		(symbol "fcBoard_ETH:RTL8211F"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
			(property "Value" "RTL8211F-CG" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Gigabit Ethernet PHY with RGMII" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "RTL8211F_0_1"
				(rectangle (start -17.78 26.67) (end 17.78 -26.67) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "RTL8211F_1_1"
				(pin power_in line (at -20.32 22.86 0) (length 2.54) (name "AVDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -20.32 20.32 0) (length 2.54) (name "DVDD" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 15.24 0) (length 2.54) (name "TXD0" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 12.7 0) (length 2.54) (name "TXD1" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 10.16 0) (length 2.54) (name "TXD2" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 7.62 0) (length 2.54) (name "TXD3" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 2.54 0) (length 2.54) (name "TX_CLK" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 0 0) (length 2.54) (name "TX_EN" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -5.08 0) (length 2.54) (name "RXD0" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -7.62 0) (length 2.54) (name "RXD1" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -10.16 0) (length 2.54) (name "RXD2" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -12.7 0) (length 2.54) (name "RXD3" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin output line (at -20.32 -17.78 0) (length 2.54) (name "RX_CLK" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin output line (at -20.32 -20.32 0) (length 2.54) (name "RX_DV" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -29.21 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 22.86 180) (length 2.54) (name "MDI0+" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 20.32 180) (length 2.54) (name "MDI0-" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 17.78 180) (length 2.54) (name "MDI1+" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 15.24 180) (length 2.54) (name "MDI1-" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 12.7 180) (length 2.54) (name "MDI2+" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 10.16 180) (length 2.54) (name "MDI2-" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 7.62 180) (length 2.54) (name "MDI3+" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 5.08 180) (length 2.54) (name "MDI3-" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 -2.54 180) (length 2.54) (name "MDC" (effects (font (size 1.016 1.016)))) (number "24" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 -5.08 180) (length 2.54) (name "MDIO" (effects (font (size 1.016 1.016)))) (number "25" (effects (font (size 1.016 1.016)))))
				(pin input line (at 20.32 -10.16 180) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "26" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -15.24 180) (length 2.54) (name "INT_N" (effects (font (size 1.016 1.016)))) (number "27" (effects (font (size 1.016 1.016)))))
				(pin input line (at 20.32 -20.32 180) (length 2.54) (name "CLKIN" (effects (font (size 1.016 1.016)))) (number "28" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_ETH:RJ45_Magjack"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "RJ45_Magjack" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "RJ45 with Integrated Magnetics" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "RJ45_Magjack_0_1"
				(rectangle (start -7.62 12.7) (end 7.62 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "RJ45_Magjack_1_1"
				(pin bidirectional line (at -10.16 10.16 0) (length 2.54) (name "TX+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "TX-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "RX+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "RX-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "BI_D1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "BI_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "BI_D2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "BI_D2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 5.08 180) (length 2.54) (name "LED_G+" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 2.54 180) (length 2.54) (name "LED_G-" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 -2.54 180) (length 2.54) (name "LED_Y+" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 -5.08 180) (length 2.54) (name "LED_Y-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -15.24 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
			)
		)
		(symbol "fcBoard_ETH:Crystal"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "Y" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Crystal Oscillator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Crystal_0_1"
				(rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.524 -1.27) (xy -1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 1.524 -1.27) (xy 1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Crystal_1_1"
				(pin passive line (at -3.81 0 0) (length 2.286) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.286) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_ETH:R"
			(pin_numbers hide)
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Resistor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "R_0_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_ETH:C"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Capacitor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "C_0_1"
				(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
			)
			(symbol "C_1_1"
				(pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_ETH:GND"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "GND" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Power Ground" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "GND_0_1"
				(polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "GND_1_1"
				(pin power_in line (at 0 0 270) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "fcBoard_ETH:+3V3"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+3V3" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+3.3V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+3V3_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+3V3_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
	)'''


def generate_schematic():
    sch = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{SCHEMATIC_UUID}")
	(paper "A3")
	(title_block
		(title "Gigabit Ethernet Subsystem")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "Dual RTL8211F-CG Gigabit Ethernet PHY")
		(comment 2 "RGMII Interface - Embedded Symbols")
	)
{LIB_SYMBOLS}
{generate_instances()}
{generate_labels()}
{generate_text()}
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
'''
    return sch


def generate_instances():
    instances = []

    # ==================== ETH1: RTL8211F PHY (PS Ethernet) ====================
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:RTL8211F",
        ref="U1", value="RTL8211F-CG",
        x=76.2, y=76.2,
        footprint="Package_QFP:QFN-48-1EP_6x6mm_P0.4mm",
        lcsc=""
    ))

    # Crystal for ETH1 (25MHz)
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:Crystal",
        ref="Y1", value="25MHz",
        x=106.68, y=96.52,
        footprint="Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        lcsc=""
    ))

    # Decoupling capacitors
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:C",
        ref="C1", value="100nF",
        x=50.8, y=58.42,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:C",
        ref="C2", value="100nF",
        x=55.88, y=58.42,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # RJ45 Connector for ETH1
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:RJ45_Magjack",
        ref="J1", value="RJ45_ETH1",
        x=152.4, y=76.2,
        footprint="Connector_RJ:RJ45_Amphenol_RJMG1BD3B8K1ANR",
        lcsc=""
    ))

    # Power symbols for ETH1
    instances.append(create_power_symbol("fcBoard_ETH:+3V3", 50.8, 48.26))
    instances.append(create_power_symbol("fcBoard_ETH:+3V3", 55.88, 48.26))
    instances.append(create_power_symbol("fcBoard_ETH:GND", 76.2, 109.22))
    instances.append(create_power_symbol("fcBoard_ETH:GND", 152.4, 96.52))

    # ==================== ETH2: RTL8211F PHY (PL Ethernet) ====================
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:RTL8211F",
        ref="U2", value="RTL8211F-CG",
        x=76.2, y=177.8,
        footprint="Package_QFP:QFN-48-1EP_6x6mm_P0.4mm",
        lcsc=""
    ))

    # Crystal for ETH2 (25MHz)
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:Crystal",
        ref="Y2", value="25MHz",
        x=106.68, y=198.12,
        footprint="Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        lcsc=""
    ))

    # Decoupling capacitors
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:C",
        ref="C3", value="100nF",
        x=50.8, y=160.02,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:C",
        ref="C4", value="100nF",
        x=55.88, y=160.02,
        footprint=f"{JLC_FP}:C0402",
        lcsc="C11702"
    ))

    # RJ45 Connector for ETH2
    instances.append(create_symbol(
        lib_id="fcBoard_ETH:RJ45_Magjack",
        ref="J2", value="RJ45_ETH2",
        x=152.4, y=177.8,
        footprint="Connector_RJ:RJ45_Amphenol_RJMG1BD3B8K1ANR",
        lcsc=""
    ))

    # Power symbols for ETH2
    instances.append(create_power_symbol("fcBoard_ETH:+3V3", 50.8, 149.86))
    instances.append(create_power_symbol("fcBoard_ETH:+3V3", 55.88, 149.86))
    instances.append(create_power_symbol("fcBoard_ETH:GND", 76.2, 210.82))
    instances.append(create_power_symbol("fcBoard_ETH:GND", 152.4, 198.12))

    return '\n'.join(instances)


def create_symbol(lib_id: str, ref: str, value: str, x: float, y: float,
                  footprint: str = "", lcsc: str = ""):
    lcsc_property = ""
    if lcsc:
        lcsc_property = f'''
		(property "LCSC Part" "{lcsc}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))'''

    return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "{ref}" (at {x} {y-5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{value}" (at {x} {y+5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide)){lcsc_property}
		(instances
			(project "fcBoard"
				(path "/{SCHEMATIC_UUID}" (reference "{ref}") (unit 1))
			)
		)
	)'''


def create_power_symbol(lib_id: str, x: float, y: float):
    value = lib_id.split(":")[-1]
    return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom no)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR" (at {x} {y+2.54} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Value" "{value}" (at {x} {y-2.54} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(instances
			(project "fcBoard"
				(path "/{SCHEMATIC_UUID}" (reference "#PWR") (unit 1))
			)
		)
	)'''


def generate_labels():
    labels = []

    # ETH1 RGMII interface (PS)
    eth1_signals = [
        ("ETH1_TXD0", 48.26, 91.44), ("ETH1_TXD1", 48.26, 88.9),
        ("ETH1_TXD2", 48.26, 86.36), ("ETH1_TXD3", 48.26, 83.82),
        ("ETH1_TX_CLK", 48.26, 78.74), ("ETH1_TX_EN", 48.26, 76.2),
        ("ETH1_RXD0", 48.26, 71.12), ("ETH1_RXD1", 48.26, 68.58),
        ("ETH1_RXD2", 48.26, 66.04), ("ETH1_RXD3", 48.26, 63.5),
        ("ETH1_RX_CLK", 48.26, 58.42), ("ETH1_RX_DV", 48.26, 55.88),
        ("ETH1_MDC", 104.14, 73.66), ("ETH1_MDIO", 104.14, 71.12),
        ("ETH1_RESET_N", 104.14, 66.04), ("ETH1_INT_N", 104.14, 60.96),
    ]
    for name, x, y in eth1_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    # ETH2 RGMII interface (PL)
    eth2_signals = [
        ("ETH2_TXD0", 48.26, 193.04), ("ETH2_TXD1", 48.26, 190.5),
        ("ETH2_TXD2", 48.26, 187.96), ("ETH2_TXD3", 48.26, 185.42),
        ("ETH2_TX_CLK", 48.26, 180.34), ("ETH2_TX_EN", 48.26, 177.8),
        ("ETH2_RXD0", 48.26, 172.72), ("ETH2_RXD1", 48.26, 170.18),
        ("ETH2_RXD2", 48.26, 167.64), ("ETH2_RXD3", 48.26, 165.1),
        ("ETH2_RX_CLK", 48.26, 160.02), ("ETH2_RX_DV", 48.26, 157.48),
        ("ETH2_MDC", 104.14, 175.26), ("ETH2_MDIO", 104.14, 172.72),
        ("ETH2_RESET_N", 104.14, 167.64), ("ETH2_INT_N", 104.14, 162.56),
    ]
    for name, x, y in eth2_signals:
        labels.append(create_hlabel(name, x, y, "bidirectional"))

    return '\n'.join(labels)


def create_hlabel(name: str, x: float, y: float, shape: str = "passive"):
    return f'''	(hierarchical_label "{name}"
		(shape {shape})
		(at {x} {y} 0)
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)'''


def generate_text():
    return f'''	(text "ETH1: PS Gigabit Ethernet\\nRGMII to Zynq PS"
		(exclude_from_sim no)
		(at 76.2 40.64 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)
	(text "ETH2: PL Gigabit Ethernet\\nRGMII to Zynq PL"
		(exclude_from_sim no)
		(at 76.2 142.24 0)
		(effects (font (size 1.5 1.5)) (justify left))
		(uuid "{gen_uuid()}")
	)'''


def main():
    print("=" * 60)
    print("Ethernet Subsystem Schematic Generator (Embedded Symbols)")
    print("=" * 60)

    schematic = generate_schematic()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {OUTPUT_FILE}")
    print()
    print("Components:")
    print("  - U1, U2: RTL8211F-CG (Gigabit Ethernet PHY)")
    print("  - J1, J2: RJ45 with Integrated Magnetics")
    print("  - Y1, Y2: 25MHz Crystals")
    print("  - C1-C4: Decoupling Capacitors")
    print()
    print("[NOTE] All symbols embedded - no external library needed.")


if __name__ == "__main__":
    main()
