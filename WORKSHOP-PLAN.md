# The Great Grocery Data Challenge

## Vibe Coding Workshop: Coda

**Client:** Coda — Data & AI Engineering Team
**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Format:** Full-day (7 hours, 10:00–17:00), Onsite at Coda SSC
**Team Size:** Pairs (driver/navigator, 15-min swaps), up to 5 pairs (10 participants)
**Platform:** Coding Agents Databricks App (browser-based terminal)

---

## The Challenge

> You're a pair of data engineers at an Australian grocery retailer. Your CEO wants a
> **Grocery Intelligence Platform** that turns public data into actionable insights.
> You have a full day to build it end-to-end: data pipeline, web app, and natural language
> query interface. **May the best pair win.**

Each pair builds a complete platform using real Australian public data:

1. A **Lakeflow Declarative Pipeline** (Bronze → Silver → Gold)
2. A **FastAPI web app** with at least one AI-powered feature
3. A **Genie space** for natural language queries on their data
4. An **AI/BI dashboard** with key retail metrics

**Data Sources (all public, pre-configured):**

| Source | What It Provides | Update Frequency |
|--------|-----------------|------------------|
| ABS Retail Trade API | Monthly retail turnover by state & industry (2010–present) | Monthly |
| ABS Consumer Price Index API | Quarterly food price indices by state (2010–present) | Quarterly |
| FSANZ Food Recalls | Food safety recall notices with product details | As issued |
| ACCC Supermarket Inquiry | Public reports on grocery market competition (PDFs) | Ad hoc |

**Suggested Pair Angles** (or invent your own):

| Angle | Key Questions |
|-------|--------------|
| **Retail Performance Tracker** | Which states are growing? What industries are trending? Where should we invest? |
| **Food Inflation Monitor** | Where are prices rising fastest? How does food CPI vary by state? What's the 12-month trend? |
| **Food Safety Dashboard** | What are the recall trends? Which products/companies are most affected? What states are impacted? |
| **Market Intelligence Hub** | Cross-source analysis: how do retail trends, inflation, and safety intersect? |

---

## Learning Objectives

By end of day, participants will be able to:

1. Apply the **R.V.P.I. loop** (Research → Validate → Plan → Implement) to direct AI coding agents
2. Use conversation to initialize projects and guide AI coding agents (CLAUDE.md, PRDs)
3. Use BDD/TDD to dramatically improve agentic code generation accuracy
4. Build and deploy Lakeflow Declarative Pipelines with Databricks Asset Bundles
5. Use **skills** and **MCP** for practical tool integration with agents
6. Connect agents to external tools via **MCP** (Model Context Protocol)
7. Create **Genie spaces** and **AI/BI dashboards** for natural language analytics
8. Ship a working end-to-end application on Databricks
9. (DS) Track and compare experiments with MLflow, train and serve a model
10. (Analyst) Create Genie spaces and AI/BI dashboards for business users

---

## Workshop Rhythm

Every block follows the same pattern for maximum engagement:

```
Theory / Demo (live)  →  Practice (pair, R.V.P.I.)  →  Discussion (5–15 min)
```

Short, punchy teaching → hands-on practice in pairs → share learnings with the group.

Pairs swap driver/navigator every 15 minutes. Navigator reads, verifies, and steers — never passive.

---

## Agenda Overview

| Time | Duration | Activity | Mode |
|------|----------|----------|------|
| **10:00** | 10 min | Opener — why this matters, end-output teaser | Engage |
| **10:10** | 15 min | Internal Demo — coding agents at Databricks + live pipeline + dashboard | Demo |
| **10:40** | 10 min | Break | |
| **10:50** | 70 min | **Get-to-know-Claude** — R.V.P.I. + CLAUDE.md + Small Steps + tools + BDD + Sycophancy + Context | Theory/Demo |
| **12:00** | 60 min | Lunch | |
| **13:00** | 15 min | Challenge brief + pair formation + Lab 1 briefing | Briefing |
| **13:15** | 90 min | **Lab 1** (track-specific, pairs) | Exercise |
| **14:45** | 15 min | Show & Tell (Lab 1 highlights) | Discussion |
| **15:00** | 10 min | Break | |
| **15:10** | 80 min | **Lab 2** (track-specific, pairs) | Exercise |
| **16:30** | 30 min | Team demos + Let Go of the Code + Takeaways + Hackathon + Close | Wrap-up |

**Time breakdown:** 10 min opener · 15 min internal demo · 70 min teaching block · 170 min pair labs · 45 min demos/discussion · 80 min breaks/lunch · 15 min briefing

---

## Slide Order

See `WORKSHOP-TRANSCRIPT.md` for the authoritative block-by-block slide plan. Summary:

| Block | Slides | Notes |
|-------|--------|-------|
| Opener | Title, AI Coding Moment, End-Output Teaser | Time strip updated to 10:00 |
| Internal Demo | Coding Agents at Databricks, Watch First, Live Pipeline + Dashboard | Demos run live from terminal |
| Get-to-Know-Claude | R.V.P.I. intro, R.V.P.I. in terminal, Techniques divider, Why Specs, CLAUDE.md, Rule #1, Small Steps, Power Tools, Skills, MCP, BDD, Sycophancy, Memory-as-untrusted-input, Tokens, Context | ~18 slides |
| Challenge Brief | Today's Challenge, Pair Programming Norms, Lab 1 Briefing | |
| Lab 1 | Lab 1 divider | Silent block, agent work |
| Show & Tell | Show & Tell (Lab 1 highlights) | |
| Lab 2 | Lab 2 divider, Lab 2 Briefing | |
| Close | Team Demos, Let Go of the Code, Takeaways, Next Steps, APJ Hackathon, Closing | |
| Appendix | Rosetta Stone, Subagents/Skills/Hooks/Plugins, Skills for BDD, Subagents vs Agent Teams, What/How MCP, MCP on Databricks, AI Dev Kit | Reference |

