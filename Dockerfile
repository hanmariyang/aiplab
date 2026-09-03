# AIP Lab 스튜디오 랜딩 — 정적 단일 페이지를 Caddy 로 서빙 (Railway).
# 빌드는 Railway 원격에서 수행(로컬 docker build 금지 — Mac mini 디스크 보호).
FROM caddy:2-alpine
# 주의: 제품 랜딩을 새로 만들면 아래 COPY 목록에 반드시 추가할 것.
# 빠뜨리면 배포는 성공하는데 그 경로만 404 가 난다 (planning 에서 실제로 겪음).
COPY Caddyfile /etc/caddy/Caddyfile
COPY index.html /srv/index.html
COPY README.md /srv/README.md
COPY img /srv/img
COPY working /srv/working
COPY grouping /srv/grouping
COPY sliding /srv/sliding
COPY applying /srv/applying
COPY planning /srv/planning
COPY blog /srv/blog
COPY sitemap.xml /srv/sitemap.xml
COPY robots.txt /srv/robots.txt
EXPOSE 8080
