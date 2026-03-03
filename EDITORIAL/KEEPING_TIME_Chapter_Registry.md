# CHAPTER REGISTRY — KEEPING TIME, VOLUME ONE
## Canonical Per-Chapter Reference

> **Version**: 1.0 — Compiled from Master Outline, live manuscript HTML, and project knowledge chapters
> **Purpose**: Single source of truth for each chapter's planned specs vs. confirmed execution, with pre-identified editorial flags
> **Use with**: `KEEPING_TIME_Analysis_Prompt_v2.md` (Appendix D reference), `KEEPING_TIME_Chapter_Template.docx` (front matter)
> **Note on titles**: Several live chapter titles differ from the TOC. Both are recorded. Canonical title requires author decision (see Writer's Guide v2, Section 10, item 4).

---

## HOW TO READ THIS REGISTRY

Each entry contains:
- **Specs** (from Master Outline): what was planned
- **Execution** (from manuscript scan / project knowledge): what was written
- **Divergences**: where planned ≠ executed — these are not automatically errors; some divergences are improvements
- **Pre-identified flags**: issues confirmed by editorial review — bring these to the template before reading the chapter

---

## PHASE I — THE IMPULSE (Chapters 1–3)
**Physics**: A high-energy spike enters a stable system
**UI Theme**: "The Glitch" vs "The System"
**Expected prose texture**: Raw, disorienting, high-tension, unpredictable

---

### CHAPTER 1
| Field | Value |
|---|---|
| **Live title** | The Zap |
| **TOC title** | The Zap |
| **Title status** | ✅ Match |
| **Phase** | I — Impulse |
| **Est. word count** | ~2,134 |
| **Scene headers** | `[00:00:00] THE ZAP` · `[00:14:32] THE FLOOR` · `[00:14:45] THE CRASH` |
| **HUD presence** | ✅ Active |

**Planned (Master Outline)**
- Event: Taro's NAI boots up. He sees the "Wrong Note" as a code injection.
- AR Focus: Establishing the HUD, "The Stave" overlay, and "Buffer Overflow" errors.
- Manga Beat: The splash page of the "God Ray" (880Hz) erupting from his hand.

**Confirmed execution**
- NAI boot sequence present ✅
- God Ray climax present ✅ — but uses "pure sine-wave strike" language (see Flags)
- Crown icon classification present ✅
- Remi Sato introduced ✅ (uses "Hey, Glitch" as address)
- HUD opens with `> SENSATION: BOOT_SEQUENCE` (see Flags)
- Chapter uses `> LOGIC_FAILURE / > EMOTIONAL_OVERRIDE` — confirmed exemplary ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | God Ray described as "a pure sine-wave strike" — Voss's waveform type, not Taro's Irregular. Must be revised to aperiodic/sawtooth output. |
| 🔴 CRITICAL | `> SENSATION: BOOT_SEQUENCE` — prohibited prefix. Replace with `> PROCESS: NAI_BOOT [STAGE: 1/3]`. |
| ⚠️ HIGH | Chapter opens in 2nd person ("It hits you...") for 3 sentences, then shifts to 1st person. Intentionality unresolved — requires author decision (see Writer's Guide v2, §10 items 2–3). |
| ⚠️ HIGH | No seed for Ayane Nishimura (mother reveal lands in Ch. 3 without preparation). |
| ⚠️ HIGH | Remi Sato introduced vividly but does not reappear in Phase II. "Hey, Glitch" address requires arc resolution. |
| ⚠️ MED | Chapter ends at system crash with no post-climax sequel beat before blackout. Consider one line of internal state. |

---

### CHAPTER 2
| Field | Value |
|---|---|
| **Live title** | The Assessment |
| **TOC title** | The Assessment |
| **Title status** | ✅ Match |
| **Phase** | I — Impulse |
| **Est. word count** | ~1,140 |
| **Scene headers** | `[02:00:00] THE WHITE ROOM` |
| **HUD presence** | ✅ Active |

**Planned (Master Outline)**
- Event: Interrogation by Adjutant Voss in the "White Room."
- AR Focus: Social Tagging. Voss's deceptive "Safe" tags vs. Taro's "Threat" perception.
- Manga Beat: The extreme close-up of Voss's eye glitching green for one frame.

**Confirmed execution**
- White Room interrogation present ✅
- Compliance collar installed ✅
- Malkuth Academy destination established ✅
- Voss established as threat ✅
- Social tagging mechanic introduced ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | Designated manga beat (Voss eye glitch — one frame green, `> ANOMALY: DETECTED / > CLASSIFICATION: [REDACTED]`) is **absent from the prose**. Must be added at interrogation close. This is the Phase III double-agent foreshadowing plant. |
| ⚠️ HIGH | POV transition (1st person Ch. 1 → 3rd person Ch. 2) has no bridging device. Requires author decision on framing. |
| ⚠️ MED | No HUD tag for Taro's suppressed emotional spike during interrogation. Recommend: `> EMOTIONAL_SPIKE: SUPPRESSED [COLLAR: ACTIVE]`. |
| ⚠️ MED | Short chapter (~1,140 words). Verify this density is intentional (clinical coldness of White Room) rather than an incomplete draft. |

---

### CHAPTER 3
| Field | Value |
|---|---|
| **Live title** | Modulation |
| **TOC title** | Modulation |
| **Title status** | ✅ Match |
| **Phase** | I — Impulse |
| **Est. word count** | ~1,408 |
| **Scene headers** | `[20:01:15] THE DEAD ZONE` |
| **HUD presence** | ✅ Active |

**Planned (Master Outline)**
- Event: Taro says goodbye to Kael (Father).
- AR Focus: "Impedance Mismatch." Visualizing the static/distortion between them.
- Manga Beat: Kael handing over the Analog Headphones (Relic of the old world).

**Confirmed execution**
- Kael farewell present ✅
- Analog headphones gift present ✅ — `> OBJECT_ANALYSIS: UNKNOWN_TECH [CONNECTIVITY: NONE]` ✅
- Headphones silence sequence present ✅ — Phase I emotional apex ✅
- Ayane Nishimura reveal: `> QUERY: AYANE_NISHIMURA / > ERROR: FILE_CORRUPTED` ✅ — confirmed exemplary
- Thematic close: "I know. That's the problem." (Kael) ✅ — **PRESERVE, do not alter**
- TRACK: 03_COMPLETE end marker ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | Ayane reveal arrives without prior seeding in Ch. 1–2. Maximum impact requires one planted reference earlier. Do not alter the Ch. 3 reveal itself. |
| ⚠️ MED | Ch. 2 → Ch. 3 transition: clinical White Room coldness to warm kitchen scene with no transit buffer. One-paragraph bridge recommended. |
| ✅ PRESERVE | "I know. That's the problem." — five words, thematic core. Never expand, soften, or contextualize. |
| ✅ PRESERVE | Headphones silence sequence — HUD going quiet while Taro finds his Sawtooth Oscillation. Do not add HUD tags to this silence. |
| ✅ PRESERVE | `> QUERY: AYANE_NISHIMURA / > ERROR: FILE_CORRUPTED` — institutional absence as horror. Format is correct and must not be changed. |

---

## PHASE II — PROPAGATION (Chapters 4–8)
**Physics**: The signal travels through a medium (Malkuth Academy)
**UI Theme**: "High Fidelity" & "Data Density"
**Expected prose texture**: Dense, curious, world-expanding, building momentum
**HUD gap warning**: Chapters 6–8 show minimal HUD in live manuscript. Revision should restore Phase II density.

---

### CHAPTER 4
| Field | Value |
|---|---|
| **Live title** | The Medium |
| **TOC title** | The Medium |
| **Title status** | ✅ Match |
| **Phase** | II — Propagation |
| **Est. word count** | ~1,750 |
| **Scene headers** | `[08:03:00] THE REFERENCE SIGNAL` · `[08:15:00] THE HARMONIC STORM` |
| **HUD presence** | ✅ Active |

**Planned (Master Outline)**
- Event: Arrival at Malkuth. Meeting Hana Chord.
- AR Focus: "Server-Grade" 8K resolution. Hana's "Square Wave" tags.
- Manga Beat: The room rotating 90 degrees when the Headmaster speaks.

**Confirmed execution**
- Arrival at Malkuth ✅
- Hana Chord introduction ✅
- HUD social tagging of characters ✅ (`> TAG: DISGUST [8.5%]` confirmed in scan)
- `> STATUS: MARKED [TARDY]` — confirms Taro's outsider status ✅
- `> ALERT: EXTERNAL_PROBE_DETECTED` present ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | Verify: room-rotation manga beat (Headmaster's entrance) — confirm it is executed, not just implied. |
| ⚠️ MED | Ch. 3 → Ch. 4 transition: no transit from Taro's apartment to Malkuth. The physical journey and emotional prep are unwritten. One bridging paragraph would raise stakes. |

---

### CHAPTER 5
| Field | Value |
|---|---|
| **Live title** | The Sync Check |
| **TOC title** | The Sync Check |
| **Title status** | ✅ Match |
| **Phase** | II — Propagation |
| **Est. word count** | ~1,161 |
| **Scene headers** | `[09:15:00] THE HANDSHAKE` |
| **HUD presence** | ✅ Active |

**Planned (Master Outline)**
- Event: First training session. Taro syncs with Ven (The Sink).
- AR Focus: "Team Link" status bars. "Thermal Load" warnings.
- Manga Beat: The Bass Drop shockwave clearing the room.

**Confirmed execution**
- Sandbox Triad training sequence ✅
- Ven's Sink absorption mechanic established ✅ — clear and physically grounded
- Bass Drop / signal saturation climax present ✅ — `> TOTAL_OUTPUT: 140dB [LETHAL]`
- Phase-lock / trio dynamic formed ✅
- `> SYNC: LOCKED.` end line ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | `> CONNECTION: ESTABLISHED` — prohibited networking jargon. Replace with `> SYNC: LOCKED [STATUS: STABLE]`. |
| 🔴 CRITICAL | `> LATENCY: 0ms` — prohibited networking jargon. Replace with `> DRIFT: ZERO [LOCK: CONFIRMED]`. |
| ⚠️ HIGH | Scene header uses "THE HANDSHAKE" — also prohibited jargon. Replace with `[09:15:00] THE SYNC` or `THE TRIAD LOCK`. |
| ⚠️ MED | `HANDSHAKE` appears multiple times in Hana's dialogue ("the handshake succeeds"). Replace with "sync" or "lock" throughout. |
| ⚠️ MED | `PACKETS` appears in Hana's dialogue ("you are screaming raw data at the server and it is rejecting your packets"). Replace: "it is rejecting your signal." |

---

### CHAPTER 6
| Field | Value |
|---|---|
| **Live title** | The Ground State |
| **TOC title** | The Ground State |
| **Title status** | ✅ Match |
| **Phase** | II — Propagation |
| **Est. word count** | ~1,362 |
| **Scene headers** | `[10:05:00] THE HEAT SINK` · `[22:00:00] THE COMMODITY OF SILENCE` |
| **HUD presence** | ⚠️ Minimal — environmental headers only |

**Planned (Master Outline)**
- Event: Ven vents the heat. The "Ground Link" is formed.
- AR Focus: Industrial UI. Temperature gauges. "Cooling" mechanics.
- Manga Beat: Steam venting from Ven's armor vents.

**Confirmed execution**
- Grounding Vault sequence ✅ — Ven discharging into the building's electrical grid
- Ven's character voice established ✅ — "You're a generator with no cable" is strong
- Environmental headers used (`TEMP: 45°C [WARNING]`, `STATUS: VENTING`) but these are atmosphere, not active HUD
- `> UNIT_STATUS: VEN_CALIBRATOR / > THERMAL_LOAD: 98% [CRITICAL]` present ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | HUD drops out after the thermal sequences. Restore Phase II density through the chapter's second half. Add social tags, Taro's internal state tags, and ambient scan data. |
| ⚠️ MED | Steam venting manga beat — confirm it is rendered with sufficient visual specificity for a panel (cervical vents, thermal distortion, copper smell). |
| ℹ️ LOW | Ven calls Taro "a generator with no cable" — this is excellent. Flag for preservation list. |

---

### CHAPTER 7
| Field | Value |
|---|---|
| **Live title** | The Architecture of Sound |
| **TOC title** | The Rival |
| **Title status** | ⚠️ MISMATCH — author decision required |
| **Phase** | II — Propagation |
| **Est. word count** | ~1,058 |
| **Scene headers** | `[14:00:00] THE ARCHITECTURE OF SOUND` · `[14:30:00] MIL-SPEC SIMULATION` |
| **HUD presence** | ⚠️ Minimal in scan — but chapter text confirms active HUD |

**Planned (Master Outline)**
- Event: Introduction of Marcus Staccato (Vanguard Elite).
- AR Focus: "Combat UI." Threat assessment, path prediction.
- Manga Beat: Marcus moving faster than the frame rate (Glitch movement).

**Confirmed execution**
- Marcus Staccato introduced ✅ — "he didn't walk; he ticked forward"
- `> OPPONENT: MARCUS_STACCATO / > CLASS: RHYTHM_OPERATOR / > THREAT: SEVERE` ✅
- `> VISUAL_ARTIFACT: FRAME_SKIP` — manga beat executed ✅ — confirmed exemplary
- Rhythm Cage trap executed ✅ — `> TRAP_DETECTED: RHYTHM_CAGE / > STATUS: CONTAINED`
- `> INTERFERENCE: DESTRUCTIVE / > ATTACK: NULLIFIED` ✅
- `> OUTPUT: 80% / > TOPOLOGY: SAWTOOTH_BURST` — Taro's waveform correctly Sawtooth ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | Title mismatch requires author decision. "The Architecture of Sound" (live) is more thematically resonant with the Dorian Vale lecture context; "The Rival" (TOC) emphasizes the character introduction. Which is the narrative priority? |
| ⚠️ MED | Chapter is short (~1,058 words) and contains a full combat simulation. Verify the post-simulation fallout (Taro's physical/psychological state after losing) is sufficiently developed. |
| ✅ PRESERVE | `> VISUAL_ARTIFACT: FRAME_SKIP` — the best execution of Marcus's ability in the volume. |

---

### CHAPTER 8
| Field | Value |
|---|---|
| **Live title** | The Golden Filter |
| **TOC title** | The Sortie |
| **Title status** | ⚠️ MISMATCH — author decision required |
| **Phase** | II — Propagation |
| **Est. word count** | ~1,046 |
| **Scene headers** | `[18:00:00] THE GOLDEN FILTER` |
| **HUD presence** | ✅ Active — with violations |

**Planned (Master Outline)**
- Event: First field mission. Into the "Twilight Band."
- AR Focus: "Fog of War." Limited data, interference patterns.
- Manga Beat: The team dropping from the dropship in formation.

**Confirmed execution**
- Field mission in city ✅
- `> MASKING_PROTOCOL: MAX_LOAD / > ANALYSIS: SELECTIVE_OMISSION_ACTIVE` — C-Order filter system shown ✅
- Taro sees unregistered residents the C-Order filters blank ✅ — thematic delivery is strong
- First Silence contact ✅ — `> ENEMY: [REDACTED_ANOMALY] / > SIGNAL: ABSOLUTE_SILENCE`
- Divergence: the planned manga beat (dropship drop in formation) is not the chapter's actual climactic moment — the Silence first contact is.

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | Title mismatch. "The Golden Filter" (live) directly names the C-Order's rendering system and is more thematically precise than "The Sortie" (TOC). Recommend canonical title: *The Golden Filter*. |
| ⚠️ HIGH | Planned manga beat (dropship formation drop) does not appear to be the chapter's primary visual moment. The Silence first contact (`> SIGNAL: ABSOLUTE_SILENCE`) is the more powerful beat. Verify whether the dropship beat appears earlier in the chapter. |
| ⚠️ MED | `> SCENT: COMFORT_V3` appears in the scan — this is a `SENSATION:` adjacent tag. Evaluate whether it violates the clinical register rule. (SCENT: is not explicitly prohibited, but requires clinical justification.) |

---

## PHASE III — INTERFERENCE (Chapters 9–11)
**Physics**: Signals collide, complex topology
**UI Theme**: "Signal Corruption" & "Encryption"
**Expected prose texture**: Unstable, paranoid, unreliable — HUD should begin visibly degrading
**HUD gap warning**: Chapters 9–11 show near-zero HUD in live manuscript. This is the most critical gap. Phase III HUD should be *corrupted*, not absent.

---

### CHAPTER 9
| Field | Value |
|---|---|
| **Live title** | The Blue Screen |
| **TOC title** | The Silence |
| **Title status** | ⚠️ MISMATCH — author decision required |
| **Phase** | III — Interference |
| **Est. word count** | ~905 |
| **Scene headers** | `[18:15:00] THE BLUE SCREEN` |
| **HUD presence** | ❌ Not detected |

**Planned (Master Outline)**
- Phase III: The Incident — A Silence attack on the city.
- Phase III: The Shift — Safe Mode filters drop; Taro sees the real world.

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | No HUD detected. Phase III HUD should be *corrupted/degrading*, not absent. Introduce glitch-format tags: `> SI_GNAL L__OSS`, `> PR_OCES_SING...`, null returns. |
| ⚠️ HIGH | Shortest chapter in the volume (~905 words). If this is intentionally a gut-punch sprint chapter, confirm intentionality. If a draft stub, expand. |
| ⚠️ HIGH | Title mismatch: "The Blue Screen" (live) conflicts with Ch. 11's TOC title also being "The Blue Screen." One of these names must change. |

---

### CHAPTER 10
| Field | Value |
|---|---|
| **Live title** | The Unmasking |
| **TOC title** | The Breach |
| **Title status** | ⚠️ MISMATCH — author decision required |
| **Phase** | III — Interference |
| **Est. word count** | ~975 |
| **Scene headers** | `[18:20:00] THE UNMASKING` |
| **HUD presence** | ❌ Not detected |

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | No HUD detected. Phase III should have corrupted HUD, not silence. |
| ⚠️ HIGH | "The Unmasking" is a significant narrative event title. Confirm the chapter's actual content delivers a true unmasking (Taro, Voss, or both) — not a milder version. |

---

### CHAPTER 11
| Field | Value |
|---|---|
| **Live title** | The Wire |
| **TOC title** | The Blue Screen |
| **Title status** | ⚠️ MISMATCH — author decision required. Also conflicts: Ch. 9 live title is also "The Blue Screen." |
| **Phase** | III — Interference |
| **Est. word count** | ~1,028 |
| **Scene headers** | `[TIME: UNKNOWN] THE WIRE` |
| **HUD presence** | ❌ Not detected |

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | No HUD detected. Phase III HUD must be present, even if degraded/corrupted. |
| ⚠️ HIGH | Timestamp `[TIME: UNKNOWN]` — confirm this is intentional (Taro has lost temporal orientation) and not an unfilled placeholder. If intentional, this is an excellent detail; add `> TIMESTAMP: [CORRUPTED]` to reinforce. |
| ⚠️ HIGH | Title conflict: two chapters (live Ch. 9 and TOC Ch. 11) share the title "The Blue Screen." One must change regardless of canonical title decision. |
| ⚠️ MED | Phase III Voss double-agent reveal — confirm whether any reveal or foreshadowing of Voss's true allegiance occurs in Ch. 9–11, as the outline specifies. |

---

## PHASE IV — FEEDBACK LOOP (Chapters 12–14)
**Physics**: Runaway amplification; resonance disaster
**UI Theme**: "System Crash" & "Blue Screen"
**Expected prose texture**: Overwhelming, fragmented, past the point of recovery

---

### CHAPTER 12
| Field | Value |
|---|---|
| **Live title** | The Audit |
| **TOC title** | The Audit |
| **Title status** | ✅ Match |
| **Phase** | IV — Feedback Loop |
| **Est. word count** | ~1,499 |
| **Scene headers** | `[TIME: 08:00:00] THE DEBUGGING SUITE` |
| **HUD presence** | ✅ Active — Phase IV stripped format |

**Confirmed execution (from editorial review)**
- Forced compliance chip sequence ✅ — devastating: "The screaming in his head suddenly stopped"
- `> WELCOME_BACK_USER` post-compliance ✅ — confirmed exemplary
- Adjutant Krell (industrial brutality register vs. Voss's administrative coldness) ✅
- "Death is biological failure. Deletion is administrative." ✅
- Base64 easter egg present ✅ — decodes to "VERSION_RECOVERY_KEY: GRAND_CONCORD_IS_AN_ILLUSION" — **PRESERVE**
- `> LOG_FRAGMENT_CORRUPTED` used for redacted memory ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ HIGH | Bone-conduction probe / forced oral examination is body-horror adjacent. This is a different tonal register from Phase I–III. Ensure progressive build toward this brutality level is in place in Ch. 9–11, or the tonal jump is jarring. |
| ✅ PRESERVE | `> WELCOME_BACK_USER` — the horror of compliance rendered as a greeting. Do not alter. |
| ✅ PRESERVE | Base64 easter egg. Do not remove or alter. |
| ✅ PRESERVE | "Death is biological failure. Deletion is administrative." — Krell's defining line. |

---

### CHAPTER 13
| Field | Value |
|---|---|
| **Live title** | Reboot |
| **TOC title** | The Patch |
| **Title status** | ⚠️ MISMATCH — author decision required |
| **Phase** | IV — Feedback Loop |
| **Est. word count** | ~1,154 |
| **Scene headers** | `[TIME: 07:00:00] REBOOT` |
| **HUD presence** | ❌ Not detected |

**Planned**
- Phase IV: Taro pushes past 100%. "Unmasking" completely.
- Project Dissonance installed (Ch. 13) — triggers Dissonance Vision (see Writer's Guide v2, §8).

**Pre-identified flags**
| Severity | Flag |
|---|---|
| 🔴 CRITICAL | No HUD detected. Post-Dissonance Vision (if installed here) should produce a dramatically changed HUD interface — raw integers, stress lines, stripped of musical aesthetics. This is the single most significant HUD transition in the book. |
| ⚠️ HIGH | "Reboot" (live) vs. "The Patch" (TOC) — "Reboot" is a stronger title if Project Dissonance is installed here (a genuine system reboot). Recommend canonical title: *Reboot*. |

---

### CHAPTER 14
| Field | Value |
|---|---|
| **Live title** | The Return |
| **TOC title** | The Return |
| **Title status** | ✅ Match |
| **Phase** | IV → V Transition |
| **Est. word count** | ~2,178 |
| **Scene headers** | `[08:00:00] THE UNCANNY VALLEY` · `[08:15:00] THE AMPHITHEATER` · `[12:00:00] THE MESS HALL` |
| **HUD presence** | ✅ Active — V2.0 stripped format |

**Confirmed execution**
- Return to Malkuth post-compliance ✅
- `> V2.0 DIAGNOSTICS / > SIGNAL: MASKED` — post-compliance interface ✅ — confirmed exemplary
- Major Staccato as authority figure (changed role from rival to instructor) ✅
- `> DETECTED: NEGATIVE_RESONANCE_SINK` ✅
- Taro observing Silence interference that others cannot see ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ✅ PRESERVE | `> V2.0 DIAGNOSTICS / > SIGNAL: MASKED` as the opening HUD — the poverty of the new interface is the character note. |
| ⚠️ MED | Staccato as authority figure: verify whether his dialogue maintains his Rhythm Operator voice or slides into generic authority-figure territory. |

---

## PHASE V — EQUILIBRIUM (Chapters 15–17)
**Physics**: New stable state achieved
**UI Theme**: Restored / Rebooted
**Expected prose texture**: Clear, earned, resonant — HUD sparse but precise
**HUD gap warning**: No HUD detected in Ch. 15–16 scan. Phase V HUD should be sparse but present — the silence must be earned, not absent.

---

### CHAPTER 15
| Field | Value |
|---|---|
| **Live title** | The Phantom Mesh |
| **TOC title** | The Phantom Mesh |
| **Title status** | ✅ Match |
| **Phase** | V — Equilibrium |
| **Est. word count** | ~1,241 |
| **Scene headers** | `[03:42:00] THE MIRROR` · `[04:15:00] THE PRACTICE ROOM` |
| **HUD presence** | ❌ Not detected in scan |

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ MED | Verify HUD absence is intentional (Phase V sparseness) and not a draft gap. If intentional, at least one key HUD tag should appear — even sparse Phase V HUD has a moment. The silence must feel earned, not simply missing. |

---

### CHAPTER 16
| Field | Value |
|---|---|
| **Live title** | Illegal Modulations |
| **TOC title** | Illegal Modulations |
| **Title status** | ✅ Match |
| **Phase** | V — Equilibrium |
| **Est. word count** | ~1,130 |
| **Scene headers** | `[05:00:00] THE CONVERSATION` |
| **HUD presence** | ❌ Not detected in scan |

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ MED | "Illegal Modulations" implies a transgressive resonance event. Confirm whether the chapter's content matches its title's promise (a genuinely illegal modulation) or if the title is metaphorical. |
| ⚠️ MED | Elara/Kimura — if she appears here, confirm Resonance Dysphoria language follows Writer's Guide v2, §9. |

---

### CHAPTER 17
| Field | Value |
|---|---|
| **Live title** | The Underground |
| **TOC title** | The Underground |
| **Title status** | ✅ Match |
| **Phase** | V — Equilibrium |
| **Est. word count** | ~2,888 |
| **Scene headers** | `[23:45:00] THE DESCENT` · `[00:00:00] THE NULL` |
| **HUD presence** | ✅ Active |

**Confirmed execution**
- `> SYSTEM_STATUS: RESONANCE_ACCEPTED` ✅
- `> HULL_TYPE: NULL_VOID [UNIQUE]` ✅ — likely Elara unmasked
- `> TRACK: 17_COMPLETE` end marker ✅ — tooltip: "The session ends in shadow, the truth revealed—another step into the abyss where the only light is the one you bring yourself."
- Longest chapter in the volume (~2,888 words) ✅

**Pre-identified flags**
| Severity | Flag |
|---|---|
| ⚠️ MED | `> HULL_TYPE: NULL_VOID [UNIQUE]` — confirm this is Elara's unmasked form and not an unresolved placeholder. |
| ℹ️ LOW | Timestamp `[00:00:00]` at chapter's climax scene — confirm intentional (the reset, the null point, the beginning again) rather than coincidence. If intentional, this is strong. |

---

## SUMMARY — CHAPTER STATUS AT A GLANCE

| Ch | Title (live) | Phase | Words | HUD | Critical flags | Title conflict |
|---|---|---|---|---|---|---|
| 1 | The Zap | I | ~2134 | ✅ | 🔴 God Ray physics; 🔴 SENSATION: tags; ⚠️ POV | — |
| 2 | The Assessment | I | ~1140 | ✅ | 🔴 Missing eye-glitch manga beat; ⚠️ POV bridge | — |
| 3 | Modulation | I | ~1408 | ✅ | ⚠️ Ayane not seeded earlier | — |
| 4 | The Medium | II | ~1750 | ✅ | ⚠️ Verify room-rotation beat | — |
| 5 | The Sync Check | II | ~1161 | ✅ | 🔴 CONNECTION/LATENCY jargon; 🔴 HANDSHAKE × 3 | — |
| 6 | The Ground State | II | ~1362 | ⚠️ min | ⚠️ HUD gap in second half | — |
| 7 | The Architecture of Sound | II | ~1058 | ⚠️ min | ⚠️ Title mismatch | *The Rival* |
| 8 | The Golden Filter | II | ~1046 | ✅ | ⚠️ Title mismatch; ⚠️ Planned manga beat divergence | *The Sortie* |
| 9 | The Blue Screen | III | ~905 | ❌ | 🔴 HUD absent; ⚠️ Title conflict with TOC Ch.11 | *The Silence* |
| 10 | The Unmasking | III | ~975 | ❌ | 🔴 HUD absent | *The Breach* |
| 11 | The Wire | III | ~1028 | ❌ | 🔴 HUD absent; ⚠️ Title conflict | *The Blue Screen* |
| 12 | The Audit | IV | ~1499 | ✅ | ⚠️ Tonal build to Ch.12 brutality | — |
| 13 | Reboot | IV | ~1154 | ❌ | 🔴 HUD absent; critical Dissonance Vision transition | *The Patch* |
| 14 | The Return | IV→V | ~2178 | ✅ | — | — |
| 15 | The Phantom Mesh | V | ~1241 | ❌ | ⚠️ Verify HUD intentional | — |
| 16 | Illegal Modulations | V | ~1130 | ❌ | ⚠️ Verify HUD intentional | — |
| 17 | The Underground | V | ~2888 | ✅ | — | — |

**Volume total**: ~24,169 words (17 chapters)
**Critical 🔴 flags**: 9 across the volume
**HUD gap chapters**: 9, 10, 11, 13, 15, 16 — six chapters require HUD review
**Title decisions required**: 6 chapters

---

*Chapter Registry v1.0 — Keeping Time, Volume One*
*Compiled from: Master Outline, KeepingTime_VolumeOne.html structural scan, project knowledge chapters 5–8, 14*
*Cross-reference: `KEEPING_TIME_Writers_Guide_v2.md`, `KEEPING_TIME_HUD_Tag_Glossary.md`, `KEEPING_TIME_Analysis_Prompt_v2.md`*
