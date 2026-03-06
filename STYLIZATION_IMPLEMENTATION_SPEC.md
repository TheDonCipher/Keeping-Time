# KEEPING TIME — STYLIZATION IMPLEMENTATION SPEC
## Version 2.0 | For: Web Developer / AI Code Agent

> **Codebase target:** `KeepingTime_VolumeOne_Scrollytelling_.html` (single-file)
> **Stack:** Vanilla JS, Canvas 2D, CSS custom properties, Web Audio API
> **Implementation order:** Follow priority tiers. Each spec is self-contained
> and references exact existing variable names, function names, and data attributes.

---

## HOW TO READ THIS DOCUMENT

Each spec entry contains:
- **WHAT** — The feature and its narrative purpose
- **WHERE** — Exact hook into the existing codebase
- **HOW** — Copy-paste-ready code
- **PRIORITY** — `P1` (High impact, low effort) → `P3` (High effort, transformative)

---
---

# TIER 1 — WEB AUDIO (Highest narrative ROI)

---

## SPEC 01 — AMBIENT DRONE ENGINE
**Priority: P1 | Effort: Medium | Impact: Transformative**

### WHAT
A barely-audible ambient audio layer that shifts frequency and character based on
the current chapter. Because the story is *about* sound, the absence of sound design
is the single largest missed opportunity in the current build.

Story → Sound mapping:
- Standard C-Order chapters: Low 40Hz drone, warm. Enforced calm.
- High-surveillance chapters (ch02, ch12, ch13): High thin tinnitus-range tone.
- Flux Syndicate / Analog chapters (ch17): Warm static, vinyl crackle character.
- Silence encounter (ch09): Complete audio fadeout. Silence IS the horror.
- Void / Breach (ch10): White noise burst, then dead air.

### WHERE
Hook into `window.onload` after `window.engine.init()`.
Reads from existing `CHAPTER_CONFIG[signal]` — extend that object with `drone` key.
Trigger changes inside `NarrativeState.update(beat)` at line ~1620.

### HOW

**Step 1 — Extend CHAPTER_CONFIG with drone definitions:**
```javascript
// ADD `drone` key to each chapter in CHAPTER_CONFIG object (lines ~1470-1578)
// drone: { type, baseFreq, gain, detune }
// type options: 'sine' | 'sawtooth' | 'noise' | 'silence' | 'crackle'

// Example entries to add:
"ch01_zap":       { ..., drone: { type: 'sine',     baseFreq: 55,  gain: 0.04 } },
"ch02_assessment":{ ..., drone: { type: 'sine',     baseFreq: 880, gain: 0.025, detune: 5 } },
"ch09_silence":   { ..., drone: { type: 'silence',  baseFreq: 0,   gain: 0    } },
"ch10_breach":    { ..., drone: { type: 'sawtooth', baseFreq: 110, gain: 0.06 } },
"ch11_safe_mode": { ..., drone: { type: 'sine',     baseFreq: 220, gain: 0.03 } },
"ch17_underground":{ ..., drone: { type: 'crackle', baseFreq: 60,  gain: 0.05 } },
```

**Step 2 — Add AudioEngine class before `window.onload`:**
```javascript
// ============================================================
// SPEC 01: AMBIENT DRONE ENGINE
// Manages Web Audio API drone layer. Initialised on first user
// interaction (click/scroll) to comply with browser autoplay policy.
// ============================================================
class AudioEngine {
  constructor() {
    this.ctx = null;          // AudioContext - created on first interaction
    this.masterGain = null;   // Master volume node
    this.droneOsc = null;     // Primary oscillator node
    this.droneGain = null;    // Per-drone gain node
    this.noiseNode = null;    // BufferSourceNode for noise/crackle types
    this.currentType = null;  // Track current drone type to avoid restarts
    this.ready = false;       // True after user gesture unlocks AudioContext
  }

  // Call once on first user interaction
  init() {
    if (this.ready) return;
    this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    this.masterGain = this.ctx.createGain();
    this.masterGain.gain.value = 0.7; // Overall ambient volume ceiling
    this.masterGain.connect(this.ctx.destination);
    this.ready = true;
  }

  // Generate white noise buffer for crackle/static types
  _createNoiseBuffer() {
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;
    return buffer;
  }

  // Apply a biquad lowpass to shape noise into crackle character
  _createCrackleFilter() {
    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.value = 800;
    filter.Q.value = 0.5;
    return filter;
  }

  // Main method: called by NarrativeState.update() on chapter change
  setDrone(droneConfig) {
    if (!this.ready || !droneConfig) return;
    if (droneConfig.type === this.currentType) return; // No restart if same type
    this.currentType = droneConfig.type;

    // Gracefully fade out current drone over 2 seconds
    this._fadeOut(() => this._startDrone(droneConfig));
  }

  _fadeOut(callback) {
    if (this.droneGain) {
      this.droneGain.gain.setTargetAtTime(0, this.ctx.currentTime, 0.5);
    }
    setTimeout(() => {
      // Stop and disconnect existing nodes
      if (this.droneOsc) { try { this.droneOsc.stop(); } catch(e){} this.droneOsc = null; }
      if (this.noiseNode) { try { this.noiseNode.stop(); } catch(e){} this.noiseNode = null; }
      if (callback) callback();
    }, 2000);
  }

  _startDrone({ type, baseFreq, gain, detune = 0 }) {
    // 'silence' type: just fade out, don't start new source
    if (type === 'silence') return;

    this.droneGain = this.ctx.createGain();
    this.droneGain.gain.value = 0; // Start silent, fade in
    this.droneGain.connect(this.masterGain);

    if (type === 'crackle' || type === 'noise') {
      // Noise-based source
      this.noiseNode = this.ctx.createBufferSource();
      this.noiseNode.buffer = this._createNoiseBuffer();
      this.noiseNode.loop = true;
      const filter = this._createCrackleFilter();
      this.noiseNode.connect(filter);
      filter.connect(this.droneGain);
      this.noiseNode.start();
    } else {
      // Oscillator-based source (sine | sawtooth)
      this.droneOsc = this.ctx.createOscillator();
      this.droneOsc.type = type;
      this.droneOsc.frequency.value = baseFreq;
      if (detune) this.droneOsc.detune.value = detune * 100; // cents
      this.droneOsc.connect(this.droneGain);
      this.droneOsc.start();
    }

    // Fade in over 3 seconds
    this.droneGain.gain.setTargetAtTime(gain, this.ctx.currentTime, 1.0);
  }
}

const audioEngine = new AudioEngine();
```

