---
title: Running a fleet of coding agents on your own machines
date: 2026.08.23
category: Build log
product: coxpit
read: 7
excerpt: Parallel git worktrees, a live board, and merging the winner. A cockpit for agents, with no cloud in the loop.
ccard_cta: ★ Star on GitHub
cta_title: Own your agent fleet with Coxpit
---
One agent on one branch is easy. The interesting problems start when you want several agents working at once, each taking a run at the same task, and you want to keep the best result without untangling five half-finished branches.

## Isolate first, compare later

Coxpit gives every run its own git worktree and its own branch. The agents never step on each other because they're literally in different working copies. A live board shows each run streaming its output, so you watch them think instead of waiting for a wall of logs at the end.

![The Coxpit fleet console with parallel runs](../img/coxpit-board.png "Each run streams live on its own card.")

When they finish, you diff the results side by side and merge the one you like. The rest are just branches you delete.

[[cta]]

## Your machines, your network

Every part of this runs where you tell it to: your laptop, a spare Mac, a box under the desk. The agents are Claude Code and Codex, driven locally, and your code never leaves your network. Self-hosted isn't a feature bolted on at the end. It's the whole point.
