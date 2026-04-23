# Demo Sidebar: Small-Steps Save (The Anti-Pattern)

**When:** Lab 2, approximately minute 20 (~14:20 PM)
**Duration:** 90 seconds
**Style:** **Pre-recorded video** (live is risky — see below)
**Pre-flight:** Record the demo once the week before, host at `https://dgokeeffe.github.io/databricks-vibe-coding-with-coda/demos/small-steps-save.mp4` or equivalent. Test playback on the presentation laptop before the workshop.

---

## Purpose

Make the Small Steps principle (slide 21) **felt**, not just argued. Watching a big-bang prompt hang for 30 seconds with no visibility — and then seeing a small-step version finish cleanly in the same time — teaches the lesson in a way no slide can.

This is also a mid-Lab-2 energy intervention: teams are in the grind phase, and a 90-second "watch what NOT to do" demo gives leaders something new to think about and laggards a break.

---

## The Pre-Recorded Video (90 seconds)

### Segment 1: The Big-Bang Fail (~45 seconds)

Screen recording of a terminal. Cursor types:

```
Build me the entire FSANZ pipeline for Lab 2:
- Bronze table ingesting recalls from the FSANZ website
- Silver table with cleaned dates and normalized state names
- All data quality expectations for bronze and silver
- Cross-source gold view joining with retail and CPI
- Tests for every layer
- Pipeline scheduling
```

Agent starts responding. Narration (voiceover):

> "I'm 20 seconds in. The agent is reading files, planning, about to generate 6 files in parallel. I have no idea which part will fail. If it does fail, I'm debugging a 6-file blast radius."
>
> "I'm going to stop it at 45 seconds — because this is exactly what we warned against on slide 21."

Cut the recording when it's just starting to produce output.

### Segment 2: The Small-Steps Version (~40 seconds)

Same terminal, reset. Show five small prompts in quick succession:

```
Prompt 1: Write ONE test for bronze_food_recalls schema (3 sample rows, non-null product and date).
→ 8 seconds. Test exists. Verified.

Prompt 2: Implement bronze_food_recalls as @dp.table. Just the ingest, no transformations.
→ 12 seconds. File exists. Read it — clean.

Prompt 3: Run the test. Fix only if it fails.
→ 6 seconds. Green.

Prompt 4: Add @dp.expect for product non-null. Nothing else.
→ 5 seconds. One decorator. Test still green.
```

Narration:

> "Four prompts. 31 seconds of agent time total. And I know exactly what changed at each step. If step 3 had failed, I'd be debugging *one* file, not six. **That's the save.**"

### Segment 3: The Lesson (~5 seconds)

Single text card:

> **After each prompt: "Do I know if this worked?"**
>
> **If no — split it.**

---

## Why pre-recorded, not live

Live, this demo is risky:
- Agent might not cooperate on the "fail dramatically" half — could finish fine in 2 min, ruining the point
- Live demos of anti-patterns are always harder than demos of things working
- A botched live version eats 4+ min and kills energy at exactly the moment you wanted to lift it

Pre-recorded gives you:
- Guaranteed timing (exactly 90 sec)
- Predictable teaching beats
- Can be practiced/iterated once and then reused for future workshops

---

## Facilitator intro before playing the video (15 sec)

> "Quick pause — we're about halfway through Lab 2, and this is the moment I'd warn my past self about. I'm going to play a 90-second video. Watch what happens when someone forgets the Small Steps principle — and then what happens when they remember it."

Press play. Don't talk over it. Afterwards:

> "Back to Lab 2. If your next prompt is starting to feel like the one in the first half of that video — you know what to do."

---

## Fallback — if video fails to play

Don't try to recover by demoing live. Fall back to:

> "Short version: if you're about to send a big prompt — the kind that'd take 10+ minutes — stop and split it into 3 or 4. You'll be faster, you'll see what broke, and you won't spend 20 minutes debugging a blast radius. Slide 21. Back to it."

---

## Recording notes (for when you shoot the video)

- Use a real project (the reference implementation is fine)
- Do the big-bang prompt first; record it genuinely failing or just being slow
- For the small-steps segment, use `&&` between commands to chain quickly on screen
- Add a simple timer overlay so viewers can see the "45 sec" / "31 sec" claim
- Keep the voiceover tight — silent stretches feel longer than they are

## What NOT to do

- Don't make the big-bang prompt *so* exaggerated it feels cartoonish — keep it plausible
- Don't let the video run longer than 90 seconds; short is the point
- Don't narrate over the small-steps half — let the speed speak for itself
