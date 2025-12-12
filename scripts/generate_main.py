#!/usr/bin/env python3
"""
Main Schematic Generator

Generates the top-level hierarchical schematic (fcBoard.kicad_sch) with:
- All embedded symbols in lib_symbols (required for hierarchical sheets)
- Sheet references to all sub-schematics
- Title block and annotations

IMPORTANT: KiCad hierarchical designs require all symbols to be defined
in the root schematic's lib_symbols section for proper symbol resolution.

Usage:
    python scripts/generate_main.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib.symbols import COMMON_SYMBOLS, POWER_SYMBOLS, IC_SYMBOLS, CONNECTOR_SYMBOLS
from kicad_lib.generator import gen_uuid, generate_deterministic_uuid

# All symbols used across all sub-schematics
ALL_COMMON = ["R", "C", "CP", "L", "LED", "D_Schottky", "Crystal", "Ferrite_Bead", "Fuse"]
ALL_POWER = ["GND", "+12V", "+5V", "+3V3", "+1V8", "+2V5", "VBUS"]
ALL_IC = ["LM2596S-5", "LM2596S-ADJ", "USB5744", "USB3320", "RTL8211F",
          "IT6801FN", "IT66121FN", "MAX485", "CP2102N"]
ALL_CONNECTOR = ["Barrel_Jack", "USB_A", "USB_C", "RJ45_Magjack", "HDMI_A",
                 "Conn_2x10", "SW_Push", "TestPoint"]

PREFIX = "fcBoard"
PROJECT = "fcBoard"
SCHEMATIC_UUID = generate_deterministic_uuid(f"{PROJECT}_main")


def build_lib_symbols():
    """Build the complete lib_symbols section with all symbols."""
    symbols = []

    # Add common symbols
    for name in ALL_COMMON:
        if name in COMMON_SYMBOLS:
            symbols.append(COMMON_SYMBOLS[name].format(prefix=PREFIX))

    # Add power symbols
    for name in ALL_POWER:
        if name in POWER_SYMBOLS:
            symbols.append(POWER_SYMBOLS[name].format(prefix=PREFIX))

    # Add IC symbols
    for name in ALL_IC:
        if name in IC_SYMBOLS:
            symbols.append(IC_SYMBOLS[name].format(prefix=PREFIX))

    # Add connector symbols
    for name in ALL_CONNECTOR:
        if name in CONNECTOR_SYMBOLS:
            symbols.append(CONNECTOR_SYMBOLS[name].format(prefix=PREFIX))

    return '\n\t\t'.join(symbols)


def generate_main_schematic():
    """Generate the main hierarchical schematic."""

    lib_symbols = build_lib_symbols()

    schematic = f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{SCHEMATIC_UUID}")
	(paper "A3")
	(title_block
		(title "ACU5EV SoM Carrier Board")
		(date "2024-12-12")
		(rev "1.0")
		(company "fcBoard Project")
		(comment 1 "Full-featured carrier board for ALINX ACU5EV SoM")
		(comment 2 "Zynq UltraScale+ MPSoC XCZU5EV - Embedded Symbols")
	)
	(lib_symbols
		{lib_symbols}
	)
	(text "ACU5EV SoM Carrier Board - Main Sheet\\n\\nHierarchical Design:\\n1. Power Supply (12V/5V/3.3V/1.8V)\\n2. USB 3.0 Hub (4 ports)\\n3. Gigabit Ethernet (2 ports)\\n4. HDMI In/Out\\n5. Peripherals (RS485, UART, GPIO)"
		(exclude_from_sim no)
		(at 25.4 30.48 0)
		(effects
			(font (size 2 2))
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)
	(text "All sub-schematics use EMBEDDED symbols.\\nNo external library dependencies required.\\nJLCPCB LCSC Part numbers included for BOM."
		(exclude_from_sim no)
		(at 152.4 30.48 0)
		(effects
			(font (size 1.5 1.5))
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)
	(sheet
		(at 25.4 76.2)
		(size 50.8 30.48)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 255 255 194 1.0000))
		(uuid "{gen_uuid()}")
		(property "Sheetname" "Power Supply"
			(at 25.4 75.4884 0)
			(effects (font (size 1.27 1.27)) (justify left bottom))
		)
		(property "Sheetfile" "fcBoard_Power.kicad_sch"
			(at 25.4 107.2216 0)
			(effects (font (size 1.27 1.27)) (justify left top))
		)
	)
	(sheet
		(at 88.9 76.2)
		(size 50.8 30.48)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 194 255 194 1.0000))
		(uuid "{gen_uuid()}")
		(property "Sheetname" "USB 3.0 Hub"
			(at 88.9 75.4884 0)
			(effects (font (size 1.27 1.27)) (justify left bottom))
		)
		(property "Sheetfile" "fcBoard_USB.kicad_sch"
			(at 88.9 107.2216 0)
			(effects (font (size 1.27 1.27)) (justify left top))
		)
	)
	(sheet
		(at 152.4 76.2)
		(size 50.8 30.48)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 194 194 255 1.0000))
		(uuid "{gen_uuid()}")
		(property "Sheetname" "Gigabit Ethernet"
			(at 152.4 75.4884 0)
			(effects (font (size 1.27 1.27)) (justify left bottom))
		)
		(property "Sheetfile" "fcBoard_Ethernet.kicad_sch"
			(at 152.4 107.2216 0)
			(effects (font (size 1.27 1.27)) (justify left top))
		)
	)
	(sheet
		(at 215.9 76.2)
		(size 50.8 30.48)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 255 194 194 1.0000))
		(uuid "{gen_uuid()}")
		(property "Sheetname" "HDMI In/Out"
			(at 215.9 75.4884 0)
			(effects (font (size 1.27 1.27)) (justify left bottom))
		)
		(property "Sheetfile" "fcBoard_HDMI.kicad_sch"
			(at 215.9 107.2216 0)
			(effects (font (size 1.27 1.27)) (justify left top))
		)
	)
	(sheet
		(at 279.4 76.2)
		(size 50.8 30.48)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 255 255 255 1.0000))
		(uuid "{gen_uuid()}")
		(property "Sheetname" "Peripherals"
			(at 279.4 75.4884 0)
			(effects (font (size 1.27 1.27)) (justify left bottom))
		)
		(property "Sheetfile" "fcBoard_Peripherals.kicad_sch"
			(at 279.4 107.2216 0)
			(effects (font (size 1.27 1.27)) (justify left top))
		)
	)
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
'''
    return schematic


def main():
    """Main entry point."""
    print("=" * 60)
    print("Main Schematic Generator")
    print("=" * 60)

    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    output_file = project_root / "fcBoard.kicad_sch"

    schematic = generate_main_schematic()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(schematic)

    print(f"[OK] Generated: {output_file}")
    print()
    print("Embedded symbols included:")
    print(f"  - Common: {', '.join(ALL_COMMON)}")
    print(f"  - Power: {', '.join(ALL_POWER)}")
    print(f"  - ICs: {', '.join(ALL_IC)}")
    print(f"  - Connectors: {', '.join(ALL_CONNECTOR)}")
    print()
    print("Hierarchical sheets:")
    print("  - Power Supply (fcBoard_Power.kicad_sch)")
    print("  - USB 3.0 Hub (fcBoard_USB.kicad_sch)")
    print("  - Gigabit Ethernet (fcBoard_Ethernet.kicad_sch)")
    print("  - HDMI In/Out (fcBoard_HDMI.kicad_sch)")
    print("  - Peripherals (fcBoard_Peripherals.kicad_sch)")
    print()
    print("[NOTE] All symbols are embedded in lib_symbols for hierarchical compatibility")


if __name__ == "__main__":
    main()
