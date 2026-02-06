import re
import os

file_path = r'c:\Users\Japan\OneDrive\Documents\Books\Keeping Time\PUBLICATION_READY_NOVEL.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Preserve the header and styles (already cleaned)
# Split by Chapter 1 start
parts = content.split('<div class="chapter" id="ch1">', 1)
header = parts[0]
body = parts[1]

# 2. Clean the body
# Remove redundant blockquotes
body = body.replace('</blockquote>', '')
body = body.replace('<blockquote>', '<BLOCKQUOTE_TEMP>')

# Fix line gaps and formatting
lines = body.splitlines()
cleaned_lines = []

in_system_block = False

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Chapter Headers
    if line.startswith('## Chapter'):
        chapter_title = line.replace('## ', '').strip()
        cleaned_lines.append(f'</div>\n\n<div class="chapter">')
        cleaned_lines.append(f'    <h3>{chapter_title}</h3>')
        continue

    # Divider residues
    if line == '---':
        continue
        
    # Standard Paragraphs or System Messages
    if '<BLOCKQUOTE_TEMP>' in line:
        msg = line.replace('<BLOCKQUOTE_TEMP>', '').replace('**', '').strip()
        if not in_system_block:
            cleaned_lines.append('    <div class="system-block">')
            in_system_block = True
        cleaned_lines.append(f'        {msg}<br>')
    else:
        if in_system_block:
            # Close system block if we hit a normal paragraph
            # But wait, some system blocks are multi-line.
            # Usually they are grouped.
            # If the next line doesn't have BLOCKQUOTE_TEMP, we'll close it.
            pass
        
        # Heading 4 residues
        if line.startswith('<h4>'):
             cleaned_lines.append(f'    {line}')
             continue
             
        # End chapter residue
        if 'END CHAPTER' in line:
            if in_system_block:
                cleaned_lines.append('    </div>')
                in_system_block = False
            cleaned_lines.append('    <hr>')
            cleaned_lines.append(f'    <p style="text-align: center; font-family: var(--font-display); font-weight: bold; margin-top: 40px; border-top: 1px solid var(--border); padding-top: 20px;">{line.replace("**", "")}</p>')
            continue

        # Normal Paragraph Content
        if line and not line.startswith('<'):
            if in_system_block:
                cleaned_lines.append('    </div>')
                in_system_block = False
            cleaned_lines.append(f'    <p>{line}</p>')
        else:
            cleaned_lines.append(f'    {line}')

# Final pass to merge consecutive system-block lines and fix dropcaps
final_body = ""
current_in_system = False
for line in cleaned_lines:
    if 'system-block' in line:
        if not current_in_system:
            final_body += line + "\n"
            current_in_system = True
    elif '</p>' in line and current_in_system:
        final_body += "    </div>\n" + line + "\n"
        current_in_system = False
    else:
        final_body += line + "\n"

# Recombine
new_content = header + '<div class="chapter" id="ch1">\n' + final_body

# Simple post-processing fixes
new_content = new_content.replace('<p></div></p>', '')
new_content = new_content.replace('</div>\n\n<div class="chapter">', '</div>\n<div class="chapter">')

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Cleanup complete.")
