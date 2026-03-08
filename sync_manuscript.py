"""
sync_manuscript.py — Keeping Time Manuscript Sync
===================================================
Extracts narrative prose from KeepingTime_VolumeOne.html
and updates the MANUSCRIPT/chapter_XX.md files.

Usage:
    python sync_manuscript.py              # dry-run (print diff, no write)
    python sync_manuscript.py --apply      # write changes to disk
    python sync_manuscript.py --chapter 6  # sync only chapter 6
    python sync_manuscript.py --apply --chapter 12

What this script does:
  1. Parses KeepingTime_VolumeOne.html, finds each chapter div (data-ch-id)
  2. Converts the HTML prose back to the manuscript's markdown dialect
  3. Compares that output to the existing chapter_XX.md file
  4. Reports what is new / changed, and optionally writes the update

Conversion rules (HTML → Markdown):
  <p data-vol data-coh>CONTENT</p>     → paragraph prose
  <p> with `backtick text`              → system log line  (> `LOG_LINE`)
  <hr>                                  → ---
  <blockquote class="epigraph">         → > quoted epigraph
  <blockquote class="lore-epigraph">   → <aside> lore block (preserved as-is)
  <h3>                                  → ## Chapter heading
  <strong>                              → **text**
  <em>                                  → *text*
  <br>                                  → newline within paragraph
  <span class="tooltip" data-tip="..."> → tooltip text kept, tip appended as footnote
  <!-- HTML comments -->                → dropped
  data-tag="ghost" beats               → preserved in prose, no markdown side-effect
  // [NOTE: ...]                        → preserved inline
"""

import sys
import os
import io
import re
import html
import difflib
import argparse
from pathlib import Path

# Force UTF-8 stdout so em-dashes and other characters in the novel prose
# don't crash on Windows default cp1252 console encoding.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    from bs4 import BeautifulSoup, Tag, NavigableString, Comment
except ImportError:
    print("ERROR: BeautifulSoup4 is required. Run: pip install beautifulsoup4")
    sys.exit(1)

# ──────────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────────
SCRIPT_DIR    = Path(__file__).parent
HTML_SOURCE   = SCRIPT_DIR / "KeepingTime_VolumeOne.html"
MANUSCRIPT    = SCRIPT_DIR / "MANUSCRIPT"

# Map data-ch-id → chapter_XX.md filename + display number
CHAPTER_MAP = {
    "ch1":  ("chapter_01.md", 1,  "Chapter 1: The Zap"),
    "ch2":  ("chapter_02.md", 2,  "Chapter 2: The Assessment"),
    "ch3":  ("chapter_03.md", 3,  "Chapter 3: Modulation"),
    "ch4":  ("chapter_04.md", 4,  "Chapter 4: The Medium"),
    "ch5":  ("chapter_05.md", 5,  "Chapter 5: Sync Check"),
    "ch6":  ("chapter_06.md", 6,  "Chapter 6: The Ground State"),
    "ch7":  ("chapter_07.md", 7,  "Chapter 7: The Rival"),
    "ch8":  ("chapter_08.md", 8,  "Chapter 8: The Sortie"),
    "ch9":  ("chapter_09.md", 9,  "Chapter 9: The Silence"),
    "ch10": ("chapter_10.md", 10, "Chapter 10: The Unmasking"),
    "ch11": ("chapter_11.md", 11, "Chapter 11: The Wire"),
    "ch12": ("chapter_12.md", 12, "Chapter 12: The Audit"),
    "ch13": ("chapter_13.md", 13, "Chapter 13: Reboot"),
    "ch14": ("chapter_14.md", 14, "Chapter 14: The Return"),
    "ch15": ("chapter_15.md", 15, "Chapter 15: The Phantom Mesh"),
    "ch16": ("chapter_16.md", 16, "Chapter 16: Modulation"),
    "ch17": ("chapter_17.md", 17, "Chapter 17: The Underground"),
}

# ──────────────────────────────────────────────────────────────────────────────
# HTML → Markdown conversion
# ──────────────────────────────────────────────────────────────────────────────

def inner_text(tag) -> str:
    """Recursively convert a tag's children to markdown inline text."""
    parts = []
    for child in tag.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif isinstance(child, Tag):
            name = child.name
            if name == "strong":
                parts.append(f"**{inner_text(child)}**")
            elif name == "em":
                parts.append(f"*{inner_text(child)}*")
            elif name == "br":
                parts.append("\n")
            elif name == "span" and "tooltip" in child.get("class", []):
                tip = child.get("data-tip", "")
                text = inner_text(child)
                # Render as: text (tip in parens, italic)
                parts.append(f"{text} *({tip})*" if tip else text)
            elif name == "span":
                parts.append(inner_text(child))
            elif name == "code":
                parts.append(f"`{inner_text(child)}`")
            else:
                parts.append(inner_text(child))
    return "".join(parts)