Target: ~48 slides total (down from 53).

---

## Detailed Agenda

### 10:00–10:10 | Opener (10 min)

**Slides:** Title, AI Coding Moment, End-Output Teaser

**Purpose:** Frame why this matters *now*, then preview what participants will ship today.

**How it works:**

1. **Title + why this matters** (~3 min)
   - Name the mixed-experience room.
   - Land the thesis: *"The bottleneck in software is no longer typing. The new scarce resource is verification and coordination. Today you learn the technique."*

2. **The AI Coding Moment** (~3 min)
   - One lead stat: Pragmatic Engineer on verification as the bottleneck.
   - Other stats (Stack Overflow adoption, METR, Stanford) move to appendix.

3. **End-Output Teaser** (~4 min)
   - Three-pane mosaic: pipeline graph (DE), UC-registered model + predictions chart (DS), Genie dashboard + FastAPI app with Genie embed (Analyst).
   - *"Six hours from now. One pair last quarter built something I'd have budgeted six weeks for. I want that for you today."*

---

### 10:10–10:25 | Internal Demo — Coding Agents at Databricks (15 min)

**Slides:** Coding Agents at Databricks, Watch First, Live Pipeline + Dashboard (frame only)

**Purpose:** Show the agent working live before teaching about it. Credibility beats polish.

**How it works:**

1. **Coding Agents at Databricks** (~2 min)
   - High-level: what we use Claude Code for internally — PR review, refactors, test generation, compliance gates.
   - Sets up that this is not a demo toy.

2. **Watch First — mini-demo** (~2 min)
   - Open terminal in CODA.
   - Quick tour: `git log`, skills directory, CLAUDE.md, a couple of recent PRs.
   - 90-second task live (e.g., *"add a feature-flag check to this endpoint with a test"*).
   - Narrate the R.V.P.I. loop as you go **without naming it yet** — save the name for Block 4.

3. **Live Pipeline + Dashboard Demo** (~4 min) **← MAJOR DEMO**
   - **Pre-requisite:** reference-implementation pipeline pre-deployed; AI/BI dashboard pre-built + open in a tab; CODA terminal pre-opened; warehouse warm.
   - **Flow:** Dashboard (already running) → terminal → prompt for pytest (yoy_growth_pct) → red → prompt to implement window function → green → `databricks bundle deploy && run` → dashboard refresh → new column visible.
   - **Land:** *"Four prompts, one new metric, end-to-end loop. Two things I want you to notice. First: I didn't write most of that code — I *directed* it. Second: every step had a way for me to verify it worked. No verification, no trust. We'll return to that idea all day."*
   - Full script + fallbacks: `starter-kit/demos/pipeline-and-dashboard-demo.md`.

> **Facilitator note:** This is the credibility block. If the demo fails live, read the fallback paragraph and move on. Do not try to fix live — cost of failure is silence; cost of trying to fix is 3–4 lost minutes and a room that's tuned out.

---

### 10:40–10:50 | Break (10 min)

---

### 10:50–12:00 | Get-to-Know-Claude — R.V.P.I. + Techniques (70 min)

**Slides:** R.V.P.I. Intro, R.V.P.I. in Terminal, Techniques divider, Why Specs, CLAUDE.md + Scopes + Rule #1 (hands-on), Small Steps, Power Tools, Skills, MCP, BDD + Gherkin, Anthropic Best Practices, Sycophancy, Memory-as-untrusted-input, Tokens, Context Windows

**Purpose:** Teach the meta-framework (R.V.P.I.) and its specialisations. This is the pressure block — 70 minutes, ~18 slides, guided-demo style. Drive from the terminal; slides are backdrop.

**Framing:** *"Everything I'm about to teach fits inside one loop. Let me name it first, then walk you through it."*

---

#### Sub-section 1 — R.V.P.I. Framework Intro (5 min)

**R.V.P.I. = Research → Validate → Plan → Implement.**

Most people have heard of R.P.I. (research, plan, implement). The missing letter is **V**. Before you plan on top of the research, you *audit* the research. Is it current? Is it consistent? Is it trustworthy?

**Why V matters:**
- Memory drifts. CLAUDE.md files rot.
- An agent's summary from yesterday can quietly contradict today's reality.
- The agent will plan on top of that contradiction without flagging it.
- The **single biggest difference** between a junior prompter and an experienced one is validating inputs before building on them.

**R.V.P.I. in the terminal:**
- **Research** = `/init`, grep, read, documentation lookups.
- **Validate** = re-read CLAUDE.md, check a test still passes, ask *"is this still how it works?"*, audit retrieved memory.
- **Plan** = `/plan` or `ExitPlanMode`.
- **Implement** = small steps, verify after each.

**Callback policy:** Point back at R.V.P.I. at every sub-section boundary below. Everything else is a specialisation of one phase.

---

#### Sub-section 2 — CLAUDE.md Scopes (Validate's artifact) (10 min)

