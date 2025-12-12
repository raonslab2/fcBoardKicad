
def generate_sexpr():
    wires = []
    labels = []

    # U7~U10 TPS2041B
    # Center X = 266.52
    # Pin 3 (EN) offset: X -8.89, Y -(-2.54) = +2.54 (down) => Screen Y = CenterY + 2.54
    # Pin 4 (FAULT) offset: X +8.89, Y +2.54 => Screen Y = CenterY + 2.54
    
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
        # Wire from Pin(257.63) to Left(252.63)
        wires.append(f'(wire (pts (xy {en_pin_x} {pin_y}) (xy {en_pin_x - 5.0} {pin_y})) (stroke (width 0) (type default)))')
        # Label
        labels.append(f'(global_label "USB{usb_port}_VBUS_EN" (shape input) (at {en_pin_x - 5.0} {pin_y} 180) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify right)))')
        
        # FAULT (Right side)
        # Wire from Pin(275.41) to Right(280.41)
        wires.append(f'(wire (pts (xy {fault_pin_x} {pin_y}) (xy {fault_pin_x + 5.0} {pin_y})) (stroke (width 0) (type default)))')
        # Label
        labels.append(f'(global_label "USB{usb_port}_OC" (shape output) (at {fault_pin_x + 5.0} {pin_y} 0) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify left)))')

    # U2 USB5744 ULPI
    # Center X = 96.52, Y = 83.82
    # Pin X = 96.52 - 15.24 = 81.28
    # Pin Ys:
    # Pin 1 (CLK, +20.32) -> Screen Y = 83.82 - 20.32 = 63.5
    # Each pin is 2.54mm step down (except gaps)
    
    u2_center_y = 83.82
    pin_x = 81.28
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
        # Using local labels for ULPI inside the sheet, or hierarchical labels are already defined?
        # The user wanted "modifications". Assuming we connect to the hierarchical labels.
        # Hierarchical labels in KiCad are just labels with special type.
        # Here we just use 'label' for net name, assuming the Hierarchical pins are already on the sheet or will be matched by name.
        # The user modified hierarchical labels earlier. We should use labels to connect them.
        labels.append(f'(label "{name}" (at {target_x} {screen_y} 180) (fields_autohidden) (effects (font (size 1.27 1.27)) (justify right)))')

    print("\n".join(wires))
    print("\n".join(labels))

if __name__ == "__main__":
    generate_sexpr()


