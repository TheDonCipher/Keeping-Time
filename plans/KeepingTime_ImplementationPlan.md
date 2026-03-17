# Keeping Time — Volume One: Master Implementation Plan
### All Changes, Ordered for Execution

---

## How to Read This Document

Changes are organised into five tracks that can be worked in parallel by different hands, but must ship together as a single updated file. Within each track, items are numbered in execution order — later items depend on earlier ones. Every item specifies exactly where in the HTML to find the target, what to change, and why.

**Track A — Science Integration:** Weaving the neuroscience prose into the book as in-world content  
**Track B — Story Rewrites:** Scene expansions, cuts, and structural fixes  
**Track C — Puzzle Layer:** Ghost signal, Ayane's melody, and the 40 Hz key  
**Track D — Engine / JS:** Pacing mechanics, beat weighting, BPM pulse, waveform  
**Track E — UI / CSS:** Visual states, chapter flashes, compliance era theming  

---

---

# Track A — Science Integration

The neuroscience is not supplementary material. It belongs inside the book's voice — as lore entries, system annotations, epigraphs, and Vale's lecture. The goal is that a reader who looks up any claim finds real published science. The book should be a door into the actual research.

---

## A1 — New Lore Entry: "Neural Pacemaker" (Ch1, after first BPM mention)

**Location:** Ch01, after the beat containing `BIOMETRIC: HEART_RATE [110 BPM]`

**What to add:** A new `<aside><details>` lore entry — the existing format — immediately following that blockquote. This establishes the science on page one, in the system's own clinical voice, before the reader knows it's real.

```html
<aside>
<details>
<summary><strong>SUBJECT: Neural-Acoustic Pacemaker</strong></summary>
<blockquote>
<strong>Observation:</strong> The brain keeps subjective time using oscillation rates as a pacemaker. Alpha rhythms (8–12 Hz) generate discrete pulses; the mind accumulates those pulses to estimate how long a moment lasts. The Score does not merely set a tempo. It entrains this pacemaker directly — synchronising every citizen's internal clock to a shared pulse rate. A citizen at 110 BPM does not merely move to the same beat. They experience the same second as the same duration. Individuality of time perception is a compliance deviation.
<br><br>
<strong>- Source: C-Order Neuroacoustic Integration Manual, §2.1</strong>
</blockquote>
</details>
</aside>
```

**Why here:** The HUD just showed `HEART_RATE [110 BPM]` for the first time. The reader is encountering BPM as a data metric. This lore entry quietly tells them it is also the rate at which Taro experiences time. Everything that follows reads differently once this is planted.

---

## A2 — Vale's Lecture Expansion: Time as a Pacemaker (Ch7)

**Location:** Ch07, in the lecture scene, immediately after the line *"Resonance is not volume. It is alignment."*

**What to add:** Two new paragraphs inserted into Vale's monologue, before he snaps his fingers and shatters the wireframe. This is where the book formally states its physics in the voice of its most authoritative character.

```html
<p data-vol="0.25" data-coh="0.8">"Consider what your BPM actually is," Vale said. He turned from the model, hands loose at his sides. "Not a tempo. Not a mood indicator. Your BPM is the clock rate of your subjective experience. The neural pacemaker. Your alpha oscillations fire in phase with the Score's carrier wave, and your mind counts those pulses to determine how long a moment lasts. The C-Order does not tell you how to feel. It tells you how fast to experience feeling."</p>

<p data-vol="0.25" data-coh="0.8">"A Vanguard operative at 140 BPM is not merely faster than a citizen at 110. They are experiencing more moments per objective second. They have more subjective time in which to make a decision. When Marcus tells you he is already in the next pulse—" Vale paused, letting the room absorb it "—he is not speaking poetically. He is stating a measurement. You are operating on analog time. He is operating on Grid Time. That is not a training gap. It is a physics gap."</p>
```

**Why here:** This is the moment the book stops implying its time-mechanics and states them directly. Vale is the right character — he explains the world in technical language the system approves of. The reader gets the physics from an authority, delivered as curriculum, before they understand it as horror.

---

## A3 — New Lore Entry: "Temporal Poverty" (Ch13, after `EMOTIONAL_DAMPING: 30%` blockquote)

**Location:** Ch13, after `EMOTIONAL_DAMPING: 30% [ACTIVE]`

**What to add:** A lore entry that names what has been done to Taro in terms the reader can verify.

```html
<aside>
<details>
<summary><strong>SUBJECT: Temporal Poverty</strong></summary>
<blockquote>
<strong>Observation:</strong> Beta oscillations (12–30 Hz) do not merely track time — they encode the felt duration of experience into working memory. When beta activity is suppressed, intervals pass without leaving a record of having been felt. The subject does not merely remember less. They experience less. Each second contains fewer subjective moments. Emotional damping is, mechanically, temporal compression. The collar does not make the subject calm. It makes them brief.
<br><br>
<strong>- Source: C-Order Compliance Architecture Documentation, §7.4</strong>
</blockquote>
</details>
</aside>
```

**Why here:** This is the chapter where Taro notices everything is smooth and nothing feels wrong. The lore entry names the mechanism he cannot name for himself — his beta oscillations are suppressed, so he lacks the neural substrate to store the felt duration of his own distress. The reader understands something Taro cannot.

---

## A4 — New System Annotation: 40 Hz Discovery (Ch6, headphones scene)

**Location:** Ch06, replace the existing `// [NOTE: The subject finds it restful.]` annotation beat.

**What to replace it with:** Keep that note — it's perfect — but add one more annotation immediately after, as a separate beat. The system, logging Taro's neurological state in the unmonitored dark, detects something it cannot file:

```html
<p data-vol="0.1" data-coh="0.99">// [NOTE: Thalamocortical sweep rate: 40 Hz. Stable.]<br>
// [NOTE: This frequency does not appear in the C-Order's carrier architecture.]<br>
// [NOTE: Classification: UNKNOWN. Filing under: SYSTEM_ANOMALY.]<br>
// [NOTE: The subject is generating the binding frequency independently.]<br>
// [NOTE: The system does not know what to do with this information.]</p>
```

