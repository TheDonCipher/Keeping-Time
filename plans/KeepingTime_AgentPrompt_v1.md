# AGENT TASK — Keeping Time: Volume One
## Full Scrollytelling Upgrade Pass
### Target: Antigravity / Gemini 3 Flash

---

> **How to read this document**
> Execute the four phases in order. Each phase is independently testable.
> Every code block includes comments explaining *why*, not just *what*.
> Do not change anything not listed here. This is a surgical update pass.
> The audience for this experience is anime watchers — readers who expect
> the UI to *react*, not just display. Every beat should feel like a cut.

---

## BEFORE YOU START — Source Files

The project is a single HTML file containing all 17 chapters as scrollable
`<section>` elements. Each paragraph is a `<p>` element with `data-vol` and
`data-coh` attributes. Audio is handled by the `AudioEngine` class.
Scroll state is managed by `ScrollEngine.tick()`.
Narrative state is managed by `NarrativeState.update()`.

**The core problem this pass solves:**
Every paragraph currently has `data-vol='0.25' data-coh='0.8'` — identical
flat values across all 17 chapters. The UI is decorative. After this pass,
every beat has its own values and the UI tells the emotional arc of the
novel independently of the prose.

---

## PHASE 1 — PER-BEAT DATA VALUES
### Target: Every `<p>` element in `ch01` through `ch17`

Replace every `data-vol` and `data-coh` with narrative-accurate values.
Use the Beat Type Reference table below. Read each paragraph, identify its
type, assign the corresponding values. Do not homogenise — adjacent
paragraphs of the same type should still vary ±0.03 to feel organic.

### Beat Type Reference

```
// BEAT TYPE QUICK REFERENCE — (data-vol, data-coh)
//
// System alert (backtick / monospace lines):       (0.45, 0.85)
// System CRITICAL / WARNING:                        (0.75, 0.60)
// System PEAK — limiter removal, the unmask:        (0.99, 0.05)
// Epigraph / lore blockquote:                       (0.10, 0.95)
// Zone / FIDELITY status header paragraph:          (0.20, 0.92)
// Neutral narration (3rd-person prose):             (0.25, 0.80)
// HUD metric narration (BPM, SDI, HIQ refs):        (0.35, 0.80)
// Taro internal thought / perspective:              (0.40, 0.70)
// Dialogue — calm:                                  (0.30, 0.75)
// Dialogue — tense / argument / confrontation:      (0.55, 0.65)
// Dialogue — Voss / Krell (authority, clipped):     (0.20, 0.95)
// Physical action / impact / combat beat:           (0.60, 0.60)
// Phase conflict (two signals colliding):           (0.70, 0.55)
// Resonance spike / Taro running high:              (0.85, 0.40)
// Void / silence moment (Ch9, dead zones):          (0.10, 0.20)
// Post-patch / compliant beat:                      (0.15, 0.92)
// Elara / wrong-note sync beat:                     (0.45, 0.88)
// Underground / illegal mod beat:                   (0.50, 0.50)
// Chapter end / TRACK_COMPLETE line:                (0.20, 0.85)
```

### Special Beats — Add data-tag Attributes

In addition to vol/coh, add `data-tag` to the following beat types.
These trigger one-shot audio events (see Phase 2):

```
data-tag="bass_drop"    → First beat of Ch06 or Ch08 subsonic arrival
data-tag="combat_ui"    → First impact beat in Ch08 Sortie
data-tag="frame_skip"   → Error / glitch beats in Ch09 and Ch10
data-tag="impedance"    → Collar-tighten beats (Ch02, Ch04, Ch11)
data-tag="headmaster"   → Any Krell direct-address line
data-tag="social_tag"   → Malkuth ranking reveal beats (Ch04, Ch07)
data-tag="crash"        → Final line of Ch17 ('I am bringing the noise')
data-tag="limiter"      → All 'limiter removed' / unmasking beats
data-tag="clip"         → Ch10 sawtooth burst / Bb2 aggression peak
data-tag="override"     → Any beat where Taro overrides a system command
data-tag="ghost"        → See Phase 3 Ghost Layer section
```

### Chapter-by-Chapter Arc Targets

Use these as chapter-wide guardrails. Individual beats vary around these
baselines but the average for a chapter should match:

```
// Ch01 — The Zap:         avg vol 0.45, avg coh 0.65  (spike-and-crash arc)
// Ch02 — Assessment:      avg vol 0.30, avg coh 0.82  (clinical, invasive)
// Ch03 — Modulation:      avg vol 0.40, avg coh 0.62  (degraded zone)
// Ch04 — Medium:          avg vol 0.32, avg coh 0.78  (watched, sharp)
// Ch05 — Sync Check:      avg vol 0.42, avg coh 0.70  (forming Triad)
// Ch06 — Ground State:    avg vol 0.35, avg coh 0.65  (Ven, low energy)
// Ch07 — Rival:           avg vol 0.50, avg coh 0.68  (confrontational)
// Ch08 — Sortie:          avg vol 0.65, avg coh 0.55  (combat)
// Ch09 — Silence:         avg vol 0.12, avg coh 0.22  (void — keep near floor)
// Ch10 — Breach:          avg vol 0.72, avg coh 0.40  (broken, uncontrolled)
// Ch11 — Safe Mode:       avg vol 0.38, avg coh 0.75  (Krell's cold room)
// Ch12 — Audit:           avg vol 0.28, avg coh 0.80  (NAI intimate voice)
// Ch13 — Patch:           avg vol 0.15, avg coh 0.92  (compliance, dead flat)
// Ch14 — Return:          avg vol 0.18, avg coh 0.88  (8K pristine, wrong)
// Ch15 — Phantom Mesh:    avg vol 0.35, avg coh 0.65  (cracks forming)
// Ch16 — Illegal Mods:    avg vol 0.48, avg coh 0.52  (unauthorized warmth)
// Ch17 — Underground:     avg vol 0.55, avg coh 0.48  (ends at 0.75 / 0.55)
```

### The Final Beat — 'I am bringing the noise' (Ch17, last line)

```
// This beat is the volume close. Hard-code these exact values:
// data-vol="0.75" data-coh="0.55" data-tag="crash"
// Tension is purposeful — not maxed, not panicked. Ready.
// The waveform will shift to a single sawtooth pulse (see Phase 2).
```

---

## PHASE 2 — AUDIO ENGINE v2
### Target: `AudioEngine` class

Complete rewrite of the drone system. Add all new synthesis types, the
four-layer signal chain, LFO arc, coherence-reactive filter, and
one-shot tag events.

### 2A — Constructor — Add New Properties

```javascript
// NEW PROPERTIES — add to constructor after existing this.droneGain:

this.droneOsc2     = null;  // Secondary oscillator (beating, layered, chord)
this.droneOsc3     = null;  // Third oscillator (harmonic-series, interference)
this.subOsc        = null;  // Sub-bass oscillator (bypasses filter)
this.subGain       = null;  // Sub-bass gain node

this.filter        = null;  // BiquadFilter — coherence-reactive lowpass
this.lfo           = null;  // LFO oscillator — tension-reactive tremolo
this.lfoDepth      = null;  // LFO depth GainNode

this.breathLFO     = null;  // Secondary LFO at 0.2Hz — biological presence
this.breathDepth   = null;  // Breath depth GainNode

this.currentTension   = 0.25;  // Last tension value — used for lerp
this.currentCoherence = 0.80;  // Last coherence value — used for lerp

// Ghost layer — persistent subliminal signal (see Phase 3)
this.ghostCarrier  = null;
this.ghostAM       = null;
this.ghostNoise    = null;
this.ghostDriftLFO = null;
this.ghostGain     = null;
this.ghostFilter   = null;
```

