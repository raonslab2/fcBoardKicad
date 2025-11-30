#!/usr/bin/env python3
"""
KiCad Schematic Tools - Annotate, ERC, Footprint Assignment, BOM Generation
Works by parsing KiCad 8 S-expression schematic files directly
"""

import re
import os
import json
from collections import defaultdict
from datetime import datetime

PROJECT_DIR = r"D:\git2\fcBoardKicad"

# Schematic files to process
SCHEMATIC_FILES = [
    "fcBoard_Power.kicad_sch",
    "fcBoard_USB.kicad_sch",
    "fcBoard_Ethernet.kicad_sch",
    "fcBoard_HDMI.kicad_sch",
    "fcBoard_Peripherals.kicad_sch",
]

# Footprint mappings by component type and value
FOOTPRINT_MAP = {
    # Capacitors
    "C": {
        "default": "Capacitor_SMD:C_0402_1005Metric",
        "100uF": "Capacitor_SMD:C_1206_3216Metric",
        "47uF": "Capacitor_SMD:C_0805_2012Metric",
        "22uF": "Capacitor_SMD:C_0805_2012Metric",
        "10uF": "Capacitor_SMD:C_0603_1608Metric",
        "4.7uF": "Capacitor_SMD:C_0603_1608Metric",
        "1uF": "Capacitor_SMD:C_0402_1005Metric",
        "100nF": "Capacitor_SMD:C_0402_1005Metric",
        "10nF": "Capacitor_SMD:C_0402_1005Metric",
        "1nF": "Capacitor_SMD:C_0402_1005Metric",
        "100pF": "Capacitor_SMD:C_0402_1005Metric",
        "10pF": "Capacitor_SMD:C_0402_1005Metric",
        "12pF": "Capacitor_SMD:C_0402_1005Metric",
        "15pF": "Capacitor_SMD:C_0402_1005Metric",
        "18pF": "Capacitor_SMD:C_0402_1005Metric",
        "22pF": "Capacitor_SMD:C_0402_1005Metric",
        "27pF": "Capacitor_SMD:C_0402_1005Metric",
    },
    # Resistors
    "R": {
        "default": "Resistor_SMD:R_0402_1005Metric",
    },
    # Inductors
    "L": {
        "default": "Inductor_SMD:L_0603_1608Metric",
        "4.7uH": "Inductor_SMD:L_1210_3225Metric",
        "10uH": "Inductor_SMD:L_1210_3225Metric",
        "2.2uH": "Inductor_SMD:L_0805_2012Metric",
        "1uH": "Inductor_SMD:L_0603_1608Metric",
    },
    # Ferrite beads
    "FB": {
        "default": "Inductor_SMD:L_0402_1005Metric",
    },
    # Diodes
    "D": {
        "default": "Diode_SMD:D_0603_1608Metric",
        "LED": "LED_SMD:LED_0603_1608Metric",
    },
    # Crystals
    "Y": {
        "default": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        "24MHz": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        "25MHz": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
        "27MHz": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
    },
    # ICs
    "U": {
        "default": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        "TPS54360": "Package_SO:HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm",
        "TPS62827": "Package_DFN_QFN:QFN-12-1EP_2x2mm_P0.4mm_EP0.8x0.8mm",
        "TPS73118": "Package_TO_SOT_SMD:SOT-23-5",
        "USB5744": "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm",
        "USB3320": "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm",
        "TPS2041": "Package_TO_SOT_SMD:SOT-23-5",
        "TPD4S012": "Package_DFN_QFN:UQFN-10_1.4x1.8mm_P0.4mm",
        "RTL8211F-CG": "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm",
        "IT6801FN": "Package_QFP:LQFP-64_10x10mm_P0.5mm",
        "IT66121FN": "Package_QFP:LQFP-64_10x10mm_P0.5mm",
        "TPD12S016": "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm",
        "TXB0108": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
        "CP2102N": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm",
        "SN65HVD230": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        "MAX485": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        "AP2112K": "Package_TO_SOT_SMD:SOT-23-5",
    },
    # Connectors
    "J": {
        "default": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        "DC_Jack": "Connector_BarrelJack:BarrelJack_Horizontal",
        "USB_A": "Connector_USB:USB_A_Stewart_SS-52100-001_Horizontal",
        "USB_Micro": "Connector_USB:USB_Micro-B_Wuerth_629105150521",
        "RJ45": "Connector_RJ:RJ45_Amphenol_RJHSE538X_Horizontal",
        "HDMI_A": "Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal",
        "MicroSD": "Connector_Card:microSD_HC_Wuerth_693072010801",
        "Terminal_1x02": "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal",
        "Terminal_1x03": "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal",
    },
    # Switches
    "SW": {
        "default": "Button_Switch_SMD:SW_SPST_TL3342",
    },
    # Power symbols - no footprint needed
    "PWR": {
        "default": "",
    },
}