**Step 3 — Unlock AudioContext on first interaction:**
```javascript
// ADD inside window.onload, before engine.init():
// Unlock audio on first scroll or click (browser autoplay policy)
const unlockAudio = () => {
  audioEngine.init();
  window.removeEventListener('scroll', unlockAudio);
  window.removeEventListener('click', unlockAudio);
};
window.addEventListener('scroll', unlockAudio, { passive: true, once: true });
window.addEventListener('click', unlockAudio, { once: true });
```

**Step 4 — Call audioEngine.setDrone() inside NarrativeState.update():**
```javascript
// MODIFY NarrativeState.update() at line ~1623 — ADD after accent line:
if (beat.config) {
  this.mode = beat.config.waveMode;
  this.accent = beat.config.accent;
  document.documentElement.style.setProperty('--accent', this.accent);
  if (beat.config.analogMode && !window.analogMode) enterAnalogMode();
  // SPEC 01: Trigger drone change on chapter config change
  if (beat.config.drone) audioEngine.setDrone(beat.config.drone);
}
```

---

## SPEC 02 — SCROLL-LOCKED SILENCE ENCOUNTER
**Priority: P1 | Effort: Low | Impact: Very High**

### WHAT
When the reader enters ch09 (The Silence), the page locks scrolling for 4 seconds.
A Score tag materialises mid-screen. The reader cannot proceed. They are forced to
wait. That enforced helplessness IS the experience of The Silence. This is only
possible in the web medium — use it.

### WHERE
Hook inside `ScrollEngine.tick()` at line ~1689. Detect chapter signal change to
`ch09_silence`. Use a one-shot flag to prevent repeat triggering.

### HOW

**Step 1 — Add CSS for the lock overlay:**
```css
/* SPEC 02: Silence lock screen */
#silence-lock {
  position: fixed; inset: 0; z-index: 5000;
  background: #000;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  opacity: 0; pointer-events: none;
  transition: opacity 0.8s ease;
  font-family: var(--font-mono);
}
#silence-lock.active { opacity: 1; pointer-events: all; }
#silence-lock-text {
  color: var(--danger); font-size: 0.85rem;
  letter-spacing: 0.2em; text-transform: uppercase;
  text-align: center; line-height: 2.5;
}
#silence-lock-bar {
  width: 0; height: 1px; background: var(--danger);
  margin-top: 2rem;
  transition: width 4s linear; /* Matches lock duration */
}
#silence-lock.active #silence-lock-bar { width: 200px; }
```

**Step 2 — Add HTML element (place before closing `</body>`):**
```html
<!-- SPEC 02: Silence lock overlay -->
<div id="silence-lock">
  <div id="silence-lock-text">
    > SIGNAL_LOSS<br>
    > ATTEMPTING_RECOVERY...<br>
    <span style="color: var(--text-dim);">[ SUBJECT IS UNRESPONSIVE ]</span>
  </div>
  <div id="silence-lock-bar"></div>
</div>
```

**Step 3 — Add trigger logic inside ScrollEngine.tick():**
```javascript
// ADD to ScrollEngine.tick() after beat.tag checks (~line 1720):
// SPEC 02: One-shot silence lock — fires once when ch09 is entered
if (beat.signal === 'ch09_silence' && !window.silenceLockFired) {
  window.silenceLockFired = true;
  const lockEl = document.getElementById('silence-lock');
  const barEl = document.getElementById('silence-lock-bar');

  // Disable scroll during lock
  document.body.style.overflow = 'hidden';
  lockEl.classList.add('active');

  // Trigger audio silence (Spec 01 integration)
  audioEngine.setDrone({ type: 'silence', baseFreq: 0, gain: 0 });

  // Trigger bar animation on next frame so CSS transition fires
  requestAnimationFrame(() => { if (barEl) barEl.style.width = '200px'; });

  // Release after 4 seconds
  setTimeout(() => {
    lockEl.classList.remove('active');
    document.body.style.overflow = '';
  }, 4200);
}
```

---
---

# TIER 2 — SCROLLYTELLING & VISUAL SYSTEMS

---

## SPEC 03 — RENDER MODE CSS THEMING PER PHASE
**Priority: P1 | Effort: Low | Impact: High**

### WHAT
The four system render modes (Standard, Hi-Fi, Safe Mode, Void) defined in the lore
currently only affect accent colour via `CHAPTER_CONFIG`. This spec makes them drive
the full visual palette — background, text, wave colour, and filter — so the page
itself changes "render mode" as the story does.

### WHERE
Extend existing `CHAPTER_CONFIG` with `renderMode` key.
Modify `NarrativeState.update()` to apply CSS class to `document.body`.
Add render mode CSS classes.

### HOW

