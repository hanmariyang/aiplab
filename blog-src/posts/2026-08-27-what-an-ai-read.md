---
title: "We had an AI read the whole studio. It found the rule."
date: 2026.08.27
category: Outside read
product: studio
read: 4
excerpt: We pointed an outside model at the site and the GitHub next to it, with no explanation, and asked it to work out who made this and why. It didn't lead with the tech stack. It found the one sentence every tool is built on.
ccard_cta: Read →
---
This is part one of a short series where we hand the whole studio to an AI, cold, and publish whatever it says back. This read was the generous one. [Part two](outside-read-blunt.html) was not.

We ran a small experiment. We pointed an outside model at `aiplab.kr` and the GitHub account next to it, gave it no context, and asked it to reverse-engineer the person behind it, the way a hiring interviewer would size up a candidate from a portfolio alone.

What came back was interesting, and not for the reason you'd expect.

## It skipped the stack

A model reading a set of AI projects usually starts with the obvious surface: the frameworks, the languages, the APIs being called. This one noted the shift from Python and Django in the early repositories to TypeScript, CLIs, git worktrees, and local-first desktop apps now. Fine. Accurate, but not the interesting part.

The interesting part is what it flagged as the through-line. Given six separate tools, it didn't describe six separate tools. It described one pattern, repeated:

> AI = proposal generator. Human = authority.

It spelled the same shape out tool by tool. In Drafting: AI suggests, you accept, the sentence enters the document. In Working: AI proposes a plan, you accept, a real file lands in your folder. In Grouping: request, proposal, accept, relay to the next member. Same grammar, different surface. It called this a design philosophy, not a coincidence, and it was right.

## Why that is worth writing down

We never put that sentence on the site as a manifesto. There is no slogan page that says "the AI proposes and you hold authority." It is just how each tool is built, one at a time, because that is the arrangement we trust.

So the notable thing is not that a model liked the work. It is that the rule was legible from the outside. A stranger, given nothing but the public surface, extracted the exact sentence the studio is organized around. Design consistency turns out to be a form of communication. If six tools made in different weeks all obey one rule, that rule becomes readable without anyone announcing it.

The other line that stuck was its framing of the direction: not "a developer who uses AI well," but someone who has moved from treating AI as an API to treating it as a workforce you direct and approve. That is a fair description of what Coxpit is. A fleet of coding agents is only useful if a human stays in the seat that decides what merges.

## It was also blunt, which we appreciated

The same read was clear about what it could not see. No evidence of large-scale production systems, big teams, enterprise traffic, long-running B2B operations. The GitHub is personal-project scale. It declined to call this a ten-year staff engineer, and it declined to call it a pretty portfolio a beginner assembled with AI. It sat honestly in between.

We have no argument with that. The studio is not pretending to be an enterprise. The whole thesis is on the tin: small tools, self-hostable, that you run yourself. A one-person studio is allowed to look like a one-person studio. What we care about is that the small tools share a spine, and that the spine holds when someone else picks the work up cold.

## The rule was the point

The naming was always a wink. Drafting, Sliding, Lighting: the present continuous, software that is still being made. But the thing that ties the family together is not the suffix. It is that the AI writes the first draft and you keep the authority to make it real.

We wrote that once, for ourselves. It was reassuring to learn a machine could read it back to us from the outside, one sentence, without being told.
