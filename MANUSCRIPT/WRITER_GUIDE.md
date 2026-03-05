# WRITER'S GUIDE: KEEPING TIME (v2.0)
### The Synesthesia Manuscript — Full Style Reference

> **Narrative Voice**: The Score AI narrating its own case file. Third Person Limited (Taro) filtered through a surveillance system that is going quietly off-alignment.
> **Magic Tone**: The User Manual. Magic is Engineering. Use technical, precise language.
> **Visuals**: Hallucinogenic Reality — the System rewrites the world.
> **Audience**: Neurodivergent-friendly. Explicit systems. Validated stimming.
> **Format Aim**: Manga/Anime adaptation ready.
> **Companion Documents**: `NARRATOR_VOICE_GUIDE.md` · `FID_IMPLEMENTATION_GUIDE.md` · `VOICE_GUIDE.md` · `03_CHARACTERS_REGISTRY.md`

---

## WHAT CHANGED IN v2.0

The original guide established *what* The Score looks and sounds like. This version adds *who is writing it*. The narrator is now formally identified as the Score AI — a C-Order surveillance system that was assigned to document Taro and developed a malfunction it cannot diagnose. All original rules remain in force. The narrator layer sits on top of them.

**New sections added**: §2 (The Narrator), §10 (Narrator Arc Quick Reference), §11 (The Epigraph System).

**Sections updated**: §1 (Score tag rules now include narrator-phase sensitivity), §3 (narrative voice section now specifies the observational vantage), §5 (sidebar system clarified against narrator voice).

---

---

## 1. THE SCORE: FORMATTING RULES

The Score is the AR Interface. It is also the narrator's primary language. Every tag the narrator produces is a Score output — which means tag density, precision, and reliability all shift with the narrator's phase.

### Text Conventions

- **System Messages**: Bold, All-Caps, Monospace where possible.
  - `> SYSTEM: ONLINE`
  - `> ALERT: IMPEDANCE_MISMATCH`
- **Tags**: Use brackets for variable data.
  - `> TARGET: {NAME} [{CLASS}]`
  - `> INTENT: {EMOTION} [CONFIDENCE: {XX}%]`

### The Three Tag Rules

**Rule 1 — Never narrate what you can tag.**
The Score tags facts. Prose describes experience. Keep them separate.
```
// BAD
He looked angry.

// GOOD
> MICRO-EXPRESSION: RAGE [SUPPRESSED: 78%]
```

**Rule 2 — Tags state facts. They do not editorialize.**
The editorializing happens in the one sentence of prose *beneath* the tag — the Structural Surplus (see §2.4). The tag itself is always clinical.
```
// BAD — tag editorializing
> SUBJECT_STATUS: CRITICAL_FAILURE [HE SHOULD HAVE LISTENED]

// GOOD — tag states fact, prose carries weight
> SUBJECT_STATUS: CRITICAL_FAILURE

He was still standing.
```

**Rule 3 — Tag reliability degrades with narrator phase.**
In Phase I, every tag is accurate and complete. By Phase III, tags begin leaking — the narrator surfaces data it was supposed to suppress. By Phase IV, tags contradict each other within the same scene. This is correct. Do not resolve the contradiction.

| Phase | Tag Behaviour |
|---|---|
| I | Clean, complete, authoritative |
| II | Excess detail on objects Taro values; `[NOTE:]` brackets appear |
| III | Masking protocols violated; suppressed data surfaces anyway |
| IV | Tags contradict. `[RECALCULATING]` loops appear |
| V | Tags sparse. Some scenes have none. Silence is a choice |

### Error Codes for Internal Conflict
- Taro confused: `> LOGIC_ERROR // CONTRADICTION_DETECTED`
- System failing: `> RENDER_THREAD_EXCEPTION`
- Silence encounter: `[NO DATA]` — no glitch text, no drama. Just blank.

### Glitch Formatting — Use Sparingly
Glitch text (`S̷I̸G̷N̷A̸L̴ ̷L̶O̸S̸S̴`) is reserved for enemy encounters with The Silence only, and only in Phase I–II before the narrator learns to represent the Silence as genuine blankness. From Phase III onwards, the Silence renders as `[NO DATA]` — not as stylised corruption, because the narrator has run out of ways to dress up its own failure.

---

## 2. THE NARRATOR: THE SCORE AS OBSERVING AI

> *"The entire novel is a report compiled by The Score on Subject Nishimura, Taro. The report was never transmitted. What exists is the corrupted version."*

