#!/usr/bin/env node
// Export the deck as shareable files (run from the project folder):
//
//   exports/slides/NN.png                 one still per presenter stop (1920x1080)
//   exports/digiwell-deck.pdf             one page per SLIDE (its final build state)
//   exports/digiwell-deck-walkthrough.mp4 autoplay version: every transition plays,
//                                         then holds on each stop so it reads
//
// Usage:
//   node scripts/export.mjs                 render standard quality, then export
//   node scripts/export.mjs --skip-render   reuse renders/deck.mp4
//
// Needs ffmpeg, plus Playwright for the PDF (`npm install` at the workspace root —
// it's a devDependency there). Set CHROMIUM_PATH to use a specific browser.

import { execFileSync } from 'node:child_process';
import { readFileSync, mkdirSync, writeFileSync, existsSync, rmSync } from 'node:fs';
import { resolve } from 'node:path';
import { createRequire } from 'node:module';

const FPS = 30;
const HOLD = 2.5;        // seconds held on each slide's final stop
const HOLD_BUILD = 1.2;  // seconds held on intermediate build steps
const HOLD_LAST = 4.0;   // closing slide
const SRC = 'renders/deck.mp4';

const run = (cmd, args) => execFileSync(cmd, args, { stdio: ['ignore', 'inherit', 'inherit'] });

if (!process.argv.includes('--skip-render')) {
  run('npx', ['hyperframes', 'render', '--quality', 'standard', '--output', SRC]);
}
if (!existsSync(SRC)) { console.error(`missing ${SRC} — run without --skip-render`); process.exit(1); }

const html = readFileSync('index.html', 'utf8');
const island = JSON.parse(html.match(/application\/hyperframes-slideshow\+json">([\s\S]*?)<\/script>/)[1]);
// Every stop, tagged with whether it is the final build state of its slide.
const stops = island.slides.flatMap((s, si) => s.fragments.map((t, fi) => ({
  t, frame: Math.floor(t * FPS), slide: si, last: fi === s.fragments.length - 1
})));

// 1 — stills at the exact frame the presenter parks on
rmSync('exports', { recursive: true, force: true });
mkdirSync('exports/slides', { recursive: true });
stops.forEach((s, i) => {
  const out = `exports/slides/${String(i + 1).padStart(2, '0')}.png`;
  run('ffmpeg', ['-y', '-loglevel', 'error', '-i', SRC,
    '-vf', `select=eq(n\\,${s.frame})`, '-vsync', '0', '-frames:v', '1', out]);
  s.png = out;
});
console.log(`stills: ${stops.length}`);

// 2 — walkthrough: play each transition, then freeze on the stop
const parts = [];
let prev = 0;
stops.forEach((s, i) => {
  const end = (s.frame + 1) / FPS;
  const hold = i === stops.length - 1 ? HOLD_LAST : s.last ? HOLD : HOLD_BUILD;
  parts.push(`[0:v]trim=start=${prev.toFixed(4)}:end=${end.toFixed(4)},setpts=PTS-STARTPTS,` +
    `tpad=stop_mode=clone:stop_duration=${hold}[v${i}]`);
  prev = end;
});
const graph = parts.join(';') + ';' + stops.map((_, i) => `[v${i}]`).join('') +
  `concat=n=${stops.length}:v=1:a=0[out]`;
run('ffmpeg', ['-y', '-loglevel', 'error', '-i', SRC, '-filter_complex', graph, '-map', '[out]',
  '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
  'exports/digiwell-deck-walkthrough.mp4']);
console.log('walkthrough: exports/digiwell-deck-walkthrough.mp4');

// 3 — PDF: one page per slide, using each slide's final build state
let chromium;
try {
  const req = createRequire(resolve('package.json'));
  ({ chromium } = req('playwright'));
} catch {
  console.warn('PDF skipped: Playwright not found (run `npm install` at the workspace root).');
  process.exit(0);
}
const pages = stops.filter((s) => s.last).map((s) =>
  `<section><img src="data:image/png;base64,${readFileSync(s.png).toString('base64')}"></section>`).join('');
writeFileSync('exports/.pdf.html', `<!doctype html><html><head><style>
  @page { size: 1920px 1080px; margin: 0; }
  html, body { margin: 0; }
  section { width: 1920px; height: 1080px; page-break-after: always; overflow: hidden; }
  section:last-child { page-break-after: auto; }
  img { display: block; width: 1920px; height: 1080px; }
</style></head><body>${pages}</body></html>`);
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage();
await page.goto('file://' + resolve('exports/.pdf.html'));
await page.pdf({ path: 'exports/digiwell-deck.pdf', width: '1920px', height: '1080px', printBackground: true });
await browser.close();
rmSync('exports/.pdf.html');
console.log(`pdf: exports/digiwell-deck.pdf (${stops.filter((s) => s.last).length} pages)`);
