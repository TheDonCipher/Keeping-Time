# SIGNAL ACQUISITION GUIDE
### Keeping Time — Volume One
#### UI Beat Reactivity Specification

*waveform · tension · coherence · HUD · beat transitions*

---

## 01 — The Model

The UI is not decoration. It is Taro's HUD — a second narrator running in parallel to the prose. Every bar, waveform, and readout is a direct translation of what the Score is doing to him in that moment. The reader should not need to understand the system to feel it. The data should make them feel surveilled, clipped, corrupted, and liberated alongside him.

### The Three Instruments

| INSTRUMENT | METAPHOR | READS AS |
|---|---|---|
| Tension bar | Taro's output gain | How much signal he's broadcasting — danger of clipping |
| Coherence bar | Local grid stability | How much the world is holding together around him |
| Waveform | The Score's shape | The character of the frequency currently in control |

### The Voltage Curve

Every chapter in Volume 1 maps onto a single arc: **Suppressed → Pushed → Broken → Patched → Cracking again.**

The UI should trace that arc. The reader who never reads the prose should be able to reconstruct the emotional shape of the novel from the tension and coherence bars alone.

**Baseline rules:**

- `vol` (tension): starts 0.15, should feel like pressure building across the entire volume
- `coh` (coherence): starts 0.85, should erode gradually — the world is decaying under Taro's presence
- Chapter headers always spike tension briefly, then settle — signal acquisition animation
- System-format beats (backtick lines) should max coherence momentarily — the Score speaking clearly
- Dialogue beats between characters should drift tension by ±0.1 based on emotional content
- Lore epigraph blocks are always low tension, high coherence — the C-Order presenting its official face

---

## 02 — Data Value Specification

Currently every beat in the HTML uses `data-vol='0.25' data-coh='0.8'` — identical for every paragraph across all 17 chapters. This flat value is what makes the UI feel decorative rather than reactive. Every paragraph needs its own values.

### Beat Type Reference

| BEAT TYPE | VOL | COH | WAVEFORM | TRIGGER CONDITION |
|---|---|---|---|---|
| Chapter header | 0.35 | 0.90 | SPIKE → settle | h3 / chapter title |
| Epigraph / lore block | 0.10 | 0.95 | sine clean | blockquote elements |
| Zone status line | 0.20 | 0.92 | flat/grid | ZONE: / FIDELITY: lines |
| System alert (backtick) | 0.45 | 0.85 | square pulse | `` ` ` `` monospace lines |
| System CRITICAL alert | 0.75 | 0.60 | sawtooth burst | WARNING / CRITICAL lines |
| Neutral narration | 0.25 | 0.80 | sine standard | Standard 3rd-person prose |
| HUD/metric narration | 0.35 | 0.80 | sine + dropout | BPM, SDI, HIQ references |
| Taro internal thought | 0.40 | 0.70 | sine distorted | His perspective, not system |
| Dialogue — calm | 0.30 | 0.75 | sine | Conversational exchange |
| Dialogue — tense | 0.55 | 0.65 | sawtooth | Argument, confrontation |
| Dialogue — Voss/Krell | 0.20 | 0.95 | sine clean | Authority figures, clipped tone |
| Physical action | 0.60 | 0.60 | dropout/square | Combat, running, impact |
| Phase conflict moment | 0.70 | 0.55 | sawtooth | Two signals colliding |
| Resonance spike | 0.85 | 0.40 | sawtooth burst | Taro running high |
| Limiter removal / peak | 0.99 | 0.20 | collapse | The unmask moments |
| Void / silence moment | 0.15 | 0.30 | collapse | Ch9, dead zones |
| Post-patch / compliant | 0.15 | 0.92 | flat/sine | After firmware install |
| Elara / wrong note sync | 0.45 | 0.88 | beating | Two signals finding phase |
| Underground / illegal mod | 0.50 | 0.50 | static | Jailbreak, off-grid |
| End of chapter / saving | 0.20 | 0.85 | sine decay | TRACK: N_COMPLETE lines |

---

## 03 — Chapter-by-Chapter Beat Map

For each chapter: the emotional arc, key beat moments, and exact UI prescriptions. The waveform column refers to the canvas background waveform mode — distinct from the progress bar waveform.

---

### CH.01 — The Zap

The system speaks first. Taro is introduced as a data object before we experience him as a person. The UI should feel **clinical and orderly** — the Score is fully in control. Until the Zap.

