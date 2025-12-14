#!/usr/bin/env python3
"""
Automatic component placement for ACU5EV SoM Carrier Board PCB
Board size: 150mm x 100mm with offset (100, 100)
Board area: X=100-250, Y=100-200
"""

import re

def parse_components(content):
    """Extract all component references and their current positions from PCB file"""
    components = {}

    # Find each footprint block and extract info
    # Structure: (footprint "name" (placed ...) (layer ...) (uuid ...) (at X Y [angle]) ... (property "Reference" "REF")

    # Split by footprint blocks
    fp_pattern = r'\(footprint\s+"([^"]+)"\s*\n\s+\(placed[^)]+\)\s*\n\s+\(layer[^)]+\)\s*\n\s+\(uuid[^)]+\)\s*\n\s+\(at\s+([\d.]+)\s+([\d.]+)(?:\s+([\d.]+))?\)'

    # Find all footprint headers with position
    for match in re.finditer(fp_pattern, content):
        footprint = match.group(1)
        x = float(match.group(2))
        y = float(match.group(3))
        angle = float(match.group(4)) if match.group(4) else 0

        # Find the reference within the next ~2000 chars after this match
        start_pos = match.end()
        end_pos = min(start_pos + 2000, len(content))
        block = content[start_pos:end_pos]

        ref_match = re.search(r'property\s+"Reference"\s+"([^"]+)"', block)
        if ref_match:
            ref = ref_match.group(1)
            components[ref] = {
                'footprint': footprint,
                'x': x,
                'y': y,
                'angle': angle
            }

    return components

