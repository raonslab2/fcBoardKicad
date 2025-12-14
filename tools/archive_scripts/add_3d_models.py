#!/usr/bin/env python3
"""
Add 3D model references to footprints in PCB file
"""

import re

def add_3d_models_to_pcb(pcb_path):
    """Add 3D model paths to footprints in PCB file"""

    with open(pcb_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3D model mappings: footprint pattern -> model path
    model_map = {
        'Connector_RJ:RJ45_Hanrun_HR911105A_Horizontal': '${KIPRJMOD}/3dmodels/RJ45_Hanrun_HR911105A_Horizontal.step',
        'Connector_BarrelJack:BarrelJack_Horizontal': '${KIPRJMOD}/3dmodels/BarrelJack_Horizontal.step',
        'Connector_Card:microSD_HC_Wuerth_693072010801': '${KIPRJMOD}/3dmodels/microSD_HC_Wuerth_693072010801.step',
    }

    updated_count = 0

    for fp_name, model_path in model_map.items():
        # Find footprint blocks that don't already have a model
        # Pattern: (footprint "NAME" ... ) without (model inside
        pattern = rf'(\(footprint "{re.escape(fp_name)}".*?)(\n\t\))'

        def add_model(match):
            block = match.group(1)
            ending = match.group(2)

            # Check if already has model
            if '(model ' in block:
                return match.group(0)

            # Add model before closing parenthesis
            model_block = f'''
		(model "{model_path}"
			(offset (xyz 0 0 0))
			(scale (xyz 1 1 1))
			(rotate (xyz 0 0 0))
		)'''
            return block + model_block + ending

        new_content = re.sub(pattern, add_model, content, flags=re.DOTALL)

        if new_content != content:
            count = content.count(f'(footprint "{fp_name}"')
            updated_count += count
            content = new_content
            print(f"  Added 3D model to: {fp_name} ({count} instances)")

    if updated_count > 0:
        with open(pcb_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nSaved {updated_count} 3D model references to PCB file")
    else:
        print("No updates needed")

    return updated_count


if __name__ == "__main__":
    pcb_path = r"D:\git2\fcBoardKicad\fcBoard.kicad_pcb"
    print("Adding 3D models to PCB footprints...")
    add_3d_models_to_pcb(pcb_path)
