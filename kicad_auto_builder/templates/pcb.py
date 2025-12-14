"""
PCB Template - KiCad PCB 파일 생성 템플릿 v1.0

최소 PCB 생성:
- Board outline (Edge.Cuts)
- Connector footprint placeholder
- Mounting holes
"""

import uuid
from dataclasses import dataclass
from typing import Optional


@dataclass
class MountingHoleSpec:
    """마운팅 홀 명세."""
    x: float
    y: float
    diameter: float = 3.2  # M3 hole
    pad_diameter: float = 6.0


@dataclass
class ConnectorPlacement:
    """커넥터 배치 명세."""
    ref: str
    x: float
    y: float
    rotation: float = 0.0
    footprint: str = ""  # 풋프린트 이름


class PCBTemplate:
    """KiCad PCB 템플릿 생성기."""

    @staticmethod
    def create_pcb(
        project_name: str,
        board_width: float,
        board_height: float,
        connectors: list[ConnectorPlacement],
        mounting_holes: list[MountingHoleSpec],
        generator_version: str = "1.5",
    ) -> str:
        """최소 PCB 파일을 생성합니다.

        Args:
            project_name: 프로젝트 이름
            board_width: 보드 너비 (mm)
            board_height: 보드 높이 (mm)
            connectors: 커넥터 배치 목록
            mounting_holes: 마운팅 홀 목록
            generator_version: 생성기 버전

        Returns:
            KiCad PCB S-expression 문자열
        """
        pcb_uuid = str(uuid.uuid4())

        # Board outline (Edge.Cuts)
        outline = PCBTemplate._create_board_outline(board_width, board_height)

        # Connector footprints (placeholder)
        footprints = []
        for conn in connectors:
            fp = PCBTemplate._create_connector_placeholder(conn)
            footprints.append(fp)

        # Mounting holes
        holes = []
        for i, hole in enumerate(mounting_holes):
            h = PCBTemplate._create_mounting_hole(hole, i + 1)
            holes.append(h)

        pcb = f'''(kicad_pcb
  (version 20240108)
  (generator "kicad_auto_builder")
  (generator_version "{generator_version}")
  (general
    (thickness 1.6)
    (legacy_teardrops no)
  )
  (paper "A4")
  (title_block
    (title "{project_name}")
    (date "")
    (rev "1.0")
    (company "Auto Generated")
  )
  (layers
    (0 "F.Cu" signal)
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
    (52 "User.3" user)
    (53 "User.4" user)
    (54 "User.5" user)
    (55 "User.6" user)
    (56 "User.7" user)
    (57 "User.8" user)
    (58 "User.9" user)
  )
  (setup
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000000)
      (disableapertmacros no)
      (usegerberextensions no)
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
      (drillshape 1)
      (scaleselection 1)
      (outputdirectory "")
    )
  )
  (net 0 "")
{outline}
{chr(10).join(footprints)}
{chr(10).join(holes)}
)'''

        return pcb

    @staticmethod
    def _create_board_outline(width: float, height: float) -> str:
        """보드 외곽선을 생성합니다 (Edge.Cuts).

        Args:
            width: 보드 너비 (mm)
            height: 보드 높이 (mm)

        Returns:
            Edge.Cuts 라인 S-expression
        """
        # 좌상단 (0, 0) 기준으로 사각형
        lines = []

        # 4개의 선분
        edges = [
            (0, 0, width, 0),        # 상단
            (width, 0, width, height),  # 우측
            (width, height, 0, height),  # 하단
            (0, height, 0, 0),        # 좌측
        ]

        for x1, y1, x2, y2 in edges:
            line_uuid = str(uuid.uuid4())
            line = f'''  (gr_line
    (start {x1:.2f} {y1:.2f})
    (end {x2:.2f} {y2:.2f})
    (stroke (width 0.15) (type solid))
    (layer "Edge.Cuts")
    (uuid "{line_uuid}")
  )'''
            lines.append(line)

        return "\n".join(lines)

    @staticmethod
    def _create_connector_placeholder(conn: ConnectorPlacement) -> str:
        """커넥터 placeholder footprint를 생성합니다.

        Args:
            conn: 커넥터 배치 정보

        Returns:
            Footprint S-expression
        """
        fp_uuid = str(uuid.uuid4())

        # 120핀 커넥터 크기 (대략)
        width = 60.0
        height = 8.0

        footprint = f'''  (footprint "Placeholder:Connector_120pin"
    (layer "F.Cu")
    (uuid "{fp_uuid}")
    (at {conn.x:.2f} {conn.y:.2f} {conn.rotation:.0f})
    (property "Reference" "{conn.ref}"
      (at 0 -{height/2 + 3:.2f} 0)
      (layer "F.SilkS")
      (uuid "{str(uuid.uuid4())}")
      (effects (font (size 1.5 1.5) (thickness 0.3)))
    )
    (property "Value" "SoM_Connector"
      (at 0 {height/2 + 3:.2f} 0)
      (layer "F.Fab")
      (uuid "{str(uuid.uuid4())}")
      (effects (font (size 1.5 1.5) (thickness 0.3)))
    )
    (fp_rect
      (start {-width/2:.2f} {-height/2:.2f})
      (end {width/2:.2f} {height/2:.2f})
      (stroke (width 0.12) (type solid))
      (fill none)
      (layer "F.SilkS")
      (uuid "{str(uuid.uuid4())}")
    )
    (fp_rect
      (start {-width/2 - 1:.2f} {-height/2 - 1:.2f})
      (end {width/2 + 1:.2f} {height/2 + 1:.2f})
      (stroke (width 0.05) (type solid))
      (fill none)
      (layer "F.CrtYd")
      (uuid "{str(uuid.uuid4())}")
    )
  )'''

        return footprint

    @staticmethod
    def _create_mounting_hole(hole: MountingHoleSpec, index: int) -> str:
        """마운팅 홀을 생성합니다.

        Args:
            hole: 마운팅 홀 명세
            index: 홀 번호 (1부터)

        Returns:
            Mounting hole footprint S-expression
        """
        fp_uuid = str(uuid.uuid4())
        pad_uuid = str(uuid.uuid4())

        footprint = f'''  (footprint "MountingHole:MountingHole_{hole.diameter:.1f}mm"
    (layer "F.Cu")
    (uuid "{fp_uuid}")
    (at {hole.x:.2f} {hole.y:.2f})
    (property "Reference" "H{index}"
      (at 0 -{hole.pad_diameter/2 + 2:.2f} 0)
      (layer "F.SilkS")
      (uuid "{str(uuid.uuid4())}")
      (effects (font (size 1 1) (thickness 0.15)))
    )
    (property "Value" "MountingHole"
      (at 0 {hole.pad_diameter/2 + 2:.2f} 0)
      (layer "F.Fab")
      (uuid "{str(uuid.uuid4())}")
      (effects (font (size 1 1) (thickness 0.15)))
    )
    (pad "" np_thru_hole circle
      (at 0 0)
      (size {hole.diameter:.2f} {hole.diameter:.2f})
      (drill {hole.diameter:.2f})
      (layers "*.Cu" "*.Mask")
      (uuid "{pad_uuid}")
    )
    (fp_circle
      (center 0 0)
      (end {hole.pad_diameter/2:.2f} 0)
      (stroke (width 0.12) (type solid))
      (fill none)
      (layer "F.SilkS")
      (uuid "{str(uuid.uuid4())}")
    )
  )'''

        return footprint