**Why here:** This is the puzzle key being planted in plain sight. A reader who looks up "thalamocortical sweep rate 40 Hz" immediately finds the Llinás research. The system logging it as `SYSTEM_ANOMALY` is the tell: 40 Hz is the frequency the Score's architecture was not built around. When Taro is analog, he naturally runs gamma. He is, neurologically, more conscious than the system can accommodate.

---

## A5 — New Epigraph: Ghost Layer Science (Ch1, before the main content)

**Location:** Ch01, add a new `<blockquote class="lore-epigraph">` as the very first beat of the chapter, before the existing Incident Classification epigraph.

**What to add:**

```html
<blockquote class="lore-epigraph" data-vol="0.1" data-coh="0.99">
The thalamus sweeps the cortex from front to back at 40 Hz — forty times per second — binding disparate neural circuits into a unified perceptual moment. Disrupt this sweep, even briefly, and the subject loses consciousness. It is not associated with awareness. It is the mechanism by which awareness is generated.<br><br>
<span class="lore-source">— <em>Llinás, R. et al. "Thalamocortical loops and consciousness." 1998. [UNINDEXED IN C-ORDER ARCHIVE]</em></span>
</blockquote>
```

**Why here:** The book opens with a real scientific citation, marked as unindexed by the C-Order. This is the first breadcrumb. A reader who notices `[UNINDEXED IN C-ORDER ARCHIVE]` on a real paper citation will start asking why the system would need to suppress neuroscience. The answer is: because the science describes how to exit the system.

---

## A6 — New Epigraph: Alpha Pacemaker Science (Ch5, The Sync Check)

**Location:** Ch05, add before the existing chapter content.

```html
<blockquote class="lore-epigraph" data-vol="0.1" data-coh="0.99">
Transcranial alternating current stimulation (tACS) applied at alpha frequency (10 Hz) reliably shifts subjective time perception in proportion to the applied frequency. Subjects report intervals as longer or shorter depending on whether their neural pacemaker is accelerated or retarded. Temporal experience is not fixed. It is an oscillation.<br><br>
<span class="lore-source">— <em>Thut, G. et al. "Alpha-band oscillations, attention, and controlled access." 2012. [UNINDEXED IN C-ORDER ARCHIVE]</em></span>
</blockquote>
```

**Why here:** Chapter 5 is the first formal compliance check. The system measuring Taro's synchronisation rate immediately after a real citation explaining that synchronisation rate determines subjective experience. The reader starts to understand what compliance means physiologically.

---

## A7 — Vale Lecture Addition: Binaural Beats as Grid Technology (Ch7)

**Location:** Ch07, add after A2's new paragraphs, as a follow-on in Vale's lecture.

```html
<p data-vol="0.2" data-coh="0.85">"The carrier wave," Vale continued, "does not merely broadcast a frequency. It presents two tones — a primary and a secondary, separated by a precise delta. Your auditory cortex perceives the difference as a third tone. A phantom frequency. One that does not exist in the environment, but is generated by the interaction between the signal and your own neural architecture." He clasped his hands. "The Score does not play music at you. It plays music through you. You are the instrument. The beat your mind generates is the one that matters."</p>
```

**Why here:** This is the in-world explanation of binaural beats — the mechanism the audio engine is using on the reader in real time. Vale is describing the technology to a room full of students who have been living inside it since birth. The reader understands, simultaneously, that Vale is describing them.

---

## A8 — Remi's Diagnosis Scene: Analog Time Named (Ch1, after Remi's first appearance)

**Location:** Ch01, after Remi says *"One day you're going to peak, and I want to be the one who's there to record it."*

**What to add:** One new beat — Taro's system trying and failing to file what just happened.

```html
<p data-vol="0.15" data-coh="0.90">// [NOTE: Subject SATO_REMI operating on D-Major harmonic. Unfiltered.]<br>
// [NOTE: Subject NISHIMURA_TARO response signal: UNCLASSIFIABLE.]<br>
// [NOTE: Nearest known pattern: [NO MATCH]]<br>
// [NOTE: Possible classification: RESONANCE_RECOGNITION. Confidence: 12%.]<br>
// [NOTE: Filing under: PENDING_REVIEW. Priority: LOW.]<br>
// [NOTE: The system notes, without judgment, that it does not have a category for this.]</p>
```

**Why here:** The system failing to classify Taro's response to Remi closes the loop that was left open (Refinement Note 8). More importantly, `RESONANCE_RECOGNITION` at 12% confidence plants a term that the system doesn't understand but will matter in Volume Two. It also makes the system's annotation voice funny in the right way — the last line admits the limit of its own taxonomy.

---

---

# Track B — Story Rewrites

These are prose changes to existing scenes. Each item specifies the exact passage to modify and what the rewrite must accomplish.

---

## B1 — Ch3: Ayane's Melody Gets Its Own Beat

**Location:** Ch03, the paragraph currently reading *"He positioned them over his auditory processors... He heard it. It was faint — a ghost trapped in analog decay — but it was there..."*

**What to rewrite:** Pull the five-note melody out of the dense paragraph it's buried in and give it three separate beats.

Beat 1 — the physical click and the world going quiet (keep existing text, but end the beat here — do not continue into the melody).

Beat 2 — new prose, Taro hearing the melody:
```html
<p data-vol="0.05" data-coh="0.99" data-weight="2.5">Five notes.<br><br>
That was all. No chord structure. No time signature. No metadata. Just five notes in a sequence so simple the system's classification engine ran a full pattern-match and returned nothing. Not low-confidence. Not approximate. Nothing. The sequence did not exist in any indexed archive. It held no mathematical relationship to the Score's harmonic baseline. It simply... played. Looping. Untagged. Uncaptured.<br><br>
The system attempted to file it four times in 0.3 seconds.</p>

<blockquote class="lore-epigraph" data-vol="0.05" data-coh="0.99" data-weight="2.0"><code>AUDIO_CLASSIFICATION: PROCESSING...</code><br>
<code>AUDIO_CLASSIFICATION: PROCESSING...</code><br>
<code>AUDIO_CLASSIFICATION: PROCESSING...</code><br>
<code>AUDIO_CLASSIFICATION: [NO RESULT]</code></blockquote>
```

