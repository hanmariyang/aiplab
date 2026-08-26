# AIP Lab 블로그 글 쓰는 법

`aiplab.kr/blog` 은 **정적 생성기**로 굴러간다. 글은 마크다운 파일 하나, 빌드하면 HTML 이 나오고, 커밋+배포하면 올라간다. 서버도 DB 도 없다.

> 언제든 "블로그에 ○○ 글 써줘 / 새 글 추가해줘" 라고 하면 이 문서 절차대로 처리한다.

## 3단계 요약

```
1. blog-src/posts/2026-09-01-my-slug.md  파일 작성   (아래 양식)
2. python3 blog-src/build.py                          (→ blog/ 재생성)
3. git add -A && git commit && railway up -s aiplab-web   (aiplab.kr 반영)
```

`railway up` 대신 push 만 해도 GitHub Pages 미러(`hanmariyang.github.io/aiplab/blog/`)에는 뜨지만, **aiplab.kr(운영)은 Railway 라 `railway up` 이 필요**하다. (Pages 는 빌드 큐가 자주 밀린다.)

## 글 파일

- 위치: `blog-src/posts/`
- 이름: **`YYYY-MM-DD-slug.md`** (앞 11자 = 날짜, 나머지가 URL slug). 예: `2026-09-01-drafting-v2.md` → `aiplab.kr/blog/drafting-v2.html`
- 목록은 **날짜 내림차순**, 맨 위 글이 자동으로 **featured**(대형 카드).

## 프론트매터 (파일 맨 위)

```
---
title: 제목 (콜론 있어도 됨)
date: 2026.09.01
category: Release        # Release / Build log / Note / Preview 등 자유
product: drafting        # 색·마스코트·커버·CTA 결정 (아래 표). 없으면 studio
read: 4                  # 읽기 분(숫자)
excerpt: 목록·상단에 쓰이는 한두 문장 요약.
ccard_cta: Try it →      # 목록 카드 하단 라이트 CTA 문구 (선택)
cta_title: 큰 엔드 CTA 제목 (선택, studio 글은 무시)
# views: 1200            # (선택) 넣으면 조회수 표시. 안 넣으면 숨김 — 허수 금지
---
```

## product 값 (제품 레지스트리)

`product:` 하나로 그 글의 **액센트 색·커버 이미지·다운로드/저장소 링크·CTA** 가 전부 자동 세팅된다. `blog-src/build.py` 의 `PRODUCTS` 에 정의.

| product | 색 | 커버 | CTA |
|---|---|---|---|
| `working` | 코랄 | Worky 마스코트 | Download for macOS (dmg) |
| `drafting` | 그린 | 제품 스크린샷 | Try Drafting (랜딩) |
| `coxpit` | 민트 | 제품 스크린샷 | Get Coxpit (랜딩) |
| `sliding` | 블루 | 제품 스크린샷 | See Sliding (랜딩) |
| `lighting` | 앰버 | 제품 스크린샷 | Get notified (building) |
| `studio` | 그레이 | 5색 그라데이션 | (제품 CTA 없음) |

새 제품이 생기면 `PRODUCTS` 에 항목 추가(색 클래스 `g/b/t/a/c/n`, 커버 배경, 마스코트/스크린샷 파일명, 링크, specs).

## 마크다운에서 쓸 수 있는 것

- `## 소제목` , `### 더 작은 제목`
- 문단: 빈 줄로 구분
- `> 인용` (코랄 왼쪽 선 pull-quote)
- 코드블록: ```` ``` ```` 로 감싸기. `#` 로 시작하는 줄은 회색 주석으로 표시됨
- 이미지: `![대체텍스트](../img/파일.png "캡션")` — 캡션은 선택. 이미지는 `../img/` 에 둔다(제품 스크린샷 재사용)
- 목록: `- 항목`
- 인라인: `**볼드**`, `` `코드` ``, `[링크](주소)`
- **`[[cta]]`** — 이 줄을 넣으면 그 자리에 **제품 다운로드 콜아웃 카드**(마스코트+이름+버튼)가 들어간다. 글 하나에 한 번 권장.

엔드 CTA(큰 다운로드 박스)와 관련글은 **자동 추가**된다(studio 글 제외).

## 규칙

- ⚠️ **em-dash( — ) 금지.** 쉼표·마침표·콜론·중점(·)으로. (의뢰자 규칙, 공개 웹 카피 전반)
- **허수 금지.** 조회수 등 실측 안 되는 숫자는 지어내지 않는다. (조회수는 카운터 붙이기 전까지 숨김)
- 실제 내용으로. 톤은 담백하게, 제품과 연결.
- 이미지 대체텍스트 꼭.

## 아직 백엔드 필요 (지금은 미동작)

- **조회수**: `views` 슬롯은 있으나 자동 집계 없음 → GoatCounter(무료 스크립트) 또는 aiplab 백엔드 카운터 붙이면 표시.
- **구독**: 이메일 폼 UI 만. Buttondown/Resend 등 연동해야 실제 수집.

## 파일 지도

```
blog-src/
  build.py        생성기 (제품 레지스트리 PRODUCTS 여기)
  blog.css        공유 스타일 (디자인 수정은 여기)
  WRITING.md      이 문서
  posts/*.md      글 소스 (여기에 새 글 추가)
blog/             생성물 (커밋 대상, Railway 가 서빙) — 직접 수정 금지
```
