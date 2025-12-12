#!/usr/bin/env python3
"""
Fix missing footprints - replace with available KiCad library footprints
"""

import re
import os

def fix_footprints_in_file(filepath, replacements):
    """Replace footprint names in schematic file"""

    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_count = 0
    original_content = content

    for old_fp, new_fp in replacements.items():
        if old_fp in content:
            content = content.replace(old_fp, new_fp)
            updated_count += 1
            print(f"  Replaced: {old_fp}")
            print(f"       -> {new_fp}")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Saved changes to: {filepath}")

    return updated_count


def main():
    project_dir = r"D:\git2\fcBoardKicad"

    # Footprint replacements - old name -> new available name
    replacements = {
        # RJ45 - use a standard available footprint
        'Connector_RJ:RJ45_Amphenol_RJHSE538X_Horizontal': 'Connector_RJ:RJ45_Amphenol_ARJM11D7-805-AB-EW2',

        # HDMI - use standard HDMI-A footprint
        'Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal': 'Connector_HDMI:HDMI_A_Molex_47151-0001_Horizontal',

        # QFN-48 - check exact name available
        'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm',
    }

    schematic_files = [
        'fcBoard.kicad_sch',
        'fcBoard_Power.kicad_sch',
        'fcBoard_USB.kicad_sch',
        'fcBoard_HDMI.kicad_sch',
        'fcBoard_Peripherals.kicad_sch',
        'fcBoard_Ethernet.kicad_sch',
    ]

    print("=" * 60)
    print("Fixing missing footprints")
    print("=" * 60)

    total_updated = 0

    for sch_file in schematic_files:
        sch_path = os.path.join(project_dir, sch_file)
        print(f"\n[{sch_file}]")
        count = fix_footprints_in_file(sch_path, replacements)
        total_updated += count

    print("\n" + "=" * 60)
    print(f"Total replacements: {total_updated}")
    print("=" * 60)
    print("\nNow run 'Update PCB from Schematic' (F8) in KiCad again.")

    return total_updated


if __name__ == "__main__":
    main()