def is_system_log(text: str) -> bool:
    """True if this paragraph is a system log / console readout."""
    stripped = text.strip()
    # System logs start with backtick or NOTE/ERROR/WARNING style
    return (
        stripped.startswith("`")
        or stripped.startswith("// [NOTE")
        or stripped.startswith("// [")
        or bool(re.match(r"^\[?[A-Z_0-9]{3,}", stripped))
    )


def convert_system_log(text: str) -> str:
    """
    Wrap each line of a system log block as a markdown blockquote.
    Multi-line (via <br>) become multiple > lines.
    """
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    out = []
    for line in lines:
        # Ensure line is wrapped in backticks if it looks like a console log
        # but isn't already a // [NOTE line
        if line.startswith("//"):
            out.append(f"{line}")
        elif not line.startswith("`"):
            out.append(f"> `{line}`")
        else:
            out.append(f"> {line}")
    return "\n".join(out)


def paragraph_to_md(p: Tag) -> str:
    """Convert a single <p> tag to markdown."""
    text = inner_text(p).strip()
    if not text:
        return ""

    # Normalise HTML entities
    text = html.unescape(text)

    # Detect system log paragraphs
    if is_system_log(text):
        return convert_system_log(text)

    # Plain prose — return as-is (may contain *italic*, **bold**, newlines)
    return text


def blockquote_epigraph_to_md(bq: Tag) -> str:
    """Convert <blockquote class="epigraph"> to markdown block-quote."""
    text = inner_text(bq).strip()
    text = html.unescape(text)
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    return "\n".join(f"> {l}" for l in lines)


def lore_epigraph_to_md(bq: Tag) -> str:
    """Convert <blockquote class="lore-epigraph"> to an <aside> block."""
    # Extract the subject heading and observation
    subject_tag  = bq.find("strong")
    subject      = subject_tag.get_text(strip=True) if subject_tag else "LORE"
    source_span  = bq.find("span", class_="lore-source")
    source       = source_span.get_text(strip=True) if source_span else "- Source: In-World Text"

    # Remove source span from the tag temporarily to get the observation text
    obs_parts = []
    for child in bq.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, Tag) and "lore-source" in child.get("class", []):
            continue
        if isinstance(child, Tag) and child.name == "strong":
            continue
        obs_parts.append(inner_text(child) if isinstance(child, Tag) else str(child))

    observation = html.unescape("".join(obs_parts)).strip()
    observation = re.sub(r"\n+", " ", observation).strip()

    return (
        f"<aside>\n"
        f"<details>\n"
        f"<summary><strong>{subject}</strong></summary>\n"
        f"<blockquote>\n"
        f"<strong>Observation:</strong> {observation}\n"
        f"<br><br>\n"
        f"<strong>{source}</strong>\n"
        f"</blockquote>\n"
        f"</details>\n"
        f"</aside>"
    )


def chapter_html_to_md(chapter_div: Tag, ch_title: str) -> str:
    """
    Convert one chapter's HTML <div class="chapter"> into manuscript markdown.
    Returns the full markdown string for that chapter.
    """
    lines = []
    lines.append("# KEEPING TIME")
    lines.append(f"## {ch_title}")
    lines.append("")

    # Walk direct children of the chapter div
    for child in chapter_div.children:
        if isinstance(child, Comment):
            continue
        if isinstance(child, NavigableString):
            s = str(child).strip()
            if s:
                lines.append(s)
            continue

        tag = child
        name = tag.name

        if name == "h3":
            # Chapter heading — already added above
            continue

        elif name == "hr":
            lines.append("")
            lines.append("---")
            lines.append("")

        elif name == "blockquote":
            classes = tag.get("class", [])
            if "epigraph" in classes:
                lines.append(blockquote_epigraph_to_md(tag))
                lines.append("")
            elif "lore-epigraph" in classes:
                lines.append(lore_epigraph_to_md(tag))
                lines.append("")
            else:
                lines.append(blockquote_epigraph_to_md(tag))
                lines.append("")

        elif name == "p":
            md = paragraph_to_md(tag)
            if md:
                lines.append(md)
                lines.append("")

        elif name == "div":
            # Nested divs (shouldn't normally appear in chapter body, but handle gracefully)
            for sub in tag.descendants:
                if isinstance(sub, Tag) and sub.name == "p":
                    md = paragraph_to_md(sub)
                    if md:
                        lines.append(md)
                        lines.append("")

    # Remove trailing blank lines, add a clean ending
    while lines and lines[-1] == "":
        lines.pop()

    lines.append("")  # final newline
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Diff utility
# ──────────────────────────────────────────────────────────────────────────────

