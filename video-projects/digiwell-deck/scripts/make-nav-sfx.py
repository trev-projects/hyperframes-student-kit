#!/usr/bin/env python3
"""Synthesize the presenter's navigation sounds into sfx/*.mp3.

`hyperframes present` plays sfx/advance.mp3, sfx/fragment.mp3, sfx/back.mp3 and
sfx/branch-enter.mp3 from the deck folder on navigation (missing files are
silently skipped). These are short, quiet and warm so they sit under a voice.
Stdlib-only synthesis to WAV, then ffmpeg encodes MP3. Deterministic.
"""
import math, struct, subprocess, wave
from pathlib import Path

SR = 44100
OUT = Path(__file__).resolve().parent.parent / "sfx"
OUT.mkdir(exist_ok=True)
_seed = 42

def noise():
    global _seed
    _seed = (1103515245 * _seed + 12345) & 0x7FFFFFFF
    return _seed / 0x3FFFFFFF - 1.0

def render(name, dur, fn, gain=0.5):
    n = int(SR * dur)
    buf = [fn(i / SR, dur) for i in range(n)]
    peak = max(abs(v) for v in buf) or 1.0
    wav = OUT / f"{name}.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(v / peak * gain * 32767)) for v in buf))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-b:a", "128k", str(OUT / f"{name}.mp3")], check=True)
    wav.unlink()
    print("wrote", name)

def whoosh(rev=False):
    lp = [0.0]
    def f(t, d):
        u = t / d
        u2 = 1 - u if rev else u
        lp[0] += (0.03 + 0.25 * math.sin(math.pi * u2) ** 2) * (noise() - lp[0])
        return lp[0] * math.sin(math.pi * u) ** 1.6
    return f

def tick(freq, decay):
    return lambda t, d: math.sin(2 * math.pi * freq * t) * math.exp(-t * decay)

def mix(*parts):
    return lambda t, d: sum(g * p(t, d) for g, p in parts)

render("advance", 0.34, mix((1.0, whoosh()), (0.35, tick(1400, 60))), gain=0.35)
render("fragment", 0.12, tick(1900, 45), gain=0.28)
render("back", 0.30, whoosh(rev=True), gain=0.3)
render("branch-enter", 0.9, lambda t, d: (math.sin(2 * math.pi * 880 * t) + 0.5 * math.sin(2 * math.pi * 1318.5 * t)) * math.exp(-t * 5), gain=0.3)
