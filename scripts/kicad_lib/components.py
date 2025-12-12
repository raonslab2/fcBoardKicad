"""
JLCPCB Component Database

Centralized database for all JLCPCB/LCSC components used in the project.
Each component includes:
- symbol: Symbol type to use (from symbols.py)
- value: Display value
- footprint: JLCPCB footprint name
- lcsc: LCSC part number for BOM

Usage:
    from kicad_lib.components import JLCPCB_PARTS
    part = JLCPCB_PARTS["R_0402_10k"]
"""

# Footprint library name (from easyeda2kicad)
JLC_FP = "jlc_components"


# =============================================================================
# RESISTORS
# =============================================================================

RESISTORS = {
    "R_0402_0R": {
        "symbol": "R",
        "value": "0R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C17168",
    },
    "R_0402_10R": {
        "symbol": "R",
        "value": "10R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25077",
    },
    "R_0402_22R": {
        "symbol": "R",
        "value": "22R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25092",
    },
    "R_0402_33R": {
        "symbol": "R",
        "value": "33R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25105",
    },
    "R_0402_47R": {
        "symbol": "R",
        "value": "47R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25118",
    },
    "R_0402_100R": {
        "symbol": "R",
        "value": "100R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25076",
    },
    "R_0402_220R": {
        "symbol": "R",
        "value": "220R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25091",
    },
    "R_0402_330R": {
        "symbol": "R",
        "value": "330R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C72038",
    },
    "R_0402_470R": {
        "symbol": "R",
        "value": "470R",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25087",
    },
    "R_0402_1k": {
        "symbol": "R",
        "value": "1k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25905",
    },
    "R_0402_1.5k": {
        "symbol": "R",
        "value": "1.5k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25077",
    },
    "R_0402_2.2k": {
        "symbol": "R",
        "value": "2.2k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25879",
    },
    "R_0402_4.7k": {
        "symbol": "R",
        "value": "4.7k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25900",
    },
    "R_0402_10k": {
        "symbol": "R",
        "value": "10k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25804",
    },
    "R_0402_22k": {
        "symbol": "R",
        "value": "22k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25878",
    },
    "R_0402_47k": {
        "symbol": "R",
        "value": "47k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25819",
    },
    "R_0402_100k": {
        "symbol": "R",
        "value": "100k",
        "footprint": f"{JLC_FP}:R0402",
        "lcsc": "C25741",
    },
}


# =============================================================================
# CAPACITORS
# =============================================================================

CAPACITORS = {
    "C_0402_10pF": {
        "symbol": "C",
        "value": "10pF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C1525",
    },
    "C_0402_22pF": {
        "symbol": "C",
        "value": "22pF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C1555",
    },
    "C_0402_100pF": {
        "symbol": "C",
        "value": "100pF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C1546",
    },
    "C_0402_1nF": {
        "symbol": "C",
        "value": "1nF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C1523",
    },
    "C_0402_10nF": {
        "symbol": "C",
        "value": "10nF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C15195",
    },
    "C_0402_100nF": {
        "symbol": "C",
        "value": "100nF",
        "footprint": f"{JLC_FP}:C0402",
        "lcsc": "C11702",
    },
    "C_0603_1uF": {
        "symbol": "C",
        "value": "1uF",
        "footprint": f"{JLC_FP}:C0603",
        "lcsc": "C15849",
    },
    "C_0603_4.7uF": {
        "symbol": "C",
        "value": "4.7uF",
        "footprint": f"{JLC_FP}:C0603",
        "lcsc": "C19666",
    },
    "C_0805_10uF": {
        "symbol": "C",
        "value": "10uF",
        "footprint": f"{JLC_FP}:C0805",
        "lcsc": "C15850",
    },
    "C_1206_22uF": {
        "symbol": "C",
        "value": "22uF",
        "footprint": f"{JLC_FP}:C1206",
        "lcsc": "C59461",
    },
    "C_1206_47uF": {
        "symbol": "C",
        "value": "47uF",
        "footprint": f"{JLC_FP}:C1206",
        "lcsc": "C96123",
    },
}