def parse_schematic(filepath):
    """Parse a KiCad schematic file and extract component information"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    components = []

    # Find all symbol instances
    # Pattern: (symbol (lib_id "...") ... (property "Reference" "X?" ...) ...)
    symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

    for match in re.finditer(symbol_pattern, content, re.DOTALL):
        lib_id = match.group(1)
        symbol_content = match.group(2)

        # Extract reference
        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', symbol_content)
        ref = ref_match.group(1) if ref_match else "?"

        # Extract value
        val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', symbol_content)
        value = val_match.group(1) if val_match else ""

        # Extract UUID
        uuid_match = re.search(r'\(uuid\s+"?([^"\)]+)"?\)', symbol_content)
        uuid = uuid_match.group(1) if uuid_match else ""

        # Extract footprint
        fp_match = re.search(r'\(property\s+"Footprint"\s+"([^"]*)"', symbol_content)
        footprint = fp_match.group(1) if fp_match else ""

        # Extract position
        at_match = re.search(r'\(at\s+([\d.]+)\s+([\d.]+)', symbol_content)
        x = float(at_match.group(1)) if at_match else 0
        y = float(at_match.group(2)) if at_match else 0

        components.append({
            'lib_id': lib_id,
            'reference': ref,
            'value': value,
            'uuid': uuid,
            'footprint': footprint,
            'x': x,
            'y': y,
            'file': os.path.basename(filepath)
        })

    return components, content


def annotate_schematic(filepath, ref_counters):
    """Annotate symbols in a schematic file with sequential numbers"""
    components, content = parse_schematic(filepath)

    # Sort components by position (top to bottom, left to right)
    components.sort(key=lambda c: (c['y'], c['x']))

    changes = []

    for comp in components:
        ref = comp['reference']
        if not ref or ref == "?":
            continue

        # Check if reference needs annotation (ends with ? or has no number)
        ref_match = re.match(r'^([A-Za-z_]+)(\d*)(\??)$', ref)
        if not ref_match:
            continue

        prefix = ref_match.group(1)
        number = ref_match.group(2)
        has_question = ref_match.group(3)

        # Skip power symbols
        if prefix in ['PWR', '#PWR', 'GND', '#GND', 'VCC', 'VDD']:
            continue

        if has_question or not number:
            # Needs annotation
            ref_counters[prefix] = ref_counters.get(prefix, 0) + 1
            new_ref = f"{prefix}{ref_counters[prefix]}"
            changes.append({
                'old_ref': ref,
                'new_ref': new_ref,
                'value': comp['value'],
                'uuid': comp['uuid']
            })

    return changes, ref_counters


def apply_annotations(filepath, changes):
    """Apply annotation changes to a schematic file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for change in changes:
        old_ref = change['old_ref']
        new_ref = change['new_ref']

        # Replace the reference in property
        pattern = rf'(\(property\s+"Reference"\s+)"{re.escape(old_ref)}"'
        replacement = rf'\1"{new_ref}"'
        content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(changes)


