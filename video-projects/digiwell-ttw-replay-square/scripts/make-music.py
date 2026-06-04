"""Generate the warm-electronic ambient bed for digiwell-ttw-replay.

~19s — same warm C-major palette as the other Digiwell beds, sized for the
5-beat replay trailer. Shimmer plucks climb the scale at each layer seam
(Context -> Skills -> Workflows -> CTA), reinforcing the "stack building up"
metaphor. Noise sweep crests at the CTA opening (~15s).

Beat transitions (whip-streaks): 3s, 7s, 11s, 15s.
"""
import numpy as np
import soundfile as sf

SR = 44100
DUR = 19.0
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
pad *= 0.85 + 0.15 * np.sin(2*np.pi*0.10*t_full)

# ---- Ghost kick — 90 BPM half-time -----------------------------------------
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
    kick[s:s+L] += 0.19 * env * np.sin(ph)

# ---- Synth-pluck shimmers at the layer seams — climbing the scale ----------
def pluck(freq, start_s, decay=0.55, amp=0.085):
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

# Climbing pitches: each layer seam lifts the note — the stack building up.
shimmer_targets = [2.90, 6.90, 10.90, 14.90]
shimmer_pitches = [392.00, 523.25, 659.25, 1046.50]  # G4 C5 E5 C6
mix_shimmer = np.zeros(N)
for st, fr in zip(shimmer_targets, shimmer_pitches):
    mix_shimmer += pluck(fr, st, decay=0.55, amp=0.085)

# ---- Filtered noise sweep — swell crested at the CTA opening (~15s) ---------
rng = np.random.default_rng(seed=61)
noise = rng.standard_normal(N) * 0.020
window = 35
noise_lp = np.convolve(noise, np.ones(window)/window, mode='same')
sweep_env = np.exp(-((t_full - 15.0) ** 2) / (2 * 3.5 ** 2))
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
    hat[s:s+L] += 0.019 * env * n_h

# ---- Mix --------------------------------------------------------------------
mixed = pad + kick + mix_shimmer + noise_layer + hat

# Master fade in / out
fi = int(1.0 * SR)
fo = int(2.5 * SR)
mixed[:fi]  *= np.linspace(0, 1, fi)
mixed[-fo:] *= np.linspace(1, 0, fo)

peak = np.max(np.abs(mixed))
if peak > 0:
    mixed = mixed / peak * 0.78

OUT = '/home/user/hyperframes-student-kit/video-projects/digiwell-ttw-replay/assets/music.wav'
sf.write(OUT, mixed, SR)
print(f"Wrote {DUR:.1f}s warm-electronic bed -> {OUT}")
