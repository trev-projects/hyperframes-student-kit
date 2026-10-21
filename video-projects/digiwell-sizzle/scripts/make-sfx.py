#!/usr/bin/env python3
"""Synthesize the sizzle reel's sound design, sample-accurate to the cut times.

Pure standard library (no numpy). Deterministic: the noise source is a fixed-seed
LCG, so every run writes a byte-identical assets/sfx.wav.

Event times are GLOBAL seconds and mirror index.html + the compositions'
timelines. If you retime a beat, retime its event here too.
"""
import math
import struct
import wave
from array import array
from pathlib import Path

SR = 44100
DUR = 34.0
N = int(SR * DUR)
buf = array("f", [0.0]) * N

_seed = 1234567
def noise():
    global _seed
    _seed = (1103515245 * _seed + 12345) & 0x7FFFFFFF
    return _seed / 0x3FFFFFFF - 1.0

def add(start, length, fn):
    i0 = int(start * SR)
    for k in range(int(length * SR)):
        i = i0 + k
        if 0 <= i < N:
            buf[i] += fn(k / SR)

def kick(t0, gain=0.9, base=48):
    ph = [0.0]
    def f(t):
        freq = base + 130 * math.exp(-t * 32)
        ph[0] += 2 * math.pi * freq / SR
        return gain * math.sin(ph[0]) * math.exp(-t * 8.5)
    add(t0, 0.45, f)

def thump(t0, gain=0.45):
    kick(t0, gain, base=85)

def tick(t0, gain=0.22, freq=2600):
    add(t0, 0.035, lambda t: gain * (math.sin(2 * math.pi * freq * t) * 0.7 + noise() * 0.3) * math.exp(-t * 140))

def whoosh(t0, dur=0.42, gain=0.42):
    lp = [0.0]
    def f(t):
        u = t / dur
        cutoff = 0.02 + 0.28 * math.sin(math.pi * u)      # sweeps open then closed
        lp[0] += cutoff * (noise() - lp[0])
        return gain * lp[0] * 3.0 * math.sin(math.pi * u) ** 1.5
    add(t0, dur, f)

def sweep(t0, dur, f0, f1, gain):
    ph = [0.0]
    def f(t):
        u = t / dur
        freq = f0 * (f1 / f0) ** u
        ph[0] += 2 * math.pi * freq / SR
        env = (u ** 2) * (1 - max(0.0, (u - 0.92) / 0.08))
        return gain * env * (math.sin(ph[0]) + 0.15 * noise())
    add(t0, dur, f)

def chime(t0, gain=0.32):
    parts = [(880.0, 1.0), (1318.5, 0.55), (1760.0, 0.3)]
    add(t0, 1.8, lambda t: gain * sum(a * math.sin(2 * math.pi * fr * t) for fr, a in parts) * math.exp(-t * 2.6))

# ---- Warm pad bed (whole piece) -------------------------------------------
for i in range(N):
    t = i / SR
    env = min(1.0, t / 1.0) * min(1.0, max(0.0, (DUR - t) / 1.6))
    trem = 0.85 + 0.15 * math.sin(2 * math.pi * 0.4 * t)
    buf[i] += 0.06 * env * trem * (
        math.sin(2 * math.pi * 98.0 * t)
        + 0.6 * math.sin(2 * math.pi * 146.8 * t + 0.4)
        + 0.4 * math.sin(2 * math.pi * 196.4 * t + 1.1))

# ---- z1 hook (0-5.8) --------------------------------------------------------
for w in range(4):
    thump(0.30 + w * 0.07, gain=0.18)
for t0 in (0.90, 1.20, 1.50):                            # list, newsletter, sequence cards
    tick(t0, gain=0.24, freq=1800); tick(t0 + 0.07, gain=0.18, freq=2400)
t, step = 2.15, 0.16                                     # day counter, accelerating
while t < 3.45:
    tick(t, gain=0.10, freq=3000)
    t += step; step = max(0.05, step * 0.86)
for w in range(3):
    thump(3.20 + w * 0.06, gain=0.2)
kick(3.55, gain=0.7)

# ---- z2 thesis (5.4-9.6) ----------------------------------------------------
sweep(4.95, 0.45, 180, 800, 0.12)
whoosh(5.35, 0.5, 0.5)
kick(5.65)
for w in range(5):
    tick(5.85 + w * 0.06, gain=0.1, freq=2200)
whoosh(6.55, 0.22, 0.35)                                 # strike-through
for w in range(4):
    tick(7.0 + w * 0.07, gain=0.1, freq=2200)
thump(7.5, gain=0.5); chime(7.55, gain=0.16)

# ---- z3 services (9.2-15.6) -------------------------------------------------
whoosh(9.15)
kick(9.45)
for i in range(4):                                       # four service cards deal in
    thump(10.2 + i * 0.15, gain=0.28); tick(10.22 + i * 0.15, gain=0.14, freq=1700)
for i in range(4):                                       # highlight walks the services
    tick(11.1 + i * 0.35, gain=0.18, freq=2600)
thump(12.6, gain=0.4)                                    # "Start with the one that matters most."
chime(12.95, gain=0.16)

# ---- z4 how we work (15.2-25.6) ---------------------------------------------
whoosh(15.15)
kick(15.45)
for t0 in (15.65, 18.1, 20.55, 23.0):                    # each step lands
    thump(t0, gain=0.42); whoosh(t0 - 0.28, 0.25, 0.22)
for t0 in (16.2, 16.6, 17.0):                            # chat bubbles
    tick(t0, gain=0.16, freq=1900)
for t0 in (18.72, 18.97, 19.22, 20.82, 21.07, 21.32):    # ticks
    tick(t0, gain=0.18, freq=2300)
kick(21.95, gain=0.75)                                   # SIGNED OFF stamp
whoosh(23.95, 0.7, 0.3)                                  # handover slide
chime(24.6, gain=0.14)

# ---- z5 commitments (25.2-28.8) ---------------------------------------------
whoosh(25.15, 0.48, 0.5)
for t0 in (25.65, 26.15, 26.65, 27.15):
    kick(t0, gain=0.55)

# ---- z6 CTA (28.4-34) ------------------------------------------------------
sweep(27.85, 0.55, 200, 900, 0.12)
whoosh(28.35, 0.5, 0.45)
kick(28.65)
tick(29.55, gain=0.18, freq=1400)
thump(29.9, gain=0.4)
chime(30.0, gain=0.3)

# ---- Normalize + write -----------------------------------------------------
peak = max(abs(v) for v in buf) or 1.0
scale = 0.89 / peak
out = Path(__file__).resolve().parent.parent / "assets" / "sfx.wav"
with wave.open(str(out), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, v * scale)) * 32767)) for v in buf))
print(f"wrote {out} ({DUR}s, peak normalized from {peak:.2f})")