**Step 1 — Define render mode CSS classes:**
```css
/* SPEC 03: Render Mode Palettes
   Applied as body class: body.render-standard | render-hifi | render-safe | render-void */

/* STANDARD (C-Order) — Default. Gold warmth. Marble perfection. */
body.render-standard {
  --bg: #0A0A0C; --text: #EAEAEA; --text-dim: #888888;
  --accent: #c8a84b; --danger: #ff3366;
  --wave-color: rgba(200,168,75,0.08);
  --ui-border: rgba(200,168,75,0.15);
}

/* HI-FI — Overclocked. Too much information. Cyan overload. */
body.render-hifi {
  --bg: #030508; --text: #f0f8ff; --text-dim: #6090b0;
  --accent: #00f3ff; --danger: #ff3366;
  --wave-color: rgba(0,243,255,0.1);
  filter: contrast(1.08) saturate(1.1);
}

/* SAFE MODE (BIOS) — Stripped. Blueprint world. Cold. */
body.render-safe {
  --bg: #02080F; --text: #4488ff; --text-dim: #224488;
  --accent: #4488ff; --danger: #ff4466;
  --wave-color: rgba(68,136,255,0.1);
  --ui-border: rgba(68,136,255,0.2);
}

/* VOID — Render failure. Purple-black checkerboard signature. */
body.render-void {
  --bg: #000000; --text: #c0c0c0; --text-dim: #505050;
  --accent: #7b00d4; --danger: #ff0044;
  --wave-color: rgba(123,0,212,0.15);
}
/* Void adds noise texture via pseudo-element */
body.render-void::before {
  content: '';
  position: fixed; inset: 0; z-index: 0;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  opacity: 0.12;
  animation: voidFlicker 0.08s infinite;
}
@keyframes voidFlicker {
  0%, 100% { opacity: 0.12; }
  50%       { opacity: 0.08; }
}
```

**Step 2 — Add `renderMode` key to CHAPTER_CONFIG:**
```javascript
// Render mode options: 'standard' | 'hifi' | 'safe' | 'void'
// Add to each chapter entry in CHAPTER_CONFIG:
"ch01_zap":          { ..., renderMode: 'hifi'     }, // NAI boot — overloaded
"ch02_assessment":   { ..., renderMode: 'standard' }, // C-Order space
"ch03_modulation":   { ..., renderMode: 'standard' },
"ch04_medium":       { ..., renderMode: 'hifi'     }, // 8K academy
"ch05_sync_check":   { ..., renderMode: 'safe'     }, // Wireframe sandbox
"ch06_ground_state": { ..., renderMode: 'safe'     },
"ch07_rival":        { ..., renderMode: 'hifi'     },
"ch08_sortie":       { ..., renderMode: 'standard' },
"ch09_silence":      { ..., renderMode: 'void'     }, // Silence = render failure
"ch10_breach":       { ..., renderMode: 'void'     }, // Void exposed
"ch11_safe_mode":    { ..., renderMode: 'safe'     }, // BIOS recovery
"ch12_audit":        { ..., renderMode: 'standard' },
"ch13_patch":        { ..., renderMode: 'standard' }, // Compliant. Gold.
"ch14_return":       { ..., renderMode: 'hifi'     }, // Dissonance Vision on
"ch15_phantom_mesh": { ..., renderMode: 'hifi'     },
"ch16_illegal_modulations": { ..., renderMode: 'standard' },
"ch17_underground":  { ..., renderMode: 'void'     }, // Flux. Raw.
```

**Step 3 — Apply class in NarrativeState.update():**
```javascript
// ADD inside the if (beat.config) block in NarrativeState.update():
// SPEC 03: Apply render mode body class on chapter change
if (beat.config.renderMode) {
  const modes = ['render-standard', 'render-hifi', 'render-safe', 'render-void'];
  document.body.classList.remove(...modes);
  document.body.classList.add('render-' + beat.config.renderMode);
}
```

---

## SPEC 04 — WAVEFORM PROGRESS BAR
**Priority: P2 | Effort: Medium | Impact: Medium**

### WHAT
Replace the current thin linear progress bar with an SVG waveform that fills
left-to-right as the reader scrolls. The waveform shape matches the chapter's
current `waveMode` from CHAPTER_CONFIG. Progress becomes diegetic — it IS the
story's waveform completing.

### WHERE
Replace existing `#progress-bar` element and its CSS.
Update the progress calculation inside `ScrollEngine.tick()` at line ~1692.

### HOW

**Step 1 — Replace the progress bar HTML:**
```html
<!-- REPLACE existing: <div id="progress-container"><div id="progress-bar"></div></div> -->
<!-- WITH: -->
<div id="progress-container">
  <svg id="progress-wave" width="100%" height="20" preserveAspectRatio="none"
       style="position:fixed;top:0;left:0;z-index:9999;pointer-events:none;">
    <!-- Clip path defines how much of the wave is revealed (left to right) -->
    <defs>
      <clipPath id="progress-clip">
        <rect id="progress-clip-rect" x="0" y="0" width="0%" height="20"/>
      </clipPath>
    </defs>
    <!-- The waveform path — updated by JS per chapter -->
    <path id="progress-wave-path" clip-path="url(#progress-clip)"
          fill="none" stroke-width="1.5"
          stroke="url(#progress-gradient)"/>
    <defs>
      <linearGradient id="progress-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="var(--accent)"/>
        <stop offset="100%" stop-color="var(--danger)"/>
      </linearGradient>
    </defs>
  </svg>
</div>
```

**Step 2 — CSS for the new element:**
```css
/* SPEC 04: Replace old #progress-bar rules */
#progress-container { position: fixed; top: 0; left: 0; width: 100%; z-index: 9999; }
#progress-wave { overflow: visible; filter: drop-shadow(0 0 3px var(--accent)); }
```

