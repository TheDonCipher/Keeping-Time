# AGENT TASK — Keeping Time: Volume One
## Mobile-First Responsive Pass
### Target: Antigravity / Gemini 3 Flash

---

> **How to read this document**
> Execute the six phases in order. Each is independently testable on device.
> The reading experience — scrollytelling, reactive HUD, audio — must feel
> *native* on a phone, not like a desktop site squeezed onto a small screen.
> The audience is anime watchers. On mobile this means: crisp at every size,
> HUD always visible, audio unlocking without friction, and no element
> getting clipped by a notch or hidden behind a browser chrome bar.

---

## BEFORE YOU START — Element Inventory

Every element that needs responsive treatment is listed below with its
current expected ID or class. Verify each exists before modifying.

```
FIXED ELEMENTS (position: fixed):
  #hud-panel              — Right-side or top HUD with bars + readouts
  #progress-bar           — Bottom or side scrollytell progress bar
  #chapter-flash-overlay  — Full-screen chapter transition flash
  #silence-lock           — Full-screen void overlay (Ch09)
  #ghost-signal-fragment  — Top-left persistent ghost broadcast text
  #fragment-container     — Bottom-right floating system notification fragments

CANVAS ELEMENTS:
  #waveform-canvas        — Background waveform visualiser
  #progress-canvas        — Progress bar waveform

STAGE / LAYOUT:
  #stage                  — Main scrollable reading container
  .chapter-section        — Each of the 17 chapter <section> elements
  .beat-container         — Each paragraph / beat <p> wrapper
  .hud-line               — Individual HUD readout lines (monospace)
  .tension-bar            — The tension bar fill element
  .coherence-bar          — The coherence bar fill element
  .chapter-title          — h3 / chapter header

AUDIO:
  AudioEngine             — The Web Audio API engine class
  #audio-toggle           — The audio on/off button
```

If any ID differs from the above, match your changes to the actual IDs
in the file. Do not rename elements.

---

## PHASE 1 — FOUNDATION
### Target: `<head>`, root CSS variables, global layout

### 1A — Viewport Meta (verify / add if missing)

```html
<!-- Ensure this is the FIRST meta tag in <head>.
     viewport-fit=cover is required for iPhone notch and home bar safe areas.
     user-scalable=no prevents accidental pinch-zoom breaking scroll detection. -->
<meta name="viewport"
      content="width=device-width, initial-scale=1.0,
               viewport-fit=cover, user-scalable=no">

<!-- Theme color matches the HUD background — hides browser chrome on Android -->
<meta name="theme-color" content="#0a0a0c">
```

### 1B — Safe Area CSS Variables

```css
/* ── SAFE AREA INSETS ───────────────────────────────────────────────
   iOS notch, Dynamic Island, Android camera cutout, home indicator bar.
   All fixed elements must respect these. Define once on :root, reference
   everywhere. env() falls back to 0 on desktop. */
:root {
  --safe-top:    env(safe-area-inset-top,    0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left,   0px);
  --safe-right:  env(safe-area-inset-right,  0px);
}
```

### 1C — Fluid Typography

```css
/* ── FLUID TYPE SCALE ───────────────────────────────────────────────
   clamp(min, preferred, max) — scales smoothly between breakpoints.
   No abrupt jumps. Prose should be readable at 320px without zooming.
   HUD readouts use a tighter scale — they are data, not body text. */

:root {
  /* Prose — the novel text */
  --type-body:     clamp(1rem, 2.4vw + 0.5rem, 1.25rem);

  /* HUD monospace readouts */
  --type-hud:      clamp(0.55rem, 1.2vw + 0.3rem, 0.75rem);

  /* Chapter titles */
  --type-title:    clamp(1.1rem, 3vw + 0.5rem, 1.75rem);

  /* System alert / backtick lines */
  --type-system:   clamp(0.65rem, 1.4vw + 0.3rem, 0.85rem);

  /* Ghost signal fragment — always tiny */
  --type-ghost:    clamp(0.5rem, 0.9vw + 0.2rem, 0.65rem);
}

/* Apply fluid type */
body                  { font-size: var(--type-body); }
.hud-line             { font-size: var(--type-hud); }
.chapter-title        { font-size: var(--type-title); }
.system-alert,
code, pre             { font-size: var(--type-system); }
#ghost-signal-fragment { font-size: var(--type-ghost); }
```

