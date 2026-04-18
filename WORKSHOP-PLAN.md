# The Great Grocery Data Challenge

## Vibe Coding Workshop: Coles Group

**Client:** Coles Group — Data & AI Engineering Team
**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Format:** Full-day (6.5 hours, 9:30–16:00), Onsite at Coles SSC
**Team Size:** Teams of 2–3, up to 5 teams (10–15 participants)
**Platform:** Coding Agents Databricks App (browser-based terminal)

---

## The Challenge

> You're a team of data engineers at an Australian grocery retailer. Your CEO wants a
> **Grocery Intelligence Platform** that turns public data into actionable insights.
> You have a full day to build it end-to-end: data pipeline, web app, and natural language
> query interface. **May the best team win.**

Each team builds a complete platform using real Australian public data:

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

**Suggested Team Angles** (or invent your own):

| Angle | Key Questions |
|-------|--------------|
| **Retail Performance Tracker** | Which states are growing? What industries are trending? Where should we invest? |
| **Food Inflation Monitor** | Where are prices rising fastest? How does food CPI vary by state? What's the 12-month trend? |
| **Food Safety Dashboard** | What are the recall trends? Which products/companies are most affected? What states are impacted? |
| **Market Intelligence Hub** | Cross-source analysis: how do retail trends, inflation, and safety intersect? |

---

## Learning Objectives

By end of day, participants will be able to:

1. Use conversation to initialize projects and guide AI coding agents (CLAUDE.md, PRDs)
2. Use TDD to dramatically improve agentic code generation accuracy
3. Build and deploy Lakeflow Declarative Pipelines with Databricks Asset Bundles
4. Use **skills** and **MCP** for practical tool integration with agents
5. Connect agents to external tools via **MCP** (Model Context Protocol)
6. Create **Genie spaces** and **AI/BI dashboards** for natural language analytics
7. Ship a working end-to-end application on Databricks
8. (DS) Track and compare experiments with MLflow, train and serve a model
9. (Analyst) Create Genie spaces and AI/BI dashboards for business users

---

## Workshop Rhythm

Every block follows the same pattern for maximum engagement:

```
Theory (15–20 min)  →  Exercise (10–70 min)  →  Discussion (5–15 min)
```

Short, punchy teaching → hands-on practice in teams → share learnings with the group.

---

## Agenda Overview

| Time | Duration | Activity | Mode |
|------|----------|----------|------|
| **9:30** | 15 min | Welcome, Icebreaker: Grocery Data Predictions, Team Formation | Engage |
| **9:45** | 45 min | Theory: Vibe Coding, CLAUDE.md, TDD (Specs → CLAUDE.md → TDD → Context Windows) | Theory |
| **10:30** | 15 min | Break | |
| **10:45** | 45 min | **Lab 0: Guided Hands-On** (initialize project, first test, bronze ingest — ALL together) | Exercise |
| **11:30** | 20 min | Theory: Skills, MCP, Genie, AI/BI Dashboards | Theory |
| **11:50** | 10 min | Track Briefing — choose your track (DE / DS / Analyst) | Briefing |
| **12:00** | 60 min | **Lab 1** (track-specific) | Exercise |
| **13:00** | 15 min | Show & Tell + Prediction Reveal | Discussion |
| **13:15** | 45 min | Lunch | |
| **14:00** | 60 min | **Lab 2** (track-specific) | Exercise |
| **15:00** | 30 min | Team Demos | Discussion |
| **15:30** | 15 min | Takeaways + Close | Wrap-up |
| **15:45** | 15 min | Buffer / Q&A | |

**Time breakdown:** 65 min theory · 45 min guided hands-on · 120 min track labs · 45 min demos/discussion · 15 min icebreaker · 60 min breaks/lunch · 25 min briefings/buffer

---

## Slide Order