**Step 3 — Add waveform path generator function:**
```javascript
// ADD new function — generates an SVG path string for a given wave type
// Called when chapter changes to redraw the waveform shape
function generateProgressWavePath(waveMode, width, height) {
  const cy = height / 2; // Vertical center
  const amp = 7;         // Wave amplitude in px
  let d = '';

  if (waveMode === 'sine' || waveMode === 'dropout') {
    // Smooth sine — default story mode
    d = `M 0 ${cy}`;
    for (let x = 0; x <= width; x += 4) {
      const y = cy + Math.sin((x / width) * Math.PI * 8) * amp;
      d += ` L ${x} ${y}`;
    }
  } else if (waveMode === 'square' || waveMode === 'flat' || waveMode === 'grid') {
    // Square wave — Hana / C-Order / compliance chapters
    const period = width / 16;
    d = `M 0 ${cy - amp}`;
    for (let i = 0; i < 16; i++) {
      const x1 = i * period; const x2 = x1 + period / 2; const x3 = x1 + period;
      const y = i % 2 === 0 ? cy - amp : cy + amp;
      d += ` H ${x2} V ${cy - y + cy} H ${x3}`;
    }
  } else if (waveMode === 'sawtooth') {
    // Sawtooth — breach, overload, phase IV
    const period = width / 12;
    d = `M 0 ${cy}`;
    for (let i = 0; i < 12; i++) {
      d += ` L ${(i + 1) * period} ${cy - amp} L ${(i + 1) * period} ${cy + amp}`;
    }
  } else if (waveMode === 'collapse' || waveMode === 'wireframe') {
    // Near-flat with jitter — collapse / safe mode
    d = `M 0 ${cy}`;
    for (let x = 0; x <= width; x += 8) {
      const jitter = (Math.random() - 0.5) * 3;
      d += ` L ${x} ${cy + jitter}`;
    }
  } else if (waveMode === 'static') {
    // Noise / static — underground, void
    d = `M 0 ${cy}`;
    for (let x = 0; x <= width; x += 2) {
      const y = cy + (Math.random() - 0.5) * amp * 2;
      d += ` L ${x} ${y}`;
    }
  } else {
    // Fallback: flat line
    d = `M 0 ${cy} H ${width}`;
  }
  return d;
}
```

**Step 4 — Update ScrollEngine.tick() to drive the progress wave:**
```javascript
// MODIFY the progress block inside ScrollEngine.tick() (~line 1692):
// REPLACE: const pb = document.getElementById('progress-bar'); if (pb) pb.style.transform = ...
// WITH:
const progress = Math.min(1, y / (this.totalHeight - window.innerHeight));
const clipRect = document.getElementById('progress-clip-rect');
if (clipRect) clipRect.setAttribute('width', (progress * 100) + '%');

// Regenerate path only on chapter change (not every frame)
if (idx !== this._lastProgressChapter) {
  this._lastProgressChapter = idx;
  const beat = this.data[idx];
  const wavePath = document.getElementById('progress-wave-path');
  if (wavePath && beat?.config?.waveMode) {
    wavePath.setAttribute('d', generateProgressWavePath(
      beat.config.waveMode,
      window.innerWidth,
      20
    ));
  }
}
```

---

## SPEC 05 — SURVEILLANCE CURSOR
**Priority: P2 | Effort: Low | Impact: Medium**

### WHAT
The cursor appearance shifts based on the current chapter's surveillance level
(from existing `NARRATIVE_SIGNALS`). Low surveillance: crosshair. High surveillance:
concentric-circle target. Maximum (ch12 Audit, ch13 Patch): target with rotating
outer ring. Felt subconsciously — exactly how surveillance in the story works.

### WHERE
Read from existing `NARRATIVE_SIGNALS[signal].surveillance` value.
Update via CSS custom cursor on chapter signal change inside `NarrativeState.update()`.

### HOW

**Step 1 — Add SVG cursor generator:**
```javascript
// ADD function before window.onload — generates inline SVG cursor data URI
function buildCursorSVG(surveillanceLevel) {
  // surveillanceLevel: 0.0 (none) to 1.0 (full)

  // Base crosshair (always present)
  const baseColor = surveillanceLevel < 0.5 ? '%2300f3ff' : '%23ff3366';
  const size = 24;
  const cx = size / 2;

  let rings = '';

  if (surveillanceLevel > 0.4) {
    // Inner ring appears at moderate surveillance
    rings += `<circle cx='${cx}' cy='${cx}' r='7' fill='none' stroke='${baseColor}' stroke-width='1' opacity='0.7'/>`;
  }
  if (surveillanceLevel > 0.75) {
    // Outer ring at high surveillance
    rings += `<circle cx='${cx}' cy='${cx}' r='11' fill='none' stroke='${baseColor}' stroke-width='0.5' opacity='0.4'/>`;
  }

  const svg = `
    <svg xmlns='http://www.w3.org/2000/svg' width='${size}' height='${size}' viewBox='0 0 ${size} ${size}'>
      <!-- Crosshair lines -->
      <line x1='${cx}' y1='2' x2='${cx}' y2='9'   stroke='${baseColor}' stroke-width='1.5'/>
      <line x1='${cx}' y1='15' x2='${cx}' y2='22' stroke='${baseColor}' stroke-width='1.5'/>
      <line x1='2'  y1='${cx}' x2='9'  y2='${cx}' stroke='${baseColor}' stroke-width='1.5'/>
      <line x1='15' y1='${cx}' x2='22' y2='${cx}' stroke='${baseColor}' stroke-width='1.5'/>
      <!-- Center dot -->
      <circle cx='${cx}' cy='${cx}' r='1.5' fill='${baseColor}'/>
      ${rings}
    </svg>`;

  return `url("data:image/svg+xml,${svg.trim().replace(/\n\s*/g, ' ')}") ${cx} ${cx}, crosshair`;
}
```

