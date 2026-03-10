const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('KeepingTime_VolumeOne.html', 'utf8');
const $ = cheerio.load(html, { decodeEntities: false });

const chapBaselines = {
    ch1: [0.45, 0.65],
    ch2: [0.30, 0.82],
    ch3: [0.40, 0.62],
    ch4: [0.32, 0.78],
    ch5: [0.42, 0.70],
    ch6: [0.35, 0.65],
    ch7: [0.50, 0.68],
    ch8: [0.65, 0.55],
    ch9: [0.12, 0.22],
    ch10: [0.72, 0.40],
    ch11: [0.38, 0.75],
    ch12: [0.28, 0.80],
    ch13: [0.15, 0.92],
    ch14: [0.18, 0.88],
    ch15: [0.35, 0.65],
    ch16: [0.48, 0.52],
    ch17: [0.55, 0.48]
};

function jitter(val, maxVar = 0.03) {
    let nv = val + (Math.random() * maxVar * 2 - maxVar);
    return Math.max(0, Math.min(1, nv)).toFixed(2);
}

let lastType = null;

$('div.chapter').each((i, chapElem) => {
    const chId = $(chapElem).attr('id');
    const baseline = chapBaselines[chId] || [0.25, 0.8];
    
    // Find all narrative beats
    $(chapElem).find('p, blockquote').each((j, beat) => {
        const text = $(beat).text().trim();
        const htmlContent = $(beat).html() || '';
        const lowerText = text.toLowerCase();
        let classes = $(beat).attr('class') || '';

        if (!text && !$(beat).find('img, svg').length) return; // Skip empty elements
        
        let vol = baseline[0];
        let coh = baseline[1];
        let typeName = 'neutral';
        let tag = null;

        // --- TAGGING LOGIC ---
        // bass_drop: First beat of Ch06 or Ch08 subsonic arrival
        if (chId === 'ch6' && j <= 2 && lowerText.includes('fifty-five hertz')) tag = 'bass_drop';
        else if (chId === 'ch8' && j <= 2) tag = 'bass_drop';
        
        // combat_ui: First impact beat in Ch08 Sortie
        else if (chId === 'ch8' && (lowerText.includes('struck') || lowerText.includes('slammed') || lowerText.includes('hit'))) tag = 'combat_ui';
        
        // frame_skip: Error / glitch beats in Ch09 and Ch10
        else if ((chId === 'ch9' || chId === 'ch10') && (lowerText.includes('error') || lowerText.includes('glitch'))) tag = 'frame_skip';
        
        // impedance: Collar-tighten beats (Ch02, Ch04, Ch11)
        else if ((chId === 'ch2' || chId === 'ch4' || chId === 'ch11') && lowerText.includes('collar tightened')) tag = 'impedance';
        
        // headmaster: Krell direct-address
        else if (chId === 'ch11' && (lowerText.includes('headmaster') || text.includes('Krell')) && text.includes('"')) tag = 'headmaster';
        
        // social_tag: Malkuth ranking reveal beats
        else if ((chId === 'ch4' || chId === 'ch7') && lowerText.includes('malkuth')) tag = 'social_tag';
        
        // clip: Ch10 sawtooth burst / Bb2 aggression peak
        else if (chId === 'ch10' && lowerText.includes('bb2') && lowerText.includes('peak')) tag = 'clip';
        else if (chId === 'ch10' && lowerText.includes('burst')) tag = 'clip';
        
        // override: Any beat where Taro overrides a system command
        else if (lowerText.includes('override') || lowerText.includes('bypassed')) tag = 'override';
        
        // limiter: All 'limiter removed' / unmasking beats
        else if (lowerText.includes('limiter removed') || lowerText.includes('unmask')) tag = 'limiter';
        
        // ghost: Specific beats (Ch02 Artifact, Ch05 bleed-through, Ch08 jagged circle, Ch11 unformatted end it, Ch16 authenticated ghost)
        else if (chId === 'ch2' && text.includes('[ARTIFACT: H——p ——. DISCARDING]')) tag = 'ghost';
        else if (chId === 'ch5' && lowerText.includes('bleed-through')) tag = 'ghost';
        else if (chId === 'ch8' && lowerText.includes('jagged circle')) tag = 'ghost';
        else if (chId === 'ch11' && text.includes('[UNFORMATTED: End it...]')) tag = 'ghost';
        else if (chId === 'ch16' && lowerText.includes('authenticated ghost')) tag = 'ghost';

        // crash: Final line
        if (text === 'I am bringing the noise.') {
            $(beat).attr('data-vol', "0.75");
            $(beat).attr('data-coh', "0.55");
            $(beat).attr('data-tag', 'crash');
            return;
        }

        // --- NARRATIVE ASSIGNMENT LOGIC ---
        if (classes.includes('format-system') || htmlContent.includes('<code') || text.includes('SYSTEM_ALERT') || text.includes('// [NOTE:')) {
            if (text.includes('CRITICAL') || text.includes('WARNING') || text.includes('FATAL')) {
                vol = 0.75; coh = 0.60; typeName = 'sys_crit';
            } else if (lowerText.includes('limiter removed') || lowerText.includes('unmask')) {
                vol = 0.99; coh = 0.05; typeName = 'sys_peak';
            } else {
                vol = 0.45; coh = 0.85; typeName = 'sys_alert';
            }
        } else if (classes.includes('lore-epigraph') || classes.includes('format-epigraph')) {
            vol = 0.10; coh = 0.95; typeName = 'epigraph';
        } else if (text.startsWith('ZONE:') || text.includes('FIDELITY:') || (j < 3 && text.startsWith('STATUS:'))) {
            vol = 0.20; coh = 0.92; typeName = 'zone_head';
        } else if (classes.includes('format-thought')) {
            vol = 0.40; coh = 0.70; typeName = 'thought';
        } else if (htmlContent.includes('&quot;') || text.includes('"') || text.includes('“')) {
            if (text.includes('Voss') || text.includes('Krell')) {
                vol = 0.20; coh = 0.95; typeName = 'dia_auth';
            } else if (text.includes('!') || lowerText.includes('snapped') || lowerText.includes('shouted') || lowerText.includes('hissed')) {
                vol = 0.55; coh = 0.65; typeName = 'dia_tense';
            } else {
                vol = 0.30; coh = 0.75; typeName = 'dia_calm';
            }
        } else if (text.includes('BPM') || text.includes('SDI') || text.includes('HIQ')) {
            vol = 0.35; coh = 0.80; typeName = 'hud_metric';
        } else if (lowerText.includes('struck') || lowerText.includes('combat') || lowerText.includes('impact') || lowerText.includes('slammed')) {
            vol = 0.60; coh = 0.60; typeName = 'combat';
        } else if (lowerText.includes('colliding') || lowerText.includes('conflict') || lowerText.includes('mismatch')) {
            vol = 0.70; coh = 0.55; typeName = 'phase_conflict';
        } else if (lowerText.includes('spike') || lowerText.includes('thermal load') || lowerText.includes('pressure')) {
            vol = 0.85; coh = 0.40; typeName = 'resonance_spike';
        } else if (chId === 'ch9' || lowerText.includes('void') || lowerText.includes('silence')) {
            vol = 0.10; coh = 0.20; typeName = 'void';
        } else if (chId === 'ch13' || lowerText.includes('compliant') || lowerText.includes('patch')) {
            vol = 0.15; coh = 0.92; typeName = 'post_patch';
        } else if (lowerText.includes('elara') || lowerText.includes('wrong note')) {
            vol = 0.45; coh = 0.88; typeName = 'elara';
        } else if (chId === 'ch16' || chId === 'ch17' || lowerText.includes('underground') || lowerText.includes('illegal')) {
            vol = 0.50; coh = 0.50; typeName = 'underground';
        } else if (lowerText.includes('TRACK_COMPLETE') || text.includes('FILE: ANGER / STATUS: HIDDEN') || (j === $(chapElem).find('p').length - 1)) {
            // "File: ANGER / Status: HIDDEN" in Ch13 needs vol 0.22, let's hardcode it
            if (text.includes('FILE: ANGER / STATUS: HIDDEN')) {
                vol = 0.22; coh = 0.92; typeName = 'hidden_anger';
            } else {
                vol = 0.20; coh = 0.85; typeName = 'chap_end';
            }
        }

        if (typeName === lastType) {
            vol = parseFloat(jitter(vol, 0.04));
            coh = parseFloat(jitter(coh, 0.04));
        } else {
            vol = parseFloat(jitter(vol, 0.01));
            coh = parseFloat(jitter(coh, 0.01));
        }
        
        lastType = typeName;

        $(beat).attr('data-vol', vol.toFixed(2));
        $(beat).attr('data-coh', coh.toFixed(2));
        
        // Retain original tags if they manually existed, but replace if we found one
        if (tag) {
            $(beat).attr('data-tag', tag);
        }
    });
});

fs.writeFileSync('KeepingTime_VolumeOne.html', $.html());
console.log('Update Complete.');
