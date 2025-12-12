"""
KiCad Symbol Templates

All symbols are embedded in lib_symbols section with 2.54mm grid aligned pins.
Use {prefix} placeholder for library name (e.g., fcBoard_Power, fcBoard_USB).
"""

# =============================================================================
# COMMON PASSIVE SYMBOLS
# =============================================================================

COMMON_SYMBOLS = {
    "R": '''(symbol "{prefix}:R"
			(pin_numbers hide)
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Resistor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "R_0_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "C": '''(symbol "{prefix}:C"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Capacitor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "C_0_1"
				(polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
			)
			(symbol "C_1_1"
				(pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "CP": '''(symbol "{prefix}:CP"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Value" "CP" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
			(property "Footprint" "" (at 0.9652 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Polarized Capacitor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "CP_0_1"
				(rectangle (start -2.286 0.508) (end 2.286 1.016) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -1.778 2.286) (xy -0.762 2.286)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -1.27 1.778) (xy -1.27 2.794)) (stroke (width 0) (type default)) (fill (type none)))
				(rectangle (start 2.286 -0.508) (end -2.286 -1.016) (stroke (width 0) (type default)) (fill (type outline)))
			)
			(symbol "CP_1_1"
				(pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "L": '''(symbol "{prefix}:L"
			(pin_numbers hide)
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "L" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "L" (at 1.905 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Inductor" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "L_0_1"
				(arc (start 0 -2.54) (mid 0.6323 -1.905) (end 0 -1.27) (stroke (width 0) (type default)) (fill (type none)))
				(arc (start 0 -1.27) (mid 0.6323 -0.635) (end 0 0) (stroke (width 0) (type default)) (fill (type none)))
				(arc (start 0 0) (mid 0.6323 0.635) (end 0 1.27) (stroke (width 0) (type default)) (fill (type none)))
				(arc (start 0 1.27) (mid 0.6323 1.905) (end 0 2.54) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "L_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "D_Schottky": '''(symbol "{prefix}:D_Schottky"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Schottky diode" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "D_Schottky_0_1"
				(polyline (pts (xy 1.27 0) (xy -1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.905 0.635) (xy -1.905 1.27) (xy -1.27 1.27) (xy -1.27 -1.27) (xy -0.635 -1.27) (xy -0.635 -0.635)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "D_Schottky_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "LED": '''(symbol "{prefix}:LED"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LED" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "LED" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "LED_0_1"
				(polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.27 0) (xy 1.27 0)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -3.048 -1.524) (xy -1.27 -3.302)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -1.778 -1.524) (xy 0 -3.302)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -2.032 -2.794) (xy -1.27 -3.556) (xy -1.778 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -0.762 -2.794) (xy 0 -3.556) (xy -0.508 -2.794)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "LED_1_1"
				(pin passive line (at -3.81 0 0) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "Crystal": '''(symbol "{prefix}:Crystal"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "Y" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Crystal" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Crystal Oscillator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Crystal_0_1"
				(rectangle (start -0.762 -1.524) (end 0.762 1.524) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.524 -1.27) (xy -1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 1.524 -1.27) (xy 1.524 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Crystal_1_1"
				(pin passive line (at -3.81 0 0) (length 2.286) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 3.81 0 180) (length 2.286) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "Ferrite_Bead": '''(symbol "{prefix}:Ferrite_Bead"
			(pin_numbers hide)
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "FB" (at -1.27 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "Ferrite_Bead" (at 1.905 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Ferrite Bead" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Ferrite_Bead_0_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -1.016 -2.54) (xy 1.016 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Ferrite_Bead_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "Fuse": '''(symbol "{prefix}:Fuse"
			(pin_numbers hide)
			(pin_names (offset 0))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "F" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "Fuse" (at 0 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Fuse" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Fuse_0_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0 -2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Fuse_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',
}


# =============================================================================
# POWER SYMBOLS
# =============================================================================

POWER_SYMBOLS = {
    "GND": '''(symbol "{prefix}:GND"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "GND" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Power Ground" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "GND_0_1"
				(polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "GND_1_1"
				(pin power_in line (at 0 0 270) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "+12V": '''(symbol "{prefix}:+12V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+12V" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+12V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+12V_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+12V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "+5V": '''(symbol "{prefix}:+5V"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+5V" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+5V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+5V_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+5V_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "+3V3": '''(symbol "{prefix}:+3V3"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+3V3" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+3.3V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+3V3_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+3V3_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "+1V8": '''(symbol "{prefix}:+1V8"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+1V8" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+1.8V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+1V8_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+1V8_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "+2V5": '''(symbol "{prefix}:+2V5"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "+2V5" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "+2.5V Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "+2V5_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "+2V5_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "VBUS": '''(symbol "{prefix}:VBUS"
			(power)
			(pin_numbers hide)
			(pin_names (offset 0) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
			(property "Value" "VBUS" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB VBUS Power Rail" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "VBUS_0_1"
				(polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "VBUS_1_1"
				(pin power_in line (at 0 0 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',
}


# =============================================================================
# IC SYMBOLS - Voltage Regulators
# =============================================================================

IC_SYMBOLS = {
    "LM2596S-5": '''(symbol "{prefix}:LM2596S-5"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LM2596S-5" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "5V 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "LM2596S-5_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "LM2596S-5_1_1"
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "LM2596S-ADJ": '''(symbol "{prefix}:LM2596S-ADJ"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LM2596S-ADJ" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Adjustable 3A Step-Down Regulator" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "LM2596S-ADJ_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "LM2596S-ADJ_1_1"
				(pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at 10.16 -2.54 180) (length 2.54) (name "FB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "ON/OFF" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "USB5744": '''(symbol "{prefix}:USB5744"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB5744" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB 3.0 4-Port Hub Controller" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB5744_0_1"
				(rectangle (start -15.24 24.13) (end 15.24 -24.13) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB5744_1_1"
				(pin power_in line (at -17.78 20.32 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -17.78 17.78 0) (length 2.54) (name "VDDA33" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 12.7 0) (length 2.54) (name "USB_DM" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 10.16 0) (length 2.54) (name "USB_DP" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 5.08 0) (length 2.54) (name "SSRXM" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 2.54 0) (length 2.54) (name "SSRXP" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -2.54 0) (length 2.54) (name "SSTXM" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -17.78 -5.08 0) (length 2.54) (name "SSTXP" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -10.16 0) (length 2.54) (name "XTALIN" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin output line (at -17.78 -12.7 0) (length 2.54) (name "XTALOUT" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin input line (at -17.78 -17.78 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -26.67 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 20.32 180) (length 2.54) (name "DN1_DM" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 17.78 180) (length 2.54) (name "DN1_DP" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 12.7 180) (length 2.54) (name "DN2_DM" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 10.16 180) (length 2.54) (name "DN2_DP" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 5.08 180) (length 2.54) (name "DN3_DM" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 2.54 180) (length 2.54) (name "DN3_DP" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -2.54 180) (length 2.54) (name "DN4_DM" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 17.78 -5.08 180) (length 2.54) (name "DN4_DP" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "USB3320": '''(symbol "{prefix}:USB3320"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB3320" (at 0 20.32 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB 2.0 ULPI PHY" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB3320_0_1"
				(rectangle (start -12.7 19.05) (end 12.7 -19.05) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB3320_1_1"
				(pin power_in line (at -15.24 15.24 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -15.24 12.7 0) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -15.24 7.62 0) (length 2.54) (name "DP" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -15.24 5.08 0) (length 2.54) (name "DM" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin input line (at -15.24 0 0) (length 2.54) (name "REFCLK" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at -15.24 -5.08 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -21.59 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 15.24 180) (length 2.54) (name "DATA0" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 12.7 180) (length 2.54) (name "DATA1" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "DATA2" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 7.62 180) (length 2.54) (name "DATA3" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 5.08 180) (length 2.54) (name "DATA4" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 2.54 180) (length 2.54) (name "DATA5" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 0 180) (length 2.54) (name "DATA6" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 15.24 -2.54 180) (length 2.54) (name "DATA7" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -7.62 180) (length 2.54) (name "CLK" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -10.16 180) (length 2.54) (name "DIR" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 15.24 -12.7 180) (length 2.54) (name "NXT" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin input line (at 15.24 -15.24 180) (length 2.54) (name "STP" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "RTL8211F": '''(symbol "{prefix}:RTL8211F"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
			(property "Value" "RTL8211F-CG" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Gigabit Ethernet PHY with RGMII" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "RTL8211F_0_1"
				(rectangle (start -17.78 26.67) (end 17.78 -26.67) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "RTL8211F_1_1"
				(pin power_in line (at -20.32 22.86 0) (length 2.54) (name "AVDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -20.32 20.32 0) (length 2.54) (name "DVDD" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 15.24 0) (length 2.54) (name "TXD0" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 12.7 0) (length 2.54) (name "TXD1" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 10.16 0) (length 2.54) (name "TXD2" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 7.62 0) (length 2.54) (name "TXD3" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 2.54 0) (length 2.54) (name "TX_CLK" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 0 0) (length 2.54) (name "TX_EN" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -5.08 0) (length 2.54) (name "RXD0" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -7.62 0) (length 2.54) (name "RXD1" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -10.16 0) (length 2.54) (name "RXD2" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -12.7 0) (length 2.54) (name "RXD3" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin output line (at -20.32 -17.78 0) (length 2.54) (name "RX_CLK" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin output line (at -20.32 -20.32 0) (length 2.54) (name "RX_DV" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -29.21 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 22.86 180) (length 2.54) (name "MDI0+" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 20.32 180) (length 2.54) (name "MDI0-" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 17.78 180) (length 2.54) (name "MDI1+" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 15.24 180) (length 2.54) (name "MDI1-" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 12.7 180) (length 2.54) (name "MDI2+" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 10.16 180) (length 2.54) (name "MDI2-" (effects (font (size 1.016 1.016)))) (number "21" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 7.62 180) (length 2.54) (name "MDI3+" (effects (font (size 1.016 1.016)))) (number "22" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 5.08 180) (length 2.54) (name "MDI3-" (effects (font (size 1.016 1.016)))) (number "23" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 -2.54 180) (length 2.54) (name "MDC" (effects (font (size 1.016 1.016)))) (number "24" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 20.32 -5.08 180) (length 2.54) (name "MDIO" (effects (font (size 1.016 1.016)))) (number "25" (effects (font (size 1.016 1.016)))))
				(pin input line (at 20.32 -10.16 180) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "26" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -15.24 180) (length 2.54) (name "INT_N" (effects (font (size 1.016 1.016)))) (number "27" (effects (font (size 1.016 1.016)))))
				(pin input line (at 20.32 -20.32 180) (length 2.54) (name "CLKIN" (effects (font (size 1.016 1.016)))) (number "28" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "IT6801FN": '''(symbol "{prefix}:IT6801FN"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
			(property "Value" "IT6801FN" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI 1.4 Receiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "IT6801FN_0_1"
				(rectangle (start -17.78 26.67) (end 17.78 -26.67) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "IT6801FN_1_1"
				(pin power_in line (at -20.32 22.86 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -20.32 20.32 0) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 15.24 0) (length 2.54) (name "HDMI_D0+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 12.7 0) (length 2.54) (name "HDMI_D0-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 10.16 0) (length 2.54) (name "HDMI_D1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 7.62 0) (length 2.54) (name "HDMI_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 5.08 0) (length 2.54) (name "HDMI_D2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 2.54 0) (length 2.54) (name "HDMI_D2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -2.54 0) (length 2.54) (name "HDMI_CLK+" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -5.08 0) (length 2.54) (name "HDMI_CLK-" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -10.16 0) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -12.7 0) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 -17.78 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -29.21 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 22.86 180) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 17.78 180) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 15.24 180) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 12.7 180) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 7.62 180) (length 2.54) (name "D[23:0]" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -5.08 180) (length 2.54) (name "INT_N" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "IT66121FN": '''(symbol "{prefix}:IT66121FN"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))
			(property "Value" "IT66121FN" (at 0 27.94 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI 1.4 Transmitter" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "IT66121FN_0_1"
				(rectangle (start -17.78 26.67) (end 17.78 -26.67) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "IT66121FN_1_1"
				(pin power_in line (at -20.32 22.86 0) (length 2.54) (name "VDD33" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -20.32 20.32 0) (length 2.54) (name "VDD18" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 15.24 0) (length 2.54) (name "PCLK" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 12.7 0) (length 2.54) (name "HSYNC" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 10.16 0) (length 2.54) (name "VSYNC" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 7.62 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 2.54 0) (length 2.54) (name "D[23:0]" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -5.08 0) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -20.32 -7.62 0) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin input line (at -20.32 -12.7 0) (length 2.54) (name "RESET_N" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -29.21 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 15.24 180) (length 2.54) (name "TX0+" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 12.7 180) (length 2.54) (name "TX0-" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 10.16 180) (length 2.54) (name "TX1+" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 7.62 180) (length 2.54) (name "TX1-" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 5.08 180) (length 2.54) (name "TX2+" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 2.54 180) (length 2.54) (name "TX2-" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -2.54 180) (length 2.54) (name "TXC+" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -5.08 180) (length 2.54) (name "TXC-" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin output line (at 20.32 -10.16 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "MAX485": '''(symbol "{prefix}:MAX485"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
			(property "Value" "MAX485" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "RS-485 Transceiver" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "MAX485_0_1"
				(rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "MAX485_1_1"
				(pin output line (at -10.16 2.54 0) (length 2.54) (name "RO" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 0 0) (length 2.54) (name "RE" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 -2.54 0) (length 2.54) (name "DE" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin input line (at -10.16 -5.08 0) (length 2.54) (name "DI" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -8.89 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "A" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "B" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 8.89 270) (length 2.54) (name "VCC" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "CP2102N": '''(symbol "{prefix}:CP2102N"
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "CP2102N" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB to UART Bridge" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "CP2102N_0_1"
				(rectangle (start -10.16 10.16) (end 10.16 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "CP2102N_1_1"
				(pin power_in line (at -12.7 7.62 0) (length 2.54) (name "VDD" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -12.7 2.54 0) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -12.7 0 0) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin output line (at 12.7 7.62 180) (length 2.54) (name "TXD" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 5.08 180) (length 2.54) (name "RXD" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin output line (at 12.7 0 180) (length 2.54) (name "RTS" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 -2.54 180) (length 2.54) (name "CTS" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin output line (at 12.7 -5.08 180) (length 2.54) (name "DTR" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin input line (at 12.7 -7.62 180) (length 2.54) (name "DSR" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
			)
		)''',
}


# =============================================================================
# CONNECTOR SYMBOLS
# =============================================================================

CONNECTOR_SYMBOLS = {
    "Barrel_Jack": '''(symbol "{prefix}:Barrel_Jack"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Barrel_Jack" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 1.27 -1.016 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 1.27 -1.016 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "DC Barrel Jack" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Barrel_Jack_0_1"
				(rectangle (start -5.08 3.81) (end 3.81 -3.81) (stroke (width 0.254) (type default)) (fill (type background)))
				(arc (start -3.302 3.175) (mid -3.9288 2.54) (end -3.302 1.905) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy -3.302 3.175) (xy 0 3.175)) (stroke (width 0.254) (type default)) (fill (type none)))
				(polyline (pts (xy 0 3.175) (xy 0 1.905) (xy -3.302 1.905)) (stroke (width 0.254) (type default)) (fill (type none)))
				(rectangle (start 0 -1.27) (end -2.54 -1.905) (stroke (width 0) (type default)) (fill (type outline)))
				(polyline (pts (xy -2.54 -1.27) (xy -3.81 0) (xy -2.54 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
			)
			(symbol "Barrel_Jack_1_1"
				(pin passive line (at 6.35 2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 6.35 -2.54 180) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "USB_A": '''(symbol "{prefix}:USB_A"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_A" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB Type-A Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB_A_0_1"
				(rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB_A_1_1"
				(pin power_out line (at 7.62 2.54 180) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 0 180) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 7.62 -2.54 180) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "USB_C": '''(symbol "{prefix}:USB_C"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Value" "USB_C" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "USB Type-C Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "USB_C_0_1"
				(rectangle (start -7.62 10.16) (end 7.62 -10.16) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "USB_C_1_1"
				(pin power_out line (at 10.16 7.62 180) (length 2.54) (name "VBUS" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 5.08 180) (length 2.54) (name "CC1" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 2.54 180) (length 2.54) (name "CC2" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "D+" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "D-" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -5.08 180) (length 2.54) (name "SBU1" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -7.62 180) (length 2.54) (name "SBU2" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -12.7 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "RJ45_Magjack": '''(symbol "{prefix}:RJ45_Magjack"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "RJ45_Magjack" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "RJ45 with Integrated Magnetics" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "RJ45_Magjack_0_1"
				(rectangle (start -7.62 12.7) (end 7.62 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "RJ45_Magjack_1_1"
				(pin bidirectional line (at -10.16 10.16 0) (length 2.54) (name "TX+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 7.62 0) (length 2.54) (name "TX-" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "RX+" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "RX-" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 0 0) (length 2.54) (name "BI_D1+" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "BI_D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "BI_D2+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -7.62 0) (length 2.54) (name "BI_D2-" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 5.08 180) (length 2.54) (name "LED_G+" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 2.54 180) (length 2.54) (name "LED_G-" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 -2.54 180) (length 2.54) (name "LED_Y+" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin output line (at 10.16 -5.08 180) (length 2.54) (name "LED_Y-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 0 -15.24 90) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "HDMI_A": '''(symbol "{prefix}:HDMI_A"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
			(property "Value" "HDMI_A" (at 0 -22.86 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "HDMI Type-A Connector" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "HDMI_A_0_1"
				(rectangle (start -7.62 20.32) (end 7.62 -20.32) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "HDMI_A_1_1"
				(pin bidirectional line (at -10.16 17.78 0) (length 2.54) (name "D2+" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 15.24 0) (length 2.54) (name "D2_SH" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 12.7 0) (length 2.54) (name "D2-" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 10.16 0) (length 2.54) (name "D1+" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 7.62 0) (length 2.54) (name "D1_SH" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 5.08 0) (length 2.54) (name "D1-" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 2.54 0) (length 2.54) (name "D0+" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 0 0) (length 2.54) (name "D0_SH" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -2.54 0) (length 2.54) (name "D0-" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -5.08 0) (length 2.54) (name "CLK+" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at -10.16 -7.62 0) (length 2.54) (name "CLK_SH" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at -10.16 -10.16 0) (length 2.54) (name "CLK-" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 10.16 180) (length 2.54) (name "CEC" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin no_connect line (at 10.16 5.08 180) (length 2.54) (name "NC" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 0 180) (length 2.54) (name "SCL" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin bidirectional line (at 10.16 -2.54 180) (length 2.54) (name "SDA" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin power_in line (at 10.16 -7.62 180) (length 2.54) (name "GND" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin power_out line (at 10.16 -12.7 180) (length 2.54) (name "+5V" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin input line (at 10.16 -17.78 180) (length 2.54) (name "HPD" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "Conn_2x10": '''(symbol "{prefix}:Conn_2x10"
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "J" (at 0 15.24 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_2x10" (at 0 -15.24 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "2x10 Pin Header" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "Conn_2x10_0_1"
				(rectangle (start -5.08 12.7) (end 5.08 -12.7) (stroke (width 0.254) (type default)) (fill (type background)))
			)
			(symbol "Conn_2x10_1_1"
				(pin passive line (at -7.62 10.16 0) (length 2.54) (name "1" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 10.16 180) (length 2.54) (name "2" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 7.62 0) (length 2.54) (name "3" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 7.62 180) (length 2.54) (name "4" (effects (font (size 1.016 1.016)))) (number "4" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 5.08 0) (length 2.54) (name "5" (effects (font (size 1.016 1.016)))) (number "5" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 5.08 180) (length 2.54) (name "6" (effects (font (size 1.016 1.016)))) (number "6" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 2.54 0) (length 2.54) (name "7" (effects (font (size 1.016 1.016)))) (number "7" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 2.54 180) (length 2.54) (name "8" (effects (font (size 1.016 1.016)))) (number "8" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 0 0) (length 2.54) (name "9" (effects (font (size 1.016 1.016)))) (number "9" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 0 180) (length 2.54) (name "10" (effects (font (size 1.016 1.016)))) (number "10" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -2.54 0) (length 2.54) (name "11" (effects (font (size 1.016 1.016)))) (number "11" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -2.54 180) (length 2.54) (name "12" (effects (font (size 1.016 1.016)))) (number "12" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -5.08 0) (length 2.54) (name "13" (effects (font (size 1.016 1.016)))) (number "13" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -5.08 180) (length 2.54) (name "14" (effects (font (size 1.016 1.016)))) (number "14" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -7.62 0) (length 2.54) (name "15" (effects (font (size 1.016 1.016)))) (number "15" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -7.62 180) (length 2.54) (name "16" (effects (font (size 1.016 1.016)))) (number "16" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -10.16 0) (length 2.54) (name "17" (effects (font (size 1.016 1.016)))) (number "17" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -10.16 180) (length 2.54) (name "18" (effects (font (size 1.016 1.016)))) (number "18" (effects (font (size 1.016 1.016)))))
				(pin passive line (at -7.62 -12.7 0) (length 2.54) (name "19" (effects (font (size 1.016 1.016)))) (number "19" (effects (font (size 1.016 1.016)))))
				(pin passive line (at 7.62 -12.7 180) (length 2.54) (name "20" (effects (font (size 1.016 1.016)))) (number "20" (effects (font (size 1.016 1.016)))))
			)
		)''',

    "SW_Push": '''(symbol "{prefix}:SW_Push"
			(pin_numbers hide)
			(pin_names (offset 1.016) hide)
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "SW" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "SW_Push" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Push Button" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "SW_Push_0_1"
				(circle (center -2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
				(circle (center 2.032 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy 0 1.27) (xy 0 2.54)) (stroke (width 0) (type default)) (fill (type none)))
				(polyline (pts (xy -2.54 1.27) (xy 2.54 1.27)) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "SW_Push_1_1"
				(pin passive line (at -5.08 0 0) (length 2.54) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 0 180) (length 2.54) (name "2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)''',

    "TestPoint": '''(symbol "{prefix}:TestPoint"
			(pin_numbers hide)
			(pin_names (offset 0.762) hide)
			(exclude_from_sim no)
			(in_bom no)
			(on_board yes)
			(property "Reference" "TP" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Value" "TestPoint" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Datasheet" "" (at 5.08 0 0) (effects (font (size 1.27 1.27)) hide))
			(property "Description" "Test Point" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
			(symbol "TestPoint_0_1"
				(circle (center 0 1.524) (radius 0.762) (stroke (width 0) (type default)) (fill (type none)))
			)
			(symbol "TestPoint_1_1"
				(pin passive line (at 0 0 90) (length 0.762) (name "1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)''',
}


def get_symbol(category: str, name: str, prefix: str) -> str:
    """Get a formatted symbol definition.

    Args:
        category: 'common', 'power', 'ic', or 'connector'
        name: Symbol name (e.g., 'R', 'GND', 'LM2596S-5')
        prefix: Library prefix (e.g., 'fcBoard_Power')

    Returns:
        Formatted symbol definition string
    """
    symbol_dicts = {
        'common': COMMON_SYMBOLS,
        'power': POWER_SYMBOLS,
        'ic': IC_SYMBOLS,
        'connector': CONNECTOR_SYMBOLS,
    }

    symbol_dict = symbol_dicts.get(category)
    if symbol_dict and name in symbol_dict:
        return symbol_dict[name].format(prefix=prefix)

    raise ValueError(f"Symbol '{name}' not found in category '{category}'")