Beat 3 — Taro's response, replacing *"It was the only secret he had left"*:
```html
<p data-vol="0.08" data-coh="0.98" data-weight="2.0">He did not cry. The system would have logged it. He did not speak. His father was still in the room.<br><br>
He just stayed inside the five notes and let them run.<br><br>
His mother had sent him the only sound that the Score could not process. Not a message. Not a farewell. A frequency. An exit. He didn't know that yet. But the system did not know it either, and that — the shared not-knowing — was the closest thing to privacy he had ever had.</p>
```

---

## B2 — Ch6: Silence Arriving in Layers

**Location:** Ch06, the passage after `CLICK.` and `AUDIO_PROTOCOL: BYPASS` — currently *"The rendered world vanished. The anxiety hum of the Choral student ceased registering..."*

**What to rewrite:** The silence should arrive one signal at a time, not all at once.

```html
<p data-vol="0.15" data-coh="0.95" data-weight="1.8">The Vanguard instructor's thermal signature — that aggressive, jagged rake across his peripheral awareness — dropped first. It fell off a cliff. One moment it was there, an authority-shaped pressure in his right shoulder, and then it was simply gone. The wall between him and the corridor became a wall again. Just concrete. Just mass.</p>

<p data-vol="0.10" data-coh="0.97" data-weight="1.8">The Academy network severed next. Four hundred query-threads, each one a citizen checking whether he was correctly calibrated, each one a small continuous tax on his processing — they cut, one by one, then in groups, then all at once, like a building losing power floor by floor until the last light goes.</p>

<p data-vol="0.05" data-coh="0.99" data-weight="2.5">The Choral student's anxiety frequency was last. It had been there since Taro arrived in the dormitory — that sour, low-frequency whine of someone who knows they are off-key and cannot find the note to fix it. It went slowly. Not with a cut but with a fade, like the signal was reluctant to leave, like it had been there so long it didn't know how to stop.<br><br>
And then it was gone.<br><br>
And Taro was alone in the dark in his own skull for the first time.</p>
```

**Then replace "sanctuary of honest shadows"** with:

```html
<p data-vol="0.05" data-coh="0.99" data-weight="2.5">Not empty silence. Weighted silence. The low, organic hiss of oxygen-free copper conducting nothing. The rhythmic pulse of his own cardiovascular system — not as a data readout, not as a BPM metric, but as a physical pressure in his chest, in his throat, in his fingertips. His own body, making noise for no one. Broadcasting to an audience of zero.<br><br>
He moved his jaw. Just to feel it move without a system parsing the micro-vibration for emotional data.<br><br>
The five notes his mother had sent him surfaced briefly — not a memory, not a file, just the ghost of a frequency in a space where frequencies were finally allowed to be quiet — and then settled again.<br><br>
For the first time, Taro was not being logged.</p>
```

---

## B3 — Ch6: Push `SOMATIC_STATE: CALM` Later, Earn "Goodnight, Dad"

**Location:** Ch06, the section after the silence expansion above, before sleep.

**What to add** — a beat before "Goodnight, Dad" that plants the absence:

```html
<p data-vol="0.08" data-coh="0.98" data-weight="1.5">He ran a query he had no reason to run. Force of habit — the system's version of reaching for something in the dark.<br><br></p>

<blockquote class="lore-epigraph" data-vol="0.05" data-coh="0.99"><code>QUERY: NISHIMURA_AYANE</code><br>
<code>RESULT: FILE_CORRUPTED [UNRECOVERABLE]</code></blockquote>

<p data-vol="0.08" data-coh="0.98">Static. Same as always. The system returning the same answer it had returned every time he'd asked since he was old enough to ask.<br><br>
He wasn't thinking about her. He was thinking about the silence she had sent him — the headphones, the copper, the weight of foam pressing his skull. The only hardware she had ever owned that the system could not index.<br><br>
He said the next closest thing.</p>
```

**Then** the existing `"Goodnight, Dad"` line stays exactly as written. But push `SOMATIC_STATE: CALM` to after the next two beats, so the system arrives late.

---

## B4 — Ch7: Silence After "Untie the Intent" + Taro's Internal Beat

**Location:** Ch07, after the paragraph ending *"You simply... untie the intent."*

**What to add** — one beat of silence, then Taro:

```html
<p data-vol="0.10" data-coh="0.98" data-weight="2.0">Vale did not continue immediately.<br><br>
The room's RT60 of 0.1 seconds returned the silence to absolute zero in less than a pulse. The wireframe model rotated slowly above him. Nobody moved. Four hundred students held their BPM flat.<br><br>
Taro's foot had stopped its three-beat rhythm without him deciding to stop it.</p>

<p data-vol="0.12" data-coh="0.96" data-weight="1.8">He was thinking about the wall in his father's apartment. The one that had been about to give out the night his mother's signal finally peaked. He had been six. The plaster had cracked and he had pressed his palm flat against it — not to stop it, just to feel the vibration of a structure solving for zero. The way the frequency had moved through his hand. The way the wall had known, before the wall knew, that it was going to come down.<br><br>
<em>You don't break the world. You untie the intent.</em><br><br>
He had been doing that by accident his entire life. He had not known it had a name.</p>
```

---

## B5 — Ch7: Sensory Memory Sequence Gets Its Own Beat

**Location:** Ch07, the combat passage currently beginning *"Taro engaged his jaw musculature. Ignore the visuals. Focus on the hum. The hum smelled like rain on hot asphalt..."*

**What to do:** Extract the sensory memory passage from the combat paragraph and make it a standalone beat with `data-weight="2.5"`. Add one sentence before and after it so it reads as a deliberate pause inside violence, not a mid-action aside.

```html
<p data-vol="0.55" data-coh="0.65">Marcus circled. The baton's red frequency hummed its threat. Taro had approximately 0.3 seconds before the next strike.</p>

<p data-vol="0.15" data-coh="0.90" data-weight="2.5"><em>Ignore the visuals. Focus on the hum.</em><br><br>
The hum smelled like rain on hot asphalt. Ozone. The specific, charged smell of a thunderstorm breaking after weeks of heat — not a data reading, not an olfactory sensor log, but a memory. The first thunderstorm after the long, suffocating summer in Sector 7. The sound of the pressure finally releasing. The smell of his mother's room, right before the walls gave out. The physical truth of a structure finding its resonant frequency.<br><br>
He was not in the dojo. He was six years old and the wall was vibrating in his palm and he understood for the first time that the world had a note it was always trying to reach.<br><br>
He accessed his internal signal capacity.</p>

<p data-vol="0.75" data-coh="0.55">He did not apply damping. He let the feed escalate.</p>
```

