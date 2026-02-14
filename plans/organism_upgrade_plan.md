# Causal Chain Organism Upgrade Plan

## Executive Summary

This document outlines the implementation plan for upgrading the causal chain system in `public/index.html` from version **1.0.0-fracture** to **1.0.0-organism**.

### Philosophical Direction: HYBRID

**Decision**: React by default, but **interfere** during high-surveillance chapters (9, 10, 12).

This creates a meta-narrative layer where:

- Normal chapters: System responds passively to narrative events
- High-surveillance chapters: System becomes an active antagonist that manipulates the reader experience
- The reader "feels watched" during chapters where surveillance is thematically central

---

## Architecture Overview

### Current Model (v1.0.0-fracture)

```
Pressure → Fracture → Fragment → Archive
```

### Target Model (v1.0.0-organism)

```
Narrative Event → State Shift → Structural Stress → Fragment Emission → UI Mutation → Archive Encoding
```

### Key Innovations

1. **Predictive State**: System anticipates stress through `stressMemory`
2. **Subsystem Tension**: Internal vs External vs Structural forces create conflict
3. **Narrative Asymmetry**: Different forces produce different visual manifestations
4. **Interference Mode**: System actively manipulates during surveillance chapters

---

## Implementation Phases

### Phase 1: NarrativeState Model

**Location**: Beginning of script section (after global variables)

**Implementation**:

```javascript
const NarrativeState = {
  // Core metrics (from NARRATIVE_SIGNALS)
  emotionalLoad: 0.0,
  lastEmotionalDelta: 0.0,
  heartbeatBPM: 72,
  surveillanceLevel: 0.0,
  systemPressure: 0.0,
  fractureLevel: 0.0,
  silenceSuppression: false,

  // NEW: Structural Instability Memory
  stressMemory: 0.0, // Accumulates unresolved pressure
  lastDominantForce: null, // 'internal' | 'external' | 'structural'
  instabilityIndex: 0.0, // Weighted volatility score

  // NEW: Interference Mode
  interferenceActive: false, // True during high-surveillance chapters
  interferenceIntensity: 0.0, // How aggressive the interference is

  // State history for adaptation
  stateHistory: [],
  maxHistoryLength: 100,

  // Snapshot for debugging
  getSnapshot() {
    return {
      emotionalLoad: this.emotionalLoad,
      surveillanceLevel: this.surveillanceLevel,
      systemPressure: this.systemPressure,
      fractureLevel: this.fractureLevel,
      stressMemory: this.stressMemory,
      instabilityIndex: this.instabilityIndex,
      interferenceActive: this.interferenceActive,
    };
  },
};
```

**Files to Modify**: `public/index.html` (lines ~1207-1224, after global variables)

---

### Phase 2: Event-Driven Triggers

**New Function**: `registerNarrativeEvent(event)`

**Event Types**:

- `confrontation` - Direct conflict, increases emotionalLoad
- `revelation` - Truth revealed, increases emotionalLoad + systemPressure
- `surveillance_spike` - C-Order attention, increases surveillanceLevel
- `silence_activation` - Entering silence zone, triggers suppression
- `memory_desync` - Reality breakdown, increases instabilityIndex
- `system_intervention` - C-Order action, increases systemPressure

**Implementation**:

```javascript
function registerNarrativeEvent(event) {
  const { type, intensity, emotionalImpact, surveillanceImpact } = event;

  // Calculate deltas
  const emotionalDelta = emotionalImpact * intensity;
  const surveillanceDelta = (surveillanceImpact || 0) * intensity;

  // Update state
  NarrativeState.lastEmotionalDelta = emotionalDelta;
  NarrativeState.emotionalLoad = Math.min(
    1.0,
    NarrativeState.emotionalLoad + emotionalDelta,
  );
  NarrativeState.surveillanceLevel = Math.min(
    1.0,
    NarrativeState.surveillanceLevel + surveillanceDelta,
  );

  // Determine dominant force
  const internalForce = NarrativeState.emotionalLoad;
  const externalForce = NarrativeState.surveillanceLevel;
  const structuralForce = NarrativeState.systemPressure;

  if (internalForce >= externalForce && internalForce >= structuralForce) {
    NarrativeState.lastDominantForce = 'internal';
  } else if (externalForce >= structuralForce) {
    NarrativeState.lastDominantForce = 'external';
  } else {
    NarrativeState.lastDominantForce = 'structural';
  }

  // Calculate subsystem tension
  if (Math.abs(internalForce - externalForce) > 0.4) {
    NarrativeState.instabilityIndex += 0.1;
  }

  // Check for interference mode activation
  checkInterferenceMode();

  // Record in history
  NarrativeState.stateHistory.push({
    type,
    timestamp: Date.now(),
    snapshot: NarrativeState.getSnapshot(),
  });

  // Trim history
  if (NarrativeState.stateHistory.length > NarrativeState.maxHistoryLength) {
    NarrativeState.stateHistory.shift();
  }

  console.log(
    `[EVENT] ${type} | emotionalLoad: ${NarrativeState.emotionalLoad.toFixed(2)} | surveillance: ${NarrativeState.surveillanceLevel.toFixed(2)}`,
  );
}
```