- Persistent instructions the agent follows on every prompt — the primary artifact Validate audits.
- **Three scope levels:**
  - User (`~/.claude/CLAUDE.md`) — personal standards, always loaded.
  - Project (`<repo>/CLAUDE.md`) — team standards, checked in.
  - Folder (nested CLAUDE.md) — local overrides for specific components.
- **Rule #1: Just say what you want.** No manual config-file edits. Tell Claude about the project; it writes the CLAUDE.md.

**Hands-on (pair-friendly, 5 min):**
- Driver asks Claude for a CLAUDE.md about their role/project.
- Navigator reviews what it produces and flags anything that looks stale or wrong.
- Swap after ~3 min.
- _"This is V in practice — you're validating the output before it becomes load-bearing."_

---

#### Sub-section 3 — Small Steps (Implement stays honest) (10 min)

- **Each prompt = one verifiable step.** Small Steps is how Implement stays honest.
- Big-bang prompting is a habit from ChatGPT; Claude Code rewards tight iteration.
- 10–20 min wait → attendee sits idle, agent drifts in silence, multiple failures hit at once.
- 1–3 min prompts → active review, isolated failures, verification every 90 seconds.
- _Heuristic:_ *"After this prompt, will I KNOW whether it worked?"* If no → split it.
- **R.V.P.I. crossover:** each prompt is a mini-RVPI loop. Research what to change → Validate it's still the right change → Plan the step → Implement + verify.

---

#### Sub-section 4 — Power Tools: Skills, MCP, Hooks, Subagents (15 min, live demos)

Tools that **automate V**. This is the hands-on tools section.

- **Skills** — reusable slash commands (`/commit`, `/review`, `/test`). Live demo: invoke one.
- **MCP** — "USB for AI" — open protocol for agents to call external tools. Three tiers:
  - **Managed:** Built into Databricks (Unity Catalog, DBSQL, Vector Search).
  - **External:** Community-built (Slack, JIRA, GitHub, Confluence, Databricks Docs).
  - **Custom:** You build them (internal APIs, data tools, monitoring).
  - Live demo: Databricks Docs MCP searching documentation in real time.
- **Hooks** — deterministic guardrails (PreToolUse/PostToolUse/Stop). **Framed as V-step automation** — Stop-hook checks *"is the CLAUDE.md I'm about to follow consistent with the current project structure?"*
- **Subagents** — fresh-context workers (`/review`, `Agent` tool). Compression: vast exploration distilled to clean signal.
- Plugins: package for teams (Databricks fe-vibe marketplace).
- _Deep dive available in appendix slides for motivated attendees._

---

#### Sub-section 5 — BDD / Gherkin (Verification inside Implement) (15 min)

- Human writes spec (Gherkin or pytest assertions) → agent implements → agent iterates on failures.
- The key insight: **structural verification the agent can't bluff.**
- _"If you take one thing from today: write the tests first. Always."_
- Labs use pytest; same principles apply whether you write Gherkin or plain assertions.
- **Anthropic Best Practices slide** — verify before moving on, plan in chunks, extended thinking for complex problems, trust but verify.

---

#### Sub-section 6 — Sycophancy + Memory-as-Untrusted-Input (What skipping V costs) (10 min)

- **Stanford Science (Mar 2026):** 11 LLMs, 49% more agreement than humans, 51% still agree when user is 100% wrong.
- **Karpathy's 4-hour experiment:** model demolished its own prior argument when asked to argue the opposite.
- RLHF selected for likeability, not truth.
- **Two modes of sycophancy:**
  - Agent agrees with you *now*.
  - Agent agrees with itself from a past session when the past session was wrong. ← context poisoning.
- **Four defenses:** Karpathy Test, "Wait a minute..." prefix, structural verification (BDD), separate prompts.
- **Memory-as-untrusted-input framing:** *"Retrieved memory should be treated as untrusted input, the same way external API responses are."* This is a security-posture reframe experienced engineers remember because it rhymes with existing discipline.
- _"The discipline of stress-testing AI output is the career skill of this decade."_

---

#### Sub-section 7 — Tokens + Context Windows (Why V's value compounds) (5 min)

- The unit of "thought" for LLMs — roughly 4 chars per token.
- Context = working memory; use `/compact` when agent starts contradicting itself.
- **V prevents drift. Drift is why context management matters.** The longer the session, the more V earns its keep.

---

**Key messages for Block 4:**
- *R.V.P.I. — name the loop, use it. Validate is the cheapest intervention in the stack.*
- *CLAUDE.md is an artifact that rots. Validate it.*
- *Small Steps beat Big Bang. Every prompt = a mini-RVPI loop.*
- *Verification is the new bottleneck. You own that, no one else does.*

---

### 12:00–13:00 | Lunch (60 min)

Prize for demo winner awarded at close.

---

### 13:00–13:15 | Challenge Brief + Pair Formation + Lab 1 Briefing (15 min)

**Slides:** Today's Challenge, Pair Programming Norms, Lab 1 Briefing

**Content:**

1. **Today's Challenge** (~3 min)
   - Grocery Intelligence Platform: 4 data sources, pair angles.
   - Three tracks — pick one:
     - **Data Engineering:** Lakeflow pipeline, dashboard.
     - **Data Science:** Forecasting model, UC-registered with `@champion` alias, batch predictions in a notebook (Tier 1) or Lakeflow job (Tier 2 stretch).
     - **Analyst:** Genie spaces, FastAPI app with embedded Genie.

