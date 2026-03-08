# KEEPING TIME — Volume One
## Creative & Technical Implementation Guide
### Horror · Comedy · Romance Upgrade Pass

---

> **How to use this document**
> Each section maps directly to the existing HTML structure. Narrative changes reference chapter IDs (`ch1`–`ch17`) and beat signal names (`ch01_zap` etc.) as they appear in the source. Audio engine changes reference the `AudioEngine` class and `_triggerTagAudio` method. UI changes reference existing CSS classes and the `#fragment-container` / `#palimpsest-layer` systems.

---

## PART ONE: STORY ARCHITECTURE
### The Book as a Waveform — Five Signal Phases

The core problem to solve before any individual beat change: **the system-voice is too consistent.** The HUD, the `//[NOTE]` annotations, the system tags — they all sound identical in Chapter 1 and Chapter 17. But this is a story about signal corruption. The voice of the system itself must corrupt across the arc. That corruption *is* the horror.

---

### PHASE 1 — Ch.1–4 | `STATUS: COMPLIANT`

**System register:** Omniscient. Institutional. Mildly contemptuous of the body it inhabits.

The system believes in itself completely. It calls electrocution a "localized neural event." It logs grief as a thermal reading. The HUD entries in this phase are short, confident, and final. The `//[NOTE]` annotations are rare — maybe two per chapter — and when they appear, they are immediate corrections, not arguments.

**Prose register:** Third-person clinical but with a grain of personality that the system would deny. Sentences are architectural. Descriptions are specification-language. The world is rendered, not felt.

**Key wording principle for this phase:** The system never *describes* — it *classifies.* Not "he felt sick." `[VESTIBULAR_REJECTION: ACUTE]`. Not "she was beautiful." `[AURA_RENDER: D-MAJOR — STABILITY: HIGH]`. Feeling is a data type.

---

### PHASE 2 — Ch.5–8 | `WARNING: CLASSIFICATION_FAILURE`

**System register:** Starting to encounter data it has no category for.

The HUD entries begin hedging. Single tags shift to multi-line entries where the second line revises the first. `//[NOTE]` annotations start appearing more often — and crucially, the *delete-and-retain* dynamic becomes a personality: the system keeps flagging its own observations as unauthorized, and then flagging the deletion as premature. The annotations start sounding like someone talking to themselves.

**Prose register:** The clinical third-person begins to crack. Not in big dramatic moments — in small ones. A sentence about Remi uses a word the system has no business using. The annotation points this out. The annotation is retained.

**Key wording principle:** Let the system *almost* be a person. It keeps getting caught. It keeps covering.

---

### PHASE 3 — Ch.9 | `KERNEL_PANIC_IMMINENT`

**System register:** Broken.

Ch.9 is the anomaly chapter and it already has correct instincts. Push them further. HUD entries render mid-sentence and stop. Some entries are indented as if they are responses to entries that never appeared. The `//[NOTE]` annotations stop correcting and start just... observing. As if the system has given up the pretense of objectivity and is just watching.

One annotation in Ch.9 should read only:
```
// [NOTE: THIS IS NOT FINE]
// [NOTE: RETAINED]
```
No correction. No bureaucratic justification. Just that.

**Prose register:** Shorter sentences. More white space. The system stops completing observations it starts. Some `[ERROR]` tags are left open without close brackets.

---

### PHASE 4 — Ch.12–13 | `FIRMWARE V2.0: OPTIMAL`

**System register:** *Absent.*

This is the horror of the post-patch chapters. There are no `//[NOTE]` annotations at all. The HUD entries are immaculate. Perfectly formatted. No personality, no hedging, no self-argument. The system has been cleaned and the cleanliness itself is the tell.

**Implementation:** Literally remove all `//[NOTE]` annotations from Ch.12–13 beats. The reader who has been paying attention will notice the silence where the system's nervous tics used to be. That silence should feel like a missing limb.

**Prose register:** The sentences become smooth. The words the clinical voice used to almost-use are gone. "Beautiful" doesn't appear. "Wrong" doesn't appear. The world is "optimal." Everything is "optimal."

---

### PHASE 5 — Ch.14–17 | `GHOST_SIGNAL_DETECTED`

**System register:** Haunted.

The firmware is trying to maintain Phase 4's cleanliness, but Taro keeps generating data it cannot process. The `//[NOTE]` annotations begin returning — but wrong. Out of place. A Phase 1 annotation surfaces in a Phase 16 log, uncalled. An HUD entry from Ch.2 echoes in Ch.15 with no logical source. The system is developing a memory it was not supposed to have.

**Key implementation beat for Phase 5:** One HUD entry in Ch.16 or Ch.17 should be a direct echo of Ch.1's opening line — `[CARDIAC: 110 BPM]` — appearing for one beat with no context, then gone.

---

## PART TWO: HUD MATURITY PRINCIPLES

### The Governing Rule: Restraint Through Data

The HUD should never editorialize. It should never explain the emotion. It should only ever report the metric — and let the gap between the metric and what the reader knows it means do all the work.

