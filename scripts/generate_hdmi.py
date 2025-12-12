#!/usr/bin/env python3
"""
HDMI Subsystem Schematic Generator (Refactored)

Generates a KiCad schematic with:
- IT6801FN HDMI Input Receiver
- IT66121FN HDMI Output Transmitter
- HDMI Type-A connectors for input and output

Uses the kicad_lib module for common symbols and components.

Usage:
    python scripts/generate_hdmi.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib import SchematicGenerator


def main():
    """Generate the HDMI subsystem schematic."""
    print("=" * 60)
    print("HDMI Subsystem Schematic Generator (Refactored)")
    print("=" * 60)

    # Create generator
    sch = SchematicGenerator("HDMI", "HDMI Input/Output")

    # Add required symbols
    sch.add_common_symbols("R", "C", "Ferrite_Bead")
    sch.add_power_symbols("GND", "+3V3", "+1V8", "+5V")
    sch.add_ic_symbol("IT6801FN")
    sch.add_ic_symbol("IT66121FN")
    sch.add_connector_symbol("HDMI_A")

    # ==================== HDMI INPUT (IT6801FN) ====================
    sch.add_text("HDMI 1.4 Input Receiver\\n(IT6801FN)", 35.56, 25.4)

    # U1: IT6801FN HDMI Receiver
    sch.place_component("IT6801FN", "U1", 76.2, 76.2)

    # Decoupling caps for IT6801FN
    sch.place_component("C_0402_100nF", "C1", 48.26, 50.8)
    sch.place_component("C_0402_100nF", "C2", 48.26, 58.42)
    sch.place_component("C_0603_1uF", "C3", 48.26, 66.04)

    # Pull-up resistors for I2C
    sch.place_component("R_0402_4.7k", "R1", 48.26, 86.36)
    sch.place_component("R_0402_4.7k", "R2", 55.88, 86.36)

    # J1: HDMI Input connector
    sch.place_component("HDMI_A_Receptacle", "J1", 25.4, 76.2)

    # Power symbols for HDMI Input
    sch.place_power("+3V3", 48.26, 43.18)
    sch.place_power("+3V3", 48.26, 78.74)
    sch.place_power("+3V3", 55.88, 78.74)
    sch.place_power("GND", 48.26, 73.66)
    sch.place_power("GND", 76.2, 109.22)
    sch.place_power("GND", 25.4, 101.6)

    # ==================== HDMI OUTPUT (IT66121FN) ====================
    sch.add_text("HDMI 1.4 Output Transmitter\\n(IT66121FN)", 147.32, 25.4)

    # U2: IT66121FN HDMI Transmitter
    sch.place_component("IT66121FN", "U2", 187.96, 76.2)

    # Decoupling caps for IT66121FN
    sch.place_component("C_0402_100nF", "C4", 160.02, 50.8)
    sch.place_component("C_0402_100nF", "C5", 160.02, 58.42)
    sch.place_component("C_0603_1uF", "C6", 160.02, 66.04)

    # Pull-up resistors for I2C
    sch.place_component("R_0402_4.7k", "R3", 160.02, 71.12)
    sch.place_component("R_0402_4.7k", "R4", 167.64, 71.12)

    # J2: HDMI Output connector
    sch.place_component("HDMI_A_Receptacle", "J2", 231.14, 76.2)

    # Power symbols for HDMI Output
    sch.place_power("+3V3", 160.02, 43.18)
    sch.place_power("+3V3", 160.02, 63.5)
    sch.place_power("+3V3", 167.64, 63.5)
    sch.place_power("GND", 160.02, 73.66)
    sch.place_power("GND", 187.96, 109.22)
    sch.place_power("GND", 231.14, 101.6)
    sch.place_power("+5V", 241.3, 60.96)

    # ==================== HIERARCHICAL LABELS ====================
    # HDMI Input parallel RGB interface (from IT6801FN to FPGA)
    sch.add_hierarchical_label("HDMI_IN_PCLK", 101.6, 50.8, "output")
    sch.add_hierarchical_label("HDMI_IN_HSYNC", 101.6, 53.34, "output")
    sch.add_hierarchical_label("HDMI_IN_VSYNC", 101.6, 55.88, "output")
    sch.add_hierarchical_label("HDMI_IN_DE", 101.6, 58.42, "output")
    sch.add_hierarchical_label("HDMI_IN_D[23:0]", 101.6, 63.5, "output")
    sch.add_hierarchical_label("HDMI_IN_INT_N", 101.6, 71.12, "output")

    # HDMI Input I2C
    sch.add_hierarchical_label("HDMI_IN_SCL", 101.6, 86.36, "bidirectional")
    sch.add_hierarchical_label("HDMI_IN_SDA", 101.6, 88.9, "bidirectional")

    # HDMI Output parallel RGB interface (from FPGA to IT66121FN)
    sch.add_hierarchical_label("HDMI_OUT_PCLK", 160.02, 91.44, "input", 180)
    sch.add_hierarchical_label("HDMI_OUT_HSYNC", 160.02, 88.9, "input", 180)
    sch.add_hierarchical_label("HDMI_OUT_VSYNC", 160.02, 86.36, "input", 180)
    sch.add_hierarchical_label("HDMI_OUT_DE", 160.02, 83.82, "input", 180)
    sch.add_hierarchical_label("HDMI_OUT_D[23:0]", 160.02, 78.74, "input", 180)

    # HDMI Output I2C
    sch.add_hierarchical_label("HDMI_OUT_SCL", 160.02, 55.88, "bidirectional", 180)
    sch.add_hierarchical_label("HDMI_OUT_SDA", 160.02, 58.42, "bidirectional", 180)

    # Power rails
    sch.add_hierarchical_label("+3V3", 25.4, 35.56, "input", 180)
    sch.add_hierarchical_label("+1V8", 25.4, 40.64, "input", 180)
    sch.add_hierarchical_label("+5V", 25.4, 45.72, "input", 180)
    sch.add_hierarchical_label("GND", 25.4, 50.8, "passive", 180)

    # Save the schematic
    sch.save()

    print()
    print("Components used:")
    print("  - U1: IT6801FN (HDMI Receiver)")
    print("  - U2: IT66121FN (HDMI Transmitter)")
    print("  - J1: HDMI Input connector")
    print("  - J2: HDMI Output connector")
    print("  - R1-R4: I2C pull-up resistors")
    print()
    print("[NOTE] Using kicad_lib module for embedded symbols")


if __name__ == "__main__":
    main()