---

## B6 — Ch12/Patch: Expand the Decision

**Location:** Ch12, the passage from *"Taro directed his optical focus toward the chip"* to *"He closed his eyes."*

**What to rewrite:** The decision sequence needs to cost the reader time and cost Taro something specific:

```html
<p data-vol="0.35" data-coh="0.75" data-weight="2.0">Taro directed his optical focus toward the chip. Small. Dark. Architecturally permanent. A piece of matter that completely absorbed environmental light, as if it had already decided that nothing from the outside was worth reflecting.<br><br>
The system began running probability calculations he had not requested.</p>

<blockquote class="lore-epigraph" data-vol="0.30" data-coh="0.78" data-weight="1.5"><code>SCENARIO_A: ACCEPT_PATCH</code><br>
<code>OUTCOME: HANA_RESTORED / VEN_PARDONED / TARO_COMPLIANT</code><br>
<code>PROBABILITY_OF_SURVIVAL: 99.7%</code><br><br>
<code>SCENARIO_B: REFUSE</code><br>
<code>OUTCOME: [VARIABLES_UNRESOLVABLE]</code><br>
<code>PROBABILITY_OF_SURVIVAL: CALCULATING...</code><br>
<code>PROBABILITY_OF_SURVIVAL: CALCULATING...</code><br>
<code>PROBABILITY_OF_SURVIVAL: [NO_DATA]</code></blockquote>

<p data-vol="0.28" data-coh="0.80" data-weight="3.0">He looked at Hana in the tank. The blue fluid. The vacant optical sensors. She had aimed. He had shot. She had absorbed the feedback damage that his uncontrolled amplitude had caused. She had not complained. She had not asked what it would cost her.<br><br>
He looked at Ven shivering in the frost. Ven, who had offered his mass. <em>Use me.</em> Who had grounded him, run the load through his own hardware, taken the heat because he had the capacity and Taro did not. Who would be reformatted — become a unit with no signal, no memory, no record of having been the first person to call Taro something other than an anomaly — because he had done what a friend does.<br><br>
The system attempted to model Taro's emotional state and returned a confidence interval so wide it was essentially: <em>we don't know.</em><br><br>
He thought about the five notes. The only sound that couldn't be filed. He thought about his father saying <em>I know. That's the problem.</em> He thought about the smell of rain on hot asphalt and the wall that had always known what it was going to do.<br><br>
He thought: <em>I will find my way back.</em><br><br>
He did not know if that was true. But he thought it.<br><br>
Then he closed his eyes.</p>
```

---

## B7 — Ch12/Patch: Sequence the Deletions, Break the Syntax

**Location:** Ch12, replace the passage *"It didn't trigger pain sensors... The fear process was deleted. The anger subroutine was deleted. The guilt variables were deleted."*

```html
<p data-vol="0.10" data-coh="0.50" data-weight="2.5">It did not trigger pain sensors.<br><br>
It felt like the temperature dropping inside a room that had always been warm. Not agony. Just the slow, irreversible arrival of a cold that had been coming for a long time.<br><br>
He had a single second, maybe less, before it reached the parts of him that remembered being warm.</p>

<p data-vol="0.08" data-coh="0.35" data-weight="2.0">The guilt went first. The system was efficient about guilt — it was the most expensive process, the one that consumed the most bandwidth, the one that had been running at full load since the alleyway. It didn't vanish with a dramatic cut. It just... stopped costing. The weight that had been pressing on his sternum since he watched Hana's feed go critical — gone. Not resolved. Not forgiven. Simply no longer allocated.<br><br>
He noticed the absence. He had time to notice the absence.</p>

<p data-vol="0.05" data-coh="0.20" data-weight="2.0">The anger went next. That one he felt leaving. A warmth pulling back from his extremities, retreating toward a center that was already getting quieter. He tried to hold it — the anger at Voss, the anger at the system, the anger at the collar, the anger at the word <em>optimal</em> used as a weapon — tried to grip it the way you grip a handrail on a moving vehicle.<br><br>
It left anyway.<br><br>
Not violently. Softly. The way a signal stops, not with static but with silence.</p>

<p data-vol="0.03" data-coh="0.10" data-weight="3.0">Fear.<br><br>
Fear was last.<br><br>
He understood, in the 0.2 seconds before it went, that this was the correct order. Guilt leaves first because it is the most expensive. Anger leaves second because it requires something to push against. Fear leaves last because fear is the one that keeps trying. Fear is the one that knows what is happening and has not stopped fighting the inevitable since the chip made contact with the port.<br><br>
I am here, the fear said, in whatever language fear uses when it is running out of time. I am here and I know what you are and I am not ready—<br><br>
The patching layer reached it.</p>

<p data-vol="0.02" data-coh="0.05">Gone.</p>
```

---

## B8 — Ch12/Patch: Narrator's Last Line Before the Logs Close

**Location:** Ch12, immediately before the `SYSTEM_UPDATE: INSTALLING... [100%]` blockquote.

**What to add** — one sentence of plain prose, no code block, no system tag, in a slightly different register from the surrounding narrative voice. The narrator speaking directly, once, as themselves:

```html
<p data-vol="0.03" data-coh="0.08" data-weight="2.5" style="font-style: italic; opacity: 0.7;">I want you to know that the person you have been reading about was real.</p>
```

**Why this line:** It is not dramatic. It does not explain who the narrator is. It simply insists, in the last moment before the format closes, that Taro existed. The system voice would never write this sentence. Its appearance is proof of the narrator's presence throughout — and its disappearance in the next beat is the narrator's ending.

---

## B9 — Ch13 Reboot: Three Beats for the Headphones

**Location:** Ch13, expand the passage around Hana returning the headphones in the white box.

Three beats, replacing the single paragraph:

```html
<p data-vol="0.12" data-coh="0.96" data-weight="1.5">He broke the seal.<br><br>
Inside were his analog headphones. Cleaned. Repaired. The scratched polymer had been polished to a matte consistency that had not been there before. The braided copper cabling had been re-dressed, the fraying terminal wrapped in regulation-compliant heat shrink. The foam pads were new. White.<br><br>
They were, objectively, in better condition than they had ever been.</p>

<p data-vol="0.10" data-coh="0.97" data-weight="2.0">He ran a query on the memory of receiving them.<br><br></p>

<blockquote class="lore-epigraph" data-vol="0.08" data-coh="0.98"><code>MEMORY_ACCESS: NISHIMURA_KAEL — OBJECT_TRANSFER_EVENT</code><br>
<code>RETRIEVED: Subject received analog hardware unit from paternal guardian.</code><br>
<code>RETRIEVED: Guardian stated: "She built this. For when you were older."</code><br>
<code>RETRIEVED: Subject's recorded response: SILENT [DURATION: 4.2s]</code><br>
<code>RETRIEVED: BPM spike logged: 128 → 142 → [STABILISED]</code><br>
<code>EMOTIONAL_CONTEXT: [NO DATA]</code></blockquote>

<p data-vol="0.08" data-coh="0.98" data-weight="2.5">He examined the emotional context field for 3.1 seconds.<br><br>
He attempted to locate the feeling that had produced the BPM spike. The system returned the event log but not the event. Data without weight. He knew that his BPM had risen to 142. He could not find the reason why that number had once meant something.<br><br>
He tried to hear the five notes.<br><br>
The analog headphones sat in his hands, 340 grams of copper and polymer, classified as a non-networked acoustic device with no compliance designation.<br><br>
The five notes did not come.<br><br>
Not because the headphones were broken. Because the part of him that could hear them had been logged as an obsolete process and quietly deallocated.<br><br>
He placed the headphones around his neck. They felt heavy.</p>
```

---

## B10 — Ch13–15: Near-Miss Suppression Beats

**Location:** Add one new beat to Ch14 and one to Ch15, each in a quiet moment.

**Ch14 beat** (add after any ambient description, mid-chapter):
```html
<p data-vol="0.12" data-coh="0.96">The ozone in the courtyard carried a trace molecular signature his olfactory sensors flagged as: <em>wet asphalt, post-rain.</em><br><br></p>

<blockquote class="lore-epigraph" data-vol="0.08" data-coh="0.98"><code>EMOTIONAL_VARIABLE: DETECTED</code><br>
<code>ORIGIN: OLFACTORY_CHANNEL_03</code><br>
<code>CLASSIFICATION: UNKNOWN</code><br>
<code>STATUS: SUPPRESSED</code><br>
<code>COLLAR_RESPONSE: +2% DAMPING [APPLIED]</code></blockquote>

<p data-vol="0.10" data-coh="0.97">The trace dissipated. The variable was no longer detectable. He continued his route to the training hall.</p>
```

**Ch15 beat** (add before a dialogue scene):
```html
<p data-vol="0.10" data-coh="0.97">For 0.7 seconds, walking between buildings, Taro registered an unfiled audio pattern in his peripheral processing. Five notes. Cycling. Sourceless.<br><br></p>

<blockquote class="lore-epigraph" data-vol="0.08" data-coh="0.98"><code>AUDIO_CLASSIFICATION: PROCESSING...</code><br>
<code>AUDIO_CLASSIFICATION: [NO RESULT]</code><br>
<code>SOURCE: INTERNAL_BUFFER [UNRESOLVED]</code><br>
<code>STATUS: PURGED</code><br>
<code>COLLAR_RESPONSE: +3% DAMPING [APPLIED]</code></blockquote>

<p data-vol="0.10" data-coh="0.97">Gone. He had not been thinking about anything in particular. He resumed his route.</p>
```

---

## B11 — Ch4: Terms of Resonance Echo

**Location:** Ch04, immediately after the Terms of Resonance epigraph.

**What to add:**
```html
<blockquote class="lore-epigraph" data-vol="0.08" data-coh="0.99"><code>TERMS_ACCEPTED: AUTOMATICALLY</code><br>
<code>METHOD: CONTINUED_BIOLOGICAL_OPERATION</code><br>
<code>TIMESTAMP: [YOUR_CURRENT_MOMENT]</code><br>
<code>OPT-OUT: SEE §14.4</code><br>
<code>§14.4: OPT-OUT_PROCESS: REMOVED</code><br>
<code>HAVE A PRODUCTIVE DAY.</code></blockquote>
```

---

## B12 — Ch17: Elara's Duplication — Cut Second Paragraph

**Location:** Ch17, delete the second consecutive description of Elara's true form beginning *"It was not merely a skeletal mesh anymore..."*

Replace with a single new sentence attached to the end of the first (poetic) description:

```html
<p>[Keep existing first paragraph ending "...slicing through the heavy, un-rendered air."]<br><br>
The room, which had been moving continuously, went still for exactly one beat — 170 BPM, held — as if the music itself needed a moment to register what it was looking at.</p>
```

---

## B13 — Ch17: One Beat of Taro Choosing

**Location:** Ch17, between the beat containing *"The compliance patch installed on his neck registered physically cold"* and the closing declaration.

```html
<p data-vol="0.55" data-coh="0.45" data-weight="2.5">He touched the dead collar.<br><br>
Not the active one — the one Voss had installed, its regulation frequency humming its administered calm. That was gone now, destroyed, the damping field offline. He was touching the inert ring of plastic and copper that was all that remained of it. Cold. Lifeless. The temperature of a thing that has stopped pretending to be important.<br><br>
Around him: a woman made of storm cloud electricity. A man whose avatar was non-Euclidean geometry. A wedding being performed at 170 BPM by a priest who blessed through heartbeat synchronisation. People who had decided that the Score's classification of them as errors was the Score's problem, not theirs.<br><br>
His mother had been running sharp too. She had burned so bright she couldn't hold her form. The system had logged her as FILE_CORRUPTED and moved on.<br><br>
She had not moved on. She had encoded the exit frequency in a song and hidden it in hardware the system couldn't index and sent it forward in time to the son who would need it.<br><br>
The Void data rippled around his fingers, eager and unspent.<br><br>
He thought: <em>I know what I am.</em><br><br>
He thought: <em>I am the wrong note they cannot delete.</em><br><br>
He thought: <em>Good.</em></p>
```