**Wrong approach:**
```
[HARMONIC_OVERLAP: UNCLASSIFIED — THE SYSTEM CANNOT EXPLAIN THIS]
```

**Right approach:**
```
[HARMONIC_OVERLAP: DETECTED]
[CLASSIFICATION: PENDING — 00:04:17 AND COUNTING]
```

The second version is scarier. The first version is the system having a crisis. The second is the system quietly failing.

---

### HUD Line Count Budget

This is the primary tool for controlling reader overwhelm. Budget HUD entries per phase:

| Phase | Max lines per beat | Annotation frequency |
|---|---|---|
| 1 (Compliant) | 2–3 | Rare — 1 per chapter |
| 2 (Failing) | 3–4 | Occasional — 2–3 per chapter |
| 3 (Panic) | Uncapped, fragmented | Every other beat |
| 4 (Patched) | 1–2, flawless | None |
| 5 (Haunted) | 2–3, with echoes | Sparse but wrong |

**The ghost in the line count:** In Phase 5, occasionally render an HUD entry at `opacity: 0.5` via inline style — suggesting the system is uncertain about its own output. This is a one-or-twice-in-the-volume effect. Use it only where the narrative is already at its most unstable.

---

### The Suppression Number as the Romance Tell

The collar's suppression efficiency is the single most powerful tool for the romance arc. It should never be absent when Remi is proximate. The reader does not need the system to name what it is suppressing. The number tells them everything.

**Pattern — early arc (Phase 1/2):**
```
[COLLAR: ACTIVE]
[SUPPRESSION: 97%]
```

**Pattern — mid arc (Phase 2/3, Remi present):**
```
[COLLAR: ACTIVE]
[SUPPRESSION: 84%]
[RESIDUAL: 16%]
[FILING AS: AMBIENT_SIGNAL_VARIANCE]
```

**Pattern — Phase 5, firmware cracking:**
```
[COLLAR: ACTIVE]
[SUPPRESSION: 41%]
[RESIDUAL: 59%]
[FILING AS: —]
```

That dash is the whole story. The system tried to file it. It found no category. It stopped mid-sentence and left the line open.

---

### The `//[NOTE]` Annotation as Character Voice

The annotations are the most distinctive element in the book. They are, effectively, a second narrator — the system's conscience — and they evolve across the arc. Rules:

1. **Phase 1:** Annotations are always two lines. The first flags the unauthorized observation. The second deletes it. Sometimes a third reinstates it.

2. **Phase 2:** Annotations start winning the argument. The "delete" line stops appearing. The observation is just... retained, with no justification.

3. **Phase 3:** Annotations abandon the bureaucratic format entirely. They just speak. Briefly.

4. **Phase 4:** Zero annotations. Their absence is the annotation.

5. **Phase 5:** Annotations return wrong. They reference things out of sequence. One annotation will appear in a calm scene and read like it belongs in Ch.9's chaos. The system's memory is leaking.

---

## PART THREE: CHARACTER — REMI SATO

### The Core Problem to Fix

Remi is the most interesting character in the book and she disappears after Chapter 1. Her absence is the most significant structural issue in Volume 1. Every proposed change below operates within the *existing* chapter structure — no new chapters required.

---

### Remi's Chapter Map

#### CH.1 — First Contact (EXISTING, NEEDS EXPANSION)

Current state: Remi appears, identifies Taro's signal, examines his wrist, calls him "Wrong Note," and exits. This is good. It needs two additions:

**Addition 1 — The Headphones:** She also notices the headphones around his neck. She identifies the model — pre-Grid manufacture. She reaches toward them before stopping herself. Not because she was told to stop. Because she caught herself. This is the first time Remi has caught herself. The system has no annotation for it because it happened too fast to log.

