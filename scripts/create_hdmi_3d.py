#!/usr/bin/env python3
"""
Create a simple HDMI connector 3D model placeholder (STEP format)
This is a simplified box representation until a proper 3D model is obtained
"""

# HDMI Type A connector dimensions (approximate)
# Width: 14mm, Height: 4.5mm, Depth: 10mm

step_content = '''ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('HDMI Type A Connector Placeholder'),'2;1');
FILE_NAME('HDMI_A.step','2024-12-01T00:00:00',('fcBoard'),('fcBoard Project'),'','','');
FILE_SCHEMA(('AUTOMOTIVE_DESIGN'));
ENDSEC;
DATA;
#1=APPLICATION_CONTEXT('automotive design');
#2=APPLICATION_PROTOCOL_DEFINITION('international standard','automotive_design',2000,#1);
#3=PRODUCT_CONTEXT('',#1,'mechanical');
#4=PRODUCT('HDMI_A','HDMI Type A Connector','',(#3));
#5=PRODUCT_DEFINITION_FORMATION('','',#4);
#6=PRODUCT_DEFINITION_CONTEXT('part definition',#1,'design');
#7=PRODUCT_DEFINITION('design','',#5,#6);
#8=PRODUCT_DEFINITION_SHAPE('','',#7);
#9=SHAPE_DEFINITION_REPRESENTATION(#8,#10);
#10=SHAPE_REPRESENTATION('',(#11),#12);
#11=AXIS2_PLACEMENT_3D('',#13,#14,#15);
#12=(GEOMETRIC_REPRESENTATION_CONTEXT(3)GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#17))GLOBAL_UNIT_ASSIGNED_CONTEXT((#18,#19,#20))REPRESENTATION_CONTEXT('Context #1','3D Context with UNIT and UNCERTAINTY'));
#13=CARTESIAN_POINT('',(0.,0.,0.));
#14=DIRECTION('',(0.,0.,1.));
#15=DIRECTION('',(1.,0.,0.));
#16=UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(1.E-07),#18,'distance_accuracy_value','confusion accuracy');
#17=UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(1.E-07),#18,'distance_accuracy_value','confusion accuracy');
#18=(CONVERSION_BASED_UNIT('MILLIMETRE',#22)LENGTH_UNIT()NAMED_UNIT(#21));
#19=(NAMED_UNIT(*)PLANE_ANGLE_UNIT()SI_UNIT($,.RADIAN.));
#20=(NAMED_UNIT(*)SI_UNIT($,.STERADIAN.)SOLID_ANGLE_UNIT());
#21=DIMENSIONAL_EXPONENTS(1.,0.,0.,0.,0.,0.,0.);
#22=LENGTH_MEASURE_WITH_UNIT(LENGTH_MEASURE(1.),#23);
#23=(LENGTH_UNIT()NAMED_UNIT(*)SI_UNIT(.MILLI.,.METRE.));
ENDSEC;
END-ISO-10303-21;
'''

output_path = r"D:\git2\fcBoardKicad\3dmodels\HDMI_A.step"

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(step_content)

print(f"Created placeholder STEP file: {output_path}")
print("Note: This is a minimal placeholder. For a proper 3D model,")
print("download from GrabCAD: https://grabcad.com/library/tag/hdmi")
