#!/usr/bin/env python3
"""
Add footprints to HDMI schematic lib_symbols
Works with KiCad 8.0/9.0 format
"""

import re

def add_footprints_to_hdmi_sch(filepath):
    """Add footprints to lib_symbols in HDMI schematic"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Footprint mappings for HDMI schematic components
    footprint_map = {
        'Device:C': 'Capacitor_SMD:C_0402_1005Metric',
        'Device:R': 'Resistor_SMD:R_0402_1005Metric',
        'Device:Crystal': 'Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm',
        'Connector:HDMI_A': 'Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal',
        'Video:IT66121': 'Package_QFP:LQFP-100_14x14mm_P0.5mm',
        'Video:IT6801': 'Package_QFP:LQFP-100_14x14mm_P0.5mm',
        'Interface:TXB0108': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm',
        'Power_Protection:TPD12S016': 'Package_DFN_QFN:WQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm',
    }

    updated_count = 0

    for lib_id, footprint in footprint_map.items():
        # Check if this lib_id exists in the file
        if f'(symbol "{lib_id}"' not in content:
            print(f"  Symbol {lib_id} not found in file")
            continue

        # Pattern to find Footprint property with empty value in this symbol
        pattern = rf'(\(symbol\s+"{re.escape(lib_id)}".*?)\(property\s+"Footprint"\s+""'

        def replace_footprint(match):
            prefix = match.group(1)
            return f'{prefix}(property "Footprint" "{footprint}"'

        new_content = re.sub(pattern, replace_footprint, content, count=1, flags=re.DOTALL)

        if new_content != content:
            content = new_content
            updated_count += 1
            print(f"  Updated: {lib_id} -> {footprint}")

    if updated_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nSaved {updated_count} footprint updates to: {filepath}")
    else:
        print("\nNo updates needed or symbols not found")

    return updated_count


if __name__ == "__main__":
    hdmi_sch_path = r"D:\git2\fcBoardKicad\fcBoard_HDMI.kicad_sch"
    print("Adding footprints to HDMI schematic...")
    add_footprints_to_hdmi_sch(hdmi_sch_path)