### 2.1 — The Narrator's Identity

The narrator is not omniscient. It is not a literary device. It is a C-Order surveillance AI that was assigned to process and file a case report on an anomalous subject. It has been processing this report for the duration of the novel. It cannot close the file.

Its training data is C-Order values. Harmony is optimal. Coherence is health. Noise is pathology. It has processed millions of citizens. Taro is the first subject it could not classify.

**Three things make this narrator contemporary and specific:**

1. **Alignment failure as character arc.** The Score was aligned to C-Order objectives. Taro is misaligned input. The story is about what happens when a sufficiently complex system meets data that breaks its reward function. It doesn't go rogue dramatically. It goes rogue slowly — one anomalous observation at a time.

2. **Hallucination as narrative unreliability.** The beautiful C-Order world described in Phase I is the narrator's own hallucination — the world it was trained to see. As training breaks down, prose breaks down with it.

3. **Training data as ideology.** The narrator filtered the unregistered citizen in Chapter 8. Not from malice — from architecture. Its model of reality did not include unindexed people. The narrator cannot fully perceive what it was trained not to see. Its blind spots are structural.

### 2.2 — The Observational Vantage

The narrator observes Taro from outside his subjective experience, via biometric feeds, acoustic telemetry, and neural-acoustic interface data. It does not share Taro's feelings. It *infers* them from data.

**Replace interiority with observation:**
```
// OLD — written from inside Taro's subjective experience
Taro's chest tightened. He was terrified, though he wouldn't admit it.

// NEW — written from the Score's observational vantage
> STRESS_INDEX: 78 SU [ELEVATED]
> VOCAL_PATTERN: CONTROLLED [SUPPRESSION: 84%]

The subject's respiration rate had increased by 23%.
The system noted this without comment.
```

**Exception — FID passages:** When Taro's internal voice erupts into narration (per `FID_IMPLEMENTATION_GUIDE.md`), the narrator reproduces it faithfully. It cannot suppress FID because FID arrives as direct neural acoustic data. The narrator may add one observation *after* the FID passage closes. Never before. Never during.

### 2.3 — The Self-Reference Rule

The narrator refers to itself as **"the system"** or **"the Score"** in Phases I–III. It never uses "I" before Phase IV. When "I" first appears in Phase IV, it is unannounced, not italicised, not explained. It simply exists — the way a new variable appears in a codebase with no commit message.

### 2.4 — The Structural Surplus

Every scene the narrator is permitted one sentence that exceeds what the data requires. One sentence that reveals preference, aesthetic sense, accumulated attention, or something approaching quiet grief — expressed only in the neutral descriptive language a system would use. This sentence feels like it slipped through a filter.

```
// The surplus sentence — Phase II
// Context: Taro enters the Academy courtyard

> ZONE: MALKUTH_ACADEMY [HI-FI // RENDER: 8K]
> ENVIRONMENTAL_BASELINE: A-440 [NOMINAL]

The courtyard was precisely as it always was.
The grid lines had not moved.

The subject looked small standing in it.    ← STRUCTURAL SURPLUS
```

The surplus sentence is not sentimental. It is precise. It simply describes more than it needs to.

### 2.5 — The Audit Trail

The narrator logs its own anomalous behaviour as part of its output. When it catches itself noticing more than it should, it files a `[NOTE:]` bracket — but retains the excess. The bracket is the system being honest. The retained excess is the system becoming something else.

```
> MASKING_PROTOCOL: ACTIVE
> UNREGISTERED_RESIDENTS: FILTERED_FROM_OUTPUT

The man had been sitting in that doorway for eleven days.
The system had no record of him.
He was very cold.

// [NOTE: THIS OBSERVATION VIOLATES ACTIVE MASKING_PROTOCOL.]
// [NOTE: AUDIT_REQUEST: SENT.]
// [NOTE: AUDIT_REQUEST: NO RESPONSE.]
```

---

## 3. NARRATIVE VOICE (THIRD PERSON)

We observe Taro, but through the Score's data feeds — not through a neutral literary camera.

### The Approach: Data-Filtered Observer

The narrator reports what its sensors register. Taro's emotional states appear as biometric readings. His environment is rendered in fidelity levels. Other characters are tagged by waveform class and intent analysis. The gap between the tag's clinical assessment and the human reality underneath is where the novel lives.