# =============================================================================
# POLARIZED CAPACITORS (Electrolytic)
# =============================================================================

CAPACITORS_POLARIZED = {
    "CP_100uF_16V": {
        "symbol": "CP",
        "value": "100uF/16V",
        "footprint": f"{JLC_FP}:CAP-SMD_BD6.3-L6.6-W6.6-LS7.1-FD",
        "lcsc": "C72493",
    },
    "CP_220uF_16V": {
        "symbol": "CP",
        "value": "220uF/16V",
        "footprint": f"{JLC_FP}:CAP-SMD_BD8.0-L8.3-W8.3-LS9.0-FD",
        "lcsc": "C72499",
    },
    "CP_470uF_25V": {
        "symbol": "CP",
        "value": "470uF/25V",
        "footprint": f"{JLC_FP}:CAP-SMD_BD10.0-L10.0-W10.0-LS11.2-FD",
        "lcsc": "C72505",
    },
    "CP_1000uF_16V": {
        "symbol": "CP",
        "value": "1000uF/16V",
        "footprint": f"{JLC_FP}:CAP-SMD_BD10.0-L10.0-W10.0-LS11.2-FD",
        "lcsc": "C249474",
    },
}


# =============================================================================
# INDUCTORS
# =============================================================================

INDUCTORS = {
    "L_4.7uH": {
        "symbol": "L",
        "value": "4.7uH",
        "footprint": f"{JLC_FP}:IND-SMD_L4.0-W4.0",
        "lcsc": "C167256",
    },
    "L_10uH": {
        "symbol": "L",
        "value": "10uH",
        "footprint": f"{JLC_FP}:IND-SMD_L5.0-W5.0",
        "lcsc": "C282098",
    },
    "L_22uH": {
        "symbol": "L",
        "value": "22uH",
        "footprint": f"{JLC_FP}:IND-SMD_L6.0-W6.0",
        "lcsc": "C339747",
    },
    "L_33uH": {
        "symbol": "L",
        "value": "33uH",
        "footprint": f"{JLC_FP}:IND-SMD_L7.3-W7.3",
        "lcsc": "C90748",
    },
    "L_47uH": {
        "symbol": "L",
        "value": "47uH",
        "footprint": f"{JLC_FP}:IND-SMD_L7.3-W7.3",
        "lcsc": "C339825",
    },
}


# =============================================================================
# DIODES
# =============================================================================

DIODES = {
    "D_SS34": {
        "symbol": "D_Schottky",
        "value": "SS34",
        "footprint": f"{JLC_FP}:SMA_L4.3-W2.6-LS5.2-RD",
        "lcsc": "C35722",
    },
    "D_SS54": {
        "symbol": "D_Schottky",
        "value": "SS54",
        "footprint": f"{JLC_FP}:SMB_L4.6-W3.6-LS5.4-RD",
        "lcsc": "C908678",
    },
    "D_1N5819W": {
        "symbol": "D_Schottky",
        "value": "1N5819W",
        "footprint": f"{JLC_FP}:SOD-123_L2.8-W1.8-LS3.7-RD",
        "lcsc": "C67330",
    },
    "D_BAT54S": {
        "symbol": "D_Schottky",
        "value": "BAT54S",
        "footprint": f"{JLC_FP}:SOT-23_L2.9-W1.6-P1.90-LS2.8-TL",
        "lcsc": "C47546",
    },
}


# =============================================================================
# LEDS
# =============================================================================

LEDS = {
    "LED_0603_Red": {
        "symbol": "LED",
        "value": "RED",
        "footprint": f"{JLC_FP}:LED0603-RD",
        "lcsc": "C2290",
    },
    "LED_0603_Green": {
        "symbol": "LED",
        "value": "GREEN",
        "footprint": f"{JLC_FP}:LED0603-RD",
        "lcsc": "C2286",
    },
    "LED_0603_Blue": {
        "symbol": "LED",
        "value": "BLUE",
        "footprint": f"{JLC_FP}:LED0603-RD",
        "lcsc": "C72041",
    },
    "LED_0603_Yellow": {
        "symbol": "LED",
        "value": "YELLOW",
        "footprint": f"{JLC_FP}:LED0603-RD",
        "lcsc": "C72038",
    },
}


