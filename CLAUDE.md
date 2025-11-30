# CLAUDE.md - AI Assistant Guide for fcBoardKicad

## Project Overview

This is a **KiCad 8/9 hardware design project** for a carrier board targeting the **ALINX ACU5EV SoM** (System on Module) based on the Xilinx Zynq UltraScale+ XCZU5EV MPSoC.

**Primary Language:** Korean (documentation), English (technical labels)

## Repository Structure

```
fcBoardKicad/
├── fcBoard.kicad_pro          # Main KiCad project file
├── fcBoard.kicad_sch          # Top-level hierarchical schematic
├── fcBoard.kicad_pcb          # PCB layout file
├── fcBoard.kicad_prl          # Project local settings
├── fcBoard_*.kicad_sch        # Hierarchical sub-schematics:
│   ├── fcBoard_Power.kicad_sch      # Power supply circuits
│   ├── fcBoard_USB.kicad_sch        # USB 3.0 hub (USB5744)
│   ├── fcBoard_Ethernet.kicad_sch   # Dual Gigabit Ethernet
│   ├── fcBoard_HDMI.kicad_sch       # HDMI I/O (IT6801FN/IT66121FN)
│   └── fcBoard_Peripherals.kicad_sch # RS485, CAN, GPIO, etc.
├── fcBoard_BOM.csv            # Bill of Materials (generated)
├── fcBoard_BOM.txt            # BOM text format
├── libraries/                  # Project-specific libraries
│   ├── fcBoard.kicad_sym      # Custom symbol library
│   ├── fcBoard.pretty/        # Custom footprint library
│   ├── symbols/               # SoM connector symbols (J29-J32)
│   └── 3dmodels/              # 3D models for components
├── docs/
│   ├── pinmap/                # SoM connector pinout CSVs
│   │   ├── J29_BANK65_66.csv  # HDMI, MIPI, Ethernet PL
│   │   ├── J30_BANK25_26_MGT.csv # PCIe, SFP
│   │   ├── J31_BANK24_44.csv  # RS485, GPIO
│   │   └── J32_MIO_POWER.csv  # PS MIO, Power
│   └── work/                  # Working documents/images
├── scripts/                    # Python automation tools
│   ├── kicad_tools.py         # Annotation, footprint assignment
│   ├── generate_*.py          # Schematic generators
│   └── verify_connections.py  # Connection verification
├── down/                       # Downloaded component files
│   └── AXK6A2337YG/           # Panasonic connector resources
├── fcBoard-backups/           # KiCad auto-backup files
├── sym-lib-table              # Symbol library configuration
└── fp-lib-table               # Footprint library configuration
```

## KiCad File Formats

| Extension | Format | Description |
|-----------|--------|-------------|
| `.kicad_sch` | S-expression text | Schematic files (human-readable) |
| `.kicad_pcb` | S-expression text | PCB layout (human-readable) |
| `.kicad_sym` | S-expression text | Symbol library |
| `.kicad_mod` | S-expression text | Footprint definition |
| `.kicad_pro` | JSON | Project settings |
| `.kicad_prl` | JSON | Local project settings |

**Important:** KiCad files use S-expression format (Lisp-like syntax). When editing:
- Maintain proper indentation
- Preserve UUID fields - do not modify or duplicate
- Keep coordinate precision consistent

## Hardware Design Overview

### SoM Connectors (4x 120-pin Panasonic AXK6A2337YG)

| Connector | Primary Functions |
|-----------|-------------------|
| **J29** | BANK65/66: HDMI Input, MIPI CSI-2, Ethernet PL |
| **J30** | MGT505/BANK25/26: PCIe x2, SFP+ |
| **J31** | BANK24/44: RS485 x2, User LEDs, Buttons |
| **J32** | PS MIO: USB, Ethernet PS, SD Card, Power (+12V, VCCO) |

### Key ICs and Interfaces

- **USB Hub:** Microchip USB5744 (4-port USB 3.0)
- **Ethernet PHY:** Realtek RTL8211F-CG (RGMII)
- **HDMI Input:** ITE IT6801FN
- **HDMI Output:** ITE IT66121FN
- **USB-UART:** Silicon Labs CP2102N
- **Power:** TPS54360 (12V→5V), TPS62827 (5V→3.3V/1.8V)

