# KEEPING TIME — Effects Implementation Plan
## Chapters 2–17 | Scrollytelling Experience

> **Basis**: All effects from Ch.1 are already built and working.
> This plan defines *how* they extend, *what's new* per chapter, and the exact
> `data-vol` / `data-coh` tension arc to assign to each beat.
> Follow phases in order — each phase introduces one new system-level effect
> that carries forward into later chapters.

---

## THE CORE SYSTEM (Already Done — Ch.1 Reference)

These run in every chapter without modification:

| Effect | Trigger | Notes |
|---|---|---|
| Scanlines | Always on | Static CSS overlay |
| Waveform (3-layer) | Always on | Driven by `vol` + `coh` |
| Vignette | `coh` < 0.8 | Edges darken as coherence drops |
| Ambient glow | `vol` > 0.2 | Shifts cyan → red at `vol` > 0.75 |
| Chromatic aberration | `vol` > 0.60 | CSS text-shadow split |
| Glitch distortion | `vol` > 0.82 + `coh` < 0.30 | Clip-path channel split |
| Typewriter cursor | `.format-system` active | Blinking `█` |
| Text scramble | `.format-system` on entry | Decrypt noise → real text |
| Chapter flash | `beat.type === 'chapter'` | Cyan shutter wipe |
| Fragments | Interval, keyed to `data-tag` | Rise + fade animation |
| Heartbeat | Every frame | BPM in HUD, bar flash |
| HUD boot | Page load only | Sequential tick-up sequence |

---

## PHASE I — THE IMPULSE (Chapters 1–3)
**Physics**: A high-energy spike enters a stable system.
**UI Theme**: "The Glitch" vs "The System"

---

### Chapter 2: The Assessment
**Signal**: `ch02_assessment` → `emotional_load: 0.50`, `system_pressure: 0.60`, `surveillance: 0.70`
**Event**: Taro interrogated by Voss in the White Room. Voss's "Safe" tag is visually contradicted by Taro's Threat perception.
**Manga Beat**: Voss's eye glitching green for one frame.

#### Tension Arc
```
Arrival in White Room: vol 0.35, coh 0.80
Voss speaks (calm, surgical): vol 0.30, coh 0.85
Social tag conflict begins: vol 0.50, coh 0.65
Voss reveals he knows everything: vol 0.70, coh 0.45
The green eye glitch moment: vol 0.85, coh 0.25 → GLITCH triggers
Taro accepts terms: vol 0.55, coh 0.55
```

#### NEW EFFECT: Social Tag Overlays
Voss is described as having a "Safe" system tag that Taro perceives as wrong.
When Voss's dialogue beats are active, add a persistent **green `[SAFE]` badge**
in the corner of the `#beat-container` that flickers and occasionally corrupts to
`[THREAT]` — driven by `vol` crossing 0.60.

```javascript
// Add to tick() — runs only when currentChapter === 'ch02'
function updateSocialTagDisplay(vol) {
  let badge = document.getElementById('social-tag');
  if (!badge) { /* create fixed badge element */ }

  if (vol > 0.60) {
    // Corrupt the tag at high tension — matches Taro's perception breaking through
    badge.textContent = Math.random() > 0.7 ? '[!!THREAT!!]' : '[SAFE]';
    badge.style.color  = Math.random() > 0.7 ? 'var(--danger)' : 'var(--accent)';
  } else {
    badge.textContent = '[SAFE]';
    badge.style.color = '#00ff88'; // Green — the system's "reassuring" colour
  }
}
```

#### NEW EFFECT: Surveillance Crosshair (Introduce Here)
Surveillance is 0.70 in this chapter — the first time Taro is truly being watched.
This is the **debut chapter** for the surveillance crosshair overlay from the suggestions doc.
Render it at ~30% opacity (not full) — Taro is monitored, not fully exposed yet.

```javascript
// Crosshair opacity formula for ch02:
// opacity = surveillance * 0.35  (lower ceiling than later chapters)
```

#### Fragment Pool (ch02)
```javascript
'ch02': [
  'RECORDING: ACTIVE', 'COMPLIANCE REVIEW', 'THREAT_LEVEL: UNKNOWN',
  'VOSS_ID: ADMIN_GOLD', 'SOCIAL_TAG: [SAFE?]', 'EYE_TRACK: ENGAGED'
]
```

---

### Chapter 3: Modulation
**Signal**: `ch03_modulation` → `emotional_load: 0.40`, `system_pressure: 0.40`, `surveillance: 0.30`
**Event**: Taro says goodbye to Kael (father). "Impedance Mismatch" — the distortion between them.
**Manga Beat**: Kael handing over the Analog Headphones.