Arc: `FLAT → SPIKE → CRASH → RECONNECT → SUPPRESS`

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 01 | Epigraph: 'There was no incident' | 0.10 | 0.95 | sine clean | Bars minimal. Coherence near full. The C-Order's official version. |
| 01 | ZONE: SECTOR 7-C / STATUS: CONNECTED | 0.20 | 0.92 | flat | Grid lines render. Everything nominal. Boring is the point. |
| 01 | The Zap — electrical discharge | 0.85 | 0.35 | collapse | Tension bar SPIKES hard. Coherence drops. Waveform collapses to static. |
| 01 | SYSTEM_ALERT: ELECTRICAL_DISCHARGE | 0.90 | 0.30 | sawtooth | Full tension alert. Coherence at floor. Progress bar goes sawtooth. |
| 01 | His heartbeat thumped against his ribs | 0.55 | 0.60 | sine distorted | Tension mid. BPM readout jumps to 110. Coherence recovering slowly. |
| 01 | PERCEPTION: ONLINE / A-440 STANDARD | 0.30 | 0.85 | sine | System reboots. Coherence climbs back. Tone returns to gold. |
| 01 | The golden sine wave propagated... | 0.25 | 0.88 | sine | Ambient state. The Score running the room. Low, stable. |
| 01 | STRESS_ACCUMULATION [84 SU] | 0.55 | 0.70 | sine + dropout | Building pressure. Orange warning in prose = tension climbing. |
| 01 | The Zap happens — grid rejection | 0.92 | 0.15 | collapse | PEAK EVENT. Tension maxes. Coherence collapses. Waveform: noise. |
| 01 | OPTION_A: REFORMAT / OPTION_B: INTEGRATION | 0.30 | 0.88 | flat | Voss's clinical delivery. Tension falls. Coherence high — system in control. |
| 01 | We will simply turn you off | 0.45 | 0.90 | sine clean | Cold authority. Tension spike on threat, then Voss clamps it down. |
| 01 | SESSION: TERMINATED / optical feed black | 0.15 | 0.92 | flat/decay | Chapter close. Everything quiets. Saving state. |

---

### CH.02 — The Assessment

Taro is in the white void of a diagnostic. The UI should feel **invasive and pristine** — maximum coherence because the system has total access to him.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 02 | Privacy mask active — white void | 0.20 | 0.98 | flat | Near-zero tension. Coherence at ceiling. The system owns this space. |
| 02 | Voss renders: TARGET_ANALYSIS: VOSS_KAEL | 0.15 | 0.95 | sine clean | Authority figure. Perfect signal. Voss's waveform is always a clean sine. |
| 02 | VOCAL_ANALYSIS: CALIBRATED [WASTE: 0%] | 0.20 | 0.95 | sine clean | System confirming Voss. Coherence holds high. |
| 02 | The wireframe of the dead Vanguard soldier | 0.45 | 0.70 | sine dropout | Tension rises on accusation. Coherence dips slightly. |
| 02 | You bricked a Class-4 Vanguard unit | 0.60 | 0.65 | sawtooth | Taro under pressure. Accusation beat. Tension climbs. |
| 02 | SIGNAL_INSTABILITY / collar tightens | 0.55 | 0.72 | sine | Collar suppresses. Tension held down artificially. Coherence rising. |
| 02 | ANOMALY: DETECTED [CLASSIFICATION: REDACTED] | 0.70 | 0.55 | sawtooth burst | Key narrative beat. Redaction = coherence gap. Tension high. |
| 02 | COMMAND: EXECUTE_TRANSFER to Malkuth | 0.35 | 0.88 | flat | Administrative resolution. Voss takes control. System satisfied. |

---

### CH.03 — Modulation

The Sector 7-C slums. Low-fidelity zone. The UI should feel **degraded and analogue-warm** — the Score struggling to maintain signal. Kael's presence is the counterpoint: a perfect sine in a room of static. This is also the headphones chapter.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 03 | ZONE: SECTOR 7-C [DEAD ZONE] / FIDELITY: DEGRADED | 0.25 | 0.62 | dropout | First degraded zone. Coherence noticeably lower. Waveform has gaps. |
| 03 | 150ms latency / 15% carrier wave penetration | 0.30 | 0.58 | dropout | Signal barely holding. Coherence below 0.6 — add flicker to coh bar. |
| 03 | Tap. Tap. Tap. — somatic calibration | 0.35 | 0.65 | sine | Taro stabilising himself. Tension mid. Coherence ticks up slightly. |
| 03 | Kael: WAVEFORM: SINE_PURE / DISTORTION: 0.00% | 0.20 | 0.95 | sine clean | Kael enters. Coherence SNAPS to near-full. His field dominates the room. |
| 03 | Walking into a wall of solid gold | 0.50 | 0.60 | sine + sawtooth | Phase conflict between them. Both waveforms visible — beat interference. |
| 03 | ERROR: PHASE_CONFLICT / frame drop | 0.65 | 0.50 | sawtooth | Tension climbs. Coherence drops. System failing to reconcile them. |
| 03 | Your mother: file CORRUPTED [UNRECOVERABLE] | 0.60 | 0.45 | collapse | Emotional hit. Coherence drops further. Waveform fragments briefly. |
| 03 | It's a muzzle — Kael about the collar | 0.70 | 0.55 | sawtooth | Tension peak for this chapter. Kael's anger spike. |
| 03 | The lead-lined containment case — mother's gift | 0.35 | 0.70 | sine | Tone shift. Tension eases. Something tender in a hostile environment. |