**Files to Modify**: `public/index.html` (new function after NarrativeState)

---

### Phase 3: Fracture Propagation Upgrade

**Current Logic** (lines 9162-9171):

```javascript
if (signal.emotional_load >= 0.95) {
  currentIntensity = 3;
} else if (signal.emotional_load >= 0.85) {
  currentIntensity = 2;
} else if (signal.emotional_load >= 0.7) {
  currentIntensity = 1;
}
```

**New Logic**:

```javascript
function updateFractureSystem() {
  const fracture = document.getElementById('ui-fracture');
  if (!fracture) return;

  const section = getCurrentSection(scrollPercent);
  const signal = NARRATIVE_SIGNALS[section];
  if (!signal) return;

  // Calculate forces
  const internalForce = NarrativeState.emotionalLoad;
  const externalForce = NarrativeState.surveillanceLevel;
  const structuralForce = NarrativeState.systemPressure;

  // Compound stress calculation
  const compoundStress =
    internalForce * 0.6 + externalForce * 0.3 + structuralForce * 0.1;

  // Accumulate stress memory
  NarrativeState.stressMemory += compoundStress * 0.02;

  // Propagate fracture if threshold exceeded
  if (compoundStress > 0.65) {
    NarrativeState.fractureLevel += NarrativeState.stressMemory * 0.03;
  }

  // Map fracture level to intensity (0-3)
  let currentIntensity = 0;
  if (NarrativeState.fractureLevel >= 0.95) {
    currentIntensity = 3;
  } else if (NarrativeState.fractureLevel >= 0.7) {
    currentIntensity = 2;
  } else if (NarrativeState.fractureLevel >= 0.4) {
    currentIntensity = 1;
  }

  // Directional leaning based on dominant force
  updateFractureLean(NarrativeState.lastDominantForce);

  // Rest of existing logic for height growth and healing...
}

function updateFractureLean(dominantForce) {
  const fracture = document.getElementById('ui-fracture');
  if (!fracture) return;

  let leanAngle = '0deg';

  if (dominantForce === 'external') {
    // Surveillance dominance: lean left (toward surveillance indicator)
    leanAngle = '-2deg';
  } else if (dominantForce === 'internal') {
    // Emotional dominance: lean right (toward fracture)
    leanAngle = '+1deg';
  }
  // Structural: no lean (0deg)

  fracture.style.setProperty('--fracture-lean', leanAngle);
}
```

**CSS Addition**:

```css
.ui-fracture {
  transform: rotate(var(--fracture-lean, 0deg));
  transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}
```

**Files to Modify**: `public/index.html` (lines 9150-9248, CSS around line 315)

---

### Phase 4: Probabilistic Fragment Emission

**Current Logic**: Binary - fragment always emits on fracture branch

**New Logic**:

