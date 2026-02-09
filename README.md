# Keeping Time

**"The score is listening."**

*Keeping Time* is a web-native science fiction novel about resonance, sound, and authoritarian control. It explores a world where reality is enforced by a global frequency known as "The Score," and silence is an act of rebellion.

## 📁 Repository Structure

*   **`MANUSCRIPT/`**: The source markdown files for the novel's chapters. This is the single source of truth for the narrative.
## 📁 Repository Structure

*   **`public/`**: The deployment-ready website directory.
    *   **`index.html`**: The complete novel (formerly `PUBLICATION_COMPLETE.html`).
    *   **`portal.html`**: The legacy portal/landing page.
    *   **Assets**: All supplementary lore files and styles.
*   **`MANUSCRIPT/`**: The source markdown files for the novel's chapters. This is the single source of truth for the narrative.
*   **`WEBSITE/`**: Source assets for the web deployment.
*   **`build_publication.ps1`**: PowerShell script to compile `MANUSCRIPT` files into the final HTML output.
*   **`vercel.json`**: Configuration for Vercel deployment.

## 🫀 The Residual Archive (System v2.0)

This project features a diegetic "Second Nervous System" running parallel to the text. It is not just a sidebar; it is a bio-reactive interface that responds to the reader's behavior.

### Key Features
1.  **Resonance Loop (Heartbeat):**
    *   A vertical monitor line pulses at 60 BPM (Resting) or 300 BPM (Stress).
    *   Stress levels increase with scroll velocity. High-speed scrolling "panics" the system.
2.  **Organic Text Emergence:**
    *   Lore fragments do not fade in; they **inhale** (opacity + blur + scale).
    *   Text appears only when the reader **stops scrolling**, rewarding stillness.
3.  **Vertical Palimpsest (Ghosting):**
    *   Old fragments linger as faint "ghosts" behind new text, creating a history of reading.
4.  **Mutation:**
    *   Fragments vary on re-reads. The system randomly selects variant texts for specific triggers.
5.  **Alignment Events:**
    *   Specific narrative moments (e.g., "The Zap", "The Drop") trigger locked, high-intensity visual events in the sidebar.

### How to Experience
*   **Passive:** Read the main text. Let the sidebar pulse in your periphery.
*   **Active:** When the sidebar reacts or "inhales," **hover or click** the line to lock it open and read the hidden data.
*   **Deep Dive:** Inspect the HTML source for hidden comments (`<!-- SYSTEM_BOOT -->`) left by the Author.

## 🛠️ Build Instructions

To rebuild the novel from the source markdown:

```powershell
./build_publication.ps1
```

This script will:
1.  Parse all chapters in `MANUSCRIPT/`.
2.  Inject them into the `PUBLICATION_COMPLETE.html` template.
3.  Apply the latest CSS/JS for the Residual Archive.

## 📱 Mobile Support

The system is fully responsive.
*   **Desktop:** Left-aligned, variable-width sidebar.
*   **Mobile:** Collapses into a glassmorphism "Trigger" in the bottom-left. Tap to access the Archive.

---
*System Status: ONLINE*
*Observer Count: 1*