### 1D — Root Layout

```css
/* ── ROOT LAYOUT ────────────────────────────────────────────────────
   Three tiers: mobile (<600px), tablet (600–1024px), desktop (>1024px).
   Mobile is the primary design target — desktop is the enhancement. */

html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  /* Prevent horizontal scroll on any screen size */
  overflow-x: hidden;
  /* Smooth momentum scrolling on iOS */
  -webkit-overflow-scrolling: touch;
}

/* Reading column — centered, max-width constrained */
#stage {
  width: 100%;
  max-width: 680px;          /* Comfortable line length on desktop */
  margin: 0 auto;
  /* Padding: top clears HUD bar, bottom clears progress bar + home indicator */
  padding:
    calc(var(--hud-height, 60px) + var(--safe-top) + 1rem)
    clamp(1rem, 4vw, 2.5rem)
    calc(var(--progress-height, 48px) + var(--safe-bottom) + 2rem)
    clamp(1rem, 4vw, 2.5rem);
  box-sizing: border-box;
}

/* Beat containers — full width within the column */
.beat-container {
  width: 100%;
  margin-bottom: clamp(0.6em, 2vw, 1em);
}
```

---

## PHASE 2 — HUD PANEL RESPONSIVE LAYOUT
### Target: `#hud-panel`, all `.hud-line`, tension/coherence bars, readouts

The HUD is Taro's second narrator. On desktop it probably lives on the right
side. On mobile it must move to a fixed bar at the top or bottom — it cannot
eat reading width. The instruments (tension, coherence, drone Hz) must remain
always visible. Nothing in the HUD can be hidden on any screen size.

### 2A — HUD Layout Modes

```css
/* ── HUD — DESKTOP (sidebar) ────────────────────────────────────────
   Right-side panel, fixed, vertical stack of readouts. */
@media (min-width: 1024px) {
  #hud-panel {
    position: fixed;
    top: var(--safe-top);
    right: var(--safe-right);
    width: 180px;
    height: 100dvh; /* dvh = dynamic viewport height — excludes browser chrome */
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    padding: 1.5rem 1rem;
    box-sizing: border-box;
    /* The panel should not compress the reading column */
    /* #stage max-width is already 680px — on large screens there's room */
  }
}

/* ── HUD — TABLET (compact sidebar) ─────────────────────────────────
   Narrower panel. HUD labels hide; only values show. */
@media (min-width: 600px) and (max-width: 1023px) {
  #hud-panel {
    position: fixed;
    top: var(--safe-top);
    right: var(--safe-right);
    width: 120px;
    height: 100dvh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.75rem;
    padding: 1rem 0.75rem;
    box-sizing: border-box;
  }
  /* Hide verbose labels — keep values and bars */
  .hud-label { display: none; }
}

/* ── HUD — MOBILE (top bar) ──────────────────────────────────────────
   Collapses to a horizontal bar pinned to the top of the viewport.
   All instruments remain visible but arranged horizontally.
   Top-pinned (not bottom) so it doesn't compete with the browser
   home indicator or keyboard. */
@media (max-width: 599px) {
  :root { --hud-height: 52px; }

  #hud-panel {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    /* Respect notch / Dynamic Island on iOS */
    padding-top: var(--safe-top);
    height: calc(var(--hud-height) + var(--safe-top));
    z-index: 200;

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    padding-left: calc(var(--safe-left) + 0.75rem);
    padding-right: calc(var(--safe-right) + 0.75rem);
    box-sizing: border-box;

    /* Semi-transparent — prose can scroll behind it */
    background: rgba(10, 10, 12, 0.92);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-bottom: 1px solid rgba(0, 243, 255, 0.08);
  }

  /* Hide labels entirely on mobile — bars and values only */
  .hud-label { display: none; }

  /* Bars stack vertically within their mobile cell */
  .hud-bar-group {
    display: flex;
    flex-direction: column;
    gap: 3px;
    flex: 1;
  }

  /* Bars themselves — thinner on mobile */
  .tension-bar,
  .coherence-bar {
    height: 3px;
    border-radius: 1.5px;
  }

  /* Drone Hz readout — centred */
  #drone-readout {
    flex: 0 0 auto;
    text-align: center;
    min-width: 60px;
  }

  /* BPM readout — right-aligned */
  #bpm-readout {
    flex: 0 0 auto;
    text-align: right;
    min-width: 48px;
  }
}
```

