#!/usr/bin/env python3
"""
Verify schematic connections v2 - improved parsing
"""

import re
import os
from collections import defaultdict

PROJECT_DIR = r"D:\git2\fcBoardKicad"

SCHEMATIC_FILES = [
    "fcBoard_Power.kicad_sch",
    "fcBoard_USB.kicad_sch",
    "fcBoard_Ethernet.kicad_sch",
    "fcBoard_HDMI.kicad_sch",
    "fcBoard_Peripherals.kicad_sch",
]


def parse_schematic(filepath):
    """Parse schematic with improved patterns"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'symbols': 0,
        'power_symbols': 0,
        'wires': 0,
        'labels': [],
        'hierarchical_labels': [],
        'junctions': 0,
    }

    # Find lib_symbols end
    lib_start = content.find('(lib_symbols')
    lib_end = 0
    if lib_start != -1:
        depth = 0
        for i, c in enumerate(content[lib_start:], lib_start):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    lib_end = i + 1
                    break

    instance_content = content[lib_end:]

    # Count symbols (excluding lib_symbols definitions)
    symbol_count = len(re.findall(r'\(symbol\s+\(lib_id', instance_content))
    power_count = len(re.findall(r'lib_id\s+"power:', instance_content))
    data['symbols'] = symbol_count - power_count
    data['power_symbols'] = power_count

    # Count wires
    data['wires'] = len(re.findall(r'\(wire\s+\(pts', instance_content))

    # Count junctions
    data['junctions'] = len(re.findall(r'\(junction\s+\(at', instance_content))

    # Parse labels - improved pattern
    label_pattern = r'\(label\s+"([^"]+)"\s*\n?\s*\(at\s+([\d.-]+)\s+([\d.-]+)'
    for match in re.finditer(label_pattern, content):
        name = match.group(1)
        x, y = float(match.group(2)), float(match.group(3))
        data['labels'].append({'name': name, 'x': x, 'y': y})

    # Parse hierarchical labels - improved pattern
    hlabel_pattern = r'\(hierarchical_label\s+"([^"]+)"\s*\n?\s*\(shape\s+\w+\)\s*\n?\s*\(at\s+([\d.-]+)\s+([\d.-]+)'
    for match in re.finditer(hlabel_pattern, content):
        name = match.group(1)
        x, y = float(match.group(2)), float(match.group(3))
        data['hierarchical_labels'].append({'name': name, 'x': x, 'y': y})

    return data


def main():
    print("=" * 70)
    print("Schematic Connection Verification v2")
    print("=" * 70)

    total_issues = 0
    all_hlabels = defaultdict(list)

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        print(f"\n[{sch_file}]")

        data = parse_schematic(filepath)

        print(f"  Symbols: {data['symbols']}")
        print(f"  Power symbols: {data['power_symbols']}")
        print(f"  Wires: {data['wires']}")
        print(f"  Labels: {len(data['labels'])}")
        print(f"  Hierarchical labels: {len(data['hierarchical_labels'])}")
        print(f"  Junctions: {data['junctions']}")

        issues = []

        if data['wires'] == 0:
            issues.append("No wires found")

        if len(data['hierarchical_labels']) == 0:
            issues.append("No hierarchical labels - may be isolated")

        if issues:
            print(f"  Issues: {', '.join(issues)}")
            total_issues += len(issues)
        else:
            print(f"  Status: OK")

        # Collect hierarchical labels
        for hl in data['hierarchical_labels']:
            all_hlabels[hl['name']].append(sch_file)

    print("\n" + "=" * 70)
    print("Hierarchical Labels Summary")
    print("=" * 70)

    if all_hlabels:
        print(f"  Total unique labels: {len(all_hlabels)}")
        for name, files in sorted(all_hlabels.items()):
            files_str = ", ".join([f.replace("fcBoard_", "").replace(".kicad_sch", "") for f in files])
            print(f"    {name}: {files_str}")
    else:
        print("  No hierarchical labels found!")

    print("\n" + "=" * 70)
    print(f"Total issues: {total_issues}")
    print("=" * 70)


if __name__ == "__main__":
    main()