### Power Rails

| Rail | Voltage | Source |
|------|---------|--------|
| Input | +12V DC | External supply (5A min) |
| +5V | 5.0V | TPS54360 buck converter |
| +3V3 | 3.3V | TPS62827 from 5V |
| +1V8 | 1.8V | TPS73118 LDO / carrier supply |
| VCCO_65/66 | 1.8V | Carrier board supplies to SoM |

## Development Workflow

### Opening the Project
```bash
# KiCad 8.0+ required
kicad fcBoard.kicad_pro
```

### Python Scripts (in `scripts/`)

Scripts use **Python 3** and parse KiCad S-expression files directly.

| Script | Purpose |
|--------|---------|
| `kicad_tools.py` | Annotation, footprint assignment, BOM generation |
| `generate_power_sch.py` | Generate power supply schematic |
| `generate_usb_sch.py` | Generate USB hub schematic |
| `generate_ethernet_sch.py` | Generate Ethernet schematic |
| `generate_hdmi_sch.py` | Generate HDMI I/O schematic |
| `generate_peripherals_sch.py` | Generate peripheral schematic |
| `verify_connections.py` | Verify schematic connectivity |
| `fix_annotations.py` | Fix reference designators |

**Note:** Scripts have hardcoded Windows paths (`D:\git2\fcBoardKicad`). Update `PROJECT_DIR` for your environment.

### Running Verification
```bash
cd scripts
python verify_connections.py
```

## Coding Conventions

### Reference Designators
- `C` - Capacitors
- `R` - Resistors
- `L` - Inductors
- `FB` - Ferrite beads
- `D` - Diodes/LEDs
- `U` - ICs
- `J` - Connectors
- `Y` - Crystals
- `SW` - Switches

### Net Naming
- Power: `+12V`, `+5V`, `+3V3`, `+1V8`, `GND`
- Differential pairs: `*_P` / `*_N` suffix
- Bus signals: `SIGNAL[n]` or `SIGNAL_n`
- FPGA banks: `B65_L1_P` (Bank65, Lane1, Positive)

### Footprint Sizes (Default SMD)
- Resistors: 0402 (1005 Metric)
- Capacitors: 0402-1206 depending on value
- Standard passives prefer 0402 for space efficiency

## AI Assistant Guidelines

### DO
- Read schematic files to understand circuit topology
- Parse pinmap CSVs for connector information
- Suggest component values based on reference designs
- Help with Python script modifications
- Explain circuit functionality from schematics
- Verify net connectivity using existing scripts

### DON'T
- Generate random UUIDs - let KiCad manage them
- Modify `.kicad_prl` files (local settings)
- Edit schematic coordinates without understanding hierarchy
- Change library paths in `*-lib-table` files arbitrarily
- Delete backup files in `fcBoard-backups/`

### When Editing Schematics
1. Preserve all UUID fields exactly as-is
2. Maintain S-expression structure and nesting
3. Keep coordinate values as floats with consistent precision
4. Use existing symbols from `libraries/fcBoard.kicad_sym`
5. Reference pinmap CSVs for correct signal assignments

### Common Tasks

**Adding a component:**
1. Check if symbol exists in `libraries/fcBoard.kicad_sym`
2. Use footprints from `libraries/fcBoard.pretty/` or standard KiCad libs
3. Follow reference designator conventions

**Checking connections:**
```bash
python scripts/verify_connections.py
```

**Generating BOM:**
```bash
python scripts/kicad_tools.py
```

## PCB Design Specifications

- **Layers:** 6-layer recommended
- **Thickness:** 1.6mm
- **Impedance:** Single-ended 50Ω, Differential 100Ω
- **Min trace/space:** 0.1mm / 0.1mm
- **Min via drill:** 0.3mm

## External References

- ACU5EV SoM documentation (ALINX)
- Panasonic AXK6A2337YG connector datasheet
- Xilinx UltraScale+ MPSoC technical reference

## File Encoding

All text files use **UTF-8** encoding. KiCad schematic files may contain Korean characters in comments.
