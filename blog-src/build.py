#!/usr/bin/env python3
"""
AIP Lab 블로그 정적 생성기 — 마크다운 글 → 정적 HTML(목록·글·RSS).
빌드 의존성 0(순수 표준 라이브러리). 로컬에서 돌리고 산출물(../blog/)을 커밋한다.

사용:
  python3 blog-src/build.py
  → ../blog/index.html · ../blog/<slug>.html · ../blog/rss.xml 생성

글 추가: blog-src/posts/<yyyy-mm-dd>-<slug>.md 만들고 다시 실행.
경로는 전부 상대(../img ../working ..)라 aiplab.kr(루트)·github.io/aiplab(서브패스) 둘 다 동작.
"""
import os, re, glob, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'blog'))
POSTS_DIR = os.path.join(HERE, 'posts')
SITE = 'https://aiplab.kr'

# 제품 레지스트리 — 색·마스코트·커버·CTA 를 product 하나로 결정한다.
DL_WORKING = 'https://github.com/hanmariyang/aiplab/releases/download/working-v0.1.0/Working-0.1.0-arm64.dmg'
PRODUCTS = {
    'working':  dict(name='Working', cls='c', cover_bg='linear-gradient(140deg,#FDE8E0,#F6C3B2)',
                     mascot='worky.png', shot='working-accept.jpg', version='v0.1.0',
                     landing='../working/', cta='Download for macOS ↓', cta_href=DL_WORKING,
                     repo='https://github.com/hanmariyang/working', specs='Apple Silicon · macOS 12+ · 107MB',
                     blurb='A free macOS app for planning. Signed, notarized, and it runs entirely on your machine.'),
    'drafting': dict(name='Drafting', cls='g', cover_bg='#E4F3EE',
                     mascot=None, shot='drafting-doc.png', version='v1.6.2',
                     landing='https://hanmariyang.github.io/drafting/', cta='Try Drafting ↗', cta_href='https://hanmariyang.github.io/drafting/',
                     repo='https://github.com/hanmariyang/drafting', specs='npx · docker · MIT',
                     blurb='An AI planning workspace. Runs from your terminal, keeps every document in a local file.'),
    'coxpit':   dict(name='Coxpit', cls='t', cover_bg='#0d1117',
                     mascot=None, shot='coxpit-board.png', version='v5.3.1',
                     landing='https://hanmariyang.github.io/coxpit-oss/', cta='Get Coxpit ↗', cta_href='https://hanmariyang.github.io/coxpit-oss/',
                     repo='https://github.com/hanmariyang/coxpit-oss', specs='npx · docker · MIT',
                     blurb='A self-hosted cockpit for a fleet of AI coding agents on your own machines.'),
    'sliding':  dict(name='Sliding', cls='b', cover_bg='#EAEDFB',
                     mascot=None, shot='sliding-editor.jpg', version='v0.1.1',
                     landing='https://hanmariyang.github.io/sliding/', cta='See Sliding ↗', cta_href='https://hanmariyang.github.io/sliding/',
                     repo='https://github.com/hanmariyang/sliding', specs='local Claude · MIT',
                     blurb='An AI slide studio that writes layout code, then measures the result with a render scan.'),
    'lighting': dict(name='Lighting', cls='a', cover_bg='#FBEFD8',
                     mascot=None, shot='lighting-workspace.png', version='building',
                     landing=None, cta='Get notified →', cta_href='https://github.com/hanmariyang',
                     repo='https://github.com/hanmariyang', specs='in development',
                     blurb='An AI e-book studio, in the making. Interview to chapter drafts to EPUB3.'),
    'studio':   dict(name='AIP Lab', cls='n', cover_bg='linear-gradient(120deg,#E4F3EE,#EAEDFB,#E1F4EF,#FBEFD8,#FDE8E0)',
                     mascot='dots', shot=None, version='',
                     landing='../index.html', cta='See the tools ↓', cta_href='../index.html#family',
                     repo='https://github.com/hanmariyang', specs='self-hostable · open source',
                     blurb='Small, self-hostable tools from a one-person studio.'),
}

