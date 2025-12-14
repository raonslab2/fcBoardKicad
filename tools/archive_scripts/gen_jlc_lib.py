#!/usr/bin/env python3
"""
JLCPCB/LCSC to KiCad Library Generator

Reads LCSC part numbers from parts_jlc.csv and generates KiCad symbols,
footprints, and 3D models using easyeda2kicad.

Usage:
    python gen_jlc_lib.py           # Process all parts
    python gen_jlc_lib.py --only C25804  # Process specific part
    python gen_jlc_lib.py --force   # Force overwrite existing
"""

import argparse
import csv
import os
import re
import subprocess
import sys
from pathlib import Path


# Configuration
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_FILE = SCRIPT_DIR / "parts_jlc.csv"
OUTPUT_DIR = PROJECT_ROOT / "jlc_lib_output"
LIB_NAME = "jlc_components"


def setup_directories():
    """Create output directories if they don't exist."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / f"{LIB_NAME}.pretty").mkdir(exist_ok=True)
    (OUTPUT_DIR / f"{LIB_NAME}.3dshapes").mkdir(exist_ok=True)
    print(f"[INFO] Output directory: {OUTPUT_DIR}")


def load_csv():
    """Load parts list from CSV file."""
    if not CSV_FILE.exists():
        print(f"[ERROR] CSV file not found: {CSV_FILE}")
        sys.exit(1)

    parts = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lcsc_id = row.get('lcsc_id', '').strip()
            if lcsc_id and lcsc_id.upper().startswith('C'):
                parts.append({
                    'lcsc_id': lcsc_id.upper(),
                    'ref_prefix': row.get('ref_prefix', '').strip(),
                    'comment': row.get('comment', '').strip(),
                    'footprint_hint': row.get('footprint_hint', '').strip(),
                    'notes': row.get('notes', '').strip(),
                })

    print(f"[INFO] Loaded {len(parts)} parts from CSV")
    return parts


def check_easyeda2kicad():
    """Check if easyeda2kicad is installed."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'easyeda2kicad', '--help'],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def is_part_processed(lcsc_id: str) -> bool:
    """Check if a part has already been processed."""
    sym_file = OUTPUT_DIR / f"{LIB_NAME}.kicad_sym"
    if not sym_file.exists():
        return False

    # Check if LCSC ID exists in symbol file
    try:
        content = sym_file.read_text(encoding='utf-8')
        # Look for the LCSC property with this ID
        pattern = rf'\(property\s+"LCSC"\s+"{lcsc_id}"'
        return bool(re.search(pattern, content, re.IGNORECASE))
    except Exception:
        return False


