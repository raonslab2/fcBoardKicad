"""
KiCad Schematic Generation Library

A library for generating KiCad schematics with embedded symbols.
All symbols are 2.54mm grid aligned and include LCSC part numbers for JLCPCB compatibility.

Usage:
    from kicad_lib import SchematicGenerator

    sch = SchematicGenerator("Power", "Power Supply")
    sch.add_common_symbols("R", "C", "L")
    sch.add_power_symbols("GND", "+5V", "+3V3")
    sch.place_resistor("R1", "10k", 100, 50, lcsc="C25804")
    sch.save()
"""

from .generator import SchematicGenerator
from .symbols import COMMON_SYMBOLS, POWER_SYMBOLS, IC_SYMBOLS, CONNECTOR_SYMBOLS
from .components import JLCPCB_PARTS

__all__ = [
    'SchematicGenerator',
    'COMMON_SYMBOLS',
    'POWER_SYMBOLS',
    'IC_SYMBOLS',
    'CONNECTOR_SYMBOLS',
    'JLCPCB_PARTS',
]

__version__ = "1.0.0"
