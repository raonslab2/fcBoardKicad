#!/usr/bin/env python3
"""
Check which footprints are missing 3D models
"""

import re
import os

def get_unique_footprints(pcb_path):
    """Extract unique footprints from PCB file"""
    with open(pcb_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'\(footprint "([^"]+)"'
    footprints = set(re.findall(pattern, content))
    return sorted(footprints)

def main():
    pcb_path = r"D:\git2\fcBoardKicad\fcBoard.kicad_pcb"

    footprints = get_unique_footprints(pcb_path)

    print("=" * 70)
    print("UNIQUE FOOTPRINTS IN PCB")
    print("=" * 70)
    print(f"\nTotal unique footprints: {len(footprints)}\n")

    for fp in footprints:
        print(f"  {fp}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
