#!/usr/bin/env python3
"""
Fix duplicate annotations by re-annotating all schematics with globally unique references
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


def reset_and_annotate():
    """Reset all references to ? and then re-annotate globally"""
    print("=" * 60)
    print("Fix Duplicate Annotations")
    print("=" * 60)

    # Step 1: Reset all references to X?
    print("\n[Step 1] Resetting references...")
    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reset references like U1, R1, C1 to U?, R?, C?
        # But skip power symbols (#PWR, #FLG)
        pattern = r'(\(property\s+"Reference"\s+")([A-Za-z]+)(\d+)(")'

        def reset_ref(match):
            prefix = match.group(2)
            if prefix in ['#PWR', '#FLG', 'PWR']:
                return match.group(0)
            return f'{match.group(1)}{prefix}?{match.group(4)}'

        new_content = re.sub(pattern, reset_ref, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  Reset: {sch_file}")

    # Step 2: Collect all symbols from all files
    print("\n[Step 2] Collecting symbols...")
    all_symbols = []

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find symbols
        symbol_pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)\n'

        for match in re.finditer(symbol_pattern, content, re.DOTALL):
            lib_id = match.group(1)
            inner = match.group(2)

            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
            ref = ref_match.group(1) if ref_match else ""

            val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', inner)
            value = val_match.group(1) if val_match else ""

            at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', inner)
            x = float(at_match.group(1)) if at_match else 0
            y = float(at_match.group(2)) if at_match else 0

            uuid_match = re.search(r'\(uuid\s+"?([^"\)]+)"?\)', inner)
            uuid = uuid_match.group(1) if uuid_match else ""

            prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
            prefix = prefix_match.group(1) if prefix_match else ""

            if prefix in ['#PWR', '#FLG', 'PWR']:
                continue

            all_symbols.append({
                'file': sch_file,
                'prefix': prefix,
                'ref': ref,
                'value': value,
                'uuid': uuid,
                'x': x,
                'y': y
            })

    print(f"  Found {len(all_symbols)} symbols")

    # Step 3: Sort and assign new references
    print("\n[Step 3] Assigning unique references...")

    # Group by prefix
    by_prefix = defaultdict(list)
    for sym in all_symbols:
        by_prefix[sym['prefix']].append(sym)

    # Sort each group by file order, then position
    file_order = {f: i for i, f in enumerate(SCHEMATIC_FILES)}

    assignments = {}  # uuid -> new_ref

    for prefix, symbols in by_prefix.items():
        # Sort by file, then y (top to bottom), then x (left to right)
        symbols.sort(key=lambda s: (file_order.get(s['file'], 99), s['y'], s['x']))

        for i, sym in enumerate(symbols, 1):
            new_ref = f"{prefix}{i}"
            assignments[sym['uuid']] = new_ref

        print(f"  {prefix}: 1-{len(symbols)}")

    # Step 4: Apply new references
    print("\n[Step 4] Applying new references...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changes = 0

        # Process each symbol
        def update_symbol(match):
            nonlocal changes
            full = match.group(0)
            inner = match.group(2)

            # Get UUID
            uuid_match = re.search(r'\(uuid\s+"?([^"\)]+)"?\)', inner)
            if not uuid_match:
                return full
            uuid = uuid_match.group(1)

            if uuid not in assignments:
                return full

            new_ref = assignments[uuid]

            # Replace reference
            ref_pattern = r'(\(property\s+"Reference"\s+)"([^"]+)"'
            new_full = re.sub(ref_pattern, rf'\1"{new_ref}"', full, count=1)

            if new_full != full:
                changes += 1

            return new_full

        symbol_pattern = r'(\(symbol\s+\(lib_id\s+"[^"]+"\)(.*?)\n\t\)\n)'
        new_content = re.sub(symbol_pattern, update_symbol, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  {sch_file}: {changes} references updated")

    print("\n" + "=" * 60)
    print("Done! All references are now unique.")
    print("=" * 60)


if __name__ == "__main__":
    reset_and_annotate()