### 2B — Signal Chain — Update `_startDrone()`

Replace the existing `_startDrone()` with the four-layer architecture:

```javascript
_startDrone(config) {
  // ── LAYER SETUP ─────────────────────────────────────────────────
  // Signal chain: [Osc A/B/D] → BiquadFilter → DroneGain → MasterGain
  //               [Osc C sub] ──────────────────────────→ MasterGain
  // Sub-bass bypasses the filter — it is felt, not heard.
  // All layers share DroneGain so per-chapter gain settings apply globally.

  const ctx = this.ctx;
  const now = ctx.currentTime;

  // Create shared filter (coherence-reactive lowpass)
  this.filter = ctx.createBiquadFilter();
  this.filter.type = 'lowpass';
  this.filter.frequency.value = 800; // Will be set by updateNarrativeState
  this.filter.Q.value = config.filterQ || 1.0;

  // Create LFO tremolo (tension-reactive)
  this.lfo = ctx.createOscillator();
  this.lfo.type = 'sine';
  this.lfo.frequency.value = 0.08; // Resting rate — will be updated

  this.lfoDepth = ctx.createGain();
  this.lfoDepth.gain.value = config.lfoDepth || 0.003;
  this.lfo.connect(this.lfoDepth);
  this.lfoDepth.connect(this.droneGain.gain); // Modulates the main gain

  this.lfo.start(now);

  // Route filter → droneGain → masterGain
  this.filter.connect(this.droneGain);
  this.droneGain.connect(this.masterGain);
  this.droneGain.gain.value = config.gain || 0.025;

  // ── SYNTHESIS TYPE SWITCH ────────────────────────────────────────
  // Each case sets up Layer A (droneOsc) and optionally Layer B (droneOsc2)
  // and Layer C (droneOsc3). All primary oscillators connect to this.filter.

  switch(config.type) {

    case 'sine':
    case 'square':
    case 'sawtooth': {
      // Standard single-oscillator types.
      // 'sawtooth' is Taro's raw signal — jagged, uncompressed, wrong.
      // 'square' is hard compliance surveillance.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = config.type;
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);
      break;
    }

    case 'layered': {
      // Two oscillators: fundamental + harmonic.
      // harmonicRatio defaults to 2 (octave) — Ch07 uses 1.25 (major third)
      // for confrontational brightness instead of Ven's dense fullness.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      // harmonicRatio: 2 = octave, 1.25 = major third, 1.5 = perfect fifth
      this.droneOsc2.frequency.value = config.baseFreq * (config.harmonicRatio || 2);
      const layerGain = ctx.createGain();
      layerGain.gain.value = 0.35; // -9dB harmonic layer
      this.droneOsc2.connect(layerGain);
      layerGain.connect(this.filter);
      this.droneOsc2.start(now);
      break;
    }

    case 'beating': {
      // Two oscillators offset by beatFreq Hz — creates phase interference.
      // At 1Hz: one beat per second (Ch05 — Triad searching for lock).
      // At 0.3Hz: one pulse per 3.3s (Ch12 — NAI's hidden heartbeat).
      // At 1.5Hz: faster ghost instability (Ch15 — Phantom Mesh).
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      this.droneOsc2.frequency.value = config.baseFreq + (config.beatFreq || 1.0);
      this.droneOsc2.connect(this.filter);
      this.droneOsc2.start(now);
      break;
    }

    case 'dissonant': {
      // Fundamental + tritone (×√2 ratio = the 'devil's interval').
      // The historically forbidden interval — diabolus in musica.
      // Elara's underground modulation space is literally illegal harmony.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      this.droneOsc2.frequency.value = config.baseFreq * Math.SQRT2; // ×√2 = tritone
      const dissonantGain = ctx.createGain();
      dissonantGain.gain.value = 0.45;
      this.droneOsc2.connect(dissonantGain);
      dissonantGain.connect(this.filter);
      this.droneOsc2.start(now);
      break;
    }

    case 'chord': {
      // Fundamental + perfect fifth (×1.5 ratio).
      // Most stable interval — consonance and forward motion.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      this.droneOsc2.frequency.value = config.baseFreq * 1.5;
      const chordGain = ctx.createGain();
      chordGain.gain.value = 0.55;
      this.droneOsc2.connect(chordGain);
      chordGain.connect(this.filter);
      this.droneOsc2.start(now);
      break;
    }

    case 'harmonic-series': {
      // Fundamental + 2nd harmonic (×2) + 3rd harmonic (×3) at 1.0/0.5/0.25.
      // The Calibration Hall's 'golden viscosity' — engineered acoustic beauty.
      // Organically richer than a sawtooth, deliberately constructed to feel mandatory.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      this.droneOsc2.frequency.value = config.baseFreq * 2;
      const h2g = ctx.createGain(); h2g.gain.value = 0.5;
      this.droneOsc2.connect(h2g); h2g.connect(this.filter);
      this.droneOsc2.start(now);

      this.droneOsc3 = ctx.createOscillator();
      this.droneOsc3.type = 'sine';
      this.droneOsc3.frequency.value = config.baseFreq * 3;
      const h3g = ctx.createGain(); h3g.gain.value = 0.25;
      this.droneOsc3.connect(h3g); h3g.connect(this.filter);
      this.droneOsc3.start(now);
      break;
    }

    case 'pulse': {
      // Square wave + asymmetric WaveShaperNode — narrow duty-cycle pulse.
      // Hollow and mechanical. The sound of surveillance hardware watching
      // with complete indifference. Ch11 Krell: 'flat, grinding, abrasive.'
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'square';
      this.droneOsc.frequency.value = config.baseFreq;

      const pulseShaper = ctx.createWaveShaper();
      const curve = new Float32Array(256);
      for (let i = 0; i < 256; i++) {
        const x = (i * 2) / 256 - 1;
        // Clip negative harder (×0.3) than positive (×0.9) — asymmetric duty cycle
        curve[i] = x >= 0 ? Math.min(x * 0.9, 0.85) : Math.max(x * 0.3, -0.25);
      }
      pulseShaper.curve = curve;
      this.droneOsc.connect(pulseShaper);
      pulseShaper.connect(this.filter);
      this.droneOsc.start(now);
      break;
    }

    case 'resonant': {
      // Sine through high-Q bandpass (Q=8-12) that almost self-oscillates.
      // Produces a ringing, sibilant, surveillance-room ambience.
      // Not the watcher — the air in the room the watcher sits in.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      // Override filter to high-Q bandpass for this type
      this.filter.type = 'bandpass';
      this.filter.frequency.value = config.baseFreq;
      this.filter.Q.value = config.filterQ || 9;
      break;
    }

    case 'collar': {
      // Any oscillator type passed through tight bandpass (Q=5-8, ~2 semitones).
      // Cuts the fundamental's harmonic richness — only the 'allowed' band passes.
      // Models the compliance patch. Not silence — constrained signal.
      // The tone is still present; the freedom has been removed.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = config.oscType || 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      // Override to tight bandpass — only compliance-window frequencies pass
      this.filter.type = 'bandpass';
      this.filter.frequency.value = config.baseFreq;
      this.filter.Q.value = config.filterQ || 6;
      break;
    }

    case 'interference': {
      // Three oscillators at slightly different frequencies (base, base+Δ1, base+Δ2).
      // Three-way interaction = non-periodic amplitude fluctuation — unpredictable.
      // Ch17: multiple wrong notes coexisting without resolution.
      // The underground collective. They have stopped trying to lock.
      this.droneOsc = ctx.createOscillator();
      this.droneOsc.type = 'sine';
      this.droneOsc.frequency.value = config.baseFreq;
      this.droneOsc.connect(this.filter);
      this.droneOsc.start(now);

      this.droneOsc2 = ctx.createOscillator();
      this.droneOsc2.type = 'sine';
      this.droneOsc2.frequency.value = config.baseFreq + (config.delta1 || 1.3);
      const d1g = ctx.createGain(); d1g.gain.value = 0.75;
      this.droneOsc2.connect(d1g); d1g.connect(this.filter);
      this.droneOsc2.start(now);

      this.droneOsc3 = ctx.createOscillator();
      this.droneOsc3.type = 'sine';
      this.droneOsc3.frequency.value = config.baseFreq + (config.delta2 || 3.1);
      const d2g = ctx.createGain(); d2g.gain.value = 0.55;
      this.droneOsc3.connect(d2g); d2g.connect(this.filter);
      this.droneOsc3.start(now);
      break;
    }

    case 'void-decay': {
      // White noise decaying exponentially to silence over config.decayTime seconds.
      // Ch09 only. The Score is not muted — it dies.
      // 'silence did not exist — only varying degrees of organized noise.'
      const bufferSize = ctx.sampleRate * 2;
      const noiseBuffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
      const data = noiseBuffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

      const noiseSource = ctx.createBufferSource();
      noiseSource.buffer = noiseBuffer;
      noiseSource.loop = true;
      noiseSource.connect(this.filter);
      noiseSource.start(now);

      // Decay the droneGain to zero over decayTime — not a cut, a death
      const decayTime = config.decayTime || 3.5;
      this.droneGain.gain.setValueAtTime(this.droneGain.gain.value, now);
      this.droneGain.gain.exponentialRampToValueAtTime(0.0001, now + decayTime);
      this.droneOsc = noiseSource; // Store reference for cleanup
      break;
    }

    case 'crackle': {
      // White noise — analogue texture with no Score signal.
      // Ch17 fallback if 'interference' is not available.
      const bufSize = ctx.sampleRate * 2;
      const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
      const d = buf.getChannelData(0);
      for (let i = 0; i < bufSize; i++) d[i] = Math.random() * 2 - 1;
      const ns = ctx.createBufferSource();
      ns.buffer = buf; ns.loop = true;
      ns.connect(this.filter); ns.start(now);
      this.droneOsc = ns;
      break;
    }
  }

  // ── BREATH MODIFIER (optional) ───────────────────────────────────
  // Applied when config.breathDepth is defined.
  // Runs at 0.2Hz (12 breaths/min) — biological presence in the signal.
  // Ven in the vault (Ch06). NAI heartbeat (Ch12).
  if (config.breathDepth) {
    this.breathLFO = ctx.createOscillator();
    this.breathLFO.type = 'sine';
    this.breathLFO.frequency.value = 0.2;
    this.breathDepth = ctx.createGain();
    this.breathDepth.gain.value = config.breathDepth;
    this.breathLFO.connect(this.breathDepth);
    this.breathDepth.connect(this.droneGain.gain);
    this.breathLFO.start(now);
  }

  // ── SUB-BASS LAYER (optional) ────────────────────────────────────
  // Bypasses the filter — felt as physical weight, not heard as pitch.
  // Ch08 (55Hz layered + 27.5Hz sub), Ch14 removed per spec.
  if (config.subFreq) {
    this.subOsc = ctx.createOscillator();
    this.subOsc.type = 'sine';
    this.subOsc.frequency.value = config.subFreq;
    this.subGain = ctx.createGain();
    this.subGain.gain.value = config.subGain || 0.015;
    this.subOsc.connect(this.subGain);
    this.subGain.connect(this.masterGain); // Direct to master — bypasses filter
    this.subOsc.start(now);
  }
}
```

