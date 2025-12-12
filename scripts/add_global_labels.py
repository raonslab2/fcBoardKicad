#!/usr/bin/env python3
"""
Add global labels to connector.kicad_sch for all SoM connector pins.
Parses symbol definitions directly to get pin names and coordinates.
No CSV filtering - ALL pins get global labels.
"""

import uuid
import os
import re

PROJECT_DIR = r"D:\git2\fcBoardKicad"
CONNECTOR_SCH = os.path.join(PROJECT_DIR, "connector.kicad_sch")

# Connector info - lib_id only, no CSV dependency
CONNECTORS = {
    'J29': 'fcBoard:ACU5EV_J29_BANK65_66',
    'J30': 'fcBoard:ACU5EV_J30_BANK25_26_MGT',
    'J31': 'fcBoard:ACU5EV_J31_BANK24_44',
    'J32': 'fcBoard:ACU5EV_J32_MIO_POWER'
}

def generate_uuid():
    """Generate a new UUID for KiCad."""
    return str(uuid.uuid4())

def parse_symbol_pins(content, lib_id):
    """Parse symbol definition to extract all pin info.
    Returns dict: {pin_number: (pin_name, rel_x, rel_y, angle)}
    """
    pins = {}

    # Find the symbol definition
    symbol_start = content.find(f'(symbol "{lib_id}"')
    if symbol_start == -1:
        print(f"Warning: Symbol {lib_id} not found")
        return pins

    # Find the end of this symbol
    depth = 0
    symbol_end = symbol_start
    for i in range(symbol_start, len(content)):
        if content[i] == '(':
            depth += 1
        elif content[i] == ')':
            depth -= 1
            if depth == 0:
                symbol_end = i
                break

    symbol_content = content[symbol_start:symbol_end]

    # Pattern to find pin definitions with name and coordinates
    # (pin bidirectional line (at x y angle) (length ...) (name "PIN_NAME" ...) (number "NUM" ...)
    pattern = r'\(pin\s+\w+\s+\w+\s*\n?\s*\(at\s+([-\d.]+)\s+([-\d.]+)\s+(\d+)\).*?\(name\s+"([^"]+)".*?\(number\s+"(\d+)"'

    for match in re.finditer(pattern, symbol_content, re.DOTALL):
        rel_x = float(match.group(1))
        rel_y = float(match.group(2))
        angle = int(match.group(3))
        pin_name = match.group(4)
        pin_num = match.group(5)
        pins[pin_num] = (pin_name, rel_x, rel_y, angle)

    return pins

def parse_symbol_instances(content):
    """Parse symbol instances to get positions.
    Returns dict: {lib_id: (x, y, rotation, ref)}
    """
    instances = {}

    # Pattern: (symbol (lib_id "...") (at x y rot) ... (property "Reference" "Jxx"
    pattern = r'\(symbol\s*\n?\s*\(lib_id\s+"([^"]+)"\)\s*\n?\s*\(at\s+([-\d.]+)\s+([-\d.]+)\s*(\d*)\)'

    for match in re.finditer(pattern, content):
        lib_id = match.group(1)
        x = float(match.group(2))
        y = float(match.group(3))
        rot = int(match.group(4)) if match.group(4) else 0

        # Find reference
        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', content[match.end():match.end()+500])
        ref = ref_match.group(1) if ref_match else ""

        instances[lib_id] = (x, y, rot, ref)

    return instances

def generate_global_label(label_name, x, y, angle):
    """Generate KiCad global_label s-expression.
    angle: 0=pointing right, 180=pointing left
    """
    label_uuid = generate_uuid()

    # Justify based on direction
    if angle == 180:
        justify = "(justify mirror)"
    else:
        justify = ""

    label = f'''\t(global_label "{label_name}"
\t\t(shape bidirectional)
\t\t(at {x:.2f} {y:.2f} {angle})
\t\t(fields_autoplaced yes)
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.27 1.27)
\t\t\t)
\t\t\t{justify}
\t\t)
\t\t(uuid "{label_uuid}")
\t\t(property "Intersheetrefs" "${{INTERSHEET_REFS}}"
\t\t\t(at 0 0 0)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(hide yes)
\t\t\t)
\t\t)
\t)
'''
    return label

