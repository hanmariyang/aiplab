# AIP Lab 스튜디오 랜딩 — 정적 단일 페이지를 Caddy 로 서빙 (Railway).
# 빌드는 Railway 원격에서 수행(로컬 docker build 금지 — Mac mini 디스크 보호).
FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
COPY index.html /srv/index.html
COPY README.md /srv/README.md
COPY img /srv/img
COPY working /srv/working
COPY grouping /srv/grouping
COPY blog /srv/blog
COPY sitemap.xml /srv/sitemap.xml
COPY robots.txt /srv/robots.txt
EXPOSE 8080