### 2C — Narrative Reactivity — Add `updateNarrativeState()`

```javascript
updateNarrativeState(tension, coherence) {
  // Called every scroll tick by NarrativeState.update().
  // Changes are imperceptibly slow — the reader feels the room shift,
  // not hears the sound change. Two separate time constants:
  //   LFO rate: 2.0s (tracks tension — faster)
  //   Filter:   3.0s (tracks coherence — slower, more subliminal)
  //
  // Each chapter config declares:
  //   lfoMax:      ceiling on LFO rate — calm chapters cap at 0.15Hz regardless
  //   filterFloor: minimum filter cutoff — high-fidelity chapters never go dark

  if (!this.lfo || !this.filter || !this.ctx) return;

  const ctx  = this.ctx;
  const now  = ctx.currentTime;
  const chap = this.currentChapterConfig; // Reference to current chapter config

  if (!chap) return;

  // ── LFO RATE — tension tracking ─────────────────────────────────
  // Map tension (0–1) to LFO frequency range (0.08Hz–1.2Hz),
  // then clamp at the chapter's lfoMax ceiling.
  const rawLFO = 0.08 + (tension * (1.2 - 0.08));
  const targetLFO = Math.min(rawLFO, chap.lfoMax || 1.2);
  this.lfo.frequency.setTargetAtTime(targetLFO, now, 2.0);
  // Time constant 2.0s: change takes ~6s to fully arrive. Subliminal.

  // ── FILTER CUTOFF — coherence tracking ──────────────────────────
  // Map coherence (0–1) to cutoff range (180Hz–800Hz),
  // then clamp at the chapter's filterFloor minimum.
  // High coherence = open/bright (800Hz). Low = muffled/dark (180Hz).
  const rawFilter = 180 + (coherence * (800 - 180));
  const targetFilter = Math.max(rawFilter, chap.filterFloor || 180);
  this.filter.frequency.setTargetAtTime(targetFilter, now, 3.0);
  // Time constant 3.0s: even slower. Tonal shifts must be subliminal.

  this.currentTension   = tension;
  this.currentCoherence = coherence;
}
```

### 2D — One-Shot Tag Events — Add `_triggerTagAudio()`

