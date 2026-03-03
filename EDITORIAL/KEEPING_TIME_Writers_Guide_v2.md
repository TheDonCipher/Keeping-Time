# WRITER'S GUIDE v2.0 — KEEPING TIME
## The AR Manuscript: Style, Format & World Rules

> **Version**: 2.0 — Updated after Volume One editorial review
> **Supersedes**: `WRITER_GUIDE.md` (v1.0)
> **Changes from v1**: Section 1 HUD rules expanded with confirmed violations list; Section 2 neuro-accessibility rules tightened; Section 3 manga direction augmented with Volume One examples; Section 4 networking jargon list expanded; new Section 8 (Dissonance Vision); new Section 9 (Resonance Dysphoria); new Section 10 (Known Open Decisions).
> **Tone target**: "Hard System" Magic × "Sensory Overload" Cyberpunk
> **Accessibility target**: Neurodivergent-Friendly (Explicit Systems, Validated Stimming)
> **Format target**: Manga/Anime adaptation ready — all chapters must support panelling without additional direction

---

## 1. THE SCORE: FORMATTING RULES

The AR Interface ("The Score") is a character. It is not decoration. It speaks in **Data**. It perceives what Taro perceives. It fails when Taro fails. It must be present in every waking scene in Phases I–III, thinning gradually through Phase IV, and sparse but precise by Phase V.

---

### 1.1 — Approved Tag Structure

All HUD output follows this exact pattern:

```
> KEYWORD: VALUE [Modifier]
```

- **KEYWORD**: ALL-CAPS, no spaces, underscores for compound terms
- **VALUE**: ALL-CAPS or numeric, precise, clinical
- **[Modifier]**: optional, in brackets, e.g. `[CRITICAL]`, `[SUPPRESSED]`, `[CONFIDENCE: 94%]`

Multiple simultaneous outputs use line-break stacking, not concatenation:
```
> BIOMETRIC: CORTISOL_SPIKE [+400%]
> MICRO-EXPRESSION: CONTEMPT [SUPPRESSED]
> THREAT_LEVEL: ELEVATED
```

---

### 1.2 — HUD Rules (Binding)

**Rule 1 — Never narrate what you can tag.**
- ❌ *Bad*: "He looked angry."
- ✅ *Good*: `> MICRO-EXPRESSION: RAGE [SUPPRESSED]`

**Rule 2 — Use Error Codes for internal conflict, not internal monologue.**
- ❌ *Bad*: `> THOUGHT: CONFUSED`
- ✅ *Good*: `> LOGIC_ERROR // CONTRADICTION_DETECTED`

**Rule 3 — Glitch Text for horror and Silence sequences only.**
```
> SI_GNAL L__OSS // N_ULL
> PR_OCES_SING...
> B_UFFER [C_ORRUPT]
```
Do not use glitch formatting for dramatic effect in non-horror sequences. It must remain a specific register.

**Rule 4 — The one-to-one rule: pick one channel per piece of information.**
If a character's emotion is described in prose, do not repeat it in HUD. If it is tagged by HUD, do not also narrate it. One delivery channel per datum.

**Rule 5 — HUD density tracks Phase.**
- Phase I (Ch. 1–3): Dense. Reader is being onboarded to the dual-register format.
- Phase II (Ch. 4–8): Full but efficient. Tags become more precise as Taro's system matures.
- Phase III (Ch. 9–11): Degrading. Tags begin corrupting, missing, or returning null.
- Phase IV (Ch. 12–14): Fragmentary. System is post-compliance patch — stripped, clinical, cold.
- Phase V (Ch. 15–17): Sparse and earned. Only tags that matter survive.

Chapters 6–11 of Volume One were written with minimal or absent HUD. This is a known gap. When revising, reintroduce HUD at Phase-appropriate density — environmental headers alone do not substitute for The Score's active presence.

---

### 1.3 — SENSATION: Tag Rule (Resolved)

`SENSATION:` as a prefix is **prohibited** because it is too soft and emotional for a clinical system.

**Two confirmed exceptions only:**
```
> SENSATION: INTEGER_OVERFLOW    ✅ permitted — technically precise
> SENSATION: NULL                ✅ permitted — technically precise
```

All other `SENSATION:` instances must be replaced. Reference table:

| Prohibited | Replace with |
|---|---|
| `> SENSATION: PAIN` | `> STATUS: NERVE_DAMAGE [CRITICAL]` |
| `> SENSATION: NAUSEA` | `> BIOMETRIC: VAGAL_RESPONSE [SIGNAL: CORRUPTED]` |
| `> SENSATION: BOOT_SEQUENCE` | `> PROCESS: NAI_BOOT [STAGE: 1/3]` |
| `> SENSATION: GOLDEN_SYRUP` | `> AMBIENT: MIDDLE_C [EFFECT: ENTRAINMENT]` |
| `> SENSATION: FREE_FALL` | `> STATUS: LIMITER_REMOVED [AMPLITUDE: UNCAPPED]` |
| `> SENSATION: BURNING_WIRE` | `> STATUS: THERMAL_LOAD [REGISTER: HIGH // RATE: CRITICAL]` |

---

### 1.4 — Confirmed Exemplary HUD Sequences (Preserve)

These Volume One tags are correctly executed and should serve as format references:

```
> LOGIC_FAILURE / EMOTIONAL_OVERRIDE                        ← Ch. 1 — dual-register conflict
> QUERY: AYANE_NISHIMURA / ERROR: FILE_CORRUPTED            ← Ch. 3 — institutional absence as horror
> OBJECT_ANALYSIS: UNKNOWN_TECH [CONNECTIVITY: NONE]        ← Ch. 3 — headphones
> AUDIO_PROTOCOL: BYPASS [INPUT_SOURCE: ANALOG_DIRECT]      ← Ch. 3 — headphones silence sequence
> OPPONENT: MARCUS_STACCATO / CLASS: RHYTHM_OPERATOR        ← Ch. 7 — character introduction
> VISUAL_ARTIFACT: FRAME_SKIP                               ← Ch. 7 — Marcus's movement type
> INTERFERENCE: DESTRUCTIVE / ATTACK: NULLIFIED             ← Ch. 7 — physics result
> ENEMY: [REDACTED_ANOMALY] / SIGNAL: ABSOLUTE_SILENCE      ← Ch. 8 — The Silence
> V2.0 DIAGNOSTICS / SIGNAL: MASKED                        ← Ch. 14 — post-compliance system
> SENSATION: INTEGER_OVERFLOW                               ← permitted exception
```

---

### 1.5 — Prohibited HUD Jargon (Networking Terms)

These terms appear in Volume One and must be swept in revision:

| Prohibited | Replace with |
|---|---|
| `> CONNECTION: ESTABLISHED` | `> SYNC: LOCKED [STATUS: STABLE]` |
| `> LATENCY: 0ms` | `> DRIFT: ZERO [LOCK: CONFIRMED]` |
| `> HANDSHAKE: COMPLETE` | `> LINK: ESTABLISHED` |
| `BANDWIDTH` (in any context) | `CAPACITY`, `FLOW`, `BREADTH` |
| `PACKETS` (in any context) | `SIGNAL`, `DATA_STREAM`, `PULSE` |
| `PING` (as HUD term) | `PULSE`, `CALL` |

**Note on Chapter 5**: The training sequence currently reads `> CONNECTION: ESTABLISHED / > LATENCY: 0ms` — both are violations. Revise to `> SYNC: LOCKED [DRIFT: ZERO]`.

---

## 2. NEURO-ACCESSIBILITY GUIDELINES

Make the internal experience external and validated. These rules are design requirements, not stylistic suggestions.

---

### 2.1 — Social Prosthetics

Autistic readers may not read subtext easily. The Score does it for them explicitly. This is not a cheat — it is the core accessibility feature of the book's format.

- Label Sarcasm, Deception, and Threat explicitly in HUD.
- The Score's clinical precision validates the autistic need for direct communication by making the system the ultimate direct communicator.
- When the Score correctly identifies deception that a character has been told to trust, it creates narrative irony that rewards neurodivergent readers specifically.

---

### 2.2 — Gamified Sensory Processing

| Experience | Framing (Correct) | Framing (Prohibited) |
|---|---|---|
| Stimming (leg bounce, tapping) | `> MOTOR_LOOP: ACTIVE [FUNCTION: CALIBRATION]` | "He couldn't stop fidgeting" |
| Masking | `> DAMPING: ACTIVE [THERMAL_LOAD: HIGH]` | "He forced himself to act normal" |
| Sensory overload | `> BANDWIDTH_SATURATED [INPUT: 14_CHANNELS]` | "He was overwhelmed" |
| Meltdown | `> RESONANCE_EVENT [THRESHOLD: EXCEEDED]` | "He lost control" |
| Post-mask exhaustion | `> CPU_DRAIN [RESERVE: 12%]` | "He was drained from pretending" |

**Never use "can't help it," "struggled to understand," or "couldn't stop himself" as deficit framing.** These phrases frame neurodivergent traits as failures of will. Reframe all instances as system states — hardware responding to conditions.

---