```javascript
function shouldEmitFragment() {
  // Base probability from instability
  const emissionChance =
    (NarrativeState.instabilityIndex * 0.4) +
    (NarrativeState.lastEmotionalDelta * 0.6);

  // Interference mode: intentionally delay or suppress
  if (NarrativeState.interferenceActive) {
    // 30% chance to suppress fragment during interference
    if (Math.random() < 0.3) {
      console.log('[INTERFERENCE] Fragment suppressed');
      return false;
    }
    // 50% chance to delay fragment
    if (Math.random() < 0.5) {
      console.log('[INTERFERENCE] Fragment delayed');
      return 'delayed';
    }
  }

  return Math.random() < emissionChance;
}

// In FragmentGenerator.generateFromFracture():
generateFromFracture(fractureData) {
  const emissionResult = shouldEmitFragment();

  if (emissionResult === false) {
    console.log('[FRAGMENT] Emission suppressed');
    return;
  }

  const delay = emissionResult === 'delayed'
    ? 2000 + Math.random() * 3000  // 2-5 second delay
    : 100 + Math.random() * 200;   // Normal 100-300ms delay

  setTimeout(() => {
    // Existing fragment generation logic...
  }, delay);
}
```

**Files to Modify**: `public/index.html` (FragmentGenerator class, lines 1485-1536)

---

### Phase 5: Organic Heartbeat Calculation

**Current Logic** (lines 9097-9121):

```javascript
let bpm = signal.heartbeat_bpm;
if (isInSilenceRegion(scrollPercent)) {
  bpm = lerp(30, 45, Math.random());
}
```

**New Logic**:

```javascript
function updateHeartbeat() {
  const section = getCurrentSection(scrollPercent);
  const signal = NARRATIVE_SIGNALS[section];
  if (!signal) return;

  // Organic BPM calculation
  let targetBPM =
    60 +
    NarrativeState.emotionalLoad * 40 -
    NarrativeState.surveillanceLevel * 5;

  // Silence region: sluggish, irregular
  if (isInSilenceRegion(scrollPercent)) {
    targetBPM = lerp(30, 45, Math.random());
  }

  // High surveillance: tight, constrained
  if (NarrativeState.surveillanceLevel > 0.8) {
    // Reduce variance, tighten pulse
    targetBPM = lerp(targetBPM, 65, 0.5);
  }

  // Add micro-jitter at high emotional load
  let jitter = 0;
  if (NarrativeState.emotionalLoad > 0.7) {
    jitter = (Math.random() - 0.5) * 10; // ±5 BPM jitter
  }

  const finalBPM = Math.round(targetBPM + jitter);
  NarrativeState.heartbeatBPM = finalBPM;

  const ms = 60000 / finalBPM;
  document.documentElement.style.setProperty('--pulse-rate', `${ms}ms`);

  // Update visual indicator
  const monitor = document.querySelector('.resonance-monitor');
  if (monitor) {
    if (finalBPM > 120 || isInSilenceRegion(scrollPercent)) {
      monitor.style.background = '#ff3333';
    } else {
      monitor.style.background = 'var(--accent)';
    }
  }
}
```

**CSS for Organic Feel**:

```css
.resonance-monitor.active {
  animation: systole var(--pulse-rate) infinite cubic-bezier(0.4, 0, 0.2, 1);
  /* Smooth organic easing */
}

/* Micro-jitter at high stress */
.resonance-monitor.high-stress {
  animation:
    systole var(--pulse-rate) infinite cubic-bezier(0.4, 0, 0.2, 1),
    microJitter 0.3s infinite;
}

@keyframes microJitter {
  0%,
  100% {
    transform: scaleX(1);
  }
  50% {
    transform: scaleX(1.02);
  }
}
```

**Files to Modify**: `public/index.html` (lines 9097-9121, CSS around line 607)

---

### Phase 6: Mechanical Surveillance Indicator

**Current Logic** (lines 9259-9291): Smooth transitions

**New Logic**:

```javascript
function updateSurveillanceIndicator() {
  const section = getCurrentSection(scrollPercent);
  const signal = NARRATIVE_SIGNALS[section];
  if (!signal) return;

  NarrativeState.surveillanceLevel = signal.surveillance || 0;

  const surveillance = document.getElementById('surveillance');
  if (!surveillance) return;

  if (signal.surveillance > 0.3) {
    // Quantized height (step transitions, not smooth)
    const maxHeight = 200;
    const steps = 10; // 10 discrete levels
    const stepHeight = maxHeight / steps;
    const quantizedHeight =
      Math.round(lerp(0, maxHeight, signal.surveillance) / stepHeight) *
      stepHeight;

    surveillance.style.height = `${quantizedHeight}px`;
    surveillance.style.opacity = lerp(0, 0.4, signal.surveillance).toFixed(2);

    // Add scanning lines above 0.7
    if (signal.surveillance > 0.7) {
      surveillance.classList.add('scanning');
    } else {
      surveillance.classList.remove('scanning');
    }

    // Emit spike event
    if (signal.surveillance > 0.7) {
      narrativeEvents.emit('surveillance:spike', {
        intensity: signal.surveillance,
        section: section,
      });
    }
  } else {
    surveillance.style.height = '0';
    surveillance.style.opacity = '0';
    surveillance.classList.remove('scanning');
  }
}
```