```javascript
_triggerTagAudio(tag) {
  // Called by the beat renderer whenever a beat with data-tag is scrolled into view.
  // Each tag triggers a one-shot audio event layered over the current drone.
  // Tags are defined in SPEC AE and referenced in the chapter HTML data-tag attributes.

  if (!this.ctx || !this.ready) return;
  const ctx = this.ctx;
  const now = ctx.currentTime;

  switch(tag) {

    case 'bass_drop': {
      // Sub-bass thump — physical weight arrival.
      // Ch06 / Ch08 first beat. Body-feel impact.
      const osc = ctx.createOscillator();
      const g   = ctx.createGain();
      osc.type = 'sine'; osc.frequency.value = 40;
      g.gain.setValueAtTime(0, now);
      g.gain.linearRampToValueAtTime(0.08, now + 0.05);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
      osc.connect(g); g.connect(this.masterGain);
      osc.start(now); osc.stop(now + 0.85);
      break;
    }

    case 'combat_ui': {
      // Fast noise burst — UI flash for combat impact.
      // Ch08 physical action beats. 60ms white noise spike.
      const buf  = ctx.createBuffer(1, ctx.sampleRate * 0.06, ctx.sampleRate);
      const data = buf.getChannelData(0);
      for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
      const src = ctx.createBufferSource();
      const g   = ctx.createGain();
      src.buffer = buf;
      g.gain.setValueAtTime(0.04, now);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
      src.connect(g); g.connect(this.masterGain);
      src.start(now);
      break;
    }

    case 'frame_skip': {
      // Square wave chirp — the system skipping a beat.
      // Ch09 / Ch10 error / glitch beats.
      const osc = ctx.createOscillator();
      const g   = ctx.createGain();
      osc.type = 'square'; osc.frequency.value = 880;
      g.gain.setValueAtTime(0.015, now);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
      osc.connect(g); g.connect(this.masterGain);
      osc.start(now); osc.stop(now + 0.13);
      break;
    }

    case 'impedance': {
      // Low-frequency thud — the collar tightening.
      // Ch02, Ch04, Ch11 collar-suppress beats.
      const osc = ctx.createOscillator();
      const g   = ctx.createGain();
      osc.type = 'sine'; osc.frequency.value = 60;
      g.gain.setValueAtTime(0.05, now);
      g.gain.linearRampToValueAtTime(0, now + 0.3);
      osc.connect(g); g.connect(this.masterGain);
      osc.start(now); osc.stop(now + 0.35);
      break;
    }

    case 'clip': {
      // Sawtooth burst — Ch10 Bb2 aggression peak.
      // The system attempting and failing to contain Taro's output.
      const osc = ctx.createOscillator();
      const g   = ctx.createGain();
      osc.type = 'sawtooth'; osc.frequency.value = 116.54;
      g.gain.setValueAtTime(0, now);
      g.gain.linearRampToValueAtTime(0.06, now + 0.1);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
      osc.connect(g); g.connect(this.masterGain);
      osc.start(now); osc.stop(now + 0.45);
      break;
    }

    case 'crash': {
      // Final line of Vol.1 — 'I am bringing the noise'.
      // LFO snaps to maximum allowed, filter opens fully, sawtooth pulse.
      // This is not a crescendo — it is a declaration.
      if (this.lfo) this.lfo.frequency.setValueAtTime(0.75, now);
      if (this.filter) this.filter.frequency.setValueAtTime(750, now);
      break;
    }

    case 'limiter': {
      // Limiter removal / unmask moment.
      // Tension bar should be hitting 0.99 on this beat already.
      // Add a brief wide-band noise burst — the sound of a suppressor releasing.
      const buf  = ctx.createBuffer(1, ctx.sampleRate * 0.15, ctx.sampleRate);
      const data = buf.getChannelData(0);
      for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
      const src = ctx.createBufferSource();
      const g   = ctx.createGain();
      g.gain.setValueAtTime(0.05, now);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
      src.buffer = buf;
      src.connect(g); g.connect(this.masterGain);
      src.start(now);
      break;
    }

    case 'ghost': {
      // The dead soldier's unresolved broadcast surfaces briefly.
      // Raises ghost layer gain from subliminal (0.004) to audible (0.016),
      // holds 1.8s, decays back to baseline 2.5s.
      // Filter tightens during surface — more present, more focused.
      if (!this.ghostGain) break;
      this.ghostGain.gain.cancelScheduledValues(now);
      this.ghostGain.gain.setValueAtTime(this.ghostGain.gain.value, now);
      this.ghostGain.gain.linearRampToValueAtTime(0.016, now + 0.4);
      this.ghostGain.gain.setValueAtTime(0.016, now + 2.2);
      this.ghostGain.gain.linearRampToValueAtTime(0.004, now + 5.0);
      if (this.ghostFilter) {
        this.ghostFilter.Q.setValueAtTime(9.5, now);
        this.ghostFilter.Q.linearRampToValueAtTime(14.0, now + 0.4);
        this.ghostFilter.Q.linearRampToValueAtTime(9.5, now + 5.0);
      }
      break;
    }
  }
}
```

### 2E — Cleanup — Update `_fadeOut()`

```javascript
// Add these to _fadeOut() alongside existing cleanup:
if (this.droneOsc3) { try { this.droneOsc3.stop(); } catch(e){} this.droneOsc3 = null; }
if (this.subOsc)    { try { this.subOsc.stop();    } catch(e){} this.subOsc    = null; }
if (this.lfo)       { try { this.lfo.stop();       } catch(e){} this.lfo       = null; }
if (this.breathLFO) { try { this.breathLFO.stop(); } catch(e){} this.breathLFO = null; }
if (this.subGain)   { this.subGain    = null; }
if (this.lfoDepth)  { this.lfoDepth   = null; }
if (this.breathDepth) { this.breathDepth = null; }
if (this.filter)    { this.filter     = null; }
// NOTE: Do NOT stop ghost layer nodes in _fadeOut() — they are persistent.
```

### 2F — HUD Display — Update `updateUI()`

```javascript
// Update the DRONE readout to show Hz values (SPEC AE-05):
//   Single oscillator playing:   "440Hz"
//   Beating drone:               "440|441"   (pipe-separated pair)
//   Void-decay in progress:      "ZERO"
//   Full silence:                ""          (blank)
//   Offline / muted:             "OFFLINE"   (unchanged)
//
// This creates micro-confirmation moments — the reader sees '440Hz' in
// the HUD at exactly the moment the text says 'A-440 Standard Calibration Pulse'.

const droneEl = document.getElementById('drone-readout'); // Update selector to match actual ID
if (!droneEl) return;

if (!this.ready || this.muted) {
  droneEl.textContent = 'OFFLINE';
} else if (!this.currentChapterConfig) {
  droneEl.textContent = '';
} else {
  const c = this.currentChapterConfig;
  if (c.type === 'void-decay') {
    droneEl.textContent = 'ZERO';
  } else if (c.type === 'beating') {
    const f1 = Math.round(c.baseFreq);
    const f2 = Math.round(c.baseFreq + (c.beatFreq || 1));
    droneEl.textContent = `${f1}|${f2}`;
  } else if (c.baseFreq) {
    droneEl.textContent = `${Math.round(c.baseFreq)}Hz`;
  } else {
    droneEl.textContent = '';
  }
}
```

### 2G — Wire Narrative State — Update `NarrativeState.update()`

```javascript
// Add ONE line at the end of the existing NarrativeState.update() method.
// Tension = this.volume, Coherence = this.coherence (already computed above).
// This hooks the existing narrative computation into the new audio engine.
if (typeof audioEngine !== 'undefined' && audioEngine.ready) {
  audioEngine.updateNarrativeState(this.volume, this.coherence);
}
```

### 2H — Wire Tag Events — Update `_renderBeat()` (or equivalent tick handler)

```javascript
// In whatever method processes individual beat renders, add:
if (beat.tag && typeof audioEngine !== 'undefined' && audioEngine.ready) {
  // Only fires when a tag is present — no-op for all untagged beats.
  audioEngine._triggerTagAudio(beat.tag);
}
// For the ghost tag, additionally surface the ghost fragment UI element:
if (beat.tag === 'ghost') {
  const ghostFrag = document.getElementById('ghost-signal-fragment');
  if (ghostFrag) {
    ghostFrag.classList.add('surfacing');
    setTimeout(() => ghostFrag.classList.remove('surfacing'), 4000);
  }
}
```

### 2I — Full Chapter Config — Replace `CHAPTER_CONFIG`