def run_erc(filepath):
    """Run basic Electrical Rules Check on a schematic"""
    components, content = parse_schematic(filepath)
    errors = []
    warnings = []

    # Check 1: Unannotated references
    for comp in components:
        ref = comp['reference']
        if '?' in ref:
            errors.append(f"Unannotated symbol: {ref} ({comp['value']})")

    # Check 2: Duplicate references (within same file)
    refs_seen = {}
    for comp in components:
        ref = comp['reference']
        if ref in refs_seen and '?' not in ref:
            errors.append(f"Duplicate reference: {ref} at ({comp['x']}, {comp['y']})")
        refs_seen[ref] = comp

    # Check 3: Missing footprints
    for comp in components:
        ref = comp['reference']
        prefix = re.match(r'^([A-Za-z_]+)', ref)
        if prefix:
            prefix = prefix.group(1)
            # Skip power symbols
            if prefix in ['PWR', '#PWR', 'GND', '#GND', 'VCC', 'VDD', '#FLG']:
                continue
        if not comp['footprint']:
            warnings.append(f"Missing footprint: {ref} ({comp['value']})")

    # Check 4: Power connections (basic check for labels)
    power_labels = ['VCC', 'VDD', 'GND', '+5V', '+3V3', '+1V8', '+12V', 'VBUS']
    has_power = False
    has_ground = False

    for label in power_labels:
        if label.upper() in content.upper():
            if 'GND' in label.upper():
                has_ground = True
            else:
                has_power = True

    if not has_power:
        warnings.append("No power supply labels found")
    if not has_ground:
        warnings.append("No ground labels found")

    # Check 5: Unconnected pins (basic heuristic)
    # Count hierarchical labels
    hlabel_count = content.count('hierarchical_label')
    if hlabel_count == 0:
        warnings.append("No hierarchical labels found (might be isolated)")

    return errors, warnings


