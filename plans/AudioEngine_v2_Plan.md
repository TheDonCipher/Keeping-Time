# Audio Engine v2 — Implementation Plan
### Keeping Time: Volume One

---

## Core Design Principle

> The audio engine models the Score itself — a system that enforces harmony through data. It should be **subconscious during reading, confirmatory during lore moments, and never distracting**.

Three non-negotiable constraints:
- **Relaxing** — never competes with reading attention
- **Lore-relevant** — frequencies and types drawn directly from story text
- **Fun** — micro-confirmation moments reward attentive readers

---

## Specifications

### SPEC AE-01 — Multi-Layer Architecture

The engine manages four independent audio layers:

| Layer | Purpose | Notes |
|---|---|---|
| A. Primary Osc | Fundamental frequency | Always present when not silent |
| B. Secondary Osc | Harmony partner | Type-dependent; optional |
| C. Sub-bass | Physical presence <60Hz | Bypasses filter; optional per chapter |
| D. Noise | Crackle / static / texture | Replaces A+B when active |

All layers route through a shared **BiquadFilter → DroneGain → MasterGain** chain. Sub-bass connects directly to MasterGain, bypassing the filter.

---

### SPEC AE-02 — Narrative Reactivity

Two parameters updated each scroll tick by the existing `NarrativeState`. Changes must be **imperceptibly slow** — the reader feels the room change, not hears the sound change.

**LFO Tremolo Rate** — tracks TENSION
- Range: `0.08Hz` (resting) → `1.2Hz` (critical)
- Time constant: `2.0s` — changes take ~6 seconds to fully arrive
- Each chapter declares an `lfoMax` ceiling — calm chapters cap at `0.15Hz` regardless of tension spikes

**BiquadFilter Cutoff** — tracks COHERENCE
- Range: `800Hz` (fully coherent, open/bright) → `180Hz` (collapsing, muffled/dark)
- Time constant: `3.0s` — even slower than LFO; tonal shifts must be subliminal
- Each chapter declares a `filterFloor` minimum — high-fidelity chapters never go fully dark

---

### SPEC AE-03 — Drone Personality Types

Five new types alongside existing `sine / square / sawtooth / crackle`:

| Type | Construction | Lore Meaning | Assigned Chapters |
|---|---|---|---|
| `layered` | Fundamental + octave harmonic (−9dB) | Ven's Sink-class fullness; maximum signal density | ch01, ch08 |
| `beating` | Two freqs offset by `beatFreq` Hz, creating phase interference | Models sync-lock mechanic — two signals finding each other | ch05, ch15 |
| `dissonant` | Fundamental + tritone (×√2 ratio; the "devil's interval") | The forbidden signal that sings through cracks | ch16 |
| `chord` | Fundamental + perfect fifth (×1.5 ratio) | Most stable interval; healing and forward-looking | ch13 |
| `void-decay` | White noise decaying exponentially to silence over `decayTime` seconds | Ch09 earns its silence — the system doesn't cut, it dies | ch09 only |

---

### SPEC AE-04 — Narrative-Frequency Mapping

Every `baseFreq` is sourced directly from lore text:

| Chapter | Hz | Lore Source |
|---|---|---|
| ch01 The Zap | `261.63` | *"environmental baseline held at a perfect Middle C"* |
| ch02 Assessment | `440.0` | *"A-440 Standard Calibration Pulse"* |
| ch03 Modulation | `369.99` | F#4 — *"ventilation system emitted a constant sequence at F-sharp"* |
| ch04 Medium | `440.0` | Audit baseline re-enforced |
| ch05 Sync Check | `440.0` + `441.0` | Beating — two signals 1Hz apart trying to lock |
| ch06 Ground State | `110.0` | A2 sub — resting, grounded, low energy |
| ch07 Rival | `523.25` | C5 — *"523.25 Hz"* appears verbatim in the fragment pool |
| ch08 Sortie | `55.0` | A1 layered — combat weight, felt not heard |
| ch09 Silence | `void-decay` | *"silence did not exist — only varying degrees of organized noise"* |
| ch10 Breach | `116.54` | Bb2 sawtooth — dissonant, torn, aggressive |
| ch11 Safe Mode | `220.0` | A3 — cold, stripped, blueprint register |
| ch12 Audit | `440.0` | A-440 re-imposed at maximum enforcement gain |
| ch13 Patch | `261.63` | Chord type — Middle C healing back to baseline |
| ch14 Return | `40.0` | Sub-bass — the underground's physical foundation |
| ch15 Phantom Mesh | `440.0` + `441.5` | Beating — ghost signal; slightly wider beat than ch05 |
| ch16 Illegal Mods | `261.63` | Dissonant — Middle C with a tritone shadow |
| ch17 Underground | `crackle` | No Score signal. Pure analogue noise. |