### 2B — Tension and Coherence Bars

```css
/* ── BARS — BASE STYLES (all sizes) ─────────────────────────────────
   Track dimensions adapt. Fill is driven by JS (width/height % of fill).
   On desktop: tall vertical bars. On mobile: short horizontal bars.
   The transition is purely CSS — JS sets the same numeric value either way. */

.tension-bar-track,
.coherence-bar-track {
  border-radius: 2px;
  overflow: hidden;
  background: rgba(255,255,255,0.06);
}

/* Desktop / tablet: bars are vertical */
@media (min-width: 600px) {
  .tension-bar-track  { width: 4px;  height: 120px; }
  .coherence-bar-track { width: 4px; height: 120px; }
  .tension-bar,
  .coherence-bar {
    width: 100%;
    /* JS sets height as percentage string */
    transition: height 0.15s ease;
  }
}

/* Mobile: bars are horizontal, run full width of their cell */
@media (max-width: 599px) {
  .tension-bar-track  { width: 100%; height: 3px; }
  .coherence-bar-track { width: 100%; height: 3px; }
  .tension-bar,
  .coherence-bar {
    height: 100%;
    /* JS sets width as percentage string on mobile */
    transition: width 0.15s ease;
  }
}
```

### 2C — Bar JS Orientation Awareness

```javascript
// The NarrativeState.update() method sets bar fill dimensions.
// On desktop/tablet it sets `element.style.height`.
// On mobile (<600px) it must set `element.style.width` instead.
// Add this helper and call it wherever bars are updated:

function setBarFill(barEl, value) {
  // value: 0.0–1.0 from NarrativeState
  // Automatically uses width on mobile, height on desktop/tablet.
  const pct = Math.round(value * 100) + '%';
  if (window.innerWidth < 600) {
    barEl.style.width  = pct;
    barEl.style.height = '100%';
  } else {
    barEl.style.height = pct;
    barEl.style.width  = '100%';
  }
}

// Also re-apply bar fills on orientation change / resize:
window.addEventListener('resize', () => {
  // Re-trigger the current bar state so fills re-orient
  if (narrativeState) {
    setBarFill(tensionBarEl,   narrativeState.volume);
    setBarFill(coherenceBarEl, narrativeState.coherence);
  }
}, { passive: true });
```

---

## PHASE 3 — CANVAS ELEMENTS
### Target: `#waveform-canvas`, `#progress-canvas`

Canvas elements do not scale automatically. They need explicit resize logic
and devicePixelRatio handling or they will appear blurry on Retina / OLED
screens (most modern phones).

### 3A — Canvas Resize Utility

```javascript
// ── CANVAS RESIZE UTILITY ─────────────────────────────────────────
// Call this on init AND on every window resize / orientation change.
// devicePixelRatio handles Retina (2x) and high-DPI OLED (3x) displays.
// The canvas logical size (CSS pixels) stays the same; the buffer
// doubles/triples so it renders crisply on high-density screens.

function resizeCanvas(canvas) {
  if (!canvas) return;
  const dpr    = window.devicePixelRatio || 1;
  const rect   = canvas.getBoundingClientRect();

  // Set the buffer size to the physical pixel count
  canvas.width  = Math.round(rect.width  * dpr);
  canvas.height = Math.round(rect.height * dpr);

  // Scale the drawing context so coordinates stay in CSS pixels
  const ctx = canvas.getContext('2d');
  if (ctx) ctx.scale(dpr, dpr);
}

// Call on init
resizeCanvas(document.getElementById('waveform-canvas'));
resizeCanvas(document.getElementById('progress-canvas'));

// Call on resize / orientation change (throttled to 16ms)
let _resizeRAF = null;
window.addEventListener('resize', () => {
  if (_resizeRAF) return;
  _resizeRAF = requestAnimationFrame(() => {
    resizeCanvas(document.getElementById('waveform-canvas'));
    resizeCanvas(document.getElementById('progress-canvas'));
    _resizeRAF = null;
  });
}, { passive: true });

window.addEventListener('orientationchange', () => {
  // orientationchange fires before the new dimensions settle.
  // 300ms delay catches the actual new dimensions.
  setTimeout(() => {
    resizeCanvas(document.getElementById('waveform-canvas'));
    resizeCanvas(document.getElementById('progress-canvas'));
  }, 300);
});
```

