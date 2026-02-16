import re
import os
import html

# Path configuration
MANUSCRIPT_DIR = 'MANUSCRIPT'
SIDEBAR_FILE = 'REPOSITORY/SIDEBAR_LIBRARY.md'
TEMPLATE_FILE = 'PUBLICATION_READY_NOVEL.html'
OUTPUT_FILE = 'public/index.html'

def process_markdown(text):
    # 0. Tooltip Processing [[Term::Description]]
    def replace_tooltip(match):
        term = match.group(1)
        tip = html.escape(match.group(2))
        return f'<span class="tooltip" data-tip="{tip}">{term}</span>'
    
    text = re.sub(r'\[\[(.*?)::(.*?)\]\]', replace_tooltip, text)

    # 1. Horizontal Rules
    text = re.sub(r'(?m)^---[ \t\r]*$', '<hr>', text)

    # 2. Headers
    text = re.sub(r'# KEEPING TIME', '', text)
    text = re.sub(r'(?m)^## (.+?)$', r'<h3>\1</h3>', text)
    text = re.sub(r'(?m)^### (.+?)$', r'<h4>\1</h4>', text)
    
    # 3. Bold/Italic
    text = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', text)

    # 4. System Blocks (**[[> HEADER: MSG]]**)
    def replace_system_block(match):
        content = match.group(1)
        if '::' in content:
            header, msg = content.split('::', 1)
            header = header.replace('[', '').replace(']', '').replace('>', '').strip()
            return f'<div class="system-block"><p><strong>{header}</strong><br>{msg}</p></div>'
        return f'<div class="system-block"><p>{content}</p></div>'

    text = re.sub(r'(?m)^\*\*\[\[(>.*?)\]\]\*\*\r?$', replace_system_block, text)

    # 5. Paragraphs
    lines = text.splitlines()
    processed_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            processed_lines.append('')
            continue
        
        if re.match(r'<(h3|h4|hr|div|p|header|aside)', stripped):
            processed_lines.append(line)
        else:
            processed_lines.append(f'<p>{line}</p>')
    
    return '\n'.join(processed_lines)

def get_sidebar_html():
    if not os.path.exists(SIDEBAR_FILE):
        return ""
    
    with open(SIDEBAR_FILE, 'r', encoding='utf-8') as f:
        md = f.read()
    
    html_out = re.sub(r'(?m)^### (.+)$', r'<h4>\1</h4>', md)
    html_out = re.sub(r'(?m)^#### (.+)$', r'<h5>\1</h5>', html_out)
    html_out = html_out.replace('---', '<hr>')
    html_out = re.sub(r'> \*\*Usage\*\*.*', '', html_out)
    html_out = re.sub(r'> \*\*Style\*\*.*', '', html_out)
    html_out = html_out.replace('# SIDEBAR LIBRARY: COMMON TERMS', '')
    html_out = html_out.replace('<aside>', '').replace('</aside>', '')
    return html_out

def build():
    print("Starting build...")
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()
    sidebar_html = get_sidebar_html()
    chapter_html_list = []
    for i in range(1, 18):
        ch_file = os.path.join(MANUSCRIPT_DIR, f'chapter_{i:02d}.md')
        if os.path.exists(ch_file):
            print(f"Processing {ch_file}...")
            with open(ch_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            ch_processed = process_markdown(md_content)
            chapter_html_list.append(f'<div class="chapter" id="ch{i}">\n{ch_processed}\n</div>')
    full_chapters = '\n\n'.join(chapter_html_list)
    output = re.sub(r'<!-- NOTE: Full chapter content.*?-->', full_chapters, template, flags=re.DOTALL)
    output = output.replace('<!-- NOTE: Sidebar content goes here -->', sidebar_html)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Build complete: {OUTPUT_FILE}")

if __name__ == "__main__":
    build()