# ---------- 프론트매터 + 마크다운 ----------
def parse(text):
    meta, body = {}, text
    if text.startswith('---'):
        _, fm, body = text.split('---', 2)
        for line in fm.strip().splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"').strip()
    return meta, body.strip()

def esc(s):
    return html.escape(s, quote=False)

def inline(t):
    t = re.sub(r'`([^`]+)`', lambda m: '<code>' + esc(m.group(1)) + '</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a class="inl" href="\2">\1</a>', t)
    return t

def img_block(s):
    m = re.match(r'!\[([^\]]*)\]\(([^) ]+)(?:\s+"([^"]*)")?\)', s)
    if not m:
        return ''
    alt, src, cap = m.group(1), m.group(2), m.group(3)
    fig = '<figure><img src="%s" alt="%s"/>' % (src, esc(alt))
    if cap:
        fig += '<figcaption>%s</figcaption>' % esc(cap)
    return fig + '</figure>'

def callout(prod):
    p = PRODUCTS[prod]
    masc = '<img class="cm" src="../img/%s" alt=""/>' % p['mascot'] if p.get('mascot') and p['mascot'] != 'dots' else ''
    ver = '<span class="cv">%s</span>' % p['version'] if p['version'] else ''
    return ('<aside class="callout">%s<div class="ct"><div class="cn">%s %s</div>'
            '<div class="cd">%s</div><div class="cs">%s</div></div>'
            '<a class="btn" href="%s">%s</a></aside>') % (
        masc, p['name'], ver, esc(p['blurb']), esc(p['specs']).upper(), p['cta_href'], p['cta'])

def md(body, prod):
    lines = body.split('\n')
    out, para, i = [], [], 0
    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>'); para.clear()
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('```'):
            flush(); code = []; i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            i += 1
            rows = []
            for c in code:
                e = esc(c)
                rows.append('<span class="c">' + e + '</span>' if c.strip().startswith('#') else e)
            out.append('<pre>' + '\n'.join(rows) + '</pre>'); continue
        if s == '':
            flush(); i += 1; continue
        if s == '[[cta]]':
            flush(); out.append(callout(prod)); i += 1; continue
        if s.startswith('## '):
            flush(); out.append('<h2>' + inline(s[3:]) + '</h2>'); i += 1; continue
        if s.startswith('### '):
            flush(); out.append('<h3>' + inline(s[4:]) + '</h3>'); i += 1; continue
        if s.startswith('> '):
            flush(); q = [s[2:]]; i += 1
            while i < len(lines) and lines[i].strip().startswith('> '):
                q.append(lines[i].strip()[2:]); i += 1
            out.append('<blockquote>' + inline(' '.join(q)) + '</blockquote>'); continue
        if s.startswith('!['):
            flush(); out.append(img_block(s)); i += 1; continue
        if s.startswith('- '):
            flush(); it = [s[2:]]; i += 1
            while i < len(lines) and lines[i].strip().startswith('- '):
                it.append(lines[i].strip()[2:]); i += 1
            out.append('<ul>' + ''.join('<li>' + inline(x) + '</li>' for x in it) + '</ul>'); continue
        para.append(s); i += 1
    flush()
    return '\n'.join(out)

EYE = ('<svg class="eye" viewBox="0 0 16 16"><path d="M1 8s2.5-4.5 7-4.5S15 8 15 8s-2.5 4.5-7 4.5S1 8 1 8Z"/>'
       '<circle cx="8" cy="8" r="1.8"/></svg>')