---

### CH.04 — The Medium

Malkuth Academy. The system is in surveillance mode. The UI should feel **watched and sharp-edged** — high-coherence because the institution maintains a pristine render, but tension climbs steadily as Taro is processed and ranked.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 04 | ZONE: MALKUTH ACADEMY / FIDELITY: MAXIMUM | 0.25 | 0.90 | sine | Clean environment. High coherence. The Academy is a controlled space. |
| 04 | Rank broadcasts — SDI / HIQ scores public | 0.40 | 0.85 | square | Square wave: the Medium's surveillance. Hard edges, no warmth. |
| 04 | Social tag system, compliance scoring | 0.45 | 0.82 | square | Tension builds as he's ranked. The social display is on. |
| 04 | Taro's SDI is high — FLAGGED | 0.60 | 0.75 | square burst | Tension spike at flag. Coherence holds (system knows exactly what it's doing). |
| 04 | The Headmaster watching from above | 0.50 | 0.88 | sine clean | Voss's gaze = coherence up. His presence is always stabilising aesthetically. |

---

### CH.05 — Sync Check

Taro finds Ven. The Triad starts to form. The UI should trace the arc of **two signals learning to coexist** — tension through incompatibility, then a resolution beat when the link locks.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 05 | Ven absorbs Taro's spike — first contact | 0.55 | 0.65 | beating | Beating waveform: two frequencies near each other, not yet synced. |
| 05 | Hana calculating — PROBABILITY 99.4% | 0.45 | 0.78 | square | Hana's presence = square wave. Clinical. Her math is always clean. |
| 05 | SYNC_STATUS: GREEN / NETWORK: LOCKED | 0.40 | 0.88 | sine | Resolution beat. Coherence climbs. Tension falls. The trio is formed. |
| 05 | Initializing Drop | 0.60 | 0.75 | sawtooth | Beat drops. Tension rises. Excitement, not fear. |

---

### CH.06 — Ground State

The Grounding Vault. Ven overloading. The UI should feel **industrial and dangerous** — like a machine running too hot. Tension is the temperature of Ven's hardware. Coherence is the vault containing it.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 06 | ZONE: SECTION 0 / FIDELITY: INDUSTRIAL UNFILTERED | 0.35 | 0.65 | sine distorted | Unfiltered environment. Coherence below comfort. Waveform has noise. |
| 06 | Ven's core temp 104°F / 99% buffer | 0.55 | 0.55 | dropout | High tension. Low coherence. Ven is barely contained. |
| 06 | CLANG — Ven dumps heat into the copper wall | 0.65 | 0.50 | sawtooth burst | Impact beat. Physical energy release. Tension spikes then falls. |
| 06 | Sparks arc from his knuckles / lights surge | 0.70 | 0.45 | sawtooth | Dramatic moment. Tension high. Coherence low — raw energy in the space. |
| 06 | Your oscillation is clean. Full-spectrum. | 0.35 | 0.68 | sine | Ven's quiet affirmation. Tension drops. Coherence recovering. |
| 06 | It's quiet because I carry load — Kael echo | 0.30 | 0.72 | sine | Reflective beat. Similar to Ch3 but earned. Softer tension. |

---

### CH.07 — Rival

The Rival enters. C5 frequency. The UI should feel **confrontational and bright** — tension through challenge rather than threat. Coherence stays higher than you'd expect because the system approves of competition.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 07 | Rival's profile: 523.25 Hz / SDI competitive | 0.45 | 0.80 | sine | Clean rivalry. Both signals are high-res. This isn't corruption — it's friction. |
| 07 | Combat exercise / sortie training | 0.65 | 0.70 | sawtooth | Action beat. Tension climbs. Coherence moderate — the system is watching. |
| 07 | SDI: 0.98 / peak during exercise | 0.80 | 0.55 | sawtooth burst | Taro running close to his limit. Tension high. |
| 07 | Post-exercise: tension drops / collar cools | 0.35 | 0.80 | sine | Resolution. System satisfied. Tension falls sharply post-exercise. |

---

### CH.08 — Sortie

