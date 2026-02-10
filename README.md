# Keeping Time

**"The score is listening."**

*Keeping Time* is a web-native science fiction novel about resonance, sound, and authoritarian control. It is designed as a **Full Web Experience**, where the interface itself is a diegetic artifact of the world.

## 📁 Repository Structure

*   **`public/`**: The deployment-ready website.
    *   **`index.html`**: The complete novel experience (The Impulse - Complete Edition).
    *   **`assets/`**: Supplementary lore files, styles, and media.
*   **`MANUSCRIPT/`**: Source markdown files for each chapter (The single source of truth).
*   **`build_publication.ps1`**: PowerShell script to compile `MANUSCRIPT` into the final HTML output.
*   **`PUBLICATION_STRATEGY.md`**: Guide for hosting and marketing the web novel.

## 🫀 The Second Nervous System (SNS)
### Formerly: The Residual Archive (v2.0)

This project features a diegetic "Second Nervous System" running parallel to the text. It is a bio-reactive interface that responds to the reader's behavior, simulating a connection between the 'Reader' and the 'Subject'.

### Key Features
1.  **Resonance Monitor (Heartbeat):**
    *   A vertical monitor line pulses at a dynamic rate based on narrative tension and scroll velocity.
    *   High-speed scrolling "panics" the system (Stress: HIGH), causing visual instability.
2.  **Environmental Intelligence UI:**
    *   **Emotional Load:** A top-right indicator reflecting the psychological weight of the current segment.
    *   **Surveillance Intensity:** A left-edge indicator that reacts when the "Score" is observing.
3.  **Fragment Lifecycle:**
    *   Lore fragments do not simply appear; they **inhale** (opacity + blur + scale).
    *   **States:** *Dormant* (hidden) → *Emerging* (inhaling) → *Coherent* (readable) → *Decay* (fading into the palimpsest).
4.  **Palimpsest Ghosting:**
    *   Old fragments linger as faint "ghosts" behind new text, creating a visual history of your reading path.
5.  **Alignment Events:**
    *   Specific narrative beats trigger "locked" states where the sidebar glows gold and pulses in sync with the story's climax.

### How to Experience
*   **Passive:** Read the main text. Let the SNS pulse in your periphery.
*   **Active:** When the sidebar "inhales," still your scrolling to let the text become *Coherent*.
*   **Deep Dive:** Inspect the HTML source or browser console for hidden `<!-- SYSTEM_BOOT -->` logs and encrypted intercepts.

## 🚀 Publication Strategy

*Keeping Time* uses a **Hybrid 3-Tier Strategy** to preserve the code-driven experience:
1.  **Canonical Home**: Hosted on **Vercel** or **Neocities** for full fidelity (100% JS/CSS support).
2.  **Discovery Hubs**: Distributed on **Itch.io** as a "Web Game" to reach an interactive fiction audience.
3.  **Marketing Funnels**: "Lite" text-only versions on **Royal Road** and **Substack** to drive traffic back to the full experience.

## 🛠️ Build Instructions

To rebuild the novel from the source markdown:

```powershell
./build_publication.ps1
```

This script parses all chapters in `MANUSCRIPT/` and injects them into the `index.html` template, applying the latest SNS logic and styling.

---
*System Status: ONLINE*
*Environmental Intelligence: SYNCED*