CHANGED_MARK = "[CHANGED]"
SAME_MARK    = "[OK]     "
SKIP_MARK    = "[SKIP]   "
WRITE_MARK   = "[WRITE]  "


def show_diff(old: str, new: str, filename: str):
    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)
    diff = list(difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f"MANUSCRIPT/{filename}  (current)",
        tofile=f"MANUSCRIPT/{filename}  (updated)",
        n=3
    ))
    if not diff:
        print(f"  {SAME_MARK}  {filename}")
        return False
    print()
    print("  " + "".join(diff).replace("\n", "\n  "))
    return True


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Sync KeepingTime_VolumeOne.html → MANUSCRIPT chapter_XX.md files")
    p.add_argument("--apply",   action="store_true", help="Write changes to disk (default: dry-run)")
    p.add_argument("--chapter", type=int, default=None,
                   help="Only sync this chapter number (1-17). Default: all chapters.")
    return p.parse_args()


def main():
    # Reconfigure stdout for UTF-8 on Windows, if necessary
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args()

    if not HTML_SOURCE.exists():
        print(f"ERROR: HTML source not found: {HTML_SOURCE}")
        sys.exit(1)
    if not MANUSCRIPT.is_dir():
        print(f"ERROR: MANUSCRIPT directory not found: {MANUSCRIPT}")
        sys.exit(1)

    print(f"{'DRY-RUN' if not args.apply else 'APPLYING CHANGES'} — Reading {HTML_SOURCE.name} ...")
    print()

    soup = BeautifulSoup(HTML_SOURCE.read_text(encoding="utf-8"), "html.parser")

    # Collect all chapter divs from #novel-data
    novel_data = soup.find(id="novel-data")
    if not novel_data:
        print("ERROR: Could not find #novel-data in HTML source.")
        sys.exit(1)

    changed = []
    skipped = []

    # Determine which chapters to process
    target_ids = set(CHAPTER_MAP.keys())
    if args.chapter:
        ch_key = f"ch{args.chapter}"
        if ch_key not in CHAPTER_MAP:
            print(f"ERROR: Chapter {args.chapter} not in CHAPTER_MAP (valid: 1-17)")
            sys.exit(1)
        target_ids = {ch_key}

    for ch_id, (md_filename, ch_num, ch_title) in CHAPTER_MAP.items():
        if ch_id not in target_ids:
            continue

        # Find the chapter wrapper div
        ch_wrapper = novel_data.find("div", attrs={"data-ch-id": ch_id})
        if not ch_wrapper:
            print(f"  {SKIP_MARK}  {md_filename}  -- data-ch-id='{ch_id}' not found in HTML, skipping")
            skipped.append(md_filename)
            continue

        # Find the inner .chapter div
        ch_div = ch_wrapper.find("div", class_="chapter")
        if not ch_div:
            ch_div = ch_wrapper  # fall back to wrapper itself

        # Generate new markdown
        new_md = chapter_html_to_md(ch_div, ch_title)

        # Read existing .md
        md_path = MANUSCRIPT / md_filename
        if md_path.exists():
            old_md = md_path.read_text(encoding='utf-8')
        else:
            old_md = ""
            print(f"  {SKIP_MARK}  {md_filename}  -- file does not exist, will create")

        # Normalise line endings for comparison
        old_md_norm = old_md.replace("\r\n", "\n")
        new_md_norm = new_md.replace("\r\n", "\n")

        if old_md_norm == new_md_norm:
            print(f"  {SAME_MARK}  {md_filename}")
            continue

        print(f"  {CHANGED_MARK}  {md_filename}  -- changes detected:")
        has_diff = show_diff(old_md_norm, new_md_norm, md_filename)

        if has_diff:
            changed.append((md_path, new_md, md_filename))

    # Summary
    print()
    if not changed:
        print("All chapters are up to date.")
        return

    print(f"{'-' * 60}")
    print(f"  {len(changed)} file(s) with changes  |  {len(skipped)} skipped")

    if args.apply:
        for md_path, new_md, filename in changed:
            md_path.write_text(new_md, encoding='utf-8')
            print(f"  {WRITE_MARK}  {filename}")
        print()
        print("Done. Manuscript updated.")
    else:
        print()
        print("  Dry-run complete. To apply changes, run:")
        print("  python sync_manuscript.py --apply")
        if args.chapter:
            print(f"  python sync_manuscript.py --apply --chapter {args.chapter}")


if __name__ == "__main__":
    main()