### 3B — Waveform Canvas Layout

```css
/* ── WAVEFORM CANVAS — BACKGROUND ───────────────────────────────────
   Full-screen background element. Must cover the viewport completely
   at every size. pointer-events: none so it never blocks touches. */
#waveform-canvas {
  position: fixed;
  inset: 0;                  /* top/right/bottom/left: 0 */
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  /* Canvas renders crisply at any DPI because of Phase 3A resize logic */
}

/* ── PROGRESS CANVAS — BOTTOM BAR ───────────────────────────────────
   Fixed to the bottom, respects home indicator safe area. */
#progress-canvas {
  position: fixed;
  bottom: var(--safe-bottom);
  left: var(--safe-left);
  right: var(--safe-right);
  width: calc(100% - var(--safe-left) - var(--safe-right));
  /* Height: taller on desktop, more compact on mobile */
  height: clamp(28px, 4vh, 48px);
  pointer-events: none;
  z-index: 100;
}
```

### 3C — Progress Canvas Amplitude Scaling

```javascript
// In the waveform draw function, clamp amplitude based on canvas height.
// A 28px-high canvas can't render the same wave height as a 48px-high one.
// This prevents the wave from clipping its own container on mobile.

function drawProgressWave(canvas, waveMode, tension) {
  const rect   = canvas.getBoundingClientRect();
  const height = rect.height;
  const ctx    = canvas.getContext('2d');
  if (!ctx) return;

  // Amplitude: 40% of canvas height maximum, scaled by tension value
  // On a 28px bar: max amplitude = 11px. On a 48px bar: 19px.
  const maxAmp   = height * 0.4;
  const amplitude = maxAmp * Math.min(tension, 1.0);

  // [Rest of waveform drawing logic uses `amplitude` instead of a fixed value]
}
```

---

## PHASE 4 — FIXED OVERLAY ELEMENTS
### Target: `#silence-lock`, `#chapter-flash-overlay`, `#ghost-signal-fragment`, `#fragment-container`

### 4A — Silence Lock Overlay

```css
/* ── SILENCE LOCK ────────────────────────────────────────────────────
   Full-screen void overlay for Ch09. Must cover the entire display
   including notch/home bar areas. Use dvh (dynamic viewport height)
   to avoid being cut off by browser chrome on scroll. */
#silence-lock {
  position: fixed;
  inset: 0;
  /* Extend behind safe areas — this is intentional for the void effect */
  padding: var(--safe-top) var(--safe-right) var(--safe-bottom) var(--safe-left);
  width: 100%;
  height: 100dvh;         /* Dynamic viewport height */
  box-sizing: border-box;
  z-index: 9000;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: clamp(1rem, 3vh, 2rem);

  /* Text inside the silence lock */
  font-size: clamp(0.7rem, 2vw + 0.3rem, 1rem);
  text-align: center;
  padding-left: clamp(1.5rem, 6vw, 4rem);
  padding-right: clamp(1.5rem, 6vw, 4rem);
}
```

### 4B — Chapter Flash Overlay

```css
/* ── CHAPTER FLASH ───────────────────────────────────────────────────
   Must cover the full display including safe areas for impact.
   pointer-events: none so it never interrupts touch scrolling. */
#chapter-flash-overlay {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100dvh;
  pointer-events: none;
  z-index: 9999;
}

/* Ch10 stage shake — respect prefers-reduced-motion.
   Some mobile users have vestibular disorders.
   The shake should NEVER fire if reduced motion is preferred. */
@media (prefers-reduced-motion: reduce) {
  .shake,
  .shake * { animation: none !important; transform: none !important; }

  /* Replace Ch10's shake with a colour pulse instead — same emotional beat,
     no movement. The flash still fires; only the shake is suppressed. */
  .flash-breach { animation: flash-breach-reduced 800ms ease-out forwards; }
  @keyframes flash-breach-reduced {
    0%   { background: rgba(153,51,255,0.55); opacity: 1; }
    100% { background: transparent;           opacity: 0; }
  }
}
```

### 4C — Ghost Signal Fragment Repositioning