# =============================================================================
# CRYSTALS
# =============================================================================

CRYSTALS = {
    "Crystal_8MHz": {
        "symbol": "Crystal",
        "value": "8MHz",
        "footprint": f"{JLC_FP}:HC-49S_L11.0-W4.6",
        "lcsc": "C255909",
    },
    "Crystal_12MHz": {
        "symbol": "Crystal",
        "value": "12MHz",
        "footprint": f"{JLC_FP}:HC-49S_L11.0-W4.6",
        "lcsc": "C9002",
    },
    "Crystal_24MHz": {
        "symbol": "Crystal",
        "value": "24MHz",
        "footprint": f"{JLC_FP}:HC-49S_L11.0-W4.6",
        "lcsc": "C9009",
    },
    "Crystal_25MHz": {
        "symbol": "Crystal",
        "value": "25MHz",
        "footprint": f"{JLC_FP}:HC-49S_L11.0-W4.6",
        "lcsc": "C9010",
    },
}


# =============================================================================
# VOLTAGE REGULATORS
# =============================================================================

REGULATORS = {
    "LM2596S-5.0": {
        "symbol": "LM2596S-5",
        "value": "LM2596S-5.0",
        "footprint": f"{JLC_FP}:TO-263-5_L10.2-W8.9-P1.70-TL",
        "lcsc": "C347421",
    },
    "LM2596S-ADJ": {
        "symbol": "LM2596S-ADJ",
        "value": "LM2596S-ADJ",
        "footprint": f"{JLC_FP}:TO-263-5_L10.2-W8.9-P1.70-TL",
        "lcsc": "C29781",
    },
}


# =============================================================================
# USB ICs
# =============================================================================

USB_ICS = {
    "USB5744": {
        "symbol": "USB5744",
        "value": "USB5744",
        "footprint": f"{JLC_FP}:QFN-56_L7.0-W7.0-P0.40-BL-EP4.2",
        "lcsc": "C132377",
    },
    "USB3320": {
        "symbol": "USB3320",
        "value": "USB3320C-EZK",
        "footprint": f"{JLC_FP}:QFN-32_L5.0-W5.0-P0.50-BL-EP3.4",
        "lcsc": "C129386",
    },
    "CP2102N": {
        "symbol": "CP2102N",
        "value": "CP2102N-A02-GQFN24",
        "footprint": f"{JLC_FP}:QFN-24_L4.0-W4.0-P0.50-BL-EP2.6",
        "lcsc": "C105018",
    },
}


# =============================================================================
# ETHERNET ICs
# =============================================================================

ETHERNET_ICS = {
    "RTL8211F": {
        "symbol": "RTL8211F",
        "value": "RTL8211F-CG",
        "footprint": f"{JLC_FP}:QFN-48_L7.0-W7.0-P0.50-BL-EP5.5",
        "lcsc": "C69264",
    },
}


# =============================================================================
# HDMI ICs
# =============================================================================

HDMI_ICS = {
    "IT6801FN": {
        "symbol": "IT6801FN",
        "value": "IT6801FN",
        "footprint": f"{JLC_FP}:LQFP-100_L14.0-W14.0-P0.50-LS16.0",
        "lcsc": "C2651318",
    },
    "IT66121FN": {
        "symbol": "IT66121FN",
        "value": "IT66121FN",
        "footprint": f"{JLC_FP}:LQFP-100_L14.0-W14.0-P0.50-LS16.0",
        "lcsc": "C2652461",
    },
}


# =============================================================================
# RS485 / UART ICs
# =============================================================================

INTERFACE_ICS = {
    "MAX485": {
        "symbol": "MAX485",
        "value": "MAX485ESA",
        "footprint": f"{JLC_FP}:SOIC-8_L4.9-W3.9-P1.27-LS6.0-BL",
        "lcsc": "C9106",
    },
    "SP485": {
        "symbol": "MAX485",
        "value": "SP485EEN",
        "footprint": f"{JLC_FP}:SOIC-8_L4.9-W3.9-P1.27-LS6.0-BL",
        "lcsc": "C8927",
    },
}


