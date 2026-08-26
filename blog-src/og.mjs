// OG 공유 카드 PNG 생성 — build.py 가 만든 blog/og/*.html 을 1200x630 PNG 로.
// 제품이 늘거나 커버 디자인 바뀔 때만 실행: node blog-src/og.mjs
// (일반 글 추가는 불필요 — 글은 제품 카드를 재사용)
import { chromium } from 'playwright';
import { glob } from 'fs/promises';
import path from 'path';
const OG = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'blog', 'og');
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
let n = 0;
for await (const f of glob(OG + '/*.html')) {
  await p.goto('file://' + f, { waitUntil: 'networkidle' });
  await p.waitForTimeout(500);
  const out = f.replace(/\.html$/, '.png');
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: 1200, height: 630 } });
  console.log('og →', path.basename(out)); n++;
}
await b.close();
console.log('done', n, 'cards');