```css
/* ── GHOST SIGNAL FRAGMENT ───────────────────────────────────────────
   Desktop: top-left corner (as designed).
   Mobile: repositioned to avoid the HUD top bar and the notch.
   Always in peripheral vision. Never readable. Never interactive. */

#ghost-signal-fragment {
  position: fixed;
  pointer-events: none;
  z-index: 90;
  font-size: var(--type-ghost);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  line-height: 1.8;
  opacity: 0.04;
  transition: opacity 2.5s ease;
  max-width: 140px;
}

/* Desktop / tablet: top-left, below any fixed header */
@media (min-width: 600px) {
  #ghost-signal-fragment {
    top: calc(var(--safe-top) + 80px);
    left: calc(var(--safe-left) + 20px);
  }
}

/* Mobile: pushed down below the HUD top bar */
@media (max-width: 599px) {
  #ghost-signal-fragment {
    /* var(--hud-height) = 52px + safe-top */
    top: calc(var(--safe-top) + var(--hud-height, 52px) + 12px);
    left: calc(var(--safe-left) + 12px);
    /* Slightly smaller on mobile — it's a background element, not a feature */
    max-width: 100px;
  }
}

#ghost-signal-fragment.surfacing {
  opacity: 0.09;
  transition: opacity 0.4s ease;
}
```

### 4D — Fragment Container

```css
/* ── FRAGMENT CONTAINER — Floating system notifications ──────────────
   Desktop: bottom-right corner.
   Mobile: repositioned to avoid the progress bar and home indicator. */

#fragment-container {
  position: fixed;
  z-index: 150;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.4rem;
  pointer-events: none;
}

@media (min-width: 600px) {
  #fragment-container {
    bottom: calc(var(--safe-bottom) + 60px); /* Clear progress bar */
    right:  calc(var(--safe-right) + 20px);
    max-width: 240px;
  }
}

@media (max-width: 599px) {
  #fragment-container {
    /* Clear the progress bar AND the browser home indicator */
    bottom: calc(var(--safe-bottom) + clamp(28px, 4vh, 48px) + 12px);
    right:  calc(var(--safe-right) + 12px);
    /* Narrower on mobile — fragments should be peripheral, not blocking */
    max-width: 160px;
  }

  /* Fragment text — slightly smaller */
  #fragment-container .fragment-item {
    font-size: clamp(0.5rem, 1.1vw + 0.3rem, 0.65rem);
    padding: 3px 6px;
  }
}
```

---

## PHASE 5 — SCROLL ENGINE & TOUCH
### Target: `ScrollEngine`, `AudioEngine.init()`, `#audio-toggle`

### 5A — Touch-Aware Scroll Detection

```javascript
// ── TOUCH SCROLL COMPATIBILITY ───────────────────────────────────────
// The ScrollEngine currently listens to window scroll events.
// On mobile, ensure it uses passive listeners (better performance)
// and reads window.scrollY (not deprecated pageYOffset) for position.

// In ScrollEngine constructor or init():
window.addEventListener('scroll', () => {
  this.tick();
}, { passive: true });
// passive: true is CRITICAL — it tells the browser this handler will
// never call preventDefault(), allowing the browser to scroll
// without waiting for JS. Removes the most common mobile jank source.

// In ScrollEngine.tick(), replace any pageYOffset usage:
const scrollY = window.scrollY; // Standard, non-deprecated
// Also handle the case where the viewport height changes mid-session
// (mobile browser chrome showing/hiding changes 100vh dynamically):
const viewportHeight = window.innerHeight; // Not 100vh CSS — actual current height
```

### 5B — Intersection Observer for Beat Detection (Optional Enhancement)

```javascript
// ── INTERSECTION OBSERVER APPROACH ───────────────────────────────────
// For mobile performance, consider replacing scroll-position math with
// IntersectionObserver. This runs off the main thread and doesn't
// require scroll event firing to detect when beats enter the viewport.
// Add this alongside (not replacing) the existing scroll engine:

const beatObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // This beat is in the reading zone — fire beat-change logic
      const beat = entry.target;
      const vol  = parseFloat(beat.dataset.vol  || '0.25');
      const coh  = parseFloat(beat.dataset.coh  || '0.80');
      const tag  = beat.dataset.tag || null;
      narrativeState.setTarget(vol, coh);
      if (tag) audioEngine._triggerTagAudio(tag);
    }
  });
}, {
  // Trigger when a beat is in the middle third of the viewport.
  // Adjust rootMargin to control reading-position feel on mobile.
  rootMargin: '-35% 0px -35% 0px',
  threshold: 0
});

// Observe every beat container
document.querySelectorAll('.beat-container').forEach(el => {
  beatObserver.observe(el);
});
// This approach is more battery-efficient on mobile than continuous
// scroll position polling.
```