#### Tension Arc
```
Arrival home — quiet: vol 0.20, coh 0.90
Conversation starts: vol 0.30, coh 0.82
Impedance Mismatch described: vol 0.42, coh 0.72  ← static between them
Kael hands over headphones: vol 0.38, coh 0.80
Final goodbye: vol 0.45, coh 0.70
```

#### NEW EFFECT: Warm Colour Shift
Ch3 is the emotional counterpoint to Ch1's chaos. This chapter should feel
different — warmer, quieter. Override the cyan `--accent` to `#f5a623` (amber/gold)
for this chapter only, reflecting the Analog Headphones and the warmth of memory.

```javascript
// In renderBeat() or chapter init, when entering ch03:
function applyChapterTheme(chapterSignal) {
  const root = document.documentElement;
  if (chapterSignal === 'ch03_modulation') {
    // Warm amber shift — analog world, pre-Score memory
    root.style.setProperty('--accent', '#f5a623');
    root.style.setProperty('--accent-dim', 'rgba(245,166,35,0.15)');
  } else {
    // Restore cyan for all other chapters
    root.style.setProperty('--accent', '#00f3ff');
    root.style.setProperty('--accent-dim', 'rgba(0,243,255,0.12)');
  }
}
```

#### NEW EFFECT: Impedance Distortion Aura
When the "Impedance Mismatch" beats are active (Kael and Taro failing to connect),
render a subtle **static interference band** horizontally across the mid-screen —
a thin, flickering horizontal line that suggests two signals not quite aligning.
This is purely CSS + a single `<div>` element.

```css
/* A horizontal static line representing signal mismatch */
#impedance-bar {
  position: fixed;
  top: 50%;
  left: 0;
  width: 100%;
  height: 1px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0%, transparent 40%,
    rgba(245,166,35,0.4) 40%, rgba(245,166,35,0.4) 60%,
    transparent 60%
  );
  background-size: 8px 1px;
  animation: impedance-drift 0.08s linear infinite;
  opacity: 0;
  transition: opacity 1s;
  pointer-events: none;
  z-index: 8;
}
@keyframes impedance-drift {
  from { background-position: 0 0; }
  to   { background-position: 8px 0; }
}
/* Activated by JS when beat vol is in 0.35–0.50 range */
#impedance-bar.active { opacity: 1; }
```

#### Fragment Pool (ch03)
```javascript
'ch03': [
  'IMPEDANCE: HIGH', 'SIGNAL: MISMATCH', 'ANALOG DETECTED',
  'HEADPHONES: RELIC', 'GOODBYE', 'MEMORY: STORED', 'FREQUENCY: WARM'
]
```

---

## PHASE II — PROPAGATION (Chapters 4–8)
**Physics**: The signal travels through a medium (Malkuth Academy).
**UI Theme**: "High Fidelity" & "Data Density"

**Phase-level change**: Restore cyan `--accent`. Increase waveform resolution
(reduce step to `x += 4`) to reflect the Academy's 8K "High Fidelity" render mode.
HUD gains a new `FIDELITY` bar alongside TENSION and COHERENCE.

---

### Chapter 4: The Medium
**Signal**: `ch04_medium` → `emotional_load: 0.50`, `system_pressure: 0.50`, `surveillance: 0.40`
**Event**: Arrival at Malkuth. Meeting Hana Chord (Square Wave).
**Manga Beat**: The room rotating 90 degrees when the Headmaster speaks.

#### Tension Arc
```
Transport arrival — awe: vol 0.30, coh 0.85
First sight of Malkuth 8K resolution: vol 0.35, coh 0.92  ← peak clarity
Headmaster speaks: vol 0.45, coh 0.78
Hana Chord introduced: vol 0.52, coh 0.70
Room rotation moment: vol 0.65, coh 0.55  ← GLITCH trigger
```

#### NEW EFFECT: Hana's Square Wave Aura
Hana's waveform is "Rigid, instant rise/fall, no ambiguity." When her dialogue
beats are active, replace the `drawWaveform()` ambient layer with a **square wave
pattern** — sharp 90-degree corners instead of smooth sine curves. This is a
waveform mode toggle, not a permanent change.

```javascript
// Add a waveform mode parameter to drawWaveform()
// Mode: 'sine' (default) | 'square' (Hana active) | 'sawtooth' (crisis, Ch10)

function drawActiveCharacterWave(ctx, canvas, time, vol, mode) {
  if (mode === 'square') {
    // Square wave: constant high for first half of period, low for second
    ctx.strokeStyle = `rgba(255,255,255,0.06)`;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    const period = 120; // px per cycle
    for (let x = 0; x < canvas.width; x += 2) {
      const phase    = (x + time * 0.05) % period;
      const isHigh   = phase < period / 2;
      const y = (canvas.height / 2) + (isHigh ? -30 : 30) * vol;
      x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
    }
    ctx.stroke();
  }
}
// Set waveMode = 'square' when Hana dialogue tag is active
```