First real mission. Dropout waveform for this chapter — the environment is hostile and the signal is fragmenting. The UI should feel **like a feed breaking up**. Low coherence, high tension, the waveform stutters.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 08 | Mission deployment / Low-Fi sector entry | 0.50 | 0.58 | dropout | Signal degrades as they enter the hostile zone. Coherence falls. |
| 08 | Silence agents first sighted | 0.70 | 0.45 | dropout | Tension spikes on first contact. The Silence entities: coherence killers. |
| 08 | CLANG / Ven hits the pipe — physical strike | 0.80 | 0.40 | collapse | Raw physics. The Score can't process it. Coherence bottoms temporarily. |
| 08 | Run! / escape into darkness | 0.75 | 0.35 | collapse | Climax moment. Maximum tension. Waveform is noise. |
| 08 | TRACK: 09_COMPLETE / SYSTEM HALTED | 0.25 | 0.65 | sine decay | Hard stop. Tension drops sharply. Coherence beginning recovery. |

---

### CH.09 — Silence

The void-decay chapter. The UI should **go silent** — this is the only chapter where coherence actually means something to the Score rather than to Taro. The coherence bar should feel like it's tracking something frightening. The silence lock overlay fires here.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 09 | Entry into the Silence zone | 0.20 | 0.20 | collapse | Coherence at floor. Not dangerous — just gone. Void aesthetic. |
| 09 | void-decay drone begins — white noise fading | 0.10 | 0.15 | collapse | Waveform nearly flat. The silence lock fires on entry. |
| 09 | No authorized options remain | 0.35 | 0.18 | collapse | Tension spike in the void. Inversion of normal: high tension, zero coherence. |
| 09 | Silence lock overlay fires | 0.00 | 0.00 | flat | SILENCE LOCK: all values drop to zero. The chapter ends the UI. |

---

### CH.10 — The Unmasking

The limiter comes off. The single biggest tension event in the volume. The UI should build to a **maximum everything state** — then cut to render-void for the aftermath. The palimpsest glitch fires on this chapter entry.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 10 | [SYNTAX_ERROR] / FIDELITY: NULL / STATUS: FAILING | 0.60 | 0.30 | collapse | Chapter opens broken. Coherence already low. Corruption visible. |
| 10 | Ven hard-locked / Hana unconscious / SDI: 1.00 | 0.80 | 0.20 | sawtooth | Peak distress. Maximum drift. The squad is down. |
| 10 | GROUND_LOST / VOLTAGE: MAXIMUM SPIKE | 0.92 | 0.12 | collapse | Taro disconnects from Ven's buffer. Signal spikes catastrophically. |
| 10 | TAMPER_DETECTED / WARRANTY: VOID | 0.95 | 0.08 | collapse | The limiter removal. Tension approaching ceiling. Coherence at floor. |
| 10 | The limiter ring snaps — CRACK | 0.99 | 0.05 | static/noise | PEAK MOMENT of Volume 1. Full tension. Zero coherence. Noise only. |
| 10 | LIMITER: REMOVED / NEURAL_DAMPING: 0.00% | 1.00 | 0.05 | static | One frame of absolute maximum. Progress bar maxed. All bars maxed. |
| 10 | The noise was mathematically beautiful | 0.85 | 0.20 | sawtooth | Coming down from peak. Still high but now expressive rather than desperate. |
| 10 | Palimpsest glitch fires (code trigger) | 0.70 | 0.25 | sawtooth | Visual corruption bleeds from the side layer. Danger palette. |

---

### CH.11 — Safe Mode

Krell's interrogation room. The system watching. The UI should feel **clinical and predatory** — high coherence because Krell controls the environment completely, but tension stays elevated because he's actively harming Taro. The two metrics contradict each other purposefully.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 11 | Diagnostic slab / restraints active | 0.60 | 0.88 | flat | Contradiction beat: HIGH coherence (Krell's control), HIGH tension (Taro's fear). |
| 11 | IM_SORRY_I_CANT_STOP_IT — the NAI speaks | 0.55 | 0.85 | flat | The NAI's hidden message. Coherence maintains (system intact), tension high. |
| 11 | Bone conduction probe — CRACK / pain spike | 0.85 | 0.80 | square burst | Tension maxes. Coherence stays high. The system is working as designed. |
| 11 | CRITICAL_ALERT: LETHAL_FORCE_AUTHORIZED | 0.90 | 0.88 | square | Coherence at maximum — the authorization is legal. Tension at near-max. |
| 11 | That's enough, Adjutant — Voss enters | 0.40 | 0.92 | sine clean | Voss arrival. Tension drops sharply. His field stabilises everything. |
| 11 | Broken toys are useless to me, Krell | 0.25 | 0.94 | sine clean | Administrative calm. Full Voss sine wave mode. |
| 11 | This is not music. This is a virus. | 0.45 | 0.90 | sawtooth replay | Voss replaying the anomaly waveform. Tension mid. Coherence high. |

---

### CH.12 — Audit