**Step 2 — Apply cursor in NarrativeState.update():**
```javascript
// ADD inside if (beat.config) block in NarrativeState.update():
// SPEC 05: Update cursor based on surveillance level
const survData = NARRATIVE_SIGNALS[beat.signal];
if (survData) {
  document.body.style.cursor = buildCursorSVG(survData.surveillance);
}
```

---

## SPEC 06 — CHAPTER TRANSITION AS SYSTEM REBOOT
**Priority: P2 | Effort: Low | Impact: Medium**

### WHAT
When the reader crosses from one chapter to the next, instead of an instant colour
flash (existing `triggerChapterFlash()`), the page briefly flips to Safe Mode
wireframe aesthetic for 800ms before transitioning to the new chapter's render mode.
Treats navigating chapters as a system process — a render pipeline flush.

### WHERE
Modify existing `triggerChapterFlash()` function (~line 1987).
Use existing `wireframe-mode` CSS class that already exists in the codebase.

### HOW
```javascript
// REPLACE existing triggerChapterFlash() function with:
function triggerChapterFlash() {
  // SPEC 06: Chapter transition = system reboot
  // Phase 1: Flash to wireframe (Safe Mode) for 500ms
  document.body.classList.add('wireframe-mode');

  // Brief flash overlay (kept from original but shorter)
  let o = document.getElementById('f-overlay');
  if (!o) {
    o = document.createElement('div');
    o.id = 'f-overlay';
    Object.assign(o.style, {
      position: 'fixed', top: 0, left: 0,
      width: '100%', height: '100%',
      background: '#4488ff', // Safe mode blue
      opacity: 0, pointerEvents: 'none', zIndex: 900
    });
    document.body.appendChild(o);
  }
  o.style.background = '#4488ff';
  o.style.transition = 'opacity 0.05s ease-in';
  o.style.opacity = 0.3;

  // Phase 2: After 500ms, remove wireframe and fade overlay
  // The new render mode class (Spec 03) will have already been applied by NarrativeState
  setTimeout(() => {
    document.body.classList.remove('wireframe-mode');
    o.style.transition = 'opacity 0.4s ease-out';
    o.style.opacity = 0;
  }, 500);
}
```

---

## SPEC 07 — THREE-LAYER PARALLAX DEPTH
**Priority: P2 | Effort: Medium | Impact: Medium**