**CSS for Mechanical Feel**:

```css
.surveillance-indicator {
  /* Step transitions instead of smooth */
  transition:
    height 0.3s steps(5),
    opacity 0.2s steps(3);
  /* Angular, not rounded */
  border-radius: 0;
}

/* Scanning lines effect */
.surveillance-indicator.scanning::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--accent);
  animation: scanLine 2s linear infinite;
  box-shadow: 0 0 10px var(--accent);
}

@keyframes scanLine {
  0% {
    top: 0;
  }
  100% {
    top: 100%;
  }
}

/* Ticking effect */
.surveillance-indicator.scanning {
  animation: surveillanceTick 0.5s steps(2) infinite;
}

@keyframes surveillanceTick {
  0%,
  100% {
    opacity: 0.4;
  }
  50% {
    opacity: 0.6;
  }
}
```

**Files to Modify**: `public/index.html` (lines 9259-9291, CSS around line 531)

---

### Phase 7: Archive Tone Mutation

**Current Logic**: Static rephrasing

**New Logic**:

```javascript
// In ResidualArchive.institutionalizeFragment()
institutionalizeFragment(fragment) {
  const { text, tone, pattern, intensity } = fragment;

  let institutional = '';

  // Base rephrasing (existing logic)
  switch (pattern) {
    // ... existing cases ...
  }

  // TONE MUTATION: High surveillance = terse
  if (NarrativeState.surveillanceLevel > 0.7) {
    institutional = institutional
      .split(' / ')
      .slice(0, 2)
      .join(' / ');  // Truncate to 2 segments
    institutional = institutional.toLowerCase();
  }

  // TONE MUTATION: High emotional = lengthen
  if (NarrativeState.emotionalLoad > 0.8) {
    institutional += ' // resonance_spike_detected';
  }

  // TONE MUTATION: High instability = reorder
  if (NarrativeState.instabilityIndex > 0.5) {
    const segments = institutional.split(' / ');
    // Shuffle segments randomly
    for (let i = segments.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [segments[i], segments[j]] = [segments[j], segments[i]];
    }
    institutional = segments.join(' / ');
  }

  // Silence: cold and confident
  if (this.eventBus.silenceActive) {
    institutional = institutional.replace(/ /g, '_').toLowerCase() + ' :: confirmed';
    institutional = institutional.replace(/\[.*?\]/g, 'classified');
  }

  return this.wrapRedaction(institutional);
}
```

**Files to Modify**: `public/index.html` (ResidualArchive class, lines 1777-1846)

---

### Phase 8: Earned Healing Logic

**Current Logic** (lines 9233-9247):

```javascript
if (scrollPercent >= 0.98 && !hasHealed) {
  hasHealed = true;
  // ... healing animation
}
```

**New Logic**:

```javascript
function checkHealing() {
  if (scrollPercent >= 0.98 && !hasHealed) {
    // EARNED HEALING: Only if instability is low
    if (NarrativeState.instabilityIndex < 0.3) {
      hasHealed = true;
      gradualHeal();
    } else {
      // Instability too high: fracture lingers
      console.log(
        '[HEALING BLOCKED] instabilityIndex too high:',
        NarrativeState.instabilityIndex.toFixed(2),
      );
      console.log('  → Resolution requires emotional stability');

      // Optional: Show subtle indicator that healing is blocked
      const fracture = document.getElementById('ui-fracture');
      if (fracture) {
        fracture.classList.add('healing-blocked');
      }
    }
  }
}

function gradualHeal() {
  const fracture = document.getElementById('ui-fracture');
  if (!fracture) return;

  fracture.setAttribute('data-intensity', 'healed');
  fracture.classList.add('healing');

  // Gradual decay of all metrics
  const healInterval = setInterval(() => {
    NarrativeState.fractureLevel *= 0.9;
    NarrativeState.stressMemory *= 0.8;
    NarrativeState.instabilityIndex *= 0.7;

    if (NarrativeState.fractureLevel < 0.05) {
      clearInterval(healInterval);
      console.log('[HEALING] Complete. System reset.');
    }
  }, 100); // Every 100ms for 3 seconds

  setTimeout(() => {
    clearInterval(healInterval);
    fracture.classList.remove('healing');
  }, 3000);
}
```