2. **Pair Programming Norms** (~5 min)
   - Two people per keyboard. **15-min driver swaps.**
   - Navigator duties: read, verify, suggest. Never passive.
   - If odd-numbered, form one triad with an observer taking notes on surprises.
   - Escalation rule: *"If a task doesn't fit R.V.P.I. in 15 min, split it."*
   - *"Why pairs: shipping with AI is a verification problem. Verification is cheaper with a second pair of eyes. Solo is slower, not faster — you'll skip V steps a navigator wouldn't."*

3. **Lab 1 Briefing** (~5 min)
   - Track-specific lab file pointers ([LAB-1-DE.md](LAB-1-DE.md) | [LAB-1-DS.md](LAB-1-DS.md) | [LAB-1-ANALYST.md](LAB-1-ANALYST.md)).
   - Five practical patterns (sidebar, not full slide):
     - Overengineering — start small.
     - Hallucinations — demand proof ("show me the git diff").
     - Course-correct early.
     - Challenge & verify.
     - Commit every 15–20 min — safety net for Esc-Esc rewind.
   - Default workflow: start every non-trivial task with `/plan`; have Claude interview you about requirements first.
   - Start with starter-kit prompts — they're copy-paste ready.
   - Track-specific callouts:
     - **Open Lakehouse / Managed Iceberg in UC** — DE track has an optional Iceberg stretch goal in Lab 2.
     - **Genie + AI/BI** — Analyst track creates these in Lab 1.
   - _"Your goal: a working Gold table (or track equivalent) ready by Show & Tell at 14:45."_

4. **Pair formation + track selection** (~2 min)
   - Find your pair. Choose your track. Open the lab guide. Go.

---

### 13:15–14:45 | Lab 1 (track-specific, pairs) (90 min)

> **See track-specific instructions:** [LAB-1-DE.md](LAB-1-DE.md) | [LAB-1-DS.md](LAB-1-DS.md) | [LAB-1-ANALYST.md](LAB-1-ANALYST.md)

> **Note:** The previous "Lab 0 guided hands-on" dissolves into Lab 1's opening 10–15 min. Pairs set up their project, write a CLAUDE.md, and run the first test as part of Phase 1 below.

> **Small Steps enforced at the lab level:** Lab 1 DE has been decomposed into 1–3 min micro-prompts (Phases 1–7) so attendees practise the cadence in their hands. DS and Analyst labs have intro callouts pointing to DE as the template. **No "build me everything" prompts** — every prompt has a verification moment.

**Summary:** Pairs work in their chosen track. DE pairs build a Lakeflow pipeline (Bronze → Silver → Gold). DS pairs build feature tables and run MLflow experiments. Analyst pairs create Genie spaces and AI/BI dashboards.

**Time-boxed phases (approximate):**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: Setup + CLAUDE.md + First Test | 15 min | Project scaffold, CLAUDE.md, write + run first failing test | — |
| Phase 2: Bronze Layer | 20 min | Ingest ABS APIs into raw tables | Checkpoint 1A: pre-loaded bronze tables |
| Phase 3: Silver Layer | 25 min | Transformations, data quality | Checkpoint 1B: pre-loaded silver tables |
| Phase 4: Gold Layer | 20 min | Materialized views, business metrics | Checkpoint 1B: pre-loaded gold tables |
| Phase 5: Deploy + Query | 10 min | Validate, deploy with DABs, query gold tables to confirm end-to-end flow | Checkpoint 1C: complete pipeline code |

**Pair roles (driver/navigator, swap every 15 min):**
- **Driver:** Holds the keyboard, drives the agent terminal, implements.
- **Navigator:** Reads, verifies, flags, suggests. Owns the R.V.P.I. Validate step. Checks tests, reviews git diffs, catches drift.

**Facilitator actions during Lab 1:**
- Circulate every 10 min. Single question per pair: *"Have you validated your CLAUDE.md yet?"*
- At 30 min (13:45): "You should have a test passing — if not, grab Checkpoint 1A."
- At 60 min (14:15): "You should have one Gold table or track equivalent — if not, Checkpoint 1B."
- At 75 min (14:30): "Start wrapping up — Show & Tell in 15 minutes."

**Facilitator Demo Sidebars during Lab 1:** see Facilitation Notes section below.

---

### 14:45–15:00 | Show & Tell (15 min)

**Slide:** Show & Tell

**Format (per track, ~30 sec each):** One highlight per pair — not a full demo, just one thing they're proud of.

**Optional (~5 min):** Query a couple of pairs' Lab 1 Gold tables live to show the room concrete end-state outputs (e.g., "highest food retail turnover by state"). Rotate across pairs.

**Group discussion prompt:** *"Where did Validate help you catch something early? Where did you skip it and regret it?"*

---

### 15:00–15:10 | Break (10 min)

---

### 15:10–16:30 | Lab 2 (track-specific, pairs) (80 min)

> **See track-specific instructions:** [LAB-2-DE.md](LAB-2-DE.md) | [LAB-2-DS.md](LAB-2-DS.md) | [LAB-2-ANALYST.md](LAB-2-ANALYST.md)

**Summary:** Pairs continue in their chosen track. DE pairs add data quality, FSANZ ingest, and scheduling. DS pairs train forecasting models, register them in Unity Catalog with a `@champion` alias, and score predictions — in a notebook by default (Tier 1), or via a Lakeflow batch job using `mlflow.spark_udf` as a stretch (Tier 2). No Model Serving endpoints this lab. Analyst pairs build a FastAPI web app with embedded Genie/dashboards. Skills and MCP are used throughout.