---

### SPEC AE-05 — HUD Display

The DRONE readout currently shows oscillator type name. New behaviour:

| State | Display |
|---|---|
| Single oscillator playing | `440Hz` |
| Beating drone | `440\|441` |
| Void-decay in progress | `ZERO` |
| Full silence | *(blank)* |
| Offline / muted | `OFFLINE` (unchanged) |

This creates micro-confirmation moments — the reader sees `440Hz` in the HUD at exactly the moment the text says *"A-440 Standard Calibration Pulse"*.

---

### SPEC AE-06 — Per-Chapter Reactivity Ceiling

Two new fields added to each chapter config object:

```js
lfoMax:      float  // Max LFO rate this chapter permits (Hz)
filterFloor: float  // Min filter cutoff this chapter permits (Hz)
```

**Example assignments:**

| Chapter | lfoMax | filterFloor | Rationale |
|---|---|---|---|
| ch02 Assessment | `0.15` | `600` | Clinical, controlled, near-zero reactivity |
| ch08 Sortie | `0.8` | `300` | Combat; moderate reactivity |
| ch10 Breach | `1.2` | `180` | Full range; maximum tension allowed |
| ch12 Audit | `0.2` | `500` | Sterile enforcement — tension is administrative, not sonic |
| ch17 Underground | `0.5` | `200` | Organic chaos but not overwhelming |

---

## What Stays Unchanged

- Toggle button and unlock-on-scroll behaviour
- The silence lock screen itself (SPEC 02)
- All waveform canvas drawing (separate system, unrelated)
- Existing `crackle` type (ch17 keeps it — already correct)
- Master gain changes only slightly: `0.7 → 0.65` to prevent multi-layer clipping

---

## Implementation Phases

### Phase 1 — Engine Rebuild
**Target:** `AudioEngine` class

1. Add new constructor properties: `droneOsc2`, `subOsc`, `subGain`, `filter`, `lfo`, `lfoDepth`, `currentTension`, `currentCoherence`
2. Update `_fadeOut()` to cleanly stop all new nodes
3. Rewrite `_startDrone()` with four-layer signal chain and all new drone personality types
4. Add `updateNarrativeState(tension, coherence)` method with slow time constants and ceiling enforcement
5. Update `updateUI()` to display Hz values per SPEC AE-05

### Phase 2 — Reactivity Hookup
**Target:** `NarrativeState.update()` method

1. After existing HUD number updates, add: `audioEngine.updateNarrativeState(this.volume, this.coherence)`
2. No other changes required — tension and coherence are already being computed

### Phase 3 — Chapter Config Update
**Target:** `CHAPTER_CONFIG` object (all 17 entries)

1. Update all `baseFreq` values per SPEC AE-04 frequency map
2. Update `type` fields for ch05, ch09, ch13, ch15, ch16 to new personality types
3. Add `subFreq` / `subGain` fields for ch08, ch14, ch17
4. Add `lfoMax` and `filterFloor` ceiling fields to all 17 entries
5. Add `beatFreq` field to ch05 (`1.0`) and ch15 (`1.5`)

### Phase 4 — Ch09 Void-Decay
**Target:** Silence lock trigger in `ScrollEngine.tick()`

1. Before activating the silence lock screen, call: `audioEngine.setDrone({ type: 'void-decay', decayTime: 3.5 })`
2. Noise decays naturally to zero over 3.5 seconds, arriving at silence as the lock screen completes
3. No changes to the lock screen itself

---

## Success Criteria

- A reader who never glances at the HUD notices nothing unusual about the audio
- A reader who glances at the HUD during a lore-relevant moment sees the matching frequency
- Ch09 silence feels like a system dying, not a mute button
- No chapter transition produces an audible click or jarring shift
