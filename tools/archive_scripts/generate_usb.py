#!/usr/bin/env python3
"""
USB Subsystem Schematic Generator (Refactored)

Generates a KiCad schematic with:
- USB5744 USB 3.0 Hub (4-port)
- USB3320 ULPI PHY
- 4x USB Type-A Connectors
- ESD Protection

Uses the kicad_lib module for common symbols and components.

Usage:
    python scripts/generate_usb.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib import SchematicGenerator


def main():
    """Generate the USB subsystem schematic."""
    print("=" * 60)
    print("USB Subsystem Schematic Generator (Refactored)")
    print("=" * 60)

    # Create generator
    sch = SchematicGenerator("USB", "USB 3.0 Hub Subsystem")

    # Add required symbols
    sch.add_common_symbols("R", "C", "Crystal")
    sch.add_power_symbols("GND", "+3V3", "+5V", "VBUS")
    sch.add_ic_symbol("USB5744")
    sch.add_ic_symbol("USB3320")
    sch.add_connector_symbol("USB_A")

    # ==================== USB5744 HUB CONTROLLER ====================
    sch.add_text("USB 3.0 4-Port Hub Controller", 45.72, 30.48)

    # U1: USB5744
    sch.place_component("USB5744", "U1", 76.2, 76.2)

    # Decoupling caps for USB5744
    sch.place_component("C_0402_100nF", "C1", 50.8, 55.88)
    sch.place_component("C_0402_100nF", "C2", 50.8, 66.04)

    # 24MHz Crystal for USB5744
    sch.place_component("Crystal_24MHz", "Y1", 50.8, 88.9)
    sch.place_component("C_0402_22pF", "C3", 43.18, 96.52)
    sch.place_component("C_0402_22pF", "C4", 58.42, 96.52)

    # Power symbols
    sch.place_power("+3V3", 50.8, 48.26)
    sch.place_power("GND", 50.8, 73.66)
    sch.place_power("GND", 43.18, 104.14)
    sch.place_power("GND", 58.42, 104.14)
    sch.place_power("GND", 76.2, 106.68)

    # ==================== USB TYPE-A CONNECTORS ====================
    sch.add_text("USB 3.0 Downstream Ports", 127, 30.48)

    # J1-J4: USB Type-A connectors
    for i, y_offset in enumerate([50.8, 76.2, 101.6, 127]):
        ref = f"J{i+1}"
        sch.place_component("USB_A_Receptacle", ref, 139.7, y_offset)
        sch.place_power("GND", 139.7, y_offset + 10.16)
        sch.place_power("VBUS", 147.32, y_offset - 5.08)

    # ==================== USB3320 ULPI PHY ====================
    sch.add_text("USB 2.0 ULPI PHY\\n(for SoM connection)", 180.34, 30.48)

    # U2: USB3320
    sch.place_component("USB3320", "U2", 200.66, 76.2)

    # Decoupling caps for USB3320
    sch.place_component("C_0402_100nF", "C5", 177.8, 60.96)
    sch.place_component("C_0402_100nF", "C6", 177.8, 71.12)

    # Power symbols
    sch.place_power("+3V3", 177.8, 53.34)
    sch.place_power("GND", 177.8, 78.74)
    sch.place_power("GND", 200.66, 101.6)

    # ==================== HIERARCHICAL LABELS ====================
    # Upstream USB signals (to SoM)
    sch.add_hierarchical_label("USB_DP", 50.8, 86.36, "bidirectional", 180)
    sch.add_hierarchical_label("USB_DM", 50.8, 88.9, "bidirectional", 180)
    sch.add_hierarchical_label("USB_SSRX_P", 50.8, 76.2, "bidirectional", 180)
    sch.add_hierarchical_label("USB_SSRX_N", 50.8, 78.74, "bidirectional", 180)
    sch.add_hierarchical_label("USB_SSTX_P", 50.8, 68.58, "bidirectional", 180)
    sch.add_hierarchical_label("USB_SSTX_N", 50.8, 71.12, "bidirectional", 180)

    # ULPI interface signals (to SoM)
    sch.add_hierarchical_label("ULPI_CLK", 223.52, 68.58, "output")
    sch.add_hierarchical_label("ULPI_DIR", 223.52, 71.12, "output")
    sch.add_hierarchical_label("ULPI_NXT", 223.52, 73.66, "output")
    sch.add_hierarchical_label("ULPI_STP", 223.52, 76.2, "input")
    sch.add_hierarchical_label("ULPI_D0", 223.52, 60.96, "bidirectional")
    sch.add_hierarchical_label("ULPI_D1", 223.52, 63.5, "bidirectional")
    sch.add_hierarchical_label("ULPI_D2", 223.52, 66.04, "bidirectional")

    # Power rails
    sch.add_hierarchical_label("+5V", 35.56, 48.26, "input", 180)
    sch.add_hierarchical_label("+3V3", 35.56, 53.34, "input", 180)
    sch.add_hierarchical_label("GND", 35.56, 58.42, "passive", 180)

    # Save the schematic
    sch.save()

    print()
    print("Components used:")
    print("  - U1: USB5744 (USB 3.0 4-port hub)")
    print("  - U2: USB3320 (ULPI PHY)")
    print("  - J1-J4: USB Type-A receptacles")
    print("  - Y1: 24MHz crystal")
    print()
    print("[NOTE] Using kicad_lib module for embedded symbols")


if __name__ == "__main__":
    main()
