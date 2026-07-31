import re
import sys

def generate_anchor(text):
    anchor = text.lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor.strip())
    return anchor

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_toc.py <filepath>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    toc_lines = []
    in_code_block = False
    
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            
        if not in_code_block and re.match(r'^#+\s', line):
            match = re.match(r'^(#+)\s+(.*)', line.strip())
            if match:
                level = len(match.group(1))
                text = match.group(2)
                
                if text.lower() == 'mục lục':
                    continue
                    
                anchor = generate_anchor(text)
                indent = '  ' * (level - 1)
                toc_lines.append(f"{indent}- [{text}](#{anchor})")
                
    toc_content = "\n## Outline (Tự động tạo)\n\n" + "\n".join(toc_lines) + "\n\n"
    
    insert_idx = -1
    for i, line in enumerate(lines):
        if line.strip().lower() == '## mục lục' or line.strip().lower() == '# mục lục':
            insert_idx = i + 1
            break
            
    if insert_idx != -1:
        lines.insert(insert_idx, toc_content)
    else:
        # If no TOC found, insert at the beginning after the title
        lines.insert(1 if len(lines) > 0 else 0, toc_content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        
    print(f"Generated TOC with {len(toc_lines)} items.")

if __name__ == "__main__":
    main()