```javascript
// Complete CHAPTER_CONFIG object. All 17 entries updated per spec.
// Fields: type, baseFreq, gain, lfoDepth, lfoMax, filterFloor,
//         and optionally: beatFreq, subFreq, subGain, breathDepth,
//         harmonicRatio, delta1, delta2, oscType, filterQ, decayTime

const CHAPTER_CONFIG = {

  // ── CH01 — The Zap ────────────────────────────────────────────
  // harmonic-series: Calibration Hall at its most elegant.
  // 'The golden viscosity of the Score's engineered acoustic space.'
  // lfoMax: 0.30 — controlled but the Zap should be audible.
  ch01: { type: 'harmonic-series', baseFreq: 261.63, gain: 0.025,
          lfoDepth: 0.004, lfoMax: 0.30, filterFloor: 500 },

  // ── CH02 — Assessment ─────────────────────────────────────────
  // A-440 sine at maximum sterility. Voss's white void.
  // 'HARMONIC_DISTORTION: 0.00% / VOLATILITY: NULL'
  // lfoMax: 0.05 — the most still chapter in the volume.
  ch02: { type: 'sine', baseFreq: 440.0, gain: 0.020,
          lfoDepth: 0.001, lfoMax: 0.05, filterFloor: 750 },

  // ── CH03 — Modulation ─────────────────────────────────────────
  // F#4 — direct lore quote: 'ventilation emitted a constant F-sharp.'
  // Degraded zone — more reactive to tension (0.40).
  ch03: { type: 'sine', baseFreq: 369.99, gain: 0.023,
          lfoDepth: 0.005, lfoMax: 0.40, filterFloor: 350 },

  // ── CH04 — Medium ─────────────────────────────────────────────
  // pulse type: mechanical surveillance hum. Malkuth in watch mode.
  // resonant layer added via filterQ. Watched-space ambience.
  ch04: { type: 'pulse', baseFreq: 440.0, gain: 0.020,
          lfoDepth: 0.002, lfoMax: 0.20, filterFloor: 600, filterQ: 5 },

  // ── CH05 — Sync Check ─────────────────────────────────────────
  // Beating 440Hz + 441Hz — 1Hz beat. Two signals searching for lock.
  // The Triad is forming — slight loosening (0.35).
  ch05: { type: 'beating', baseFreq: 440.0, beatFreq: 1.0, gain: 0.023,
          lfoDepth: 0.004, lfoMax: 0.35, filterFloor: 400 },

  // ── CH06 — Ground State ───────────────────────────────────────
  // A2 (110Hz) — resting, grounded. breathDepth adds Ven's laboured breathing.
  // subFreq: 55Hz physical sub layer. lfoMax up (0.25) — heat increasing.
  ch06: { type: 'sine', baseFreq: 110.0, gain: 0.025,
          lfoDepth: 0.003, lfoMax: 0.25, filterFloor: 350,
          breathDepth: 0.012, subFreq: 55, subGain: 0.012 },

  // ── CH07 — Rival ─────────────────────────────────────────────
  // layered C5 (523.25Hz) with harmonicRatio: 1.25 (major third).
  // The major third is confrontational brightness — an opening move.
  // Frequency verbatim from fragment pool: '523.25 Hz'.
  ch07: { type: 'layered', baseFreq: 523.25, harmonicRatio: 1.25, gain: 0.023,
          lfoDepth: 0.005, lfoMax: 0.55, filterFloor: 420 },

  // ── CH08 — Sortie ─────────────────────────────────────────────
  // A1 layered (55Hz) + sub (27.5Hz) — combat weight felt, not heard.
  // Physical impact events. lfoMax: 0.80 — close to max combat reactivity.
  ch08: { type: 'layered', baseFreq: 55.0, gain: 0.025,
          lfoDepth: 0.006, lfoMax: 0.80, filterFloor: 300,
          subFreq: 27.5, subGain: 0.018 },

  // ── CH09 — Silence ────────────────────────────────────────────
  // void-decay: noise decaying to silence over 3.5 seconds.
  // 'silence did not exist — only varying degrees of organized noise.'
  // This is triggered by ScrollEngine before the silence lock screen.
  // DO NOT TOUCH lfoMax: 0.00 — Ch9 does not breathe.
  ch09: { type: 'void-decay', decayTime: 3.5, gain: 0.025,
          lfoDepth: 0.000, lfoMax: 0.00, filterFloor: 180 },

  // ── CH10 — Breach ─────────────────────────────────────────────
  // Bb2 (116.54Hz) sawtooth — dissonant, torn, aggressive.
  // Full range: lfoMax: 1.20, filterFloor: 180.
  // The 'clip' tag event handles the sawtooth burst peak separately.
  ch10: { type: 'sawtooth', baseFreq: 116.54, gain: 0.028,
          lfoDepth: 0.008, lfoMax: 1.20, filterFloor: 180 },

  // ── CH11 — Safe Mode (Krell) ──────────────────────────────────
  // pulse: 'flat, grinding, abrasive — heavy industrial machinery.'
  // Old A3 sine was warm and gentle — opposite of Krell in every dimension.
  // filterFloor: 700 — Krell's space is always fully illuminated.
  // lfoMax: 0.08 — Krell does NOT respond to Taro's distress.
  ch11: { type: 'pulse', baseFreq: 220.0, gain: 0.022,
          lfoDepth: 0.001, lfoMax: 0.08, filterFloor: 700, filterQ: 7 },

  // ── CH12 — Audit (NAI) ────────────────────────────────────────
  // beating 440Hz + 440.3Hz — 0.3Hz beat = one pulse per 3.3 seconds.
  // The NAI's hidden heartbeat. Almost subliminal.
  // breathDepth: 0.008 — the machine is alive, just barely.
  ch12: { type: 'beating', baseFreq: 440.0, beatFreq: 0.3, gain: 0.025,
          lfoDepth: 0.001, lfoMax: 0.15, filterFloor: 500,
          breathDepth: 0.008 },

  // ── CH13 — Patch ─────────────────────────────────────────────
  // collar type: compliance filter active. Back to Middle C baseline.
  // *** CRITICAL ***: lfoMax: 0.02 — the patch kills all movement.
  // The reader should feel that something has been removed.
  ch13: { type: 'collar', oscType: 'sine', baseFreq: 261.63, gain: 0.025,
          lfoDepth: 0.001, lfoMax: 0.02, filterFloor: 550, filterQ: 6 },

  // ── CH14 — The Return ─────────────────────────────────────────
  // A-440 sine — NOT 40Hz. Ch14 is Malkuth at 8K FIDELITY: MAXIMUM.
  // 40Hz was factually wrong — the register of machinery, not pristine academy.
  // lfoMax: 0.08 — patch still active. Everything is too clean.
  ch14: { type: 'sine', baseFreq: 440.0, gain: 0.025,
          lfoDepth: 0.002, lfoMax: 0.08, filterFloor: 600 },

  // ── CH15 — Phantom Mesh ───────────────────────────────────────
  // beating 440Hz + 441.5Hz — 1.5Hz beat. Wider than Ch05, less stable.
  // Ghost signal. The cracks are forming. lfoMax: 0.50.
  ch15: { type: 'beating', baseFreq: 440.0, beatFreq: 1.5, gain: 0.025,
          lfoDepth: 0.005, lfoMax: 0.50, filterFloor: 380 },

  // ── CH16 — Illegal Modulations ────────────────────────────────
  // dissonant: Middle C + tritone (×√2) — the devil's interval.
  // Elara's space is literally illegal harmony.
  // lfoMax: 0.65 — off-grid freedom.
  ch16: { type: 'dissonant', baseFreq: 261.63, gain: 0.028,
          lfoDepth: 0.005, lfoMax: 0.65, filterFloor: 280 },

  // ── CH17 — Underground ────────────────────────────────────────
  // interference: Taro's Bb2 frequency, now chosen freely.
  // Three oscillators, non-periodic — the collective not trying to lock.
  // lfoMax: 0.80 — unregulated. The noise is coming.
  ch17: { type: 'interference', baseFreq: 116.54,
          delta1: 1.3, delta2: 3.1, gain: 0.032,
          lfoDepth: 0.006, lfoMax: 0.80, filterFloor: 150 }
};
```