def generate_wire(x1, y1, x2, y2):
    """Generate KiCad wire s-expression."""
    wire_uuid = generate_uuid()
    return f'''\t(wire
\t\t(pts
\t\t\t(xy {x1:.2f} {y1:.2f}) (xy {x2:.2f} {y2:.2f})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type default)
\t\t)
\t\t(uuid "{wire_uuid}")
\t)
'''

def main():
    print("Adding global labels to connector.kicad_sch...")
    print("Mode: ALL pins (including GND, +12V, VCCO)")

    # Read current schematic
    with open(CONNECTOR_SCH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse symbol instances (get symbol positions)
    instances = parse_symbol_instances(content)
    print(f"\nFound {len(instances)} symbol instances")
    for lib_id, (x, y, rot, ref) in instances.items():
        if 'ACU5EV' in lib_id:
            print(f"  {ref}: {lib_id} at ({x}, {y}) rot={rot}")

    # Collect all labels and wires
    all_labels = []
    all_wires = []

    for conn_name, lib_id in CONNECTORS.items():
        if lib_id not in instances:
            print(f"Warning: Symbol {lib_id} not found in schematic")
            continue

        symbol_x, symbol_y, symbol_rot, ref = instances[lib_id]
        print(f"\nProcessing {conn_name} ({ref}) at ({symbol_x}, {symbol_y}) rot={symbol_rot}...")

        # Parse symbol definition for pin positions and names
        symbol_pins = parse_symbol_pins(content, lib_id)
        print(f"  Found {len(symbol_pins)} pins in symbol definition")

        for pin_num, (pin_name, rel_x, rel_y, pin_angle) in symbol_pins.items():
            # Calculate absolute position
            # pin_angle: 0=pin points right, 180=pin points left
            # For angle 0, the wire connects at the left end of the pin

            abs_x = symbol_x + rel_x
            abs_y = symbol_y + rel_y

            # Wire goes from pin end outward
            wire_length = 10  # mm

            if pin_angle == 0:
                # Pin points right, wire extends left
                wire_end_x = abs_x - wire_length
                wire_end_y = abs_y
                label_angle = 0  # Label points right
            elif pin_angle == 180:
                # Pin points left, wire extends right
                wire_end_x = abs_x + wire_length
                wire_end_y = abs_y
                label_angle = 180  # Label points left
            elif pin_angle == 90:
                # Pin points up, wire extends down
                wire_end_x = abs_x
                wire_end_y = abs_y - wire_length
                label_angle = 90
            elif pin_angle == 270:
                # Pin points down, wire extends up
                wire_end_x = abs_x
                wire_end_y = abs_y + wire_length
                label_angle = 270
            else:
                wire_end_x = abs_x - wire_length
                wire_end_y = abs_y
                label_angle = 0

            # Generate wire
            wire = generate_wire(abs_x, abs_y, wire_end_x, wire_end_y)
            all_wires.append(wire)

            # Generate label at end of wire
            label = generate_global_label(pin_name, wire_end_x, wire_end_y, label_angle)
            all_labels.append(label)

        print(f"  Generated {len(symbol_pins)} labels for {conn_name}")

    print(f"\nTotal: {len(all_labels)} labels, {len(all_wires)} wires")

    # Insert labels and wires before the closing parenthesis
    insert_pos = content.rfind(')')
    new_content = '\n'.join(all_labels) + '\n' + '\n'.join(all_wires) + '\n'
    content = content[:insert_pos] + new_content + content[insert_pos:]

    # Write to new file
    output_file = CONNECTOR_SCH.replace('.kicad_sch', '_with_labels.kicad_sch')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nOutput written to: {output_file}")

if __name__ == '__main__':
    main()
