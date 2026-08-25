# AIP Lab

**Small software you run yourself.** A one-person studio building self-hostable, open-source tools — the AI writes the first draft; the file never leaves your machine.

**Live:** https://aiplab.kr  ·  https://hanmariyang.github.io/aiplab/

Each tool has its own mascot, its own colour, its own repo — one family, one workshop.

## Catalog

| # | Tool | What it does | Run | Status |
|---|------|--------------|-----|--------|
| `AIP·001` | **[Drafting](https://github.com/hanmariyang/drafting)** | AI planning workspace. Idea interview → PRD, feature spec, IA. Every AI sentence is a suggestion; only what you accept becomes the document. | `npx @hanmariyang/drafting serve` | live |
| `AIP·002` | **[Sliding](https://github.com/hanmariyang/sliding)** | AI slide studio on your local Claude subscription. AI writes layout code per slide; a render scan measures cropping, overlap and typesetting. | `git clone` | live |
| `AIP·003` | **[Coxpit](https://github.com/hanmariyang/coxpit-oss)** | Self-hosted cockpit for a fleet of AI coding agents across your own machines. Parallel worktree runs, live board, compare & merge, web terminal. | `npx coxpit` | live |
| `AIP·004` | **Lighting** | AI e-book studio. Interview → AI chapter drafts → edit & cover → EPUB3 / PDF export (validated). Same interview → draft → yours flow. | — | building |

*Drafting, Sliding and Lighting are the `-ing` family — software in the present tense, always being made. Coxpit runs the machines that make the rest.*

## This repo

A static, single-page studio landing (`index.html` + `img/`, no build). Served two ways from the same repo: **Railway** (Caddy container → `aiplab.kr`) and **GitHub Pages** (`hanmariyang.github.io/aiplab`). Built by [hanmariyang](https://github.com/hanmariyang).