def assign_footprints(filepath):
    """Assign footprints to components based on type and value"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = []

    # Find all symbol blocks
    symbol_pattern = r'(\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?))\n\t\)\n'

    def replace_footprint(match):
        full_match = match.group(0)
        lib_id = match.group(2)
        symbol_content = match.group(3)

        # Extract reference and value
        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', symbol_content)
        ref = ref_match.group(1) if ref_match else ""

        val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', symbol_content)
        value = val_match.group(1) if val_match else ""

        # Get prefix
        prefix_match = re.match(r'^([A-Za-z_]+)', ref)
        if not prefix_match:
            return full_match
        prefix = prefix_match.group(1)

        # Skip power symbols
        if prefix in ['PWR', '#PWR', 'GND', '#GND', 'VCC', 'VDD', '#FLG']:
            return full_match

        # Determine footprint
        footprint = None
        if prefix in FOOTPRINT_MAP:
            fp_dict = FOOTPRINT_MAP[prefix]
            # Try value-specific footprint first
            if value in fp_dict:
                footprint = fp_dict[value]
            else:
                # Try partial value match (for IC names)
                for key, fp in fp_dict.items():
                    if key != 'default' and key in value:
                        footprint = fp
                        break
                if not footprint:
                    footprint = fp_dict.get('default', '')

        if not footprint:
            return full_match

        # Check if footprint property exists
        fp_pattern = r'(\(property\s+"Footprint"\s+)"([^"]*)"'
        fp_match = re.search(fp_pattern, full_match)

        if fp_match:
            old_fp = fp_match.group(2)
            if old_fp != footprint:
                changes.append({
                    'ref': ref,
                    'value': value,
                    'old_fp': old_fp,
                    'new_fp': footprint
                })
                new_match = re.sub(fp_pattern, rf'\1"{footprint}"', full_match)
                return new_match

        return full_match

    new_content = re.sub(symbol_pattern, replace_footprint, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes


def generate_bom(schematic_files, output_file):
    """Generate Bill of Materials from all schematic files"""
    all_components = []

    for sch_file in schematic_files:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if os.path.exists(filepath):
            components, _ = parse_schematic(filepath)
            for comp in components:
                # Skip power symbols
                ref = comp['reference']
                prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
                if prefix_match:
                    prefix = prefix_match.group(1)
                    if prefix in ['PWR', '#PWR', 'GND', '#GND', 'VCC', 'VDD', '#FLG']:
                        continue
                all_components.append(comp)

    # Group by value and footprint
    grouped = defaultdict(list)
    for comp in all_components:
        key = (comp['value'], comp['footprint'], comp['lib_id'])
        grouped[key].append(comp['reference'])

    # Sort by reference type then number
    def sort_key(ref):
        match = re.match(r'^([A-Za-z_]+)(\d+)?', ref)
        if match:
            prefix = match.group(1)
            num = int(match.group(2)) if match.group(2) else 0
            return (prefix, num)
        return (ref, 0)

    # Generate BOM
    bom_lines = []
    bom_lines.append("=" * 100)
    bom_lines.append("BILL OF MATERIALS - fcBoard Carrier Board")
    bom_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    bom_lines.append("=" * 100)
    bom_lines.append("")
    bom_lines.append(f"{'Qty':<6} {'References':<30} {'Value':<25} {'Footprint':<35}")
    bom_lines.append("-" * 100)

    total_parts = 0
    total_unique = 0

    for (value, footprint, lib_id), refs in sorted(grouped.items(), key=lambda x: sort_key(x[1][0])):
        refs_sorted = sorted(refs, key=sort_key)
        qty = len(refs_sorted)
        refs_str = ", ".join(refs_sorted)
        if len(refs_str) > 28:
            refs_str = refs_str[:25] + "..."

        fp_short = footprint.split(":")[-1] if footprint else "N/A"
        if len(fp_short) > 33:
            fp_short = fp_short[:30] + "..."

        bom_lines.append(f"{qty:<6} {refs_str:<30} {value:<25} {fp_short:<35}")
        total_parts += qty
        total_unique += 1

    bom_lines.append("-" * 100)
    bom_lines.append(f"Total unique parts: {total_unique}")
    bom_lines.append(f"Total components: {total_parts}")
    bom_lines.append("")

    # Also generate CSV
    csv_lines = ["Qty,References,Value,Footprint,Library"]
    for (value, footprint, lib_id), refs in sorted(grouped.items(), key=lambda x: sort_key(x[1][0])):
        refs_sorted = sorted(refs, key=sort_key)
        qty = len(refs_sorted)
        refs_str = " ".join(refs_sorted)
        csv_lines.append(f'{qty},"{refs_str}","{value}","{footprint}","{lib_id}"')

    # Write files
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(bom_lines))

    csv_file = output_file.replace('.txt', '.csv')
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(csv_lines))

    return total_unique, total_parts, bom_lines


def main():
    print("=" * 60)
    print("KiCad Schematic Tools")
    print("=" * 60)

    # Step 1: Annotate
    print("\n[1/4] Annotating symbols...")
    print("-" * 40)

    ref_counters = {}
    total_annotated = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            print(f"  SKIP: {sch_file} not found")
            continue

        changes, ref_counters = annotate_schematic(filepath, ref_counters)
        if changes:
            apply_annotations(filepath, changes)
            total_annotated += len(changes)
            print(f"  {sch_file}: {len(changes)} symbols annotated")
            for ch in changes[:5]:
                print(f"    {ch['old_ref']} -> {ch['new_ref']} ({ch['value']})")
            if len(changes) > 5:
                print(f"    ... and {len(changes) - 5} more")
        else:
            print(f"  {sch_file}: already annotated")

    print(f"\n  Total annotated: {total_annotated}")

    # Step 2: ERC
    print("\n[2/4] Running ERC (Electrical Rules Check)...")
    print("-" * 40)

    total_errors = 0
    total_warnings = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        errors, warnings = run_erc(filepath)
        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors or warnings:
            print(f"\n  {sch_file}:")
            for err in errors:
                print(f"    ERROR: {err}")
            for warn in warnings:
                print(f"    WARNING: {warn}")
        else:
            print(f"  {sch_file}: OK")

    print(f"\n  ERC Summary: {total_errors} errors, {total_warnings} warnings")

    # Step 3: Footprint assignment
    print("\n[3/4] Assigning footprints...")
    print("-" * 40)

    total_fp_changes = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        changes = assign_footprints(filepath)
        total_fp_changes += len(changes)

        if changes:
            print(f"  {sch_file}: {len(changes)} footprints assigned")
            for ch in changes[:5]:
                print(f"    {ch['ref']}: {ch['new_fp']}")
            if len(changes) > 5:
                print(f"    ... and {len(changes) - 5} more")
        else:
            print(f"  {sch_file}: footprints already assigned or N/A")

    print(f"\n  Total footprints assigned: {total_fp_changes}")

    # Step 4: BOM generation
    print("\n[4/4] Generating BOM...")
    print("-" * 40)

    bom_file = os.path.join(PROJECT_DIR, "fcBoard_BOM.txt")
    unique, total, bom_lines = generate_bom(SCHEMATIC_FILES, bom_file)

    print(f"  BOM saved to: {bom_file}")
    print(f"  CSV saved to: {bom_file.replace('.txt', '.csv')}")
    print(f"  Unique parts: {unique}")
    print(f"  Total components: {total}")

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