| # | Slide | Section |
|---|-------|---------|
| 1 | Title | — |
| 2 | **The AI Coding Moment** — 5 recent reads (Pragmatic Engineer, Thoughtworks, Stack Overflow, CIO, Anthropic) | Welcome |
| 3 | Your Weekly Specials (David's Coles example) | Welcome |
| 4 | Agenda | Welcome |
| 5 | Ice Breaker — Grocery Data Predictions | Welcome |
| 6 | Databricks Today (Platform Overview) | Welcome |
| 7 | Section: The Paradigm Shift | Theory Arc B |
| 8 | What is Vibe Coding | Theory Arc B |
| 8B | CODA — Coding Agents on Databricks Apps (interstitial) | Theory Arc B |
| 9 | Platform Architecture | Theory Arc B |
| 10 | Section: Specs & Testing | Theory Arc C |
| 11 | Why Specs Matter | Theory Arc C |
| 12 | CLAUDE.md in Action | Theory Arc C |
| 13 | CLAUDE.md Scope Levels | Theory Arc C |
| 14 | Rule #1 — Just Say What You Want | Theory Arc C |
| 15 | BDD / TDD Workflow | Theory Arc C |
| 16 | Why BDD / TDD Works with Agents | Theory Arc C |
| 17 | Writing Gherkin / Tests That Guide | Theory Arc C |
| 18 | **Power Tools — Subagents, Skills, Hooks, Plugins** | Theory Arc C |
| 19 | Verification Patterns / Best Practices | Theory Arc C |
| 20 | **The Sycophancy Problem** (was 19B — now numbered) | Theory Arc C |
| 21 | **Small Steps Beat Big Bang** (NEW — the central technique) | Theory Arc C |
| 22 | What Are Tokens | Theory Arc C |
| 23 | Managing Context Windows | Theory Arc C |
| 24 | Live Demo — TDD in Action | Theory Arc C |
| 25 | **What We're Building — End State** (MOVED to pre-Lab-0 motivation slot) | Theory Arc D |
| 26 | **Today's Challenge — Grocery Intelligence Platform** (MOVED) | Theory Arc D |
| 27 | Section: Lab 0 — Guided Hands-On | Lab 0 |
| 28 | Practical Tips for the Labs (5 patterns) | Lab 0 |
| 29 | Section: **Capabilities for Your Track** (renamed from Skills/MCP/Genie) | Session 2 |
| 30 | Skills & Tools — Practical Tools | Session 2 |
| 31 | MCP on Databricks | Session 2 |
| 32 | Demo — How Databricks Uses Claude Internally | Session 2 |
| 33 | **Open Lakehouse — Managed Iceberg in UC** (DE-relevant) | Session 2 |
| 34 | Genie + AI/BI Dashboards (Analyst-relevant) | Session 2 |
| 35 | Section: Lab 1 | Lab 1 |
| 36 | Lab 1 Briefing (with parallel task assignments, incl. Track Briefing) | Lab 1 |
| 37 | Show & Tell + Prediction Reveal | Lab 1 |
| 38 | Section: Lab 2 | Lab 2 |
| 39 | Lab 2 Briefing (with parallel task assignments) | Lab 2 |
| 40 | Team Demos & Voting | Closing |
| 41 | Key Takeaways | Closing |
| 42 | Next Steps | Closing |
| 43 | APJ Building Intelligent Apps Hackathon (teaser) | Closing |
| 44 | Closing | Closing |
| 45 | Appendix Divider | Appendix |
| 46 | Appendix: Subagents, Skills, Hooks & Plugins (full deep-dive) | Appendix |
| 47 | Appendix: Skills for BDD | Appendix |
| 48 | Appendix: Subagents vs Agent Teams | Appendix |
| 49 | Appendix: What is MCP | Appendix |
| 50 | Appendix: How MCP Works | Appendix |
| 51 | Appendix: MCP Architecture on Databricks | Appendix |
| 52 | Appendix: AI Dev Kit | Appendix |
| — | Appendix: Subagents vs Teams | Appendix |
| — | Appendix: Skills TDD Chain | Appendix |
| — | Appendix: MCP Architecture | Appendix |
| — | Appendix: AI Dev Kit | Appendix |

---

## Detailed Agenda

### 9:30–9:45 | Welcome, Industry Context, Icebreaker & Team Formation (15 min)

**Slides:** 1–6 (Title, The AI Coding Moment, Your Weekly Specials, Agenda, Icebreaker, Platform Overview)

**Purpose:** Frame why this matters *now*, show proof it works, orient on the day, form teams, and connect participants to the data they'll be building pipelines for.

**How it works:**

1. **Title + The AI Coding Moment** — industry context (3 min)
   - Name the mixed-experience room: some have used Claude Code for months, some haven't.
   - Walk the 4 stats: 65% weekly adoption (Stack Overflow), METR −19% disconnect (felt 20% faster, were 19% slower), 4h→2m inflection (Dilley, MIT Tech Review), −20% junior dev employment (Stanford).
   - Land the thesis: *"The difference is technique, not tool. Today you learn the technique."*
   - Ask: *"Anyone felt the METR thing — you FEEL faster with AI but the day ends with less done?"* Expect nods from experienced users.
2. **Your Weekly Specials** — proof the technique works (4 min)
   - David's personal example: 4.5M members, 857 commits, 7 weeks spare time, not a data scientist.
   - Transition: *"Here's the shape of the day."*
3. **Agenda** — orient on the day structure (1 min)
   - Theory block → Lab 0 together → track-specific Labs 1 and 2 → demos.
4. **Form teams** of 2–3 (David assigns to balance skill levels) — 1 min
5. **Grocery data predictions** — 3 questions projected, teams discuss and write guesses on prediction cards (no phones!) — 4 min:
   - Q1: Which Australian state has the highest monthly food retail turnover?
   - Q2: By what percentage have Australian food prices (CPI) increased since January 2020?
   - Q3: Which food category has seen the largest price increase since 2020 — dairy, meat, fruit, or bread & cereals?
6. **Each team announces their boldest prediction** — 1 min
7. **The twist:** In Lab 1, you'll build the pipeline that ingests this exact ABS data — during Show & Tell we'll query your Gold tables to reveal the real answers — 1 min

> **Facilitator note:** Answers are hidden on the slide (click to reveal). Do NOT reveal
> during the ice breaker — save the reveal for Show & Tell after Lab 1. Print prediction
> cards in advance. Have a visible scoreboard (whiteboard or shared doc). If the room
> reacts strongly to the METR stat, give it an extra 30s — that resonance is worth the time.

---

### 9:45–10:30 | Theory: Paradigm Shift → Technique → Challenge (45 min)

**Slides:** 6–25 (Databricks Today → Today's Challenge)

**Flow:** Three clear arcs — **Arc B: Paradigm Shift (5 min)** → **Arc C: How to direct agents well (32 min)** → **Arc D: What you're building (3 min, pre-Lab 0 motivation)**

**Concepts covered:** Vibe coding, workshop platform, specs-first approach, CLAUDE.md at three scope levels, TDD workflow, **Power Tools (subagents, skills, hooks, plugins)**, verification patterns, **the sycophancy problem**, context windows, end-state preview, today's challenge

---

#### Arc B — The Paradigm Shift (5 min)

1. **What is vibe coding?** (3 min)
   - The shift from writing code to directing AI agents (Andrej Karpathy, Feb 2025)
   - "You see stuff, you say stuff, you run stuff, and you vibe"
   - Not replacing developers — amplifying them. Tool-agnostic: Claude Code, Cursor, Windsurf, Copilot.

2. **Platform architecture** (2 min)
   - Quick tour of the Coding Agents App (browser-based terminal)
   - Verify everyone can access their instance

---

#### Arc C — The Technique: Specs → Tests → Power Tools → Verification → Context (32 min)

3. **Specs & Testing section divider + Why Specs Matter** (4 min)
   - Garbage in, garbage out — at 100x speed
   - The "brilliant new employee" framing: smart but zero context
   - A good spec = clear acceptance criteria + constraints + example inputs/outputs

4. **CLAUDE.md + Scope Levels + Rule #1** (7 min)
   - Persistent instructions the agent follows on every prompt
   - Three levels: user (`~/.claude/CLAUDE.md`), project, folder
   - Rule #1: Just say what you want — no manual config file edits

5. **TDD/BDD Workflow + Why it works + Writing tests that guide** (8 min)
   - Human writes test (the spec) → agent implements → agent iterates on failures
   - The key insight: structural verification the agent can't bluff
   - _"If you take one thing from today: write the tests first. Always."_
   - Note: labs use pytest; the same principles apply whether you write Gherkin or plain assertions.

6. **Power Tools — Subagents, Skills, Hooks, Plugins** (3 min)
   - For experienced attendees: quick orientation, not deep dive.
   - Subagents: fresh-context workers (`/review`, `Agent` tool)
   - Skills: reusable slash commands from marketplace
   - Hooks: deterministic guardrails (PreToolUse/PostToolUse/Stop) — the live MCP-auth-guard is a real example
   - Plugins: package for teams (Databricks fe-vibe marketplace)
   - _Deep dive: appendix slides 45–47 if time allows._

7. **Verification Patterns / Best Practices** (3 min)
   - Always verify before moving on: run tests, check outputs
   - Plan in chunks, use extended thinking for complex problems
   - Trust but verify

8. **The Sycophancy Problem** (3 min) **← now numbered slide 20, no longer script-only**
   - Stanford Science (Mar 2026): 11 LLMs, 49% more agreement than humans, 51% still agree when user is 100% wrong
   - Karpathy's 4-hour experiment: model demolished its own prior argument when asked to argue the opposite
   - RLHF selected for likeability, not truth
   - Four defenses: Karpathy Test, "Wait a minute..." prefix, structural verification (TDD), Separate prompts
   - _"The discipline of stress-testing AI output is the career skill of this decade."_

9. **Small Steps Beat Big Bang** (3 min) **← NEW slide 21, the central technique**
   - The synthesis of Verification + Sycophancy + Writing Tests: **each prompt = one verifiable step**.
   - Big-bang prompting is learned from ChatGPT; Claude Code rewards tight iteration.
   - 10–20 min wait → attendees sit idle, agent drifts in silence, multiple failures hit at once.
   - 1–3 min prompts → active review, isolated failures, verification every 90 seconds.
   - _Heuristic:_ *"After this prompt, will I KNOW whether it worked?"* If no → split it.
   - **This is also the answer to the "workshop waiting around" problem.** Labs are built around this cadence.

10. **Tokens + Context Windows** (2 min)
   - The unit of "thought" for LLMs — roughly 4 chars per token
   - Context = working memory; use `/compact` when agent starts contradicting itself

11. **Live Demo — TDD in Action** (2 min)
    - 3 failing tests → agent implements → green. The technique in 2 minutes.
    - Uses small-step prompts (from slide 21) so attendees see the cadence in practice.

---

#### Arc D — What You're Building (3 min, pre-Lab 0 motivation)

12. **What We're Building — End State** (2 min) **← MOVED from early theory**
    - Show the complete finished product: pipeline DAG, running web app, Genie, AI/BI dashboard
    - _"By 4pm, every team will have all four of these running. Now let's start."_

13. **Today's Challenge** (1 min) **← MOVED**
    - Grocery Intelligence Platform, 4 data sources, team angles
    - Segue into Lab 0

---

**Key messages:**
- _The work is moving from writing code to orchestrating agents that write code. Today you learn the practices that put you on the leverage side._
- _Specs + Tests + Power Tools + Verification + Context — five techniques. The rest is just typing._
- _Don't trust what the model agrees with. Test what it does._

---

### 10:30–10:45 | Break (15 min)

---

### 10:45–11:30 | Lab 0: Guided Hands-On (45 min)

**Slides:** 27–28 (Section: Lab 0, Practical Tips for the Labs)

**Purpose:** Everyone does the same thing together — guided by the facilitator. By the end, every team has a working CLAUDE.md, a passing bronze test, and has experienced the TDD loop firsthand. This ensures all teams are ready to split into tracks.

**Reference:** [LAB-0-GETTING-STARTED.md](LAB-0-GETTING-STARTED.md) for setup, then guided bronze ingest.

**How it works:**

1. **Rule #1: Just Say What You Want** (10 min)
   - Teams open their Coding Agents terminal
   - Tell Claude about their project — tech stack, data sources, team standards
   - Claude creates the CLAUDE.md, project structure, and initial config
   - Teams review and refine through conversation, not manual editing

   > **Just say:**
   >
   > _"I'm building a grocery intelligence platform on Databricks. Tech stack: PySpark,
   > Lakeflow Declarative Pipelines, FastAPI + React, DABs. Data sources: ABS SDMX APIs,
   > FSANZ web scraping, ACCC PDF ingestion via UC Volumes. Unity Catalog namespace:
   > workshop_vibe_coding.<team_schema>. Set up the project and create a CLAUDE.md."_

2. **Write your first test** (10 min)
   - Teams copy `test_bronze` from `starter-kit/test_pipeline.py`
   - Walk through the test together — what it asserts, why it's structured this way
   - Run the test — it should fail (red)
   - _"This is the spec. The agent now knows exactly what to build."_

3. **Get the agent to pass the test** (20 min)
   - Teams prompt the agent to build the bronze layer ingest
   - Agent reads the failing test, implements the code, runs the test
   - Facilitator circulates — helps teams steer the agent when it drifts
   - Goal: green test, working bronze ingest

4. **Checkpoint + sync** (5 min)
   - Verify every team has a passing bronze test
   - Teams that are stuck: grab Checkpoint 0 (pre-loaded bronze tables)
   - Quick debrief: _"You just did TDD with an agent. That loop is what you'll repeat all day."_

**Facilitator actions during Lab 0:**
- At 10 min: "CLAUDE.md should be done — move to the test"
- At 20 min: "Test should be written and failing — agent should be implementing"
- At 35 min: "Bronze test should be passing — if stuck, grab Checkpoint 0"
- At 40 min: "Start wrapping up — we'll sync in 5 minutes"

**Goal:** Every team has a working CLAUDE.md + passing bronze test before splitting into tracks.

---

### 11:30–11:55 | Theory: Capabilities for Your Track (25 min)

**Slides:** 29–34 (Section: Capabilities for Your Track → Genie + AI/BI Dashboards)

**Concepts covered:** Skills, MCP, **Managed Iceberg in UC (DE track)**, Genie spaces, AI/BI dashboards (Analyst track)

**Framing for this block:** *"These are the Databricks-specific capabilities that amplify what you just learned. Each one matters for at least one of the tracks."*

> **Timing trade:** Block extended from 20 min to 25 min. Subsequent slots shift: Lab 1 Briefing → 11:55, Lab 1 → 12:05–13:05, Show & Tell → 13:05 (10 min, down from 15). Labs remain 60 min each.

**Content:**

1. **Skills & MCP — practical tools** (4 min)
   - Skills: reusable agent capabilities — `/commit`, `/review`, `/test`, plus custom skills
   - MCP: "USB for AI" — open protocol for agents to call external tools
   - Three tiers:
     - **Managed:** Built into Databricks (Unity Catalog, DBSQL, Vector Search)
     - **External:** Community-built (Slack, JIRA, GitHub, Confluence, Databricks Docs)
     - **Custom:** You build them (internal APIs, data tools, monitoring)
   - _"Without MCP, the agent guesses. With MCP, it knows."_

2. **MCP on Databricks + Demo** (4 min)
   - Demo: Use the Databricks Docs MCP to search documentation live
   - Show how MCP connects the agent to real-time data and tools
   - Databricks internal demo of MCP in action

3. **Open Lakehouse — Managed Iceberg in UC** (4 min) **← NEW**
   - Callback to platform-stack slide (Open Formats row): this is what it means in practice.
   - Managed Iceberg tables in UC: `CREATE TABLE ... USING ICEBERG` — no `LOCATION`, `CLUSTER BY` only, same UC governance.
   - External engines (Snowflake, Trino, DuckDB, BigQuery via BigLake) read via Iceberg REST Catalog — **zero copy**.
   - Trade-off: Delta is still deeper (CDF, UniForm, deletion vectors); Iceberg is vendor-neutral interop.
   - DE track Lab 2 has an optional **Iceberg stretch goal** for teams who finish early.

4. **Genie: natural language on your data** (4 min)
   - What it is: AI-powered Q&A interface on Unity Catalog tables
   - How it works: user asks a question → Genie generates SQL → returns results + visualization
   - Demo: create a Genie space on the workshop gold tables, ask a question live
   - Why it matters: business users can self-serve without knowing SQL

5. **AI/BI Dashboards** (4 min)
   - What they are: auto-generated dashboards that understand your data
   - Natural language to visualization: "show me monthly revenue by state as a line chart"
   - Connected to the same Unity Catalog tables
   - Complement to Genie: dashboards for recurring views, Genie for ad-hoc questions

**Key message:** _Skills and MCP extend what agents can do. Open formats (Iceberg) extend who can read your data. Genie and AI/BI put data in the hands of business users._

---

### 11:55–12:05 | Track Briefing — Choose Your Track (10 min)

**Slide:** 30 (Track Briefing — Choose Your Track)

**Content:**

1. **Present the three tracks** (5 min)
   - **Data Engineering:** Lakeflow pipeline (Silver→Gold), data quality, scheduling
   - **Data Science:** Feature engineering, MLflow experiments, model serving
   - **Analyst:** Genie spaces, AI/BI dashboards, FastAPI web app
   - All tracks build on the bronze layer from Lab 0

2. **Teams self-select** (3 min)
   - Facilitator recommends based on team composition (ML experience → DS, analyst background → Analyst)
   - Teams announce their track choice

3. **Practical tips** (3 min)
   - Five patterns: overengineering, hallucinations, course-correct early, challenge & verify, commit as checkpoints
   - Default workflow: start every non-trivial task with `/plan`; have Claude interview you about requirements first
   - After Claude implements, demand proof: "show me the git diff", "grill me on these changes"
   - Commit every 15-20 min — safety net for Esc-Esc rewind
   - Start with the starter-kit prompts — they're copy-paste ready
   - Run tests after every change
   - Use checkpoints if you fall behind — nobody gets stuck
   - _"Your goal: track deliverables ready by Show & Tell at 13:00."_

---

### 12:05–13:05 | Lab 1 (track-specific) (60 min)

> **See track-specific instructions:** [LAB-1-DE.md](LAB-1-DE.md) | [LAB-1-DS.md](LAB-1-DS.md) | [LAB-1-ANALYST.md](LAB-1-ANALYST.md)

> **Small Steps enforced at the lab level:** Lab 1 DE has been decomposed into 1–3 min micro-prompts (Phases 1–7) so attendees practise the cadence from slide 21 in their hands. DS and Analyst labs have intro callouts pointing to DE as the template. **No "build me everything" prompts** — every prompt has a verification moment.

**Summary:** Teams work in their chosen track. DE teams build a Lakeflow pipeline (Silver→Gold) building on the bronze layer from Lab 0. DS teams build feature tables and run MLflow experiments. Analyst teams create Genie spaces and AI/BI dashboards.

**Time-boxed phases with parallel task assignments:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: Tests + Setup | 15 min | Write tests, explore data, set up project | — |
| Phase 2: Bronze Layer | 15 min | Ingest ABS APIs into raw tables | Checkpoint 1A: pre-loaded bronze tables |
| Phase 3: Silver + Gold | 25 min | Transform, enrich, create materialized views | Checkpoint 1B: pre-loaded silver+gold tables |
| Phase 4: Deploy | 5 min | Validate, deploy, query gold tables | Checkpoint 1C: complete pipeline code |

**Parallel Task Assignments — Lab 1:**

| Phase | Person A | Person B | Person C |
|-------|----------|----------|----------|
| **Phase 1** (Tests + Setup, 15 min) | Explore data sources in terminal (curl APIs, inspect responses) | Set up project structure from starter-kit | Read test stubs and data source docs |
| **Phase 2** (Bronze, 15 min) | Build retail trade bronze ingestion | Build CPI food bronze ingestion | Verify UC schema access + prepare checkpoint fallback |
| **Phase 3** (Silver + Gold, 25 min) | Build silver retail transformations | Build silver CPI transformations | Monitor tests + prepare gold layer specs |
| **Phase 4** (Deploy, 5 min) | Validate pipeline + deploy with DABs | Verify tables appear in UC UI | Query gold tables for icebreaker prediction answers |

> **Note for teams of 2:** Combine Person B and Person C tasks. The driver handles
> Person A tasks; the navigator handles Person B + C tasks.

**Facilitator actions during lab:**
- Circulate every 10 min, check progress
- At 15 min: "You should have tests written — if not, grab Checkpoint 1A and skip to Silver"
- At 30 min: "Bronze should be working — if stuck, grab Checkpoint 1A"
- At 50 min: "Gold tables should exist — if not, grab Checkpoint 1B for Lab 2 readiness"

---

### 13:05–13:15 | Show & Tell + Prediction Reveal (10 min)

**Slide:** 33 (Show & Tell + Prediction Reveal)

**Each team (2 min each):**
- Show their pipeline DAG (what tables did you create?)
- Share one interesting insight from their Gold data
- What worked well? Where did they steer the agent?

**Prediction Reveal (3 min):**
- Query the actual data live: _"OK let's check — which state DOES have the highest food retail turnover?"_
- Score the prediction cards from the ice breaker
- Award bragging rights to the most accurate team

**Group discussion prompt:** _"Where did TDD help the agent stay on track? Where did it go off-rails?"_

---

### 13:15–14:00 | Lunch (45 min)

---

### 14:00–15:00 | Lab 2 (track-specific) (60 min)

> **See track-specific instructions:** [LAB-2-DE.md](LAB-2-DE.md) | [LAB-2-DS.md](LAB-2-DS.md) | [LAB-2-ANALYST.md](LAB-2-ANALYST.md)

**Summary:** Teams continue in their chosen track. DE teams add data quality, new sources, and scheduling. DS teams train models, deploy serving endpoints, and build a prediction app. Analyst teams build a FastAPI web app with embedded dashboards. Skills and MCP are used throughout.

**Time-boxed phases with parallel task assignments:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: PRD + Tests + Genie | 10 min | Write PRD, API tests, start Genie space | — |
| Phase 2: Build | 30 min | Backend, frontend, AI/BI dashboard | Checkpoint 2A: basic app skeleton |
| Phase 3: Wire + Polish | 15 min | Deploy app, test Genie, polish dashboard | Checkpoint 2B: Genie space instructions |
| Phase 4: Demo Prep | 5 min | Prepare 3-minute team demo | Checkpoint 2D: complete solution |

**Parallel Task Assignments — Lab 2:**

| Phase | Person A | Person B | Person C |
|-------|----------|----------|----------|
| **Phase 1** (PRD + Tests, 10 min) | Write PRD for the app (use starter-kit template) | Write API tests (use starter-kit test stubs) | Start Genie space in UI (select gold tables, add descriptions) |
| **Phase 2** (Build, 30 min) | Build FastAPI backend (endpoints, data connection) | Build frontend (HTML/Tailwind/htmx) | Create AI/BI dashboard in UI (charts, filters, layout) |
| **Phase 3** (Wire + Polish, 15 min) | Deploy app to Databricks Apps | Test Genie space + refine instructions/descriptions | Polish dashboard + get embed URL |
| **Phase 4** (Demo Prep, 5 min) | All: prepare 3-minute demo | All: pick best Genie question | All: rehearse narrative |

> **Note for teams of 2:** Person A handles backend + deployment. Person B handles
> frontend + Genie + dashboard (Genie and dashboard are UI tasks that run in parallel).

**Facilitator actions during lab:**
- At 10 min: "PRD and tests should be done — agent should be implementing"
- At 30 min: "Backend should be working — start on Genie space even if frontend isn't perfect"
- At 45 min: "Genie space should be created — start AI/BI dashboard if not already"
- At 55 min: "Start preparing your 3-minute demo!"

---

### 15:00–15:30 | Team Demos, Voting & Retro (30 min)

**Slide:** 36 (Team Demos & Voting)

**Team Demos (18 min):** Each team gets 3 minutes to demo:
- Their pipeline (what data, what transformations)
- Their app (show it running, ask the AI a question)
- Their Genie space (ask a natural language question)
- One thing that surprised them

**Voting (5 min):** Each person votes for the best team (can't vote for yourself). Criteria:

| Criteria | Weight |
|----------|--------|
| End-to-end completeness (pipeline → app → Genie) | 40% |
| Insight quality (interesting findings, good visualizations) | 30% |
| Creativity (unique features, clever AI use) | 20% |
| Best use of agent (TDD, CLAUDE.md, steering) | 10% |

**Retro (7 min):** Quick group discussion:
- What was the most valuable technique you learned today?
- What will you take back to your daily work on Monday?
- Where do you see the biggest opportunity for your team?

---

### 15:30–15:45 | Takeaways + Close (15 min)

**Slides:** 37–39 (Key Takeaways, Next Steps, Closing)

**Key takeaways:**
1. _CLAUDE.md and PRDs are your leverage multipliers_
2. _TDD + agents = deterministic outcomes_
3. _Skills and MCP extend agents from code to systems_
4. _Genie + AI/BI puts data in everyone's hands_

**Next steps:**
- Roll out to wider team, establish team CLAUDE.md standards
- Build shared skill libraries
- Explore MCP for internal tools

**David available for follow-up support.**

---

### 15:45–16:00 | Buffer / Q&A (15 min)

Open floor for questions, extra demos, or overflow from any session.

---

## Track System

After the shared theory sessions, teams choose one of three tracks:

| Track | Lab 1 Focus | Lab 2 Focus | Key Tools |
|-------|------------|------------|-----------|
| **Data Engineering** | Lakeflow pipeline (Bronze→Silver→Gold) | Data quality, new sources, scheduling | Lakeflow, DABs, @dp.expect |
| **Data Science** | Feature engineering, MLflow experiments | Model training, serving, prediction app | MLflow, Model Serving, scikit-learn |
| **Analyst** | Genie spaces, AI/BI dashboards | FastAPI web app with embedded dashboards | Genie, AI/BI, FastAPI + htmx |

### Track Selection
- Teams self-select during the Track Briefing at 11:50 (after Lab 0, before Lab 1)
- Facilitator should recommend based on team composition (ML experience → DS, analyst background → Analyst)
- All tracks share the same bronze layer built in Lab 0 + gold tables via Checkpoint 0

### Track Files
- Shared: `LAB-0-GETTING-STARTED.md` (all tracks do this first)
- DE: `LAB-1-DE.md`, `LAB-2-DE.md`, `starter-kit/prompts/de/`
- DS: `LAB-1-DS.md`, `LAB-2-DS.md`, `starter-kit/prompts/ds/`
- Analyst: `LAB-1-ANALYST.md`, `LAB-2-ANALYST.md`, `starter-kit/prompts/analyst/`

---

## Starter Kit

### What It Contains

The `starter-kit/` folder is distributed to every team at the start. It contains everything teams need to hit the ground running:

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Pre-written project CLAUDE.md template — teams customise for their angle |
| `test_stubs/` | Pytest test stubs for both labs — tests are pre-written, teams just need to run them |
| `prompts/` | Exact copy-paste prompts for every phase of both labs — no interpretation needed |
| `cheatsheet.md` | Quick-reference for Lakeflow syntax, DABs config, FastAPI patterns |
| `config/` | Template `databricks.yml`, `.env` examples, project scaffold |

### How Teams Use It

1. **During Lab 0 (Guided Hands-On):** Copy the CLAUDE.md template and customise it
2. **At each lab phase:** Open the corresponding prompt file, copy-paste the prompt into the agent
3. **When stuck:** Check the cheatsheet for syntax reminders
4. **For tests:** The test stubs define exact expected behavior — teams don't need to write tests from scratch

### Key Principle

> Every prompt in the starter-kit is exact copy-paste. No interpretation needed.
> Teams that follow the prompts in order will have a working platform by the end.

---

## Parallel Task Design

### Why Parallel Tasks?

Teams of 3 can achieve far more when each person works on a different piece simultaneously. The parallel task assignments ensure:

- **No idle time** — everyone has something to do at every phase
- **Clear ownership** — no confusion about who's doing what
- **Natural checkpoints** — phases end with integration points where the team syncs up
- **Resilience** — if one person is stuck, the others are still making progress

### How It Works

1. **Briefing slide** shows the task table for each phase
2. Teams assign Person A/B/C at the start of each lab
3. Each person works on their task independently (separate terminal or UI)
4. At phase boundaries, the team syncs: "What's done? What's blocked? What's next?"
5. Person C often handles UI tasks (Genie, dashboards) that don't need the agent terminal

### For Teams of 2

Combine Person B and Person C tasks. One person drives the agent; the other handles UI tasks, testing, and review. Rotate roles between labs.

---

## Checkpoint System

**No team should ever be stuck.** Pre-loaded checkpoints ensure everyone can participate in demos.

### How Checkpoints Work

Each checkpoint is available as:
1. **Pre-loaded data** in Unity Catalog (tables ready to query)
2. **Code templates** in a shared Git repo (copy and go)

Teams should try to build it themselves first. Use checkpoints only when falling behind.

### Lab 1 Checkpoints

| Checkpoint | When to Use | What You Get |
|-----------|-------------|-------------|
| **1A: Bronze Tables** | Bronze ingestion failing (API issues, parsing errors) | Pre-loaded `abs_retail_trade_bronze` and `abs_cpi_food_bronze` tables in your schema |
| **1B: Silver + Gold Tables** | Silver transformations not working at the 50-min mark | Pre-loaded `retail_turnover`, `food_price_index`, `retail_summary`, `food_inflation_yoy` |
| **1C: Complete Pipeline** | Want to focus on Lab 2; need the full pipeline code | Complete pipeline source code + databricks.yml + all tables |

### Lab 2 Checkpoints

| Checkpoint | When to Use | What You Get |
|-----------|-------------|-------------|
| **2A: App Skeleton** | Backend not working at the 30-min mark | Working FastAPI app with health endpoint, data connection, basic structure |
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
#  into my schema workshop_vibe_coding.<team_schema>"
```

---

## Concept Coverage Map

| Concept | Where Taught | Where Practiced | Depth |
|---------|-------------|----------------|-------|
| **Agents / Vibe Coding** | Theory (9:45, demo + theory) | Lab 0 + both labs | Deep |
| **CLAUDE.md / PRDs** | Theory (9:45, theory) | Lab 0 (first thing teams write) | Deep |
| **TDD with Agents** | Theory (9:45, theory + demo) | Lab 0 (first test + bronze) + both labs | Deep |
| **Tokens / Context Windows** | Theory (9:45, theory) | All labs (context management) | Light |
| **Skills** | Session 2 (11:30, overview) | Both labs (using skills throughout) | Medium |
| **Lakeflow Pipelines** | Lab 0 (10:45, guided) + Track Briefing (11:50) | Lab 0 + Lab 1 (build full pipeline) | Deep |
| **MCP** | Session 2 (11:30, demo + tiers) | Lab 2 (Databricks docs MCP) | Medium |
| **Genie Spaces** | Session 2 (11:30, demo) | Lab 1/Lab 2 (create Genie space) | Medium |
| **AI/BI Dashboards** | Session 2 (11:30, demo) | Lab 1/Lab 2 (create dashboard) | Medium |

---

## Discussion Questions

### After Lab 1 (Show & Tell)

- Where did TDD help the agent stay on track? Where did it go off-rails?
- What's the most effective prompt you gave the agent today?
- How did parallel tasks work for your team? What would you change?

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
> methodology — PRDs, CLAUDE.md, TDD, context management — transfers to Cursor, Windsurf,
> GitHub Copilot, and any agentic coding tool. The discipline is the differentiator, not the tool.

---

## Facilitation Notes

### Key Principles

1. **Show, don't tell.** Every concept is demoed live before teams try it.
2. **Real data, real outcomes.** Public Australian data — relevant to Coles' domain.
3. **Fail forward.** When the agent gets something wrong, use it as a teaching moment.
4. **Nobody gets stuck.** Checkpoints ensure every team can demo something at the end.
5. **Energy over perfection.** It's a hackathon, not an exam.

### Timing Flex

- If theory runs long: compress Session 2 to 15 min (cut Databricks internal demo)
- If Lab 0 runs long: borrow 5 min from the break, but ensure every team has a passing test
- If Lab 1 runs long: borrow 5 min from lunch, reduce Lab 2 to 55 min
- If teams are advanced: extend Lab 2, add bonus challenges (MCP server, custom skills)
- If environment issues: have David's laptop as backup with pre-recorded demos
- If teams finish early: bonus challenges in each lab guide, or help other teams
- Buffer at 15:45 absorbs any overflow from demos or Q&A

### Materials to Prepare

- [ ] Prediction cards (printed, 1 per team — grocery data questions for Show & Tell reveal)
- [ ] Scoreboard (whiteboard or shared Google Sheet)
- [ ] **Starter-kit folder** distributed to all teams (CLAUDE.md template, test stubs, prompts, cheatsheet, config)
- [ ] Checkpoint data pre-loaded in Unity Catalog (`workshop_vibe_coding.checkpoints.*`)
- [ ] Checkpoint code in shared Git repo
- [ ] Coding Agents App instances deployed and tested
- [ ] Slides for theory sessions (slides.html)
- [ ] Quick-reference cards (printed, 1 per person) (quick-reference.html)
- [ ] Backup: pre-recorded demos on David's laptop

### Team Formation Tips

- Balance skill levels (1 experienced + 1-2 newer engineers per team)
- Mix roles if possible (data engineer + analyst, or DE + DS)
- Assign Person A/B/C roles at team formation — rotate between labs
- Person A: primary agent driver; Person B: secondary agent driver; Person C: UI tasks + review

---

## Pre-Workshop Requirements

> **See [PRE-WORKSHOP-SETUP.md](PRE-WORKSHOP-SETUP.md) for full setup instructions.**

### For Platform Team (Farbod & Swee Hoe)

1. Deploy Coding Agents App instances (1 per participant)
2. Configure AI Gateway with Claude Opus 4.6 (rate limits: 20 calls/min/user)
3. Unity Catalog setup:
   - Catalog: `workshop_vibe_coding`
   - Per-team schemas: `workshop_vibe_coding.team_01` through `team_05`
   - Shared read-only: `workshop_vibe_coding.checkpoints` (pre-loaded checkpoint data)
   - Shared read-only: `workshop_vibe_coding.raw_data` (source data volumes)
4. Pre-load checkpoint tables at every stage (Bronze, Silver, Gold)
5. Network verification (ZScaler, WiFi, WebSocket support)
6. Genie space permissions (teams need CREATE GENIE SPACE)
7. AI/BI dashboard permissions (teams need CREATE DASHBOARD)
8. End-to-end test from conference room WiFi

### For Participants

- Laptop with modern browser (Chrome recommended)
- Databricks workspace access (already have)
- No software installation required — everything runs in the browser
- Optional: think of a project you'd like to try with an agent after the workshop

---

## Post-Workshop

### Immediate (Same Week)
- Share workshop materials and quick-reference cards
- Collect feedback survey (keep it short: 3 questions)
- Debrief with Yass, Swee Hoe, Farbod on what to refine

### Short-Term (2–4 Weeks)
- Refine content based on pilot feedback
- Schedule full team workshop (end of March / early April 2026)
- Help Coles establish team-wide CLAUDE.md standards
- Set up shared skill library repo

### Long-Term
- Support Coles in building internal MCP servers for their systems
- Monthly office hours for agentic development questions
- Track adoption metrics: developer velocity, code quality, satisfaction

---

## Appendix

### Subagents vs Agent Teams

Moved from Session 3 to appendix — available for overflow or advanced discussion.

- **Subagents = fire-and-forget**
  - Isolated context, one job, result returns to parent
  - Can't talk to each other — that's a feature (predictable information flow)
  - Key benefit: **compression** — vast exploration distilled to clean signal
  - Use when: embarrassingly parallel (research, exploration, lookups)

- **Agent Teams = ongoing coordination**
  - Long-running instances with shared state and peer-to-peer messaging
  - Shared task list with dependencies (`blockedBy`)
  - Key benefit: **negotiation** — discovery in one thread changes what another does
  - Use when: agents must reconcile outputs before proceeding

- **The #1 design principle:** Start with a single agent. Push it until it breaks. That failure point tells you exactly what to add. Design around _context boundaries_, not roles.

- **Warning for coding:** Parallel agents writing code make incompatible assumptions — subagents should explore and answer questions, not write code simultaneously with the main agent

### Skills TDD Chain

How skills chain together in a TDD workflow: write test → run test (fail) → implement → run test (pass) → commit → deploy. Each step can be a skill.

### MCP Architecture Detail

Detailed MCP architecture diagram and protocol flow for advanced participants who want to build custom MCP servers.

### AI Dev Kit

Pre-built Databricks-specific agent skills from the AI Dev Kit. Overview of available skills and how to install/customise them.