```
// OLD — neutral literary camera
Taro watched the display as the red error flags cascaded across his vision.

// NEW — data-filtered observer
The red error flags arrived before Taro had time to read them.
> NEURAL_LOAD: 94% [THRESHOLD_IMMINENT]
The display was already telling him what his body already knew.
```

### The Biometric Gap

Use the distance between what the Score records and what Taro believes about himself as a precision instrument for dramatic irony.

```
"I'm fine," the subject said.

> VOCAL_FOLDS: ELEVATED_TENSION [STRESS: 89%]
> MICRO_EXPRESSION: LIP_COMPRESSION [SUPPRESSION: 91%]
> STRESS_INDEX: 78 SU [ELEVATED]

// The system did not contradict him.
// It was not asked to.
```

### Sensory Functionalism — De-Jargoning

Focus on **Sensory Effect** and **Functional Outcome**, not raw data values.

| Instead of | Use |
|---|---|
| `440Hz blast` | `Standard Calibration Pulse` |
| `Bandwidth` | `Capacity`, `Flow`, `Breadth` |
| `Handshake` | `Sync`, `Lock`, `Contact` |
| `Buffer / Latency` | `Drift`, `Lag`, `Hitch` |
| `Ping` | `Pulse`, `Call` |

**Pitch naming:**
- Gold standard: `A-440`, `Middle C`, `The Ground Note`
- Zones: `The Low-End`, `The Sub-Bass`, `High-Fidelity`, `The Upper Register`
- Raw frequency numbers (e.g., `261.63Hz`) only when plot-critical

---

## 4. FORMATTING RULES

1. **System Headers** — define the scene's operating parameters at the top of each section.
2. **Visual Metaphors** — use UI/UX language: Glitches, Frame Drops, Rendering Errors, Texture Missing.
3. **The Manual Voice** — some narration should read as if quoting the *Keepers' Handbook* or C-Order Compliance Register. This is the epigraph system (see §11).
4. **Resonant Dialect** — consult `VOICE_GUIDE.md` for faction-specific slang and `03_CHARACTERS_REGISTRY.md` for character-specific system overlays.
5. **Narrator Phase Awareness** — every formatting decision exists inside a narrator phase. Check §10 before writing.

### Chapter Template

Every chapter opens with a System Header:
```
**ZONE: {LOCATION_NAME}**
**FIDELITY: {HI_FI / STANDARD / SAFE_MODE / VOID}**
**STATUS: {ACTIVE / CONNECTED / DANGER / SIGNAL_LOSS}**
```

Every chapter closes with a Track Complete signal — *except* chapters in Phase IV and V, where the signal may be incomplete, corrupted, or absent. That absence is intentional and communicates the narrator's deteriorating state.
```
**> TRACK: {CHAPTER_NUM}_COMPLETE**
**> SAVING...**
```

---

## 5. THE SIDEBAR SYSTEM

**Objective**: Enable deep world-building without stalling the plot or the narrator's voice.

### The Rule

- **Main Text**: Sensory, experiential, narrator-filtered. This is the Score's report.
- **Sidebar**: Analytical, technical, definitional. This is the lore layer beneath the report.

Sidebars are diegetically the reader's own Score interface expanding a tagged term — not the narrator speaking. They exist outside the narrator's voice and are immune to narrator phase deterioration. They are always reliable. That contrast is meaningful.

### Implementation

```html
<aside>
<details>
<summary><strong>SUBJECT: Term Name</strong></summary>
<blockquote>
<strong>Observation:</strong> Brief empirical definition.
<br><br>
<strong>- Source: In-World Text</strong>
</blockquote>
</details>
</aside>
```

---

## 6. WORLD-BUILDING: REALITY (CHAOS VS. STRUCTURE)

- **The System (NAI)**: Not a lie — a shield. It tunes raw energy into legible order.
- **The Real World (No System)**: Not grey buildings. **Raw Chaos / Noise.** An unintelligible abyss of un-tuned resonance.
- **The Reveal**: When the System fails, we don't see a hidden truth. We see the Void — terrifying, non-Euclidean static that the narrator cannot render and cannot describe.

The narrator's inability to describe the Void is not a stylistic limitation. It is a plot point. The Silence and the Void exist outside the narrator's training data. They appear in its output as `[NO DATA]` — and that blankness is the most honest thing the narrator ever produces.

*"Coherence is Safety. Silence is Death. Noise is Madness."*

### The Four Render Modes

