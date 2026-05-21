"""Generate the warm-electronic ambient bed for digiwell-ttw-workshop.

~13s — shorter, snappier cousin of the 30s digiwell-trailer bed. Same warm
C-major pad palette, but the noise-sweep crest is centered earlier (~9s, at
the Beat-2 cards landing) so the CTA arrives over the swell instead of the
fade.

Shimmer plucks placed at the trailer's whip-streak seams:
  2.40s (Beat 0 → Beat 1)
  5.80s (Beat 1 → Beat 2)
  9.30s (Beat 2 → Beat 3 — CTA opening)
"""
import numpy as np
import soundfile as sf

SR = 44100
DUR = 13.0
N = int(SR * DUR)
t_full = np.arange(N) / SR

# ---- Slow pad — C major (C-E-G-B for warmth) -------------------------------
pad_freqs_lo = [130.81, 164.81, 196.00, 246.94]   # C3 E3 G3 B3
pad_freqs_hi = [261.63, 329.63, 392.00, 493.88]   # C4 E4 G4 B4
pad = np.zeros(N)
for f in pad_freqs_lo:
    pad += 0.045 * (np.sin(2*np.pi*f*t_full) + 0.35 * np.sin(2*np.pi*(f*1.001)*t_full))
for f in pad_freqs_hi:
    pad += 0.030 * np.sin(2*np.pi*f*t_full)
# Slow tremolo so it breathes
pad *= 0.85 + 0.15 * np.sin(2*np.pi*0.12*t_full)

# ---- Ghost kick — 90 BPM half-time, sub-bass felt-not-heard ----------------
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
    kick[s:s+L] += 0.20 * env * np.sin(ph)

# ---- Synth-pluck shimmers at the whip-streak seams ------------------------
def pluck(freq, start_s, decay=0.45, amp=0.08):
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

# Each shimmer placed ~0.1s before the whip-streak so the pluck attacks
# right as the transition fires.
shimmer_targets = [2.40, 5.80, 9.30]
shimmer_pitches = [523.25, 659.25, 1046.50]  # C5, E5, C6 — climbing
mix_shimmer = np.zeros(N)
for st, fr in zip(shimmer_targets, shimmer_pitches):
    mix_shimmer += pluck(fr, st, decay=0.55, amp=0.085)

# ---- Filtered noise sweep — swell centered at Beat 2/3 boundary ------------
rng = np.random.default_rng(seed=49)
noise = rng.standard_normal(N) * 0.022
window = 35
noise_lp = np.convolve(noise, np.ones(window)/window, mode='same')
# Gaussian centered at 9s (CTA opening), sigma 3s
sweep_env = np.exp(-((t_full - 9.0) ** 2) / (2 * 3.0 ** 2))
noise_layer = noise_lp * sweep_env * 0.9

# ---- Tiny shaker hi-hats at half-time --------------------------------------
hat = np.zeros(N)
for ht in np.arange(0.5 + beat/2, DUR, beat):
    s = int(ht * SR)
    L = int(0.04 * SR)
    if s + L > N: break
    env = np.exp(-np.arange(L) / (0.012 * SR))
    n   = rng.standard_normal(L)
    n_h = np.diff(n, prepend=0)
    hat[s:s+L] += 0.020 * env * n_h

# ---- Mix --------------------------------------------------------------------
mixed = pad + kick + mix_shimmer + noise_layer + hat

# Master fade in / out — shorter than the 30s bed since runtime is only 13s
fi = int(1.0 * SR)
fo = int(2.2 * SR)
mixed[:fi]  *= np.linspace(0, 1, fi)
mixed[-fo:] *= np.linspace(1, 0, fo)

peak = np.max(np.abs(mixed))
if peak > 0:
    mixed = mixed / peak * 0.78

OUT = '/home/user/hyperframes-student-kit/video-projects/digiwell-ttw-workshop/assets/music.wav'
sf.write(OUT, mixed, SR)
print(f"Wrote {DUR:.1f}s warm-electronic bed -> {OUT}")