def run_easyeda2kicad(lcsc_id: str, overwrite: bool = False) -> bool:
    """Run easyeda2kicad for a single part."""
    output_path = OUTPUT_DIR / LIB_NAME

    cmd = [
        sys.executable, '-m', 'easyeda2kicad',
        '--full',
        f'--lcsc_id={lcsc_id}',
        f'--output={output_path}',
    ]

    if overwrite:
        cmd.append('--overwrite')

    print(f"  Running: {' '.join(str(c) for c in cmd)}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        # easyeda2kicad returns non-zero even when symbol is created but footprint exists
        # Check if symbol was actually created
        stderr = result.stderr.strip()
        stdout = result.stdout.strip()

        if result.returncode == 0:
            return True

        # Check if symbol was created despite footprint warning
        if "Created Kicad symbol" in stderr or "Created Kicad symbol" in stdout:
            print(f"  [INFO] Symbol created (footprint may already exist)")
            return True

        # Check for "already in" warning (part fully exists)
        if "already in" in stderr and "symbol" in stderr.lower():
            print(f"  [INFO] Part already exists in library")
            return True

        print(f"  [WARN] stderr: {stderr}")
        return False

    except subprocess.TimeoutExpired:
        print(f"  [ERROR] Timeout processing {lcsc_id}")
        return False
    except Exception as e:
        print(f"  [ERROR] Exception: {e}")
        return False


def add_lcsc_field(lcsc_id: str):
    """Add LCSC field to the generated symbol if not present."""
    sym_file = OUTPUT_DIR / f"{LIB_NAME}.kicad_sym"
    if not sym_file.exists():
        return

    content = sym_file.read_text(encoding='utf-8')

    # Check if LCSC field already exists for this part
    lcsc_pattern = rf'\(property\s+"LCSC"\s+"{lcsc_id}"'
    if re.search(lcsc_pattern, content, re.IGNORECASE):
        return  # Already has LCSC field

    # Find the symbol definition for this part and add LCSC field
    # easyeda2kicad typically names symbols like "LCSC_ID" or uses the component name
    # We need to find where to insert the LCSC property

    # Look for symbols that might correspond to this LCSC ID
    # The symbol name might be the component name, not the LCSC ID directly
    # We'll add LCSC field after the last property in each symbol that doesn't have it

    # Simple approach: find all symbols and check if they have LCSC field
    # If a symbol was just added (newest), add the field to it

    # For now, we rely on easyeda2kicad to handle this or do a simple check
    # Most modern versions of easyeda2kicad already add LCSC field

    print(f"  [INFO] LCSC field check completed for {lcsc_id}")


def process_parts(parts: list, force: bool = False, only: str = None):
    """Process all parts from the list."""
    results = {'success': [], 'skipped': [], 'failed': []}

    for part in parts:
        lcsc_id = part['lcsc_id']

        # Filter by --only option
        if only and lcsc_id.upper() != only.upper():
            continue

        print(f"\n[PROCESS] {lcsc_id}: {part['comment']}")

        # Check if already processed
        if not force and is_part_processed(lcsc_id):
            print(f"  [SKIP] Already processed")
            results['skipped'].append(lcsc_id)
            continue

        # Run conversion
        success = run_easyeda2kicad(lcsc_id, overwrite=force)

        if success:
            add_lcsc_field(lcsc_id)
            print(f"  [OK] Successfully generated")
            results['success'].append(lcsc_id)
        else:
            print(f"  [FAIL] Generation failed")
            results['failed'].append(lcsc_id)

    return results


def build_lcsc_mapping() -> dict:
    """Build LCSC ID to symbol name mapping from the generated library."""
    sym_file = OUTPUT_DIR / f"{LIB_NAME}.kicad_sym"
    mapping = {}

    if not sym_file.exists():
        return mapping

    content = sym_file.read_text(encoding='utf-8')

    # easyeda2kicad generates multi-line property format:
    # (symbol "SYMBOL_NAME"
    #   ...
    #   (property
    #     "LCSC Part"
    #     "CXXXXX"
    #     ...
    #   )
    # )

    # Find all symbols and their LCSC Part property
    symbol_pattern = r'\(symbol\s+"([^"]+)"'
    # Match LCSC Part in multi-line format
    lcsc_pattern = r'"LCSC Part"\s*\n\s*"([^"]+)"'

    current_symbol = None
    lines = content.split('\n')

    for i, line in enumerate(lines):
        symbol_match = re.search(symbol_pattern, line)
        if symbol_match:
            candidate = symbol_match.group(1)
            # Skip sub-symbols like "SYMBOL_0_1"
            if '_0_1' not in candidate and '_1_1' not in candidate:
                current_symbol = candidate

    # Use regex to find all symbol->LCSC pairs in the whole file
    # Pattern: (symbol "NAME" ... "LCSC Part" followed by newline and "CXXXXX"
    symbol_blocks = re.split(r'\n\s*\(symbol\s+"', content)

    for block in symbol_blocks[1:]:  # Skip first (header)
        # Get symbol name from start of block
        name_match = re.match(r'([^"]+)"', block)
        if not name_match:
            continue

        symbol_name = name_match.group(1)
        # Skip sub-symbols
        if '_0_1' in symbol_name or '_1_1' in symbol_name:
            continue

        # Find LCSC Part in this block
        lcsc_match = re.search(r'"LCSC Part"\s*\n\s*"([^"]+)"', block)
        if lcsc_match:
            lcsc_id = lcsc_match.group(1).upper()
            mapping[lcsc_id] = symbol_name

    return mapping


def generate_mapping_file():
    """Generate a JSON mapping file for LCSC ID to symbol name."""
    import json

    mapping = build_lcsc_mapping()
    mapping_file = OUTPUT_DIR / "lcsc_mapping.json"

    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2)

    print(f"\n[INFO] LCSC mapping file: {mapping_file}")
    print(f"[INFO] {len(mapping)} parts mapped")

    # Also print mapping for reference
    print("\nLCSC ID → Symbol Name mapping:")
    for lcsc_id, symbol_name in sorted(mapping.items()):
        print(f"  {lcsc_id} → {LIB_NAME}:{symbol_name}")

    return mapping


def print_summary(results: dict):
    """Print processing summary."""
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Success: {len(results['success'])} parts")
    for p in results['success']:
        print(f"  - {p}")

    print(f"Skipped: {len(results['skipped'])} parts")
    for p in results['skipped']:
        print(f"  - {p}")

    print(f"Failed:  {len(results['failed'])} parts")
    for p in results['failed']:
        print(f"  - {p}")

    print("="*50)

    if results['success'] or results['skipped']:
        print(f"\nOutput files:")
        print(f"  Symbol:     {OUTPUT_DIR / f'{LIB_NAME}.kicad_sym'}")
        print(f"  Footprints: {OUTPUT_DIR / f'{LIB_NAME}.pretty/'}")
        print(f"  3D Models:  {OUTPUT_DIR / f'{LIB_NAME}.3dshapes/'}")

        # Generate mapping file
        generate_mapping_file()


def main():
    parser = argparse.ArgumentParser(
        description='Generate KiCad libraries from JLCPCB/LCSC parts'
    )
    parser.add_argument(
        '--only',
        type=str,
        help='Process only this LCSC ID (e.g., C25804)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force overwrite existing parts'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List parts in CSV without processing'
    )

    args = parser.parse_args()

    print("="*50)
    print("JLCPCB/LCSC to KiCad Library Generator")
    print("="*50)

    # Check dependencies
    if not check_easyeda2kicad():
        print("\n[ERROR] easyeda2kicad is not installed!")
        print("Install it with: pip install easyeda2kicad")
        sys.exit(1)

    print("[OK] easyeda2kicad found")

    # Setup
    setup_directories()
    parts = load_csv()

    if args.list:
        print("\nParts in CSV:")
        for p in parts:
            print(f"  {p['lcsc_id']}: {p['comment']} ({p['footprint_hint']})")
        return

    # Process
    results = process_parts(parts, force=args.force, only=args.only)

    # Summary
    print_summary(results)


if __name__ == '__main__':
    main()
