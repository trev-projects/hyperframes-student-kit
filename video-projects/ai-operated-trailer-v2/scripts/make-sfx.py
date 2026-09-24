#!/usr/bin/env python3
"""Synthesize the trailer's sound design, sample-accurate to the cut times.

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
DUR = 16.0
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
    env = min(1.0, t / 0.8) * min(1.0, max(0.0, (DUR - t) / 1.2))
    trem = 0.85 + 0.15 * math.sin(2 * math.pi * 0.5 * t)
    buf[i] += 0.07 * env * trem * (
        math.sin(2 * math.pi * 110.0 * t)
        + 0.6 * math.sin(2 * math.pi * 164.81 * t + 0.4)
        + 0.4 * math.sin(2 * math.pi * 220.4 * t + 1.1))

# ---- S1 noise (0–3.4) ------------------------------------------------------
kick(0.10)
for k in range(1, 17):                                   # count-up ticks follow power3.out
    u = 1 - (1 - k / 16) ** (1 / 3)
    tick(0.15 + 1.0 * u, gain=0.16)
thump(1.12)
whoosh(1.48, 0.3, 0.3)
kick(1.84)
t = 1.86
while t < 2.56:                                          # scramble chatter
    tick(t, gain=0.12, freq=3400)
    t += 0.045

# ---- S2 signal (3.0–5.2) ---------------------------------------------------
whoosh(2.96)
sweep(3.55, 1.0, 300, 1200, 0.10)                        # scanner tone
tick(4.50, gain=0.2, freq=1800)

# ---- S3 turn (4.8–7.2) -----------------------------------------------------
sweep(4.30, 0.55, 180, 900, 0.16)                        # riser into the iris
whoosh(4.76, 0.5, 0.5)
kick(5.10)
for w in (0.52, 0.64, 0.84, 0.94, 1.04, 1.14):
    thump(4.8 + w, gain=0.32)

# ---- S4 inside (6.8–10.4) --------------------------------------------------
whoosh(6.78)
kick(7.05)
for t_in in (7.20, 8.32, 9.44):
    tick(t_in, gain=0.25, freq=1500)
    whoosh(t_in - 0.02, 0.22, 0.25)
for t_out in (8.16, 9.28):
    whoosh(t_out, 0.2, 0.22)

# ---- S5 CTA (10.0–16.0) ----------------------------------------------------
sweep(9.45, 0.55, 220, 1000, 0.14)
whoosh(9.98, 0.52, 0.5)
kick(10.26)
for i in range(10):
    tick(10.42 + i * 0.035 + 0.12, gain=0.10, freq=2200)
tick(10.95, gain=0.18, freq=1200)
for imp, g in ((11.17, 0.5), (11.39, 0.28), (11.50, 0.15)):
    thump(imp, gain=g)
chime(11.17)
for i in range(35):
    tick(11.55 + i * 0.024, gain=0.07, freq=3000)
thump(12.45, gain=0.35)

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