### 5C — AudioContext Mobile Unlock

```javascript
// ── AUDIO UNLOCK — iOS / MOBILE BROWSERS ────────────────────────────
// iOS Safari and some Android browsers require a user gesture before
// AudioContext.resume() is allowed. The engine must not assume the
// context is running — it must wait for the first user interaction.
//
// Implementation: add a global one-time gesture handler that resumes
// the context if it was suspended. This is in addition to the existing
// audio toggle button.

function unlockAudioContext() {
  if (audioEngine && audioEngine.ctx &&
      audioEngine.ctx.state === 'suspended') {
    audioEngine.ctx.resume().then(() => {
      // Context is now running — start the drone if a chapter is active
      if (audioEngine.currentChapterConfig && !audioEngine.ready) {
        audioEngine.init();
      }
    });
  }
  // Remove all unlock listeners once context is running
  ['touchstart', 'touchend', 'mousedown', 'keydown'].forEach(evt => {
    document.removeEventListener(evt, unlockAudioContext);
  });
}

// Register the unlock on any first interaction type
['touchstart', 'touchend', 'mousedown', 'keydown'].forEach(evt => {
  document.addEventListener(evt, unlockAudioContext, { once: true, passive: true });
});
```

### 5D — Audio Toggle Button — Touch Target Size

```css
/* ── AUDIO TOGGLE — TOUCH TARGET ─────────────────────────────────────
   WCAG and Apple HIG both specify minimum 44×44px touch targets.
   The toggle button must meet this on all screen sizes.
   Use padding to expand the hit area without changing visual size. */
#audio-toggle {
  /* Minimum touch target — expand with padding if element is smaller */
  min-width:  44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  /* Prevent double-tap zoom on the button */
  touch-action: manipulation;
  /* Cursor is irrelevant on touch but correct for desktop */
  cursor: pointer;
  /* No tap highlight flash on Android */
  -webkit-tap-highlight-color: transparent;
}

/* On mobile, move the toggle into the HUD bar alongside the readouts */
@media (max-width: 599px) {
  #audio-toggle {
    /* Compact within the 52px HUD bar */
    padding: 0;
    width: 36px;
    height: 36px;
    flex: 0 0 auto;
  }
}
```

---

## PHASE 6 — CHAPTER SECTIONS & PROSE LAYOUT
### Target: `.chapter-section`, `.beat-container`, blockquotes, system alert lines

### 6A — Chapter Sections

```css
/* ── CHAPTER SECTIONS ────────────────────────────────────────────────
   Each section is a narrative zone. Padding gives breathing room.
   On mobile, tighter vertical padding — screen space is limited. */
.chapter-section {
  width: 100%;
  padding-top:    clamp(2rem,  6vh, 5rem);
  padding-bottom: clamp(2rem,  6vh, 5rem);
}

/* Chapter title */
.chapter-title {
  font-size: var(--type-title);
  /* Accent colour set per-chapter by JS (--chapter-accent variable) */
  color: var(--chapter-accent, var(--accent));
  margin-bottom: clamp(1rem, 3vh, 2rem);
  /* Letter-spacing for the anime-UI feel */
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
```

### 6B — System Alert Lines

```css
/* ── SYSTEM ALERT / HUD PROSE LINES ─────────────────────────────────
   Backtick / monospace formatted system lines within the prose.
   On narrow screens they must not overflow horizontally. */
.system-alert,
code, pre,
.hud-prose-block {
  font-size: var(--type-system);
  /* Horizontal scroll if a line is genuinely too long — 
     better than overflowing into the margin */
  overflow-x: auto;
  /* Prevent line-breaks inside long system strings like [WAVEFORM: SINE_PURE] */
  white-space: pre;
  /* Scrollbar styling — thin, matches accent colour */
  scrollbar-width: thin;
  scrollbar-color: var(--accent, #00f3ff) transparent;
  /* Add left padding so content reads distinctly from prose */
  padding-left: clamp(0.75rem, 2vw, 1.5rem);
  border-left: 1px solid rgba(0, 243, 255, 0.15);
  /* On mobile, slightly smaller left padding */
  margin-left: 0;
}

@media (max-width: 599px) {
  .system-alert,
  code, pre,
  .hud-prose-block {
    /* Allow system lines to scroll horizontally rather than wrapping */
    /* This preserves the monospace alignment that is part of the aesthetic */
    max-width: 100%;
    -webkit-overflow-scrolling: touch;
  }
}
```