### WHAT
The three narrative layers (Score tags / FID prose / plain narration) scroll at
different rates to give cognitive depth to the text layers. Score tags scroll
fractionally AHEAD (they arrive before Taro processes them). FID prose LAGS slightly
(it is Taro's interpretation, always a beat behind the data).

### WHERE
Inside `ScrollEngine._updateSentences()` (~line 1776).
Detect sentence format from `s.format` — 'system' | standard | 'dialogue' | 'thought'.
Apply per-format Y offset multiplier to existing `transform` string.

### HOW
```javascript
// MODIFY inside the el.classList.contains('active') block in _updateSentences()
// ADD after the existing transform calculation, before el.style.transform = transform:

// SPEC 07: Parallax depth by narrative layer
// Score tags (system) scroll ahead — data arrives before processing
// FID prose (thought) scrolls behind — interpretation lags
// Plain narration is baseline
let parallaxOffset = 0;
if (s.format === 'system') {
  // Score leads by up to 8px — information arrives early
  parallaxOffset = -8 * (1 - intensity);
} else if (s.format === 'thought') {
  // FID lags by up to 12px — processing takes time
  parallaxOffset = 12 * (1 - intensity);
}
// Append parallax Y to existing transform
if (parallaxOffset !== 0) {
  transform = transform.replace(
    /translate3d\(([^,]+),([^,]+),/,
    (match, x, y) => `translate3d(${x},${parseFloat(y) + parallaxOffset}px,`
  );
}
```

---
---

# TIER 3 — PROSE & TEXT STYLIZATION

---

## SPEC 08 — TYPOGRAPHIC DISRUPTION BY EMOTIONAL STATE
**Priority: P2 | Effort: Low | Impact: High (prose resonance)**

### WHAT
When Taro reaches State C (overload), the text formatting itself degrades to match
his internal state. Sentence fragments that trail off get reduced opacity. Incomplete
thoughts apply increasing letter-spacing (text is "spreading apart"). When he
stabilises, the typography snaps back. The page becomes sensory evidence of his state.

### WHERE
Read existing `narrativeState.volume` and `narrativeState.coherence`.
Apply CSS classes to `#beat-container` based on thresholds.
Add CSS classes for the typographic states.

### HOW

**Step 1 — Add typographic state CSS:**
```css
/* SPEC 08: Typographic disruption — emotional readout via text rendering */

/* STATE B elevated — slight tracking increase on body text */
#beat-container.state-elevated .sentence:not(.format-system) {
  letter-spacing: 0.01em;
  transition: letter-spacing 0.8s ease;
}

/* STATE C overload — text starts to fragment */
#beat-container.state-overload .sentence:not(.format-system):not(.active) {
  letter-spacing: 0.04em;
  opacity: 0.6;
  transition: letter-spacing 0.4s ease, opacity 0.4s ease;
}
/* Active (focused) sentence remains readable even in overload */
#beat-container.state-overload .sentence.active {
  letter-spacing: 0em;
}

/* VOID state — text barely holds together */
#beat-container.state-void .sentence:not(.active) {
  letter-spacing: 0.08em;
  opacity: 0.35;
  filter: blur(0.5px);
}
#beat-container.state-void .sentence.active {
  letter-spacing: 0.02em;
  opacity: 0.9;
}

/* Incomplete fragment trail — applies to sentences ending in em-dash or ellipsis */
/* Tag these in HTML with data-fmt="fragment" */
.format-fragment {
  opacity: 0.7;
  letter-spacing: 0.06em;
  font-style: italic;
  color: var(--text-dim);
}
.format-fragment::after {
  content: '—';
  opacity: 0.4;
  animation: fragmentPulse 2s infinite;
}
@keyframes fragmentPulse {
  0%, 100% { opacity: 0.4; }
  50%       { opacity: 0.1; }
}
```

**Step 2 — Apply state class in ScrollEngine.tick():**
```javascript
// ADD to ScrollEngine.tick() after narrativeState.update(beat):
// SPEC 08: Apply typographic state class to beat-container
const container = document.getElementById('beat-container');
if (container) {
  const vol = narrativeState.volume;
  const coh = narrativeState.coherence;
  container.classList.remove('state-elevated', 'state-overload', 'state-void');

  if (vol > 0.85 || coh < 0.3) {
    // STATE C or Void: text fragmenting
    container.classList.add(coh < 0.2 ? 'state-void' : 'state-overload');
  } else if (vol > 0.55) {
    // STATE B: elevated processing
    container.classList.add('state-elevated');
  }
  // STATE A / STATE D: no class, clean default typography
}
```

**Step 3 — Mark fragment sentences in prose HTML:**
```html
<!-- USAGE: Add data-fmt="fragment" to sentences that trail off mid-thought -->
<!-- These get the fragment trail CSS treatment -->
<p data-vol="0.88" data-coh="0.22" data-fmt="fragment">
  He started to say something, but the Score was already—
</p>
```

---

## SPEC 09 — IN-WORLD DOCUMENT EPIGRAPHS
**Priority: P2 | Effort: Low | Impact: High (thematic)**

### WHAT
Each chapter gets an optional epigraph written in the cold bureaucratic voice of
the C-Order Compliance Handbook or the Keepers' Handbook. Placed before the first
prose beat. Recontextualises what follows by showing the official version first.
The horror comes from reading the regulation for something the reader has just
experienced as a human being.

### WHERE
Add new `type: 'epigraph'` support to `compileNarrative()`.
Add corresponding CSS styling.
Author epigraphs in the `#novel-data` hidden div using a new element type.

### HOW

**Step 1 — Add epigraph CSS:**
```css
/* SPEC 09: In-world document epigraph styling */
.format-epigraph {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--text-dim);
  border-left: 2px solid var(--text-dim);
  padding: 1rem 1.5rem;
  margin-bottom: 0.5rem;
  line-height: 1.8;
  opacity: 0.75;
  letter-spacing: 0.02em;
}
.format-epigraph .epigraph-source {
  display: block;
  margin-top: 0.75rem;
  font-size: 0.7rem;
  color: var(--accent);
  opacity: 0.6;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
/* Epigraph fades in slower than standard sentences */
.sentence.active.format-epigraph {
  border-left-color: var(--accent);
  opacity: 1;
  transition: opacity 1.2s ease, border-left-color 0.5s ease;
}
```

**Step 2 — Add `<blockquote class="epigraph">` parsing to compileNarrative():**
```javascript
// MODIFY compileNarrative() — ADD support for blockquote elements:
// Inside the container.querySelectorAll(...).forEach() block,
// CHANGE the selector from 'h3, h4, p' to 'h3, h4, p, blockquote':

container.querySelectorAll('h3, h4, p, blockquote').forEach(el => {
  // ... existing code ...
  // ADD new branch for blockquote (epigraph):
  if (el.tagName === 'BLOCKQUOTE') {
    NARRATIVE_DATA.push({
      type: 'standard', vol: 0.1, coh: 0.95, fmt: 'epigraph',
      tag: null, signal, config,
      sentences: [{ text: el.innerHTML, format: 'epigraph' }]
    });
  }
  // ... rest of existing branches ...
});
```

**Step 3 — Example epigraphs to add to each chapter in #novel-data:**
```html
<!-- Chapter 2: The Assessment — add BEFORE the first <p> in ch2 div -->
<blockquote class="epigraph">
  REGULATORY NOTICE: Impedance Mismatch events between bonded citizens are 
  classified as a Class-2 Coherence Deviation. Families are advised to schedule 
  voluntary recalibration within 72 hours of symptom onset. Failure to present 
  for calibration constitutes a Drift Event under Article 9, Section 3 of the 
  Concord Compliance Framework.
  <span class="epigraph-source">— C-Order Compliance Handbook, Vol. IV, §9.3</span>
</blockquote>

<!-- Chapter 10: The Breach -->
<blockquote class="epigraph">
  INCIDENT CLASSIFICATION: Spontaneous Resonance Discharge events above 100% 
  rated output are designated Class-Ω Anomalies. All witnesses are required to 
  submit to mandatory memory indexing within 6 hours. The sector will be 
  repainted within 48 hours. There was no incident.
  <span class="epigraph-source">— G-Vanguard Field Protocol, Directive 7-ZETA</span>
</blockquote>

<!-- Chapter 15: The Phantom Mesh -->
<blockquote class="epigraph">
  NOTICE OF HULL INTEGRITY POLICY: Resonance Dysphoria (colloquially "The Wrong 
  Note") is not a recognized medical condition within the Concord framework. 
  Citizens experiencing Hull Drift are advised to increase damping band usage and 
  submit to standard Error Correction. Unauthorized Modulation of one's base 
  frequency is a Class-1 data corruption offense.
  <span class="epigraph-source">— C-Order Medical Compliance Register, Section 44</span>
</blockquote>
```

---

## SPEC 10 — SECOND-PERSON VOID INTRUSION
**Priority: P3 | Effort: Low | Impact: Very High (singular moment)**

### WHAT
During the Void encounter (ch10, the Breach chapter), the narrator's third-person
voice breaks. For exactly two sentences, the prose shifts to second-person ("you").
The frame ruptures at exactly the moment the world's coherence ruptures.
Used ONCE. Never again. That singularity is its power.

### WHERE
Author in prose HTML using a new `data-fmt="void-break"` attribute.
Add CSS treatment. No JS modification needed.

### HOW

**Step 1 — Add CSS for void-break format:**
```css
/* SPEC 10: Second-person void intrusion — used ONCE in ch10 */
.format-void-break {
  font-family: var(--font-body);
  font-style: italic;
  color: var(--text);
  /* Slightly wider tracking — the voice is not quite in sync */
  letter-spacing: 0.03em;
  /* No left border — this is not tagged data, it has no system label */
  border-left: none !important;
  padding-left: 0 !important;
  /* Subtle but distinct — the prose voice has changed */
  text-indent: 0;
}
/* The sentence before and after the void-break get extra margin for breathing room */
.sentence.format-void-break + .sentence { margin-top: 1rem; }
```

**Step 2 — Author the two void-break sentences in ch10 prose:**
```html
<!-- INSERT in ch10 (The Breach/Unmasking) — place at the peak of the Void exposure
     IMMEDIATELY before "KERNEL_PANIC: REALITY_NOT_FOUND" line -->

<p data-vol="0.95" data-coh="0.05" data-fmt="void-break">
  You don't filter this.
</p>
<p data-vol="0.95" data-coh="0.05" data-fmt="void-break">
  There is nothing to filter.
</p>
```

**Step 3 — Add void-break format detection to compileNarrative():**
```javascript
// Inside compileNarrative(), MODIFY the format detection for 'p' elements:
// ADD 'void-break' to the format detection logic alongside existing checks:
let det = fmt;
if (!det) {
  if (el.innerText.trim().startsWith('>')) det = 'system';
  else if (el.innerText.trim().startsWith('"')) det = 'dialogue';
  // Existing logic continues
}
// The data-fmt="void-break" attribute is already read via `fmt` above.
// No additional change needed — it flows through naturally.
```

---

## SPEC 11 — PALIMPSEST AS ACCUMULATED READING HISTORY
**Priority: P3 | Effort: High | Impact: High (late arc)**

### WHAT
As the reader progresses, every Score tag they've passed leaves a ghost in the
fragment container — faint, past-tense traces of all the data Taro has accumulated.
By Phase III, the sidebar is visibly dense with the reader's own reading history.
At the Void sequence, all ghosts glitch simultaneously. The reader's accumulated
experience of the story becomes visible as trauma on the interface.

### WHERE
Extend `spawnFragment()` to also push to a persistent `PALIMPSEST_POOL` array.
New `renderPalimpsest()` function renders the pool as ghost elements.
Void trigger in `ScrollEngine.tick()` glitches all ghost elements.

### HOW

**Step 1 — Add CSS for palimpsest ghost layer:**
```css
/* SPEC 11: Palimpsest — the accumulated reading history */
#palimpsest-layer {
  position: fixed;
  /* Anchored to left edge — the "memory" sidebar */
  left: 0; top: 0;
  width: 180px; height: 100vh;
  pointer-events: none;
  z-index: 2; /* Below HUD, above wave */
  overflow: hidden;
}
.palimpsest-ghost {
  position: absolute;
  font-family: var(--font-mono);
  font-size: 0.6rem;
  color: var(--accent);
  opacity: 0.06; /* Barely visible — memory, not signal */
  letter-spacing: 0.08em;
  text-transform: uppercase;
  white-space: nowrap;
  pointer-events: none;
  transition: opacity 0.5s ease;
  /* Randomly positioned vertically by JS */
}
/* Void glitch state — all ghosts activate simultaneously */
#palimpsest-layer.void-glitch .palimpsest-ghost {
  opacity: 0.25;
  animation: ghostGlitch 0.15s infinite;
  color: var(--danger);
}
@keyframes ghostGlitch {
  0%   { transform: translateX(0); }
  25%  { transform: translateX(-3px); }
  75%  { transform: translateX(3px); }
  100% { transform: translateX(0); }
}
```

**Step 2 — Add HTML element:**
```html
<!-- ADD after #fragment-container div -->
<div id="palimpsest-layer"></div>
```

**Step 3 — Add palimpsest pool and rendering logic:**
```javascript
// ADD before window.onload:

// SPEC 11: Palimpsest pool — stores up to 40 ghost traces
const PALIMPSEST_POOL = [];
const PALIMPSEST_MAX = 40;

function addToPalimpsest(text) {
  // Only store Score system tags (they are the data Taro accumulates)
  if (!text || !text.trim().startsWith('>')) return;

  PALIMPSEST_POOL.push(text.slice(0, 30)); // Truncate long tags
  if (PALIMPSEST_POOL.length > PALIMPSEST_MAX) PALIMPSEST_POOL.shift();

  renderPalimpsest();
}

function renderPalimpsest() {
  const layer = document.getElementById('palimpsest-layer');
  if (!layer) return;
  layer.innerHTML = ''; // Clear and redraw

  PALIMPSEST_POOL.forEach((text, i) => {
    const ghost = document.createElement('div');
    ghost.className = 'palimpsest-ghost';
    ghost.textContent = text;

    // Distribute vertically — newer entries slightly lower
    const topPct = (i / PALIMPSEST_MAX) * 90 + 5; // 5% to 95%
    ghost.style.top = topPct + '%';

    // Slight horizontal variation for visual texture
    ghost.style.left = (Math.random() * 20) + 'px';

    // Opacity fades with age — newer = slightly more visible
    const ageFactor = i / PALIMPSEST_POOL.length;
    ghost.style.opacity = (0.03 + ageFactor * 0.06).toString();

    layer.appendChild(ghost);
  });
}

// SPEC 11: Void glitch — trigger all ghosts at ch10
function triggerPalimpsestGlitch() {
  const layer = document.getElementById('palimpsest-layer');
  if (!layer) return;
  layer.classList.add('void-glitch');
  setTimeout(() => layer.classList.remove('void-glitch'), 3000);
}
```

**Step 4 — Hook into existing spawnFragment() to capture Score tags:**
```javascript
// MODIFY spawnFragment() — ADD palimpsest logging for system-type beats:
function spawnFragment(tag) {
  const isD = ['pain','override','clip','limiter','overflow','crash','warning'].includes(tag);
  const pool = FRAGMENT_POOL[tag] || FRAGMENT_POOL.default;
  const t = pool[Math.floor(Math.random()*pool.length)];
  const f = document.createElement('div');
  f.className = `narrative-fragment${isD?' danger':''}`;
  f.innerHTML = `<span class="fragment-text">${t}</span>`;
  const c = document.getElementById('fragment-container');
  if (c) { c.appendChild(f); setTimeout(() => f.remove(), 4100); }

  // SPEC 11: Log Score tags to palimpsest
  addToPalimpsest('> ' + t);
}
```

**Step 5 — Trigger void glitch in ScrollEngine.tick():**
```javascript
// ADD inside ScrollEngine.tick() after the silence lock check (Spec 02):
// SPEC 11: Void glitch — fires once when ch10 (Breach) begins
if (beat.signal === 'ch10_breach' && !window.palimpsestGlitchFired) {
  window.palimpsestGlitchFired = true;
  triggerPalimpsestGlitch();
}
```

---
---

# IMPLEMENTATION PRIORITY MATRIX

```
┌─────────────────────────────────────────────┬──────────┬────────┬──────────┐
│ SPEC                                        │ EFFORT   │ IMPACT │ PRIORITY │
├─────────────────────────────────────────────┼──────────┼────────┼──────────┤
│ 01 — Ambient Drone Engine                   │ Medium   │ ★★★★★ │ P1 FIRST │
│ 02 — Scroll-Locked Silence                  │ Low      │ ★★★★★ │ P1 FIRST │
│ 03 — Render Mode CSS Theming                │ Low      │ ★★★★☆ │ P1       │
│ 08 — Typographic Disruption                 │ Low      │ ★★★★☆ │ P1       │
│ 09 — In-World Epigraphs                     │ Low      │ ★★★★☆ │ P1       │
│ 06 — Chapter Reboot Transition              │ Low      │ ★★★☆☆ │ P2       │
│ 05 — Surveillance Cursor                    │ Low      │ ★★★☆☆ │ P2       │
│ 10 — Second-Person Void Intrusion           │ Very Low │ ★★★★★ │ P2       │
│ 07 — Three-Layer Parallax Depth             │ Medium   │ ★★★☆☆ │ P2       │
│ 04 — Waveform Progress Bar                  │ Medium   │ ★★★☆☆ │ P2       │
│ 11 — Palimpsest Reading History             │ High     │ ★★★★☆ │ P3       │
└─────────────────────────────────────────────┴──────────┴────────┴──────────┘

RECOMMENDED IMPLEMENTATION ORDER:
  Session 1: Spec 02 + Spec 03 + Spec 08 (all low-effort, high-impact)
  Session 2: Spec 01 (audio engine — medium effort, transformative)
  Session 3: Spec 09 + Spec 10 (prose additions — author work, minimal code)
  Session 4: Spec 04 + Spec 05 + Spec 06 + Spec 07 (UI polish pass)
  Session 5: Spec 11 (palimpsest — architectural addition)
```

---

## GLOBAL NOTES FOR CODE AGENT

1. **Single-file constraint** — all changes go into the one `.html` file.
   CSS goes inside the `<style>` block. JS goes inside the `<script>` block.
   New HTML elements go immediately before `</body>`.

2. **Never break the ScrollEngine loop** — `_loop()` calls `requestAnimationFrame`
   every frame. Any code added to `tick()` must be O(1) per frame. Heavy operations
   (DOM creation, path generation) must be gated by change-detection flags.

3. **Existing `wireframe-mode` class** — already defined in CSS and toggled by
   `waveMode === 'wireframe'` in tick(). Spec 03 adds render mode classes alongside
   it. They are not mutually exclusive — wireframe-mode overrides on top of render mode.

4. **`window.analogMode`** — existing flag set by `enterAnalogMode()`. When true,
   `drawWaveform()` exits early and the UI layer is hidden. Spec 01's audio engine
   should switch to `crackle` type when this flag is true.

5. **`data-vol` and `data-coh` attributes** — range 0.0–1.0. Already compiled into
   `NARRATIVE_DATA` by `compileNarrative()`. These drive `narrativeState.volume`
   and `narrativeState.coherence` which feed into almost every visual system.
   Use them as the primary emotional signals for Spec 08's typographic states.

6. **Browser compatibility note for Web Audio API** — always create AudioContext
   inside a user gesture handler. The `unlockAudio` pattern in Spec 01 is the
   correct approach. Do NOT create AudioContext at module load time.

---

*Spec compiled from: KeepingTime_VolumeOne_Scrollytelling_.html (2062 lines)*
*Cross-reference: WRITER_GUIDE.md, FID_IMPLEMENTATION_GUIDE_MiniMax.md*