The NAI's reveal — the system's internal voice is revealed as having feelings. This is the most intimate chapter. The UI should go **unexpectedly quiet** — coherence high but tension eerily low. The Score is listening.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 12 | NAI narrating in first person — intimate register | 0.20 | 0.88 | sine | Quiet chapter. Low tension. The AI voice is tender, not aggressive. |
| 12 | I tried to reach him but was blocked | 0.30 | 0.82 | sine dropout | Small tension spike when the NAI describes its limitation. Tiny grief. |
| 12 | PLEASE_NO embedded in system alert | 0.50 | 0.70 | dropout | Hidden message in the alert text. Tension spike on recognition. |
| 12 | The audit processes him — all data visible | 0.25 | 0.92 | flat | System is watching everything. Coherence high. Taro exposed but calm. |

---

### CH.13 — Patch

Voss installs the compliance firmware. The UI should execute the **most disturbing UI moment in the volume**: as the patch installs, tension and coherence should both rise toward 'optimal' — the system considers this a success. The reader should feel the horror of the bars looking healthy.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 13 | Pre-patch: Taro resisting | 0.55 | 0.60 | sawtooth | Standard resistance state. Tension moderate. Coherence low. |
| 13 | Patch installation begins | 0.40 | 0.70 | sine | Tension falling. Coherence climbing. The horror is that it 'works'. |
| 13 | STATUS: COMPLIANT — patch complete | 0.15 | 0.92 | sine clean | Full compliance. Bars look perfect. Reader should feel sick. |
| 13 | Headphones returned — feels wrong | 0.20 | 0.90 | flat | Post-patch. Everything nominal. The flatness is the tragedy. |
| 13 | I don't need them anymore — fake smile | 0.15 | 0.93 | flat | TRACK: 13_OPTIMIZED. Lowest tension in the whole volume. Most disturbing. |
| 13 | File: ANGER / Status: HIDDEN | 0.22 | 0.89 | sine | Tiny spike on the hidden file beat — something underneath. Small but vital. |

---

### CH.14 — The Return

Back at Malkuth under the patch. The UI should feel **wrong in a clean way** — 8K render, perfect coherence, but tension gradually bleeding back in as the patch fails to fully suppress Taro's perception.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 14 | FIDELITY: MAXIMUM [8K_RENDER] / ONLINE_AND_OPTIMAL | 0.15 | 0.95 | flat | Post-patch world. Aesthetically perfect. Bars look great. Something is off. |
| 14 | Anxiety waveforms visible in 'verified laughter' | 0.28 | 0.88 | sine | Taro seeing through the patch. Tension ticking up. He can't stop seeing. |
| 14 | Damping field in the hologram replay | 0.40 | 0.80 | dropout | His perception breakthrough. Dropout: he's detecting holes in the render. |
| 14 | TARO_METRICS_SPIKE: SDI 0.85 // HIQ 0.72 | 0.60 | 0.70 | sawtooth | Spike: his real signal bleeding through the patch suppression. |
| 14 | COMMS_INTERCEPT ACTIVE — Krell watching | 0.70 | 0.78 | square | Krell's surveillance. Square wave. Tension high but coherence stays up — he's trapped. |
| 14 | I'm fine, Mom / Everything is great parameters | 0.45 | 0.85 | flat | The lie. Tension drops because he suppresses it himself. Devastating. |
| 14 | The wrong note is inside the house — wireframe girl | 0.55 | 0.72 | sine | Chapter close spike. Something new detected. Tension rising again. |

---

### CH.15 — The Phantom Mesh

Taro sees his own wireframe in the mirror. He sees Elara's. The UI should execute a **flicker beat** — brief coherence collapse when the hull drops, then recovery when they recognise each other. The 'two wrong notes in phase' beat is the emotional peak of the chapter.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 15 | Hull_integrity compromised / SDI 0.14 | 0.30 | 0.88 | flat | Patch holding. Low tension, high coherence. But the number is wrong. |
| 15 | Mirror flicker — wireframe visible | 0.60 | 0.35 | collapse | FLICKER EVENT: Coherence drops sharply for 1-2 beats. Then recovers. |
| 15 | WARNING: HULL_INTEGRITY_COMPROMISED | 0.55 | 0.55 | dropout | Tension mid. Coherence mid. Taro holding it together barely. |
| 15 | Elara playing cello — wrong note bleeding through | 0.40 | 0.65 | beating | Beating waveform: two signals close to phase. Tension easing. |
| 15 | Taro shows his wireframe — deliberate drop | 0.55 | 0.40 | collapse | Intentional hull drop. Coherence falls when he chooses to show it. |
| 15 | RESONANCE_SYNC_CONFIRMED — in phase moment | 0.45 | 0.82 | beating | Peak emotional beat. Two signals locked. Coherence climbs warmly. |
| 15 | SIGNAL_STATUS: UNFILTERED | 0.50 | 0.78 | sine | Resolution. Calm. Something new and warm in the signal. |

