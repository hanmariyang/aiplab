---
title: Shipping Working: nothing exists until you accept it
date: 2026.08.26
category: Note
product: working
read: 6
excerpt: The fifth tool is a macOS app for planning a program end to end. Its hardest rule is not a feature you can toggle. The database itself refuses to create a file the human never accepted.
ccard_cta: Download for macOS ↓
cta_title: Plan your next program with Working
---
Working proposes a structure, drafts the sections, and suggests the wording. But nothing lands on disk until you accept it. That sounds like a setting. It isn't. The database enforces it. A document with no record of a human accepting it simply cannot reach a confirmed state.

> A document the human never accepted can't be confirmed. Not by policy. By schema.

A single test, `api/test/automatic-confirmation.test.js`, guards this rule. If a future change ever lets the AI confirm its own output, that test goes red before the change ships.

![Working proposes a plan structure with accept and reject buttons](../img/working-accept.jpg "Working proposes a structure, and you accept before any file is created.")

## Why bother

Because "AI-assisted" quietly slides into "AI-authored" the moment the human is only a spectator. The accept step keeps a person in the loop where it matters, not as a rubber stamp, but as the one who decides what becomes real.

[[cta]]

## Where the files go

Every accepted document is a real `.md` file in a folder you chose. No account, no server, no lock-in. Close the app and the work is still yours, in plain text, on your machine.

```
# a project, on your disk
~/Projects/2026-hackathon/
  01-파악.md
  02-기획.md
  03-실행.md
  04-정리.md
```

That's the whole idea, and it's the same idea in every tool the studio ships: **the AI writes the first draft; you write the document.**
