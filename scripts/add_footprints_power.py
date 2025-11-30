#!/usr/bin/env python3
"""
Add footprints to Power schematic lib_symbols
Works with KiCad 9.0 format
"""

import re

def add_footprints_to_power_sch(filepath):
    """Add footprints to lib_symbols in Power schematic"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Footprint mappings for Power schematic components
    footprint_map = {
        'Connector:Barrel_Jack_Switch': 'Connector_BarrelJack:BarrelJack_Horizontal',
        'Device:CP': 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm',
        'Device:D_Schottky': 'Diode_SMD:D_SMA',
        'Device:LED': 'LED_SMD:LED_0805_2012Metric',
        'Device:L': 'Inductor_SMD:L_Bourns_SRN8040',
        'Device:R': 'Resistor_SMD:R_0603_1608Metric',
        'Regulator_Switching:LM2596S-ADJ': 'Package_TO_SOT_SMD:TO-263-5_TabPin3',
        'Regulator_Switching:LM2596S-5': 'Package_TO_SOT_SMD:TO-263-5_TabPin3',
    }

    updated_count = 0

    for lib_id, footprint in footprint_map.items():
        # Check if this lib_id exists in the file
        if f'(symbol "{lib_id}"' not in content:
            print(f"  Symbol {lib_id} not found in file")
            continue

        # Pattern to find Footprint property with empty value in this symbol
        # KiCad 9 format: (property "Footprint" ""\n\t\t\t\t(at ...
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
    power_sch_path = r"D:\git2\fcBoardKicad\fcBoard_Power.kicad_sch"
    print("Adding footprints to Power schematic...")
    add_footprints_to_power_sch(power_sch_path)
