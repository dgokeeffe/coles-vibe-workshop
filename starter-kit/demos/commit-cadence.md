# Demo Sidebar: Commit Cadence — `/commit` After Every Green Test

**When:** Lab 2, approximately minute 40 (~14:40 PM)
**Duration:** 60 seconds
**Style:** Live (quick, reliable)
**Pre-flight:** Have a teams' project cloned locally *or* use your own working repo with at least one green test to run `/commit` against.

---

## Purpose

Teach a habit they'll actually use at work: **commit after every green test**, not once at the end of the day. The `/commit` skill generates a good commit message automatically, so the excuse of "I'll write a proper message later" disappears.

This is the late-lab moment where teams have real code and could lose it if CODA reloads or they accidentally revert. Checkpointing becomes concrete, not theoretical.

---

## The Script (60 seconds)

### Opening (10 sec)

> "One more thing before you wrap up Lab 2 — a habit that'll save you a headache tomorrow at work."

### The demo (40 sec)

Open your terminal. Assume you have uncommitted changes with at least one green test:

```
# Run the test — confirm green
pytest tests/test_bronze_retail_trade.py -v
# → passes

# Commit using the skill
/commit
```

Narrate while `/commit` runs:

> "The skill reads my git diff, summarises the changes, writes a conventional-commits message. I just approve it. Takes 5 seconds."

When the generated message appears, read it aloud:

> "See — `feat: add bronze retail trade ingestion with schema test`. Clean, specific, good enough for code review."

Confirm the commit:

```
Y
```

### Key message (10 sec)

> "Green test → `/commit`. Green test → `/commit`. It takes five seconds and it means you never lose work. Back to your labs — and commit what you have before the demo round."

---

## Fallback — if `/commit` isn't configured or misbehaves

Skip the skill:

> "The principle holds even without the skill: `git add` your changes, write a one-line conventional-commits message, commit. The skill just automates the message. **Green test → commit.** Every time."

---

## Why this demo is worth 60 seconds at minute 40 of Lab 2

- Practical habit they'll take back to work
- Demonstrates Skills (Power Tools slide) in a one-word invocation
- Reduces end-of-lab panic ("wait, did I save that?")
- Creates a natural rhythm for the last 20 min of Lab 2: work → test → commit → next

## What NOT to do

- Don't explain conventional-commits syntax — the skill handles it, that's the point
- Don't commit a big diff — pick a small, clean change so the generated message is readable
- Don't run more than one `/commit` — one is the demo, more is a lecture
