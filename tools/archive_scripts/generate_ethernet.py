#!/usr/bin/env python3
"""
Ethernet Subsystem Schematic Generator (Refactored)

Generates a KiCad schematic with:
- 2x RTL8211F-CG Gigabit Ethernet PHY
- 2x RJ45 Connectors with Magnetics
- RGMII Interface to SoM

Uses the kicad_lib module for common symbols and components.

Usage:
    python scripts/generate_ethernet.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib import SchematicGenerator


def main():
    """Generate the Ethernet subsystem schematic."""
    print("=" * 60)
    print("Ethernet Subsystem Schematic Generator (Refactored)")
    print("=" * 60)

    # Create generator
    sch = SchematicGenerator("Ethernet", "Dual Gigabit Ethernet")

    # Add required symbols
    sch.add_common_symbols("R", "C", "Crystal", "Ferrite_Bead")
    sch.add_power_symbols("GND", "+3V3", "+1V8")
    sch.add_ic_symbol("RTL8211F")
    sch.add_connector_symbol("RJ45_Magjack")

    # ==================== ETH0: PS Ethernet (U1) ====================
    sch.add_text("PS Gigabit Ethernet (ETH0)\\nRGMII Interface", 35.56, 25.4)

    # U1: RTL8211F
    sch.place_component("RTL8211F", "U1", 76.2, 76.2)

    # Decoupling caps
    sch.place_component("C_0402_100nF", "C1", 48.26, 50.8)
    sch.place_component("C_0402_100nF", "C2", 48.26, 58.42)
    sch.place_component("C_0603_1uF", "C3", 48.26, 66.04)

    # 25MHz Crystal
    sch.place_component("Crystal_25MHz", "Y1", 48.26, 96.52)
    sch.place_component("C_0402_22pF", "C4", 40.64, 104.14)
    sch.place_component("C_0402_22pF", "C5", 55.88, 104.14)

    # Pull-up resistor for RESET_N
    sch.place_component("R_0402_10k", "R1", 101.6, 48.26)

    # J1: RJ45 with magnetics
    sch.place_component("RJ45_Magjack", "J1", 139.7, 76.2)

    # Power symbols for ETH0
    sch.place_power("+3V3", 48.26, 43.18)
    sch.place_power("+3V3", 101.6, 40.64)
    sch.place_power("GND", 48.26, 73.66)
    sch.place_power("GND", 40.64, 111.76)
    sch.place_power("GND", 55.88, 111.76)
    sch.place_power("GND", 76.2, 109.22)
    sch.place_power("GND", 139.7, 96.52)

    # ==================== ETH1: PL Ethernet (U2) ====================
    sch.add_text("PL Gigabit Ethernet (ETH1)\\nRGMII Interface", 35.56, 137.16)

    # U2: RTL8211F
    sch.place_component("RTL8211F", "U2", 76.2, 187.96)

    # Decoupling caps
    sch.place_component("C_0402_100nF", "C6", 48.26, 162.56)
    sch.place_component("C_0402_100nF", "C7", 48.26, 170.18)
    sch.place_component("C_0603_1uF", "C8", 48.26, 177.8)

    # 25MHz Crystal
    sch.place_component("Crystal_25MHz", "Y2", 48.26, 208.28)
    sch.place_component("C_0402_22pF", "C9", 40.64, 215.9)
    sch.place_component("C_0402_22pF", "C10", 55.88, 215.9)

    # Pull-up resistor for RESET_N
    sch.place_component("R_0402_10k", "R2", 101.6, 160.02)

    # J2: RJ45 with magnetics
    sch.place_component("RJ45_Magjack", "J2", 139.7, 187.96)

    # Power symbols for ETH1
    sch.place_power("+3V3", 48.26, 154.94)
    sch.place_power("+3V3", 101.6, 152.4)
    sch.place_power("GND", 48.26, 185.42)
    sch.place_power("GND", 40.64, 223.52)
    sch.place_power("GND", 55.88, 223.52)
    sch.place_power("GND", 76.2, 220.98)
    sch.place_power("GND", 139.7, 208.28)

    # ==================== HIERARCHICAL LABELS ====================
    # ETH0 RGMII signals (PS Ethernet)
    sch.add_hierarchical_label("PS_ETH_TXD0", 48.26, 91.44, "input", 180)
    sch.add_hierarchical_label("PS_ETH_TXD1", 48.26, 88.9, "input", 180)
    sch.add_hierarchical_label("PS_ETH_TXD2", 48.26, 86.36, "input", 180)
    sch.add_hierarchical_label("PS_ETH_TXD3", 48.26, 83.82, "input", 180)
    sch.add_hierarchical_label("PS_ETH_TX_CLK", 48.26, 78.74, "input", 180)
    sch.add_hierarchical_label("PS_ETH_TX_EN", 48.26, 76.2, "input", 180)
    sch.add_hierarchical_label("PS_ETH_RXD0", 48.26, 68.58, "output", 180)
    sch.add_hierarchical_label("PS_ETH_RXD1", 48.26, 66.04, "output", 180)
    sch.add_hierarchical_label("PS_ETH_RXD2", 48.26, 63.5, "output", 180)
    sch.add_hierarchical_label("PS_ETH_RXD3", 48.26, 60.96, "output", 180)
    sch.add_hierarchical_label("PS_ETH_RX_CLK", 48.26, 55.88, "output", 180)
    sch.add_hierarchical_label("PS_ETH_RX_DV", 48.26, 53.34, "output", 180)
    sch.add_hierarchical_label("PS_ETH_MDC", 101.6, 73.66, "input")
    sch.add_hierarchical_label("PS_ETH_MDIO", 101.6, 71.12, "bidirectional")

    # ETH1 RGMII signals (PL Ethernet)
    sch.add_hierarchical_label("PL_ETH_TXD0", 48.26, 203.2, "input", 180)
    sch.add_hierarchical_label("PL_ETH_TXD1", 48.26, 200.66, "input", 180)
    sch.add_hierarchical_label("PL_ETH_TXD2", 48.26, 198.12, "input", 180)
    sch.add_hierarchical_label("PL_ETH_TXD3", 48.26, 195.58, "input", 180)
    sch.add_hierarchical_label("PL_ETH_TX_CLK", 48.26, 190.5, "input", 180)
    sch.add_hierarchical_label("PL_ETH_TX_EN", 48.26, 187.96, "input", 180)
    sch.add_hierarchical_label("PL_ETH_RXD0", 48.26, 180.34, "output", 180)
    sch.add_hierarchical_label("PL_ETH_RXD1", 48.26, 177.8, "output", 180)
    sch.add_hierarchical_label("PL_ETH_RXD2", 48.26, 175.26, "output", 180)
    sch.add_hierarchical_label("PL_ETH_RXD3", 48.26, 172.72, "output", 180)
    sch.add_hierarchical_label("PL_ETH_RX_CLK", 48.26, 167.64, "output", 180)
    sch.add_hierarchical_label("PL_ETH_RX_DV", 48.26, 165.1, "output", 180)
    sch.add_hierarchical_label("PL_ETH_MDC", 101.6, 185.42, "input")
    sch.add_hierarchical_label("PL_ETH_MDIO", 101.6, 182.88, "bidirectional")

    # Power rails
    sch.add_hierarchical_label("+3V3", 25.4, 43.18, "input", 180)
    sch.add_hierarchical_label("GND", 25.4, 48.26, "passive", 180)

    # Save the schematic
    sch.save()

    print()
    print("Components used:")
    print("  - U1, U2: RTL8211F-CG (Gigabit PHY)")
    print("  - J1, J2: RJ45 with magnetics")
    print("  - Y1, Y2: 25MHz crystals")
    print("  - R1, R2: 10k pull-up resistors")
    print()
    print("[NOTE] Using kicad_lib module for embedded symbols")


if __name__ == "__main__":
    main()
