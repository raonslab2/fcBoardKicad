#!/usr/bin/env python3
"""
Fix all references including symbol_instances section
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

# Prefixes to annotate (skip power symbols)
ANNOTATE_PREFIXES = ['U', 'R', 'C', 'L', 'D', 'J', 'Y', 'FB', 'SW', 'Q', 'F']


def find_section_end(content, section_name):
    """Find where a section ends by counting parentheses"""
    start = content.find(f'({section_name}')
    if start == -1:
        return -1, -1

    depth = 0
    for i, c in enumerate(content[start:], start):
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return start, i + 1
    return start, len(content)


def main():
    print("=" * 60)
    print("Fix All References (including symbol_instances)")
    print("=" * 60)

    # Global counters per prefix
    global_counters = defaultdict(int)

    # First pass: collect all symbols and assign numbers
    all_assignments = []  # [(file, uuid, old_ref, new_ref), ...]

    print("\n[Pass 1] Collecting and assigning references...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find lib_symbols section to skip it
        lib_start, lib_end = find_section_end(content, 'lib_symbols')

        # Find all symbols after lib_symbols
        search_content = content[lib_end:] if lib_end > 0 else content

        # Pattern for symbol with uuid
        symbol_pattern = r'\(symbol\s+\(lib_id\s+"[^"]+"\)(.*?)\n\t\)'

        symbols = []
        for match in re.finditer(symbol_pattern, search_content, re.DOTALL):
            inner = match.group(1)

            # Get reference
            ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
            if not ref_match:
                continue
            ref = ref_match.group(1)

            # Get UUID
            uuid_match = re.search(r'\(uuid\s+"?([^"\)]+)"?\)', inner)
            if not uuid_match:
                continue
            uuid = uuid_match.group(1)

            # Get position for sorting
            at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', inner)
            x = float(at_match.group(1)) if at_match else 0
            y = float(at_match.group(2)) if at_match else 0

            # Get prefix
            prefix_match = re.match(r'^([A-Za-z_#]+)', ref)
            if not prefix_match:
                continue
            prefix = prefix_match.group(1)

            # Skip power symbols
            if prefix in ['#PWR', '#FLG', 'PWR']:
                continue

            if prefix not in ANNOTATE_PREFIXES:
                continue

            symbols.append({
                'uuid': uuid,
                'ref': ref,
                'prefix': prefix,
                'x': x,
                'y': y,
            })

        # Sort by y then x
        symbols.sort(key=lambda s: (s['y'], s['x']))

        # Assign new references
        for sym in symbols:
            global_counters[sym['prefix']] += 1
            new_ref = f"{sym['prefix']}{global_counters[sym['prefix']]}"
            all_assignments.append((sch_file, sym['uuid'], sym['ref'], new_ref))

        print(f"  {sch_file}: {len(symbols)} symbols")

    print(f"\n  Reference ranges:")
    for prefix in sorted(global_counters.keys()):
        print(f"    {prefix}: 1-{global_counters[prefix]}")

    # Second pass: apply changes
    print("\n[Pass 2] Applying changes...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get assignments for this file
        file_assignments = [(uuid, old, new) for (f, uuid, old, new) in all_assignments if f == sch_file]

        changes = 0
        for uuid, old_ref, new_ref in file_assignments:
            if old_ref == new_ref:
                continue

            # Replace in property "Reference"
            # Find the symbol block with this UUID and replace its reference
            pattern = rf'(\(symbol\s+\(lib_id\s+"[^"]+"\).*?\(uuid\s+"{uuid}"\).*?\(property\s+"Reference"\s+)"[^"]+"'

            def replace_in_symbol(m):
                return m.group(1) + f'"{new_ref}"'

            new_content, n = re.subn(pattern, replace_in_symbol, content, flags=re.DOTALL)
            if n > 0:
                content = new_content
                changes += n

            # Also replace in symbol_instances section: (reference "X?")
            # This is inside (path "/uuid" (reference "X?") (unit 1))
            inst_pattern = rf'(\(path\s+"/[^"]*{uuid}"[^)]*\(reference\s+)"[^"]+"'
            new_content, n = re.subn(inst_pattern, rf'\1"{new_ref}"', content)
            if n > 0:
                content = new_content

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  {sch_file}: {len(file_assignments)} references processed")

    # Verification
    print("\n[Pass 3] Verification...")

    remaining = 0
    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find lib_symbols end
        lib_start, lib_end = find_section_end(content, 'lib_symbols')
        check_content = content[lib_end:] if lib_end > 0 else content

        # Count remaining ? for annotatable prefixes
        for prefix in ANNOTATE_PREFIXES:
            pattern = rf'"{prefix}\?"'
            matches = re.findall(pattern, check_content)
            if matches:
                print(f"  WARNING: {sch_file} has {len(matches)} remaining {prefix}?")
                remaining += len(matches)

        if not any(re.findall(rf'"{p}\?"', check_content) for p in ANNOTATE_PREFIXES):
            print(f"  {sch_file}: OK")

    print("\n" + "=" * 60)
    if remaining == 0:
        print("SUCCESS! All references annotated.")
    else:
        print(f"WARNING: {remaining} references still need annotation")
    print("=" * 60)


if __name__ == "__main__":
    main()