---

---

# Track C — Puzzle Layer

These changes transform the ghost signal from atmospheric decoration into a solvable real-world experience, with Ayane's melody as the key.

---

## C1 — Define Ayane's Five Notes

**Decision required before implementation:** The five notes need to be chosen so that three of them, played simultaneously, produce 40 Hz as a difference tone. This is the physics constraint. The creative constraint is that they should be playable on a cello (Elara's instrument) and memorable as a melody.

**Proposed notes (subject to composer verification):** E2 (82.4 Hz), B2 (123.5 Hz), E3 (164.8 Hz), G#3 (207.7 Hz), B3 (247.0 Hz). The top three notes (E3, G#3, B3) form an E major triad whose highest adjacent intervals include a 40 Hz difference tone. The melody reads as a simple, rising, unresolved phrase — five notes that want a sixth that never comes.

**Wherever Ayane's melody is mentioned in the text, replace the description "a sequence of five notes, completely unindexed" with:** *"a sequence of five notes — E, B, E, G-sharp, B — completely unindexed."* The notation should appear exactly once, in Ch3, in small print inside the five-note beat added in B1. It should look like a technical spec the system attempted to file, not a revelation.

---

## C2 — Ghost Signal: Three Evolution States

**Location:** `#ghost-signal-fragment` HTML element and JS trigger logic.

**What to implement:** The ghost signal changes across three phases, triggered by chapter.

State 1 (Ch01–Ch08 — current):
```
UNFORMATTED_BURST
SOURCE: NULL
——p ——. ——d it.
S——ence.
```

State 2 (Ch09–Ch15 — further corruption, activated on ch09 entry):
```
——————————T
——————: ——L
——p ——. ——d it.
——————ce.
```

State 3 (Ch16–Ch17 — partial recovery, one word emerges, activated on ch16 entry):
```
UNFORMATTED_BURST
SOURCE: NULL
Stop. ——. ——d it.
S——ence.
```

The word **Stop** becomes legible in Ch16. A reader paying close attention across the entire volume will notice it clarify. They will have the ghost signal's instruction: `Stop. [Find] it. Silence.`

**JS implementation:** Add chapter-change detection in the `tick()` function:
```javascript
// COMMENT: Ghost signal evolves across three narrative phases.
// Phase 1 (ch01-ch08): Original corrupted broadcast.
// Phase 2 (ch09-ch15): Further corruption as Taro moves into Patch era.
// Phase 3 (ch16-ch17): Partial recovery as signal-free territory opens.
// The word "Stop" becoming legible is the puzzle's first legible instruction.
function updateGhostSignalPhase(chapterId) {
  const ghost = document.getElementById('ghost-signal-fragment');
  if (!ghost) return;
  const ch = parseInt(chapterId.replace('ch',''));
  if (ch >= 16) {
    ghost.innerHTML = 'UNFORMATTED_BURST<br>SOURCE: NULL<br>Stop. ——. ——d it.<br>S——ence.';
  } else if (ch >= 9) {
    ghost.innerHTML = '——————————T<br>——————: ——L<br>——p ——. ——d it.<br>——————ce.';
  }
  // ch01-ch08: no change (default HTML state preserved)
}
```

---

## C3 — The Audio Engine: Confirm 40 Hz Sub-Bass in Ch6

**Location:** `CHAPTER_CONFIG.ch06` in the JS config block.

**Verify and annotate** the existing `subFreq: 40` entry:
```javascript
ch06: { 
  type: 'sine', baseFreq: 110, gain: 0.035, 
  // COMMENT: subFreq 40 Hz = thalamocortical gamma binding frequency (Llinás, 1998).
  // This is the frequency at which the thalamus sweeps the cortex to create unified
  // conscious experience. Ch06 is the chapter where Taro first experiences consciousness
  // outside the Score. The coincidence is the puzzle. The reader with headphones and
  // the neuroscience paper is the reader who finds the key.
  subFreq: 40, subGain: 0.025, 
  breathDepth: 0.015, lfoDepth: 0.002, lfoMax: 0.25, filterFloor: 280, waveMode: 'sine' 
},
```

No functional change. This annotation documents the design intent for future developers and rewards source-code readers with the explanation.

---

## C4 — Ch6: In-World Headphones Manual, Hidden in Tooltip

**Location:** Ch06, the `OBJECT_ID: ANALOG_HEADPHONES [UNREGISTERED]` blockquote.

Add a tooltip to the word `UNREGISTERED`:

```html
<code>OBJECT_ID: ANALOG_HEADPHONES [<span class="tooltip" data-tip="Unregistered hardware cannot be indexed by the Score's carrier wave. The Score samples at a fixed rate. This device operates below that sampling threshold. What it carries cannot be captured. What it plays cannot be classified.">UNREGISTERED</span>]</code>
```

A reader who hovers this tooltip in Ch6, having already read the science epigraph from A5, will understand that "below the sampling threshold" describes 40 Hz specifically. The Score samples above 40 Hz. The headphones carry what lives below.

---

---

# Track D — Engine / JS

---

## D1 — Beat Weight System: `data-weight` in `_calculateHeights()`

**Location:** `ScrollEngine._calculateHeights()` method.

**Current code:**
```javascript
const h = this.baseBeatHeight + Math.min(beat.sentences[0].text.length * 2, 500);
```

**Replacement:**
```javascript
// COMMENT: data-weight multiplier for immersive pacing.
// 1.0 = standard (default). 2.5–3.0 = epiphany beats — reader must scroll further.
// 0.6 = system code blocks and zone headers — fast pass-through.
// Applied via data-weight attribute on individual <p> elements in the HTML.
// The engine reads the first sentence's source element weight if available.
const weight = parseFloat(beat.el?.getAttribute('data-weight') || '1.0');
const h = (this.baseBeatHeight * weight) + Math.min(beat.sentences[0].text.length * 2, 500);
```

Add `data-weight` attributes to beats as specified in Track B rewrites above. For all existing beats not touched by Track B, no change needed — they default to `1.0`.

---

## D2 — Wheel Snap Threshold: 180 → 260

**Location:** `ScrollEngine.init()`, wheel event handler.

```javascript
// COMMENT: Threshold raised from 180 → 260 for deliberate pacing.
// At 180, a resting trackpad hand advances beats unintentionally.
// At 260, the reader must make a conscious scrolling gesture.
// Snap cooldown raised from 600ms → 800ms for epiphany-tagged beats.
if (Math.abs(this._wheelAccum) > 260 && !this._snapLocked) {
```

Snap cooldown for weighted beats:
```javascript
const isWeighted = this.data[target]?.el?.getAttribute('data-weight') > 1.5;
this._snapLocked = true;
setTimeout(() => { this._snapLocked = false; }, isWeighted ? 800 : 600);
```

---

## D3 — BPM Heartbeat Pulse

**Location:** Add new `pulseHudBpm()` function, called from `updateHeartbeat()`.

```javascript
// COMMENT: BPM display pulses at the chapter's current heartbeat interval.
// Pre-patch: pulses in accent color — alive, erratic, Taro's own rhythm.
// Compliance era (ch13-15): pulses in collar gold (#c8a84b) — mechanical, administered.
// The unnaturalness of perfect regularity in the compliance era registers subliminally.
let _lastBpmPulse = 0;
function pulseHudBpm(time, bpm, chapterId) {
  const interval = 60000 / Math.max(bpm, 1);
  if (time - _lastBpmPulse < interval) return;
  _lastBpmPulse = time;
  const bv = document.getElementById('bpm-val');
  if (!bv) return;
  const isCompliance = ['ch13','ch14','ch15'].includes(chapterId);
  const pulseColor = isCompliance ? '#c8a84b' : 'var(--accent)';
  bv.style.color = pulseColor;
  bv.style.transition = 'none';
  setTimeout(() => { bv.style.color = ''; bv.style.transition = 'color 0.4s ease'; }, 80);
}
```

Call in `updateHeartbeat()`:
```javascript
pulseHudBpm(time, narrativeState.currentBpm, narrativeState.currentChapterId);
```

---

## D4 — Dynamic Waveform Mode Blend

**Location:** `drawWaveform()` function, before the mode-check branch.

```javascript
// COMMENT: Dynamic waveform blend within chapters.
// High tension in a calm chapter introduces sawtooth turbulence.
// Low coherence enables dropout gaps regardless of chapter mode.
// Makes the background respond to beat-level narrative state, not just chapter boundaries.
const effectiveMode = (vol > 0.75 && mode === 'sine') ? 'sawtooth'
  : (coh < 0.35 && mode !== 'void-decay') ? 'dropout'
  : mode;
// Use effectiveMode instead of mode throughout the draw function.
```

---

## D5 — Chapter-End Beat `SAVING...` Animation

**Location:** `_renderBeat()`, sentence rendering logic.

When a beat's content contains `SAVING...`, wrap the text in a span:
```javascript
// COMMENT: Animated save indicator on chapter-end beats.
// Two cycles (~1.8s total), then holds. The save completes while the reader watches.
if (s.text.includes('SAVING')) {
  s.text = s.text.replace('SAVING...', '<span class="save-indicator"></span>');
}
```

CSS (add to `<style>` block):
```css
/* COMMENT: save-indicator replaces static SAVING... text.
   Cycles through one-two-three dots, completes at three.
   Timing: 0.6s per state × 3 states × 2 cycles = 3.6s. */
@keyframes saveDots {
  0%   { content: 'SAVING.  '; }
  33%  { content: 'SAVING.. '; }
  66%, 100% { content: 'SAVING...'; }
}
.save-indicator::before {
  content: 'SAVING.  ';
  animation: saveDots 1.8s steps(1) 2 forwards;
  font-weight: bold;
}
```

---

## D6 — Chapter-End Text Differentiation

**Location:** Story HTML, chapter-end beat paragraphs.

Update chapter endings as follows (find by text content, replace):

| Chapter | Find | Replace |
|---|---|---|
| Ch09 | `TRACK: 09_COMPLETE` | `TRACK: 09_CORRUPTED` |
| Ch09 | `SAVING...` | `DATA_LOSS: UNRECOVERABLE` |
| Ch12 | `TRACK: 12_COMPLETE` | `TRACK: 12_ARCHIVED` |
| Ch12 | `SAVING...` | `ACCESS: ADMIN_ONLY` |
| Ch13 | `TRACK: 13_COMPLETE` | `TRACK: 13_OVERWRITTEN` |
| Ch13 | `SAVING...` | `PREVIOUS_VERSION: DELETED` |
| Ch16 | `TRACK: 16_COMPLETE` | `TRACK: 16_ILLEGAL` |
| Ch16 | `SAVING...` | `FLAGGED_FOR_AUDIT` |
| Ch17 | Already `TRACK: 17_ABORTED` | No change |

---

## D7 — Ghost Signal Phase Updates in tick()

Add to `ScrollEngine.tick()` on chapter change:
```javascript
// COMMENT: Ghost signal phase update on chapter transition.
if (nextBeat?.type === 'chapter') {
  updateGhostSignalPhase(chapterId);
}
```

(Function defined in C2 above.)

---

## D8 — Silence Lock Text and Color: Compliance Era Variant

**Location:** Ch09 silence lock trigger in `tick()`.

Add compliance-era variant check:
```javascript
// COMMENT: Silence lock text and color varies by narrative phase.
// Pre-patch and post-patch ch16-17: red urgency (signal loss framing).
// Compliance era ch13-15: collar gold, check-in framing.
// This makes the system's inactivity response feel administered, not alarmed.
const isCompliance = ['ch13','ch14','ch15'].includes(chapterId);
const lockText = document.getElementById('silence-lock-text');
const lockBar = document.getElementById('silence-lock-bar');
if (isCompliance && lockText) {
  lockText.innerHTML = '&gt; COMPLIANCE_CHECK<br>&gt; SUBJECT: NOMINAL<br><span style="color: #c8a84b;">[ CONTINUE WHEN READY ]</span>';
  lockText.style.color = '#c8a84b';
  if (lockBar) lockBar.style.background = '#c8a84b';
} else if (lockText) {
  lockText.innerHTML = '&gt; SIGNAL_LOSS<br>&gt; ATTEMPTING_RECOVERY...<br><span style="color: var(--text-dim);">[ SUBJECT IS UNRESPONSIVE ]</span>';
  lockText.style.color = 'var(--danger)';
  if (lockBar) lockBar.style.background = 'var(--danger)';
}
```

---

---

# Track E — UI / CSS

---

## E1 — Compliance Era Inverted Protocol Bar

**Location:** CSS `<style>` block + `syncHud()` JS function.

CSS addition:
```css
/* COMMENT: Post-patch compliance bar fills right-to-left.
   "Full" now means "fully administered." The wrong direction to go.
   Collar gold color differentiates it from standard coherence bar.
   Activated by .compliance-mode class on #hud, set in syncHud(). */
#hud.compliance-mode #hud-coherence {
  left: auto;
  right: 0;
  background: #c8a84b;
}
#hud.compliance-mode #hud-tension {
  background: #c8a84b;
}
```

JS in `syncHud()` — add after existing label logic:
```javascript
// COMMENT: Apply compliance-mode class to HUD during ch13-15.
const hud = document.getElementById('hud');
if (hud) hud.classList.toggle('compliance-mode', isCompliance);
```

---

## E2 — Chapter Flash Differentiation

**Location:** `triggerChapterFlash()` function.

Add cases:
```javascript
// COMMENT: Chapter-specific flash types.
// Ch06 (Ground State): no flash — arrives in silence, the system doesn't announce it.
// Ch03 (Transposition): amber static, low intensity — homecoming to a dying sector.
// All others: existing logic preserved.
if (chapterId === 'ch06') return; // silence arrival — no flash
if (chapterId === 'ch03') {
  overlay.style.backgroundColor = 'rgba(245,166,35,0.08)';
  overlay.className = 'active flash-standard';
  setTimeout(() => overlay.classList.remove('active'), 600);
  return;
}
```

---

## E3 — Chapter Selector: Auto-Update + History Dimming

**Location:** `tick()` function, selector update block (already exists, line ~3369).

Add history dimming after selector value update:
```javascript
// COMMENT: Dim chapter selector options for chapters not yet reached.
// Mirrors Score's access-control framing — locked content has a visual cost.
// Uses _maxChapterReached to track read progress across sessions.
if (!window._maxChapterReached) window._maxChapterReached = 0;
const currentChNum = parseInt(chapterId.replace('ch','')) || 1;
if (currentChNum > window._maxChapterReached) {
  window._maxChapterReached = currentChNum;
  try { localStorage.setItem('kt_max_chapter', currentChNum); } catch(e) {}
}
Array.from(selector.options).forEach(opt => {
  const optNum = parseInt(opt.value.replace('ch','')) || 1;
  opt.style.opacity = optNum <= window._maxChapterReached ? '1' : '0.35';
});
```

On page load, restore from localStorage:
```javascript
// COMMENT: Restore chapter history on load.
try {
  const saved = localStorage.getItem('kt_max_chapter');
  if (saved) window._maxChapterReached = parseInt(saved);
} catch(e) {}
```

---

## E4 — `//[NOTE:]` Audit: Remove Three Overused Annotations

**Location:** Story HTML, these three specific annotations:

1. Remove: `// [NOTE: VALE'S CLASSIFICATION OF LOW-FIDELITY ALIGNS WITH SUBJECT'S BASELINE.]` and `// [NOTE: RETAINED. NO RESOLUTION ACTIONABLE.]` — the reader has already felt this. The system naming it removes the sting.

2. Remove: any `// [NOTE:]` annotations that arrive in the same beat as the emotion they're labeling. The rule going forward: annotations land one beat after the feeling, not during it.

3. Keep all `// [NOTE:]` annotations that are wrong, cold, or arrive too late. Those are working exactly as intended.

---

---

# Execution Order

| Order | Track | Item | Dependency |
|---|---|---|---|
| 1 | C | C1 — Define Ayane's five notes | None — creative decision required first |
| 2 | A | A5 — Ch1 science epigraph | None |
| 3 | A | A6 — Ch5 science epigraph | None |
| 4 | B | B1 — Ch3 melody beats | Requires C1 |
| 5 | A | A1 — Neural pacemaker lore entry | None |
| 6 | B | B2, B3 — Ch6 silence rewrite | Requires B1 (melody established) |
| 7 | A | A4 — 40 Hz system annotation in Ch6 | Requires B2 |
| 8 | C | C4 — Ch6 headphones tooltip | Requires A4 |
| 9 | A | A2, A7 — Vale lecture additions | None |
| 10 | B | B4, B5 — Ch7 silence beat + sensory memory beat | Requires A2 |
| 11 | B | B6, B7, B8 — Patch decision + deletions + narrator line | None |
| 12 | A | A3 — Temporal poverty lore entry | Requires B7 |
| 13 | B | B9 — Ch13 headphone three-beats | Requires B1 |
| 14 | B | B10 — Ch14/15 near-miss beats | None |
| 15 | A | A8 — Remi scene annotation | None |
| 16 | B | B11 — Ch4 Terms echo | None |
| 17 | B | B12 — Ch17 Elara duplication cut | None |
| 18 | B | B13 — Ch17 choosing beat | Requires B1, B9 |
| 19 | C | C2 — Ghost signal three states | Requires B13 |
| 20 | C | C3 — Ch6 audio engine annotation | None |
| 21 | D | D1 — Beat weight system | All Track B data-weight attributes |
| 22 | D | D2 — Wheel threshold 260 | None |
| 23 | D | D3 — BPM heartbeat pulse | None |
| 24 | D | D4 — Dynamic waveform blend | None |
| 25 | D | D5 — SAVING... animation | None |
| 26 | D | D6 — Chapter-end text variants | None |
| 27 | D | D7 — Ghost signal phase in tick() | Requires C2 |
| 28 | D | D8 — Silence lock compliance variant | None |
| 29 | E | E1 — Compliance HUD bar | None |
| 30 | E | E2 — Chapter flash differentiation | None |
| 31 | E | E3 — Chapter selector history | None |
| 32 | E | E4 — NOTE annotation audit | All Track B rewrites complete |

---

*Plan complete. Item count: 32 discrete changes across 5 tracks. Items 1–20 are content; items 21–32 are code. All Track B rewrites include the exact HTML to insert or replace. All Track D/E items include commented implementation code ready for direct integration.*