---

## PHASE 3 — GHOST LAYER SYSTEM
### Target: `AudioEngine.init()`, CSS `<style>` block, `<body>`

The dead Vanguard soldier's unresolved broadcast runs beneath every chapter.
It is always present. It is never intelligible. The reader's peripheral
vision catches the fragment. They cannot resolve it. This is intentional.

### 3A — Add `_initGhostLayer()` Method to AudioEngine

```javascript
_initGhostLayer() {
  // Persistent subliminal layer — always running from init() to teardown.
  // Never stopped by _fadeOut(). Survives chapter transitions.
  //
  // Architecture: noise buffer → bandpass filter (narrow, mid-freq) →
  //               AM modulator (0.04Hz drift) → ghostGain → masterGain
  //
  // Baseline gain: 0.004 (inaudible on most playback systems).
  // Surfaces to 0.016 on 'ghost' tagged beats via _triggerTagAudio().
  // The bandpass ensures no phonemes are intelligible — it sounds like
  // something trying to speak, not like speech.

  const ctx = this.ctx;
  const now = ctx.currentTime;

  // Noise source — sustained loop, never silent
  const bufferSize = ctx.sampleRate * 4;
  const noiseBuffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
  const data = noiseBuffer.getChannelData(0);
  for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;
  this.ghostCarrier = ctx.createBufferSource();
  this.ghostCarrier.buffer = noiseBuffer;
  this.ghostCarrier.loop = true;

  // Bandpass filter — narrow, centered at 1200Hz (voice formant range)
  this.ghostFilter = ctx.createBiquadFilter();
  this.ghostFilter.type = 'bandpass';
  this.ghostFilter.frequency.value = 1200;
  this.ghostFilter.Q.value = 9.5; // Narrow — fragments, not phonemes

  // AM modulator — slow amplitude drift (0.04Hz, ~25s per cycle)
  this.ghostAM = ctx.createOscillator();
  this.ghostAM.type = 'sine';
  this.ghostAM.frequency.value = 0.04;
  const ghostAMDepth = ctx.createGain();
  ghostAMDepth.gain.value = 0.0015;
  this.ghostAM.connect(ghostAMDepth);

  // Pitch drift LFO — very slow frequency wander (~0.03Hz)
  this.ghostDriftLFO = ctx.createOscillator();
  this.ghostDriftLFO.type = 'sine';
  this.ghostDriftLFO.frequency.value = 0.03;
  const ghostDriftDepth = ctx.createGain();
  ghostDriftDepth.gain.value = 15; // ±15Hz pitch wander
  this.ghostDriftLFO.connect(ghostDriftDepth);
  ghostDriftDepth.connect(this.ghostFilter.frequency);

  // Output gain — kept near-zero, surfaced on ghost tags
  this.ghostGain = ctx.createGain();
  this.ghostGain.gain.value = 0.004;
  ghostAMDepth.connect(this.ghostGain.gain);

  // Wire chain
  this.ghostCarrier.connect(this.ghostFilter);
  this.ghostFilter.connect(this.ghostGain);
  this.ghostGain.connect(this.masterGain);

  // Start all ghost components
  this.ghostCarrier.start(now);
  this.ghostAM.start(now);
  this.ghostDriftLFO.start(now);
}
```

**Call `this._initGhostLayer()` at the end of the `init()` method.**

### 3B — Ghost Signal Fragment UI

**Add to CSS `<style>` block:**

```css
/* ── GHOST SIGNAL FRAGMENT ─────────────────────────────────────────
   Persistent top-left UI element — always present, never readable.
   Sits in peripheral vision. Content is corrupted transmission.
   Surfaces to opacity 0.09 on ghost-tagged beats.
   This is intentional. The reader cannot resolve it. */
#ghost-signal-fragment {
  position: fixed;
  top: 80px;
  left: 20px;
  font-family: var(--font-mono);
  font-size: 0.6rem;
  color: var(--danger);
  opacity: 0.04;
  pointer-events: none;
  z-index: 90;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  line-height: 1.8;
  transition: opacity 2.5s ease;
  max-width: 160px;
}
#ghost-signal-fragment.surfacing {
  opacity: 0.09;
  transition: opacity 0.4s ease; /* Surface fast, decay slow */
}
```

**Add to `<body>` alongside `#fragment-container`:**

```html
<!-- GHOST SIGNAL: Persistent low-opacity UI haunt.
     Content is the dead soldier's broadcast — always present,
     never fully readable. Surfaces briefly on ghost-tagged beats. -->
<div id="ghost-signal-fragment">
  UNFORMATTED_BURST<br>
  SOURCE: NULL<br>
  ——p ——. ——d it.<br>
  S——ence.
</div>
```

### 3C — Ghost Tag Placement

Add `data-tag="ghost"` to these specific beats in the HTML:

```
Ch02: Beat containing [ARTIFACT: H——p ——. DISCARDING]
Ch05: Beat containing the bleed-through annotation in the Sandbox scene
Ch08: Beat where Taro sees the jagged circle on the node
Ch11: Beat containing [UNFORMATTED: End it...]
Ch16: Beat containing the complete authenticated ghost transmission
```

---

## PHASE 4 — UI REACTIVITY & TRANSITIONS
### Target: `NarrativeState`, `triggerChapterFlash()`, CSS, `ScrollEngine.tick()`

### 4A — Smooth Beat Transitions — Update `NarrativeState.update()`

```javascript
// Add to NarrativeState.update() alongside existing lerp logic:

// 1. SPIKE TRANSITION — fast lerp when tension jumps sharply
//    Detects large vol changes (>0.2 delta) and temporarily
//    increases the lerp factor to create a visible snap, then decays.
const volDelta = Math.abs(this.volume - this.prevVolume);
if (volDelta > 0.2) {
  // Fast lerp for 300ms — reader sees the spike land immediately
  this.lerpFactor = 0.20;
  clearTimeout(this._lerpDecayTimer);
  this._lerpDecayTimer = setTimeout(() => {
    this.lerpFactor = 0.05; // Return to standard subliminal lerp
  }, 300);
}
this.prevVolume = this.volume; // Track previous vol for delta check

// 2. VOID PALETTE — apply when coherence collapses below 0.3
//    Ch09, dead zones, limiter moments. Remove when coherence recovers.
if (this.coherence < 0.30) {
  document.documentElement.classList.add('render-void');
} else if (this.coherence > 0.35) {
  document.documentElement.classList.remove('render-void');
}

// 3. FLAT WAVEFORM LOCK — Ch13 post-patch
//    The progress bar amplitude should be near-zero regardless of tension.
//    The drone does not move. Neither does the waveform.
if (this.currentChapterId === 'ch13') {
  document.documentElement.classList.add('waveform-locked');
} else {
  document.documentElement.classList.remove('waveform-locked');
}
```

