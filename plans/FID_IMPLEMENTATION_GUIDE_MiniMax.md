# FREE INDIRECT DISCOURSE — IMPLEMENTATION GUIDE
## For: MiniMax 2.5 | Project: *Keeping Time* | Author Reference

> **What this document is:** A precise, rule-based system for applying Free Indirect Discourse (FID)
> to the *Keeping Time* manuscript. This guide is formatted for AI agent use — every rule is
> explicit, every instruction is actionable, and every example is drawn from the project's
> existing characters and world.
>
> **Mandatory prerequisite files:** `WRITER_GUIDE.md`, `03_CHARACTERS_REGISTRY.md`, `VOICE_GUIDE.md`

---

## SECTION 1: WHAT IS FID — THE ONE-SENTENCE DEFINITION

**Free Indirect Discourse (FID)** is third-person narration that temporarily borrows the POV
character's vocabulary, rhythm, and emotional bias — without using a dialogue tag like
"he thought" or "he felt."

The narrator and the character merge. Then they separate again. The reader always knows
whose voice is bleeding through because of *word choice* and *sentence rhythm*, not because
the author labeled it.

---

## SECTION 2: THE THREE MODES — KNOW WHICH LAYER YOU ARE IN

Every sentence you write falls into one of three modes. You must be aware of which mode
you are in at all times. Blurring the distinction *intentionally* is FID. Blurring it
*by accident* is just bad writing.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  MODE 1: PLAIN NARRATION                                                │
│  The author's neutral camera. No character voice bleeds in.             │
│  Sentence rhythm: even, consistent.                                     │
│                                                                         │
│  EXAMPLE:                                                               │
│  "Taro entered the hall. Kael was standing near the window."            │
├─────────────────────────────────────────────────────────────────────────┤
│  MODE 2: DIRECT THOUGHT (tagged)                                        │
│  Explicitly labeled as the character's voice.                           │
│  USE SPARINGLY — it is the least elegant option.                        │
│                                                                         │
│  EXAMPLE:                                                               │
│  Taro thought: This room has already been recalibrated.                 │
│  OR: He wondered if Kael had been here all night.                       │
├─────────────────────────────────────────────────────────────────────────┤
│  MODE 3: FREE INDIRECT DISCOURSE ← YOUR TARGET                         │
│  Third-person grammar, but the character's vocabulary and rhythm.       │
│  No tag. The voice announces itself through word choice alone.          │
│                                                                         │
│  EXAMPLE:                                                               │
│  "The room had already been recalibrated. Of course it had.             │
│  The man never just entered a space — he overwrote it."                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 3: THE KEEPING TIME THREE-LAYER STACK