### 2.3 — The "Square Wave" Ideal

Hana Chord is the book's neurodivergent hero archetype. Her hyper-systemizing is portrayed as genuine, high-fidelity competence — not a limitation waiting to be overcome by emotional growth.

- Her rigidity is not a flaw to be "fixed" by contact with Taro.
- Her development of "Fuzzy Logic" is cognitive *expansion* — gaining new processing modes — not the replacement of her square-wave nature with something softer.
- Her literalism cuts through deception in ways emotionally intuitive characters cannot. This must be demonstrated in plot consequences, not merely stated.

---

### 2.4 — Remi's "Glitch" Nickname (Open Question)

In Chapter 1, Remi Sato uses "Hey, Glitch" as an address for Taro. This could read as deficit-language. Resolution path: Remi's nickname must become clearly *reclaimed* language by Ch. 6–8, functioning as a badge of distinction rather than a slur. If Remi does not reappear to fulfill this arc, consider whether the nickname should be removed from Ch. 1. See Section 10 (Open Decisions).

---

## 3. MANGA/ANIME VISUALIZATION

Every chapter must support panelling without additional direction from the author. Write prose that translates directly to panels.

---

### 3.1 — Panel Direction (Sound Effects)

Sound effects are written as **physical impacts** in italics or bold, not as descriptions:

| Effect | Correct | Prohibited |
|---|---|---|
| Bass impact | *THOOM.* | "a deep boom" |
| High-freq arc | *ZZZTT.* | "a crackling sound" |
| Notification | *PING.* | "a chime" |
| Baton strike / beat | *CRACK.* (with resonance description) | "he hit him" |
| Resonance collapse | *THOOM.* + `> INTERFERENCE: CONSTRUCTIVE` | describing the physics in prose |

---

### 3.2 — Camera Angles

Signal clearly in prose which visual mode the scene is in:

| Mode | Signal phrase | Use for |
|---|---|---|
| HUD View | "Through his lens..." / "The overlay positioned itself..." | Taro actively reading the Score |
| Profile Scan | "The wireframe assembled itself around [name]..." | Introducing/assessing a character |
| Speed Lines | "Marcus was already in the next pulse" / "The frame couldn't hold him" | Fast combat, frame-skip movement |
| Wide Establishing | "The [location] sprawled..." / "Five hundred cadets sat in concentric rings" | Environment introduction |
| Extreme Close-Up | Single sensory detail filling the prose frame | Emotional apex, manga-beat moment |

---

### 3.3 — Visual Metaphors (Binding)

| Concept | Required visual language | Prohibited |
|---|---|---|
| Injury / damage | Digital corruption — pixelation, greyscaling, frame drops | Blood, gore, bruising language |
| Bio-plasma aura | Waveform shape — jagged (sawtooth), smooth (sine), blocky (square) | "glowing energy," "aura," "power" |
| The Silence | Void, negative space, absolute absence of data | An army, a presence, an opposing force |
| Resonance Event | System crash, blue screen, signal loss | Emotional breakdown, crying, rage |
| Masking fatigue | Thermal dump, cooling vents, copper smell, CPU drain | Being tired, needing rest |

---

### 3.4 — Confirmed Volume One Manga Beats (Reference)

These beats executed well and define the standard:

- **Ch. 1** — God Ray (880Hz) erupting from Taro's hand — designated splash page
- **Ch. 3** — Analog Headphones scene — HUD silence, Taro finding Sawtooth Oscillation in the quiet — Phase I emotional apex
- **Ch. 7** — Marcus moving faster than the frame rate: `> VISUAL_ARTIFACT: FRAME_SKIP`
- **Ch. 8** — The Silence first contact: `> ENEMY: [REDACTED_ANOMALY] / > SIGNAL: ABSOLUTE_SILENCE`
- **Ch. 12** — "The screaming in his head suddenly stopped" + `> WELCOME_BACK_USER`
- **Ch. 14** — V2.0 Diagnostics — stripped interface, no harmonics, no melodies

Beats that are planned but unconfirmed executed in prose (verify in chapter):
- **Ch. 2** — Voss eye glitch, one frame green — ⚠️ MISSING from draft
- **Ch. 4** — Room rotating 90 degrees when Headmaster speaks
- **Ch. 5** — Bass Drop shockwave clearing the Sandbox
- **Ch. 6** — Steam venting from Ven's armor vents

---

## 4. VOCABULARY & REGISTER

---

### 4.1 — The Book's Approved Sound Vocabulary

Use these terms naturally. They are the world's vocabulary, not technical jargon:

| Category | Terms |
|---|---|
| Reference pitch | A-440, Middle C, The Ground Note, Standard Pitch |
| Frequency zones | The Low-End, The Sub-Bass, High-Fidelity, The Upper Register |
| Resonance states | Calibration, Damping, Phase Lock, Interference, Constructive/Destructive |
| Character abilities | Variable Oscillation (Taro), Phase Lock (Hana), Grounding Discharge (Ven), Rhythm Cage (Marcus) |
| System states | Buffer, Thermal Load, Resonance Event, Signal Loss, Octave Drop |

### 4.2 — Prohibited Networking Jargon (Full List)

Must not appear in prose or HUD without substitution:

| Prohibited | Use instead |
|---|---|
| Bandwidth | Capacity, Flow, Breadth |
| Handshake | Sync, Lock, Contact |
| Latency / Buffer | Drift, Lag, Hitch |
| Ping | Pulse, Call |
| Packet | Signal, Data-stream, Pulse |
| Connection (as networking term) | Link, Lock, Bond |
| Download / Upload | Receive, Transmit |
| Server | Grid, Node, Anchor |

---

## 5. THE SIDEBAR SYSTEM

**Objective**: Enable deep world-building without stalling narrative momentum.

| Channel | Content type | Rule |
|---|---|---|
| Main narrative text | Sensory, emotional, experiential | No lore exposition |
| HUD / The Score | Clinical, system-derived data | Tagged format only |
| Sidebar / Tooltip | Analytical, technical, definitional | Delivered via `[[Term::Definition]]` syntax in HTML chapters |

### Sidebar Syntax

```html
[[Term::Definition sentence. Single observation. In-world register.]]
```

Example from Volume One (correct):
```
Ven was a [[Sink::A heavy-class resonator designed to absorb and ground 
incoming kinetic/acoustic energy, converting it to waste heat or stored 
bass potential.]]
```

Rule: sidebars define terms the reader has already encountered in action. They never introduce concepts. The concept must appear first; the sidebar clarifies.

---

## 6. WORLD-BUILDING: THE REALITY LAYER

- **The System (NAI)**: Is not a lie. It is a shield. It renders raw resonance energy into coherent, navigable reality ("Music/Order"). Without it, reality is not "ugly but true." It is **unintelligible chaos.**
- **The Real World (No System)**: Is not a slum beneath the golden textures. It is **Raw Noise** — a non-Euclidean abyss of un-tuned resonance that the human nervous system cannot process.
- **The Reveal**: When the System fails, the reader does not see the truth of poverty and corruption (that is present but it is a surface truth). They see the **Void** — terrifying, non-representational static.

*"Coherence is Safety. Silence is Death. Noise is Madness."*

This distinction is critical for Phase III. When Taro's Safe Mode filters drop, what he sees is not simply "the real world stripped of propaganda." He sees the real resonance topology — and it is overwhelming precisely because his Irregular/Glitch nature allows him to perceive what others' systems filter out.

---

## 7. FACTION DIALECTS

Dialogue must distinguish faction membership before character name is given. Each faction has a legible voice:

| Faction | Voice style | Key terms | Sample |
|---|---|---|---|
| C-Order (Standard Pitch) | Clinical, authoritative, HR-speak for the soul | Calibration, Compliance, Harmony, Standard, Deviation | *"Your current behavior is a 3-decibel deviation from community standards. Please recalibrate or face damping."* |
| G-Vanguard (Military Tempo) | Terse, rhythmic, action-driven | Vector, Tempo, Impact, Deployment, Overwatch | *"Target locked at 440Hz. Shift phase on the fourth beat. Go!"* |
| Flux Syndicate (Glitch/Pirate) | Fragmented, slang-heavy, analog-cool | Static, Noise, Feedback, Raw, Unfiltered | *"Forget the gold lines. The raw signal is where the truth is."* |
| The Underground (The Null) | Stripped, architectural, sparse | Wireframe, Hull, Modulation, True Form | *"The hull is just a suggestion. Beneath the armor, we are all just light and math."* |

---

## 8. PHASE V UPDATE: DISSONANCE VISION (POST-PATCH, CH. 13+)

After "Project Dissonance" is installed in Chapter 13, Taro's HUD and perceptual system changes fundamentally:

**Old Vision (Ch. 1–12):** Musical, immersive, sensory. Waveform auras, harmonic overlays, emotional resonance tagging.

**New Vision (Ch. 13–17):** Structural, mathematical, predatory. Cold. Invasive. "Dirty" — seeing too much raw information.
- **Stress Lines**: Glowing fractures in objects and people where they are structurally weakest.
- **Raw Integers**: Potential energy values visible directly (e.g., *Potential: 50,000J*) instead of beautiful waveforms.
- **Biological Overlay**: Organs and nervous systems rendered as engineering schematics.

