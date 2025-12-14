# ==============================================================================
# DEPRECATED - 이 스크립트는 더 이상 공식 실행 경로가 아닙니다.
#
# 정식 실행 방법:
#   python -m kicad_auto_builder.cli validate <yaml>
#   python -m kicad_auto_builder.cli build <yaml>
#
# 이 파일은 레거시 레퍼런스 용도로만 보관됩니다.
# ==============================================================================

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