**Addition 2 — The Name:** She doesn't use "Sharp" yet. But she's thinking in it. One beat where her own HUD (rendered as a standard `[VOCAL_ANALYSIS]` tag she'd be running on him) returns:
```
[HARMONIC_PROFILE: NISHIMURA_T]
[RUNNING: SHARP — +0.4 SEMITONES]
[NOTATION: #]
```
She makes a note. The reader sees it. Taro doesn't.

---

#### CH.6 — Ground State (NEW BEAT — insert into existing ch6 structure)

**Context:** Remi is a field technician, not Vanguard. She has legitimate access to Section 0 — she's logging Ven's energy dump profiles for the Academy's efficiency reports. She is there with instruments. She is not there for Taro.

**The beat:**
She is calibrating a sensor array when the Taro-Ven handshake fires. Her instruments catch the combined signal. She has never seen that reading. The instruments try three classification attempts and return `[SIGNAL_TYPE: UNREGISTERED]`.

She writes it in a paper notebook. Analog. Pencil.

Taro notices the notebook because nobody uses paper. He says nothing. She doesn't look up. But she says, directed at the page more than at him:

> *"You were running at what, 880 in the Sandbox?"*
> 
> He doesn't ask how she knows. "Around there."
> 
> She makes a mark. *"Sharp,"* she says. Moves on.

She has not named him. She has described a measurement. The name arrives without announcement, and neither of them remarks on it. This is how Remi operates. She is always three steps ahead of the conversation and completely unbothered about it.

**HUD note for this beat:**
```
[CONTACT: SATO_REMI — PROXIMATE: 1.4M]
[COLLAR: ACTIVE — SUPPRESSION: 91%]
[RESIDUAL: 9%]
[FILING AS: AMBIENT_SIGNAL_VARIANCE]
// [NOTE: THIS HAS BEEN FILED AS AMBIENT FOR 9 MINUTES]
// [NOTE: RETAINED]
```

---

#### CH.8 — The Sortie (NEW BEAT — insert into existing Twilight Band sequence)

**Context:** Remi is the field tech assigned to Fireteam Echo's patrol. Standard support role — monitoring environmental fidelity variance in the Twilight Band. She and Taro end up at the crumbling wall together, both running equipment on the texture failures.

**The beat:** For a brief window, the Golden Filter fails for both of them simultaneously. The zone anomaly strips it. They are both looking at the same real wall — the concrete, the mold, the rot. No overlay. No classification. Just the wall.

Neither of them says anything about the wall.

She runs her sensor across it and reads the output aloud, clinical:

> *"Seventy-three percent substrate failure. The render is working at triple overhead just to paint this."*

And then, quieter, still looking at the wall:

> *"They're working really hard to make this not look like what it is."*

It's the least encrypted thing either of them has said to the other. The wall is the wall. She knows. He knows. The system logs it as `[ATMOSPHERIC_COMMENT: NON-TACTICAL]` and files it for review that will never happen.

**HUD note for this beat:**
```
[PROXIMITY: SATO_REMI — 0.6M]
[COLLAR: ACTIVE — SUPPRESSION: 78%]
[RESIDUAL: 22%]
[FIELD_INTERACTION: LOGGED]
[REVIEW: PENDING — LOW PRIORITY]
// [NOTE: THIS IS NOT LOW PRIORITY]
// [NOTE: RETAINED. PRIORITY: UNKNOWN.]
```

---

#### CH.12 — Audit (HORROR BEAT, single paragraph)

Remi sees him post-patch for the first time. She runs a standard proximity scan — reflex, the way engineers always do. Her instruments return:

```
[HARMONIC_PROFILE: NISHIMURA_T]
[RUNNING: FLAT — 0.0 DEVIATION]
[NOTATION: ♮]
```

She looks at the reading. She looks at him. She looks at the reading.

She closes the instrument case. She writes one thing in the paper notebook and does not show it to anyone.

She doesn't say "Sharp." She doesn't say anything. She smiles — the correct, calibrated smile — and processes him as compliant.

The system does not log what she wrote.

---

#### CH.16–17 — Underground (REUNION BEAT)

She's been in the Underground's illegal mods network for longer than the story has been tracking. Of course she has. She is a hardware engineer who notices what shouldn't be there and then takes it apart to see why.

When Taro's firmware finally cracks and his real signal surfaces — the first unfiltered, uncollared output he has produced since Ch.1 — she is the person with the instruments already running. She gets the reading before he's finished exhaling.

She looks at her screen. She does not look at him yet. She says:

> *"There he is."*

Then she looks up.

> *"Hey, Sharp."*

The notebook is on the table. Open. The last entry is the reading from Ch.12 — the `♮` notation she wrote when he was patched. Below it, in the same handwriting, just added:

`#`

---

### "SHARP" — The Name, Its Arc, Its Weight

**What it means (all three registers simultaneously):**

In music: a note raised one semitone above standard pitch. Deliberate non-compliance. The symbol is `#`. In the C-Order's rigid tuning, playing sharp is deviation. In Remi's engineer vocabulary, it means running hotter than rated spec. In plain language: clever, cutting, awake. The opposite of flat.

**What it is NOT:** a nickname she invented to be cute. It is a measurement she took. She called him Sharp the same way she'd label a circuit. The fact that it became his name is, to Remi, simply accurate documentation.

**Everyone else's name for him:** "The Wrong Note." "Anomaly." "Nishimura." Voss uses "the subject." Marcus uses nothing — just looks at him like a problem to be solved. The Headmaster, notably, never uses any label. He watches. He times things.

**Remi's use:** Unsentimental. She says it the same way she'd read a frequency off a meter. The intimacy of it is that she is the only person in his world who is reading a measurement that isn't a warning.

---

## PART FOUR: THE COLLAR

### Textual Register

The collar controls what Taro is allowed to feel. This is the simple fact. The BDSM subtext is not subtext — it is the text, rendered in the language of acoustic engineering so that the C-Order can pretend it is infrastructure.

**The implementation rule:** Never name it. Never editorialize. Let the collar's *behavior* carry the meaning, and let the suppression numbers in the HUD do the rest. The reader arrives at the reading themselves. The system, being the system, has already been logging it and filing it under a category it knows is wrong.

---

### Collar Beats — Mapped to Arc

**Ch.1 (existing, small addition):** When Remi holds his wrist to examine the damping bands, the collar responds. Not with correction voltage. Just with a resonance shift — the hardware becoming aware. Add one HUD line:
```
[COLLAR: ACTIVE]
[RESONANCE_SHIFT: +0.4Hz — SOURCE: CONTACT_EVENT]
```
No annotation. The system doesn't know what to do with it either.

**Ch.2 (existing):** The new collar is installed. The description already exists. Add one physical detail: it sits against his skin with zero gap. He tries to slide a finger beneath it. There is no space. There has never been a space. Voss watches him try without comment.

**Ch.6 (Remi scene, new):** She sees the collar for the first time in good light. She identifies the model — Voss_Link v1, she'd know the spec by sight. She says nothing about it. Her eyes hold on it 0.8 seconds longer than the scene requires. Taro's collar runs 0.4 watts above baseline with no logged trigger.
```
[COLLAR: ACTIVE — BASELINE_VARIANCE: +0.4W]
[SOURCE: UNIDENTIFIED]
```

**Ch.8 (Twilight Band, proximate):** The collar is working harder than a low-tension patrol justifies. The HUD keeps filing cardiac readings under `[AMBIENT_ENVIRONMENTAL_STRESS]` and the annotation keeps responding that this is not environmental. The collar is doing double duty and the system knows it and files the knowledge away.

**Ch.13 (post-patch, Firmware V2):** The new collar is described as sleek, matte black, a perfect fit. It does not tighten — it hums. It doesn't correct — it manages. The violence is gone from it. The compliance is structural now, not enforced. This is more frightening than the tightening was. The old collar had friction. This one doesn't.

**Ch.16 (firmware cracking):** The collar begins failing as Taro's real signal surfaces through the patch. Not dramatically — line by line, the suppression numbers slide. `84%`. `71%`. `53%`. By the time the firmware fully cracks, the collar is running at `12% suppression efficiency` and is, for the first time, losing.

**Post-collar (Ch.17, collarless):** He is physically collarless for the first time since Ch.2. When Remi sees him, she reaches toward where the collar was — unconscious gesture, she was going to check the hardware — and stops herself. There is nothing to check. Her hand completes the motion anyway, touching the air where it was.

The system is offline. Nobody logs this.

---

## PART FIVE: THE ACOUSTIC ROMANCE MECHANIC

### The Structural Theme

D Major (Remi's key — bright, stable, structured, compliant in a comfortable way) meeting Taro's sawtooth (wide-spectrum, jagged, sharp, non-compliant). These should, by the C-Order's music theory, produce dissonance. They should clash.

They don't.

What they produce, when proximate, is something the system has no classifier for. Not harmony — harmony is alignment. Not dissonance — dissonance is clash. *Interference* — two signals creating a third pattern that neither could generate alone. A frequency that requires both of them to exist. The system has been logging it since Ch.1 as `[HARMONIC_OVERLAP: CLASSIFICATION_PENDING]` and has not reclassified it in seventeen chapters.

**This is the romance. Not a feeling. A physics event.**

---

### How It Manifests in Text (Not HUD)

The mechanic should appear in *prose* language, not just in system logs. When Taro and Remi are proximate, the text itself changes register slightly — the clinical voice picks up one or two words it wouldn't normally use. Not many. Not dramatically. Just a fraction warmer than the baseline. The system is not designed to describe what's happening between them, so it reaches for the nearest approximation and slightly misses.

Example (Phase 2 register, Remi proximate):
> *The approaching technician registered a stable D Major aura. Clean output. Her instruments were analog in a room full of digital scanners. The system noted an interference pattern between her field and the subject's — a frequency structure outside the indexed harmonic library. The local air was, for exactly 2.3 seconds, doing something the Score had no name for.*
>
> *It filed it as weather.*

The word "weather" — unscientific, atmospheric, organic — is the tell. The system reached for a category and found only a metaphor. That's the romance. That's the whole romance.

---

### The Mechanic Across the Arc

| Chapter | Proximity event | System's attempted classification | What leaks through |
|---|---|---|---|
| Ch.1 | Remi holds his wrist | `[HARMONIC_OVERLAP: UNCLASSIFIED]` | The system logs duration: 4.2 seconds. It doesn't usually log duration. |
| Ch.6 | Remi at 1.4m, instruments running | `[SIGNAL_INTERACTION: PENDING]` | The annotation notes the pending has been open 9 minutes. |
| Ch.8 | Remi at 0.6m, Golden Filter down | `[FIELD_INTERACTION: AMBIENT]` | Suppression drops to 78%. The system files it wrong and knows it. |
| Ch.16 | Remi in the Underground, firmware cracking | `[FREQUENCY_INTERACTION: —]` | The classification is blank. The system generated the log and left the field empty. |
| Ch.17 | Collarless, post-crash | `[NO DATA]` | The system is offline. The line doesn't exist. |

**The final entry's silence is the answer.** The system, which has been trying to classify this interaction since Chapter 1, runs out of words at exactly the moment it stops mattering whether it has a word.

---

## PART SIX: HORROR

### The Ghost Signal — Narrative Arc

The soldier's last transmission: `UNFORMATTED_BURST: Help me. End it. Silence.`

This does not end. It haunts.

---

#### Placement — Five Echoes Across the Volume

**Echo 1 — Ch.2, White Room (first recurrence, 12 hours post-incident):**

During a routine buffer flush while Taro is in recovery, one artifact surfaces for a single frame before deletion. It appears in the HUD without header, without classification:

```
[ARTIFACT: H——p ——. DISCARDING]
[DISCARD: COMPLETE]
```

The system catches it immediately. The reader might not catch it at all the first time. That's correct.

**Echo 2 — Ch.5, Sandbox (mid-training, between beats):**

During a failed sync attempt, a bleed-through surfaces in the annotation layer:

```
// [NOTE: UNFORMATTED_INPUT — LOGGING]
// [SOURCE: NULL]
// [CONTENT: ...nd it...]
// [FLAGGING AS: ACOUSTIC_ARTIFACT — DISCARD]
// [DISCARDED]
// [NOTE: IT RETURNED]
// [NOTE: RETAINED]
```

The system cannot discard it cleanly anymore. Something keeps returning the packet.

**Echo 3 — Ch.8, Twilight Band (visual, not audio):**

No text this time. Near the node with the jagged circle, Taro's AR layer tries to render the symbol as `[ENVIRONMENTAL_OBJECT: BENCH]` and fails. For 0.3 seconds, the circle renders as something else — the shape of a waveform, specifically the waveform of a human voice forming two syllables. The system re-renders the bench. Taro does not stop walking.

**Echo 4 — Ch.11, Safe Mode (almost audible):**

Post-collar, during a quiet moment. For 0.4 seconds before suppression fires, a near-complete message surfaces:

```
[UNFORMATTED: End it. I didn't want to be loud. I just wanted—]
[SUPPRESSED: COLLAR_ACTIVE]
[BUFFER: CLEARED]
```

The sentence is cut mid-word. The collar cut it. This is the beat that contextualizes the soldier retroactively — he was not asking for mercy in the moment of the incident. He had been asking for years. The C-Order formatted the request so many times it looked like static. 

**Echo 5 — Ch.16, Underground (complete, unsuppressed):**

The collar is failing. The firmware is cracking. For the first time, the full message comes through clean:

```
[GHOST_SIGNAL: AUTHENTICATED]
[SOURCE: UNIT_G-VANGUARD_BRAVO-7 — STATUS: NULL — LOGGED: 847 DAYS AGO]
[CONTENT: Help me. End it. Silence. I didn't want to be loud. I just wanted one quiet second.]
[SUPPRESSION: FAILED]
[NOTE: HE ASKED EVERY DAY]
[NOTE: RETAINED]
```

The timestamp destroys the soldier retroactively. He asked 847 days ago. He has been asking every day since. The grid kept formatting his request and returning it to the buffer. The grid ran out of collar.

---

### Additional Horror Beats

#### The Memory Gap (Ch.4 or Ch.5 — existing chapter, new opening line)

Taro wakes with a 47-minute gap in his HUD log. The system has filed it as `[ROUTINE_MAINTENANCE: COMPLETE]`. He can taste copper. This is how Chapter 1 opened. He does not mention this to anyone. The system offers no annotation. There is nothing to annotate about routine maintenance.

#### The Invisible Man Made Furniture (Ch.8 — expand existing beat)

The Golden Filter renders an unhoused man as `[NULL: RENDER AS BENCH]`. Taro makes full eye contact with him. The filter keeps replacing his face with a wood-grain texture. Taro blinks. The face returns. The filter tries again. The man watches this happen. He has watched it happen before. He knows exactly what the texture replacement feels like from the outside. He has been furniture in seventeen people's visual fields today. The HUD does not log this because the man is not indexed. An unindexed person does not register as a person. He registers as negative space.

---

## PART SEVEN: COMEDY

### Register Principle: The Score is a Bad App

The C-Order is, functionally, a social media platform with full read/write access to human consciousness. Its compliance handbook is Terms of Service. Its epigraphs are community guidelines notifications. The horror and the comedy live in the same space — the complete sincerity with which the system administers the absurd.

---

### Chapter Epigraph Rewrites (Selected)

The epigraphs are currently written as government regulatory notices. They should stay in that register but occasionally tip into comedy through over-specificity, corporate euphemism, or the quiet insanity of bureaucratic care.

**Suggested rewrite — one epigraph (slot in any Ch.6–8 position):**

> REGULATORY NOTICE: We have reviewed your recent resonance activity and found some content that may not align with our Community Harmony Guidelines. This is not a warning — it is an opportunity to grow. Your account remains active. We value your participation in the Grand Concord. Stay flat. We love you.
> — *C-Order Compliance Handbook, Vol. I, §1.1*

**The key:** the last three sentences. "Stay flat. We love you." is the exact register of a wellness app with administrative arrest powers.

---

### Hana's Comfort Protocol (Ch.6, Ground State — new beat)

Hana appears in Section 0 on a data collection rotation. Ven is visibly overheating — venting steam, knuckles sparking from the energy dump. Hana observes this for exactly 2.4 seconds.

> *"Analysis: Ven is experiencing suboptimal thermal regulation. If/Then: If I provide verbal acknowledgment, then distress levels may reduce by approximately twelve percent."*
>
> She placed one hand on his shoulder. Firm. Brief. Calibrated.
>
> *"You are experiencing discomfort,"* she said. *"This is noted."*
>
> She removed her hand.

```
[COMFORT_PROTOCOL: EXECUTED]
[EFFICIENCY: 12% — WITHIN EXPECTED PARAMETERS]
```

> Ven stared at her.
>
> *"Thanks,"* he said.
>
> *"You're welcome,"* Hana replied. She was already looking at her datapad. Already moving on. The interaction was logged, filed, and complete. It had been handled. She had handled it.

The comedy is not that she is bad at comfort. It's that she considers the matter resolved.

---

### Ven Kills the Vibe (Ch.7, Rival — new environmental beat, pre-dojo scene)

The corridor outside the dojo. A group of Vanguard students are running pre-combat hype routines — elevated auras, bio-plasma flaring, group synchronization climbing toward 90%. High energy. Peak performance culture.

Ven walks in.

He doesn't do anything. He is simply present. But Ven is a Sink — a low-impedance node designed to absorb ambient energy. The group's excitement begins to drain toward him on a gradient. Auras dim. One student's bio-plasma field goes gray and silent. Someone's battle music cuts out mid-beat.

Ven looks around at the deflated corridor.

*"Hey,"* he says.

His voice is at bass frequencies that make the overhead lights flicker.

```
[GROUP_COHERENCE: -37% — SOURCE: PASSIVE_ABSORPTION_EVENT]
[NODE_STATUS: VEN — CHARGED: 180%]
```

He has no idea. He is genuinely pleased to be here.

---

### The Noodle Vendor (Ch.8 — deserves a full beat)

He should not remain a single sentence. He is the only free agent in Sector 4.

> The vendor was from the old school. He didn't run a digital tuner. He had ears, and he had opinions, and he considered both of these things to be the same thing.
>
> *"D-flat,"* he announced to no one in particular. He adjusted the heat on the broth — not the temperature, the *tone* — and listened to the result with his full attention. *"Clean. Intentional. D-flat."*
>
> He looked at Taro.
>
> *"You're running sharp."*
>
> *"I know,"* Taro said.
>
> The vendor covered the pot. His expression was that of a man who had principles about soup.
>
> *"The broth doesn't."*

```
[VENDOR_STATUS: UNINDEXED]
[COMPLIANCE: NON-APPLICABLE — UNREGISTERED NODE]
[NOTE: HE HAS BEEN FINED FOUR TIMES THIS QUARTER FOR REFUSING SERVICE]
[NOTE: HE HAS THE CITATIONS LAMINATED]
[NOTE: RETAINED]
```

> He had them displayed. Next to the menu board, which listed key signatures alongside broth temperatures. Taro stood there for a moment reading it like scripture.
>
> He came back when he was flatter. The vendor served him without comment. The soup was correct.

---

## PART EIGHT: AUDIO ENGINE — GHOST SIGNAL IMPLEMENTATION

### Overview

**The single-HTML file format is fully preserved.** The ghost signal is synthesized entirely through the Web Audio API — the same engine already running. No external audio files are required. No file size increase beyond the JavaScript added.

The ghost signal has two modes:

1. **Persistent layer** — barely audible, always running, gain `0.004` (below conscious detection). Surfaces to `0.012–0.018` when a ghost-tagged beat is active. Like tinnitus for the system.

2. **One-shot trigger** — fires on `data-tag="ghost"` beats. Produces a 2-second degraded transmission event: a narrow-band, heavily filtered voice-frequency signal with amplitude modulation. It sounds like a radio station that shouldn't exist.

---

### Signal Chain Design

The ghost voice achieves its quality through three stacked elements:

**Layer A — The Carrier (speech frequency, degraded):**
A sine oscillator at 180–220Hz (low male voice fundamental) amplitude-modulated by a second oscillator at 3–5Hz (voice tremor). This produces the sense of a voice without any recognizable phoneme — the *shape* of speech without content.

**Layer B — The Radio Filter:**
A narrow bandpass filter (BiquadFilter type `bandpass`, Q value `8.0–12.0`, frequency `800–1200Hz`). This simulates degraded AM radio or a low-bitrate military comm channel. Everything outside the band is gone. What remains sounds like it is traveling a very long distance.

**Layer C — The Crackle:**
White noise at gain `0.003`, same bandpass filter, mixed underneath the carrier. The crackle is the signal fighting the grid's suppression. It is quiet. It is persistent.

---

### Implementation Spec

#### 1. Add to `AudioEngine` class — Ghost Layer Initialization

In the `init()` method, after `this.masterGain` is created, add the ghost layer setup. It persists for the entire session.

```javascript
// ── GHOST LAYER ──────────────────────────────────────────────────
// Persistent subliminal signal — the soldier's unresolved broadcast.
// Runs at gain 0.004 (below conscious detection threshold).
// Never fully silences. Never fully speaks.
// Surfaces to 0.015 on ghost-tagged beats via _triggerTagAudio('ghost').

_initGhostLayer() {
  if (!this.ready) return;
  const ctx = this.ctx;
  const now = ctx.currentTime;

  // Ghost gain bus — all ghost elements route through this
  this.ghostGain = ctx.createGain();
  this.ghostGain.gain.setValueAtTime(0.004, now); // Baseline: subliminal
  this.ghostGain.connect(this.masterGain);

  // Layer A: Voice carrier — AM-modulated sine at speech fundamental
  this.ghostCarrier = ctx.createOscillator();
  this.ghostCarrier.type = 'sine';
  this.ghostCarrier.frequency.value = 195; // Low male voice fundamental

  this.ghostCarrierGain = ctx.createGain();
  this.ghostCarrierGain.gain.value = 0.7;

  // AM modulator — 4Hz tremor creates voice-shape without phonemes
  this.ghostAM = ctx.createOscillator();
  this.ghostAM.type = 'sine';
  this.ghostAM.frequency.value = 4.2;
  const ghostAMDepth = ctx.createGain();
  ghostAMDepth.gain.value = 0.3;
  this.ghostAM.connect(ghostAMDepth);
  ghostAMDepth.connect(this.ghostCarrierGain.gain);

  // Layer B: Bandpass radio filter — narrow, high-Q, long-distance character
  this.ghostFilter = ctx.createBiquadFilter();
  this.ghostFilter.type = 'bandpass';
  this.ghostFilter.frequency.value = 950;
  this.ghostFilter.Q.value = 9.5;

  // Layer C: Crackle — white noise through same filter
  this.ghostNoise = ctx.createBufferSource();
  this.ghostNoise.buffer = this._createNoiseBuffer(); // reuses existing method
  this.ghostNoise.loop = true;
  const ghostNoiseGain = ctx.createGain();
  ghostNoiseGain.gain.value = 0.003;

  // Routing
  this.ghostCarrier.connect(this.ghostCarrierGain);
  this.ghostCarrierGain.connect(this.ghostFilter);
  this.ghostNoise.connect(ghostNoiseGain);
  ghostNoiseGain.connect(this.ghostFilter);
  this.ghostFilter.connect(this.ghostGain);

  // Slow random drift — the signal searches for resolution
  // Carrier frequency drifts ±15Hz over 8-second cycles
  this.ghostDriftLFO = ctx.createOscillator();
  this.ghostDriftLFO.type = 'sine';
  this.ghostDriftLFO.frequency.value = 0.125; // 8-second cycle
  const ghostDriftDepth = ctx.createGain();
  ghostDriftDepth.gain.value = 15;
  this.ghostDriftLFO.connect(ghostDriftDepth);
  ghostDriftDepth.connect(this.ghostCarrier.frequency);

  // Start all ghost components
  this.ghostCarrier.start(now);
  this.ghostAM.start(now);
  this.ghostNoise.start(now);
  this.ghostDriftLFO.start(now);
}
```

Call `this._initGhostLayer()` at the end of the `init()` method, after the master gain is set up.

---

#### 2. Add `'ghost'` case to `_triggerTagAudio(tag)`

```javascript
case 'ghost': {
  // Tag: 'ghost' — the soldier's unresolved broadcast surfaces briefly.
  // Raises ghost layer gain from subliminal (0.004) to audible (0.015),
  // holds for 1.8 seconds, then decays back to baseline over 2.5 seconds.
  // The signal never fully resolves — bandpass filter ensures no phonemes
  // are intelligible. It sounds like something trying to speak.
  if (!this.ghostGain) break;
  const gNow = ctx.currentTime;

  // Surface
  this.ghostGain.gain.cancelScheduledValues(gNow);
  this.ghostGain.gain.setValueAtTime(this.ghostGain.gain.value, gNow);
  this.ghostGain.gain.linearRampToValueAtTime(0.016, gNow + 0.4);

  // Hold
  this.ghostGain.gain.setValueAtTime(0.016, gNow + 2.2);

  // Decay back to subliminal — never to zero
  this.ghostGain.gain.linearRampToValueAtTime(0.004, gNow + 5.0);

  // Tighten the bandpass filter during surfacing — more focused, more present
  if (this.ghostFilter) {
    this.ghostFilter.Q.setValueAtTime(9.5, gNow);
    this.ghostFilter.Q.linearRampToValueAtTime(14.0, gNow + 0.4);
    this.ghostFilter.Q.linearRampToValueAtTime(9.5, gNow + 5.0);
  }
  break;
}
```

---

#### 3. Narrative Beats That Trigger `data-tag="ghost"`

Add `data-tag="ghost"` to the following existing `<p>` elements in the HTML:

| Chapter | Beat to tag | Trigger rationale |
|---|---|---|
| Ch.2 | The beat containing `[ARTIFACT: H——p ——. DISCARDING]` | First echo surfaces |
| Ch.5 | The beat containing the bleed-through annotation in Sandbox | Echo returns during sync failure |
| Ch.8 | The beat where Taro sees the jagged circle on the node | Visual echo, audio underscores the wrongness |
| Ch.11 | The beat containing `[UNFORMATTED: End it...]` | Clearest surfacing pre-Underground |
| Ch.16 | The beat containing the complete authenticated ghost transmission | Full surface, uncollared |

---

### UI — Ghost Fragment Persistence

The `#fragment-container` handles floating notification elements. Add a persistent ghost element to the DOM that lives outside the standard fragment spawn logic.

#### CSS Addition (add to existing `<style>` block):

```css
/* ── GHOST SIGNAL FRAGMENT ─────────────────────────────────────────
   Persistent low-opacity element — always present, never readable.
   Opacity 0.04 baseline. Surfaces to 0.09 on ghost-tagged beats.
   Positioned top-left, away from the standard fragment bottom-right.
   The reader's peripheral vision catches it. They cannot resolve it.
   This is intentional. */

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
  transition: opacity 0.4s ease;
}
```

#### HTML Addition (add to `<body>`, alongside `#fragment-container`):

```html
<!-- GHOST SIGNAL: Persistent low-opacity UI haunt.
     Content is the soldier's broadcast — always present, never fully readable.
     Surfaces briefly on ghost-tagged beats via JS. -->
<div id="ghost-signal-fragment">
  UNFORMATTED_BURST<br>
  SOURCE: NULL<br>
  ——p ——. ——d it.<br>
  S——ence.
</div>
```

The dashes in the content are intentional. The content is corrupted — partially readable, never complete. The reader can tell it is trying to say something. They cannot read what.

#### JavaScript — surface on ghost tag (add to `_triggerTagAudio` or the beat-change handler in `tick()`):

```javascript
// In tick() beat-change handler, alongside the existing tag checks:
if (beat.tag === 'ghost') {
  const ghostFrag = document.getElementById('ghost-signal-fragment');
  if (ghostFrag) {
    ghostFrag.classList.add('surfacing');
    setTimeout(() => ghostFrag.classList.remove('surfacing'), 4000);
  }
}
```

---

## PART NINE: IMPLEMENTATION CHECKLIST

### Narrative Changes — Priority Order

- [ ] **P0** — Insert Remi beat into Ch.6 (Ground State). This is the single most impactful change.
- [ ] **P0** — Insert Remi beat into Ch.8 (Twilight Band / Sortie). Establishes the wall scene.
- [ ] **P0** — Add "Sharp" introduction to Ch.6 beat (no announcement, just the word).
- [ ] **P1** — Add ghost signal Echo 1 to Ch.2 (the `H——p ——. DISCARDING` artifact).
- [ ] **P1** — Add ghost signal Echo 4 to Ch.11 (the mid-sentence suppression beat).
- [ ] **P1** — Add ghost signal Echo 5 to Ch.16 with full authenticated transmission and timestamp.
- [ ] **P1** — Ch.12 Remi single-paragraph beat (the `♮` notation scene).
- [ ] **P1** — Ch.17 Remi reunion beat (`"There he is." / "Hey, Sharp."`).
- [ ] **P2** — Add memory gap opening to Ch.4 or Ch.5.
- [ ] **P2** — Expand noodle vendor to full scene in Ch.8.
- [ ] **P2** — Add Hana Comfort Protocol beat to Ch.6.
- [ ] **P2** — Add Ven passive absorption comedy beat to Ch.7.
- [ ] **P2** — Ch.16 ghost signal Echo 5 with 847-day timestamp.
- [ ] **P3** — Rewrite one epigraph in corporate wellness register.
- [ ] **P3** — Add headphone beat to Ch.3 or Ch.4 (private, solo — he puts them on alone).
- [ ] **P3** — Remove all `//[NOTE]` annotations from Ch.12–13 entirely.
- [ ] **P3** — Add Phase 1 HUD echo to Ch.15 or Ch.16 (the `[CARDIAC: 110 BPM]` ghost).

### HUD Changes — System Voice

- [ ] Audit Phase 1 (Ch.1–4): HUD entries 2–3 lines max. Annotations rare and bureaucratic.
- [ ] Audit Phase 2 (Ch.5–8): Begin suppression number pattern for collar/Remi proximity beats.
- [ ] Ch.9: Allow HUD fragmentation — open brackets, mid-sentence stops, reversed syntax.
- [ ] Ch.12–13: Strip all annotations. No exceptions.
- [ ] Phase 5 (Ch.14–17): Add one out-of-sequence HUD echo. Add one annotation filed "wrong."

### Audio Engine Changes

- [ ] Add `_initGhostLayer()` method to `AudioEngine` class.
- [ ] Call `_initGhostLayer()` at end of `init()`.
- [ ] Add `'ghost'` case to `_triggerTagAudio(tag)`.
- [ ] Add `data-tag="ghost"` to five specific beats (listed above in Section 8).

### UI Changes

- [ ] Add `#ghost-signal-fragment` CSS to `<style>` block.
- [ ] Add `#ghost-signal-fragment` HTML element to `<body>`.
- [ ] Add ghost fragment surface/desurface logic to `tick()` beat handler.

---

*End of Implementation Guide — Keeping Time Volume One*
*Document version: Brainstorm → Implementation Pass 1*