def cover(p, cls_extra=''):
    """product 로 커버 HTML 생성 — 스크린샷 있으면 shot, 없으면 마스코트/도트."""
    if p.get('shot'):
        return ('<div class="cover shot %s" style="--cg:%s"><img src="../img/%s" alt=""/></div>'
                % (cls_extra, p['cover_bg'], p['shot']))
    if p.get('mascot') == 'dots':
        return ('<div class="cover masc %s" style="--cg:%s"><span class="cdots"><span class="dots">'
                '<i class="dg"></i><i class="db"></i><i class="dt"></i><i class="da"></i><i class="dc"></i>'
                '</span></span></div>' % (cls_extra, p['cover_bg']))
    if p.get('mascot'):
        return ('<div class="cover masc %s" style="--cg:%s"><img src="../img/%s" alt=""/></div>'
                % (cls_extra, p['cover_bg'], p['mascot']))
    return '<div class="cover" style="--cg:%s"></div>' % p['cover_bg']

def views_html(meta):
    v = meta.get('views')
    return ('<span class="views">%s%s</span>' % (EYE, v)) if v else ''

# ---------- 로드 ----------
def load_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')), reverse=True):
        meta, body = parse(open(path, encoding='utf-8').read())
        slug = os.path.basename(path)[11:-3]  # yyyy-mm-dd- 제거, .md 제거
        meta['slug'] = slug
        meta['body'] = body
        prod = meta.get('product', 'studio')
        meta['p'] = PRODUCTS.get(prod, PRODUCTS['studio'])
        meta['prod'] = prod if prod in PRODUCTS else 'studio'
        posts.append(meta)
    return posts

# ---------- 공용 셸 ----------
CSS = open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read()
HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
        '<meta name="viewport" content="width=device-width, initial-scale=1"/>'
        '<title>__TITLE__</title>'
        '<meta name="description" content="__DESC__"/>'
        '<meta property="og:title" content="__TITLE__"/><meta property="og:description" content="__DESC__"/>'
        '<meta property="og:type" content="__OGTYPE__"/>'
        '<link rel="alternate" type="application/rss+xml" title="AIP Lab" href="rss.xml"/>'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E'
        '%3Ccircle cx=\'11\' cy=\'11\' r=\'5\' fill=\'%230E7B62\'/%3E%3Ccircle cx=\'21\' cy=\'11\' r=\'5\' fill=\'%233B5BDB\'/%3E'
        '%3Ccircle cx=\'11\' cy=\'21\' r=\'5\' fill=\'%2312B39A\'/%3E%3Ccircle cx=\'21\' cy=\'21\' r=\'5\' fill=\'%23C77C1A\'/%3E%3C/svg%3E"/>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>'
        '<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>'
        '<style>' + CSS + '</style></head><body>')
MARK = ('<span class="dots"><i class="dg"></i><i class="db"></i><i class="dt"></i><i class="da"></i><i class="dc"></i></span> AIP Lab')
FOOT = ('<footer><div class="foot"><span class="k"><span class="dots"><i class="dg"></i><i class="db"></i>'
        '<i class="dt"></i><i class="da"></i><i class="dc"></i></span> &nbsp;© 2026 AIP LAB</span>'
        '<nav class="n"><a href="rss.xml">rss</a><a href="https://github.com/hanmariyang">github.com/hanmariyang</a>'
        '<a href="https://aiplab.kr">aiplab.kr</a></nav></div></footer></body></html>')

def head(title, desc, ogtype='website'):
    return HEAD.replace('__TITLE__', esc(title)).replace('__DESC__', esc(desc)).replace('__OGTYPE__', ogtype)