HUD in Phase V reflects this shift — less musical, more diagnostic. Compare Ch. 14's `> V2.0 DIAGNOSTICS / > SIGNAL: MASKED` against Ch. 1's rich sensory tagging. The poverty of the new interface is itself a character note about what compliance costs.

---

## 9. RESONANCE DYSPHORIA (THE WIREFRAME)

**Concept**: Some individuals have an "Inner Resonance" (True Self) that conflicts with their system-enforced "Hull" (Assigned Class/Appearance).

**Elara/Kimura** is the primary case in Volume One:
- Assigned hull: Kimura, Tank class — deep forced bass register
- True resonance: Elara — light, sharp, chiming treble, glass-winged construct
- The hull is not just a metaphor. It is experienced as a wrong frequency — a note her system forces her to play that is not her own.

**Writing rules for Resonance Dysphoria sequences:**
- Never frame the assigned hull as "wrong" in C-Order ideological terms. The C-Order believes her hull assignment is correct.
- Frame it in Taro's perception as a frequency mismatch — a note that isn't landing at its resonant frequency.
- When she is unmasked (Elara visible), write the shift as a tuning event, not a reveal. The frequency was always there; the hull was attenuation.
- Do not use "trapped" language. Use: misaligned, filtered, damped, running below resonant frequency.

---

## 10. OPEN DECISIONS (Require Author Resolution Before Phase II Revisions)

These items were identified during the Volume One editorial review and require explicit authorial decisions. The Writer's Guide cannot resolve them — they are structural choices.

| # | Decision | Context | Options |
|---|---|---|---|
| 1 | **SENSATION: tag rule** | 6+ instances of `SENSATION:` in Volume One violate the rule as written, but some (`GOLDEN_SYRUP`, `FREE_FALL`) have legitimate synesthetic intent | **Option A**: Replace all with clinical equivalents (recommended) · **Option B**: Revise rule to permit `SENSATION:` only for cross-modal synesthetic labels |
| 2 | **Chapter 1 POV cold open** | First 3 sentences are 2nd person ("It hits you... you aren't Taro Nishimura") before shifting to 1st person | **Option A**: Mark as intentional — add `> PROCESS: NAI_BOOT [STAGE: 1/3]` to frame it as the system addressing the user · **Option B**: Revise to consistent 1st person from line one |
| 3 | **Chapter 1 → 2 POV shift** | Ch. 1 is 1st person; Ch. 2 onward is 3rd person limited | **Option A**: Frame Ch. 1 as a recovered memory log with `> MEMORY_LOG: RETRIEVED [RELIABILITY: 73%]` at open · **Option B**: Accept as deliberate structural shift with no bridging |
| 4 | **Chapter title canonization** | 5 live chapter titles diverge from TOC titles | Author must declare canonical titles. Current: Ch. 7 → *The Architecture of Sound* vs TOC *The Rival*; Ch. 8 → *The Golden Filter* vs *The Sortie*; Ch. 9 → *The Blue Screen* vs *The Silence*; Ch. 10 → *The Unmasking* vs *The Breach*; Ch. 11 → *The Wire* vs *The Blue Screen*; Ch. 13 → *Reboot* vs *The Patch* |
| 5 | **Remi Sato's arc** | Remi appears in Ch. 1 as a vivid D-Major personality using "Hey, Glitch" as address. She does not reappear in Phase II. | **Option A**: Reintroduce Remi in Ch. 4 or 5 to fulfill the arc implied by Ch. 1 · **Option B**: Remove the "Hey, Glitch" nickname and trim Remi's Ch. 1 role to match her actual function |
| 6 | **Voss eye-glitch (Ch. 2)** | The chapter's designated manga beat is absent from the prose | This is not a decision — it requires addition. See Chapter Registry, Ch. 2 flags. |
| 7 | **Ayane Nishimura plant** | Mother's reveal in Ch. 3 (`> QUERY: AYANE_NISHIMURA / > ERROR: FILE_CORRUPTED`) arrives without prior seeding | Add one reference in Ch. 1 or Ch. 2: a maker's mark on a damping band, a signal signature Remi notes as unusual |

---

*Writer's Guide v2.0 — Keeping Time*
*Updated following Volume One editorial review*
*Cross-reference: `KEEPING_TIME_Chapter_Registry.md`, `KEEPING_TIME_HUD_Tag_Glossary.md`, `KEEPING_TIME_Analysis_Prompt_v2.md`*
