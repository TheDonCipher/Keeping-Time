import os
import re

# =============================================================================
# KEEPING TIME: MANUSCRIPT TO HTML SYNC UTILITY v2.0
# =============================================================================
# Updated to support High-Fidelity HUD tags, Asides, and custom metadata.
# =============================================================================

# Configuration
MD_DIR = "MANUSCRIPT"
HTML_FILE = "KeepingTime_VolumeOne.html"
CHAPTER_COUNT = 17

def markdown_to_html(text):
    """Refined conversion for the Keeping Time engine."""
    # Tooltips: [[Text::Hint]] -> <span class="tooltip" data-tip="Hint">Text</span>
    text = re.sub(r'\[\[(.*?)::(.*?)\]\]', r'<span class="tooltip" data-tip="\2">\1</span>', text)
    # Bold: **Text** -> <strong>Text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italics: *Text* -> <em>Text</em>
    text = re.sub(r'\*([^\*]+)\*', r'<em>\1</em>', text)
    # Code/HUD units: `Text` -> <code>Text</code>
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    
    return text

def rebuild_chapter(ch_num, md_content):
    """Reconstructs the <div> structure for a single chapter with better block detection."""
    ch_id = f"ch{ch_num}"
    
    # Extract Title (## Chapter X: Title)
    title = f"Chapter {ch_num}"
    title_match = re.search(r'^## (.*?)$', md_content, re.M)
    if title_match:
        title = title_match.group(1).strip()
    
    html = f'<div class="chapter" id="{ch_id}">\n'
    html += f'<h3>{title}</h3>\n'
    html += '<hr>\n'
    
    # Split into blocks by double newline
    blocks = re.split(r'\n\n+', md_content)
    for block in blocks:
        block = block.strip()
        if not block: continue
        if block.startswith('#'): continue # Skip headers
        
        # Horizontal Rule
        if block == '---':
            html += '<hr>\n'
            continue
            
        # Sub-headers (like [00:00:00] THE ZAP)
        if block.startswith('### '):
            html += f'<h4>{block[4:].strip()}</h4>\n'
            continue
            
        # Handle Aside/Lore blocks (literal HTML)
        if block.startswith('<aside') or block.startswith('<div class="lore'):
            html += f'{block}\n'
            continue

        # Handle Blockquotes (Epigraphs)
        if block.startswith('> '):
            lines = block.split('\n')
            # Clean lines and handle the Source line
            clean_lines = []
            source = ""
            for l in lines:
                l = l.strip()
                if l.startswith('> —'):
                    source = l[2:].strip()
                elif l.startswith('> '):
                    clean_lines.append(l[2:].strip())
            
            content = "<br>".join([markdown_to_html(cl) for cl in clean_lines])
            if source:
                content += f'<span class="lore-source">{markdown_to_html(source)}</span>'
            
            html += f'<blockquote class="lore-epigraph" data-vol="0.1" data-coh="0.95">{content}</blockquote>\n'
            continue

        # HUD / System Tags (Lines starting with > but not necessarily a quote block)
        # Note: If it's a single line like "> BIOMETRIC...", we preserve the >
        is_hud = block.startswith('> ')
        
        # Convert paragraph lines
        lines = block.split('\n')
        inner_html = "<br>".join([markdown_to_html(l.strip()) for l in lines if l.strip()])
        
        if inner_html:
            vol = "0.25"
            coh = "0.8"
            css_class = ""
            
            # Auto-detect HUD blocks for styling
            if is_hud or "<code>" in inner_html:
                vol = "0.1"
                coh = "0.95"
                css_class = ' class="format-system"'
            
            html += f'<p data-vol="{vol}" data-coh="{coh}"{css_class}>{inner_html}</p>\n'
            
    html += '</div>'
    return html

def sync():
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found.")
        return

    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 1. Extract existing signals
    signals = {}
    signal_matches = re.finditer(r'<div data-ch-id="ch(\d+)" data-signal="(.*?)">', html_content)
    for m in signal_matches:
        signals[int(m.group(1))] = m.group(2)

    # 2. Rebuild the entire novel-data block
    new_novel_data = '  <div id="novel-data" hidden>\n'
    
    for ch_num in range(1, CHAPTER_COUNT + 1):
        md_path = os.path.join(MD_DIR, f"chapter_{ch_num:02d}.md")
        if not os.path.exists(md_path):
            print(f"Warning: {md_path} missing. Skipping.")
            continue
            
        print(f"Processing Chapter {ch_num}...")
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        signal = signals.get(ch_num, f"ch{ch_num:02d}_signal")
        new_novel_data += f'<div data-ch-id="ch{ch_num}" data-signal="{signal}">\n'
        new_novel_data += rebuild_chapter(ch_num, md_content)
        new_novel_data += '\n</div>\n'
        
    new_novel_data += '  </div>'

    # 3. Inject new novel-data into the HTML
    novel_data_pattern = re.compile(r'<div id="novel-data" hidden>.*?  </div>', re.S)
    if not novel_data_pattern.search(html_content):
        print("Error: Could not find <div id=\"novel-data\" hidden> in HTML.")
        return
        
    updated_html = novel_data_pattern.sub(new_novel_data, html_content)

    # 4. Save
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print("\nSUCCESS: HTML has been synchronized with the manuscript.")

if __name__ == "__main__":
    sync()
