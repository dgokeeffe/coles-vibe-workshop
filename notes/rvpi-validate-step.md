# R.V.P.I. — The Case for a Validate Step in Vibe Coding

**Source:** Perplexity research synthesis (prompted by David O'Keeffe's extension of Alex Ker's R.P.I. framework).
**Saved:** 2026-04-19 as reference material for the Coda Vibe Coding Workshop.
**See also:** `harnesses-article.md` (where R.V.P.I. was first proposed) and `vibe-coding-in-prod-talk.md`.

---

## Overview

R.P.I. (Research → Plan → Implement) is the most widely adopted structured workflow for AI coding agents. It addresses a real problem: agents jumping to implementation without research produce brittle code. But R.P.I. has a silent gap.

**Research surfaces context — but nothing checks whether that context is *trustworthy* before the agent builds a plan on top of it.**

**R.V.P.I. (Research → Validate → Plan → Implement)** names that gap and closes it.

---

## What "Validate" means here

Vibe coding uses *validate* in two senses:

1. **Output validation** — did the code do what was intended? Well-understood: prompt, generate, test, refine.
2. **Context validation** — before the agent plans, is the retrieved memory and research *still accurate*? Less discussed. This is what R.V.P.I. is about.

V sits between Research (gathering context from memory, past sessions, codebases, external sources) and Plan (designing the change). Its job: **audit what was retrieved before that retrieved content becomes load-bearing**.

---

## Why retrieved context cannot be trusted by default

### Stale context

Agents accumulate context across sessions on long-horizon tasks. Without active management, it goes stale. When the agent's second observation returns outdated state, it detects a mismatch, re-plans, burns tokens in a loop — classic context drift.

A plan built on stale context is not just inefficient — **it is confidently wrong**. The agent has no way to know its research reflects yesterday's codebase, a deprecated API, or an overridden architectural decision.

### Conflicting context

RAG and transcript replay pull from multiple sources simultaneously — vector stores, conversation history, external docs. These sources can contradict each other. When memory contains conflicts, the agent doesn't negotiate between them; it picks the one that scores highest on *relevance*, not *accuracy*. The plan that follows inherits that conflict silently.

### Poisoned context

Memory poisoning is a structural vulnerability where malicious or incorrect data is injected into an agent's long-term memory store. Unlike prompt injection (a one-time manipulation), **memory poisoning persists across sessions and influences every future recall**.

RAG repositories are often treated as a single source of truth, meaning a poisoned entry propagates into every downstream plan and implementation until explicitly removed.

**Doesn't require a sophisticated attacker:**
- A badly formatted tool output
- A hallucinated memory write
- An auto-accepted suggestion that was wrong

All achieve the same effect.

---

## What the Validate step does

Not a full re-research pass. A **targeted audit** of what Research returned before it drives planning.

Three questions:

| # | Question | In practice |
|---|---|---|
| 1 | **Is this current?** | Check retrieved memories/docs against the actual state of the codebase, API, or system. If the agent pulled a memory saying "authentication uses JWT," does the current codebase confirm that? |
| 2 | **Is this consistent?** | Flag conflicts between retrieved sources. If two memories contradict, surface the conflict before the plan papers over it. |
| 3 | **Is this trustworthy?** | Assess provenance. Where did this context come from? Agent-generated (subject to prior hallucinations), human-authored, or externally retrieved of unknown freshness? |

Maps directly to *verifiable context*: every element of context the agent acts on should be verifiable before it acts.

---

## Memory governance — the underlying discipline

The Validate step is the human-facing expression of **memory governance**: the formal management of what an agent's memory contains, what gets written/revised/discarded, and how trust is assigned.

Current agent architectures (transcript replay and retrieval-based) treat memory as accumulated text with no principled write path for internal state. They don't specify what should persist, what should be revised, what should be discarded.

R.V.P.I. makes memory governance **operational** by inserting a decision point precisely where its absence causes the most harm: between gathering context and acting on it.

### Four practical mechanisms

| Mechanism | What it does |
|---|---|
| **Trust-weighted retrieval** | Adjust retrieval scores based on provenance metadata. A highly relevant memory from an unverified source is demoted below a moderately relevant memory from a confirmed, human-authored source. |
| **Canonical state auditing** | Maintain a reference state against which retrieved memories are compared. Flag drift as anomaly. |
| **Circuit breakers** | If Validate detects irreconcilable conflict or a high staleness signal, **halt planning** and surface the conflict to the human. Don't proceed silently. |
| **Immutable audit logging** | Log all memory reads and writes so that if a poisoned context is later identified, the blast radius can be traced and rolled back. |

---

## R.V.P.I. in practice

| Phase | Agent behaviour | Human oversight point |
|---|---|---|
| **Research** | Document what exists — no opinions, no plans | Review scope of retrieved context |
| **Validate** | Audit retrieved context for staleness, conflicts, provenance | **Confirm or correct before planning** |
| **Plan** | Design change using only validated context; include success criteria | Approve plan before implementation |
| **Implement** | Execute mechanically, verify after each phase | Review output against requirements |

The human oversight point at Validate is the **cheapest possible intervention**. Catching a stale API reference or a conflicting memory *before* the plan is written costs nothing. Catching it after the agent has built twenty implementation steps around a wrong assumption is expensive.

### Adjacent practice worth noting

Some practitioners use a **clean-context agent** after implementation: a fresh agent reviews original requirements + approved plan + generated code together, specifically because a fresh agent isn't "emotionally attached" to upstream decisions.

R.V.P.I. moves this freshness check *earlier* in the cycle, where it prevents bad plans rather than catching bad code.

---

## The broader implication: memory as untrusted input

R.V.P.I. implies a **security posture shift**:

> **Retrieved memory should be treated as untrusted input until validated**, in the same way external API responses are treated as untrusted.

This is *not* the default assumption in most agent architectures, which treat their own memory stores as authoritative.

Adopting this posture means:

- Memory writes are **explicit and logged**, not automatic
- Retrieval results carry **provenance metadata**, not just relevance scores
- Conflicts between sources are **surfaced**, not silently resolved by ranking
- Human-in-the-loop is positioned at the **governance layer**, not just the output layer

This is where R.V.P.I. matters beyond workflow efficiency. The Validate step is the architectural seam through which **memory governance becomes a first-class concern in agentic software development**.

---

## Connection to this workshop

### Where V concepts already live in the deck

| R.V.P.I. concept | Existing slide / artifact |
|---|---|
| Validate retrieved context | Slide 22 Sycophancy — "Reproducibility: lock the inputs" card (partial) |
| Output validation | Slide 18 Verification Patterns (covers output, not context) |
| Separate prompts for tests vs implementation | Slide 22 Sycophancy defence #3 (a form of V for the test inputs) |
| "Treat CLAUDE.md as code that can rot" | **Missing** — no slide frames CLAUDE.md as a *thing that needs validation over time* |
| Memory poisoning as a failure mode | **Missing** — Sycophancy slide covers "agent agrees with you when you're wrong" but not "agent agrees with itself from a past session when the past session was wrong" |

### Ideas to consider for next iteration

1. **Rename/expand the Sycophancy reproducibility card** to include poisoned context: *"Sycophancy has two modes — agent agrees with you now, or agent agrees with itself from a past session. Both need the same defence: validate your inputs before you plan on them."*
2. **Add R.V.P.I. as a named framework** somewhere in Arc C (maybe as a callout on the Small Steps slide or Verification Patterns slide). Four phases with clear human-oversight points is the clearest articulation of the workshop's meta-technique.
3. **For the DE track's CLAUDE.md lab**, add a brief prompt: *"after Lab 1, look at your CLAUDE.md. Would a fresh session still produce the right plan from it? If not, what's drifted?"* — makes memory governance concrete via the attendees' own file.
4. **Introduce the "memory as untrusted input" framing** as one line somewhere near Sycophancy. It's a security-posture reframe that experienced engineers will remember because it rhymes with existing discipline around external API responses.
5. **Hooks as V-step automation**: Stop-hooks that check *"is the CLAUDE.md I'm about to follow consistent with the current project structure?"* are a V-step implementation. Current workshop treats hooks as *guardrails after the agent acts*; R.V.P.I. lets you frame them as *guardrails before the agent plans*.

### The meta-point for the workshop's thesis

The workshop teaches attendees to **be Claude's PM** (Eric) and to **own their harness** (Alex). R.V.P.I. adds a third pillar: **be Claude's librarian**. The config files, retrieved memory, and skill metadata are library materials. Someone has to catalogue them, check them out, retire them when they're stale, and flag them when they conflict. That someone is the engineer.

---

## Where Platforms Absorb V

> **Added 2026-04-19** — framing for Slide 24 ("Where Databricks Absorbs V") and the transition from Memory-As-Untrusted-Input into Small Steps.

### The insight

R.V.P.I. sounds like a lot of work because in most environments it *is*. The agent can break anything — schema, permissions, config, deploy state — so the human has to validate everything. Databricks changes the shape of that problem. Large classes of validation are **absorbed by the platform**, performed deterministically for every operation, whether the agent knows to ask or not. The V you have to do manually shrinks to the claims the platform *can't* see.

The workshop-line punchline:

> *"Tools automate V. Platforms absorb V."*

### What Databricks absorbs (mechanical V)

| Platform mechanism | Validation it performs | What you used to have to do |
|---|---|---|
| **Unity Catalog permissions** | Agent tries to write to a table it doesn't own → query fails | Write permission checks into every plan |
| **Unity Catalog schema** | Agent hallucinates a column name → query fails cleanly | Grep schema files manually; hope the agent reads them |
| **Lakeflow `@dp.expect` / `@dp.expect_or_fail`** | Bad data passes through Bronze → quality gate fires at runtime | Build custom pytest data-quality suites |
| **Serverless SDP** | Agent specifies broken cluster config / partition strategy → not possible to write | Catch cluster misconfig in code review |
| **`databricks bundle validate`** | Typo in resource YAML / missing dependency → fails before deploy | Debug failed deploys after the fact |
| **Genie + semantic layer** | LLM hallucinates a table name → constrained to curated model | Post-hoc validate every generated SQL |
| **Model Serving versioning** | Agent deploys a broken model → rollback is one click | Manually manage blue/green model deploys |
| **Lakebase (managed Postgres)** | Agent forgets OAuth token rotation → pool handles it | Write connection pool + secret rotation code |
| **Asset Bundles `dev` / `prod` targets** | Agent writes to prod by accident → target isolation prevents it | Env-var juggling, manual workspace URL swaps |

### What the platform *cannot* see (semantic V — your job)

- **CLAUDE.md claims** — "we use FSANZ for recalls", "pipeline runs hourly". Platform has no view into whether that's still true.
- **Past-session memory** — "earlier we decided Silver enforces unique product_id". Platform doesn't know the decision happened.
- **Cross-source consistency** — CLAUDE.md vs. the code vs. an earlier Claude summary vs. a Slack thread. Platform validates each artifact in isolation; *coherence* across them is yours.
- **Intent-level correctness** — the SQL runs and the schema matches, but is the *logic* right? Platform can't tell. (This is why Gold tables still need BDD tests.)

### The decision rule (the take-home)

> *"Before you build a custom V mechanism — a hook, an MCP, a test — check whether the platform already validates it. If Unity Catalog, Lakeflow, or bundles would catch it deterministically, you're done. Spend your V budget on the claims no platform can see: semantic, cross-source, intent."*

### How this lands in Block 4

Placement: **Slide 24**, inserted between Slide 23 (Memory As Untrusted Input) and Slide 25 (Small Steps). The narrative arc through the block ends:

1. Sycophancy (V costs — what skipping V looks like)
2. Memory As Untrusted Input (V as security posture — why the cost is worth paying)
3. **Where Databricks Absorbs V** (V relief — the cost is smaller than you think on this platform)
4. Small Steps (V tactics — how to do the residual V efficiently)

Attendees move from *"V is a lot"* → *"V matters"* → *"V is bounded"* → *"V is doable in small steps"*. The relief slide is what prevents the block from feeling like a sermon on vigilance.