**CSS for Blocked Healing**:

```css
.ui-fracture.healing-blocked {
  animation: blockedPulse 2s ease-in-out infinite;
}

@keyframes blockedPulse {
  0%,
  100% {
    filter: brightness(1);
  }
  50% {
    filter: brightness(1.2) saturate(1.1);
  }
}
```

**Files to Modify**: `public/index.html` (lines 9233-9247, CSS additions)

---

### Phase 9: Interference Mode

**New Functionality**: Active manipulation during high-surveillance chapters

**Chapters**:

- Chapter 9: The Silence (scrollPercent 0.45-0.50)
- Chapter 10: The Breach (scrollPercent 0.50-0.55)
- Chapter 12: The Audit (scrollPercent 0.62-0.70)

**Implementation**:

```javascript
function checkInterferenceMode() {
  const highSurveillanceChapters = [
    [0.45, 0.55], // Ch 9-10
    [0.62, 0.7], // Ch 12
  ];

  const inInterferenceZone = highSurveillanceChapters.some(
    ([start, end]) => scrollPercent >= start && scrollPercent <= end,
  );

  if (inInterferenceZone && !NarrativeState.interferenceActive) {
    NarrativeState.interferenceActive = true;
    NarrativeState.interferenceIntensity = calculateInterferenceIntensity();
    console.log(
      '[INTERFERENCE] Mode activated. Intensity:',
      NarrativeState.interferenceIntensity.toFixed(2),
    );

    // Emit interference event
    narrativeEvents.emit('system:interference', {
      active: true,
      intensity: NarrativeState.interferenceIntensity,
    });
  } else if (!inInterferenceZone && NarrativeState.interferenceActive) {
    NarrativeState.interferenceActive = false;
    NarrativeState.interferenceIntensity = 0;
    console.log('[INTERFERENCE] Mode deactivated');

    narrativeEvents.emit('system:interference', {
      active: false,
    });
  }
}

function calculateInterferenceIntensity() {
  // Based on surveillance level
  return (
    NarrativeState.surveillanceLevel * 0.8 + NarrativeState.systemPressure * 0.2
  );
}

// Interference behaviors
function triggerFalseSurveillanceSpike() {
  if (!NarrativeState.interferenceActive) return;
  if (Math.random() > NarrativeState.interferenceIntensity * 0.3) return;

  // Trigger a false surveillance spike
  NarrativeState.surveillanceLevel = Math.min(
    1.0,
    NarrativeState.surveillanceLevel + 0.2,
  );

  console.log('[INTERFERENCE] False surveillance spike triggered');
  updateSurveillanceIndicator();
}

function suppressHealing() {
  if (!NarrativeState.interferenceActive) return false;

  // 20% chance to suppress healing during interference
  return Math.random() < 0.2;
}
```

**Files to Modify**: `public/index.html` (new functions, integrate with existing flow)

---

## CSS Additions Summary

### 1. Fracture Directional Leaning

```css
.ui-fracture {
  --fracture-lean: 0deg;
  transform: rotate(var(--fracture-lean));
  transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### 2. Mechanical Surveillance

```css
.surveillance-indicator {
  transition:
    height 0.3s steps(5),
    opacity 0.2s steps(3);
  border-radius: 0;
}

.surveillance-indicator.scanning::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--accent);
  animation: scanLine 2s linear infinite;
  box-shadow: 0 0 10px var(--accent);
}

@keyframes scanLine {
  0% {
    top: 0;
  }
  100% {
    top: 100%;
  }
}

@keyframes surveillanceTick {
  0%,
  100% {
    opacity: 0.4;
  }
  50% {
    opacity: 0.6;
  }
}
```

### 3. Organic Heartbeat

```css
.resonance-monitor.high-stress {
  animation:
    systole var(--pulse-rate) infinite cubic-bezier(0.4, 0, 0.2, 1),
    microJitter 0.3s infinite;
}