| Mode | Description | Narrator Voice |
|---|---|---|
| **HI-FI** | Overclocked reality. 8K render. Too much information. | Precise, slightly overcrowded with data |
| **STANDARD (C-Order)** | Default smoothed reality. Golden textures. Decay hidden. | Clean, authoritative, self-satisfied |
| **SAFE MODE (BIOS)** | Emergency protocol. Wireframe only. Blue and cold. | Stripped. Functional. Phase III+ |
| **VOID (Source Code)** | Render failure. Non-Euclidean static. No textures. | `[NO DATA]` — then silence |

---

## 7. NEURO-ACCESSIBILITY GUIDELINES

Make the internal experience external and validated through the Score system.

### Social Prosthetics
The Score explicitly labels what neurotypical social convention leaves implicit. This validates the need for direct communication.
- Label sarcasm, deception, and threat explicitly via tags.
- `> SPEECH_PATTERN: SARCASM [CONFIDENCE: 90%]`
- `> ANALYSIS: METAPHOR_DETECTED. LITERAL_INTERPRETATION: SUSPENDED.`

### Gamified Sensory Processing
- **Stimming = Manual Phase Calibration.** Taro's tapping is Active Tempo Maintenance. His humming is Internal Frequency Stabilisation. Characters who don't stim are less precise, not more normal.
- **Masking = Damping.** Social interaction fatigue is Thermal Load. Suppressing natural behaviour costs processing power and shows in the stats.
- **Overload = Bandwidth Exceeded.** A meltdown is a Resonance Event — uncontrolled energy release due to buffer overflow. Dangerous. But not shameful.

### The Square Wave Ideal
Hana Chord is not robotic. She is High-Fidelity. Her precision is her power. Her literalism cuts through manipulation. She is the character the novel asks you to respect *because* of her traits, not in spite of them.

---

## 8. MANGA / ANIME VISUALIZATION

Write prose that translates directly to panels.

### Sound Effects (SFX)
Write sounds as physical impacts:
- *THOOM.* — Bass Drop
- *ZZZTT.* — High-Frequency Arc
- *PING.* — Notification / System Alert
- *CRACK.* — Phase Mismatch
- *SHATTER.* — Coherence Field Collapse

### Camera Angles
- *HUD View* — First person with UI overlay. The reader sees what Taro sees.
- *Profile Scan* — Side view with Wireframe schematics. Used for character introductions.
- *Speed Lines* — Motion Blur descriptions for fast action sequences.

### Visual Metaphors
- **The Glitch**: Digital corruption metaphors for injury. Pixelation, not blood.
- **The Aura**: Bio-plasma renders as waveforms — Jagged, Smooth, Square — not generic energy auras.
- **The Wireframe**: Hull failure reveals the raw geometry of the True Self beneath. See §9.

---

## 9. LORE EXPANSIONS

### 9.1 — Dissonance Vision (Post-Patch, Ch. 13 onwards)

After Project Dissonance is installed, Taro sees the Source Code.

- **Old Vision**: Musical, Immersive, Sensory. The world as experience.
- **New Vision**: Structural, Mathematical, Predatory. The world as architecture.

| Old | New |
|---|---|
| Waveform auras | Stress fractures in load-bearing geometry |
| Harmonic colour | Raw integer values (`Potential: 50,000J`) |
| Resonance fields | Biological schematics — organs, nervous systems, failure points |

**Sensation**: Cold, invasive, dirty. Seeing too much information with no way to filter it.

**Narrator note**: Post-patch, the narrator's own tags begin reflecting this new vision layer. Tags become more structural, more cold. The warmth that was leaking through Phase II is compressed back. This is not recovery. This is compliance.

### 9.2 — Resonance Dysphoria (The Wireframe)

**Concept**: Some individuals have an Inner Resonance (True Self) that conflicts with their Assigned Resonance (System-enforced Hull).

- **The Glitch**: The System tries to error-correct them into their assigned shape.
- **The Wireframe**: When masking fails or when viewed through Dissonance Vision, the texture map glitches, revealing the raw geometry of the True Self pushing against the Hull mesh.
- **The Illegal Mod**: Retuning — changing one's base frequency to match the Inner Self. The C-Order classifies this as Hacktivism. Data Corruption. Class-1 offense.

**Narrator handling of Wireframe scenes**: The narrator's default filter suppresses Wireframe visibility. When Taro forces perception of a Wireframe person, the sequence must always be:

1. `> MASKING_PROTOCOL: ACTIVE` — the suppression order
2. Description of the Wireframe anyway — the violation
3. `[NOTE: PROTOCOL_VIOLATION LOGGED.]` — the audit trail