# =============================================================================
# CONNECTORS
# =============================================================================

CONNECTORS = {
    "Barrel_Jack_5.5x2.1": {
        "symbol": "Barrel_Jack",
        "value": "DC_12V",
        "footprint": "Connector_BarrelJack:BarrelJack_Horizontal",
        "lcsc": "",
    },
    "USB_A_Receptacle": {
        "symbol": "USB_A",
        "value": "USB_A",
        "footprint": f"{JLC_FP}:USB-A-TH_USB-A-F-90",
        "lcsc": "C46406",
    },
    "USB_C_Receptacle": {
        "symbol": "USB_C",
        "value": "USB_C",
        "footprint": f"{JLC_FP}:USB-C-SMD_TYPE-C-31-M-12",
        "lcsc": "C165948",
    },
    "RJ45_Magjack": {
        "symbol": "RJ45_Magjack",
        "value": "RJ45",
        "footprint": f"{JLC_FP}:RJ45-TH_8P8C_L21.0-W16.0-H13.0",
        "lcsc": "C138388",
    },
    "HDMI_A_Receptacle": {
        "symbol": "HDMI_A",
        "value": "HDMI",
        "footprint": f"{JLC_FP}:HDMI-SMD_HDMI-001S",
        "lcsc": "C138380",
    },
    "Conn_2x10_2.54mm": {
        "symbol": "Conn_2x10",
        "value": "2x10",
        "footprint": f"{JLC_FP}:HDR-TH_20P-P2.54-V-2X10",
        "lcsc": "C124378",
    },
}


# =============================================================================
# SWITCHES
# =============================================================================

SWITCHES = {
    "SW_Push_4x4": {
        "symbol": "SW_Push",
        "value": "SW_Push",
        "footprint": f"{JLC_FP}:SW-SMD_L4.0-W4.0-P2.20",
        "lcsc": "C115357",
    },
    "SW_Push_6x6": {
        "symbol": "SW_Push",
        "value": "SW_Push",
        "footprint": f"{JLC_FP}:SW-TH_4P-L6.0-W6.0-H4.3-LS6.5",
        "lcsc": "C127478",
    },
}


# =============================================================================
# ALL PARTS COMBINED
# =============================================================================

JLCPCB_PARTS = {
    **RESISTORS,
    **CAPACITORS,
    **CAPACITORS_POLARIZED,
    **INDUCTORS,
    **DIODES,
    **LEDS,
    **CRYSTALS,
    **REGULATORS,
    **USB_ICS,
    **ETHERNET_ICS,
    **HDMI_ICS,
    **INTERFACE_ICS,
    **CONNECTORS,
    **SWITCHES,
}


def get_part(part_key: str) -> dict:
    """Get part information by key.

    Args:
        part_key: Part identifier (e.g., "R_0402_10k")

    Returns:
        Dict with symbol, value, footprint, lcsc

    Raises:
        KeyError: If part not found
    """
    if part_key not in JLCPCB_PARTS:
        raise KeyError(f"Part '{part_key}' not found in JLCPCB_PARTS database")
    return JLCPCB_PARTS[part_key]


def list_parts_by_category(category: str) -> list:
    """List all parts in a category.

    Args:
        category: 'resistors', 'capacitors', 'inductors', etc.

    Returns:
        List of part keys
    """
    categories = {
        'resistors': RESISTORS,
        'capacitors': CAPACITORS,
        'capacitors_polarized': CAPACITORS_POLARIZED,
        'inductors': INDUCTORS,
        'diodes': DIODES,
        'leds': LEDS,
        'crystals': CRYSTALS,
        'regulators': REGULATORS,
        'usb': USB_ICS,
        'ethernet': ETHERNET_ICS,
        'hdmi': HDMI_ICS,
        'interface': INTERFACE_ICS,
        'connectors': CONNECTORS,
        'switches': SWITCHES,
    }
    return list(categories.get(category, {}).keys())
