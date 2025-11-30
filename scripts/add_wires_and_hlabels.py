#!/usr/bin/env python3
"""
Add wires and hierarchical labels to schematics
This script adds basic wire connections and hierarchical labels for proper connectivity
"""

import re
import os
import uuid

PROJECT_DIR = r"D:\git2\fcBoardKicad"


def gen_uuid():
    return str(uuid.uuid4())


def add_wires_to_power():
    """Add wires to Power schematic"""
    filepath = os.path.join(PROJECT_DIR, "fcBoard_Power.kicad_sch")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where to insert wires (before sheet_instances)
    insert_pos = content.find('(sheet_instances')
    if insert_pos == -1:
        insert_pos = content.rfind(')')

    # Power schematic wires connecting the buck converters
    # Based on typical LM2596 circuit layout
    wires = []

    # +12V input section wires
    wires.append(f'''
	(wire
		(pts
			(xy 127.0 80.01)
			(xy 152.4 80.01)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    # +5V output section
    wires.append(f'''
	(wire
		(pts
			(xy 215.9 80.01)
			(xy 240.03 80.01)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    # +3V3 output section
    wires.append(f'''
	(wire
		(pts
			(xy 215.9 130.81)
			(xy 240.03 130.81)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    # +1V8 output section
    wires.append(f'''
	(wire
		(pts
			(xy 215.9 181.61)
			(xy 240.03 181.61)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Hierarchical labels for power outputs
    hlabels = []
    hlabels.append(f'''
	(hierarchical_label "+5V"
		(shape output)
		(at 254.0 80.01 0)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "+3V3"
		(shape output)
		(at 254.0 130.81 0)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "+1V8"
		(shape output)
		(at 254.0 181.61 0)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "GND"
		(shape passive)
		(at 254.0 200.66 0)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Wire to hierarchical label
    wires.append(f'''
	(wire
		(pts
			(xy 240.03 80.01)
			(xy 254.0 80.01)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    wires.append(f'''
	(wire
		(pts
			(xy 240.03 130.81)
			(xy 254.0 130.81)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    wires.append(f'''
	(wire
		(pts
			(xy 240.03 181.61)
			(xy 254.0 181.61)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Insert wires and hlabels
    insert_content = ''.join(wires) + ''.join(hlabels)
    new_content = content[:insert_pos] + insert_content + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(wires), len(hlabels)


def add_wires_to_usb():
    """Add wires to USB schematic"""
    filepath = os.path.join(PROJECT_DIR, "fcBoard_USB.kicad_sch")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_pos = content.find('(sheet_instances')
    if insert_pos == -1:
        insert_pos = content.rfind(')')

    wires = []
    hlabels = []

    # USB ULPI interface hierarchical labels
    ulpi_signals = [
        ('USB_CLK', 50.0),
        ('USB_DIR', 52.54),
        ('USB_NXT', 55.08),
        ('USB_STP', 57.62),
        ('USB_DATA0', 62.7),
        ('USB_DATA1', 65.24),
        ('USB_DATA2', 67.78),
        ('USB_DATA3', 70.32),
        ('USB_DATA4', 72.86),
        ('USB_DATA5', 75.4),
        ('USB_DATA6', 77.94),
        ('USB_DATA7', 80.48),
    ]

    for name, y in ulpi_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Power input hierarchical labels
    hlabels.append(f'''
	(hierarchical_label "+5V"
		(shape input)
		(at 50.8 100.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "+3V3"
		(shape input)
		(at 50.8 105.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "GND"
		(shape passive)
		(at 50.8 110.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    insert_content = ''.join(wires) + ''.join(hlabels)
    new_content = content[:insert_pos] + insert_content + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(wires), len(hlabels)


def add_wires_to_ethernet():
    """Add wires to Ethernet schematic"""
    filepath = os.path.join(PROJECT_DIR, "fcBoard_Ethernet.kicad_sch")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_pos = content.find('(sheet_instances')
    if insert_pos == -1:
        insert_pos = content.rfind(')')

    wires = []
    hlabels = []

    # RGMII signals for ETH1 (PS GEM3)
    rgmii1_signals = [
        ('ETH1_TXD0', 50.0),
        ('ETH1_TXD1', 52.54),
        ('ETH1_TXD2', 55.08),
        ('ETH1_TXD3', 57.62),
        ('ETH1_TX_CLK', 60.16),
        ('ETH1_TX_CTL', 62.7),
        ('ETH1_RXD0', 67.78),
        ('ETH1_RXD1', 70.32),
        ('ETH1_RXD2', 72.86),
        ('ETH1_RXD3', 75.4),
        ('ETH1_RX_CLK', 77.94),
        ('ETH1_RX_CTL', 80.48),
        ('ETH1_MDC', 85.56),
        ('ETH1_MDIO', 88.1),
    ]

    for name, y in rgmii1_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # RGMII signals for ETH2 (PL RGMII)
    rgmii2_signals = [
        ('ETH2_TXD0', 120.0),
        ('ETH2_TXD1', 122.54),
        ('ETH2_TXD2', 125.08),
        ('ETH2_TXD3', 127.62),
        ('ETH2_TX_CLK', 130.16),
        ('ETH2_TX_CTL', 132.7),
        ('ETH2_RXD0', 137.78),
        ('ETH2_RXD1', 140.32),
        ('ETH2_RXD2', 142.86),
        ('ETH2_RXD3', 145.4),
        ('ETH2_RX_CLK', 147.94),
        ('ETH2_RX_CTL', 150.48),
        ('ETH2_MDC', 155.56),
        ('ETH2_MDIO', 158.1),
    ]

    for name, y in rgmii2_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Power
    hlabels.append(f'''
	(hierarchical_label "+3V3"
		(shape input)
		(at 50.8 170.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "GND"
		(shape passive)
		(at 50.8 175.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    insert_content = ''.join(wires) + ''.join(hlabels)
    new_content = content[:insert_pos] + insert_content + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(wires), len(hlabels)


def add_wires_to_hdmi():
    """Add wires to HDMI schematic"""
    filepath = os.path.join(PROJECT_DIR, "fcBoard_HDMI.kicad_sch")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_pos = content.find('(sheet_instances')
    if insert_pos == -1:
        insert_pos = content.rfind(')')

    wires = []
    hlabels = []

    # HDMI RX video signals
    hdmi_rx_signals = [
        ('HDMI_RX_PCLK', 50.0),
        ('HDMI_RX_DE', 52.54),
        ('HDMI_RX_HSYNC', 55.08),
        ('HDMI_RX_VSYNC', 57.62),
        ('HDMI_RX_R[7:0]', 62.7),
        ('HDMI_RX_G[7:0]', 65.24),
        ('HDMI_RX_B[7:0]', 67.78),
    ]

    for name, y in hdmi_rx_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape output)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # HDMI TX video signals
    hdmi_tx_signals = [
        ('HDMI_TX_PCLK', 85.0),
        ('HDMI_TX_DE', 87.54),
        ('HDMI_TX_HSYNC', 90.08),
        ('HDMI_TX_VSYNC', 92.62),
        ('HDMI_TX_R[7:0]', 97.7),
        ('HDMI_TX_G[7:0]', 100.24),
        ('HDMI_TX_B[7:0]', 102.78),
    ]

    for name, y in hdmi_tx_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape input)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # I2C for EDID/HDCP
    hlabels.append(f'''
	(hierarchical_label "HDMI_I2C_SCL"
		(shape bidirectional)
		(at 50.8 115.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "HDMI_I2C_SDA"
		(shape bidirectional)
		(at 50.8 117.54 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Power
    hlabels.append(f'''
	(hierarchical_label "+3V3"
		(shape input)
		(at 50.8 130.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "+1V8"
		(shape input)
		(at 50.8 132.54 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "GND"
		(shape passive)
		(at 50.8 135.08 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    insert_content = ''.join(wires) + ''.join(hlabels)
    new_content = content[:insert_pos] + insert_content + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(wires), len(hlabels)


def add_wires_to_peripherals():
    """Add wires to Peripherals schematic"""
    filepath = os.path.join(PROJECT_DIR, "fcBoard_Peripherals.kicad_sch")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_pos = content.find('(sheet_instances')
    if insert_pos == -1:
        insert_pos = content.rfind(')')

    wires = []
    hlabels = []

    # SDIO signals
    sdio_signals = [
        ('SDIO_CLK', 50.0),
        ('SDIO_CMD', 52.54),
        ('SDIO_DAT0', 55.08),
        ('SDIO_DAT1', 57.62),
        ('SDIO_DAT2', 60.16),
        ('SDIO_DAT3', 62.7),
        ('SDIO_CD', 65.24),
    ]

    for name, y in sdio_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # UART signals
    hlabels.append(f'''
	(hierarchical_label "UART_TXD"
		(shape output)
		(at 50.8 80.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "UART_RXD"
		(shape input)
		(at 50.8 82.54 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # CAN signals
    can_signals = [
        ('CAN0_TX', 95.0),
        ('CAN0_RX', 97.54),
        ('CAN1_TX', 102.62),
        ('CAN1_RX', 105.16),
    ]

    for name, y in can_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # RS485 signals
    rs485_signals = [
        ('RS485_0_TX', 115.0),
        ('RS485_0_RX', 117.54),
        ('RS485_0_DE', 120.08),
        ('RS485_1_TX', 125.16),
        ('RS485_1_RX', 127.7),
        ('RS485_1_DE', 130.24),
    ]

    for name, y in rs485_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # GPIO/LED/Button
    gpio_signals = [
        ('LED0', 145.0),
        ('LED1', 147.54),
        ('LED2', 150.08),
        ('LED3', 152.62),
        ('BTN0', 157.7),
        ('BTN1', 160.24),
    ]

    for name, y in gpio_signals:
        hlabels.append(f'''
	(hierarchical_label "{name}"
		(shape bidirectional)
		(at 50.8 {y} 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    # Power
    hlabels.append(f'''
	(hierarchical_label "+3V3"
		(shape input)
		(at 50.8 175.0 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    hlabels.append(f'''
	(hierarchical_label "GND"
		(shape passive)
		(at 50.8 177.54 180)
		(fields_autoplaced yes)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify right)
		)
		(uuid "{gen_uuid()}")
	)''')

    insert_content = ''.join(wires) + ''.join(hlabels)
    new_content = content[:insert_pos] + insert_content + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(wires), len(hlabels)


def main():
    print("=" * 60)
    print("Adding Wires and Hierarchical Labels")
    print("=" * 60)

    w, h = add_wires_to_power()
    print(f"  Power: {w} wires, {h} hierarchical labels")

    w, h = add_wires_to_usb()
    print(f"  USB: {w} wires, {h} hierarchical labels")

    w, h = add_wires_to_ethernet()
    print(f"  Ethernet: {w} wires, {h} hierarchical labels")

    w, h = add_wires_to_hdmi()
    print(f"  HDMI: {w} wires, {h} hierarchical labels")

    w, h = add_wires_to_peripherals()
    print(f"  Peripherals: {w} wires, {h} hierarchical labels")

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
