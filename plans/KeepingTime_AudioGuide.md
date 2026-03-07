# SIGNAL TRANSMISSION GUIDE
### Keeping Time — Volume One
#### Audio Engine Update Specification

*drone architecture · lfo arc · filter shaping · one-shot events · new synthesis types*

---

## 01 — The Model

The audio engine is the Score made audible. It should not accompany the story — it should *be* the story's infrastructure, running beneath the reader's conscious attention. Every drone frequency, filter shape, and LFO rate is a direct translation of what the lore describes happening in the physical world of the Soundscape.

The engine currently makes several correct decisions (Ch3's F#4, Ch9's void-decay, Ch16's tritone) and several factually wrong ones (Ch11's gentle sine for Krell, Ch14's industrial subsonic for Malkuth Academy at 8K render). This guide fixes the mismatches and adds the reactive layer that is currently missing entirely: audio that responds to specific tagged beats, not just chapter transitions.

### The Audio Arc

The volume has one overarching audio trajectory:

```
REGULATED → PRESSURISED → BROKEN → SUPPRESSED → CRACKING OPEN
```

This should be audible in the LFO behaviour alone. Chapters 1–4 breathe slowly and evenly. Chapters 5–8 breathe faster as Taro gains power. Chapter 9 stops breathing entirely. Chapter 10 is uncontrolled noise. Chapter 13 flatlines — the patch is the most still drone in the volume. Chapters 14–17 slowly, unevenly, begin to breathe again.

If you read nothing else in this guide, read §04 — The LFO Arc. It is the single highest-value change.

### Engine Capabilities (Current)

| TYPE | OSCILLATORS | USE |
|---|---|---|
| `sine` | 1 | Standard Score baseline |
| `square` | 1 | Surveillance, hard compliance |
| `sawtooth` | 1 | Dissonance, aggression, breach |
| `layered` | 2 (fundamental + octave) | Dense signal, Vanguard weight |
| `beating` | 2 (freq + freq+Δ) | Phase searching, sync uncertainty |
| `dissonant` | 2 (freq + freq×√2) | Tritone, forbidden interval |
| `chord` | 2 (freq + freq×1.5) | Perfect fifth, consonance |
| `crackle` | noise buffer | Off-grid, no Score signal |
| `void-decay` | noise buffer → silence | Ch9 only — the Score dying |

Sub-bass layer (`subFreq`), LFO tremolo, and coherence-reactive lowpass filter available on all types.

---

## 02 — What's Right, What's Wrong

### Already Well-Matched

**Ch3 — F#4 (369.99Hz) with detune spread.**
The text states: *"The ventilation system emitted a constant sequence at F-sharp."* The F#4 drone is a direct lore quote. The slight detune spread adds the analogue warmth of a degraded signal environment. Keep exactly as-is.

**Ch5 — Beating 440Hz + 441Hz (1Hz beat).**
Models two signals searching for phase lock. The 1-cycle-per-second amplitude pulse is slow and uncertain — the Triad hasn't formed yet. Correct concept. The only change needed is a *resolution event* when the `SYNC_STATUS: GREEN` beat lands (see §05).

**Ch8 — Layered 55Hz + sub 27.5Hz.**
Combat weight felt in the body, not heard as pitch. The text describes physical impact events — Ven hitting pipes, running through hostile architecture. This is the right physical register. Keep.

**Ch9 — void-decay.**
The single best audio decision in the file. White noise decaying to true silence over 3.5 seconds. The text: *"silence did not exist — only varying degrees of organized noise."* The void-decay type makes that line audible. Do not touch.

**Ch10 — Bb2 (116.54Hz) sawtooth.**
Dissonant, torn, aggressive. Widest reactivity range in the volume (`lfoMax: 1.2`). The sawtooth waveform is Taro's true signal shape — jagged, uncompressed, wrong. Correct. The only addition needed is the one-shot limiter-snap event (see §05).

**Ch16 — Dissonant (Middle C + tritone √2).**
The historically forbidden interval — *diabolus in musica*. Elara's underground modulation space is literally illegal harmony. This is the most musically literate decision in the engine. Keep.

---

### Mismatches — Ordered by Severity

#### CRITICAL — Ch13 `lfoMax: 0.25`

**What's there:** `chord` type, Middle C + perfect fifth, `lfoMax: 0.25`.

**What's wrong:** The patch suppresses everything. Taro's anger is encrypted and archived. His emotional reactivity is near-zero. An `lfoMax` of 0.25 is indistinguishable from the normal chapters. The drone breathes with the same variability as a calibration hall. The reader should hear that something has been removed.

**What it should be:** `lfoMax: 0.02`. The smallest non-zero value. The drone is technically alive but does not move. This single value change is the most narratively significant audio fix in the entire update.

---

#### CRITICAL — Ch11 `sine` for Krell

**What's there:** A3 (220Hz) sine, `lfoDepth: 0.002`.

**What's wrong:** The text's description of Krell: *"the flat, grinding, abrasive tone of heavy-duty industrial machinery."* A sine wave at A3 is warm, gentle, and mathematically smooth — the opposite of Krell in every dimension.

**What it should be:** Square wave or narrow-bandwidth pulse. High-Q resonant filtering (Q=6–8) that gives it a hollow, mechanical edge. `filterFloor: 700` so it stays bright and hard. `lfoMax: 0.08` — Krell doesn't breathe. He operates.

---

#### HIGH — Ch14 subsonic drone for Malkuth Academy at 8K render

**What's there:** 40Hz sine + 20Hz sub, `filterFloor: 300`.

**What's wrong:** Ch14 is the post-patch return to Malkuth. The opening line: *"FIDELITY: MAXIMUM [8K_RENDER] / ONLINE_AND_OPTIMAL."* This is the most visually perfect environment in the volume. 40Hz is a subsonic industrial rumble — the register of machinery, basements, and Grounding Vaults. It belongs in Ch6, not in a pristine high-fidelity academy.

**What it should be:** Back toward A-440, high filterFloor, minimal LFO. Something that sounds expensive and synthetic. The compliance patch has been installed. Everything is too clean. The audio should reinforce that wrongness by being acoustically flawless.

---

#### HIGH — Ch12 NAI heartbeat missing

**What's there:** A-440 sine, `lfoDepth: 0.001`, barely reactive.

**What's wrong:** Ch12 is the NAI's intimate narration — the system's internal voice revealing it has feelings. The drone should model *consciousness underneath machinery*. Something alive but hidden. The current drone is indistinguishable from Ch2's administrative void.

**What it should be:** `beating` type, 440Hz + 440.3Hz, `beatFreq: 0.3`. One amplitude pulse every 3.3 seconds — a heartbeat at the edge of perception. Almost subliminal. The reader should feel rather than hear that something is breathing inside the machine.

---

#### MEDIUM — Ch7 Rival lacks confrontational register

**What's there:** C5 (523.25Hz) sine, `lfoDepth: 0.005`.

**What's partially wrong:** The frequency is correct — directly from the fragment pool. But a plain sine doesn't carry the Rival's challenge. The Rival's energy is *competitive brightness* — the sound of a gauntlet being thrown, not a threat.

**What it should be:** `layered` type with a major third harmonic (5:4 ratio = 654Hz) instead of the standard octave. The major third is the interval of brightness and assertion. It makes C5 feel like an opening move rather than just a tone.

---

#### MEDIUM — Ch2 Assessment too warm for the white void

**What's there:** A-440 sine, `lfoMax: 0.15`, `filterFloor: 600`.

**What's partially wrong:** Voss's spec: `HARMONIC_DISTORTION: 0.00%` / `VOLATILITY: NULL`. The current drone has the same frequency as Ch4 and Ch12, making the diagnostic void feel like just another institutional space. It should feel like the absence of all acoustic character — a reference tone in a room with no reflections.

**What it should be:** Same A-440 sine but `lfoMax: 0.05`, `filterFloor: 750`, `lfoDepth: 0.001`. The most still, controlled, high-frequency drone in the volume. The white void should be acoustically sterile. Voss is the only object in it.

---

## 03 — New Synthesis Types

Six new `type` values to add to the `_startDrone()` switch block. Each solves a specific narrative problem.

---

### `pulse`

**What it is:** Square wave oscillator with asymmetric `WaveShaperNode` clipping — effectively a narrow duty-cycle pulse (~20% on, 80% off). Hollow and mechanical rather than the full-bandwidth aggression of a standard square.

**What it models:** Electronic monitoring equipment. The specific hum of surveillance infrastructure. The sound of a system that is watching you with complete indifference.

**Use for:** Ch4 (The Medium), Ch11 (Krell's interrogation room).

**Implementation:**
```javascript
// pulse type: square oscillator + asymmetric waveshaper
// Creates the narrow duty-cycle hollow hum of surveillance hardware.
// The WaveShaperNode clips the square wave's negative side harder
// than the positive, producing an asymmetric pulse that reads as
// mechanical and indifferent rather than musical.
this.droneOsc = ctx.createOscillator();
this.droneOsc.type = 'square';
this.droneOsc.frequency.value = config.baseFreq;

const pulseShaper = ctx.createWaveShaper();
const curve = new Float32Array(256);
for (let i = 0; i < 256; i++) {
  const x = (i * 2) / 256 - 1;
  // Clip negative harder (0.3) than positive (0.9) — asymmetric pulse
  curve[i] = x >= 0 ? Math.min(x * 0.9, 0.85) : Math.max(x * 0.3, -0.25);
}
pulseShaper.curve = curve;
this.droneOsc.connect(pulseShaper);
pulseShaper.connect(this.filter);
this.droneOsc.start(now);
```

**Config example (Ch11):**
```javascript
"drone": {
  "type": "pulse",
  "baseFreq": 220,       // A3 — same pitch, completely different character
  "gain": 0.022,
  "lfoDepth": 0.001,     // Krell barely breathes
  "lfoMax": 0.08,        // Does not respond to tension with warmth
  "filterFloor": 700,    // Stays hard and bright
  "filterQ": 7           // High-Q resonance — mechanical edge
}
```

---

### `resonant`

**What it is:** Sine oscillator fed through a very high-Q (Q=8–12) bandpass filter that almost self-oscillates. Produces a narrow, ringing, sibilant tone — the characteristic frequency of a room that knows you're in it.

**What it models:** Surveillance environment ambience. The sound of monitored space — not the monitor itself, but the *air* in the room it watches.

**Use for:** Ch4 (Malkuth Academy social ranking floor), Ch11 (secondary layer under the pulse drone).

**Implementation:**
```javascript
// resonant type: sine through near-self-oscillating bandpass.
// High Q (8–12) makes the filter ring at its own frequency,
// adding a sibilant surveillance hum on top of the base tone.
// Models the acoustic character of a monitored space —
// not the watcher, but the watching itself.
this.droneOsc = ctx.createOscillator();
this.droneOsc.type = 'sine';
this.droneOsc.frequency.value = config.baseFreq;
this.droneOsc.connect(this.filter);
this.droneOsc.start(now);

// Override the main filter with high-Q bandpass
this.filter.type = 'bandpass';
this.filter.frequency.value = config.baseFreq;
this.filter.Q.value = config.filterQ || 9;
```

---

### `collar`

**What it is:** Any oscillator type with a tight bandpass filter (Q=5–8, bandwidth ~2 semitones) replacing the standard lowpass. Cuts the highs and the lows — only a thin slice of the drone's natural spectrum passes through.

**What it models:** The damping bands and collar hardware. Taro's own signal heard from the inside after suppression — full-spectrum awareness squeezed through a narrow compliance window. The drone type stays the same but the filter architecture changes to model restriction.

**Use for:** Ch13 (post-patch chapters — the compliance filter is active).

**Implementation:**
```javascript
// collar type: standard oscillator (type specified in config.oscType)
// passed through a tight bandpass that removes the fundamental's
// natural harmonic richness, leaving only the 'allowed' frequency band.
// Models hardware suppression — not silence, but constrained signal.
// The underlying tone is still present; the compliance layer just
// removes everything that makes it expressive.
this.droneOsc = ctx.createOscillator();
this.droneOsc.type = config.oscType || 'sine';
this.droneOsc.frequency.value = config.baseFreq;
this.droneOsc.connect(this.filter);
this.droneOsc.start(now);

// Override main filter to tight bandpass
this.filter.type = 'bandpass';
this.filter.frequency.value = config.baseFreq;
this.filter.Q.value = config.filterQ || 6;
// Note: coherence-reactivity still applies via updateNarrativeState(),
// but with a tight bandpass the movement is almost imperceptible —
// which is exactly correct for the patch chapter.
```

**Config example (Ch13):**
```javascript
"drone": {
  "type": "collar",
  "oscType": "sine",
  "baseFreq": 261.63,    // Middle C — back to baseline
  "gain": 0.025,
  "lfoDepth": 0.001,
  "lfoMax": 0.02,        // CRITICAL: near-zero. The patch flattens the LFO.
  "filterQ": 6,
  "filterFloor": 500
}
```

---

### `harmonic-series`

**What it is:** Three oscillators — fundamental, second harmonic (2×), third harmonic (3×) — at decreasing gains (1.0, 0.5, 0.25). Richer and fuller than the `layered` two-oscillator approach. More organically complex than a sawtooth.

**What it models:** The Calibration Hall's *"golden viscosity"* — the Score's engineered acoustic environment at its most elegant. A lush, living resonance that has been deliberately constructed to feel beautiful and mandatory.

**Use for:** Ch1 (upgrade from current `layered` to full harmonic series), Ch7 (Rival's brightness).

**Implementation:**
```javascript
// harmonic-series type: fundamental + 2nd + 3rd harmonics at
// 1.0 / 0.5 / 0.25 gain ratios (natural harmonic series weights).
// Creates organic richness that a single oscillator cannot achieve.
// Models spaces where the Score has engineered the acoustic environment
// to maximum fidelity — the Calibration Hall's 'golden viscosity'.
this.droneOsc = ctx.createOscillator();
this.droneOsc.type = 'sine';
this.droneOsc.frequency.value = config.baseFreq;
this.droneOsc.connect(this.filter);
this.droneOsc.start(now);

this.droneOsc2 = ctx.createOscillator();
this.droneOsc2.type = 'sine';
this.droneOsc2.frequency.value = config.baseFreq * 2;
const h2Gain = ctx.createGain();
h2Gain.gain.value = 0.5;
this.droneOsc2.connect(h2Gain);
h2Gain.connect(this.filter);
this.droneOsc2.start(now);

this.droneOsc3 = ctx.createOscillator();
this.droneOsc3.type = 'sine';
this.droneOsc3.frequency.value = config.baseFreq * 3;
const h3Gain = ctx.createGain();
h3Gain.gain.value = 0.25;
this.droneOsc3.connect(h3Gain);
h3Gain.connect(this.filter);
this.droneOsc3.start(now);
// Note: requires adding this.droneOsc3 = null to _fadeOut() cleanup
```

---

### `interference`

**What it is:** Three oscillators at slightly different frequencies — base, base+Δ1, base+Δ2 — creating a complex, shifting interference pattern. More chaotic than `beating`'s orderly two-oscillator pulse. The three-way interaction produces unpredictable amplitude modulation.

**What it models:** Multiple wrong notes coexisting without resolving. The underground collective in Ch17 — not two signals searching for phase lock, but a whole room of people who have stopped trying to lock.

**Use for:** Ch17 (replacing or layering under `crackle`).

**Implementation:**
```javascript
// interference type: three oscillators at slightly offset frequencies.
// Unlike 'beating' (two oscillators → clean periodic pulse), three
// oscillators produce a non-periodic interference pattern — the
// amplitude fluctuates unpredictably. Models a space where
// multiple incompatible signals coexist without resolution.
this.droneOsc = ctx.createOscillator();
this.droneOsc.type = 'sine';
this.droneOsc.frequency.value = config.baseFreq;
this.droneOsc.connect(this.filter);
this.droneOsc.start(now);

this.droneOsc2 = ctx.createOscillator();
this.droneOsc2.type = 'sine';
this.droneOsc2.frequency.value = config.baseFreq + (config.delta1 || 1.3);
const d1Gain = ctx.createGain();
d1Gain.gain.value = 0.75;
this.droneOsc2.connect(d1Gain);
d1Gain.connect(this.filter);
this.droneOsc2.start(now);

this.droneOsc3 = ctx.createOscillator();
this.droneOsc3.type = 'sine';
this.droneOsc3.frequency.value = config.baseFreq + (config.delta2 || 3.1);
const d2Gain = ctx.createGain();
d2Gain.gain.value = 0.55;
this.droneOsc3.connect(d2Gain);
d2Gain.connect(this.filter);
this.droneOsc3.start(now);
```

---

### `breath` (modifier, not a standalone type)

**What it is:** A second LFO running at exactly 0.2Hz (12 cycles/minute — human resting breath rate) applied as a slow gain envelope rather than fast tremolo. A second `GainNode` with a `0.2Hz` LFO feeding it, connected in series before `droneGain`.

**What it models:** Biological presence. Used on chapters where a character's physical state is the subject — Ven in the vault, the NAI hidden in the machine.

**Use for:** Ch6 (Ven's laboured breathing), Ch12 (NAI's hidden heartbeat). Activated when config includes `"breathDepth": 0.02` or similar.

**Implementation:** Add to `_startDrone()` as an optional modifier after the main oscillator setup:
```javascript
// breath modifier: slow amplitude modulation at human breath rate (0.2Hz).
// Runs independently of the main LFO (which tracks tension).
// Applied only when config.breathDepth is defined.
// Models biological presence — a body in the signal.
if (config.breathDepth) {
  this.breathLFO = ctx.createOscillator();
  this.breathLFO.type = 'sine';
  this.breathLFO.frequency.value = 0.2; // 12 breaths/minute

  this.breathDepth = ctx.createGain();
  this.breathDepth.gain.value = config.breathDepth;

  this.breathLFO.connect(this.breathDepth);
  this.breathDepth.connect(this.droneGain.gain);
  this.breathLFO.start(now);
}
// Also null this.breathLFO and this.breathDepth in _fadeOut() cleanup
```

---

## 04 — The LFO Arc

This is the most important section for the volume's overall audio narrative. The `lfoMax` ceiling controls how much a chapter's drone can *respond* to the reader's progress through it. A chapter with `lfoMax: 0.02` is acoustically suppressed regardless of tension. A chapter with `lfoMax: 1.2` is frenetic.

The current values are largely arbitrary. The proposed arc below follows the narrative.

| CH | CHAPTER | `lfoMax` NOW | `lfoMax` PROPOSED | REASON |
|---|---|---|---|---|
| 01 | The Zap | 0.20 | 0.30 | Calibration hall is controlled but the Zap should be audible |
| 02 | Assessment | 0.15 | 0.05 | Voss's void. Clinical non-movement. |
| 03 | Modulation | 0.35 | 0.40 | Slum degradation — more reactive to tension |
| 04 | Medium | 0.25 | 0.20 | Surveillance state: mechanical precision, not responsiveness |
| 05 | Sync Check | 0.30 | 0.35 | The Triad forming — slight loosening |
| 06 | Ground State | 0.15 | 0.25 | Ven's heat is increasing — should be more volatile |
| 07 | Rival | 0.50 | 0.55 | Challenge and brightness — high reactivity correct |
| 08 | Sortie | 0.70 | 0.80 | Combat maximum — slight increase |
| 09 | Silence | 0.00 | 0.00 | Do not touch |
| 10 | Breach | 1.20 | 1.20 | Do not touch — this is correct |
| 11 | Safe Mode | 0.20 | 0.08 | Krell does not respond to Taro's distress with warmth |
| 12 | Audit | 0.20 | 0.15 | NAI's tenderness is slight — mostly still |
| 13 | Patch | 0.25 | **0.02** | **CRITICAL** — the patch flattens everything |
| 14 | Return | 0.40 | 0.08 | Post-patch world. Still wrong. Compliance holds. |
| 15 | Phantom Mesh | 0.45 | 0.50 | Cracks forming — slight increase |
| 16 | Illegal Mods | 0.50 | 0.65 | Off-grid freedom — uncapped direction correct |
| 17 | Underground | 0.50 | 0.80 | Final chapter: unregulated. The noise is coming. |

### The filterFloor Arc

`filterFloor` sets how bright or dark the drone can be at minimum coherence. High values = always bright (the Score is maintaining clarity even under stress). Low values = can go very dark.

| CH | `filterFloor` NOW | `filterFloor` PROPOSED | REASON |
|---|---|---|---|
| 01 | 500 | 500 | Calibration hall — correct |
| 02 | 600 | 750 | Voss's diagnostic void should be bright and sterile |
| 03 | 400 | 350 | Degraded zone — allow more darkness |
| 06 | 350 | 280 | Industrial heat — can go very dark |
| 11 | 550 | 700 | Krell's space is always fully illuminated — no shadow |
| 13 | 450 | 550 | Patch chapter — compliance keeps everything bright |
| 14 | 300 | 600 | 8K render — should be acoustically pristine |
| 17 | 200 | 150 | Off-grid floor — maximum darkness available |

---

## 05 — One-Shot Tag Events

The engine currently has zero audio events tied to specific beats. These five are the highest-value additions — each is directly motivated by explicit lore text, and each is implementable by adding a `_triggerTagAudio(tag)` method called from `_renderBeat()` when `beat.tag` is defined.

---

### EVENT 1 — The Zap (`data-tag="clip"`)

**Lore trigger:** *"White light. Static. The taste of copper and burning hair."* / `SYSTEM_ALERT: ELECTRICAL_DISCHARGE`

**What happens:** A brief one-shot resonant burst — the Score's signal shorting out. A sine oscillator at 2×baseFreq, high gain, short envelope (attack 10ms, decay 300ms). The masterGain's existing soft limiter will clip it slightly, which is intentional — this is hardware failure.

```javascript
// tag: 'clip' — electrical discharge one-shot
// Models the Score's signal shorting: resonant burst into the limiter.
// Short attack (10ms) + fast decay (300ms) = physical snap event.
// Intentionally clips against masterGain — the hardware is failing.
case 'clip': {
  const osc = ctx.createOscillator();
  osc.type = 'sine';
  osc.frequency.value = (this.currentConfig?.baseFreq || 440) * 2;
  const env = ctx.createGain();
  env.gain.setValueAtTime(0, now);
  env.gain.linearRampToValueAtTime(0.4, now + 0.01);  // 10ms attack
  env.gain.exponentialRampToValueAtTime(0.001, now + 0.3); // 300ms decay
  osc.connect(env);
  env.connect(this.masterGain);
  osc.start(now);
  osc.stop(now + 0.31);
  break;
}
```

---

### EVENT 2 — Kael's Tuning Fork (`data-tag="impedance"` in Ch3)

**Lore trigger:** Ch3: *"TING. ACOUSTIC_EVENT: REFERENCE_PITCH [A-440] [ACCURACY: 100.00%]"*

**What happens:** A 2-second pure sine at exactly 440Hz played as a one-shot *over* the F#4 ambient. No gain envelope on attack — it simply appears at full amplitude like a tuning fork struck cleanly. Slow exponential decay over 2 seconds. The reference tone cutting through the slum's degraded signal.

```javascript
// tag: 'impedance' in Ch3 — Kael's tuning fork reference pitch.
// A-440 at 100% accuracy, played over the ambient F#4 drone.
// No attack envelope — tuning forks don't ramp. They appear.
// 2-second exponential decay = physical fork ringing out.
// The most coherent sound in the slum environment.
case 'impedance': {
  if (this.currentType === 'void-decay') break; // Don't fire in void
  const fork = ctx.createOscillator();
  fork.type = 'sine';
  fork.frequency.value = 440; // Exactly A-440 — lore spec
  const forkGain = ctx.createGain();
  forkGain.gain.setValueAtTime(0.15, now);  // No attack — appears fully
  forkGain.gain.exponentialRampToValueAtTime(0.001, now + 2.0); // 2s ring
  fork.connect(forkGain);
  forkGain.connect(this.masterGain);
  fork.start(now);
  fork.stop(now + 2.1);
  break;
}
```

---

### EVENT 3 — The Collar Tightening (`data-tag="override"`)

**Lore trigger:** Ch2: *"The collar tightened by one millimeter. The physical damping was highly effective."*

**What happens:** No new sound is added. Instead, the existing filter is briefly narrowed — Q value ramps from `0.8` to `8.0` over 200ms, holds for 1 second, then returns. The drone goes from broad and warm to constricted and nasal. The reader *hears* suppression as a filter event.

```javascript
// tag: 'override' — collar tightening, physical suppression.
// No new oscillator — modifies the existing filter architecture.
// Q ramps from 0.8 (natural) to 8.0 (narrow bandpass) over 200ms,
// holds 1 second, returns over 800ms.
// Models hardware restriction: the signal is still there, just
// squeezed through a narrower compliance window.
case 'override': {
  if (!this.filter) break;
  const q = this.filter.Q;
  q.setValueAtTime(q.value, now);
  q.linearRampToValueAtTime(8.0, now + 0.2);   // 200ms constriction
  q.setValueAtTime(8.0, now + 1.2);             // Hold 1 second
  q.linearRampToValueAtTime(0.8, now + 2.0);    // 800ms release
  break;
}
```

---

### EVENT 4 — The Limiter Snap (`data-tag="limiter"`)

**Lore trigger:** Ch10: *"CRACK. The limiter ring snapped."* / `LIMITER: REMOVED` / `NEURAL_DAMPING: 0.00%`

**What happens:** A brief sawtooth burst at 2× base frequency, high gain, 50ms envelope. The masterGain clips it. Simultaneously, the main filter's Q drops to 0.1 (as open as possible) and stays there for the rest of the chapter — the limiter has been physically destroyed, the filter no longer constrains.

```javascript
// tag: 'limiter' — the collar snaps, the limiter is gone.
// Two simultaneous effects:
// 1. One-shot sawtooth burst: the physical snap event.
//    High gain into masterGain = intentional clip.
// 2. Filter Q set to 0.1 permanently for this chapter.
//    The limiter is broken — the filter cannot recover.
//    Note: this persists until the next chapter's _startDrone() call.
case 'limiter': {
  // Effect 1: the snap
  const snap = ctx.createOscillator();
  snap.type = 'sawtooth';
  snap.frequency.value = (this.currentConfig?.baseFreq || 116.54) * 2;
  const snapGain = ctx.createGain();
  snapGain.gain.setValueAtTime(0, now);
  snapGain.gain.linearRampToValueAtTime(0.5, now + 0.005); // 5ms attack
  snapGain.gain.exponentialRampToValueAtTime(0.001, now + 0.05); // 50ms
  snap.connect(snapGain);
  snapGain.connect(this.masterGain);
  snap.start(now);
  snap.stop(now + 0.06);

  // Effect 2: open the filter permanently
  if (this.filter) {
    this.filter.Q.setValueAtTime(0.1, now + 0.01); // Stays open
  }
  break;
}
```

---

### EVENT 5 — Phase Lock Resolution (`data-tag="bass_drop"` in Ch5/Ch15)

**Lore trigger:** Ch5: `SYNC_STATUS: GREEN / NETWORK: LOCKED` / Ch15: `RESONANCE_SYNC_CONFIRMED`

**What happens:** In chapters using the `beating` type, the beat resolves. `droneOsc2`'s frequency is ramped toward `droneOsc`'s frequency over 3 seconds — the interference beat slows from 1Hz to 0.0Hz. Perfect unison. The pulsing disappears. This is the sound of phase lock.

```javascript
// tag: 'bass_drop' in beating-type chapters — phase lock resolution.
// Ramps droneOsc2 from (baseFreq + beatFreq) to baseFreq over 3 seconds.
// The beating amplitude pulse slows and disappears as both oscillators
// converge on the same frequency.
// This is the sound of two signals finding each other.
// Only fires in 'beating' type chapters — guards against null droneOsc2.
case 'bass_drop': {
  if (!this.droneOsc2 || this.currentType !== 'beating') break;
  const targetFreq = this.currentConfig?.baseFreq || 440;
  // Ramp to unison over 3 seconds — the lock is not instantaneous
  this.droneOsc2.frequency.linearRampToValueAtTime(targetFreq, now + 3.0);
  break;
}
```

---

### EVENT 6 — The Final Line (`data-tag="crash"` in Ch17)

**Lore trigger:** Ch17: *"I am bringing the noise."* — final line of the volume.

**What happens:** A single clean sawtooth pulse at baseFreq, 200ms attack, 4 second decay. Not an explosion — a statement. One deliberate, unhurried sawtooth that rises over the crackle and then fades. The volume's last audio event before the reader stops scrolling.

```javascript
// tag: 'crash' in Ch17 — "I am bringing the noise."
// Not a burst — a statement. Sawtooth rises slowly (200ms attack)
// and decays over 4 seconds. The one musical gesture at the end
// of a chapter that is otherwise pure noise.
// Models Taro choosing his signal deliberately, not explosively.
case 'crash': {
  const signal = ctx.createOscillator();
  signal.type = 'sawtooth';
  signal.frequency.value = 116.54; // Bb2 — Taro's frequency from Ch10
  const sigGain = ctx.createGain();
  sigGain.gain.setValueAtTime(0, now);
  sigGain.gain.linearRampToValueAtTime(0.12, now + 0.2);  // 200ms rise
  sigGain.gain.exponentialRampToValueAtTime(0.001, now + 4.0); // 4s fade
  signal.connect(sigGain);
  sigGain.connect(this.masterGain);
  signal.start(now);
  signal.stop(now + 4.1);
  break;
}
```

---

## 06 — Updated CHAPTER_CONFIG Drone Values

Full replacement values for every chapter's `drone` object. Only the `drone` key changes — all other config properties follow §05 of the UI guide.

```javascript
// ── CH01 — The Zap ────────────────────────────────────────────
// harmonic-series replaces layered: richer, more 'golden viscosity'
// Middle C as base — lore-direct: "environmental baseline held at
// a perfect Middle C, vibrating at 261.63 Hz"
"ch01_zap": {
  "drone": {
    "type": "harmonic-series",
    "baseFreq": 261.63,     // Middle C — verbatim from text
    "gain": 0.028,
    "lfoDepth": 0.003,
    "lfoMax": 0.30,         // Was 0.20 — Zap should spike audibly
    "filterFloor": 500
  }
},

// ── CH02 — The Assessment ──────────────────────────────────────
// Voss's diagnostic white void. Most still drone in the volume.
// A-440 sine but with near-zero movement — VOLATILITY: NULL
"ch02_assessment": {
  "drone": {
    "type": "sine",
    "baseFreq": 440,         // A-440 — Score's enforcement baseline
    "gain": 0.022,
    "lfoDepth": 0.001,       // Nearly imperceptible tremolo
    "lfoMax": 0.05,          // Was 0.15 — the void does not breathe
    "filterFloor": 750       // Was 600 — acoustically sterile
  }
},

// ── CH03 — Modulation ──────────────────────────────────────────
// No frequency change — F#4 is lore-direct. Slight increase to
// reactivity to allow Kael's tuning fork event to read correctly.
"ch03_modulation": {
  "drone": {
    "type": "sine",
    "baseFreq": 369.99,      // F#4 — "ventilation system at F-sharp"
    "gain": 0.030,
    "detune": 2,
    "lfoDepth": 0.004,
    "lfoMax": 0.40,          // Was 0.35 — allow more tension response
    "filterFloor": 350       // Was 400 — degraded zone, allow darkness
  }
},

// ── CH04 — The Medium ──────────────────────────────────────────
// pulse replaces square — same abrasive concept, more mechanically
// hollow. The Medium's surveillance is indifferent, not musical.
"ch04_medium": {
  "drone": {
    "type": "pulse",
    "baseFreq": 440,         // A-440 — institutional standard
    "gain": 0.018,
    "lfoDepth": 0.002,
    "lfoMax": 0.20,          // Mechanical precision — not reactive to warmth
    "filterFloor": 550,
    "filterQ": 5             // Resonant edge — the room knows you're there
  }
},

// ── CH05 — Sync Check ──────────────────────────────────────────
// No change to type or baseFreq. beatFreq unchanged — 1Hz is
// correct for uncertain sync. lfoMax slightly up.
"ch05_sync_check": {
  "drone": {
    "type": "beating",
    "baseFreq": 440,
    "beatFreq": 1,           // One pulse/second — slow, uncertain
    "gain": 0.025,
    "lfoDepth": 0.004,
    "lfoMax": 0.35,          // Was 0.30 — Triad forming, slight loosening
    "filterFloor": 450
  }
},

// ── CH06 — Ground State ────────────────────────────────────────
// Same low register. breathDepth added — Ven's laboured physical
// state should be audible as a slow biological presence.
"ch06_ground_state": {
  "drone": {
    "type": "sine",
    "baseFreq": 110,         // A2 — low, grounded, physical
    "gain": 0.035,
    "subFreq": 40,
    "subGain": 0.025,
    "breathDepth": 0.015,    // NEW — Ven's heat/breath in the vault
    "lfoDepth": 0.002,
    "lfoMax": 0.25,          // Was 0.15 — heat is building, more volatile
    "filterFloor": 280       // Was 350 — allow industrial darkness
  }
},

// ── CH07 — Rival ───────────────────────────────────────────────
// layered with major third (5:4) replaces plain sine.
// C5 pitch unchanged (lore-direct). Major third = confrontational
// brightness, not warmth. The sound of a gauntlet.
"ch07_rival": {
  "drone": {
    "type": "layered",
    "baseFreq": 523.25,      // C5 — verbatim from fragment pool
    "harmonicRatio": 1.25,   // Major third (5:4) — bright assertion
    "gain": 0.022,
    "lfoDepth": 0.005,
    "lfoMax": 0.55,          // Was 0.50 — challenge is high-energy
    "filterFloor": 400
  }
},

// ── CH08 — Sortie ──────────────────────────────────────────────
// No change — already correct. lfoMax up slightly for maximum
// combat reactivity. sub-bass keeps physical weight.
"ch08_sortie": {
  "drone": {
    "type": "layered",
    "baseFreq": 55,          // A1 — felt, not heard
    "gain": 0.035,
    "subFreq": 27.5,
    "subGain": 0.030,
    "lfoDepth": 0.006,
    "lfoMax": 0.80,          // Was 0.70 — combat maximum
    "filterFloor": 250
  }
},

// ── CH09 — Silence ─────────────────────────────────────────────
// DO NOT TOUCH. void-decay is the most narratively correct drone
// in the entire engine. It dies exactly as the text describes.
"ch09_silence": {
  "drone": {
    "type": "void-decay",
    "baseFreq": 0,
    "gain": 0.04,
    "decayTime": 3.5,
    "lfoMax": 0,
    "filterFloor": 800
  }
},

// ── CH10 — The Breach ──────────────────────────────────────────
// No config change. The snap event is handled by the 'limiter'
// tag in _triggerTagAudio(). The drone itself stays as-is.
// lfoMax: 1.2 is correct — uncontrolled post-limiter.
"ch10_breach": {
  "drone": {
    "type": "sawtooth",
    "baseFreq": 116.54,      // Bb2 — dissonant, torn
    "gain": 0.04,
    "lfoDepth": 0.008,
    "lfoMax": 1.20,          // Maximum — do not lower
    "filterFloor": 180       // Can go fully dark
  }
},

// ── CH11 — Safe Mode (Krell) ───────────────────────────────────
// pulse replaces sine. "Flat, grinding, abrasive — heavy industrial
// machinery." The old A3 sine was gentle. This is not.
// filterFloor: 700 — Krell's space is always fully illuminated.
"ch11_safe_mode": {
  "drone": {
    "type": "pulse",
    "baseFreq": 220,         // A3 — same pitch, completely different character
    "gain": 0.022,
    "lfoDepth": 0.001,       // Krell barely breathes
    "lfoMax": 0.08,          // Was 0.20 — does not respond to Taro's distress
    "filterFloor": 700,      // Always bright — no shadow in this room
    "filterQ": 7             // High mechanical edge
  }
},

// ── CH12 — Audit (NAI) ─────────────────────────────────────────
// beating replaces sine. 440Hz + 440.3Hz = 0.3Hz beat (one pulse
// per 3.3 seconds). The NAI's hidden heartbeat. Subliminal.
// breathDepth added — the machine is alive.
"ch12_audit": {
  "drone": {
    "type": "beating",
    "baseFreq": 440,
    "beatFreq": 0.3,         // Was sine — now has a slow hidden pulse
    "gain": 0.025,
    "breathDepth": 0.008,    // NEW — barely perceptible biological presence
    "lfoDepth": 0.001,
    "lfoMax": 0.15,          // Was 0.20 — NAI's tenderness is slight
    "filterFloor": 500
  }
},

// ── CH13 — Patch ───────────────────────────────────────────────
// collar replaces chord. The perfect fifth was too warmly consonant —
// it sounded earned. The patch should sound clinical and restricted.
// CRITICAL: lfoMax: 0.02 — the patch flattens everything.
"ch13_patch": {
  "drone": {
    "type": "collar",
    "oscType": "sine",
    "baseFreq": 261.63,      // Back to Middle C — compliance baseline
    "gain": 0.025,
    "lfoDepth": 0.001,
    "lfoMax": 0.02,          // *** CRITICAL *** — patch kills all movement
    "filterFloor": 550,
    "filterQ": 6             // Tight bandpass — only the allowed band passes
  }
},

// ── CH14 — The Return ──────────────────────────────────────────
// A-440 sine replaces 40Hz subsonic. Ch14 is Malkuth at 8K render —
// the most pristine environment in the volume. Was factually wrong.
// lfoMax: 0.08 — patch still active, very little movement.
"ch14_return": {
  "drone": {
    "type": "sine",
    "baseFreq": 440,         // Was 40Hz — wrong register for 8K fidelity
    "gain": 0.025,
    "lfoDepth": 0.002,
    "lfoMax": 0.08,          // Was 0.40 — patch still active
    "filterFloor": 600       // Was 300 — acoustically pristine environment
  }
},

// ── CH15 — The Phantom Mesh ────────────────────────────────────
// beatFreq: 1.5 is correct (wider than Ch5's 1Hz — less stable).
// lfoMax up slightly — the cracks are forming.
"ch15_phantom_mesh": {
  "drone": {
    "type": "beating",
    "baseFreq": 440,
    "beatFreq": 1.5,         // Ghost signal — slightly less stable than Ch5
    "gain": 0.025,
    "lfoDepth": 0.005,
    "lfoMax": 0.50,          // Was 0.45 — cracks forming, slightly looser
    "filterFloor": 380
  }
},

// ── CH16 — Illegal Modulations ─────────────────────────────────
// Tritone dissonant is correct. lfoMax up — off-grid, uncapped.
// filterFloor down — unauthorized space can go dark.
"ch16_illegal_modulations": {
  "drone": {
    "type": "dissonant",
    "baseFreq": 261.63,      // Middle C + tritone shadow
    "gain": 0.028,
    "lfoDepth": 0.005,
    "lfoMax": 0.65,          // Was 0.50 — off-grid freedom
    "filterFloor": 280       // Was 300 — unauthorized, can go darker
  }
},

// ── CH17 — Underground ─────────────────────────────────────────
// interference replaces crackle — multiple wrong notes coexisting
// without resolving. The underground collective, not pure noise.
// lfoMax up to 0.80 — unregulated, the noise is coming.
// The 'crash' tag event handles the final line separately.
"ch17_underground": {
  "drone": {
    "type": "interference",
    "baseFreq": 116.54,      // Bb2 — Taro's frequency, now chosen freely
    "delta1": 1.3,           // First interference offset
    "delta2": 3.1,           // Second — non-harmonic, unpredictable
    "gain": 0.032,
    "lfoDepth": 0.006,
    "lfoMax": 0.80,          // Was 0.50 — the noise is coming
    "filterFloor": 150       // Was 200 — maximum darkness available
  }
}
```

---

## 07 — Implementation Notes

### Cleanup: Add to `_fadeOut()`

Every new oscillator needs cleanup. Add these nulls to the `_fadeOut()` stop block:

```javascript
// NEW node cleanup — add alongside existing droneOsc, droneOsc2, etc.
if (this.droneOsc3)    { try { this.droneOsc3.stop();    } catch(e){} this.droneOsc3    = null; }
if (this.breathLFO)    { try { this.breathLFO.stop();    } catch(e){} this.breathLFO    = null; }
this.breathDepth = null;
```

### Wiring: Call `_triggerTagAudio()` from `_renderBeat()`

In whatever method processes individual beat renders, add:

```javascript
// Trigger one-shot audio events for tagged beats.
// Only fires when a tag is present — no-op for untagged beats.
if (beat.tag && audioEngine.ready) {
  audioEngine._triggerTagAudio(beat.tag);
}
```

### Guard for Ch7 `harmonicRatio`

The existing `layered` type hardcodes the second oscillator at `baseFreq * 2` (octave). Ch7 needs `baseFreq * 1.25` (major third). Add a `harmonicRatio` config field that overrides the octave default:

```javascript
// In the 'layered' case in _startDrone():
// harmonicRatio defaults to 2 (octave) if not specified.
// Ch07 sets it to 1.25 (major third) for confrontational brightness.
this.droneOsc2.frequency.value = config.baseFreq * (config.harmonicRatio || 2);
```

### Priority Order

If implementing incrementally:

1. `lfoMax: 0.02` on Ch13 — one-line change, highest narrative value
2. Ch14 drone frequency correction — one-line change, currently factually wrong
3. Ch11 type → `pulse` — requires new synthesis block
4. Ch12 type → `beating` with `breathDepth` — requires breath modifier
5. One-shot tag events — requires new `_triggerTagAudio()` method
6. Ch1 → `harmonic-series` — requires new synthesis block + `_fadeOut()` cleanup
7. Ch17 → `interference` — requires new synthesis block
8. Ch7 `harmonicRatio` guard — small addition to existing `layered` block

---

*// END OF DOCUMENT — SIGNAL_TRANSMISSION_GUIDE_V1.0*
*// Chapters updated: 17 / New synthesis types: 6 / One-shot events: 6*
*// Critical fixes: Ch11 Krell, Ch13 patch lfoMax, Ch14 register*
