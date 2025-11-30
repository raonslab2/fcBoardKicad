#!/usr/bin/env python3
"""
Verify schematic connections and report issues
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
    """Parse schematic and extract components, wires, labels"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'symbols': [],
        'wires': [],
        'labels': [],
        'hierarchical_labels': [],
        'power_symbols': [],
        'junctions': [],
        'no_connects': [],
    }

    # Find lib_symbols end
    lib_start = content.find('(lib_symbols')
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
    else:
        lib_end = 0

    instance_content = content[lib_end:]

    # Parse symbols
    symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)'
    for match in re.finditer(symbol_pattern, instance_content, re.DOTALL):
        lib_id = match.group(1)
        inner = match.group(2)

        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
        ref = ref_match.group(1) if ref_match else ""

        val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', inner)
        value = val_match.group(1) if val_match else ""

        at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', inner)
        x = float(at_match.group(1)) if at_match else 0
        y = float(at_match.group(2)) if at_match else 0

        # Check if power symbol
        if ref.startswith('#PWR') or ref.startswith('#FLG'):
            data['power_symbols'].append({'ref': ref, 'value': value, 'x': x, 'y': y})
        else:
            data['symbols'].append({'ref': ref, 'value': value, 'lib_id': lib_id, 'x': x, 'y': y})

    # Parse wires
    wire_pattern = r'\(wire\s+\(pts\s+\(xy\s+([\d.-]+)\s+([\d.-]+)\)\s+\(xy\s+([\d.-]+)\s+([\d.-]+)\)\)'
    for match in re.finditer(wire_pattern, instance_content):
        x1, y1, x2, y2 = map(float, match.groups())
        data['wires'].append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})

    # Parse labels
    label_pattern = r'\(label\s+"([^"]+)"[^)]*\(at\s+([\d.-]+)\s+([\d.-]+)'
    for match in re.finditer(label_pattern, instance_content):
        name = match.group(1)
        x, y = float(match.group(2)), float(match.group(3))
        data['labels'].append({'name': name, 'x': x, 'y': y})

    # Parse hierarchical labels
    hlabel_pattern = r'\(hierarchical_label\s+"([^"]+)"[^)]*\(at\s+([\d.-]+)\s+([\d.-]+)'
    for match in re.finditer(hlabel_pattern, instance_content):
        name = match.group(1)
        x, y = float(match.group(2)), float(match.group(3))
        data['hierarchical_labels'].append({'name': name, 'x': x, 'y': y})

    # Parse junctions
    junction_pattern = r'\(junction\s+\(at\s+([\d.-]+)\s+([\d.-]+)\)'
    for match in re.finditer(junction_pattern, instance_content):
        x, y = float(match.group(1)), float(match.group(2))
        data['junctions'].append({'x': x, 'y': y})

    # Parse no_connect
    nc_pattern = r'\(no_connect\s+\(at\s+([\d.-]+)\s+([\d.-]+)\)'
    for match in re.finditer(nc_pattern, instance_content):
        x, y = float(match.group(1)), float(match.group(2))
        data['no_connects'].append({'x': x, 'y': y})

    return data


def check_connections(data, filename):
    """Check for connection issues"""
    issues = []

    # Check 1: Symbols without connections (isolated)
    symbol_positions = set()
    for sym in data['symbols']:
        symbol_positions.add((sym['x'], sym['y']))

    wire_endpoints = set()
    for wire in data['wires']:
        wire_endpoints.add((wire['x1'], wire['y1']))
        wire_endpoints.add((wire['x2'], wire['y2']))

    # Check 2: Labels that might not connect
    label_names = defaultdict(list)
    for label in data['labels']:
        label_names[label['name']].append((label['x'], label['y']))

    for name, positions in label_names.items():
        if len(positions) == 1:
            # Single label - check if it's a power net
            if name not in ['+12V', '+5V', '+3V3', '+1V8', 'GND', 'VBUS']:
                issues.append(f"Single label '{name}' at {positions[0]} - may be unconnected")

    # Check 3: Power symbols
    power_nets = defaultdict(int)
    for pwr in data['power_symbols']:
        power_nets[pwr['value']] += 1

    # Check 4: Wire count
    if len(data['wires']) == 0:
        issues.append("No wires found - schematic may be empty or text-only")

    # Check 5: Hierarchical labels
    if len(data['hierarchical_labels']) == 0 and len(data['symbols']) > 0:
        issues.append("No hierarchical labels - sheet may be isolated from main schematic")

    return issues


def main():
    print("=" * 70)
    print("Schematic Connection Verification")
    print("=" * 70)

    all_issues = []
    all_hlabels = defaultdict(list)  # name -> [files]

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            print(f"\n  SKIP: {sch_file} not found")
            continue

        print(f"\n[{sch_file}]")

        data = parse_schematic(filepath)

        print(f"  Symbols: {len(data['symbols'])}")
        print(f"  Power symbols: {len(data['power_symbols'])}")
        print(f"  Wires: {len(data['wires'])}")
        print(f"  Labels: {len(data['labels'])}")
        print(f"  Hierarchical labels: {len(data['hierarchical_labels'])}")
        print(f"  Junctions: {len(data['junctions'])}")
        print(f"  No-connects: {len(data['no_connects'])}")

        # Collect hierarchical labels
        for hl in data['hierarchical_labels']:
            all_hlabels[hl['name']].append(sch_file)

        # Check for issues
        issues = check_connections(data, sch_file)
        if issues:
            print(f"  Issues found:")
            for issue in issues:
                print(f"    - {issue}")
                all_issues.append((sch_file, issue))
        else:
            print(f"  Status: OK")

    # Cross-sheet hierarchical label check
    print("\n" + "=" * 70)
    print("Hierarchical Label Summary")
    print("=" * 70)

    for name, files in sorted(all_hlabels.items()):
        if len(files) == 1:
            print(f"  WARNING: '{name}' only in {files[0]} - no matching sheet pin?")

    print("\n" + "=" * 70)
    print(f"Total issues: {len(all_issues)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