def get_placement_map():
    """Define target positions for all components
    Board: 100,100 to 250,200 (150x100mm)
    """
    placement = {}

    # ==========================================
    # CONNECTORS - Board edges
    # ==========================================

    # DC Jack J16 - Left side
    placement['J16'] = (108, 150, 180)  # DC barrel jack, facing left

    # USB Connectors J1-J5 - Right side (vertical stack)
    for i, ref in enumerate(['J1', 'J2', 'J3', 'J4', 'J5']):
        placement[ref] = (242, 115 + i * 12, 90)  # USB facing right

    # RJ45 J6 - Right side
    placement['J6'] = (230, 140, 90)  # RJ45 facing right

    # HDMI Connectors - Right side
    placement['J23'] = (235, 165, 90)  # HDMI IN
    placement['J24'] = (235, 185, 90)  # HDMI OUT

    # Pin Headers J7-J12 - Center area for SoM connection
    placement['J7'] = (150, 120, 0)
    placement['J8'] = (150, 130, 0)
    placement['J9'] = (150, 140, 0)
    placement['J10'] = (160, 120, 0)
    placement['J11'] = (160, 130, 0)
    placement['J12'] = (160, 140, 0)

    # ==========================================
    # POWER SECTION - Left side
    # ==========================================

    # Power regulator U26 (LM2596)
    placement['U26'] = (125, 145, 0)

    # Inductors near power regulator
    placement['L4'] = (115, 155, 0)
    placement['L5'] = (125, 155, 0)
    placement['L6'] = (135, 155, 0)

    # Power capacitors
    placement['C20'] = (115, 165, 0)
    placement['C21'] = (125, 165, 0)
    placement['C22'] = (135, 165, 0)

    # ==========================================
    # ETHERNET SECTION - Right upper
    # ==========================================

    # Ethernet PHY U1
    placement['U1'] = (200, 130, 0)

    # Crystals for Ethernet
    placement['Y1'] = (190, 125, 0)
    placement['Y2'] = (190, 135, 0)

    # ==========================================
    # HDMI SECTION - Center-right
    # ==========================================

    # HDMI TX/RX ICs
    placement['U43'] = (195, 165, 0)  # HDMI IC 1
    placement['U44'] = (195, 180, 0)  # HDMI IC 2

    # Level shifters for HDMI
    placement['U41'] = (180, 165, 0)  # TPD12S016
    placement['U42'] = (180, 180, 0)  # TXB0108

    # HDMI crystals
    placement['Y9'] = (185, 172, 0)
    placement['Y10'] = (185, 188, 0)

    # ==========================================
    # USB SECTION ICs - Right side
    # ==========================================

    # USB Hub IC
    placement['U2'] = (215, 120, 0)
    placement['U3'] = (215, 135, 0)
    placement['U4'] = (215, 150, 0)
    placement['U5'] = (205, 120, 0)
    placement['U6'] = (205, 135, 0)
    placement['U7'] = (205, 150, 0)
    placement['U8'] = (225, 120, 0)

    # ==========================================
    # PERIPHERALS SECTION - Bottom
    # ==========================================

    # UART CP2102N
    placement['U27'] = (130, 180, 0)
    placement['U28'] = (145, 180, 0)

    # Other peripheral ICs
    for i, ref in enumerate(['U9', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17']):
        row = i // 3
        col = i % 3
        placement[ref] = (140 + col * 15, 110 + row * 12, 0)

    # ==========================================
    # SWITCHES - Accessible location
    # ==========================================

    placement['SW1'] = (110, 185, 0)
    placement['SW2'] = (120, 185, 0)

    # ==========================================
    # LEDs - Status indicator area
    # ==========================================

    # Power LEDs
    for i in range(1, 17):
        ref = f'D{i}'
        row = (i - 1) // 4
        col = (i - 1) % 4
        placement[ref] = (110 + col * 6, 110 + row * 6, 0)

    # ==========================================
    # RESISTORS - Near their associated ICs
    # ==========================================

    # General resistor placement in available space
    for i in range(1, 25):
        ref = f'R{i}'
        row = (i - 1) // 6
        col = (i - 1) % 6
        placement[ref] = (165 + col * 5, 105 + row * 5, 0)

    # ==========================================
    # CAPACITORS - Near ICs
    # ==========================================

    # Additional capacitors
    for i in range(23, 38):
        ref = f'C{i}'
        idx = i - 23
        row = idx // 5
        col = idx % 5
        placement[ref] = (140 + col * 6, 190 + row * 5, 0)

    # ==========================================
    # MOUNTING HOLES - Corners (already placed)
    # ==========================================

    placement['MH1'] = (105, 105, 0)
    placement['MH2'] = (245, 105, 0)
    placement['MH3'] = (105, 195, 0)
    placement['MH4'] = (245, 195, 0)

    return placement

def update_component_position(content, ref, x, y, angle=0):
    """Update the position of a component in the PCB file"""

    # Find the footprint block containing this reference
    # We need to find the (at X Y) line that comes BEFORE the reference property

    # Strategy: Find the reference, then search backwards for the (at line
    ref_pattern = rf'property\s+"Reference"\s+"{re.escape(ref)}"'
    ref_match = re.search(ref_pattern, content)

    if not ref_match:
        return content, False

    # Find the start of this footprint block (search backwards for "(footprint")
    ref_pos = ref_match.start()

    # Search backwards from reference position to find the footprint start
    search_start = max(0, ref_pos - 3000)  # footprint block is usually within 3000 chars
    block_before = content[search_start:ref_pos]

    # Find the last (footprint occurrence before the reference
    fp_matches = list(re.finditer(r'\(footprint\s+"[^"]+"', block_before))
    if not fp_matches:
        return content, False

    # Get the absolute position of the footprint start
    fp_rel_pos = fp_matches[-1].start()
    fp_abs_pos = search_start + fp_rel_pos

    # Now find the (at X Y) line within this footprint block
    # It should be within the first 500 chars of the footprint block
    fp_block_start = content[fp_abs_pos:fp_abs_pos + 500]

    at_match = re.search(r'\(at\s+([\d.]+)\s+([\d.]+)(?:\s+([\d.]+))?\)', fp_block_start)
    if not at_match:
        return content, False

    # Calculate the absolute position of the (at line
    at_rel_start = at_match.start()
    at_rel_end = at_match.end()
    at_abs_start = fp_abs_pos + at_rel_start
    at_abs_end = fp_abs_pos + at_rel_end

    # Create the new (at line
    new_at = f"(at {x} {y})" if angle == 0 else f"(at {x} {y} {angle})"

    # Replace in content
    new_content = content[:at_abs_start] + new_at + content[at_abs_end:]

    return new_content, True

def place_components(pcb_path):
    """Main function to place all components"""

    print(f"Reading PCB file: {pcb_path}")
    with open(pcb_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse existing components
    components = parse_components(content)
    print(f"Found {len(components)} components in PCB")

    for ref, info in sorted(components.items()):
        print(f"  {ref}: {info['footprint'][:40]:<40} at ({info['x']:.1f}, {info['y']:.1f})")

    # Get placement map
    placement = get_placement_map()
    print(f"\nPlacement defined for {len(placement)} components")

    # Update positions
    updated_count = 0
    for ref, (x, y, angle) in placement.items():
        if ref in components:
            content, success = update_component_position(content, ref, x, y, angle)
            if success:
                old = components[ref]
                print(f"  Moved {ref}: ({old['x']:.1f}, {old['y']:.1f}) -> ({x}, {y}, {angle}°)")
                updated_count += 1
            else:
                print(f"  Warning: Could not update {ref}")
        else:
            print(f"  Skipped {ref}: not found in PCB")

    # Save updated PCB
    if updated_count > 0:
        print(f"\nSaving PCB with {updated_count} updated positions...")
        with open(pcb_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Done!")
    else:
        print("\nNo components were updated.")

    return updated_count

if __name__ == "__main__":
    pcb_path = r"D:\git2\fcBoardKicad\fcBoard.kicad_pcb"
    place_components(pcb_path)