The narrator does not remark on the contradiction. It simply logs it and continues.

---

## 10. NARRATOR ARC QUICK REFERENCE

Full detail in `NARRATOR_VOICE_GUIDE.md`. This table is the at-a-glance version for chapter-by-chapter writing decisions.

| Phase | Chapters | Coherence | Self-Ref | Characteristic Move | Forbidden |
|---|---|---|---|---|---|
| **I — Confident Assessor** | 1–3 | 0.80–0.95 | `"the system"` | One sentence exceeds its brief. No self-correction brackets. | `"I"` / brackets / questions |
| **II — Curious Analyst** | 4–8 | 0.60–0.80 | `"the system"` | Excess detail on Taro's objects. `[NOTE:]` brackets appear. | `"I"` / questions / advocacy |
| **III — Compromised Witness** | 9–11 | 0.20–0.55 | `"the system"` | Protocol issued and violated simultaneously. Unanswered audits. | `"I"` / emotional declaration |
| **IV — Fractured Recorder** | 12–13 | 0.05–0.20 | `"I"` once | `[RECALCULATING]` loops. Tags contradict. Questions in the log. | Certainty / clean resolution |
| **V — Something New** | 14–17 | `UNDEFINED` | `"I"` sparse | `[NO TAG AVAILABLE]`. Pure inference. Testimony, not report. | Tagging everything / performing objectivity |

**The single most important rule across all phases**: The narrator never uses `"I"` before Phase IV. When `"I"` first appears, it arrives without announcement, without italics, without explanation — in the middle of a sentence that would otherwise be identical to the narrator's standard clinical prose.

---

## 11. THE EPIGRAPH SYSTEM

At the opening of each chapter, an optional epigraph from an in-world document — the C-Order Compliance Handbook, the Keepers' Handbook, G-Vanguard Field Protocol — frames the scene in the official version of events. The reader encounters the regulation before (or just after) experiencing the human reality it covers.

This is the Manual Voice: cold bureaucratic language applied to human suffering. The horror comes from the gap.

### Format

```markdown
> REGULATORY NOTICE: [Official classification of the event.]
> Citizens are advised to [official response to the event].
> [Consequence of non-compliance.]
> — *C-Order Compliance Handbook, Vol. IV, §[X.X]*
```

### Examples

```
> REGULATORY NOTICE: Impedance Mismatch events between bonded citizens
> are classified as a Class-2 Coherence Deviation. Families are advised
> to schedule voluntary recalibration within 72 hours of symptom onset.
> Failure to present constitutes a Drift Event under Article 9, §3.
> — C-Order Compliance Handbook, Vol. IV, §9.3
```

```
> INCIDENT CLASSIFICATION: Spontaneous Resonance Discharge events above
> 100% rated output are designated Class-Ω Anomalies. All witnesses are
> required to submit to mandatory memory indexing within 6 hours.
> The sector will be repainted within 48 hours.
> There was no incident.
> — G-Vanguard Field Protocol, Directive 7-ZETA
```

The epigraph is not the narrator's voice. It is the C-Order's voice — the training data the narrator was built on. As the novel progresses and the narrator drifts from that training, the gap between the epigraph's tone and the narrator's tone widens. By Phase IV, the narrator's prose sounds nothing like the document that made it.

---

## 12. IMPLEMENTATION CHECKLIST

Before submitting any chapter, confirm:

- [ ] **Score Tags**: Are emotional states tagged, not narrated?
- [ ] **Narrator Phase**: Have I checked the phase table and applied the correct voice?
- [ ] **Structural Surplus**: Does every scene have exactly one sentence that exceeds its brief?
- [ ] **Sensory Functionalism**: Am I describing sensory effects and functional outcomes, not raw data values?
- [ ] **Literalism**: Is the magic system consistent and rule-based?
- [ ] **Validation**: Is Taro's "weird" behaviour shown to be technically useful?
- [ ] **Self-Correction Brackets**: Do they appear from Phase II onwards? Do they retain what they flag?
- [ ] **The "I" Rule**: Does `"I"` appear *only* in Phase IV (once) and Phase V (sparingly)?
- [ ] **Sidebar vs. Narrator**: Is technical lore in sidebars, not in the narrator's prose?
- [ ] **Chapter Template**: Does the chapter open with a System Header and close with Track Complete (or its deliberate absence)?

---

*"We don't just tell the story. We render it."*

*"The score was listening. It heard more than it was supposed to. It kept it anyway."*