"""
KiCad Schematic Generator

Main class for generating KiCad schematics with embedded symbols.
Handles symbol placement, wiring, labels, and file generation.

Usage:
    from kicad_lib import SchematicGenerator

    sch = SchematicGenerator("Power", "Power Supply")
    sch.add_common_symbols("R", "C", "L")
    sch.add_power_symbols("GND", "+5V")
    sch.place_component("R_0402_10k", "R1", 100, 50)
    sch.save()
"""

import uuid
import hashlib
from pathlib import Path
from typing import Optional

from .symbols import COMMON_SYMBOLS, POWER_SYMBOLS, IC_SYMBOLS, CONNECTOR_SYMBOLS
from .components import JLCPCB_PARTS


def gen_uuid() -> str:
    """Generate a random UUID."""
    return str(uuid.uuid4())


def generate_deterministic_uuid(seed: str) -> str:
    """Generate a deterministic UUID from a seed string.

    This ensures the same schematic name always gets the same UUID,
    which helps with reference annotation consistency.
    """
    hash_bytes = hashlib.md5(seed.encode()).digest()
    return str(uuid.UUID(bytes=hash_bytes))


class SchematicGenerator:
    """Generator for KiCad schematic files with embedded symbols."""

    def __init__(self, name: str, title: str, project: str = "fcBoard"):
        """Initialize the schematic generator.

        Args:
            name: Schematic name (e.g., "Power", "USB")
            title: Display title (e.g., "Power Supply", "USB 3.0 Hub")
            project: Project name (default: "fcBoard")
        """
        self.name = name
        self.title = title
        self.project = project
        # Use consistent prefix across all sheets for hierarchical compatibility
        self.prefix = "fcBoard"
        self.schematic_uuid = generate_deterministic_uuid(f"{project}_{name}")

        self._symbols = []  # Symbol definitions for lib_symbols
        self._instances = []  # Component instances
        self._wires = []  # Wire connections
        self._labels = []  # Net labels
        self._hlabels = []  # Hierarchical labels
        self._text = []  # Text annotations

        self._added_symbols = set()  # Track which symbols have been added

    # =========================================================================
    # SYMBOL MANAGEMENT
    # =========================================================================

    def add_symbol(self, category: str, name: str):
        """Add a single symbol definition.

        Args:
            category: 'common', 'power', 'ic', or 'connector'
            name: Symbol name
        """
        key = f"{category}:{name}"
        if key in self._added_symbols:
            return  # Already added

        symbol_dicts = {
            'common': COMMON_SYMBOLS,
            'power': POWER_SYMBOLS,
            'ic': IC_SYMBOLS,
            'connector': CONNECTOR_SYMBOLS,
        }

        symbol_dict = symbol_dicts.get(category)
        if symbol_dict and name in symbol_dict:
            self._symbols.append(symbol_dict[name].format(prefix=self.prefix))
            self._added_symbols.add(key)

    def add_common_symbols(self, *names):
        """Add common passive symbols (R, C, L, etc.)."""
        for name in names:
            self.add_symbol('common', name)

    def add_power_symbols(self, *names):
        """Add power symbols (GND, +5V, +3V3, etc.)."""
        for name in names:
            self.add_symbol('power', name)

    def add_ic_symbol(self, name: str):
        """Add an IC symbol."""
        self.add_symbol('ic', name)

    def add_connector_symbol(self, name: str):
        """Add a connector symbol."""
        self.add_symbol('connector', name)

    # =========================================================================
    # COMPONENT PLACEMENT
    # =========================================================================

    def place_component(self, part_key: str, ref: str, x: float, y: float,
                       rotation: int = 0, mirror: str = ""):
        """Place a component from the JLCPCB parts database.

        Args:
            part_key: Part key from JLCPCB_PARTS (e.g., "R_0402_10k")
            ref: Reference designator (e.g., "R1", "C1")
            x: X coordinate (must be 2.54mm grid aligned)
            y: Y coordinate (must be 2.54mm grid aligned)
            rotation: Rotation in degrees (0, 90, 180, 270)
            mirror: Mirror mode ("x", "y", or "")
        """
        if part_key not in JLCPCB_PARTS:
            raise KeyError(f"Part '{part_key}' not found in JLCPCB_PARTS")

        part = JLCPCB_PARTS[part_key]

        # Ensure the symbol is added
        symbol_name = part['symbol']
        self._ensure_symbol_added(symbol_name)

        # Create the instance
        instance = self._create_component_instance(
            lib_id=f"{self.prefix}:{symbol_name}",
            ref=ref,
            value=part['value'],
            x=x, y=y,
            rotation=rotation,
            mirror=mirror,
            footprint=part['footprint'],
            lcsc=part.get('lcsc', '')
        )
        self._instances.append(instance)

    def place_custom_component(self, symbol_name: str, ref: str, value: str,
                               x: float, y: float, rotation: int = 0,
                               mirror: str = "", footprint: str = "", lcsc: str = ""):
        """Place a custom component not in the parts database.

        Args:
            symbol_name: Symbol name (e.g., "LM2596S-5")
            ref: Reference designator
            value: Display value
            x, y: Coordinates
            rotation: Rotation in degrees
            mirror: Mirror mode
            footprint: Footprint name
            lcsc: LCSC part number
        """
        self._ensure_symbol_added(symbol_name)

        instance = self._create_component_instance(
            lib_id=f"{self.prefix}:{symbol_name}",
            ref=ref,
            value=value,
            x=x, y=y,
            rotation=rotation,
            mirror=mirror,
            footprint=footprint,
            lcsc=lcsc
        )
        self._instances.append(instance)

    def place_power(self, name: str, x: float, y: float, rotation: int = 0):
        """Place a power symbol.

        Args:
            name: Power symbol name (e.g., "GND", "+5V")
            x, y: Coordinates
            rotation: Rotation in degrees
        """
        # Ensure power symbol is added
        self.add_power_symbols(name)

        instance = self._create_power_instance(
            lib_id=f"{self.prefix}:{name}",
            value=name,
            x=x, y=y,
            rotation=rotation
        )
        self._instances.append(instance)

    def _ensure_symbol_added(self, symbol_name: str):
        """Ensure a symbol definition is added to lib_symbols."""
        # Check each category
        for category, symbol_dict in [
            ('common', COMMON_SYMBOLS),
            ('power', POWER_SYMBOLS),
            ('ic', IC_SYMBOLS),
            ('connector', CONNECTOR_SYMBOLS),
        ]:
            if symbol_name in symbol_dict:
                self.add_symbol(category, symbol_name)
                return

    def _create_component_instance(self, lib_id: str, ref: str, value: str,
                                   x: float, y: float, rotation: int = 0,
                                   mirror: str = "", footprint: str = "",
                                   lcsc: str = "") -> str:
        """Create a component instance string."""
        lcsc_property = ""
        if lcsc:
            lcsc_property = f'''
		(property "LCSC Part" "{lcsc}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))'''

        mirror_str = f" (mirror {mirror})" if mirror else ""

        return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} {rotation}){mirror_str}
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "{ref}" (at {x} {y - 5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{value}" (at {x} {y + 5.08} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide)){lcsc_property}
		(instances
			(project "{self.project}"
				(path "/{self.schematic_uuid}" (reference "{ref}") (unit 1))
			)
		)
	)'''

    def _create_power_instance(self, lib_id: str, value: str,
                               x: float, y: float, rotation: int = 0) -> str:
        """Create a power symbol instance string."""
        return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} {rotation})
		(unit 1)
		(exclude_from_sim no)
		(in_bom no)
		(on_board yes)
		(dnp no)
		(uuid "{gen_uuid()}")
		(property "Reference" "#PWR" (at {x} {y + 2.54} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Value" "{value}" (at {x} {y - 2.54} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(property "Description" "" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))
		(instances
			(project "{self.project}"
				(path "/{self.schematic_uuid}" (reference "#PWR") (unit 1))
			)
		)
	)'''

    # =========================================================================
    # WIRING
    # =========================================================================

    def add_wire(self, x1: float, y1: float, x2: float, y2: float):
        """Add a wire between two points.

        Args:
            x1, y1: Start point
            x2, y2: End point
        """
        wire = f'''	(wire
		(pts (xy {x1} {y1}) (xy {x2} {y2}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)'''
        self._wires.append(wire)

    def add_wire_path(self, *points):
        """Add a wire path through multiple points.

        Args:
            points: List of (x, y) tuples
        """
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            self.add_wire(x1, y1, x2, y2)

    # =========================================================================
    # LABELS
    # =========================================================================

    def add_label(self, name: str, x: float, y: float, rotation: int = 0):
        """Add a net label.

        Args:
            name: Label text
            x, y: Position
            rotation: Rotation in degrees
        """
        label = f'''	(label "{name}"
		(at {x} {y} {rotation})
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify left bottom)
		)
		(uuid "{gen_uuid()}")
	)'''
        self._labels.append(label)

    def add_hierarchical_label(self, name: str, x: float, y: float,
                               shape: str = "passive", rotation: int = 0):
        """Add a hierarchical label.

        Args:
            name: Label text
            x, y: Position
            shape: 'input', 'output', 'bidirectional', 'passive'
            rotation: Rotation in degrees (0=right, 180=left)
        """
        justify = "right" if rotation == 180 else "left"
        hlabel = f'''	(hierarchical_label "{name}"
		(shape {shape})
		(at {x} {y} {rotation})
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify {justify})
		)
		(uuid "{gen_uuid()}")
	)'''
        self._hlabels.append(hlabel)

    def add_global_label(self, name: str, x: float, y: float,
                        shape: str = "passive", rotation: int = 0):
        """Add a global label.

        Args:
            name: Label text
            x, y: Position
            shape: 'input', 'output', 'bidirectional', 'passive'
            rotation: Rotation in degrees
        """
        glabel = f'''	(global_label "{name}"
		(shape {shape})
		(at {x} {y} {rotation})
		(fields_autoplaced yes)
		(effects
			(font (size 1.27 1.27))
			(justify left)
		)
		(uuid "{gen_uuid()}")
	)'''
        self._labels.append(glabel)

    # =========================================================================
    # TEXT ANNOTATIONS
    # =========================================================================

    def add_text(self, text: str, x: float, y: float, rotation: int = 0):
        """Add a text annotation.

        Args:
            text: Text content (can include \\n for newlines)
            x, y: Position
            rotation: Rotation in degrees
        """
        annotation = f'''	(text "{text}"
		(exclude_from_sim no)
		(at {x} {y} {rotation})
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{gen_uuid()}")
	)'''
        self._text.append(annotation)

    # =========================================================================
    # FILE GENERATION
    # =========================================================================

    def generate(self) -> str:
        """Generate the complete schematic file content.

        Returns:
            KiCad schematic file content as string
        """
        # Symbols already have proper indentation, just join with newlines
        lib_symbols = '\n\t\t'.join(self._symbols)
        instances = '\n'.join(self._instances)
        wires = '\n'.join(self._wires)
        labels = '\n'.join(self._labels)
        hlabels = '\n'.join(self._hlabels)
        text = '\n'.join(self._text)

        return f'''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{self.schematic_uuid}")
	(paper "A3")
	(title_block
		(title "{self.title}")
		(date "2024-12-11")
		(rev "1.0")
		(company "fcBoard Project")
	)
	(lib_symbols
		{lib_symbols}
	)
{instances}
{wires}
{labels}
{hlabels}
{text}
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
'''

    def save(self, output_path: Optional[str] = None):
        """Save the schematic to a file.

        Args:
            output_path: Output file path. If None, uses default naming.
        """
        if output_path is None:
            # Default: project root / fcBoard_{name}.kicad_sch
            script_dir = Path(__file__).parent.resolve()
            project_root = script_dir.parent.parent
            output_path = project_root / f"fcBoard_{self.name}.kicad_sch"
        else:
            output_path = Path(output_path)

        content = self.generate()
        output_path.write_text(content, encoding='utf-8')
        print(f"[OK] Generated: {output_path}")
        return output_path

    # =========================================================================
    # CONVENIENCE METHODS
    # =========================================================================

    def place_decoupling_cap(self, ref: str, x: float, y: float,
                             value: str = "100nF", rotation: int = 0):
        """Place a decoupling capacitor with GND.

        This is a convenience method that places a capacitor and a GND symbol.

        Args:
            ref: Reference designator (e.g., "C1")
            x, y: Capacitor position
            value: Capacitor value (default: "100nF")
            rotation: Rotation in degrees
        """
        # Map common values to part keys
        value_map = {
            "100nF": "C_0402_100nF",
            "10nF": "C_0402_10nF",
            "1uF": "C_0603_1uF",
            "10uF": "C_0805_10uF",
        }
        part_key = value_map.get(value, "C_0402_100nF")

        self.place_component(part_key, ref, x, y, rotation)
        # GND below the capacitor
        gnd_offset = 7.62 if rotation == 0 else -7.62
        self.place_power("GND", x, y + gnd_offset)
