---
title: "The blunt read: senior taste, junior hands, unusual speed"
date: 2026.08.28
category: Outside read
product: studio
read: 5
excerpt: We ran the experiment again with a different model and asked it to be a hiring manager, not a fan. It was. Part two of a short series where we hand the whole studio to an AI, cold, and publish whatever it says back, kind or not.
ccard_cta: Read →
---
This is the second in a short series. We hand the whole studio to a model, with no context, and ask it to work out who made this and why. [The first read](what-an-ai-read) was generous: it found the one rule every tool obeys. This one was asked to sit in a hiring manager's chair instead of a fan's, and it did.

We are publishing it in full, the uncomfortable parts included, because a read you only publish when it flatters you is not worth running.

## What it saw first

It read the six tools as one family, not a pile of side projects. AIP·001 through 006, versions actually climbing (v1.6.2 here, v5.3.1 there), npm packages, GitHub Pages, a signed and notarized macOS dmg that updates itself. Its phrase: not a hobby list, the output of someone who has run a release cycle. That part we will happily take.

Then it made a guess about the maker, and the guess is the interesting part.

## Its verdict: a product person who learned to build

It did not read this as an engineer's portfolio. It read it as a product person who taught themselves to ship. Its reasoning was specific:

- Everything here is a tool for making documents. PRDs, feature specs, IAs, slides, program plans, an e-book. When a developer scratches their own itch you usually get a CLI, a build tool, a debugger. These are a planner's pain points, not a coder's.
- The propose-then-accept pattern across all six is a product principle, not a feature idea, and holding a principle steady across six products is the habit of someone trained in product.
- The copy is doing work. "The AI writes the first draft; the file never leaves your machine" carries positioning, differentiation, and a technical constraint in one sentence.
- Working's four steps, understand, plan, run, wrap up, are a program operations workflow lifted straight from the job.

It even sketched a career from the public surface: long on planning and operations, short on formal engineering, with AI coding agents used as the lever that closed the gap fast. Single TypeScript stack, personal-scale GitHub, a merge-without-review badge, and no trace of the usual senior-engineer signals like a test strategy or architecture docs. It called the code signing and self-updating installers evidence of how quickly that gap is closing. We are not going to confirm a resume from a stranger's inference, but we will say it was not reaching.

## The part we are publishing on purpose

Then it turned blunt, and this is why the post exists.

- **Dispersion.** From the site alone you cannot tell which of the six has real users. No stars, no download counts, no case studies. Its read: the joy of making is running ahead of the work of shipping.
- **Grouping is a warning sign.** Five products are not yet validated, and there is already a hub that ties them together. Platform thinking is a strength, but stacking an abstraction before the things underneath are proven is a trap product people fall into often.
- **No "why me."** The about section ends at "one person, small tools." A single line of the maker's own domain experience, the job where they actually hit these problems, would change how much a reader trusts the whole thing.
- **Self-hosting is a barrier.** Even at one `npx` line, the people these tools would help most, planners and operators, do not live in a terminal. The audience and the delivery are pointed in different directions.

Its one-line summary:

> Senior product sense, junior engineering, unusual execution speed. What you need is not a seventh product. It is real users on one of the six.

## What we think it got right

Most of it. So rather than argue, here is what we are taking.

The users point is correct and it is the whole game. Legible was the compliment from part one. Validated is a different word, and the studio has more of the first than the second. The next move is not another tool. It is picking one and putting real people in front of it, then showing the evidence here instead of asking you to take it on faith.

On Grouping, the warning is fair, and we will say plainly why it exists anyway: the relay between tools is the actual bet, not a decoration on top of six safe products. But building the hub before the members have users is exactly the risk the read named, and naming it does not make it disappear.

On the terminal barrier, the tension is real, and it is precisely why Working is a native app you double-click, no terminal at all. Working is the studio already agreeing with this critique in code. The open question is whether the others follow it out of the terminal or stay tools for people who like terminals. We do not have a clean answer yet.

On "why me," it is a fair hit. That line is a deliberate blank for now, not an oversight, and this series is part of how we decide what eventually goes in it.

## Why publish the harsh one

Because it runs on the same rule the whole studio does. A machine proposed a read of the work, an unflattering one, and we get to decide what to keep. We are keeping the users point, the Grouping caution, and the terminal tension. We are setting the career guesswork aside as guesswork.

Part one said the studio was legible from the outside. Part two said legible is not the same as used. Both are true, and the second one is the more useful sentence to have on the wall this month.