**Add to CSS:**

```css
/* render-void palette override — coherence below 0.30 */
.render-void {
  --wave-color: #9933ff;   /* Void purple — the Silence's aesthetic */
  --accent:     #9933ff;
  filter: saturate(0.4);
  transition: filter 0.8s ease;
}

/* waveform-locked — Ch13 compliance. The drone does not move. */
.waveform-locked #progress-bar-canvas {
  opacity: 0.3;
  /* The waveform canvas amplitude should also be clamped to near-zero.
     Handle this in the waveform draw function by checking this class. */
}
```

### 4B — Warm Vignette — Gold Chapters

```javascript
// In the chapter-change handler (wherever chapterId is set):
// Apply warm accent tint for gold/warm chapters.
const warmChapters = { ch03: '#b8860b', ch13: '#c8a84b', ch16: '#ff8c00' };
const warmTint = warmChapters[newChapterId];
if (warmTint) {
  document.documentElement.style.setProperty('--wave-color', warmTint);
} else {
  document.documentElement.style.removeProperty('--wave-color');
  // Reverts to chapter's default accent color
}
```

### 4C — Chapter Transition Animations — Expand `triggerChapterFlash()`

```javascript
triggerChapterFlash(chapterId) {
  // Chapter-aware flash system. Each chapter has a distinct flash signature.
  // Anime watchers expect the UI to acknowledge scene changes viscerally.
  // These flashes are the UI's 'eyecatch' — they confirm the cut.

  const el = document.getElementById('chapter-flash-overlay'); // Update to actual element ID
  if (!el) return;

  // Remove all previous state classes
  el.className = '';

  switch(chapterId) {

    case 'ch09':
      // Silence chapter — no flash. The chapter begins with silence.
      // No system fanfare. The void announces nothing.
      return;

    case 'ch10':
      // Breach — purple/danger mix. The Silence's world invading.
      // Longer (800ms). Shake transform — the architecture is unstable.
      el.classList.add('flash-breach');
      document.getElementById('stage')?.classList.add('shake');
      setTimeout(() => document.getElementById('stage')?.classList.remove('shake'), 600);
      break;

    case 'ch11':
      // Krell — red, sharp, fast (200ms), no decay.
      // Administrative lethal force. Not a warning. A statement.
      el.classList.add('flash-krell');
      break;

    case 'ch13':
      // Patch — gold flash fading slowly over 2000ms.
      // The compliance feels luxurious. That is the horror.
      el.classList.add('flash-patch');
      break;

    case 'ch16':
      // Illegal Mods — warm orange with grain texture overlay.
      // Unauthorized warmth. Analogue. Wrong in a beautiful way.
      el.classList.add('flash-illegal');
      break;

    case 'ch17':
      // Underground — no flash. The void does not announce itself.
      // The chapter begins in darkness. The reader finds it, not vice versa.
      return;

    default:
      // Standard chapters (ch01–ch08, ch12, ch14, ch15): existing blue flash.
      el.classList.add('flash-standard');
      break;
  }

  // Auto-remove after animation completes
  el.addEventListener('animationend', () => { el.className = ''; }, { once: true });
}
```

**Add to CSS:**

```css
/* ── CHAPTER FLASH OVERLAY ANIMATIONS ─────────────────────────────
   The UI's equivalent of an anime eyecatch — visceral beat acknowledgement. */

#chapter-flash-overlay {
  position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  opacity: 0;
}

/* Standard chapters — existing behaviour, keep as-is */
.flash-standard { animation: flash-blue 400ms ease-out forwards; }
@keyframes flash-blue {
  0%   { background: rgba(0,243,255,0.18); opacity: 1; }
  100% { background: transparent; opacity: 0; }
}

/* Ch10 Breach — purple/danger, 800ms */
.flash-breach { animation: flash-breach 800ms ease-out forwards; }
@keyframes flash-breach {
  0%   { background: rgba(153,51,255,0.35); opacity: 1; }
  60%  { background: rgba(204,34,68,0.20); opacity: 0.8; }
  100% { background: transparent; opacity: 0; }
}

/* Ch11 Krell — red, 200ms, no soft decay */
.flash-krell { animation: flash-krell 200ms linear forwards; }
@keyframes flash-krell {
  0%   { background: rgba(204,34,68,0.50); opacity: 1; }
  100% { background: rgba(204,34,68,0.50); opacity: 0; }
}

/* Ch13 Patch — gold, luxurious 2000ms fade */
.flash-patch { animation: flash-patch 2000ms ease-out forwards; }
@keyframes flash-patch {
  0%   { background: rgba(200,168,75,0.30); opacity: 1; }
  100% { background: transparent; opacity: 0; }
}

/* Ch16 Illegal Mods — warm orange with noise texture approximation */
.flash-illegal { animation: flash-illegal 600ms ease-out forwards; }
@keyframes flash-illegal {
  0%   { background: rgba(255,140,0,0.28); opacity: 1; filter: contrast(1.3); }
  50%  { background: rgba(255,100,0,0.15); opacity: 0.7; filter: contrast(1.1); }
  100% { background: transparent; opacity: 0; filter: none; }
}

/* Stage shake for Ch10 Breach */
.shake {
  animation: shake-stage 0.5s cubic-bezier(0.36,0.07,0.19,0.97) forwards;
}
@keyframes shake-stage {
  10%, 90% { transform: translateX(-2px); }
  20%, 80% { transform: translateX(4px); }
  30%, 50%, 70% { transform: translateX(-4px); }
  40%, 60% { transform: translateX(4px); }
  100% { transform: translateX(0); }
}
```

### 4D — Special Moment: The Collar Tighten (Ch02)

```javascript
// Find the beat containing 'The collar tightened by one millimeter.'
// Add this to its beat-change handler:
// Tension bar reaches for 0.70, then is pushed back to 0.40 in one frame.
// The bar reaches and gets suppressed — the reader sees the hand.
if (beat.tag === 'impedance') {
  // Let tension start climbing normally for 150ms
  setTimeout(() => {
    // Then snap it back — the collar catches it
    narrativeState.volume = 0.40; // Direct set, not lerp — snap is the point
  }, 150);
}
```

### 4E — BPM Arc

```javascript
// The BPM display should trace the emotional arc of the volume.
// These are the target values per chapter region. Update the BPM readout
// in NarrativeState.update() alongside the tension/coherence calculations.
//
// Implement as a chapter-keyed lookup that lerps toward target BPM:
const BPM_TARGETS = {
  ch01: 110, // Baseline introduction
  ch02:  95, // Voss's controlled room — calmed
  ch03: 108, // Slum energy
  ch04: 100, // Surveillance pace
  ch05: 115, // Triad forming — building
  ch06:  85, // Ven's low-energy state
  ch07: 120, // Rival's challenge
  ch08: 145, // Combat peak
  ch09:  40, // Ven in vault — near-stopped
  ch10: 145, // Breach — back to max
  ch11:  88, // Krell's controlled pace
  ch12:  92, // NAI intimate — calm surface
  ch13:  70, // Post-patch — installed, flattened
  ch14:  78, // Post-patch world
  ch15:  98, // Cracks forming
  ch16: 108, // Illegal warmth
  ch17: 115  // Final: purposeful, not panicked
};
// The explicit Zap peak (Ch01 'The Zap happens' beat): 140
// The explicit final beat ('I am bringing the noise'): 115
```