# ---------- 목록 ----------
def render_list(posts):
    feat = posts[0]
    rest = posts[1:]
    fp = feat['p']
    fbtns = '<a class="btn" href="%s.html">Read the post →</a>' % feat['slug']
    if fp.get('cta_href') and feat['prod'] != 'studio':
        fbtns += '<a class="btn g" href="%s">%s</a>' % (fp['cta_href'], fp['cta'])
    featured = (
        '<div class="feat"><a class="cover masc" style="--cg:%s" href="%s.html"><span class="big">&#9654; Featured</span>'
        '<img src="../img/%s" alt=""/></a><div class="fx"><div class="fmeta"><span class="tag %s"><span class="lv"></span>%s · %s</span>'
        '<span class="meta">%s<span>%s</span></span></div><h2>%s</h2><p>%s</p>'
        '<div style="display:flex;gap:10px;flex-wrap:wrap">%s</div></div></div>'
    ) % (fp['cover_bg'], feat['slug'], fp['mascot'] if fp.get('mascot') and fp['mascot'] != 'dots' else 'worky.png',
         fp['cls'], esc(feat.get('category', 'Note')), fp['name'], views_html(feat), feat.get('date', ''),
         esc(feat['title']), esc(feat.get('excerpt', '')), fbtns)

    cards = []
    for m in rest:
        p = m['p']
        cta_lite = esc(m.get('ccard_cta', 'Read →'))
        cards.append(
            '<a class="pcard %s" href="%s.html">%s<div class="cmeta"><span class="tag %s"><span class="lv"></span>%s · %s</span>'
            '<span class="meta">%s</span></div><h4>%s</h4><p>%s</p>'
            '<div class="foot"><span class="cta-lite">%s</span><span class="meta">%s min</span></div></a>'
            % (p['cls'], m['slug'], cover(p), p['cls'], esc(m.get('category', 'Note')), p['name'],
               views_html(m), esc(m['title']), esc(m.get('excerpt', '')), cta_lite, esc(str(m.get('read', '3')))))

    nav = ('<header><div class="bar"><a class="mark" href="../index.html">' + MARK + '</a>'
           '<nav class="n"><a href="../index.html#family" class="hs">the tools</a><a href="index.html" class="on">blog</a>'
           '<a href="../index.html#about" class="hs">about</a><a href="../index.html#family" class="navcta">Get the tools ↓</a></nav></div></header>')
    body = (
        '<div class="wrap"><section class="top"><div class="eyebrow"><span class="pr">&gt;</span> BLOG</div>'
        '<h1>Notes from the workshop.</h1><p class="sub">Build logs, release notes, and the thinking behind small '
        'self-hostable tools, with the products they are about.</p></section>' + featured +
        '<div class="sech"><h3>Latest</h3><a class="k" href="index.html">All posts</a></div>'
        '<div class="grid">' + ''.join(cards) + '</div>'
        '<section class="cta"><div><h3>New tools, in your inbox.</h3>'
        '<p>A short email when something ships or a build log goes up. No spam, unsubscribe any time.</p></div>'
        '<div><form class="subf" onsubmit="return false"><input type="email" placeholder="you@example.com"/>'
        '<button>Subscribe</button></form><div class="subnote">or follow on GitHub · RSS</div></div></section></div>')
    return head('Blog · AIP Lab', 'Build logs and release notes from AIP Lab, a one-person studio building small self-hostable tools.') + nav + body + FOOT

