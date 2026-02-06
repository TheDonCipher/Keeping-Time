# OUROBOROS: PUBLICATION CONVERSION GUIDE

Automated conversion tools, including **Pandoc**, are now installed on this system. Please use the following high-fidelity paths for publication conversion:

---

### 1. TO EPUB (Kindle / Apple Books) - *Recommended: Pandoc*

#### Option A: Using Pandoc (Preferred for direct conversion)
- **Step 1**: Open your terminal or command prompt.
- **Step 2**: Navigate to the directory containing your master draft.
- **Step 3**: Run the following command, replacing `VOLUME_1_MASTER_DRAFT.md` with your file name:
  ```bash
  pandoc VOLUME_1_MASTER_DRAFT.md -o VOLUME_1_MASTER_DRAFT.epub --toc --smart --standalone --embed-resources --metadata title="Your Book Title" --metadata author="Your Name" --css=epub.css
  ```
  *(Note: `epub.css` is an optional stylesheet for custom EPUB styling. Ensure it's in the same directory or provide a full path.)*
- **Result**: A clean, reflowable EPUB file ready for distribution.

#### Option B: Using Calibre (For advanced EPUB management and fine-tuning)
- **Step 1**: Download **Calibre** (Free/Open Source) if not already installed.
- **Step 2**: Drag your [VOLUME_1_MASTER_DRAFT.md](file:///c:/Users/Japan/OneDrive/Documents/Books/Keeping%20Time/VOLUME_1_MASTER_DRAFT.md) into Calibre.
- **Step 3**: Click **Convert Books**.
- **Step 4**: Select **EPUB** as the output format.
- **Result**: A lightweight, reflowable file ready for Amazon KDP or Apple Books. Calibre also allows for easy metadata editing, cover management, and further EPUB optimization.

### 2. TO PDF (Professional Book Format) - *Recommended: Browser Print for specific layout*

#### Option A: Using Google Chrome / Microsoft Edge (Preferred for 6x9 inch layout with custom fonts/blocks)
- **File**: Use [PUBLICATION_READY_NOVEL.html](file:///c:/Users/Japan/OneDrive/Documents/Books/Keeping%20Time/PUBLICATION_READY_NOVEL.html)
- **Step 1**: Open the file in **Google Chrome** or **Microsoft Edge**.
- **Step 2**: Press `Ctrl + P` (Print).
- **Step 3**: Set "Destination" to **Save as PDF**.
- **Step 4**: Under "More Settings," ensure **Background Graphics** is checked.
- **Result**: You will have a perfectly formatted 6x9 inch book PDF with custom fonts and system-terminal blocks, preserving the HTML's precise rendering.

#### Option B: Using Pandoc (For standard PDF conversion, requires LaTeX)
- **Step 1**: Ensure you have a LaTeX distribution (like TeX Live or MiKTeX) installed on your system.
- **Step 2**: Open your terminal or command prompt.
- **Step 3**: Navigate to the directory containing your master draft.
- **Step 4**: Run the following command, replacing `VOLUME_1_MASTER_DRAFT.md` with your file name:
  ```bash
  pandoc VOLUME_1_MASTER_DRAFT.md -o VOLUME_1_MASTER_DRAFT.pdf --toc --smart --standalone --pdf-engine=xelatex
  ```
  *(Note: `--pdf-engine=xelatex` is often preferred for better font support. You can also use `--template=eisvogel` or other custom LaTeX templates for specific styling.)*
- **Result**: A standard PDF document generated directly from your Markdown.

### 3. DIRECT PAYMENTS
- Refer to [PAYMENT_CHANNELS.md](file:///c:/Users/Japan/OneDrive/Documents/Books/Keeping%20Time/PAYMENT_CHANNELS.md) to set up your PayPal and Crypto addresses on the new portal dashboard.
