#!/usr/bin/env python3
"""
Simple fix: Replace all X? with sequential numbers across all files
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

PREFIXES = ['U', 'R', 'C', 'L', 'D', 'J', 'Y', 'FB', 'SW', 'Q', 'F']


def main():
    print("=" * 60)
    print("Simple Reference Fix")
    print("=" * 60)

    # Global counters
    counters = defaultdict(int)

    # First, find the highest existing number for each prefix
    print("\n[Step 1] Finding existing references...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for prefix in PREFIXES:
            # Find all existing numbered references
            pattern = rf'"{prefix}(\d+)"'
            for match in re.finditer(pattern, content):
                num = int(match.group(1))
                if num > counters[prefix]:
                    counters[prefix] = num

    print("  Current max:")
    for prefix in sorted(counters.keys()):
        if counters[prefix] > 0:
            print(f"    {prefix}: {counters[prefix]}")

    # Now replace all X? patterns
    print("\n[Step 2] Replacing X? patterns...")

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changes = 0
        original = content

        for prefix in PREFIXES:
            # Replace "X?" with sequential numbers
            pattern = rf'"{prefix}\?"'

            def replacer(match):
                nonlocal changes
                counters[prefix] += 1
                changes += 1
                return f'"{prefix}{counters[prefix]}"'

            content = re.sub(pattern, replacer, content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  {sch_file}: {changes} references fixed")
        else:
            print(f"  {sch_file}: no changes needed")

    # Final counts
    print("\n[Step 3] Final reference ranges:")
    for prefix in sorted(counters.keys()):
        if counters[prefix] > 0:
            print(f"    {prefix}: 1-{counters[prefix]}")

    # Verify
    print("\n[Step 4] Verification...")
    remaining = 0

    for sch_file in SCHEMATIC_FILES:
        filepath = os.path.join(PROJECT_DIR, sch_file)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        file_remaining = 0
        for prefix in PREFIXES:
            matches = re.findall(rf'"{prefix}\?"', content)
            file_remaining += len(matches)

        if file_remaining > 0:
            print(f"  WARNING: {sch_file} has {file_remaining} remaining ?")
            remaining += file_remaining
        else:
            print(f"  {sch_file}: OK")

    print("\n" + "=" * 60)
    if remaining == 0:
        print("SUCCESS! All references annotated.")
    else:
        print(f"WARNING: {remaining} references still need annotation")
    print("=" * 60)


if __name__ == "__main__":
    main()
