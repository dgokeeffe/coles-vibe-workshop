# Facilitator Demo Sidebars

Choreographed 60–90 second facilitator demos slotted into the labs. Purpose: fill natural wait moments with active teaching, keep energy up across all experience levels, give laggards a visible breather without slowing leaders down.

## Schedule

| When | Duration | Demo | Style | Link |
|---|---|---|---|---|
| Lab 1, ~minute 20 | 90 sec | **Model Mix Bake-Off** — Haiku vs Sonnet on matched tasks | Live | [model-mix-bakeoff.md](model-mix-bakeoff.md) |
| Lab 1, ~minute 40 | 90 sec | **Fresh-Context `/review`** on a team's silver/gold code | Live (pre-selected team) | [review-subagent-demo.md](review-subagent-demo.md) |
| Lab 2, ~minute 20 | 90 sec | **Small-Steps Save** — big-bang fail vs small-step success | Pre-recorded | [small-steps-save.md](small-steps-save.md) |
| Lab 2, ~minute 40 | 60 sec | **Commit Cadence** — `/commit` after every green test | Live | [commit-cadence.md](commit-cadence.md) |

## Principles

- **Four is the ceiling.** Beyond this, demos stop being spotlights and start feeling like slowdowns.
- **Live only for predictable behaviour.** If the demo's point depends on the agent doing something specific (arguing with itself, generating flawed code), pre-record. If it depends on something reliably measurable (Haiku is faster than Sonnet for a typo fix), go live.
- **Every demo teaches a habit, not a concept.** Each 90 seconds should leave attendees with something they can do on Monday, not something they understand better.
- **Consent for any demo that uses a team's work.** The `/review` demo requires asking first. Never ambush a struggling team.

## Pre-flight checklist (day before workshop)

- [ ] Model Mix: confirm `claude --model haiku-4-5` and `claude --model sonnet-4-6` both work in CODA
- [ ] `/review`: confirm the skill is available and run it once locally against reference-implementation code to verify output quality
- [ ] Small-Steps Save: record the video, host it at an accessible URL, test playback on the presentation laptop
- [ ] Commit Cadence: confirm `/commit` skill is available, pre-stage a clean green-test scenario in a scratch repo

## If a demo fails live

Each demo script has a fallback paragraph. Read it, move on, do NOT try to fix live. The cost of a failed demo attempt is silence — the cost of trying to fix it is 3–4 lost minutes and a room that's stopped paying attention.
