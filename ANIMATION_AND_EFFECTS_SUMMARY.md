# Keeping Time: Cinematic Engine Summary (Volume One)

This document provides a technical overview of the animations, waveforms, and reactive effects implemented in the `KeepingTime_VolumeOne(Scrollytelling).html` cinematic experience.

## 1. Core Engine Architecture
The experience is powered by a custom **Sticky-Scroll Engine** that decouples user scroll position from narrative progression using a Linear Interpolation (Lerp) system.

*   **Scroll Engine**: Snappy 0.07 lerp factor for smooth text transitions.
*   **Narrative State**: Asynchronous interpolation (0.04 factor) of `Tension` (Volume) and `Coherence` values to drive visual atmosphere.
*   **Dynamic HUD**: A reactive "Neural-Acoustic Interface" showing real-time stats:
    *   **Tension (0.00–1.00)**: Drives glow intensity and waveform amplitude.
    *   **Coherence (1.00–0.00)**: Drives blur, vignette size, and static interference.
    *   **BPM Display**: Scales from 70 BPM (calm) to 160 BPM (critical), matching the protagonist's physiological state.

## 2. Atmospheric & Global Effects
These effects run throughout the volume, shifting dynamically based on the current chapter's "Signal."

*   **Multiphase Waveforms (Layered Canvas)**:
    *   **Sine**: Standard Soundscape physics (Chapters 1–3, 5–7, 15–16).
    *   **Square**: High-fidelity, rigid output characteristic of Hana Chord (Chapter 4).
    *   **Sawtooth**: Aggressive, aperiodic output for Taro's breach (Chapter 10).
    *   **Dropout**: Periodic signal loss and fragmentation (Chapter 8).
    *   **Collapse/Static**: Waveform flattening into white noise (Chapter 9, 17).
*   **Dynamic Vignette**: A radial mask that "closes in" on the text as Coherence drops, simulating sensory overload or blackout.
*   **Ambient Glow**: A central light source that shifts from **Cyan** (#00f3ff) to **Danger Red** (#ff3366) as Tension hits critical levels.
*   **Narrative Fragments**: Sporadic, context-aware "data leaks" in the periphery (e.g., `BOOT_SEQUENCE`, `NEURAL OVERLOAD`, `NULL`) that reflect the current narrative tag.

## 3. Phase-Specific Cinematic Triggers
The engine detects specific `data-tag` attributes within the manuscript to trigger unique visual events.

| Phase | Chapter | Effect | Visual Cue |
| :--- | :--- | :--- | :--- |
| **I** | 02 | **Social Tagging** | [SAFE] / [!!THREAT!!] badges appear in the top-left HUD. |
| **I** | 03 | **Impedance Match** | Amber (#f5a623) vignette shadow and theme shift. |
| **II** | 04 | **Room Rotation** | The entire #stage rotates ±2° during Headmaster Voss's speech. |
| **II** | 05 | **Bass Drop** | A radial ring shockwave expands from the center of the screen. |
| **II** | 07 | **Combat UI** | Red tactical brackets [ ] pulse around active text Focus. |
| **II** | 07 | **Frame-Skipping** | High-frequency horizontal jitter/strobe on sentences. |
| **III** | 10 | **Source Code Reveal**| Hexadecimal characters (0–F) flicker behind the text during the breach. |
| **IV** | 11 | **Wireframe Mode** | The world strips back to a blue vector grid with Mono-font focus. |
| **V** | 17 | **Analog Mode** | HUD and Waveforms are forcefully hidden for the "Silence" finale. |

## 4. Text-Level Animations
*   **Focus Logic**: Active sentences use a 0.9 power sine-curve for opacity and blur, creating a "natural focus" feel while scrolling.
*   **System Scramble**: `.format-system` text undergoes a character-cycling decryption animation upon entry.
*   **Glitch Distortion**: Triggered when **Tension > 0.82** and **Coherence < 0.30**. Uses CSS `clip-path` channel splitting (Cyan/Red) to "tear" the text.
*   **Chromatic Aberration**: Subtle RGB shadow offsets that increase in intensity based on current Volume levels.

## 5. System Events
*   **Chapter Flash**: A high-speed cyan overlay flash (55ms) synchronizes with every chapter header entry.
*   **System Crash**: On the final beat of Chapter 17, the screen fades to 100% black, followed by a delayed red `> SYSTEM_CRASH` terminal message.