---

### CH.16 — Illegal Modulations

The jailbreak room. Practice Room 404. Warm amber illegal hardware. The UI should feel **off-grid and alive** — coherence moderate (they're masking but not perfectly), tension elevated but not frightened. This is excitement. Static waveform: the authorized grid can't see inside here.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 16 | Room 404 / local masking active | 0.35 | 0.62 | static | Off-grid aesthetic. Coherence below normal — they're outside the system. |
| 16 | Hacking deck — warm amber, illegal UI | 0.40 | 0.60 | static | Unauthorized hardware. Static waveform throughout this chapter. |
| 16 | We categorise it as modulating | 0.40 | 0.58 | static | The framing. Low tension. Elara explaining. Coherence soft. |
| 16 | Underground network discovered / map renders | 0.50 | 0.55 | static | Tension rises on discovery. Coherence drops slightly — bigger picture. |
| 16 | LIMITER: OFFLINE — second removal | 0.75 | 0.40 | collapse | Second limiter drop. Tension high. Coherence low. |
| 16 | Void hands — optically black appendages | 0.80 | 0.30 | collapse | Visual peak. Tension very high. Coherence low. |
| 16 | You are the Silence — Elara's revelation | 0.65 | 0.35 | collapse | Identity beat. Taro's panic spike. Tension jumps. |
| 16 | You are not a wrong note — you are the rest | 0.50 | 0.55 | beating | Resolution. The truth accepted. Beating waveform: two signals in peace. |

---

### CH.17 — Underground

The final chapter. Taro's identity is accepted. He makes a choice. The UI should build toward a **new kind of tension** — not the anxiety of suppression but the forward momentum of intent. The volume ends with mid-tension, mid-coherence: unresolved but purposeful.

| CH | BEAT / MOMENT | VOL | COH | WAVE | UI PRESCRIPTION |
|---|---|---|---|---|---|
| 17 | SYSTEM_STATUS: RESONANCE_ACCEPTED | 0.45 | 0.70 | sine | Acceptance beat. Tension mid. Coherence climbing. Something is settling. |
| 17 | HULL_TYPE: NULL_VOID [UNIQUE] | 0.50 | 0.65 | sine | Identity confirmed. Tension holds. Coherence moderate — he's outside the grid. |
| 17 | THREAT_LEVEL: ELEVATED / proximity lock on Mom | 0.65 | 0.60 | sawtooth | Stakes clarified. Tension climbs toward volume close. |
| 17 | I am plotting a course for your coordinates | 0.70 | 0.60 | sawtooth | Deliberate decision beat. Tension rising but controlled. Not panic. |
| 17 | I am bringing the noise | 0.75 | 0.55 | sawtooth | Final line. Tension at intentional high. Not max — purposeful. |
| 17 | TRACK: 17_COMPLETE / END OF VOLUME ONE | 0.55 | 0.65 | sine decay | Fade down slightly. Volume close. Not resolved — but steady. Ready. |

---

## 04 — Waveform Shape Guide

The background canvas waveform and the progress bar waveform are both driven by the chapter's `waveMode` config. This section defines what each mode should communicate and when to switch mid-chapter.

| MODE | SHAPE | CHAPTERS | MEANING |
|---|---|---|---|
| sine | Smooth rolling curve | Ch1 (baseline), Ch3, Ch6, Ch15 end | The Score is in control. Taro is contained. Harmony enforced. |
| square | Hard on/off steps | Ch4, Ch7, Ch11 | The Medium. Surveillance. Binary compliance logic. No warmth. |
| sawtooth | Aggressive ramp/drop | Ch8, Ch9, Ch10 peak, Ch16 end | Taro running high. Dissonance as weapon. The edge of the system. |
| dropout | Sine with signal gaps | Ch8, Ch14 mid, degraded zones | Signal integrity failing. The environment is hostile to coherence. |
| beating | Two sines interfering | Ch5 sync, Ch15 end, Ch16 end | Two signals finding phase. Unresolved harmony. Searching. |
| collapse | Jitter/noise | Ch9, Ch10 peak, Ch15 flicker | Total coherence failure. The Score losing control of reality render. |
| static | Random noise | Ch16 throughout, Ch17 opening | Off-grid. Unauthorized space. The system cannot see this room. |
| flat | Horizontal line | Ch13 post-patch, Ch14 open | Perfect compliance. The most disturbing waveform. Nothing moves. |

### Mid-Chapter Waveform Switching

The chapter config sets the default `waveMode`. But specific beats should trigger temporary overrides. These are the most important ones:

- **Ch1 — The Zap beat:** switch to `collapse` for 3 beats, then recover to `sine`
- **Ch10 — Limiter snap:** switch to `static` for the CRACK and LIMITER: REMOVED beats only
- **Ch11 — Voss entry:** override from `square` to `sine clean` immediately
- **Ch13 — Patch install:** transition slowly from `sawtooth` → `flat` over 4 beats
- **Ch15 — Hull flicker:** 2-beat `collapse` then snap back to chapter default

---

## 05 — HUD Extras & Special Displays

The `hudExtras` config array enables per-chapter supplemental readouts. These appear in the HUD and should always have narrative justification.

| EXTRA | CHAPTERS | WHAT IT SHOWS | NARRATIVE JUSTIFICATION |
|---|---|---|---|
| social_tag | Ch2, Ch4 | SAFE / THREAT compliance badge | Malkuth Academy ranks citizens publicly. The tag IS the surveillance. |
| impedance | Ch3, Ch6 | Phase mismatch warning glow | Kael's field vs Taro's. Visual amber vignette shows the conflict. |
| fidelity | Ch4, Ch11, Ch14 | RENDER QUALITY percentage | High-fidelity zones project their quality. A way of displaying power. |
| team_link | Ch5, Ch7, Ch8 | Triad sync status (3 nodes) | Shows how well Taro, Ven, Hana are phase-locked in the moment. |
| altimeter | Ch8 | Depth / sector-level indicator | They're descending into hostile territory. The number should feel wrong. |
| combat | Ch7, Ch8, Ch10 | SDI / HIQ real-time metrics | Combat readout. Should spike visibly on every hostile encounter. |
| hull_status | Ch15, Ch16, Ch17 | Hull integrity percentage | The phantom mesh chapters — the mask is slipping. |
| void_depth | Ch17 | Void absorption rate readout | Taro's new identity. Reads his unique null-signal as a capability metric. |

### Accent Colour Arc

The accent colour is the most immediate signal that the chapter has changed. The arc across Volume 1 should feel like a spectrum of the Score's moods.

| CHAPTERS | HEX | NAME | MEANING |
|---|---|---|---|
| 1, 2 | `#00f3ff` | Cyan | Standard C-Order. The Score's factory default. |
| 3 | `#f5a623` | Amber | Sector 7-C warmth. F#4. The slums have a different colour. |
| 4, 7 | `#00f3ff` | Cyan | Back to compliance. Malkuth's clean environment. |
| 5 | `#00f3ff` | Cyan (beating) | Standard but pulsing — the sync forming. |
| 6 | `#00f3ff` + heat | Cyan + red | Ground state. Ven's heat modulates the base colour. |
| 9 | `#9933ff` | Purple | Void. The colour of the Silence. First intrusion of their aesthetic. |
| 10 | `#9933ff` | Purple | The breach chapter. The Silence's world. |
| 11 | `#cc2244` | Danger red | Krell. The colour of lethal administrative force. |
| 12 | `#00f3ff` | Cyan (dim) | The NAI speaks. Standard palette but muted. |
| 13 | `#c8a84b` | Gold | The patch. The C-Order's most elegant, most sinister chapter. |
| 14–15 | `#00f3ff` | Cyan (cracking) | Post-patch compliance — but the cracks are starting. |
| 16 | `#ff8c00` | Warm orange | Illegal modulation space. Analogue warmth, unauthorized. |
| 17 | `#0a0a0c` | Near-void black | Taro's colour is no colour. He is the absence. |

---

## 06 — IDE Implementation Prompts

Three prompts to give your IDE. Do them in order. Each is independent and testable.

---

### Prompt A — Assign data-vol / data-coh to every beat

```
The HTML file has every paragraph tagged data-vol='0.25' data-coh='0.8'
identically. Replace these with narrative-accurate values using
the following rules:

// BEAT TYPE → (vol, coh) quick reference:
// System alert (backtick lines):          (0.45, 0.85)
// System CRITICAL/WARNING:                (0.75, 0.60)
// Epigraph / lore blockquote:             (0.10, 0.95)
// Zone status header paragraph:           (0.20, 0.92)
// Neutral narration:                      (0.25, 0.80)
// Dialogue — calm:                        (0.30, 0.75)
// Dialogue — tense/argument:              (0.55, 0.65)
// Voss / authority figure dialogue:       (0.20, 0.95)
// Physical action / impact beats:         (0.60, 0.60)
// Resonance spike / Taro running high:    (0.85, 0.40)
// Limiter removal / peak events:          (0.99, 0.05)
// Void / silence:                         (0.10, 0.20)
// Post-patch / compliance:                (0.15, 0.92)
// Chapter end / TRACK_COMPLETE:           (0.20, 0.85)

Add data-tag attributes to key beats using these tag names:
bass_drop, combat_ui, frame_skip, impedance, headmaster,
social_tag, crash, limiter, clip, override
```

---

### Prompt B — Wire per-beat vol/coh into smooth UI transitions

```
The NarrativeState.update() method currently lerps vol/coh with
factor 0.05. Add these enhancements with comprehensive comments:

1. On beats where vol changes by > 0.2 from previous: add a 300ms
   data-transition='spike' class to beat-container that temporarily
   increases lerp to 0.20 for that beat, then decays back to 0.05

2. On beats where coh drops below 0.3: apply the render-void palette
   override temporarily, remove when coh recovers above 0.35

3. The gold/amber chapters (Ch3, Ch13, Ch16): apply a warm vignette
   by setting --wave-color to the chapter's accent tint

4. The flat waveform chapters (Ch13 post-patch): lock the progress bar
   amplitude to near-zero regardless of tension value — the waveform
   should be as dead as the narrative
```

---

### Prompt C — Chapter transition animations

```
The triggerChapterFlash() function fires on every chapter beat.
Expand it to be chapter-aware with comprehensive comments:

1. Standard chapters (1-8, 14-15): current blue flash — keep as-is
2. Ch9 (Silence): no flash at all — the chapter begins with silence,
   no system fanfare
3. Ch10 (Breach): purple flash (danger + purple mix), longer duration
   800ms, add shake transform to stage
4. Ch11 (Krell): red flash — danger color, sharp and fast (200ms),
   no decay
5. Ch13 (Patch): gold flash that fades very slowly over 2 seconds —
   the compliance feels luxurious
6. Ch16 (Illegal Mods): warm orange flash with a grain/noise texture
   overlay — unauthorized warmth
7. Ch17 (Underground): no flash — the void doesn't announce itself.
   The chapter begins in darkness.
```

---

## 07 — Creative Details Worth Implementing

These are specific moments in the prose that have obvious, beautiful UI counterparts. Each one is a design opportunity.

### The BPM Arc

Taro's BPM is mentioned explicitly at 110 in Ch1. Across the volume it should be: **110 → 140** (Zap peak) **→ 95** (Voss room) **→ 40** (Ven in vault) **→ 145** (Ch10 limiter) **→ 70** (patch installed) **→ 115** (Ch17, purposeful). The BPM display should tell his arc without the reader needing to track anything consciously.

### Kael Nishimura's Coherence Footprint

Every time Kael appears (Ch3, Ch6 memory), the coherence bar should visibly rise when his dialogue is active and fall slightly when Taro responds. His `HARMONIC_DISTORTION: 0.00%` is a design spec: he is maximum coherence wherever he stands.

### The Collar Millimeter

In Ch2: *'The collar tightened by one millimeter.'* This is the perfect moment for the tension bar to visibly suppress mid-rise — it should peak, then get pushed back down by an invisible hand. The bar reaches for 0.70 then snaps to 0.40 in a single frame.

### PLEASE_NO in the System Alert (Ch11)

The NAI embeds `PLEASE_NO` inside a system alert string. This beat deserves a unique UI response: the system alert format (mono, uppercase) but the coherence bar should **glitch downward for one frame** before recovering. The system is cracking through its own readout.

### The Tuning Fork — TING / A-440

Ch3: Kael's tuning fork emits A-440 at 100.00% accuracy. This beat should momentarily max the coherence bar to 1.00 and hold it there for exactly the duration of one scroll beat — then let it drift back. It should feel like a reference tone clearing the air.

### File: ANGER / Status: HIDDEN (Ch13 end)

The most subversive beat in the volume. The system has quarantined Taro's anger in an encrypted file. The UI should register this as a tiny, almost invisible tension micro-spike (0.15 → 0.22 → back to 0.15) — small enough to miss on first read, obvious on reread. The waveform should show one frame of sawtooth inside the flat.

### The Void Hands Moment (Ch16–17)

Taro's hands go optically black. The UI's background waveform should, for these beats, invert — instead of a glowing wave on a dark background, render a dark silence on a slightly lighter background. The wave is now the absence. The accent colour drops to near-black. The bars go dim, not zero.

### 'I am bringing the noise' — Volume close

The final line of Volume 1. Tension should be sitting at a deliberate 0.75 — not maxed, not panicked, just purposeful. The waveform should shift from `sine decay` back to a single clean sawtooth pulse. The progress bar should reach exactly 100% and hold there.

The last beat the reader sees: **tension at 0.75, coherence at 0.55, waveform: sawtooth, BPM: 115.** Not resolved. Not broken. Ready.

---

*// END OF DOCUMENT — SIGNAL_ACQUISITION_GUIDE_V1.0*
*// Total chapters mapped: 17 / Total beat types defined: 20*
*// Waveform modes: 8 / HUD extras: 8 / Accent colours: 9*