**R.V.P.I. reminder before starting:** *"Before you start, re-read your CLAUDE.md. Is it still current? What drifted during Lab 1?"*

**Time-boxed phases (approximate):**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: Validate + PRD + Tests | 15 min | Audit CLAUDE.md, write PRD, write API tests, start Genie space | — |
| Phase 2: Build | 35 min | Backend, frontend, AI/BI dashboard | Checkpoint 2A: basic app skeleton |
| Phase 3: Wire + Polish | 20 min | Deploy app, test Genie, polish dashboard | Checkpoint 2B: Genie instructions |
| Phase 4: Demo Prep | 10 min | Prepare 3-minute pair demo | Checkpoint 2D: complete solution |

**Pair roles (driver/navigator, swap every 15 min):**
- Same pattern as Lab 1. Rotate driver every 15 min minimum.
- For UI work (Genie space, AI/BI dashboard) the navigator can handle in a second tab while driver works the terminal — parallel tracks within the pair.

**Facilitator actions during Lab 2:**
- At 15 min (15:25): "PRD and tests should be done — agent should be implementing."
- At 40 min (15:50): "Backend should be working — start Genie even if frontend isn't perfect."
- At 60 min (16:10): "Genie space should be created — start AI/BI dashboard if not already."
- At 75 min (16:25): "Start preparing your 3-minute demo!"

**Facilitator Demo Sidebars during Lab 2:** see Facilitation Notes section below.

---

### 16:30–17:00 | Team Demos + Let Go + Takeaways + Close (30 min)

**Slides:** Team Demos & Voting, Let Go of the Code, Key Takeaways, Next Steps, APJ Hackathon, Closing

**Team Demos (~18 min):** Each pair gets 3 minutes to demo:
- Their pipeline (what data, what transformations).
- Their app (show it running, ask the AI a question).
- Their Genie space (ask a natural language question).
- One thing that surprised them — positively or negatively.