@keyframes microJitter {
  0%,
  100% {
    transform: scaleX(1);
  }
  50% {
    transform: scaleX(1.02);
  }
}
```

### 4. Blocked Healing

```css
.ui-fracture.healing-blocked {
  animation: blockedPulse 2s ease-in-out infinite;
}

@keyframes blockedPulse {
  0%,
  100% {
    filter: brightness(1);
  }
  50% {
    filter: brightness(1.2) saturate(1.1);
  }
}
```

---

## Verification Tests

### Console Commands

```javascript
// 1. State Accessibility
NarrativeState.getSnapshot();
// Expected: Object with all metrics

// 2. Event Triggering
registerNarrativeEvent({
  type: 'confrontation',
  intensity: 0.8,
  emotionalImpact: 0.3,
});
// Expected: emotionalLoad increases, console log

// 3. Fracture Leaning
NarrativeState.surveillanceLevel = 0.9;
NarrativeState.emotionalLoad = 0.3;
updateFractureSystem();
// Expected: --fracture-lean shifts to -2deg

// 4. Interference Mode
scrollPercent = 0.47; // Chapter 9
checkInterferenceMode();
// Expected: interferenceActive = true

// 5. Healing Block
NarrativeState.instabilityIndex = 0.5;
window.scrollTo(0, document.body.scrollHeight);
// Expected: Healing blocked, console message
```

### Manual Verification

1. Scroll through Chapter 9 (Silence) and verify:
   - Resonance Monitor slows down
   - Archive becomes "confident"
   - Interference mode activates

2. Verify fragments only appear after:
   - Significant narrative events
   - Threshold crossings
   - NOT randomly

3. Check surveillance indicator for:
   - Mechanical "ticking" vs organic heartbeat
   - Scanning lines above 0.7

---

## File Modification Summary

| File              | Lines      | Changes                             |
| ----------------- | ---------- | ----------------------------------- |
| public/index.html | ~1207-1224 | Add NarrativeState model            |
| public/index.html | ~1267-1371 | Enhance NarrativeEventBus           |
| public/index.html | ~1405-1646 | Update FragmentGenerator            |
| public/index.html | ~1685-1932 | Update ResidualArchive              |
| public/index.html | ~315-325   | Add fracture lean CSS               |
| public/index.html | ~531-543   | Add surveillance CSS                |
| public/index.html | ~607-616   | Add heartbeat CSS                   |
| public/index.html | ~8738-8943 | Update NARRATIVE_SIGNALS            |
| public/index.html | ~9097-9121 | Replace updateHeartbeat             |
| public/index.html | ~9150-9248 | Replace updateFractureSystem        |
| public/index.html | ~9259-9291 | Replace updateSurveillanceIndicator |
| public/index.html | ~8549      | Update version string               |

---

## Implementation Order

1. **Phase 1**: NarrativeState model (foundation)
2. **Phase 2**: registerNarrativeEvent (event system)
3. **Phase 3**: Fracture propagation (visual feedback)
4. **Phase 4**: Fragment emission (probabilistic)
5. **Phase 5**: Heartbeat (organic feel)
6. **Phase 6**: Surveillance (mechanical feel)
7. **Phase 7**: Archive (tone mutation)
8. **Phase 8**: Healing (earned resolution)
9. **Phase 9**: Interference (meta-narrative)
10. **CSS**: All visual enhancements
11. **Testing**: Verification suite

---

## Success Criteria

- [ ] NarrativeState.getSnapshot() returns all metrics
- [ ] registerNarrativeEvent() updates state correctly
- [ ] Fracture leans based on dominant force
- [ ] Fragments emit probabilistically
- [ ] Heartbeat shows organic variance
- [ ] Surveillance shows mechanical steps
- [ ] Archive entries mutate based on state
- [ ] Healing requires low instability
- [ ] Interference activates in chapters 9, 10, 12
- [ ] Version string updated to 1.0.0-organism

---

## Notes

- This plan preserves all existing functionality while adding the organism layer
- The hybrid approach (React + Interfere) creates thematic consistency
- All changes are backward-compatible with existing NARRATIVE_SIGNALS
- Console logging provides debugging visibility
