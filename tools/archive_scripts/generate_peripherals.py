#!/usr/bin/env python3
"""
Peripherals Schematic Generator (Refactored)

Generates a KiCad schematic with:
- MAX485 RS485 transceivers (2x)
- CP2102N USB-UART bridge
- User LEDs (4x)
- User Buttons (2x)
- GPIO Header (2x10)

Uses the kicad_lib module for common symbols and components.

Usage:
    python scripts/generate_peripherals.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from kicad_lib import SchematicGenerator


def main():
    """Generate the Peripherals schematic."""
    print("=" * 60)
    print("Peripherals Schematic Generator (Refactored)")
    print("=" * 60)

    # Create generator
    sch = SchematicGenerator("Peripherals", "Board Peripherals")

    # Add required symbols
    sch.add_common_symbols("R", "C", "LED")
    sch.add_power_symbols("GND", "+3V3", "+5V")
    sch.add_ic_symbol("MAX485")
    sch.add_ic_symbol("CP2102N")
    sch.add_connector_symbol("Conn_2x10")
    sch.add_connector_symbol("USB_C")
    sch.add_connector_symbol("SW_Push")

    # ==================== RS485 INTERFACES ====================
    sch.add_text("RS485 Interface #1", 35.56, 25.4)

    # U1: MAX485 #1
    sch.place_component("MAX485", "U1", 55.88, 50.8)

    # Termination resistor
    sch.place_component("R_0402_100R", "R1", 76.2, 45.72)

    # Power symbols
    sch.place_power("+3V3", 55.88, 35.56)
    sch.place_power("GND", 55.88, 66.04)

    sch.add_text("RS485 Interface #2", 35.56, 81.28)

    # U2: MAX485 #2
    sch.place_component("MAX485", "U2", 55.88, 106.68)

    # Termination resistor
    sch.place_component("R_0402_100R", "R2", 76.2, 101.6)

    # Power symbols
    sch.place_power("+3V3", 55.88, 91.44)
    sch.place_power("GND", 55.88, 121.92)

    # ==================== USB-UART BRIDGE ====================
    sch.add_text("USB to UART Bridge\\n(Debug Console)", 119.38, 25.4)

    # U3: CP2102N
    sch.place_component("CP2102N", "U3", 149.86, 55.88)

    # USB-C connector for debug
    sch.place_component("USB_C_Receptacle", "J1", 111.76, 55.88)

    # Decoupling cap
    sch.place_component("C_0402_100nF", "C1", 129.54, 45.72)

    # Power symbols
    sch.place_power("+3V3", 129.54, 38.1)
    sch.place_power("GND", 129.54, 53.34)
    sch.place_power("GND", 111.76, 73.66)
    sch.place_power("GND", 149.86, 73.66)

    # ==================== USER LEDs ====================
    sch.add_text("User LEDs", 200.66, 25.4)

    led_y_positions = [45.72, 55.88, 66.04, 76.2]
    led_colors = ["LED_0603_Red", "LED_0603_Green", "LED_0603_Blue", "LED_0603_Yellow"]

    for i, (y, color) in enumerate(zip(led_y_positions, led_colors)):
        ref_led = f"D{i+1}"
        ref_r = f"R{i+3}"  # R3, R4, R5, R6

        sch.place_component(color, ref_led, 213.36, y)
        sch.place_component("R_0402_330R", ref_r, 226.06, y)
        sch.place_power("GND", 205.74, y)

    sch.place_power("+3V3", 233.68, 45.72)
    sch.place_power("+3V3", 233.68, 55.88)
    sch.place_power("+3V3", 233.68, 66.04)
    sch.place_power("+3V3", 233.68, 76.2)

    # ==================== USER BUTTONS ====================
    sch.add_text("User Buttons", 200.66, 91.44)

    # SW1: User button 1
    sch.place_component("SW_Push_4x4", "SW1", 213.36, 106.68)
    sch.place_component("R_0402_10k", "R7", 226.06, 99.06)
    sch.place_power("GND", 220.98, 106.68)
    sch.place_power("+3V3", 226.06, 91.44)

    # SW2: User button 2
    sch.place_component("SW_Push_4x4", "SW2", 213.36, 124.46)
    sch.place_component("R_0402_10k", "R8", 226.06, 116.84)
    sch.place_power("GND", 220.98, 124.46)
    sch.place_power("+3V3", 226.06, 109.22)

    # ==================== GPIO HEADER ====================
    sch.add_text("GPIO Header\\n(2x10, 2.54mm)", 119.38, 96.52)

    # J2: GPIO header
    sch.place_component("Conn_2x10_2.54mm", "J2", 139.7, 134.62)
    sch.place_power("+3V3", 124.46, 119.38)
    sch.place_power("GND", 154.94, 119.38)

    # ==================== HIERARCHICAL LABELS ====================
    # RS485 #1 signals
    sch.add_hierarchical_label("RS485_1_TX", 40.64, 45.72, "input", 180)
    sch.add_hierarchical_label("RS485_1_RX", 40.64, 50.8, "output", 180)
    sch.add_hierarchical_label("RS485_1_DE", 40.64, 55.88, "input", 180)
    sch.add_hierarchical_label("RS485_1_A", 86.36, 45.72, "bidirectional")
    sch.add_hierarchical_label("RS485_1_B", 86.36, 50.8, "bidirectional")

    # RS485 #2 signals
    sch.add_hierarchical_label("RS485_2_TX", 40.64, 101.6, "input", 180)
    sch.add_hierarchical_label("RS485_2_RX", 40.64, 106.68, "output", 180)
    sch.add_hierarchical_label("RS485_2_DE", 40.64, 111.76, "input", 180)
    sch.add_hierarchical_label("RS485_2_A", 86.36, 101.6, "bidirectional")
    sch.add_hierarchical_label("RS485_2_B", 86.36, 106.68, "bidirectional")

    # UART signals
    sch.add_hierarchical_label("DEBUG_TX", 167.64, 48.26, "output")
    sch.add_hierarchical_label("DEBUG_RX", 167.64, 53.34, "input")

    # LED control signals
    sch.add_hierarchical_label("LED1", 200.66, 45.72, "input", 180)
    sch.add_hierarchical_label("LED2", 200.66, 55.88, "input", 180)
    sch.add_hierarchical_label("LED3", 200.66, 66.04, "input", 180)
    sch.add_hierarchical_label("LED4", 200.66, 76.2, "input", 180)

    # Button signals
    sch.add_hierarchical_label("BTN1", 200.66, 106.68, "output", 180)
    sch.add_hierarchical_label("BTN2", 200.66, 124.46, "output", 180)

    # GPIO signals (directly from header)
    for i in range(10):
        y_pos = 127 + (i * 2.54)
        sch.add_hierarchical_label(f"GPIO{i}", 124.46, y_pos, "bidirectional", 180)
        sch.add_hierarchical_label(f"GPIO{i+10}", 154.94, y_pos, "bidirectional")

    # Power rails
    sch.add_hierarchical_label("+3V3", 25.4, 35.56, "input", 180)
    sch.add_hierarchical_label("+5V", 25.4, 40.64, "input", 180)
    sch.add_hierarchical_label("GND", 25.4, 45.72, "passive", 180)

    # Save the schematic
    sch.save()

    print()
    print("Components used:")
    print("  - U1, U2: MAX485 (RS485 transceivers)")
    print("  - U3: CP2102N (USB-UART bridge)")
    print("  - J1: USB-C connector")
    print("  - J2: 2x10 GPIO header")
    print("  - D1-D4: User LEDs (R/G/B/Y)")
    print("  - SW1, SW2: User push buttons")
    print()
    print("[NOTE] Using kicad_lib module for embedded symbols")


if __name__ == "__main__":
    main()
