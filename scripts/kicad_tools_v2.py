#!/usr/bin/env python3
"""
KiCad Schematic Tools v2 - Global Annotate across all sheets
Fixes duplicate reference issues by using global counter
"""

import re
import os
import json
from collections import defaultdict
from datetime import datetime

PROJECT_DIR = r"D:\git2\fcBoardKicad"

SCHEMATIC_FILES = [
    "fcBoard_Power.kicad_sch",
    "fcBoard_USB.kicad_sch",
    "fcBoard_Ethernet.kicad_sch",
    "fcBoard_HDMI.kicad_sch",
    "fcBoard_Peripherals.kicad_sch",
]

FOOTPRINT_MAP = {
    "C": {
        "default": "Capacitor_SMD:C_0402_1005Metric",
        "100uF": "Capacitor_SMD:C_1206_3216Metric",
        "47uF": "Capacitor_SMD:C_0805_2012Metric",
        "22uF": "Capacitor_SMD:C_0805_2012Metric",
        "10uF": "Capacitor_SMD:C_0603_1608Metric",
        "4.7uF": "Capacitor_SMD:C_0603_1608Metric",
        "1uF": "Capacitor_SMD:C_0402_1005Metric",
    },
    "R": {"default": "Resistor_SMD:R_0402_1005Metric"},
    "L": {
        "default": "Inductor_SMD:L_0603_1608Metric",
        "33uH": "Inductor_SMD:L_Bourns_SRN6045TA",
        "10uH": "Inductor_SMD:L_1210_3225Metric",
        "4.7uH": "Inductor_SMD:L_1210_3225Metric",
    },
    "FB": {"default": "Inductor_SMD:L_0402_1005Metric"},
    "D": {"default": "LED_SMD:LED_0603_1608Metric"},
    "Y": {"default": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm"},
    "U": {
        "default": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        "LM2596": "Package_TO_SOT_SMD:TO-263-5_TabPin3",
        "AMS1117": "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
        "TPS54360": "Package_SO:HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm",
        "USB5744": "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm",
        "USB3320": "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm",
        "TPS2041": "Package_TO_SOT_SMD:SOT-23-5",
        "TPD4S012": "Package_DFN_QFN:UQFN-10_1.4x1.8mm_P0.4mm",
        "RTL8211F": "Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.25x4.25mm",
        "IT6801": "Package_QFP:LQFP-64_10x10mm_P0.5mm",
        "IT66121": "Package_QFP:LQFP-64_10x10mm_P0.5mm",
        "TPD12S016": "Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm",
        "TXB0108": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
        "CP2102": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm",
        "SN65HVD230": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        "MAX485": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
    },
    "J": {
        "default": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        "DC_12V": "Connector_BarrelJack:BarrelJack_Horizontal",
        "USB_A": "Connector_USB:USB_A_Stewart_SS-52100-001_Horizontal",
        "USB_Micro": "Connector_USB:USB_Micro-B_Wuerth_629105150521",
        "RJ45": "Connector_RJ:RJ45_Amphenol_RJHSE538X_Horizontal",
        "HDMI": "Connector_HDMI:HDMI_A_Molex_2086581051_Horizontal",
        "MicroSD": "Connector_Card:microSD_HC_Wuerth_693072010801",
        "Terminal": "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal",
    },
    "SW": {"default": "Button_Switch_SMD:SW_SPST_TL3342"},
}


def parse_all_components():
    """Parse all schematics and collect components"""
    all_components = []

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all symbol instances
        symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

        for match in re.finditer(symbol_pattern, content, re.DOTALL):
            lib_id = match.group(1)
            symbol_content = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', symbol_content)
            ref = ref_match.group(1) if ref_match else "?"

            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', symbol_content)
            value = val_match.group(1) if val_match else ""

            at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', symbol_content)
            x = float(at_match.group(1)) if at_match else 0
            y = float(at_match.group(2)) if at_match else 0

            fp_match = re.search(r'\(property\s+"Footprint"\s+"([^"]*)"', symbol_content)
            footprint = fp_match.group(1) if fp_match else ""

            all_components.append({
                'file': sch_file,
                'lib_id': lib_id,
                'reference': ref,
                'value': value,
                'footprint': footprint,
                'x': x,
                'y': y,
                'match_start': match.start(),
                'match_end': match.end(),
            })

    return all_components


def global_annotate():
    """Annotate all symbols with globally unique references"""
    print("\n[1/4] Global Annotation...")
    print("-" * 50)

    # Counters per prefix, per sheet to maintain locality
    ref_counters = defaultdict(int)

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            print(f"  SKIP: {sch_file} not found")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Collect all symbols with their positions for sorting
        symbols = []
        symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

        for match in re.finditer(symbol_pattern, content, re.DOTALL):
            lib_id = match.group(1)
            symbol_content = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', symbol_content)
            ref = ref_match.group(1) if ref_match else "?"

            at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', symbol_content)
            x = float(at_match.group(1)) if at_match else 0
            y = float(at_match.group(2)) if at_match else 0

            symbols.append({
                'ref': ref,
                'x': x,
                'y': y,
                'start': match.start(),
                'end': match.end(),
                'content': match.group(0)
            })

        # Sort by position (top to bottom, left to right)
        symbols.sort(key=lambda s: (s['y'], s['x']))

        changes = []

        for sym in symbols:
            ref = sym['ref']

            # Extract prefix
            prefix_match = re.match(r'^([A-Za-z_#]+)(\d*)(\??)$', ref)
            if not prefix_match:
                continue

            prefix = prefix_match.group(1)

            # Skip power symbols - they don't need unique refs
            if prefix in ['#PWR', '#FLG', 'PWR']:
                continue

            # Check if needs annotation
            has_question = '?' in ref
            has_number = bool(prefix_match.group(2))

            if has_question or not has_number:
                ref_counters[prefix] += 1
                new_ref = f"{prefix}{ref_counters[prefix]}"
                changes.append({
                    'old': ref,
                    'new': new_ref,
                    'pattern': rf'(\(property\s+"Reference"\s+)"{re.escape(ref)}"',
                    'replacement': rf'\1"{new_ref}"'
                })

        # Apply changes
        modified = False
        for change in changes:
            new_content = re.sub(change['pattern'], change['replacement'], content, count=1)
            if new_content != content:
                content = new_content
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

        print(f"  {sch_file}: {len(changes)} symbols annotated")
        if changes:
            for ch in changes[:3]:
                print(f"    {ch['old']} -> {ch['new']}")
            if len(changes) > 3:
                print(f"    ... and {len(changes) - 3} more")

    total = sum(ref_counters.values())
    print(f"\n  Total: {total} symbols annotated")
    print(f"  Reference ranges:")
    for prefix in sorted(ref_counters.keys()):
        print(f"    {prefix}: 1-{ref_counters[prefix]}")

    return ref_counters


def run_erc():
    """Run ERC check"""
    print("\n[2/4] ERC (Electrical Rules Check)...")
    print("-" * 50)

    all_refs = defaultdict(list)  # ref -> [file, file, ...]
    total_errors = 0
    total_warnings = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        errors = []
        warnings = []

        # Find all symbols
        symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

        for match in re.finditer(symbol_pattern, content, re.DOTALL):
            symbol_content = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', symbol_content)
            ref = ref_match.group(1) if ref_match else "?"

            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', symbol_content)
            value = val_match.group(1) if val_match else ""

            fp_match = re.search(r'\(property\s+"Footprint"\s+"([^"]*)"', symbol_content)
            footprint = fp_match.group(1) if fp_match else ""

            prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
            prefix = prefix_match.group(1) if prefix_match else ""

            # Skip power symbols
            if prefix in ['#PWR', '#FLG', 'PWR']:
                continue

            # Check for unannotated
            if '?' in ref:
                errors.append(f"Unannotated: {ref} ({value})")

            # Track for duplicate check
            all_refs[ref].append(sch_file)

            # Check missing footprint
            if not footprint:
                warnings.append(f"No footprint: {ref} ({value})")

        if errors or warnings:
            print(f"\n  {sch_file}:")
            for err in errors[:5]:
                print(f"    ERROR: {err}")
            if len(errors) > 5:
                print(f"    ... and {len(errors) - 5} more errors")
            for warn in warnings[:5]:
                print(f"    WARN: {warn}")
            if len(warnings) > 5:
                print(f"    ... and {len(warnings) - 5} more warnings")
        else:
            print(f"  {sch_file}: OK")

        total_errors += len(errors)
        total_warnings += len(warnings)

    # Check for duplicates across sheets
    duplicates = {ref: files for ref, files in all_refs.items() if len(files) > 1}
    if duplicates:
        print(f"\n  Cross-sheet duplicates: {len(duplicates)}")
        for ref, files in list(duplicates.items())[:5]:
            print(f"    {ref}: {', '.join(files)}")
        total_errors += len(duplicates)

    print(f"\n  ERC Summary: {total_errors} errors, {total_warnings} warnings")
    return total_errors, total_warnings


def assign_footprints():
    """Assign footprints to all components"""
    print("\n[3/4] Assigning footprints...")
    print("-" * 50)

    total_assigned = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changes = []

        def get_footprint(prefix, value):
            """Determine footprint based on prefix and value"""
            if prefix not in FOOTPRINT_MAP:
                return None

            fp_dict = FOOTPRINT_MAP[prefix]

            # Try exact value match
            if value in fp_dict:
                return fp_dict[value]

            # Try partial match
            for key, fp in fp_dict.items():
                if key != 'default' and key in value:
                    return fp

            return fp_dict.get('default')

        # Process each symbol
        symbol_pattern = r'(\(symbol\s+\(lib_id\s+"[^"]+"\)(.*?)\n\t\)\n)'

        def replace_fp(match):
            nonlocal changes
            full = match.group(0)
            inner = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
            ref = ref_match.group(1) if ref_match else ""

            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', inner)
            value = val_match.group(1) if val_match else ""

            prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
            prefix = prefix_match.group(1) if prefix_match else ""

            # Skip power symbols
            if prefix in ['#PWR', '#FLG', 'PWR']:
                return full

            # Get appropriate footprint
            new_fp = get_footprint(prefix, value)
            if not new_fp:
                return full

            # Check current footprint
            fp_pattern = r'(\(property\s+"Footprint"\s+)"([^"]*)"'
            fp_match = re.search(fp_pattern, full)

            if fp_match:
                old_fp = fp_match.group(2)
                if old_fp != new_fp:
                    changes.append({'ref': ref, 'value': value, 'old': old_fp, 'new': new_fp})
                    return re.sub(fp_pattern, rf'\1"{new_fp}"', full)

            return full

        new_content = re.sub(symbol_pattern, replace_fp, content, flags=re.DOTALL)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        total_assigned += len(changes)

        if changes:
            print(f"  {sch_file}: {len(changes)} footprints assigned")
            for ch in changes[:3]:
                print(f"    {ch['ref']}: {ch['new']}")
            if len(changes) > 3:
                print(f"    ... and {len(changes) - 3} more")
        else:
            print(f"  {sch_file}: OK (footprints already assigned)")

    print(f"\n  Total: {total_assigned} footprints assigned")
    return total_assigned


def generate_bom():
    """Generate BOM from all schematics"""
    print("\n[4/4] Generating BOM...")
    print("-" * 50)

    components = []

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

        for match in re.finditer(symbol_pattern, content, re.DOTALL):
            lib_id = match.group(1)
            inner = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
            ref = ref_match.group(1) if ref_match else ""

            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', inner)
            value = val_match.group(1) if val_match else ""

            fp_match = re.search(r'\(property\s+"Footprint"\s+"([^"]*)"', inner)
            footprint = fp_match.group(1) if fp_match else ""

            prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
            prefix = prefix_match.group(1) if prefix_match else ""

            # Skip power symbols
            if prefix in ['#PWR', '#FLG', 'PWR']:
                continue

            components.append({
                'ref': ref,
                'value': value,
                'footprint': footprint,
                'lib_id': lib_id,
                'sheet': sch_file
            })

    # Group by value + footprint
    grouped = defaultdict(list)
    for comp in components:
        key = (comp['value'], comp['footprint'])
        grouped[key].append(comp['ref'])

    # Sort refs naturally
    def sort_key(ref):
        match = re.match(r'^([A-Za-z_]+)(\d+)?', ref)
        if match:
            return (match.group(1), int(match.group(2) or 0))
        return (ref, 0)

    # Generate BOM text
    lines = []
    lines.append("=" * 100)
    lines.append("BILL OF MATERIALS - fcBoard Carrier Board")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 100)
    lines.append("")
    lines.append(f"{'Qty':<5} {'References':<35} {'Value':<20} {'Footprint':<35}")
    lines.append("-" * 100)

    total_qty = 0

    for (value, footprint), refs in sorted(grouped.items(), key=lambda x: sort_key(x[1][0])):
        refs_sorted = sorted(refs, key=sort_key)
        qty = len(refs_sorted)
        total_qty += qty

        refs_str = ", ".join(refs_sorted)
        if len(refs_str) > 33:
            refs_str = refs_str[:30] + "..."

        fp_short = footprint.split(":")[-1] if footprint else "N/A"
        if len(fp_short) > 33:
            fp_short = fp_short[:30] + "..."

        lines.append(f"{qty:<5} {refs_str:<35} {value:<20} {fp_short:<35}")

    lines.append("-" * 100)
    lines.append(f"Unique parts: {len(grouped)}")
    lines.append(f"Total components: {total_qty}")

    # Write TXT
    bom_txt = os.path.join(PROJECT_DIR, "fcBoard_BOM.txt")
    with open(bom_txt, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

    # Write CSV
    csv_lines = ["Qty,References,Value,Footprint"]
    for (value, footprint), refs in sorted(grouped.items(), key=lambda x: sort_key(x[1][0])):
        refs_sorted = sorted(refs, key=sort_key)
        qty = len(refs_sorted)
        refs_str = " ".join(refs_sorted)
        csv_lines.append(f'{qty},"{refs_str}","{value}","{footprint}"')

    bom_csv = os.path.join(PROJECT_DIR, "fcBoard_BOM.csv")
    with open(bom_csv, 'w', encoding='utf-8') as f:
        f.write("\n".join(csv_lines))

    print(f"  BOM TXT: {bom_txt}")
    print(f"  BOM CSV: {bom_csv}")
    print(f"  Unique parts: {len(grouped)}")
    print(f"  Total components: {total_qty}")

    return len(grouped), total_qty


def main():
    print("=" * 60)
    print("KiCad Schematic Tools v2")
    print("=" * 60)

    global_annotate()
    run_erc()
    assign_footprints()
    generate_bom()

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