### 6C — Epigraph / Blockquote

```css
/* ── EPIGRAPH / BLOCKQUOTE ───────────────────────────────────────────
   Lore blocks. Centred on desktop. On mobile: left-aligned with
   indent — centred text on a narrow column is harder to read. */
blockquote {
  font-style: italic;
  opacity: 0.75;
  margin: clamp(1.5rem, 4vh, 3rem) 0;
  padding-left: clamp(1rem, 4vw, 2rem);
  border-left: 2px solid var(--accent, #00f3ff);
}

@media (min-width: 600px) {
  blockquote {
    /* Desktop: wider indent, more spacious */
    padding-left: clamp(1.5rem, 5vw, 3rem);
    padding-right: clamp(1.5rem, 5vw, 3rem);
  }
}
```

### 6D — Prose Line Length Guard

```css
/* ── LINE LENGTH ─────────────────────────────────────────────────────
   Ideal reading line length: 55–75 characters.
   ch unit = width of '0' character in the current font.
   Clamp prevents runaway line length on very wide screens. */
.beat-container p,
.beat-container .prose {
  max-width: 68ch;
  /* On mobile the column is narrower than 68ch anyway — this is a safeguard */
}
```

---

## PHASE 7 — PERFORMANCE & ACCESSIBILITY
### Target: CSS animations, JS loops, `@media` queries

### 7A — Reduced Motion

```css
/* ── PREFERS-REDUCED-MOTION ──────────────────────────────────────────
   Covers users with vestibular disorders AND battery-saving mode on iOS.
   All transitions survive — they just become instant or fade-only. */
@media (prefers-reduced-motion: reduce) {
  /* Transitions: keep opacity/color, remove transform/position */
  * {
    animation-duration:        0.01ms !important;
    animation-iteration-count: 1      !important;
    transition-duration:       0.01ms !important;
    scroll-behavior:           auto   !important;
  }

  /* Exceptions: opacity transitions are kept (not disorienting) */
  #ghost-signal-fragment,
  #chapter-flash-overlay,
  .tension-bar,
  .coherence-bar {
    transition-duration: 150ms !important;
    transition-property: opacity, background-color, width, height !important;
  }

  /* Ch10 shake: replaced with colour pulse in 4B — remove here too */
  .shake { animation: none !important; transform: none !important; }
}
```

### 7B — Canvas Draw Loop — Battery

```javascript
// ── ANIMATION LOOP OPTIMISATION ───────────────────────────────────────
// The waveform canvas draws on every requestAnimationFrame — on mobile
// this is expensive. Two optimisations:

// 1. Pause drawing when the page is not visible (tab switch, lock screen).
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    // Page is backgrounded — stop the animation loop
    if (waveformAnimationId) {
      cancelAnimationFrame(waveformAnimationId);
      waveformAnimationId = null;
    }
    // Also suspend AudioContext to save battery
    if (audioEngine?.ctx?.state === 'running') {
      audioEngine.ctx.suspend();
    }
  } else {
    // Page is visible again — resume
    startWaveformLoop(); // Whatever your loop-start function is called
    if (audioEngine?.ctx?.state === 'suspended') {
      audioEngine.ctx.resume();
    }
  }
});

// 2. Reduce canvas draw frequency on low-power mode.
// Check if the device is low-power via the battery API (where available):
async function checkBatteryMode() {
  if ('getBattery' in navigator) {
    const battery = await navigator.getBattery();
    // If battery < 20% and not charging, halve the draw rate
    if (battery.level < 0.2 && !battery.charging) {
      return 'low-power'; // Caller can set targetFPS = 30 instead of 60
    }
  }
  return 'normal';
}
```

### 7C — HUD Extras on Mobile

