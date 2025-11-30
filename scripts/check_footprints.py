#!/usr/bin/env python3
"""
Check footprint assignments in KiCad schematics
Supports both KiCad 8 and KiCad 9 formats
"""

import os
import re
from collections import defaultdict

def extract_lib_symbols_footprints(sch_content):
    """Extract footprints from lib_symbols section - supports KiCad 8 and 9"""
    lib_fps = {}

    # Pattern for KiCad 8 format (single line property)
    # (property "Footprint" "Package:Name" (at ...
    pattern_v8 = re.compile(
        r'\(symbol\s+"([^"]+)"\s*(?:\(pin_names.*?\))?\s*(?:\(exclude_from_sim\s+\w+\))?\s*\(in_bom\s+\w+\)\s+\(on_board\s+\w+\).*?'
        r'\(property\s+"Footprint"\s+"([^"]*)"',
        re.DOTALL
    )

    # Pattern for KiCad 9 format (multi-line with tabs)
    # (symbol "Name"
    #   ...
    #   (property "Footprint" "Package:Name"
    pattern_v9 = re.compile(
        r'\(symbol\s+"([^"]+)".*?'
        r'\(property\s+"Footprint"\s+"([^"]*)"',
        re.DOTALL
    )

    # Try both patterns
    for match in pattern_v9.finditer(sch_content):
        lib_id = match.group(1)
        footprint = match.group(2)
        # Don't overwrite with sub-symbol definitions
        if '_0_1' not in lib_id and '_1_1' not in lib_id:
            lib_fps[lib_id] = footprint

    return lib_fps

def extract_symbol_instances(sch_content, filename, lib_fps):
    """Extract symbol instances from schematic"""
    components = []

    # Pattern for symbol instances
    # KiCad 8: (symbol\n    (lib_id "XXX")\n    (at X Y...) ... (property "Reference" "YYY" ...
    # KiCad 9: (symbol\n\t\t(lib_id "XXX")\n\t\t(at X Y...) ... (property "Reference" "YYY" ...
    instance_pattern = re.compile(
        r'\(symbol\s*\n\s*\(lib_id\s+"([^"]+)"\)\s*\n\s*\(at\s+[\d.-]+\s+[\d.-]+.*?\(property\s+"Reference"\s+"([^"]+)"',
        re.DOTALL
    )

    for match in instance_pattern.finditer(sch_content):
        lib_id = match.group(1)
        ref = match.group(2)

        # Skip power symbols
        if lib_id.startswith('power:') or ref.startswith('#'):
            continue

        footprint = lib_fps.get(lib_id, '')

        components.append({
            'lib_id': lib_id,
            'reference': ref,
            'footprint': footprint,
            'file': filename
        })

    return components


def check_footprints(project_dir):
    """Check all schematics for footprint assignments"""

    schematic_files = [
        'fcBoard.kicad_sch',
        'fcBoard_Power.kicad_sch',
        'fcBoard_USB.kicad_sch',
        'fcBoard_Ethernet.kicad_sch',
        'fcBoard_HDMI.kicad_sch',
        'fcBoard_Peripherals.kicad_sch',
    ]

    all_components = []
    missing_footprints = []
    assigned_footprints = []

    for sch_file in schematic_files:
        sch_path = os.path.join(project_dir, sch_file)
        if os.path.exists(sch_path):
            with open(sch_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Get lib_symbols footprints
            lib_fps = extract_lib_symbols_footprints(content)

            # Debug: print found footprints
            fps_with_values = {k: v for k, v in lib_fps.items() if v}
            if fps_with_values:
                print(f"\n[{sch_file}] Found {len(fps_with_values)} lib_symbols with footprints:")
                for lib_id, fp in sorted(fps_with_values.items()):
                    print(f"  {lib_id}: {fp}")

            # Get symbol instances
            components = extract_symbol_instances(content, sch_file, lib_fps)
            all_components.extend(components)

            for comp in components:
                if comp['footprint']:
                    assigned_footprints.append(comp)
                else:
                    missing_footprints.append(comp)
        else:
            print(f"Warning: {sch_file} not found")

    # Print report
    print("\n" + "=" * 70)
    print("FOOTPRINT ASSIGNMENT REPORT")
    print("=" * 70)
    print(f"\nTotal components: {len(all_components)}")
    print(f"With footprint: {len(assigned_footprints)}")
    print(f"Missing footprint: {len(missing_footprints)}")

    if assigned_footprints:
        print("\n" + "-" * 70)
        print("ASSIGNED FOOTPRINTS:")
        print("-" * 70)

        # Group by file
        by_file = defaultdict(list)
        for comp in assigned_footprints:
            by_file[comp['file']].append(comp)

        for filename, comps in sorted(by_file.items()):
            print(f"\n[{filename}]")
            for comp in sorted(comps, key=lambda x: x['reference']):
                fp_short = comp['footprint']
                if len(fp_short) > 45:
                    fp_short = '...' + fp_short[-42:]
                print(f"  {comp['reference']:12s} -> {fp_short}")

    if missing_footprints:
        print("\n" + "-" * 70)
        print("MISSING FOOTPRINTS (Need assignment):")
        print("-" * 70)

        by_file = defaultdict(list)
        for comp in missing_footprints:
            by_file[comp['file']].append(comp)

        for filename, comps in sorted(by_file.items()):
            print(f"\n[{filename}]")
            for comp in sorted(comps, key=lambda x: x['reference']):
                print(f"  {comp['reference']:12s} ({comp['lib_id']})")

    # Summary of unique footprints used
    if assigned_footprints:
        print("\n" + "-" * 70)
        print("UNIQUE FOOTPRINTS USED:")
        print("-" * 70)

        unique_fps = set(comp['footprint'] for comp in assigned_footprints if comp['footprint'])
        for fp in sorted(unique_fps):
            count = sum(1 for c in assigned_footprints if c['footprint'] == fp)
            print(f"  {fp} ({count}x)")

    print("\n" + "=" * 70)
    print(f"Summary: {len(assigned_footprints)}/{len(all_components)} components have footprints")
    if missing_footprints:
        print(f"         {len(missing_footprints)} components need footprint assignment")
    print("=" * 70)

    return all_components, missing_footprints, assigned_footprints


if __name__ == "__main__":
    project_dir = r"D:\git2\fcBoardKicad"
    check_footprints(project_dir)
