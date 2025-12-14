#!/usr/bin/env python3
"""
Add footprints to all schematic lib_symbols
Works with KiCad 8.0/9.0 format
"""

import re
import os

def add_footprints_to_schematic(filepath, footprint_map):
    """Add footprints to lib_symbols in schematic file"""

    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_count = 0

    for lib_id, footprint in footprint_map.items():
        # Check if this lib_id exists in the file
        if f'(symbol "{lib_id}"' not in content:
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
        print(f"  Saved {updated_count} footprint updates")

    return updated_count


def main():
    project_dir = r"D:\git2\fcBoardKicad"

    # Master footprint mapping for all components
    footprint_map = {
        # Power components
        'Regulator_Switching:LM2596S-ADJ': 'Package_TO_SOT_SMD:TO-263-5_TabPin3',
        'Regulator_Switching:LM2596S-5': 'Package_TO_SOT_SMD:TO-263-5_TabPin3',
        'Device:CP': 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm',
        'Device:D_Schottky': 'Diode_SMD:D_SMA',
        'Device:LED': 'LED_SMD:LED_0805_2012Metric',
        'Device:L': 'Inductor_SMD:L_Bourns_SRN8040',
        'Device:R': 'Resistor_SMD:R_0603_1608Metric',
        'Connector:Barrel_Jack_Switch': 'Connector_BarrelJack:BarrelJack_Horizontal',

        # USB components
        'USB_A': 'Connector_USB:USB_A_Stewart_SS-52100-001_Horizontal',
        'USB5744': 'Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm',
        'TPD4S012': 'Package_TO_SOT_SMD:SOT-23-6',
        'TPS2041B': 'Package_TO_SOT_SMD:SOT-23-5',

        # HDMI components
        'Video:IT66121': 'Package_QFP:LQFP-100_14x14mm_P0.5mm',
        'Video:IT6801': 'Package_QFP:LQFP-100_14x14mm_P0.5mm',
        'Interface:TXB0108': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm',
        'Power_Protection:TPD12S016': 'Package_DFN_QFN:WQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm',
        'Device:C': 'Capacitor_SMD:C_0402_1005Metric',
        'Device:Crystal': 'Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm',
        'Connector:HDMI_A': 'Connector_HDMI:HDMI_A_Molex_47151-0001_Horizontal',

        # Peripherals components
        'CP2102N': 'Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm',
        'MAX485': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm',
        'MicroSD': 'Connector_Card:microSD_HC_Molex_47219-2001',
        'LED': 'LED_SMD:LED_0805_2012Metric',
        'R': 'Resistor_SMD:R_0603_1608Metric',
        'SW_Push': 'Button_Switch_SMD:SW_SPST_TL3342',
        'PinHeader_1x02': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical',
        'SN65HVD230': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm',

        # Ethernet components
        'RJ45_MagJack': 'Connector_RJ:RJ45_Amphenol_ARJM11D7-805-AB-EW2',
        'Crystal': 'Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm',
        'RTL8211F-CG': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm',
    }

    schematic_files = [
        'fcBoard_Power.kicad_sch',
        'fcBoard_USB.kicad_sch',
        'fcBoard_HDMI.kicad_sch',
        'fcBoard_Peripherals.kicad_sch',
        'fcBoard_Ethernet.kicad_sch',
        'fcBoard.kicad_sch',
    ]

    total_updated = 0

    print("=" * 60)
    print("Adding footprints to all schematics")
    print("=" * 60)

    for sch_file in schematic_files:
        sch_path = os.path.join(project_dir, sch_file)
        print(f"\n[{sch_file}]")
        count = add_footprints_to_schematic(sch_path, footprint_map)
        total_updated += count

    print("\n" + "=" * 60)
    print(f"Total footprints updated: {total_updated}")
    print("=" * 60)

    return total_updated


if __name__ == "__main__":
    main()