#### NEW EFFECT: Room Rotation
For the Headmaster's speech beat (tagged `data-tag="headmaster"`), apply a
CSS `rotate` transform to `#beat-container` — a slow, disorienting 2–3° tilt
that holds while the beat is active and resets on exit.

```javascript
// In _updateSentences(), when beat.tag === 'headmaster' and active:
document.getElementById('beat-container').style.transform =
  `rotate(${(Math.sin(Date.now() * 0.0003) * 2)}deg)`;
// Reset on beat exit: style.transform = ''
```

---

### Chapter 5: The Sync Check
**Signal**: `ch05_sync_check` → `emotional_load: 0.45`, `system_pressure: 0.40`, `surveillance: 0.30`
**Event**: Training session. Taro syncs with Ven (The Sink). Bass Drop shockwave.

#### Tension Arc
```
Training begins (cautious): vol 0.35, coh 0.80
Team Link established: vol 0.40, coh 0.85  ← coherence peaks here
Sync deepens — Ven absorbing: vol 0.45, coh 0.82
Thermal Load warning: vol 0.60, coh 0.65
Bass Drop moment: vol 0.80, coh 0.30  ← GLITCH + shockwave
Recovery: vol 0.45, coh 0.75
```

#### NEW EFFECT: Team Link Status Bars
When the Sync with Ven is active, show two secondary bars in the HUD:
`VEN_SYNC` and `THERMAL_LOAD`. These animate: VEN_SYNC fills up during
the sync beats, THERMAL_LOAD spikes during the Bass Drop.

```javascript
// Add to HUD HTML (hidden by default, shown for ch05 only):
// <div class="hud-line" id="team-link-hud" style="opacity:0">
//   <span>VEN_SYNC</span> <div class="hud-bar"><div id="ven-sync-bar" ...></div></div>
// </div>
// <div class="hud-line" id="thermal-hud">
//   <span>THERMAL</span> <div class="hud-bar"><div id="thermal-bar" ...></div></div>
// </div>
//
// Drive VEN_SYNC fill from coh (inverted from beat values — the cleaner the sync, higher fill)
// Drive THERMAL_LOAD from vol directly
```

#### NEW EFFECT: Bass Drop Shockwave
A single-frame full-viewport radial pulse from center — a ring that expands and
fades. Triggered by `data-tag="bass_drop"` beat becoming active.

```javascript
function triggerShockwave() {
  const ring = document.createElement('div');
  Object.assign(ring.style, {
    position: 'fixed', top: '50%', left: '50%',
    transform: 'translate(-50%, -50%) scale(0)',
    width: '100vmax', height: '100vmax',
    border: '2px solid rgba(0,243,255,0.6)',
    borderRadius: '50%',
    pointerEvents: 'none', zIndex: 50,
    transition: 'transform 0.8s ease-out, opacity 0.8s ease-out',
    opacity: 1
  });
  document.body.appendChild(ring);
  requestAnimationFrame(() => {
    ring.style.transform = 'translate(-50%, -50%) scale(2)';
    ring.style.opacity = '0';
  });
  setTimeout(() => ring.remove(), 850);
}
// Call when tag === 'bass_drop' and sentence enters active state for first time
```

---

### Chapter 6: The Ground State
**Signal**: `ch06_ground_state` → `emotional_load: 0.30`, `system_pressure: 0.30`, `surveillance: 0.20`
**Event**: Ven vents heat. The Ground Link forms. Lowest surveillance of any chapter.
**Manga Beat**: Steam venting from Ven's armor.

#### Tension Arc
```
Aftermath of Bass Drop — exhausted: vol 0.28, coh 0.78
Ven vents (industrial, deliberate): vol 0.30, coh 0.82
Ground Link forms: vol 0.25, coh 0.92  ← most stable moment in the book so far
Bond solidified: vol 0.28, coh 0.90
```

#### Treatment
This is the **quietest chapter** in Phase II. All glitch and distortion effects should be
completely dormant (`vol` never crosses 0.60). Let the waveform settle into near-flat lines.
The vignette should be nearly invisible. Let the text breathe.

