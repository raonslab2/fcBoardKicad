
import os

def apply_patch():
    sch_file = 'fcBoard_USB.kicad_sch'
    patch_file = 'patch.txt'
    
    with open(sch_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(patch_file, 'r', encoding='utf-8') as f:
        patch_content = f.read()
    
    # Find the last closing parenthesis
    last_paren_index = content.rfind(')')
    
    if last_paren_index == -1:
        print("Error: Could not find closing parenthesis")
        return

    # Insert patch content before the last parenthesis
    # We need to make sure we format it correctly with indentation
    
    # Add some indentation to patch lines
    indented_patch = ""
    for line in patch_content.splitlines():
        indented_patch += "\t" + line + "\n"
        
    new_content = content[:last_paren_index] + indented_patch + content[last_paren_index:]
    
    with open(sch_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully applied patch to {sch_file}")

if __name__ == "__main__":
    apply_patch()


