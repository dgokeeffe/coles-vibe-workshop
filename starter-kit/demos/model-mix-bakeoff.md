# Demo Sidebar: Model Mix Bake-Off

**When:** Lab 1, approximately minute 20 (~12:25 PM)
**Duration:** 90 seconds
**Style:** Live (predictable — Haiku is reliably faster)
**Pre-flight:** Verify both `--model haiku` and `--model sonnet` are configured in CODA before the workshop.

---

## Purpose

Most attendees use Claude at whatever default CODA gives them and have never touched `--model haiku`. Show them that **model selection is part of technique**. Haiku is ~3× faster and ~1/20th the cost for simple tasks; Sonnet is worth the wait for structural work.

This is the workshop's strongest standalone demo because it changes what attendees do with the **next** prompt they send — the switching cost is a flag, not a rewrite.

---

## The Script (90 seconds)

### Opening (10 sec)

> "Pause for a sec. While some of you are waiting on Claude — I want to show you one thing that'll make every wait shorter for the rest of the day."

### Task 1 — Haiku on a simple edit (30 sec)

Open a terminal, have a small file ready (e.g., `README.md` with a planted typo, or any quick edit):

```bash
claude --model haiku-4-5 "Fix the typo 'recieve' to 'receive' in README.md"
```

Count out loud: *"One Mississippi, two Mississippi, three — done."*

### Task 2 — Sonnet on structural work (40 sec)

Same terminal, different model:

```bash
claude --model sonnet-4-6 "Write a pytest with a 5-row DataFrame fixture that validates bronze_retail has columns TIME_PERIOD, OBS_VALUE, REGION, INDUSTRY non-null"
```

While it runs (~15–20 sec), narrate:

> "Sonnet is planning. It's going to generate a conftest fixture, the test function, the assertions. That's worth 20 seconds of wait. But the typo fix wasn't — Haiku nailed that in 3."

### Key message (10 sec)

> "**Same interface. Different tool for the job.** Haiku for tight loops — lint fixes, one-line edits, single test runs. Sonnet for broad tasks — generating a new module, refactoring across files. Opus when you're genuinely stuck on hard reasoning."
>
> "Pick the right one; your wait times shrink and your agent bill drops 10×. Back to your labs."

---

## Fallback — if Haiku or the network misbehaves

Don't try to fix it live. Fall back to:

> "Normally Haiku returns in 2–3 seconds — today the network isn't cooperating, but the point holds: match the model to the task."

Skip Task 2 and move on — do not let the demo eat more than 2 minutes.

---

## Why this demo (facilitator notes)

- Teaches something most attendees don't know they don't know
- Visceral — the speed difference is felt, not argued
- Practical — they'll use `--model haiku` the next time they edit a single file
- Reinforces the workshop thesis: technique (including model choice) over tool

## What NOT to do

- Don't compare answer *quality* — that's a longer conversation and muddies the demo
- Don't mention pricing specifics unless asked (keep the demo about speed/feel, not invoices)
- Don't skip Task 1 — the speed contrast is the whole point