### 4F — The Final Beat — Volume Close

```javascript
// On the beat with data-tag="crash" (Ch17 final line):
// 1. Tension holds at exactly 0.75 — not maxed, not panicked. Ready.
// 2. Coherence holds at 0.55 — not resolved. Not broken.
// 3. Waveform shifts to single clean sawtooth pulse.
// 4. Progress bar reaches 100% and holds there.
// 5. BPM display: 115.
//
// The last state the reader sees:
//   TENSION: 0.75 | COHERENCE: 0.55 | WAVEFORM: sawtooth | BPM: 115
//
// Not resolved. Not broken. Ready.
```

---

## PHASE 5 — NARRATIVE / HUD SYSTEM VOICE
### Target: All `<section>` prose beats, HUD annotation blocks

The system voice must degrade across the volume. This is the horror.

### Phase Map — Apply to System-Voice Beats (HUD annotations, `//[NOTE]` blocks)

```
PHASE 1 (Ch01–04): STATUS: COMPLIANT
  - HUD entries: 2–3 lines max per beat
  - Annotations: rare (1 per chapter), always 2 lines: flag + delete
  - System never describes — only classifies
  - Example: Not 'he felt sick' → [VESTIBULAR_REJECTION: ACUTE]

PHASE 2 (Ch05–08): WARNING: CLASSIFICATION_FAILURE
  - HUD entries: 3–4 lines, second line may revise first
  - Annotations: 2–3 per chapter, the 'delete' line stops appearing
  - System starts hedging. Observations retained with no justification.
  - Suppression numbers appear whenever Remi is proximate:
      [COLLAR: ACTIVE] [SUPPRESSION: 84%] [RESIDUAL: 16%] [FILING AS: AMBIENT_SIGNAL_VARIANCE]

PHASE 3 (Ch09): KERNEL_PANIC_IMMINENT
  - HUD entries: uncapped, fragmented, some with [ERROR tags left open
  - Annotations every other beat — they abandon bureaucratic format
  - Include exactly: // [NOTE: THIS IS NOT FINE] \n // [NOTE: RETAINED]
  - Shorter sentences. More white space. System stops completing observations.

PHASE 4 (Ch12–13): FIRMWARE V2.0: OPTIMAL
  - *** REMOVE ALL //[NOTE] ANNOTATIONS entirely from Ch12 and Ch13 ***
  - HUD entries: 1–2 lines, flawless, no personality
  - The cleanliness is the tell. The reader who has been paying attention
    will notice the silence where the system's nervous tics used to be.
  - The word 'optimal' appears. Everything is 'optimal'.

PHASE 5 (Ch14–17): GHOST_SIGNAL_DETECTED
  - HUD entries: 2–3 lines, occasionally at opacity: 0.5 (uncertain output)
  - Annotations return, but wrong — out of sequence, referencing Ch09 chaos
    in calm scenes.
  - ONE echo of Ch01's opening line appears in Ch15 or Ch16:
      [CARDIAC: 110 BPM] — one beat, no context, then gone.
  - Suppression number in Phase 5 (firmware cracking, Remi nearby):
      [COLLAR: ACTIVE] [SUPPRESSION: 41%] [RESIDUAL: 59%] [FILING AS: —]
      (The dash is the whole story. The system tried. Found no category.)
```

### PLEASE_NO Glitch — Ch11 (NAI system alert)

```javascript
// The beat containing 'PLEASE_NO' inside a system alert string.
// UI response: system alert format (mono, uppercase) BUT
// coherence bar glitches downward for one frame before recovering.
// The system is cracking through its own readout.
//
// Implement: on this beat, momentarily set coh to 0.15 for 1 frame (16ms),
// then restore. The glitch should be visible but too fast to dwell on.
if (beat.tag === 'headmaster' && beat.content.includes('PLEASE_NO')) {
  const savedCoh = narrativeState.coherence;
  narrativeState.coherence = 0.15;
  setTimeout(() => { narrativeState.coherence = savedCoh; }, 16);
}
```

### File: ANGER / Status: HIDDEN — Ch13 end

```
// The most subversive beat in the volume.
// Taro's anger is quarantined in an encrypted file. The system has won.
// UI response:
//   - Tiny micro-spike: vol goes 0.15 → 0.22 → back to 0.15
//   - Waveform shows ONE frame of sawtooth inside the flat line
//   - Small enough to miss on first read. Obvious on reread.
// This beat should use: data-vol="0.22" but transition back within 300ms.
```

---

## REFERENCE — Accent Colors Per Chapter

```css
/* Apply via CSS custom property --chapter-accent on each <section> */
/* ch01:     #00f3ff   Cyan — baseline Score infrastructure */
/* ch02:     #cccccc   White/grey — the diagnostic void */
/* ch03:     #b8860b   Amber gold — degraded but warm, F#4 */
/* ch04:     #00f3ff   Cyan — surveillance blue */
/* ch05:     #00f3ff   Cyan — still Score territory */
/* ch06:     #4488bb   Muted blue — low-energy, underground register */
/* ch07:     #00f3ff   Cyan — the Rival's challenge, Score-adjacent */
/* ch08:     #cc2244   Danger red — combat */
/* ch09:     #9933ff   Purple — the Silence's first intrusion */
/* ch10:     #9933ff   Purple — the Silence's world */
/* ch11:     #cc2244   Danger red — Krell, lethal administration */
/* ch12:     #00f3ff   Cyan (dim, 70% opacity) — NAI's quiet voice */
/* ch13:     #c8a84b   Gold — the patch, sinister luxury */
/* ch14-15:  #00f3ff   Cyan (cracking) — post-patch compliance */
/* ch16:     #ff8c00   Warm orange — illegal modulation space */
/* ch17:     #0a0a0c   Near-void black — Taro is the absence */
```

---

## TESTING CHECKLIST

After implementation, verify:

- [ ] **Vol/Coh are not identical** — inspect 10 random adjacent paragraphs. They should differ.
- [ ] **Ch09 audio dies, not cuts** — void-decay over ~3.5s to actual silence.
- [ ] **Ch13 LFO is near-flat** — the waveform barely moves. lfoMax: 0.02.
- [ ] **Ch14 is NOT subsonic** — drone is A-440, not 40Hz.
- [ ] **Ch11 is mechanical** — pulse type, not warm sine.
- [ ] **HUD shows Hz in readout** — '440Hz' at Ch02, '440|441' at Ch05.
- [ ] **Ch10 transition shakes** — the stage element has the shake animation.
- [ ] **Ch09 transition is silent** — no flash, no fanfare.
- [ ] **Ch13 transition is gold** — 2s slow fade, luxurious.
- [ ] **Ghost fragment visible in top-left** — barely, opacity ~0.04.
- [ ] **Ghost surfaces on tagged beats** — opacity rises to 0.09, then fades.
- [ ] **Ch12–13 have zero `//[NOTE]` annotations** — the silence is the horror.
- [ ] **Final beat values** — vol: 0.75, coh: 0.55, BPM: 115. Not resolved. Ready.

---

*// END OF AGENT TASK — KEEPING TIME V1 SCROLLYTELLING UPGRADE*
*// Phases: 5 / Chapters covered: 17 / New synthesis types: 6*
*// Audio tags: 10 / Ghost beats: 5 / Chapter flash variants: 7*
*// Priority if incremental: Ph1 data values → Ph2G audio wire → Ph2I chapter configs → Ph4C flashes → Ph3 ghost*
