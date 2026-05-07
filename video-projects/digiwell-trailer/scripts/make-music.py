"""Generate the warm-electronic ambient bed for digiwell-trailer.

~32s of slow C-major pad with amber-tone harmonics + 90 BPM ghost kick at 18%
mix + filtered noise sweeps timed to the trailer's whip-streak transitions.

Different palette from RVL's lime-tech bed — warmer, breathier, more "agency
premium" than "punk VC". Synth-pluck shimmers reinforce Beats 2 / 3 transitions.
"""
import numpy as np
import soundfile as sf

SR = 44100
DUR = 32.0
N = int(SR * DUR)
t_full = np.arange(N) / SR

# ---- Slow pad — C major (C-E-G-B for warmth + slight C5 sparkle) ------------
# Two voicings detuned ±2 cents for analog warmth.
pad_freqs_lo = [130.81, 164.81, 196.00, 246.94]   # C3 E3 G3 B3
pad_freqs_hi = [261.63, 329.63, 392.00, 493.88]   # C4 E4 G4 B4
pad = np.zeros(N)
for f in pad_freqs_lo:
    pad += 0.045 * (np.sin(2*np.pi*f*t_full) + 0.35 * np.sin(2*np.pi*(f*1.001)*t_full))
for f in pad_freqs_hi:
    pad += 0.030 * np.sin(2*np.pi*f*t_full)
# Slow tremolo so it breathes
pad *= 0.85 + 0.15 * np.sin(2*np.pi*0.10*t_full)

# ---- Ghost kick — 90 BPM, every other beat, low and felt -------------------
kick = np.zeros(N)
bpm = 90
beat = 60.0 / bpm
for kt in np.arange(0.5, DUR, beat * 2):
    s = int(kt * SR)
    L = int(0.22 * SR)
    if s + L > N: break
    env = np.exp(-np.arange(L) / (0.04 * SR))
    fs  = 60 * np.exp(-np.arange(L) / (0.05 * SR)) + 38
    ph  = 2*np.pi*np.cumsum(fs) / SR
    kick[s:s+L] += 0.18 * env * np.sin(ph)

# ---- Soft synth-pluck shimmers at beat transitions (whip-streak moments) ----
# Trailer beats are at 4.5 / 9.5 / 18 / 22.5 — drop a pluck just before each.
def pluck(freq, start_s, decay=0.45, amp=0.07):
    out = np.zeros(N)
    s = int(start_s * SR)
    if s >= N: return out
    L = min(N - s, int(decay * SR * 4))
    times = np.arange(L) / SR
    env = np.exp(-times / decay)
    sig = 0.7 * np.sin(2*np.pi*freq*times)
    sig += 0.3 * np.sin(2*np.pi*freq*2*times) * np.exp(-times/0.18)
    out[s:s+L] = amp * env * sig
    return out

shimmer_targets = [4.30, 9.30, 17.80, 22.30]      # ~0.2s before each whip-streak
shimmer_pitches = [523.25, 659.25, 783.99, 1046.50]  # C5 E5 G5 C6
mix_shimmer = np.zeros(N)
for st, fr in zip(shimmer_targets, shimmer_pitches):
    mix_shimmer += pluck(fr, st, decay=0.55, amp=0.07)

# ---- Filtered noise sweep — 1 long swell rising across the whole track -----
# Adds an "amber energy" sense of forward motion.
rng = np.random.default_rng(seed=37)
noise = rng.standard_normal(N) * 0.018
# Low-pass via simple moving average + envelope that swells then fades
window = 35
noise_lp = np.convolve(noise, np.ones(window)/window, mode='same')
sweep_env = np.exp(-((t_full - 18.0) ** 2) / (2 * 8.0 ** 2))   # gaussian centered at 18s, sigma 8
noise_layer = noise_lp * sweep_env * 0.8

# ---- Tiny shaker hi-hats at half-time, very low ----------------------------
hat = np.zeros(N)
for ht in np.arange(0.5 + beat/2, DUR, beat):
    s = int(ht * SR)
    L = int(0.04 * SR)
    if s + L > N: break
    env = np.exp(-np.arange(L) / (0.012 * SR))
    n   = rng.standard_normal(L)
    n_h = np.diff(n, prepend=0)
    hat[s:s+L] += 0.018 * env * n_h

# ---- Mix --------------------------------------------------------------------
mixed = pad + kick + mix_shimmer + noise_layer + hat

# Master fade in / out
fi = int(2.0 * SR)
fo = int(3.5 * SR)
mixed[:fi]  *= np.linspace(0, 1, fi)
mixed[-fo:] *= np.linspace(1, 0, fo)

peak = np.max(np.abs(mixed))
if peak > 0:
    mixed = mixed / peak * 0.78

OUT = '/home/user/hyperframes-student-kit/video-projects/digiwell-trailer/assets/music.wav'
sf.write(OUT, mixed, SR)
print(f"Wrote {DUR:.1f}s warm-electronic bed → {OUT}")
