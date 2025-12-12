
import uuid
import shutil
import os

def restore_and_patch():
    sch_file = 'fcBoard_USB.kicad_sch'
    bak_file = 'fcBoard_USB.kicad_sch.bak'
    
    # Restore from backup if exists
    if os.path.exists(bak_file):
        shutil.copy(bak_file, sch_file)
        print(f"Restored {sch_file} from backup.")
    else:
        print("Backup file not found, cannot restore. Aborting to prevent corruption.")
        return

    wires = []
    labels = []

    # Helper to generate UUID
    def gen_uuid():
        return str(uuid.uuid4())

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
        pin_y = center_y + 2.54
        
        # EN (Left side)
        # Wire
        wires.append(f'\t(wire (pts (xy {en_pin_x} {pin_y}) (xy {en_pin_x - 5.0} {pin_y})) (stroke (width 0) (type default)) (uuid "{gen_uuid()}"))')
        # Label - REMOVED (fields_autohidden)
        labels.append(f'\t(global_label "USB{usb_port}_VBUS_EN" (shape input) (at {en_pin_x - 5.0} {pin_y} 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid "{gen_uuid()}"))')
        
        # FAULT (Right side)
        # Wire
        wires.append(f'\t(wire (pts (xy {fault_pin_x} {pin_y}) (xy {fault_pin_x + 5.0} {pin_y})) (stroke (width 0) (type default)) (uuid "{gen_uuid()}"))')
        # Label - REMOVED (fields_autohidden)
        labels.append(f'\t(global_label "USB{usb_port}_OC" (shape output) (at {fault_pin_x + 5.0} {pin_y} 0) (effects (font (size 1.27 1.27)) (justify left)) (uuid "{gen_uuid()}"))')

    # U2 USB5744 ULPI
    u2_center_y = 83.82
    pin_x = 96.52 - 15.24 # 81.28
    wire_len = 5.0
    target_x = pin_x - wire_len
    
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
        # Wire
        wires.append(f'\t(wire (pts (xy {pin_x} {screen_y}) (xy {target_x} {screen_y})) (stroke (width 0) (type default)) (uuid "{gen_uuid()}"))')
        # Label - REMOVED (fields_autohidden)
        labels.append(f'\t(label "{name}" (at {target_x} {screen_y} 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid "{gen_uuid()}"))')

    patch_content = "\n".join(wires) + "\n" + "\n".join(labels)
    
    # Apply patch
    with open(sch_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the last closing parenthesis
    last_paren_index = content.rfind(')')
    
    if last_paren_index == -1:
        print("Error: Could not find closing parenthesis")
        return

    new_content = content[:last_paren_index] + patch_content + "\n" + content[last_paren_index:]
    
    with open(sch_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully patched {sch_file} with UUIDs (Corrected Syntax)")

if __name__ == "__main__":
    restore_and_patch()