# ---------- 글 ----------
def render_post(m, allposts):
    p = m['p']
    body = md(m['body'], m['prod'])
    # 커버(히어로) — 마스코트면 그라데이션, 아니면 스크린샷
    if p.get('mascot') and p['mascot'] != 'dots':
        hero = '<div class="hero-cover"><div class="cv" style="background:%s"><img src="../img/%s" alt=""/></div></div>' % (p['cover_bg'], p['mascot'])
    elif p.get('shot'):
        hero = '<div class="hero-cover"><div class="cv shot"><img src="../img/%s" alt=""/></div></div>' % p['shot']
    else:
        hero = '<div class="hero-cover"><div class="cv" style="background:%s"></div></div>' % p['cover_bg']

    # 엔드 CTA
    endcta = ''
    if m['prod'] != 'studio':
        endcta = (
            '<div class="endcta"><div class="box"><h3>%s</h3><p>%s</p><div class="row">'
            '<a class="btn d" href="%s">%s</a>'
            '<a class="btn g" style="color:#fff;border-color:#3a3a36" href="%s">&#9733; Star on GitHub</a></div>'
            '<div class="fine">%s</div></div></div>'
        ) % (esc(m.get('cta_title', 'Try ' + p['name'])), esc(p['blurb']), p['cta_href'], p['cta'], p['repo'], esc(p['specs']).upper())

    # 관련 글(자기 제외 최대 3)
    rel = [x for x in allposts if x['slug'] != m['slug']][:3]
    rc = []
    for x in rel:
        xp = x['p']
        rc.append('<a class="rc" href="%s.html">%s<h4>%s</h4><div class="rm">%s · %s · %s min</div></a>'
                  % (x['slug'], cover(xp), esc(x['title']), esc(x.get('category', 'Note')), xp['name'], esc(str(x.get('read', '3')))))
    related = '<div class="related"><div class="k">Keep reading</div><div class="rgrid">' + ''.join(rc) + '</div></div>'

    nav = ('<header><div class="bar"><a class="mark" href="../index.html">' + MARK + '</a>'
           '<nav class="n"><a href="index.html" class="on">blog</a><a href="%s" class="navcta">%s</a></nav></div></header>'
           % (p['cta_href'] if m['prod'] != 'studio' else '../index.html#family', p['cta'] if m['prod'] != 'studio' else 'Get the tools ↓'))

    art = (
        '<div class="head"><a class="back" href="index.html">← Notes</a>'
        '<div class="hmeta"><span class="tag %s"><span class="lv"></span>%s · %s</span>'
        '<span class="meta">%s<span>%s</span><span>%s min read</span></span></div>'
        '<h1>%s</h1><p class="lead">%s</p>'
        '<div class="byline"><span class="who"><span class="av"></span> %s</span>'
        '<span class="share"><a href="#">X</a><a href="#">in</a><a href="#">↗</a></span></div></div>'
    ) % (p['cls'], esc(m.get('category', 'Note')), p['name'], views_html(m), m.get('date', ''),
         esc(str(m.get('read', '3'))), esc(m['title']), esc(m.get('excerpt', '')), esc(m.get('author', 'hanmariyang')))

    return (head(m['title'] + ' · AIP Lab Blog', m.get('excerpt', ''), 'article') + nav + art + hero +
            '<article class="art"><div class="body">' + body + '</div></article>' + endcta + related + FOOT)

# ---------- RSS ----------
def render_rss(posts):
    items = []
    for m in posts:
        link = '%s/blog/%s.html' % (SITE, m['slug'])
        items.append('<item><title>%s</title><link>%s</link><guid>%s</guid>'
                     '<pubDate>%s</pubDate><description>%s</description></item>'
                     % (esc(m['title']), link, link, m.get('date', ''), esc(m.get('excerpt', ''))))
    return ('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
            '<title>AIP Lab</title><link>%s/blog/</link>'
            '<description>Build logs and release notes from AIP Lab.</description>%s</channel></rss>'
            % (SITE, ''.join(items)))

# ---------- 실행 ----------
def main():
    os.makedirs(OUT, exist_ok=True)
    posts = load_posts()
    if not posts:
        print('글이 없습니다: blog-src/posts/*.md'); return
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(render_list(posts))
    for m in posts:
        open(os.path.join(OUT, m['slug'] + '.html'), 'w', encoding='utf-8').write(render_post(m, posts))
    open(os.path.join(OUT, 'rss.xml'), 'w', encoding='utf-8').write(render_rss(posts))
    print('생성 완료: %d 글 → %s' % (len(posts), OUT))
    for m in posts:
        print('  ·', m['slug'], '(%s)' % m.get('category', ''))

if __name__ == '__main__':
    main()
