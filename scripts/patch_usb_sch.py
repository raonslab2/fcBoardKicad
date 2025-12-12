
import os

def patch_usb_sch():
    sch_file = 'fcBoard_USB.kicad_sch'
    
    wires = []
    labels = []

    # U7~U10 TPS2041B
    tps_centers = [
        (7, 53.82),
        (8, 93.82),
        (9, 133.82),
        (10, 173.82)
    ]
    
    center_x = 266.52
    en_pin_x = center_x - 8.89
    fault_pin_x = center_x + 8.89
    
    for idx, (u_num, center_y) in enumerate(tps_centers):
        usb_port = idx + 1
        pin_y = center_y + 2.54 # Y increases downwards in KiCad Eeschema usually
        # Caution: Earlier calculation: 
        # Pin Y = CenterY - PinOffset
        # If Symbol Y is +2.54 (up), Screen Y = Center - 2.54.
        # If Symbol Y is -2.54 (down), Screen Y = Center - (-2.54) = Center + 2.54.
        # TPS2041B Pin 3 EN is at (at -8.89 -2.54). So Screen Y = CenterY - (-2.54) = CenterY + 2.54.
        # Correct.
        
        # EN (Left side)
        # Wire from Pin(257.63) to Left(252.63)
        wires.append(f'(wire (pts (xy {en_pin_x} {pin_y}) (xy {en_pin_x - 5.0} {pin_y})) (stroke (width 0) (type default)))')
        # Label
        labels.append(f'(global_label "USB{usb_port}_VBUS_EN" (shape input) (at {en_pin_x - 5.0} {pin_y} 180) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify right)))')
        
        # FAULT (Right side)
        # TPS2041B Pin 4 FAULT is at (at 8.89 -2.54). Screen Y = CenterY + 2.54.
        # Wire from Pin(275.41) to Right(280.41)
        wires.append(f'(wire (pts (xy {fault_pin_x} {pin_y}) (xy {fault_pin_x + 5.0} {pin_y})) (stroke (width 0) (type default)))')
        # Label
        labels.append(f'(global_label "USB{usb_port}_OC" (shape output) (at {fault_pin_x + 5.0} {pin_y} 0) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify left)))')

    # U2 USB5744 ULPI
    # U2 Center (96.52, 83.82)
    # Pin 1 CLK at (-15.24, 20.32) -> Screen Y = 83.82 - 20.32 = 63.5
    
    u2_center_y = 83.82
    pin_x = 96.52 - 15.24 # 81.28
    wire_len = 5.0
    target_x = pin_x - wire_len
    
    # Pin Name, Y-offset (from symbol definition, + is UP)
    ulpi_pins = [
        ("ULPI_CLK", 20.32),
        ("ULPI_DIR", 17.78),
        ("ULPI_NXT", 15.24),
        ("ULPI_STP", 12.70),
        ("ULPI_DATA0", 7.62),
        ("ULPI_DATA1", 5.08),
        ("ULPI_DATA2", 2.54),
        ("ULPI_DATA3", 0.00),
        ("ULPI_DATA4", -2.54),
        ("ULPI_DATA5", -5.08),
        ("ULPI_DATA6", -7.62),
        ("ULPI_DATA7", -10.16)
    ]
    
    for name, y_offset in ulpi_pins:
        screen_y = u2_center_y - y_offset
        wires.append(f'(wire (pts (xy {pin_x} {screen_y}) (xy {target_x} {screen_y})) (stroke (width 0) (type default)))')
        labels.append(f'(label "{name}" (at {target_x} {screen_y} 180) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify right)))')

    patch_content = "\n".join(wires) + "\n" + "\n".join(labels)
    
    # Apply patch
    with open(sch_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the last closing parenthesis
    last_paren_index = content.rfind(')')
    
    if last_paren_index == -1:
        print("Error: Could not find closing parenthesis")
        return

    indented_patch = ""
    for line in patch_content.splitlines():
        indented_patch += "\t" + line + "\n"
        
    new_content = content[:last_paren_index] + indented_patch + content[last_paren_index:]
    
    with open(sch_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully patched {sch_file}")

if __name__ == "__main__":
    patch_usb_sch()


