#!/usr/bin/env python3
"""Patch kicad_builder.py to add _patch_som_sheets method."""

import re
from pathlib import Path

def main():
    # Read the file
    builder_path = Path(__file__).parent.parent / "kicad_auto_builder" / "kicad_builder.py"
    content = builder_path.read_text(encoding='utf-8')

    # Check if already patched
    if '_patch_som_sheets' in content:
        print("Already patched!")
        return

    # New _create_main_sheet method with patch support
    new_create_main_sheet = '''    def _create_main_sheet(self) -> Path:
        """메인 시트를 생성합니다 (서브시트 참조 포함).

        v1.7: apply_mode에서는 기존 시트를 보존하고 SoM sheet 블록만 패치 추가.

        Returns:
            생성된 .kicad_sch 파일 경로
        """
        import uuid

        output_path = self.output_dir / f"{self.target_basename}.kicad_sch"

        # v1.7: apply_mode + 기존 파일 존재 시 패치 모드
        if self.apply_mode and output_path.exists():
            return self._patch_som_sheets(output_path)

        # 기존 파일 없으면 새로 생성
        sheet_symbols = []
        x, y = 50.0, 50.0
        for i, conn in enumerate(self.config.som.connectors):
            ref = conn.ref
            filename = f"som_breakout_{ref}.kicad_sch"
            pin_count = len(conn.pins) if conn.pins else 120
            height = max(30.0, pin_count * 0.3)
            width = 40.0
            sheet_uuid = str(uuid.uuid4())
            sheet_symbol = f\'\'\'  (sheet
    (at {x:.2f} {y:.2f})
    (size {width:.2f} {height:.2f})
    (fields_autoplaced yes)
    (stroke (width 0.1524) (type solid))
    (fill (color 0 0 0 0.0000))
    (uuid "{sheet_uuid}")
    (property "Sheetname" "{ref}_Breakout"
      (at {x:.2f} {y - 2:.2f} 0)
      (effects (font (size 1.27 1.27)) (justify left bottom))
    )
    (property "Sheetfile" "{filename}"
      (at {x:.2f} {y + height + 2:.2f} 0)
      (effects (font (size 1.0 1.0)) (justify left top))
    )
  )\'\'\'
            sheet_symbols.append(sheet_symbol)
            x += 60.0
            if (i + 1) % 2 == 0:
                x = 50.0
                y += 80.0

        title_text = f\'\'\'  (text "{self.config.name}\\\\n\\\\nSoM Carrier Board\\\\nConnectors: {len(self.config.som.connectors)}"
    (exclude_from_sim no)
    (at 25.0 25.0 0)
    (effects (font (size 2.0 2.0)) (justify left))
    (uuid "{str(uuid.uuid4())}")
  )\'\'\'

        title_block = self._get_title_block()
        schematic = f\'\'\'(kicad_sch
  (version 20231120)
  (generator "kicad_auto_builder")
  (generator_version "{__version__}")
  (uuid "{str(uuid.uuid4())}")
  (paper "A3")
  (title_block
    (title "{title_block.title}")
    (date "{title_block.date}")
    (rev "{title_block.rev}")
    (company "{title_block.company}")
    (comment 1 "{title_block.comment1}")
    (comment 2 "{title_block.comment2 or \'\'}")
  )
  (lib_symbols
  )
{chr(10).join(sheet_symbols)}
{title_text}
)\'\'\'
        output_path.write_text(schematic, encoding=\'utf-8\')
        return output_path

    def _patch_som_sheets(self, output_path: Path) -> Path:
        """기존 메인 시트에 SoM sheet 블록만 패치 추가합니다 (v1.7).

        기존 시트(Power, USB, Ethernet 등)는 절대 수정/삭제하지 않음.
        """
        import uuid
        content = output_path.read_text(encoding=\'utf-8\')

        sheets_to_add = []
        for conn in self.config.som.connectors:
            filename = f"som_breakout_{conn.ref}.kicad_sch"
            if filename not in content:
                sheets_to_add.append(conn)

        if not sheets_to_add:
            logger.info("  SoM 시트가 이미 모두 존재합니다. 패치 스킵.")
            return output_path

        # 기존 시트들의 최대 Y 좌표 찾기
        sheet_at_pattern = r\'\\(at\\s+([\\d.]+)\\s+([\\d.]+)\\)\'
        matches = re.findall(sheet_at_pattern, content)
        max_y = 200.0
        for match in matches:
            y_val = float(match[1])
            max_y = max(max_y, y_val)

        start_y = max_y + 50.0
        x, y = 100.0, start_y
        new_sheets = []

        for i, conn in enumerate(sheets_to_add):
            ref = conn.ref
            filename = f"som_breakout_{ref}.kicad_sch"
            height = 30.0
            width = 50.8
            sheet_uuid = str(uuid.uuid4())
            sheet_block = f\'\'\'\\t(sheet
\\t\\t(at {x:.2f} {y:.2f})
\\t\\t(size {width:.2f} {height:.2f})
\\t\\t(exclude_from_sim no)
\\t\\t(in_bom yes)
\\t\\t(on_board yes)
\\t\\t(dnp no)
\\t\\t(fields_autoplaced yes)
\\t\\t(stroke
\\t\\t\\t(width 0.1524)
\\t\\t\\t(type solid)
\\t\\t)
\\t\\t(fill
\\t\\t\\t(color 194 224 255 1.0000)
\\t\\t)
\\t\\t(uuid "{sheet_uuid}")
\\t\\t(property "Sheetname" "SoM {ref} Breakout"
\\t\\t\\t(at {x:.2f} {y - 0.7112:.2f} 0)
\\t\\t\\t(effects
\\t\\t\\t\\t(font
\\t\\t\\t\\t\\t(size 1.27 1.27)
\\t\\t\\t\\t)
\\t\\t\\t\\t(justify left bottom)
\\t\\t\\t)
\\t\\t)
\\t\\t(property "Sheetfile" "{filename}"
\\t\\t\\t(at {x:.2f} {y + height + 0.5416:.2f} 0)
\\t\\t\\t(effects
\\t\\t\\t\\t(font
\\t\\t\\t\\t\\t(size 1.27 1.27)
\\t\\t\\t\\t)
\\t\\t\\t\\t(justify left top)
\\t\\t\\t)
\\t\\t)
\\t)\'\'\'
            new_sheets.append(sheet_block)
            x += 60.0
            if (i + 1) % 2 == 0:
                x = 100.0
                y += 50.0

        patch_content = \'\\n\'.join(new_sheets)

        if \'(sheet_instances\' in content:
            content = content.replace(\'(sheet_instances\', patch_content + \'\\n\\t(sheet_instances\')
        elif \'(embedded_fonts\' in content:
            content = content.replace(\'(embedded_fonts\', patch_content + \'\\n\\t(embedded_fonts\')
        else:
            last_paren = content.rfind(\')\')
            if last_paren > 0:
                content = content[:last_paren] + patch_content + \'\\n\' + content[last_paren:]

        output_path.write_text(content, encoding=\'utf-8\')
        logger.info(f"  기존 시트 보존, SoM 시트 {len(new_sheets)}개 패치 추가됨")
        return output_path

'''

    # Find the old method and replace
    old_pattern = r'    def _create_main_sheet\(self\) -> Path:.*?(?=    def _build_som_manifest)'

    new_content = re.sub(old_pattern, new_create_main_sheet, content, flags=re.DOTALL)

    if new_content == content:
        print("ERROR: Pattern not found!")
        return

    # Write back
    builder_path.write_text(new_content, encoding='utf-8')
    print("Successfully patched kicad_builder.py")
    print("Added: _patch_som_sheets method")
    print("Modified: _create_main_sheet to use patch mode in apply_mode")

if __name__ == "__main__":
    main()