**Voting (~3 min):** Each person votes for the best pair (can't vote for own). Criteria:

| Criteria | Weight |
|----------|--------|
| End-to-end completeness (pipeline → app → Genie) | 40% |
| Insight quality (interesting findings, good visualizations) | 30% |
| Creativity (unique features, clever AI use) | 20% |
| Best use of agent (R.V.P.I., CLAUDE.md, small steps) | 10% |

**Let Go of the Code (~3 min):**
- *"The most experienced engineers I work with who use Claude Code best have one thing in common: they care about the system more than they care about the code. They let the agent write the code and they focus on whether the system does what it should. Production identity lives at the interface, not the implementation. That's a skill. It takes practice."*

**Key Takeaways (~3 min):**
1. *R.V.P.I. — name the loop, use it.*
2. *CLAUDE.md is an artifact that rots. Validate it.*
3. *Small Steps every time.*
4. *Verification is the new bottleneck — you own that, no one else does.*

**Next Steps + APJ Hackathon (~2 min):**
- Roll out to wider team, establish pair/team CLAUDE.md standards.
- Build shared skill libraries.
- Explore MCP for internal tools.
- **APJ Building Intelligent Apps Hackathon in May** — build on what you shipped today, $68K in prizes. Details in the email tomorrow.

**Closing (~1 min):** *"Thanks for the day. Go build something."*

**David available for follow-up support.**

---

## Track System

After shared theory and the challenge brief, pairs choose one of three tracks:

| Track | Lab 1 Focus | Lab 2 Focus | Key Tools |
|-------|------------|------------|-----------|
| **Data Engineering** | Lakeflow pipeline (Bronze→Silver→Gold) | Data quality, FSANZ ingest, scheduling | Lakeflow, DABs, @dp.expect |
| **Data Science** | Feature engineering, MLflow experiments | Model training + UC registration + batch inference (notebook default; Lakeflow stretch) | MLflow, Unity Catalog model registry, `mlflow.spark_udf`, scikit-learn |
| **Analyst** | Genie spaces, AI/BI dashboards | FastAPI web app with embedded dashboards | Genie, AI/BI, FastAPI + htmx |

### Track Selection
- Pairs self-select during the Challenge Brief at 13:00 (after lunch, before Lab 1).
- Facilitator should recommend based on pair composition (ML experience → DS, analyst background → Analyst).
- All tracks share the same bronze-layer scaffold set up in Lab 1 Phase 1.

### Track Files
- DE: `LAB-1-DE.md`, `LAB-2-DE.md`, `starter-kit/prompts/de/`
- DS: `LAB-1-DS.md`, `LAB-2-DS.md`, `starter-kit/prompts/ds/`
- Analyst: `LAB-1-ANALYST.md`, `LAB-2-ANALYST.md`, `starter-kit/prompts/analyst/`

---

## Starter Kit

### What It Contains

The `starter-kit/` folder is distributed to every pair at the start. It contains everything pairs need to hit the ground running:

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Pre-written project CLAUDE.md template — pairs customise for their angle |
| `test_stubs/` | Pytest test stubs for both labs — tests are pre-written, pairs just need to run them |
| `prompts/` | Exact copy-paste prompts for every phase of both labs — no interpretation needed |
| `cheatsheet.md` | Quick-reference for Lakeflow syntax, DABs config, FastAPI patterns |
| `config/` | Template `databricks.yml`, `.env` examples, project scaffold |

### How Pairs Use It

1. **During Lab 1 Phase 1:** Copy the CLAUDE.md template and customise it.
2. **At each lab phase:** Open the corresponding prompt file, copy-paste the prompt into the agent.
3. **When stuck:** Check the cheatsheet for syntax reminders.
4. **For tests:** The test stubs define exact expected behavior — pairs don't need to write tests from scratch.

### Key Principle

> Every prompt in the starter-kit is exact copy-paste. No interpretation needed.
> Pairs that follow the prompts in order will have a working platform by the end.

---

## Pair Programming Design

### Why Pairs?

Shipping with AI is a verification problem. Verification is cheaper with a second pair of eyes.

- **Navigator catches drift** — sees what driver misses during rapid iteration.
- **Driver swaps force fresh eyes** — a 15-min swap is a natural V-step.
- **Small Steps cadence** — a navigator asking *"did that actually work?"* every few minutes enforces the discipline.
- **R.V.P.I. gets lived** — navigator owns the Validate step while driver is in Implement.

### Driver / Navigator Roles

**Driver (holds keyboard for 15 min):**
- Types prompts, reviews agent output, accepts/rejects suggestions.
- Runs tests, commits work.
- Stays in flow — doesn't context-switch to reviewing git log.

**Navigator (hands off keyboard for 15 min):**
- Reads agent output alongside driver.
- Verifies against CLAUDE.md and current project state.
- Flags hallucinations, skipped tests, drifting assumptions.
- Owns the R.V.P.I. Validate phase.
- At swap time: hands over with a 30-second status — "what's green, what's red, what's next."

### Swap Protocol

1. At the 15-min mark, driver commits current work.
2. Navigator takes keyboard.
3. Former driver does a 30-second verbal handover.
4. New driver continues.

### For Odd-Numbered Groups (Triads)

One triad forms with an observer who takes notes on what's surprising — not a third driver. Driver + navigator rotate every 15 min; observer rotates in after 30 min.

---

## Checkpoint System

**No pair should ever be stuck.** Pre-loaded checkpoints ensure everyone can participate in demos.

### How Checkpoints Work

Each checkpoint is available as:
1. **Pre-loaded data** in Unity Catalog (tables ready to query).
2. **Code templates** in a shared Git repo (copy and go).

Pairs should try to build it themselves first. Use checkpoints only when falling behind.

### Lab 1 Checkpoints

| Checkpoint | When to Use | What You Get |
|-----------|-------------|-------------|
| **1A: Bronze Tables** | Bronze ingestion failing (API issues, parsing errors) | Pre-loaded `abs_retail_trade_bronze` and `abs_cpi_food_bronze` tables in your schema |
| **1B: Silver + Gold Tables** | Silver/Gold transformations not working at the 60-min mark | Pre-loaded `retail_turnover`, `food_price_index`, `retail_summary`, `food_inflation_yoy` |
| **1C: Complete Pipeline** | Want to focus on Lab 2; need the full pipeline code | Complete pipeline source code + databricks.yml + all tables |

### Lab 2 Checkpoints

| Checkpoint | When to Use | What You Get |
|-----------|-------------|-------------|
| **2A: App Skeleton** | Backend not working at the 40-min mark | Working FastAPI app with health endpoint, data connection, basic structure |
| **2B: Genie Instructions** | Unsure how to create a Genie space | Step-by-step Genie space creation guide with table recommendations |
| **2C: Dashboard Template** | Need help with AI/BI dashboard | Pre-configured dashboard SQL queries and layout suggestions |
| **2D: Complete Solution** | Want a working reference to compare against | Full app code + Genie space + dashboard config |

### Grabbing a Checkpoint

```bash
# In your Coding Agents terminal:
# Copy checkpoint code (David will share the repo URL)
cp -r /Workspace/Shared/workshop-checkpoints/1A/* ./

# Or tell the agent:
# "Copy the bronze checkpoint tables from workshop_vibe_coding.checkpoints
#  into my schema workshop_vibe_coding.<pair_schema>"
```

---

## Concept Coverage Map

| Concept | Where Taught | Where Practiced | Depth |
|---------|-------------|----------------|-------|
| **R.V.P.I. Loop** | Block 4 (10:50, named + demoed) | Both labs (facilitator asks V question on every rotation) | Deep |
| **Agents / Vibe Coding** | Block 2 (live demo) | Both labs | Deep |
| **CLAUDE.md / PRDs** | Block 4 sub-section 2 (10:50+, hands-on) | Lab 1 Phase 1 (first thing pairs write) + Lab 2 Phase 1 (validate) | Deep |
| **Small Steps** | Block 4 sub-section 3 (hands-on through labs) | Both labs (every prompt) | Deep |
| **BDD / TDD with Agents** | Block 4 sub-section 5 | Lab 1 Phase 1 (first test) + both labs | Deep |
| **Power Tools (Skills/MCP/Hooks)** | Block 4 sub-section 4 (live demos) | Both labs (using skills, MCP for docs) | Medium |
| **Sycophancy / Memory-as-untrusted-input** | Block 4 sub-section 6 | Lab checkpoints (facilitator V question) | Medium |
| **Tokens / Context Windows** | Block 4 sub-section 7 | Both labs (context management with /compact) | Light |
| **Lakeflow Pipelines** | Block 2 live demo + Challenge Brief | Lab 1 (DE track, full pipeline) | Deep |
| **Genie Spaces** | Challenge Brief callout + Block 4 tools section | Lab 1/Lab 2 (Analyst track primary) | Medium |
| **AI/BI Dashboards** | Challenge Brief callout | Lab 1/Lab 2 (Analyst + DE) | Medium |
| **Open Lakehouse / Managed Iceberg** | Challenge Brief callout (DE-relevant) | Lab 2 DE stretch goal | Light |

---

## Discussion Questions

### After Lab 1 (Show & Tell)

- Where did Validate help you catch something early? Where did you skip it and regret it?
- What's the most effective prompt you gave the agent today?
- How did the driver/navigator swap feel? What would you change?

### After Lab 2 (Retro)

- What was the most valuable technique you learned today?
- What will you take back to your daily work on Monday?
- Where do you see the biggest opportunity for your team?

### Appendix Discussion Questions (if time permits)

- **Subagents vs Agent Teams:** When would you use subagents vs a full agent team? What's the coordination cost threshold?
- **Context management:** How did you manage context window limits? Did you hit them?
- **Skills adoption:** What custom skills would your team build first?

---

## Platform & Tools

| Tool | Purpose |
|------|---------|
| [Coding Agents Databricks App](https://github.com/dgokeeffe/coding-agents-databricks-apps) | Browser-based terminal with Claude Code, OpenCode, Codex |
| Databricks AI Gateway | Routes LLM calls, model switching, rate limits, cost tracking |
| MLflow Tracing | Auto-traces every agent session for observability |
| Unity Catalog | Data governance, access control, Genie + AI/BI data source |
| Lakeflow Declarative Pipelines | Pipeline orchestration (`@dp.table`, `@dp.materialized_view`) |
| Databricks Asset Bundles (DABs) | Infrastructure-as-code deployment |
| Databricks Apps | Hosting the built web applications |
| Genie | Natural language Q&A on Unity Catalog tables |
| AI/BI Dashboards | Auto-generated visualizations from data |
| [AI Dev Kit Skills](https://github.com/databricks-solutions/ai-dev-kit/tree/main/databricks-skills) | Pre-built Databricks-specific agent skills |

> **Tool-Agnostic Note:** While this workshop uses Claude Code as the primary agent, the
> methodology — R.V.P.I., CLAUDE.md, BDD, context management — transfers to Cursor, Windsurf,
> GitHub Copilot, and any agentic coding tool. The discipline is the differentiator, not the tool.

---

## Facilitation Notes

### Key Principles

1. **Show, don't tell.** Every concept is demoed live before pairs try it.
2. **Real data, real outcomes.** Public Australian data — relevant to Coda' domain.
3. **Fail forward.** When the agent gets something wrong, use it as a teaching moment.
4. **Nobody gets stuck.** Checkpoints ensure every pair can demo something at the end.
5. **Energy over perfection.** It's a hackathon, not an exam.
6. **R.V.P.I. as the recurring question.** When circulating during labs, the single question to ask every pair is *"have you validated your CLAUDE.md / context yet?"*

### Facilitator Demo Sidebars

Four choreographed 60–90 second demos slotted into the labs at natural wait moments. Purpose: fill the dead air inside lab blocks with active teaching, keep energy up across all experience levels, give laggards a visible breather without slowing leaders down.

| When | Duration | Demo | Style | What it teaches |
|---|---|---|---|---|
| Lab 1, ~min 25 (13:40) | 90 sec | **Model Mix Bake-Off** | Live | Haiku vs Sonnet on matched tasks — model selection as technique |
| Lab 1, ~min 60 (14:15) | 90 sec | **Fresh-Context `/review`** | Live (pre-selected pair) | Subagents in practice; one pair gets real feedback |
| Lab 2, ~min 25 (15:35) | 90 sec | **Small-Steps Save** | Pre-recorded video | Big-bang fail vs small-step success — the anti-pattern felt |
| Lab 2, ~min 55 (16:05) | 60 sec | **Commit Cadence** | Live | `/commit` after every green test — the habit that saves work |

**Scripts + pre-flight checklists:** `starter-kit/demos/` (one file per demo + `README.md` index).

**Principles for demo sidebars:**
- **Four is the ceiling.** Beyond this, demos stop being spotlights and start feeling like slowdowns.
- **Live only for predictable behaviour.** If the point depends on the agent doing something specific (arguing with itself, generating flawed code), pre-record. If it depends on something reliably measurable (Haiku is faster than Sonnet for a typo fix), go live.
- **Every demo teaches a habit, not a concept.** Each 90 seconds leaves attendees with something they can do on Monday, not just something they understand better.
- **Consent for any demo that uses a pair's work.** The `/review` demo requires asking first during the 14:00 walk. Never ambush a struggling pair.
- **If a demo fails live, read the fallback paragraph and move on.** Each script has one. Don't try to fix live — cost of a failed attempt is silence; cost of trying to fix is 3–4 lost minutes and a room that's tuned out.

### Timing Flex

- If Block 4 (get-to-know-Claude) runs long: compress the Power Tools sub-section — keep R.V.P.I., CLAUDE.md, Small Steps, BDD, Sycophancy. Cut deep MCP demo.
- If Lab 1 runs long: borrow 5 min from the break, reduce Lab 2 to 75 min.
- If pairs are advanced: extend Lab 2, add bonus challenges (MCP server, custom skills, Iceberg stretch).
- If environment issues: have David's laptop as backup with pre-recorded demos.
- If pairs finish early: bonus challenges in each lab guide, or help other pairs.
- Demos + close at 16:30 has no buffer — keep 30 min tight. If overflow, skip Let Go slide and go straight to takeaways.

### Materials to Prepare

- [ ] **Starter-kit folder** distributed to all pairs (CLAUDE.md template, test stubs, prompts, cheatsheet, config)
- [ ] Checkpoint data pre-loaded in Unity Catalog (`workshop_vibe_coding.checkpoints.*`)
- [ ] Checkpoint code in shared Git repo
- [ ] Coding Agents App instances deployed and tested (1 per participant)
- [ ] Slides for theory sessions (slides.html)
- [ ] Quick-reference cards (printed, 1 per person) (quick-reference.html)
- [ ] R.V.P.I. poster (printed, visible in room) — four-phase diagram
- [ ] Backup: pre-recorded demos on David's laptop

### Pair Formation Tips

- Balance skill levels (1 experienced + 1 newer engineer per pair).
- Mix roles if possible (data engineer + analyst, or DE + DS).
- Assign initial driver/navigator at pair formation — swap every 15 min throughout labs.
- For odd-numbered groups: form one triad with an observer taking notes. Observer rotates in after 30 min.

---

## Pre-Workshop Requirements

> **See [PRE-WORKSHOP-SETUP.md](PRE-WORKSHOP-SETUP.md) for full setup instructions.**

### For the Platform Team (your champions)

1. Deploy Coding Agents App instances (1 per participant).
2. Configure AI Gateway with Claude Opus 4.6 (rate limits: 20 calls/min/user).
3. Unity Catalog setup:
   - Catalog: `workshop_vibe_coding`
   - Per-pair schemas: `workshop_vibe_coding.pair_01` through `pair_05`
   - Shared read-only: `workshop_vibe_coding.checkpoints` (pre-loaded checkpoint data)
   - Shared read-only: `workshop_vibe_coding.raw_data` (source data volumes)
4. Pre-load checkpoint tables at every stage (Bronze, Silver, Gold).
6. Reference-implementation pipeline pre-deployed (needed for 10:10 internal demo).
7. AI/BI dashboard pre-built + open in a tab (needed for 10:10 internal demo).
8. Network verification (ZScaler, WiFi, WebSocket support).
9. Genie space permissions (pairs need CREATE GENIE SPACE).
10. AI/BI dashboard permissions (pairs need CREATE DASHBOARD).
11. End-to-end test from conference room WiFi.

### For Participants

- Laptop with modern browser (Chrome recommended).
- Databricks workspace access (already have).
- No software installation required — everything runs in the browser.
- Optional: think of a project you'd like to try with an agent after the workshop.

---

## Post-Workshop

### Immediate (Same Week)
- Share workshop materials and quick-reference cards.
- Collect feedback survey (keep it short: 3 questions).
- Debrief with platform champions on what to refine.

### Short-Term (2–4 Weeks)
- Refine content based on pilot feedback.
- Schedule full team workshop (end of May 2026).
- Help Coda establish team-wide CLAUDE.md standards and V-step rituals.
- Set up shared skill library repo.

### Long-Term
- Support Coda in building internal MCP servers for their systems.
- Monthly office hours for agentic development questions.
- Track adoption metrics: developer velocity, code quality, satisfaction.

---

## Appendix

### Subagents vs Agent Teams

Moved from main teaching block to appendix — available for overflow or advanced discussion.

- **Subagents = fire-and-forget**
  - Isolated context, one job, result returns to parent.
  - Can't talk to each other — that's a feature (predictable information flow).
  - Key benefit: **compression** — vast exploration distilled to clean signal.
  - Use when: embarrassingly parallel (research, exploration, lookups).

- **Agent Teams = ongoing coordination**
  - Long-running instances with shared state and peer-to-peer messaging.
  - Shared task list with dependencies (`blockedBy`).
  - Key benefit: **negotiation** — discovery in one thread changes what another does.
  - Use when: agents must reconcile outputs before proceeding.

- **The #1 design principle:** Start with a single agent. Push it until it breaks. That failure point tells you exactly what to add. Design around _context boundaries_, not roles.

- **Warning for coding:** Parallel agents writing code make incompatible assumptions — subagents should explore and answer questions, not write code simultaneously with the main agent.

### Skills BDD Chain

How skills chain together in a BDD workflow: write feature/test → run (fail) → implement → run (pass) → commit → deploy. Each step can be a skill.

### MCP Architecture Detail

Detailed MCP architecture diagram and protocol flow for advanced participants who want to build custom MCP servers.

### AI Dev Kit

Pre-built Databricks-specific agent skills from the AI Dev Kit. Overview of available skills and how to install/customise them.

### Rosetta Stone

Cross-platform reference material — maps Claude Code concepts to Cursor, Windsurf, and Copilot equivalents. Useful for attendees who use multiple agents.

### Memory as Untrusted Input

Detailed reference: `notes/rvpi-validate-step.md`. The R.V.P.I. Validate step is the architectural seam through which memory governance becomes a first-class concern in agentic software development.

Four practical mechanisms:
- **Trust-weighted retrieval** — adjust retrieval scores based on provenance.
- **Canonical state auditing** — maintain a reference state against which retrieved memories are compared.
- **Circuit breakers** — halt planning if Validate detects irreconcilable conflict or high staleness.
- **Immutable audit logging** — log all memory reads/writes so poisoned context can be traced.
