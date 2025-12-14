#!/usr/bin/env python3
"""
Power Supply Schematic Generator (Refactored)

Generates a KiCad schematic with:
- 12V DC Input (Barrel Jack)
- LM2596S-5.0 (12V -> 5V)
- LM2596S-ADJ (12V -> 3.3V)
- LM2596S-ADJ (12V -> 1.8V)

Uses the kicad_lib module for common symbols and components.

Usage:
    python scripts/generate_power.py
"""

import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib import SchematicGenerator


def main():
    """Generate the Power Supply schematic."""
    print("=" * 60)
    print("Power Supply Schematic Generator (Refactored)")
    print("=" * 60)

    # Create generator
    sch = SchematicGenerator("Power", "Power Supply")

    # Add required symbols
    sch.add_common_symbols("R", "C", "CP", "L", "LED", "D_Schottky")
    sch.add_power_symbols("GND", "+12V", "+5V", "+3V3", "+1V8")
    sch.add_ic_symbol("LM2596S-5")
    sch.add_ic_symbol("LM2596S-ADJ")
    sch.add_connector_symbol("Barrel_Jack")

    # ==================== 12V INPUT SECTION ====================
    sch.add_text("12V DC Input\\n5A minimum", 30.48, 40.64)

    # Barrel Jack
    sch.place_custom_component("Barrel_Jack", "J1", "DC_12V", 40.64, 50.8,
                               footprint="Connector_BarrelJack:BarrelJack_Horizontal")

    # Input filter capacitor 470uF
    sch.place_component("CP_470uF_25V", "C1", 55.88, 55.88)

    # Power symbols at input
    sch.place_power("+12V", 55.88, 45.72)
    sch.place_power("GND", 40.64, 60.96)
    sch.place_power("GND", 55.88, 66.04)

    # ==================== 5V BUCK CONVERTER ====================
    sch.add_text("5V @ 3A Output", 96.52, 35.56)

    # U1: LM2596S-5.0
    sch.place_component("LM2596S-5.0", "U1", 101.6, 50.8)

    # Input cap for 5V converter
    sch.place_component("C_0402_100nF", "C2", 86.36, 55.88)

    # Output inductor 33uH
    sch.place_component("L_33uH", "L1", 119.38, 48.26)

    # Schottky diode SS34
    sch.place_component("D_SS34", "D1", 119.38, 58.42)

    # Output cap 220uF
    sch.place_component("CP_220uF_16V", "C3", 132.08, 55.88)

    # Power LED (green)
    sch.place_component("LED_0603_Green", "D2", 142.24, 55.88)

    # LED current limiting resistor 330R
    sch.place_component("R_0402_330R", "R1", 142.24, 45.72)

    # Power symbols for 5V section
    sch.place_power("+12V", 86.36, 45.72)
    sch.place_power("+5V", 132.08, 45.72)
    sch.place_power("+5V", 142.24, 38.1)
    sch.place_power("GND", 86.36, 66.04)
    sch.place_power("GND", 101.6, 63.5)
    sch.place_power("GND", 119.38, 66.04)
    sch.place_power("GND", 132.08, 66.04)
    sch.place_power("GND", 142.24, 66.04)

    # ==================== 3.3V BUCK CONVERTER ====================
    sch.add_text("3.3V @ 3A Output", 96.52, 86.36)

    # U2: LM2596S-ADJ for 3.3V
    sch.place_component("LM2596S-ADJ", "U2", 101.6, 101.6)

    # Input cap
    sch.place_component("C_0402_100nF", "C4", 86.36, 106.68)

    # Feedback resistors for 3.3V: Vout = 1.23 * (1 + R2/R3)
    sch.place_component("R_0402_1.5k", "R2", 119.38, 106.68)
    sch.place_component("R_0402_1k", "R3", 119.38, 116.84)

    # Output inductor 33uH
    sch.place_component("L_33uH", "L2", 132.08, 99.06)

    # Schottky diode
    sch.place_component("D_SS34", "D3", 132.08, 109.22)

    # Output cap 220uF
    sch.place_component("CP_220uF_16V", "C5", 144.78, 106.68)

    # Power LED (green)
    sch.place_component("LED_0603_Green", "D4", 154.94, 106.68)

    # LED resistor
    sch.place_component("R_0402_470R", "R4", 154.94, 96.52)

    # Power symbols for 3.3V section
    sch.place_power("+12V", 86.36, 96.52)
    sch.place_power("+3V3", 144.78, 96.52)
    sch.place_power("+3V3", 154.94, 88.9)
    sch.place_power("GND", 86.36, 116.84)
    sch.place_power("GND", 101.6, 114.3)
    sch.place_power("GND", 119.38, 124.46)
    sch.place_power("GND", 132.08, 116.84)
    sch.place_power("GND", 144.78, 116.84)
    sch.place_power("GND", 154.94, 116.84)

    # ==================== 1.8V BUCK CONVERTER ====================
    sch.add_text("1.8V @ 3A Output", 96.52, 137.16)

    # U3: LM2596S-ADJ for 1.8V
    sch.place_component("LM2596S-ADJ", "U3", 101.6, 152.4)

    # Input cap
    sch.place_component("C_0402_100nF", "C6", 86.36, 157.48)

    # Feedback resistors for 1.8V: Vout = 1.23 * (1 + R5/R6)
    sch.place_component("R_0402_470R", "R5", 119.38, 157.48)
    sch.place_component("R_0402_1k", "R6", 119.38, 167.64)

    # Output inductor 33uH
    sch.place_component("L_33uH", "L3", 132.08, 149.86)

    # Schottky diode
    sch.place_component("D_SS34", "D5", 132.08, 160.02)

    # Output cap 220uF
    sch.place_component("CP_220uF_16V", "C7", 144.78, 157.48)

    # Power LED (red for 1.8V to distinguish)
    sch.place_component("LED_0603_Red", "D6", 154.94, 157.48)

    # LED resistor
    sch.place_component("R_0402_330R", "R7", 154.94, 147.32)

    # Power symbols for 1.8V section
    sch.place_power("+12V", 86.36, 147.32)
    sch.place_power("+1V8", 144.78, 147.32)
    sch.place_power("+1V8", 154.94, 139.7)
    sch.place_power("GND", 86.36, 167.64)
    sch.place_power("GND", 101.6, 165.1)
    sch.place_power("GND", 119.38, 175.26)
    sch.place_power("GND", 132.08, 167.64)
    sch.place_power("GND", 144.78, 167.64)
    sch.place_power("GND", 154.94, 167.64)

    # ==================== HIERARCHICAL LABELS ====================
    sch.add_hierarchical_label("+5V", 152.4, 48.26, "output")
    sch.add_hierarchical_label("+3V3", 165.1, 99.06, "output")
    sch.add_hierarchical_label("+1V8", 165.1, 149.86, "output")
    sch.add_hierarchical_label("+12V", 66.04, 48.26, "input")
    sch.add_hierarchical_label("GND", 66.04, 58.42, "passive")

    # Save the schematic
    sch.save()

    print()
    print("Components used:")
    print("  - U1: LM2596S-5.0 (5V regulator)")
    print("  - U2, U3: LM2596S-ADJ (adjustable regulator)")
    print("  - L1-L3: 33uH inductors")
    print("  - D1, D3, D5: SS34 Schottky diodes")
    print("  - D2, D4: Green LEDs")
    print("  - D6: Red LED")
    print()
    print("[NOTE] Using kicad_lib module for embedded symbols")


if __name__ == "__main__":
    main()