```css
/* ── HUD EXTRAS — MOBILE VISIBILITY ────────────────────────────────
   The additional readouts (social_tag, team_link, combat, hull_status etc.)
   that appear per-chapter. On mobile the HUD bar has limited width —
   extras should appear below the main HUD bar as a secondary strip,
   not inside the same row as tension/coherence/drone. */

#hud-extras {
  position: fixed;
  z-index: 199; /* Just below main HUD */
  pointer-events: none;
}

@media (min-width: 600px) {
  #hud-extras {
    /* Desktop/tablet: below the main panel items, same panel */
    /* Usually already in the panel flow — keep as-is */
  }
}

@media (max-width: 599px) {
  #hud-extras {
    /* Appears as a thin secondary strip below the main HUD bar */
    top: calc(var(--safe-top) + var(--hud-height, 52px));
    left: 0;
    right: 0;
    height: auto;
    padding: 2px calc(var(--safe-left) + 0.75rem);
    background: rgba(10, 10, 12, 0.80);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    border-bottom: 1px solid rgba(0, 243, 255, 0.05);

    display: flex;
    flex-wrap: nowrap;
    gap: 0.75rem;
    overflow-x: auto;           /* Horizontal scroll if too many extras */
    scrollbar-width: none;      /* Hide the scrollbar — it's incidental */
  }
  #hud-extras::-webkit-scrollbar { display: none; }

  #hud-extras .hud-extra-item {
    font-size: clamp(0.48rem, 1vw + 0.25rem, 0.6rem);
    white-space: nowrap;
    flex: 0 0 auto;
  }

  /* Update #stage top padding when extras strip is visible */
  /* Add/remove class 'has-hud-extras' on #stage via JS when extras are active */
  #stage.has-hud-extras {
    padding-top: calc(var(--safe-top) + var(--hud-height, 52px) + 24px + 1rem);
  }
}
```

---

## TESTING CHECKLIST

Test on these specific scenarios before considering complete:

**Devices to test:**
- [ ] iPhone SE (375px — the narrowest common phone)
- [ ] iPhone 14 Pro (393px — Dynamic Island notch, tall safe-area)
- [ ] Android mid-range (360–412px typical — no notch, browser chrome visible)
- [ ] iPad portrait (768px — tablet breakpoint boundary)
- [ ] Desktop at 1024px, 1440px, 1920px

**Specific checks:**
- [ ] **HUD always visible** — no element clips behind notch, Dynamic Island, or home bar at any size
- [ ] **No horizontal scroll** — at 320px the page does not overflow horizontally
- [ ] **Prose is readable at 375px** — font is ≥ 16px (prevents iOS auto-zoom on tap)
- [ ] **Audio unlocks on first touch** — tap anywhere on mobile starts the AudioContext
- [ ] **Canvas is sharp on Retina** — waveform is crisp on a 3x OLED screen, not blurry
- [ ] **Canvas resizes on orientation change** — rotate from portrait → landscape, wave redraws correctly
- [ ] **Ch09 silence lock covers full screen** — including notch area on iPhone
- [ ] **Ch10 flash covers full screen** — no white gap at top or bottom
- [ ] **Ghost fragment visible but not covering prose** — top-left, below HUD, small
- [ ] **Fragment notifications don't overlap progress bar** — bottom clearance respected
- [ ] **System alert lines scroll horizontally if long** — they do not wrap or overflow
- [ ] **Touch scrolling is smooth** — no jank (scroll listeners are passive)
- [ ] **Reduced motion preference respected** — Ch10 shake becomes a colour pulse
- [ ] **Page backgrounded → audio suspends** — tab switch, lock screen
- [ ] **Page foregrounded → audio resumes** — returns to correct chapter drone
- [ ] **Final beat visible at 375px** — 'I am bringing the noise' + all HUD values
- [ ] **Audio toggle is tappable at 44×44px minimum** — test on an actual device

---

*// END OF AGENT TASK — KEEPING TIME V1 MOBILE RESPONSIVE PASS*
*// Phases: 7 / Breakpoints: 3 (mobile <600, tablet 600–1024, desktop >1024)*
*// Key mobile risks: AudioContext iOS gesture, canvas DPR, safe-area insets, passive scroll*
*// Anime-watcher priority: HUD always visible, flashes full-bleed, no layout jank*
