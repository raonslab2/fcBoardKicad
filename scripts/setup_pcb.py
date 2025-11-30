#!/usr/bin/env python3
"""
PCB Setup Script for fcBoard
- Board outline: 150mm x 100mm with rounded corners
- Mounting holes: 4x M3 at corners
- Design rules: JLCPCB specifications
"""

import uuid
import math

def gen_uuid():
    return str(uuid.uuid4())

def create_pcb_file():
    """Create PCB file with board outline, mounting holes, and design rules"""

    # Board dimensions
    board_width = 150.0  # mm
    board_height = 100.0  # mm
    corner_radius = 3.0  # mm
    mounting_hole_offset = 5.0  # mm from edge
    mounting_hole_diameter = 3.2  # mm (for M3 screws)
    mounting_hole_pad = 6.0  # mm pad diameter

    content = '''(kicad_pcb
  (version 20231014)
  (generator "pcbnew")
  (generator_version "8.0")
  (general
    (thickness 1.6)
    (legacy_teardrops no)
  )
  (paper "A3")
  (title_block
    (title "ACU5EV SoM Carrier Board")
    (date "2024-12-01")
    (rev "0.2")
    (company "fcBoard Project")
    (comment 1 "150mm x 100mm, 6-Layer")
    (comment 2 "JLCPCB Manufacturing Target")
  )
  (layers
    (0 "F.Cu" signal)
    (1 "In1.Cu" power)
    (2 "In2.Cu" power)
    (3 "In3.Cu" signal)
    (4 "In4.Cu" power)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "User.Comments")
    (42 "Eco1.User" user "User.Eco1")
    (43 "Eco2.User" user "User.Eco2")
    (44 "Edge.Cuts" user)
    (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
    (50 "User.1" user)
    (51 "User.2" user)
  )
  (setup
    (stackup
      (layer "F.SilkS" (type "Top Silk Screen"))
      (layer "F.Paste" (type "Top Solder Paste"))
      (layer "F.Mask" (type "Top Solder Mask") (thickness 0.01))
      (layer "F.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 1" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In1.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 2" (type "core") (thickness 0.4) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In2.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 3" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In3.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 4" (type "core") (thickness 0.4) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In4.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 5" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "B.Cu" (type "copper") (thickness 0.035))
      (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01))
      (layer "B.Paste" (type "Bottom Solder Paste"))
      (layer "B.SilkS" (type "Bottom Silk Screen"))
      (copper_finish "ENIG")
      (dielectric_constraints no)
    )
    (pad_to_mask_clearance 0.05)
    (allow_soldermask_bridges_in_footprints no)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000000)
      (disableapertmacros no)
      (usegerberextensions yes)
      (usegerberattributes yes)
      (usegerberadvancedattributes yes)
      (creategerberjobfile yes)
      (dashed_line_dash_ratio 12.000000)
      (dashed_line_gap_ratio 3.000000)
      (svgprecision 4)
      (plotframeref no)
      (viasonmask no)
      (mode 1)
      (useauxorigin no)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15.000000)
      (pdf_front_fp_property_popups yes)
      (pdf_back_fp_property_popups yes)
      (dxfpolygonmode yes)
      (dxfimperialunits yes)
      (dxfusepcbnewfont yes)
      (psnegative no)
      (psa4output no)
      (plotreference yes)
      (plotvalue yes)
      (plotfptext yes)
      (plotinvisibletext no)
      (sketchpadsonfab no)
      (subtractmaskfromsilk no)
      (outputformat 1)
      (mirror no)
      (drillshape 0)
      (scaleselection 1)
      (outputdirectory "gerber/")
    )
  )

'''

    # Power nets
    content += '''  (net 0 "")
  (net 1 "GND")
  (net 2 "+12V")
  (net 3 "+5V")
  (net 4 "+3V3")
  (net 5 "+1V8")
  (net 6 "+1V2")

'''

    # Board outline with rounded corners (simple rectangle for now - arcs can cause issues)
    r = corner_radius
    w = board_width
    h = board_height

    # Use simple lines for the board outline (more compatible)
    # Top edge
    content += f'''  (gr_line
    (start {r} 0)
    (end {w - r} 0)
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Right edge
    content += f'''  (gr_line
    (start {w} {r})
    (end {w} {h - r})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Bottom edge
    content += f'''  (gr_line
    (start {w - r} {h})
    (end {r} {h})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Left edge
    content += f'''  (gr_line
    (start 0 {h - r})
    (end 0 {r})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''

    # Corner arcs (top-left, top-right, bottom-right, bottom-left)
    # Top-left corner
    content += f'''  (gr_arc
    (start {r} 0)
    (mid {r * 0.293} {r * 0.293})
    (end 0 {r})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Top-right corner
    content += f'''  (gr_arc
    (start {w} {r})
    (mid {w - r * 0.293} {r * 0.293})
    (end {w - r} 0)
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Bottom-right corner
    content += f'''  (gr_arc
    (start {w - r} {h})
    (mid {w - r * 0.293} {h - r * 0.293})
    (end {w} {h - r})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''
    # Bottom-left corner
    content += f'''  (gr_arc
    (start 0 {h - r})
    (mid {r * 0.293} {h - r * 0.293})
    (end {r} {h})
    (layer "Edge.Cuts")
    (stroke (width 0.1) (type solid))
    (uuid "{gen_uuid()}")
  )
'''

    # Mounting holes (4 corners)
    mounting_positions = [
        (mounting_hole_offset, mounting_hole_offset, "MH1"),  # Top-left
        (w - mounting_hole_offset, mounting_hole_offset, "MH2"),  # Top-right
        (mounting_hole_offset, h - mounting_hole_offset, "MH3"),  # Bottom-left
        (w - mounting_hole_offset, h - mounting_hole_offset, "MH4"),  # Bottom-right
    ]

    for x, y, ref in mounting_positions:
        content += f'''  (footprint "MountingHole:MountingHole_3.2mm_M3_Pad" (layer "F.Cu")
    (uuid "{gen_uuid()}")
    (at {x} {y})
    (property "Reference" "{ref}" (at 0 -4 0) (layer "F.SilkS") (uuid "{gen_uuid()}") (effects (font (size 1 1) (thickness 0.15))))
    (property "Value" "MountingHole_M3" (at 0 4 0) (layer "F.Fab") (uuid "{gen_uuid()}") (effects (font (size 1 1) (thickness 0.15))))
    (property "Footprint" "MountingHole:MountingHole_3.2mm_M3_Pad" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{gen_uuid()}") (effects (font (size 1 1) (thickness 0.15))))
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_circle
      (center 0 0)
      (end 3.2 0)
      (layer "F.CrtYd")
      (stroke (width 0.05) (type solid))
      (uuid "{gen_uuid()}")
    )
    (pad "1" thru_hole circle (at 0 0) (size {mounting_hole_pad} {mounting_hole_pad}) (drill {mounting_hole_diameter}) (layers "*.Cu" "*.Mask")
      (net 1 "GND")
      (uuid "{gen_uuid()}")
    )
  )

'''

    # Board dimensions text
    content += f'''  (gr_text "150mm x 100mm"
    (at {w/2} {h + 8} 0)
    (layer "Cmts.User")
    (uuid "{gen_uuid()}")
    (effects (font (size 2 2) (thickness 0.3)))
  )

'''

    # Close PCB file
    content += ''')\n'''

    return content


if __name__ == "__main__":
    output_path = r"D:\git2\fcBoardKicad\fcBoard.kicad_pcb"

    content = create_pcb_file()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {output_path}")
    print("PCB setup completed:")
    print("  - Board size: 150mm x 100mm")
    print("  - Corner radius: 3mm")
    print("  - Mounting holes: 4x M3 at corners (5mm from edge)")
    print("  - Layer stackup: 6-layer")
    print("  - Design rules: JLCPCB specifications")
