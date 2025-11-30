#!/usr/bin/env python3
"""
Fix annotations v2 - Properly handle KiCad schematic structure
Skips lib_symbols section and only modifies actual symbol instances
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


def find_lib_symbols_end(content):
    """Find where lib_symbols section ends"""
    # Find (lib_symbols and then find its closing )
    start = content.find('(lib_symbols')
    if start == -1:
        return 0

    # Count parentheses to find matching close
    depth = 0
    for i, c in enumerate(content[start:], start):
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return i + 1
    return 0


def parse_symbols_after_lib(content, lib_end):
    """Parse symbol instances after lib_symbols section"""
    symbols = []

    # Find all (symbol blocks after lib_symbols
    # Pattern: (symbol (lib_id "...")  ... (at x y) ... (property "Reference" "X?") ... )
    symbol_section = content[lib_end:]

    # Match symbol blocks - they start with (symbol (lib_id
    pattern = r'\(symbol\s+\(lib_id\s+"([^"]+)"\)(.*?)\n\t\)'

    for match in re.finditer(pattern, symbol_section, re.DOTALL):
        lib_id = match.group(1)
        inner = match.group(2)

        # Get position in original content
        abs_start = lib_end + match.start()
        abs_end = lib_end + match.end()

        # Extract reference
        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', inner)
        ref = ref_match.group(1) if ref_match else ""

        # Extract value
        val_match = re.search(r'\(property\s+"Value"\s+"([^"]+)"', inner)
        value = val_match.group(1) if val_match else ""

        # Extract position
        at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)', inner)
        x = float(at_match.group(1)) if at_match else 0
        y = float(at_match.group(2)) if at_match else 0

        # Extract UUID
        uuid_match = re.search(r'\(uuid\s+"?([^"\)]+)"?\)', inner)
        uuid = uuid_match.group(1) if uuid_match else ""

        symbols.append({
            'lib_id': lib_id,
            'ref': ref,
            'value': value,
            'x': x,
            'y': y,
            'uuid': uuid,
            'start': abs_start,
            'end': abs_end,
        })

    return symbols


def main():
    print("=" * 60)
    print("Fix Annotations v2 - Proper KiCad Structure Handling")
    print("=" * 60)

    # Global reference counters
    ref_counters = defaultdict(int)

    # Collect all symbols from all files first
    all_symbols = []

    print("\n[Step 1] Parsing schematic files...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            print(f"  SKIP: {sch_file} not found")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find end of lib_symbols
        lib_end = find_lib_symbols_end(content)
        print(f"  {sch_file}: lib_symbols ends at position {lib_end}")

        # Parse symbols after lib_symbols
        symbols = parse_symbols_after_lib(content, lib_end)

        for sym in symbols:
            sym['file'] = sch_file
            sym['filepath'] = filepath
            all_symbols.append(sym)

        print(f"    Found {len(symbols)} symbol instances")

    print(f"\n  Total symbols: {len(all_symbols)}")

    # Step 2: Assign unique references
    print("\n[Step 2] Assigning unique references...")

    # Group by prefix
    by_prefix = defaultdict(list)
    for sym in all_symbols:
        prefix_match = re.match(r'^([A-Za-z_#]+)', sym['ref'])
        if prefix_match:
            prefix = prefix_match.group(1)
            # Skip power symbols
            if prefix not in ['#PWR', '#FLG']:
                sym['prefix'] = prefix
                by_prefix[prefix].append(sym)

    # Sort each group by file order, then position
    file_order = {f: i for i, f in enumerate(SCHEMATIC_FILES)}

    for prefix, symbols in by_prefix.items():
        symbols.sort(key=lambda s: (file_order.get(s['file'], 99), s['y'], s['x']))

        for i, sym in enumerate(symbols, 1):
            sym['new_ref'] = f"{prefix}{i}"

        print(f"  {prefix}: 1-{len(symbols)}")

    # Step 3: Apply changes to each file
    print("\n[Step 3] Applying changes...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find end of lib_symbols to only modify after that
        lib_end = find_lib_symbols_end(content)

        # Split content
        lib_section = content[:lib_end]
        instance_section = content[lib_end:]

        changes = 0

        # Get symbols for this file
        file_symbols = [s for s in all_symbols if s['file'] == sch_file and 'new_ref' in s]

        # Sort by position in file (reverse to maintain positions)
        file_symbols.sort(key=lambda s: s['start'], reverse=True)

        for sym in file_symbols:
            old_ref = sym['ref']
            new_ref = sym['new_ref']

            if old_ref == new_ref:
                continue

            # Calculate position relative to instance_section
            rel_start = sym['start'] - lib_end
            rel_end = sym['end'] - lib_end

            # Extract the symbol block
            symbol_block = instance_section[rel_start:rel_end]

            # Replace reference in this specific block
            new_block = re.sub(
                r'(\(property\s+"Reference"\s+)"[^"]+"',
                rf'\1"{new_ref}"',
                symbol_block,
                count=1
            )

            if new_block != symbol_block:
                instance_section = instance_section[:rel_start] + new_block + instance_section[rel_end:]
                changes += 1

        # Recombine
        new_content = lib_section + instance_section

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  {sch_file}: {changes} references updated")

    # Step 4: Verify
    print("\n[Step 4] Verification...")

    remaining_questions = 0
    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        lib_end = find_lib_symbols_end(content)
        instance_section = content[lib_end:]

        # Count remaining ?
        questions = len(re.findall(r'\(property\s+"Reference"\s+"[A-Za-z]+\?"', instance_section))
        if questions > 0:
            print(f"  WARNING: {sch_file} still has {questions} unannotated symbols")
            remaining_questions += questions
        else:
            print(f"  {sch_file}: OK")

    print("\n" + "=" * 60)
    if remaining_questions == 0:
        print("SUCCESS! All references are now unique.")
    else:
        print(f"WARNING: {remaining_questions} symbols still need annotation")
    print("=" * 60)


if __name__ == "__main__":
    main()