**Specific beat**: When `data-tag="ground_link"` becomes active, trigger a warm
amber glow (echoing Ch3's palette) briefly at the ambient center — the Ground Link
is warm, not cold.

---

### Chapter 7: The Rival
**Signal**: `ch07_rival` → `emotional_load: 0.60`, `system_pressure: 0.70`, `surveillance: 0.60`
**Event**: Marcus Staccato introduced. Combat UI. Marcus moves faster than the frame rate.
**Manga Beat**: Marcus moving faster than the frame rate (Glitch movement).

#### Tension Arc
```
Marcus enters — immediate threat assessment: vol 0.55, coh 0.65
Combat UI tags appear: vol 0.65, coh 0.55
Marcus demonstration: vol 0.78, coh 0.38  ← frame-rate glitch
Taro's threat response: vol 0.72, coh 0.42
Standoff ends: vol 0.55, coh 0.60
```

#### NEW EFFECT: Combat UI Tags
When `data-tag="combat_ui"` beats are active, add a target reticle over each
sentence as it becomes active — not the surveillance crosshair, but a tighter
corner-bracket targeting frame. Think cursor targeting a threat.

```css
.sentence.active.combat-tagged::before {
  content: '';
  position: absolute;
  top: -4px; left: -4px;
  width: calc(100% + 8px); height: calc(100% + 8px);
  border-top: 1px solid var(--danger);
  border-left: 1px solid var(--danger);
  clip-path: polygon(0 0, 20px 0, 0 20px); /* Corner bracket only */
  pointer-events: none;
}
.sentence.active.combat-tagged::after {
  /* Mirror on bottom-right corner */
  content: '';
  position: absolute;
  bottom: -4px; right: -4px;
  width: 20px; height: 20px;
  border-bottom: 1px solid var(--danger);
  border-right: 1px solid var(--danger);
  pointer-events: none;
}
```

#### NEW EFFECT: Frame-Rate Glitch (Marcus movement)
For the `data-tag="frame_skip"` beat: apply a rapid CSS `steps()` animation
to `#beat-container` opacity — simulating dropped frames. Distinct from the
smooth glitch; this is choppy, digital, inhuman speed.

```css
@keyframes frame-skip {
  0%   { opacity: 1; transform: translateX(0); }
  15%  { opacity: 0; transform: translateX(8px); }  /* frame drop */
  16%  { opacity: 1; transform: translateX(-3px); } /* snap back */
  30%  { opacity: 0; transform: translateX(5px); }
  31%  { opacity: 1; transform: translateX(0); }
  100% { opacity: 1; transform: translateX(0); }
}
/* Applied for 1.5s on the Marcus glitch beat only */
```

---

### Chapter 8: The Sortie
**Signal**: `ch08_sortie` → `emotional_load: 0.85`, `system_pressure: 0.80`, `surveillance: 0.90`
**Event**: First field mission. "Twilight Band." Dropship deployment. Fog of war.
**Manga Beat**: Team dropping from the dropship in formation.

#### Tension Arc
```
Briefing (pre-mission tension): vol 0.55, coh 0.65
Dropship launch: vol 0.70, coh 0.52
Entering Twilight Band: vol 0.78, coh 0.40  ← interference begins
Data drops out: vol 0.85, coh 0.30  ← GLITCH active
Combat contact: vol 0.92, coh 0.18
```

#### NEW EFFECT: Fog of War — Progressive Data Dropout
In the Twilight Band, data is unreliable. Add a new waveform behaviour:
at `coh < 0.40`, randomly **drop sections of the waveform** (gaps in the
canvas path, not drawn). This simulates interference in the data feed.

```javascript
// Modify drawWaveform() — add a 'drop' chance per segment at low coherence:
const shouldDrop = coh < 0.40 && Math.random() < (0.40 - coh) * 2;
if (shouldDrop) {
  ctx.moveTo(x, y); // lift pen — creates a gap in the line
} else {
  ctx.lineTo(x, y);
}
```

#### NEW EFFECT: Altimeter Drop
On the dropship descent beat (`data-tag="drop"`), show a temporary
fixed HUD element: a rapidly counting-down altimeter.

```javascript
function runAltimeter(startAlt, targetAlt, duration) {
  const el = document.getElementById('altimeter-display') || createAltimeterEl();
  let current = startAlt;
  const step = (startAlt - targetAlt) / (duration / 16);
  const tick = setInterval(() => {
    current -= step;
    el.textContent = `ALT: ${Math.max(targetAlt, Math.round(current))}m`;
    if (current <= targetAlt) { clearInterval(tick); el.remove(); }
  }, 16);
}
```

---

## PHASE III — INTERFERENCE (Chapters 9–10)
**Physics**: Signals collide.
**UI Theme**: "Signal Corruption" & "Encryption"

**Phase-level change**: From Ch9 onward, the surveillance crosshair is **always visible**
(oscillating between 0.5–1.0 opacity based on chapter surveillance value).
The waveform's accent layer changes colour from cyan to a sickly **purple** (`#9933ff`) —
the colour of the Silence faction and bio-desync.

---

### Chapter 9: The Silence
**Signal**: `ch09_silence` → `emotional_load: 0.95`, `system_pressure: 0.20`, `surveillance: 0.10`
**Event**: A Silence attack on the city. The Safe Mode filters begin dropping.
**Note**: High emotional load but *low* system pressure — the Score itself is going offline.

#### Tension Arc
```
City ambient — false calm: vol 0.30, coh 0.88
First silence field appears: vol 0.50, coh 0.70
Score filters begin dropping: vol 0.72, coh 0.45
Full silence zone: vol 0.90, coh 0.12  ← waveform collapses to near-flat
The "real world" begins bleeding through: vol 0.95, coh 0.05
```

#### NEW EFFECT: Waveform Collapse
In the silence zones (`coh < 0.15`), the waveform doesn't just add noise — it
**decays amplitude to near-zero**. The canvas goes nearly empty. This is the
most powerful moment of visual absence in the book. Silence should *look* like silence.

```javascript
// In drawWaveform(), when coh < 0.15:
const waveAmp = canvas.height * 0.12 * vol * coh * 8; // approaches 0 with coh
// The waveform flattens to a trembling near-horizontal line
```

#### NEW EFFECT: Score Filter Dropout
As `coh` drops below 0.30 in this chapter, progressively remove UI elements:
first the fragment container, then the waveform label, then the HUD bars flicker
and show `--` instead of values. The Score itself is failing.

```javascript
// HUD value dropout:
if (coh < 0.20) {
  document.getElementById('hud-tension-val').textContent = '--';
  document.getElementById('hud-coherence-val').textContent = '--';
}
if (coh < 0.10) {
  document.getElementById('hud-section').textContent = 'NO_SIGNAL';
}
```

---

### Chapter 10: The Breach
**Signal**: `ch10_breach` → `emotional_load: 1.00`, `system_pressure: 0.90`, `surveillance: 0.20`
**Event**: Taro removes the Limiter. The Breach. Reality dissolves into Source Code.
**This is the climax of Phase III.** Everything should hit simultaneously.

#### Tension Arc
```
Cornered — Hana down, Ven failing: vol 0.80, coh 0.25
Taro considers the limiter: vol 0.88, coh 0.18
Limiter removal: vol 1.00, coh 0.05  ← ALL EFFECTS MAXIMUM
The Sawtooth Wave erupts: vol 1.00, coh 0.00
Reality dissolves: vol 1.00, coh 0.00
Kernel Panic — source code visible: vol 1.00, coh 0.00
```

#### NEW EFFECT: Sawtooth Waveform Mode
When `data-tag="breach"` fires, switch `drawWaveform()` to sawtooth mode:
a linear rise followed by an instant vertical drop, repeating. This is the
signature of Taro's Breach state — jagged, violent, tearing through the score.

```javascript
// Sawtooth wave rendering in drawWaveform():
if (waveMode === 'sawtooth') {
  const period = 80; // pixels per cycle
  for (let x = 0; x < canvas.width; x += 2) {
    const phase = ((x + time * 0.15) % period) / period; // 0→1 sawtooth
    const y = (canvas.height / 2) + (phase * 2 - 1) * canvas.height * 0.18 * vol;
    x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  }
}
```

#### NEW EFFECT: Source Code Reveal
On the `data-tag="source_code"` beat (the final moment of Ch10), overlay the
stage background with a dense grid of falling random hex values — not Matrix-style
falling (that's too on-the-nose), but a static field of raw data that replaces
all previous rendering. This is the **most intense visual in the book**.

```javascript
// Source code field — drawn on the wave canvas as a 4th layer
function drawSourceCode(ctx, canvas, intensity) {
  const chars = '0123456789ABCDEF';
  ctx.font = '10px var(--font-mono)';
  ctx.fillStyle = `rgba(0,243,255,${intensity * 0.08})`;
  for (let col = 0; col < canvas.width; col += 14) {
    for (let row = 0; row < canvas.height; row += 14) {
      ctx.fillText(chars[Math.floor(Math.random() * 16)], col, row);
    }
  }
}
// Activated only at coh === 0 and tag === 'source_code'
```

---

## PHASE IV — FEEDBACK LOOP (Chapters 11–14)
**Physics**: Runaway amplification and forced damping.
**UI Theme**: "System Crash" → "Safe Mode" → "The Patch" → Recovery

**Phase-level change**: Ch11 introduces the **wireframe render mode** — a complete
visual overhaul while Taro is in Safe Mode. The cyan `--accent` shifts to `#4488ff`
(cold blueprint blue). Background becomes a faint grid pattern.

---

### Chapter 11: Safe Mode
**Signal**: `ch11_safe_mode` → `emotional_load: 0.75`, `system_pressure: 0.40`, `surveillance: 0.60`
**Event**: Taro wakes in wireframe Safe Mode. Stripped of texture, sound, self.

#### Tension Arc
```
Waking — disorientation: vol 0.55, coh 0.30
Wireframe world registers: vol 0.45, coh 0.35
Carrier wave tinnitus begins: vol 0.65, coh 0.25
Time dilation — each second is an hour: vol 0.60, coh 0.28
Engines approaching in the distance: vol 0.70, coh 0.32
```

#### NEW EFFECT: Wireframe Mode (Biggest Visual Change in the Book)
Override the entire visual language while in Ch11. Apply these CSS changes:

```css
/* Wireframe Mode — applied as body class .wireframe-mode */
.wireframe-mode {
  --bg:   #02080F;      /* Near-black — empty render space */
  --text: #4488ff;      /* Blueprint blue — cold, geometric */
  --accent: #4488ff;
  --wave-color: rgba(68,136,255,0.05);
}
.wireframe-mode #stage::before {
  /* Fine grid overlay — the Safe Mode geometry engine */
  content: '';
  position: absolute; top: 0; left: 0;
  width: 100%; height: 100%;
  background-image:
    linear-gradient(rgba(68,136,255,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(68,136,255,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  z-index: 1; pointer-events: none;
}
/* Text renders in wireframe — sharper, no body font */
.wireframe-mode .sentence { font-family: var(--font-mono) !important; }
```

```javascript
// Apply on ch11 chapter init, remove on ch12 init
document.body.classList.add('wireframe-mode');
```

---

### Chapter 12: The Audit
**Signal**: `ch12_audit` → `emotional_load: 0.90`, `system_pressure: 1.00`, `surveillance: 1.00`
**Event**: Voss's interrogation. The Patch is offered. Hana in tank, Ven in cell.
**Max surveillance. Max system pressure.**

#### Tension Arc
```
Taro restrained in interrogation room: vol 0.55, coh 0.60  ← system pressure, not chaos
Voss reveals the grid dependency: vol 0.65, coh 0.55
Hana's video feed shown: vol 0.80, coh 0.45
Ven's video feed shown: vol 0.85, coh 0.40
"Accept the Patch": vol 0.70, coh 0.50  ← deliberate, not explosive
Taro's acceptance: vol 0.60, coh 0.55  ← the quiet collapse
```

#### Treatment
This chapter's tension is **bureaucratic** — cold authority, not chaos. Glitch
should be minimal. Surveillance crosshair at full opacity (1.0). Waveform is
almost flat (Voss's "Sine — zero distortion" damping effect). The horror here is
the *absence* of noise, not its presence.

**Specific beat**: When `data-tag="video_feed"` activates, add a brief
scan-line flicker suggesting a low-quality security camera feed is being shown.

```css
@keyframes camera-flicker {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.85; }
  52%       { opacity: 1; }
}
.sentence.active.camera-feed { animation: camera-flicker 0.4s step-end 3; }
```

---

### Chapter 13: The Patch
**Signal**: `ch13_patch` → `emotional_load: 0.30`, `system_pressure: 0.95`, `surveillance: 0.95`
**Event**: "Project Dissonance" installed. Post-patch — Taro sees Source Code instead of music.
**Narrative shift**: After this chapter, Taro's Score vision changes permanently.

#### NEW EFFECT: Vision Mode Transition
At the `data-tag="patch_installed"` beat, transition the visual language:

**Before patch**: Current system (cyan, sine waves, music metaphors in fragments)
**After patch**: The "Dissonance Vision" mode — shift `--accent` to `#00ff88` (clinical green),
fragments switch to showing raw integers (`POTENTIAL: 48,000J`, `STRESS_LINE: ACTIVE`),
waveform gains a second mathematical grid overlay.

```javascript
// This is a PERMANENT change from this beat forward — store in a flag
// that persists in chapter transitions:
window.hasPatch = true;

// After patch, fragment pool changes:
const FRAGMENT_POOL_POST_PATCH = {
  default: ['STRESS_LINE: DETECTED', 'POTENTIAL: 48,000J', 'ORGAN: NOMINAL',
            'NEURAL_MAP: ACTIVE', 'STRUCTURAL_WEAKNESS: 3', '//RAW_DATA//']
};
```

---

### Chapter 14: The Return
**Signal**: `ch14_return` → `emotional_load: 0.60`, `system_pressure: 0.80`, `surveillance: 0.85`
**Event**: Taro returns to action post-patch. New Dissonance Vision active.
**AR Focus**: Seeing stress lines, raw integers, biological overlays.

#### Tension Arc
```
Re-entering the world — everything looks wrong: vol 0.50, coh 0.55
First stress line seen on a person: vol 0.58, coh 0.50
Biological overlay — seeing organs: vol 0.65, coh 0.45
"Cold, invasive, dirty": vol 0.60, coh 0.50
```

#### Treatment
This chapter should feel **alienating** with the green Dissonance Vision palette.
The waveform switches from audio-metaphor (flowing sine) to a mathematical grid —
straight lines, right angles, data readouts. The contrast with the warm Ch3 and the
flowing Ch1 should be jarring.

---

## PHASE V — EQUILIBRIUM (Chapters 15–17)
**Physics**: Finding rest between the notes.
**UI Theme**: "The Underground" — lo-fi, analog, human

**Phase-level change**: Underground chapters (Ch16–17) are inside Faraday Cages.
The Score is offline. Effects framework needs an **"analog mode"**:
- Waveform removed entirely (just static noise, very faint)
- HUD fades out (`opacity: 0`)
- Scanlines intensify (feels like an old CRT monitor without signal)
- No system fragments — instead, handwritten/human fragments appear

---

### Chapter 15: Phantom Mesh
**Signal**: `ch15_phantom_mesh` → `emotional_load: 0.85`, `system_pressure: 0.75`, `surveillance: 0.60`
**Event**: Taro encounters the Phantom Mesh — resonance echoes of the past battle.

#### NEW EFFECT: Palimpsest Ghosting
The README describes "Palimpsest Ghosting" — old fragments lingering as ghosts.
Implement here: when fragments fade out, instead of `remove()`, drop opacity to
`0.04` and leave them in place, absolutely positioned, building a visual history.
Cap at 12 ghost fragments before clearing oldest.

```javascript
function fadeToGhost(fragEl) {
  // Instead of removing, ghost it
  fragEl.style.transition = 'opacity 2s ease';
  fragEl.style.opacity = '0.04';
  fragEl.style.pointerEvents = 'none';
  fragEl.classList.add('ghost-fragment');
  // Enforce cap — remove oldest ghost if over limit
  const ghosts = document.querySelectorAll('.ghost-fragment');
  if (ghosts.length > 12) ghosts[0].remove();
}
```

---

### Chapter 16: Illegal Modulations
**Signal**: `ch16_illegal_modulations` → `emotional_load: 0.90`, `system_pressure: 0.50`, `surveillance: 0.40`
**Event**: Taro experiments with illegal frequency manipulation. Outside the Score's rules.

#### Tension Arc
```
First illegal pulse: vol 0.60, coh 0.55
System doesn't stop it: vol 0.70, coh 0.48
Going further: vol 0.85, coh 0.35
Peak illegal modulation: vol 0.90, coh 0.25  ← GLITCH, aberration
Joy in the chaos: vol 0.78, coh 0.40
```

#### Treatment
Glitch and chromatic aberration should feel **celebratory** here, not threatening.
The danger effects are the same code but the narrative context reframes them.
Consider: the aberration colours could briefly invert (red left, cyan right —
the "wrong" direction) to suggest lawbreaking rather than damage.

---

### Chapter 17: The Underground
**Signal**: `ch17_underground` → `emotional_load: 0.95`, `system_pressure: 0.10`, `surveillance: 0.00`
**Event**: The Faraday Cage. Silence that isn't death. Peace.
**Zero surveillance. Lowest system pressure in the book.**

#### Tension Arc
```
Entering the Faraday Cage: vol 0.40, coh 0.70
HUD fades out: vol 0.30, coh 0.80
Silence that feels like relief: vol 0.20, coh 0.90
"They can't hear us here": vol 0.15, coh 0.95
The sound of their own heartbeats: vol 0.10, coh 0.98
```

#### NEW EFFECT: Analog Mode (Final Chapter Transformation)
```javascript
function enterAnalogMode() {
  // Remove the HUD entirely
  document.getElementById('ui-layer').style.opacity = '0';
  document.getElementById('ui-layer').style.transition = 'opacity 3s ease';

  // Kill the waveform canvas
  document.getElementById('wave-bg').style.opacity = '0';

  // Intensify scanlines to suggest a blank CRT
  const style = document.createElement('style');
  style.textContent = `
    #stage::after {
      background: repeating-linear-gradient(
        0deg, transparent, transparent 1px,
        rgba(0,0,0,0.08) 1px, rgba(0,0,0,0.08) 2px
      ) !important;
    }
  `;
  document.head.appendChild(style);

  // Human fragments — no more system tags
  window.analogMode = true;
}

// Analog fragment pool:
const FRAGMENT_POOL_ANALOG = [
  'no signal', '...silence...', 'faraday active', 'just us',
  'they can\'t hear us', 'breathe', 'finally', '—'
];
```

---

## IMPLEMENTATION ORDER

Work in this sequence. Each step is testable before the next begins:

**Step 1 — Foundation (1–2 days)**
Refactor the existing Ch1 file so chapter signals, vol/coh arcs, fragment pools,
and waveform modes are all driven by a shared config object rather than hardcoded values.
This is the prerequisite for multi-chapter work.

```javascript
const CHAPTER_CONFIG = {
  ch01_zap:              { accent: '#00f3ff', waveMode: 'sine',      hudExtras: [],             analogMode: false },
  ch02_assessment:       { accent: '#00f3ff', waveMode: 'sine',      hudExtras: ['social_tag'], analogMode: false },
  ch03_modulation:       { accent: '#f5a623', waveMode: 'sine',      hudExtras: ['impedance'],  analogMode: false },
  ch04_medium:           { accent: '#00f3ff', waveMode: 'square',    hudExtras: ['fidelity'],   analogMode: false },
  ch05_sync_check:       { accent: '#00f3ff', waveMode: 'sine',      hudExtras: ['team_link'],  analogMode: false },
  ch06_ground_state:     { accent: '#00f3ff', waveMode: 'sine',      hudExtras: [],             analogMode: false },
  ch07_rival:            { accent: '#00f3ff', waveMode: 'sine',      hudExtras: ['combat'],     analogMode: false },
  ch08_sortie:           { accent: '#00f3ff', waveMode: 'dropout',   hudExtras: ['altimeter'],  analogMode: false },
  ch09_silence:          { accent: '#9933ff', waveMode: 'collapse',  hudExtras: [],             analogMode: false },
  ch10_breach:           { accent: '#9933ff', waveMode: 'sawtooth',  hudExtras: [],             analogMode: false },
  ch11_safe_mode:        { accent: '#4488ff', waveMode: 'wireframe', hudExtras: [],             analogMode: false },
  ch12_audit:            { accent: '#4488ff', waveMode: 'flat',      hudExtras: ['camera'],     analogMode: false },
  ch13_patch:            { accent: '#00ff88', waveMode: 'grid',      hudExtras: [],             analogMode: false },
  ch14_return:           { accent: '#00ff88', waveMode: 'grid',      hudExtras: [],             analogMode: false },
  ch15_phantom_mesh:     { accent: '#00f3ff', waveMode: 'sine',      hudExtras: ['palimpsest'], analogMode: false },
  ch16_illegal_mods:     { accent: '#00f3ff', waveMode: 'sine',      hudExtras: [],             analogMode: false },
  ch17_underground:      { accent: '#00f3ff', waveMode: 'static',    hudExtras: [],             analogMode: true  },
};
```

**Step 2 — Phase I (Ch2–3)** — Social tag overlay, amber theme, impedance bar
**Step 3 — Phase II (Ch4–8)** — Waveform modes, team link HUD, shockwave, combat UI, altimeter
**Step 4 — Phase III (Ch9–10)** — Waveform collapse, source code reveal, sawtooth mode
**Step 5 — Phase IV (Ch11–14)** — Wireframe mode, camera flicker, Dissonance Vision transition
**Step 6 — Phase V (Ch15–17)** — Palimpsest ghosts, analog mode, HUD fade

---

## DATA TAGGING REFERENCE

Every paragraph needs `data-vol`, `data-coh`, and where relevant `data-tag`.
Tag values used across all chapters:

| Tag | Effect(s) triggered | Chapters |
|---|---|---|
| `boot` | Scramble + HUD boot | Ch1 |
| `pain` | Glitch + red fragments | Ch1, Ch10 |
| `override` | Glitch + system scramble | Ch1, Ch10 |
| `crash` | Crash overlay | Ch1 |
| `bass_drop` | Shockwave ring | Ch5 |
| `headmaster` | Room rotation | Ch4 |
| `social_tag` | Badge corruption | Ch2 |
| `impedance` | Interference bar | Ch3 |
| `combat_ui` | Corner bracket overlay | Ch7 |
| `frame_skip` | Choppy animation | Ch7 |
| `drop` | Altimeter countdown | Ch8 |
| `silence_field` | Waveform collapse | Ch9 |
| `breach` | Sawtooth + source code | Ch10 |
| `source_code` | Hex grid overlay | Ch10 |
| `wireframe` | Blue grid mode | Ch11 |
| `video_feed` | Camera flicker | Ch12 |
| `patch_installed` | Vision mode transition | Ch13 |
| `faraday` | Analog mode | Ch17 |

---

*All new effects inherit the existing `narrativeState.volume` / `narrativeState.coherence`
architecture. No new global state variables are needed beyond `window.hasPatch` and
`window.analogMode`. The config object in Step 1 is the only structural prerequisite.*