*Keeping Time* has a unique narrative architecture. FID does not replace the other layers.
It occupies its own precise lane within them.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  LAYER 1 — THE SCORE (Objective Data)                                   │
│  What: The AR system's cold readout. Emotionless. Factual.              │
│  Format: > SYSTEM_TAG [Status]                                          │
│  Job: Reports WHAT IS TRUE.                                             │
│                                                                         │
│  LAYER 2 — FID PROSE (Taro's Interpretation)                            │
│  What: The narration, filtered through Taro's bias, humor, and fear.   │
│  Format: Normal prose sentences, Taro's vocabulary.                     │
│  Job: Reports WHAT TARO MAKES OF what is true.                         │
│                                                                         │
│  LAYER 3 — PLAIN NARRATION (Neutral Camera)                             │
│  What: World events, physical description, scene-setting.              │
│  Format: Clean, neutral, author's voice.                                │
│  Job: Reports THE WORLD without character bias.                         │
└──────────────────────────────────────────────────────────────────────────┘
```

**The tension between Layer 1 and Layer 2 is where Taro's character lives.**
The Score says one thing. Taro's FID voice accepts it, rejects it, or argues with it.
That gap IS his arc.

---

## SECTION 4: TARO'S FID VOCABULARY — THE AUTHORISED WORD LIST

When FID mode activates, Taro's voice bleeds into the narration.
You MUST draw from Taro's established vocabulary (ref: `03_CHARACTERS_REGISTRY.md`).
**Do NOT use generic narrator language during FID passages.**

### Taro's Approved Internal Vocabulary

| Category | Approved Terms | Banned Generic Equivalents |
|---|---|---|
| Cognitive state | buffer, filtering, dropping frames, out of phase, logging | confused, overwhelmed, distracted |
| Effort/fatigue | thermal load, CPU drain, running hot, capacity | tired, exhausted, struggling |
| Social difficulty | signal mismatch, out of sync, noise floor too high | awkward, uncomfortable |
| Suspicion/threat | high-confidence flag, pattern detected, doesn't add up | suspicious, worried |
| Self-criticism | glitch, patch failure, bad data | stupid, broken, wrong |
| Sarcasm/dry humor | (italics + flat delivery — see Section 6) | exclamation marks, never overt |

---

## SECTION 5: SENTENCE RHYTHM AS EMOTIONAL READOUT

In Taro's POV chapters, sentence rhythm is not stylistic — it is diagnostic.
The prose itself should function as an SNS monitor. Rhythm tells the reader Taro's
internal state before the Score tags confirm it.

### The Four Rhythm States

**STATE A — BASELINE / STABLE**
Long, flowing sentences. Measured pacing. Thoughts complete themselves.
Used in: quiet moments, post-resolution, low-surveillance scenes.

```
// EXAMPLE — Taro in a low-stimulation environment:
The workshop smelled like solder and something older underneath it —
dust or resin or the ghost of every sound that had ever been made here
and never quite left.
```

---

**STATE B — ELEVATED PROCESSING**
Medium sentences. Some fragments. Thoughts are complete but clipped.
Used in: social situations, mild threat, information overload beginning.

```
// EXAMPLE — Taro in a crowded hallway:
Fourteen sources in the corridor. He was filtering. It was fine.
Serah's voice was in there somewhere — fourth from the left, slightly
flat today, stress markers in the upper register.
Fine.
```

---

**STATE C — HIGH LOAD / OVERLOAD**
Short bursts. Fragments. Interruptions. Things cut off mid-
Used in: panic, fight, high-surveillance, close encounters with Voss/The Silence.

```
// EXAMPLE — Taro approaching overload:
Too many. There were too many signals.
The wall. The floor. Forty people breathing at forty different tempos.
He found his thigh with his fingers. Four-four time.
His rhythm. Not theirs.
```

---

**STATE D — THE REST (late arc only, Phase V)**
Sparse, spacious. Deliberate silence between thoughts. The prose breathes.
Used in: Taro's transformation, resolution scenes.

```
// EXAMPLE — Taro at peace:
He didn't filter anymore.

He listened to all of it.

The city was loud. That was all right.
```

---

## SECTION 6: TARO'S DRY SARCASM — THE FID IRONY RULE

Taro's character profile notes his "Stutter-Step" and fractured processing.
His sarcasm is FLAT. It does not announce itself. The irony lives in the gap
between what the Score reads and what Taro's narration delivers in response.

**Rule: Taro's sarcasm is delivered with the same deadpan rhythm as his factual
observations. No italics on the sarcastic word. No exclamation. Just the flat,
slightly-too-precise sentence that says everything.**

```
// WRONG — Announced sarcasm (do not do this):
The Score tagged it as THREAT_HIGH. *Perfect.* Just what he needed.

// CORRECT — Flat delivery, irony from rhythm and word choice alone:
> THREAT_ASSESSMENT: HIGH [Source: Unknown]
Wonderful. His first full day and the building was already trying to kill him.
He noted this as potentially significant.
```

---

## SECTION 7: FID APPLICATION BY NARRATIVE PHASE

The *amount* of FID shifts with Taro's arc. FID density is a signal of his psychological state.

### Phase I — THE IMPULSE (Chapters 1–3)
**FID Profile:** Reactive, self-critical, fragmented.
The narration stutters like Taro does. FID bursts are short and often cut off.
His vocabulary is mostly Glitch-Speak — he frames everything through his own failure.

**Target FID density:** Moderate. Use FID to show his self-blame and overwhelm.
Plain narration carries most of the scene-setting; FID erupts at crisis points.

```
// Chapter 2: The Assessment — Taro vs. Voss in the White Room
// This scene is where FID and The Score work in direct counterpoint.
// The Score tags Voss as INTENT: DECEPTIVE, but Taro's FID layer shows
// him trying to talk himself out of believing it.

> INTENT: DECEPTIVE [Confidence: 88%]

Eighty-eight. Not ninety. Not ninety-five.
Eighty-eight meant the Score wasn't sure.
Eighty-eight meant he could be wrong.
He held onto that number like it was a handhold.
```

---

### Phase II — PROPAGATION (Chapters 4–8)
**FID Profile:** Observational, dry, beginning to find footing.
Taro is processing a new environment. His FID voice becomes his field analysis tool.
He starts making observations about others — Hana, Ven, the Academy — with wry precision.

**Target FID density:** Higher. This is the phase where his voice is most distinctive.
Use FID to characterize every named NPC through Taro's specific lens.

```
// Chapter 4: Meeting Hana Chord
// Taro's FID reads Hana the way the Score would — but with his dry humour.

> WAVEFORM_SIGNATURE: SQUARE [Class: Alignment Conductor]
> NEURO_TYPE: HYPER-SYSTEMIZER

The Score was, for once, understating it.
She had asked him three questions in sequence, each dependent on the previous
answer, and was now waiting with the specific patience of someone who had
already calculated the four most likely responses he might give.
He gave her the fifth one anyway.
She blinked. The Score flagged it as a recalculation event.
He decided he liked her.
```

---

### Phase III — INTERFERENCE (Midpoint)
**FID Profile:** Breaking down. The flat irony starts cracking.
The "Safe Mode" filters drop. Taro's FID layer becomes unreliable — the sarcasm
thins out and what's underneath starts showing.

**Target FID density:** Very high, but fragmenting. FID bursts get shorter, more
panicked. The dry humour disappears. Pure rhythmic fragmentation.

```
// The Silence attack — FID under maximum stress:
> SIGNAL_LOSS // NULL // NULL

The Score had nothing.
The Score had — nothing.
He had been running on Score data for eight months and now the feed was
gone and the world was just — sound. Raw sound. No tags. No confidence
intervals. No clean lines.
Just the noise.
He had forgotten the noise was this loud.
```

---

### Phase IV — FEEDBACK LOOP (Crisis)
**FID Profile:** Unmasked. No more Glitch-Speak. The hardware metaphors fall away.
When Taro breaks past 100%, the FID layer should become strangely clear and simple.
The most vulnerable moments are written in the plainest language.

```
// Post-break — FID stripped bare:
His hands were shaking.
He didn't bother noting the frequency.
It didn't matter what frequency it was.
He was just shaking.
```

---

### Phase V — RESOLUTION
**FID Profile:** The Rest. Taro has become the silence between notes.
FID here is sparse and spacious. Sentences have room. The irony is gone — replaced
by something quieter and more certain.

```
// Resolution — FID as acceptance:
The Score was still running.
It always would be.
He let it.
```

---

## SECTION 8: CHARACTER-SPECIFIC FID RULES

When writing FID in Taro's POV for other characters, his internal read MUST be
filtered through his Glitch-Speak vocabulary. He reads people like he reads signals.

### Kael Unison (Voss) — Taro's FID Read
- Taro reads Kael as "the room that recalibrates itself."
- FID language: enforcement verbs. *Overwrote, corrected, smoothed, damped.*
- The Score's damping field is always physically present in Kael scenes.
- Taro's FID voice resents the enforced calm while acknowledging it works on him.

```
// TEMPLATE for Kael scenes:
[Score tag establishing the damping field]
[FID observation — Taro noting what the room is doing, not Kael directly]
[Physical response Taro can't stop — tapping slows, breathing steadies]
[FID reaction to his own involuntary compliance — dry, resentful]
```

### Hana Chord — Taro's FID Read
- Taro reads Hana as "a system he respects because it doesn't pretend to be something else."
- FID language: precision words. *Exact, calibrated, binary, no ambiguity.*
- He finds her literalism restful. This is expressed through what the FID voice DOESN'T say.
- When Hana does something unexpected, Taro's FID voice registers genuine recalculation.

```
// TEMPLATE for Hana scenes:
[Score tag confirming her waveform / Hyper-Systemizer status]
[FID observation — clinical but warm, noted precision]
[The thing she says/does that subverts his read]
[FID response — brief, a single line of recalibration, no elaboration]
```

### Serah Fifthstep — Taro's FID Read
- Taro reads Serah as "a signal he can't argue with because she's always moving."
- FID language: tempo words. *Momentum, beat, double-time, no drift.*
- He can't use his Stutter-Step around her because she doesn't slow down for it.
- FID passages in Serah scenes are shorter — she doesn't give him time to process.

---

## SECTION 9: THE SCORE / FID COUNTERPOINT — MASTER PATTERN

This is the central technique of the manuscript. Use it at every emotionally significant moment.

```
PATTERN:
  [Score tag — objective, clinical]
  [FID line — Taro's interpretation, using his vocabulary]
  [FID line — what he chooses to do with that information]
  [Plain narration — the physical action]

EXAMPLE:
  > INTENT: DECEPTIVE [Confidence: 88%]
  Eighty-eight percent. High enough to flag. Low enough to doubt.
  He chose to doubt it. He always chose to doubt it.
  He sat down across from Voss and kept his hands still.

VARIATION — Score contradicts Taro's FID read:
  He had decided the room was safe.
  > THREAT_ASSESSMENT: ELEVATED [Unknown Source]
  He revised that assessment.
```

---

## SECTION 10: THE HARD RULES — NEVER VIOLATE THESE

These are non-negotiable constraints for maintaining narrative integrity.

```
❌ RULE 1 — NO "HE THOUGHT" DURING FID
   If you've opened a FID passage, don't close it with a tag.
   The absence of the tag IS the technique.

   BAD:  "He thought the room felt wrong."
   GOOD: "The room was wrong. Obviously the room was wrong."

❌ RULE 2 — NO GENERIC VOCABULARY IN FID MODE
   Once FID activates, you are writing in Taro's lexicon.
   "Overwhelmed" becomes "thermal load." "Confused" becomes "buffer issue."

❌ RULE 3 — NO FID FOR OTHER CHARACTERS IN THEIR OWN SCENES
   When Taro POV chapters describe Hana, Kael, Serah — Taro's FID reads THEM.
   We never get direct access to their internal states from Taro's POV.
   The Score can tag their emotions. Taro's FID can speculate. That's all.

❌ RULE 4 — FID IS NOT EVERY SENTENCE
   Plain narration is the baseline. FID erupts. It does not run continuously.
   Ratio target: roughly 1 FID sentence per 3–4 plain narration sentences in
   normal scenes. In crisis scenes, this ratio inverts.

❌ RULE 5 — THE SCORE CANNOT BE WRONG ABOUT FACTS
   Taro's FID voice can choose to ignore, reframe, or argue with Score data.
   But the Score's factual readouts are always accurate.
   The drama is in the gap between what IS true and what Taro DOES with it.
```

---

## SECTION 11: SELF-CHECK BEFORE COMMITTING A PASSAGE

Run every FID passage through this checklist before finalising:

```
□ 1. Is there a "he thought / he felt" tag hiding in this passage?
      If yes → remove the tag and let the voice carry it.

□ 2. Is Taro's vocabulary present? (buffer, filtering, phase, signal, etc.)
      If no → you are in plain narration, not FID. That may be correct. Check intent.

□ 3. Does the sentence rhythm match Taro's current emotional state?
      (See Section 5 — The Four Rhythm States)
      If no → adjust sentence length to match his internal load.

□ 4. If there is a Score tag in this passage, does the FID respond to it?
      The Score / FID counterpoint should be active whenever both appear.

□ 5. Is the irony flat? (Sarcasm delivered deadpan, no announcement)
      If the joke is too obvious → strip the emphasis. The rhythm does the work.

□ 6. What Phase of the arc is this?
      Confirm the FID density and vocabulary match the arc stage (Section 7).
```

---

## SECTION 12: QUICK REFERENCE — THE TEMPLATE LIBRARY

Copy-paste starting templates for common scene types.

### A — First Entry Into New Space
```
[Plain narration: physical description, neutral]
> [Score tag: environmental readout]
[FID: Taro's assessment of the space using his vocabulary]
[FID: What the space signals to him about the people who built/occupy it]
[Plain narration: what he does next]
```

### B — Face-to-Face with an Authority Figure
```
[Plain narration: their physical presence]
> [Score tag: their intent/waveform/emotional state]
[FID: Taro noticing the Score's read and choosing whether to trust it]
[FID: His own involuntary physical response, named in Glitch-Speak]
[Dialogue — their words]
[FID: His internal reaction to their words, one flat sentence]
```

### C — Sensory Overload
```
[Plain narration: the stimulus]
[FID: Initial filter attempt, Glitch-Speak vocabulary]
[FID: Fragment. Fragment. Cut off—]
> [Score tag: OVERLOAD or DAMPING_FAILURE]
[FID: The physical coping mechanism — tapping, the beat, four-four time]
[Rhythm STATE C sentences — short, interrupted, then stabilising]
```

### D — A Moment of Quiet (Late Arc)
```
[Plain narration: the environment]
[FID: One simple observation. No hardware metaphors. Plain language.]
[White space — a beat of silence]
[Plain narration: what he does]
```

---

*Guide compiled for MiniMax 2.5 — Project: Keeping Time, Volume One.*
*Cross-reference: WRITER_GUIDE.md (Sensory Functionalism, Section 3) and*
*03_CHARACTERS_REGISTRY.md (Taro — Voice Guide) for all vocabulary decisions.*
