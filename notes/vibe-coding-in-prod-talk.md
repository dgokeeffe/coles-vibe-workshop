# Vibe Coding in Prod Responsibly — Eric (Anthropic)

**Speaker:** Eric, researcher at Anthropic, coding agents focus. Co-author of *Building Effective Agents* with Barry Zhang.
**Context:** Anthropic talk. Broke his hand biking to work last year and had Claude write all his code for two months — motivated the research.
**Saved:** 2026-04-19 as reference material for the Coles Vibe Coding Workshop.

---

## Thesis

**Vibe coding ≠ heavy AI use.** Per Karpathy: you've *"forgotten the code exists."* If you're reading every diff, you're not vibe coding. The question isn't whether to do it — it's how to do it safely **in production**, because the exponential is coming.

## Why it matters — the exponential

- AI task length doubles every ~7 months. Currently ~1 hour. Next year: 1 day. Year after: 1 week.
- You can read a 1-hour PR. You can't read a 1-week PR.
- Compiler analogy: early devs read assembly output; eventually trust grew. Same trajectory for agent-written code. The question is how to get there safely.

## Core principle

**"Forget the code exists, but not the product exists."** Trust the implementation; verify the outcome.

This is the same problem CTOs, PMs, and CEOs have solved for centuries — managing experts whose work you can't fully audit. Engineers are just unused to it.

## Where to vibe code: **leaf nodes only**

- Parts of the codebase **nothing else depends on**. If tech debt lives there, it's contained.
- **Never** trunk/branches — core architecture, extensible systems — those need human review.
- Tech debt is the one thing agents can't yet self-verify, so target where it doesn't matter.
- As models improve, this tree-line will descend.

## How to succeed: **"Ask not what Claude can do for you — ask what you can do for Claude"**

- You are Claude's PM.
- 15–20 min of upfront context-gathering per feature (often a separate exploratory conversation with Claude first) beats a dozen short back-and-forths.
- Build a plan artifact with Claude, then hand it to a fresh context to execute.
- **Non-technical people shouldn't vibe code production systems** — they can't ask the right questions.

## Case study — 22K-line PR to Anthropic's RL codebase

Merged responsibly because:

1. Days of human work defining requirements
2. Change concentrated in **leaf nodes**
3. Heavy human review on the extensible parts
4. **Designed stress tests** and **human-verifiable inputs/outputs** up front
5. Verifiable checkpoints meant confidence without reading every line
6. Same confidence, fraction of the time

**Second-order effect:** features that used to be "2 weeks, not worth it" become "1 day, let's just do it." The marginal cost of software collapses — and that changes what you build.

## Four closing principles

1. **Be Claude's PM** — treat it like onboarding a junior engineer
2. **Leaf nodes only** — contain the blast radius of tech debt
3. **Design for verifiability** — how will you know this worked without reading the code?
4. **Remember the exponential** — fine not to vibe code today; crippling in 1–2 years

## Practical tips from Q&A

- **Learning**: use Claude as an always-there pair programmer that explains concepts. Lazy people won't learn; curious ones will learn faster than before.
- **Prompt length**: don't over-constrain. Think "what would a junior engineer need on day one?"
- **TDD**: tell Claude to write *minimal end-to-end tests* — happy path + 2 error cases. Read the tests, trust the impl if they pass.
- **Context window hygiene**: compact at natural stopping points; have Claude write findings to a doc *before* compacting so you don't lose the 100K tokens of exploration.
- **New codebase**: have Claude map files, classes, and similar features *before* you write anything. Build the mental model first.
- **Security**: being Claude's PM means knowing where to be careful. Vibe-coded app leaks are mostly non-engineers shipping what they shouldn't have shipped.
- **"Embrace exponentials"** means: assume models will be a *million times* better in 20 years, not twice as good. Plan accordingly.

## The one-sentence takeaway

*The engineer who insists on reading every line will be the bottleneck. The engineer who learns to specify, verify, and trust will scale with the model.*

---

## Connection to this workshop

The talk is unusually aligned with this workshop's Arc C theory block:

| Eric's concept | Workshop slide / artifact |
|---|---|
| "Be Claude's PM" | Slide 14 Rule #1 + Slide 12–13 CLAUDE.md |
| "Leaf nodes only" | **Missing** — could slot in after Small Steps (slide 20) |
| "Design for verifiability" | Slide 18 Verification Patterns + Slide 22 Sycophancy defences |
| "Forget the code, but not the product" | Slide 40 Let Go of the Code (could sharpen with this phrasing) |
| Small-step prompts + tests-first TDD | Slide 19 Small Steps + Lab 1 DE cadence |
| 22K-line PR case study | **Missing** — no external-authority case study |
| "Exponential — models will be a million times better" | Slide 2 The AI Coding Moment (touches it lightly) |

**Ideas to consider for next iteration:**

1. **Add a "leaf nodes" slide or callout** after Small Steps. Names where the small-steps technique safely applies in a production codebase.
2. **Sharpen Slide 40's language** — the talk's *"forget the code, but not the product"* preserves the permission to stop typing while giving a clear anchor (the product). Pairs well with the current *"judgement is what's left of you"*.
3. **Add the 22K-PR case study** — one slide citing Anthropic's own use gives the workshop external-authority grounding YWS and the live demo can't provide alone.
4. **"Ask not what Claude can do for you — ask what you can do for Claude"** is a better encapsulation of Rule #1 than what's currently on Slide 14.
