---
title: Measure the slide, don't trust the AI
date: 2026.08.21
category: Build log
product: sliding
read: 5
excerpt: The model writes layout code; a render scan checks cropping, overlap and typesetting before you ever open the deck.
ccard_cta: See how →
cta_title: Make a deck with Sliding
---
Ask a model to design a slide and it will happily write layout code that looks fine and, once rendered, clips the title, overlaps two boxes, and pushes a bullet off the edge. The code reads well. The slide is broken. You only find out by looking.

## So look, automatically

Sliding renders every slide it generates and scans the result. It measures the actual pixels: is any text cropped, do elements overlap, is the type set inside its box. A slide that fails the scan gets fixed or flagged before it reaches you.

![The Sliding editor](../img/sliding-editor.jpg "Layout as code, checked by a render scan.")

The point is a small shift in trust. The AI is good at proposing a layout and bad at knowing whether it actually fits. So we don't ask it to grade its own work. We measure.

[[cta]]

## On your machine, on your subscription

Sliding runs on your local Claude subscription, so there are no per-slide credits to burn, and the deck stays on your disk. Generate, scan, fix, repeat, all without sending your slides to anyone.
