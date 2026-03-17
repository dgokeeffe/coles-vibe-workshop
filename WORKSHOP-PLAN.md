# The Great Grocery Data Challenge

## Vibe Coding Workshop: Coles Group

**Client:** Coles Group — Data & AI Engineering Team
**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Format:** Half-day (5 hours), Onsite at Coles SSC
**Team Size:** Teams of 2–3, up to 5 teams (10–15 participants)
**Platform:** Coding Agents Databricks App (browser-based terminal)

---

## The Challenge

> You're a team of data engineers at an Australian grocery retailer. Your CEO wants a
> **Grocery Intelligence Platform** that turns public data into actionable insights.
> You have 5 hours to build it end-to-end: data pipeline, web app, and natural language
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

1. Write effective CLAUDE.md files and PRDs that guide AI coding agents
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

| Time | Duration | Block | Type |
|------|----------|-------|------|
| **9:00** | 15 min | Welcome, Icebreaker: Grocery Data Predictions, Team Formation | Engage |
| **9:15** | 10 min | Vibe Coding + Platform + What We're Building (show end state) | Theory |
| **9:25** | 5 min | Today's Challenge Details | Theory |
| **9:30** | 15 min | Why Specs Matter + CLAUDE.md (scope levels, in action) | Theory |
| **9:45** | 15 min | Exercise: Write Your CLAUDE.md (use starter-kit) | Exercise |
| **10:00** | 10 min | Break | |
| **10:10** | 15 min | TDD (workflow, why it works, writing tests that guide) | Theory |
| **10:25** | 5 min | Tokens + Context Windows + Live Demo | Theory |
| **10:30** | 5 min | Lab 1 Briefing + Practical Tips | Briefing |
| **10:35** | 55 min | **Lab 1: Build Your Data Pipeline** (parallel tasks) | Exercise |
| **11:30** | 10 min | Show & Tell + Prediction Reveal | Discussion |
| **11:40** | 30 min | Lunch | |
| **12:10** | 15 min | Skills, MCP, Genie + AI/BI Dashboards | Theory |
| **12:25** | 5 min | Lab 2 Briefing | Briefing |
| **12:30** | 55 min | **Lab 2: Build Your App & Dashboard** (parallel tasks) | Exercise |
| **13:25** | 10 min | Break | |
| **13:35** | 20 min | Team Demos, Voting & Retro | Discussion |
| **13:55** | 5 min | Key Takeaways + Next Steps + Closing | Closing |
| **14:00** | — | End | |

**Time breakdown:** 70 min theory · 125 min hands-on · 30 min discussion · 15 min icebreaker · 50 min breaks/lunch · 10 min briefings

---

## Slide Order

| # | Slide | Section |
|---|-------|---------|
| 1 | Title | — |
| 2 | Opening Demo | — |
| 3 | Icebreaker — Grocery Data Predictions | Welcome |
| 4 | Agenda (updated) | Welcome |
| 5 | Databricks Platform Overview | Welcome |
| 6 | Section: The Paradigm Shift | Session 1 |
| 7 | What is Vibe Coding | Session 1 |
| 8 | Platform Architecture | Session 1 |
| 9 | **What We're Building — End State** (pipeline + app + Genie + dashboard) | Session 1 |
| 10 | Today's Challenge — Grocery Intelligence Platform | Session 1 |
| 11 | Section: Specs & TDD (merged session) | Session 1 |
| 12 | Why Specs Matter | Session 1 |
| 13 | CLAUDE.md in Action | Session 1 |
| 14 | CLAUDE.md Scope Levels | Session 1 |
| 15 | Exercise: Write Your CLAUDE.md | Session 1 |
| 16 | TDD Workflow | Session 1 |
| 17 | Why TDD is Exponentially More Powerful | Session 1 |
| 18 | Writing Tests That Guide | Session 1 |
| 19 | Best Practices — Verification & Planning | Session 1 |
| 20 | What Are Tokens | Session 1 |
| 21 | Managing Context Windows | Session 1 |
| 22 | Live Demo — TDD in Action | Session 1 |
| 23 | Section: Lab 1 | Lab 1 |
| 24 | Practical Tips | Lab 1 |
| 25 | Lab 1 Briefing (with parallel task assignments) | Lab 1 |
| 26 | Show & Tell + Prediction Reveal | Lab 1 |
| 27 | Section: Tools for Lab 2 | Session 2 |
| 28 | **Skills & MCP — Practical Tools** (condensed) | Session 2 |
| 29 | MCP on Databricks | Session 2 |
| 30 | Databricks Internal Demo | Session 2 |
| 31 | Genie + AI/BI Dashboards | Session 2 |
| 32 | Section: Lab 2 | Lab 2 |
| 33 | Lab 2 Briefing (with parallel task assignments) | Lab 2 |
| 34 | Team Demos & Voting | Closing |
| 35 | Key Takeaways | Closing |
| 36 | Next Steps | Closing |
| 37 | Closing | Closing |
| — | Appendix: Subagents vs Teams | Appendix |
| — | Appendix: Skills TDD Chain | Appendix |
| — | Appendix: MCP Architecture | Appendix |
| — | Appendix: AI Dev Kit | Appendix |

---

## Detailed Agenda

### 9:00–9:15 | Welcome, Icebreaker & Team Formation (15 min)

**Slides:** 1–5 (Title, Opening Demo, Icebreaker, Agenda, Platform Overview)

**Purpose:** Form teams, get energy up, and connect participants to the data they'll be building pipelines for.

**How it works:**

1. **Form teams** of 2–3 (David assigns to balance skill levels) — 2 min
2. **Grocery data predictions** — project 5 questions on screen, teams discuss and write their best guesses on prediction cards (30 seconds each, no phones!) — 8 min:
   - Q1: Which Australian state has the highest monthly food retail turnover?
   - Q2: By what percentage have Australian food prices (CPI) increased since January 2020?
   - Q3: How much does the average Australian household spend on groceries per week?
   - Q4: What month of the year do Australians spend the most on retail?
   - Q5: Which food category has seen the largest price increase since 2020 — dairy, meat, fruit, or bread & cereals?
3. **Each team picks their boldest prediction** and announces it — 3 min
4. **The twist:** In Lab 1, you'll build the pipeline that ingests this exact ABS data — and during Show & Tell, we'll query your Gold tables to reveal the real answers — 2 min explanation

> **Facilitator note:** Answers are hidden on the slide (click to reveal). Do NOT reveal
> during the ice breaker — save the reveal for Show & Tell after Lab 1. Print prediction
> cards in advance. Have a visible scoreboard (whiteboard or shared doc).

---

### 9:15–9:25 | Vibe Coding + Platform + What We're Building (10 min)

**Slides:** 6–10 (Section: The Paradigm Shift, What is Vibe Coding, Platform Architecture, What We're Building — End State, Today's Challenge)

**Concepts covered:** Vibe coding basics, platform architecture, end-state preview, challenge overview

**Content:**

1. **What is vibe coding?** (3 min)
   - The shift from writing code to directing AI agents (Andrej Karpathy, Feb 2025)
   - "You see stuff, you say stuff, you run stuff, and you vibe"
   - Not replacing developers — amplifying them 10x
   - Tool-agnostic: Claude Code, Cursor, Windsurf, GitHub Copilot, OpenCode — the patterns transfer

2. **Platform architecture** (2 min)
   - Quick tour of the Coding Agents App (browser-based terminal)
   - Show where Claude Code, OpenCode, and Codex are available
   - Verify everyone can access their instance

3. **What we're building — end state** (3 min)
   - Show the complete finished product: pipeline DAG, running web app, Genie space answering questions, AI/BI dashboard with live metrics
   - _"By 2pm, every team will have all four of these running."_
   - This is the north star — everything today builds toward this

4. **Today's challenge details** (2 min)
   - Grocery Intelligence Platform: 4 data sources, 4 deliverables
   - Team angles: Retail Performance, Food Inflation, Food Safety, Market Intelligence
   - Scoring criteria preview

**Key message:** _You've just seen the end state. Every session from here gives you the skills and tools to build it._

---

### 9:25–9:30 | Today's Challenge Details (5 min)

**Slide:** 10 (Today's Challenge — Grocery Intelligence Platform)

**Content:**

- Walk through the four data sources and what each provides
- Explain the four deliverables (pipeline, app, Genie space, dashboard)
- Teams pick their angle (or invent their own)
- Briefly show the starter-kit folder and what's inside

---

### 9:30–9:45 | Why Specs Matter + CLAUDE.md (15 min)

**Slides:** 11–14 (Section: Specs & TDD, Why Specs Matter, CLAUDE.md in Action, CLAUDE.md Scope Levels)

**Concepts covered:** Specs-first approach, CLAUDE.md at three scope levels, PRDs for agents

**Content:**

1. **Why specs matter MORE with AI** (5 min)
   - Garbage in, garbage out — at 100x speed
   - The "brilliant new employee" framing: your agent is smart but has zero context
   - A good spec = clear acceptance criteria + constraints + example inputs/outputs
   - The agent treats the spec as its "definition of done"

2. **CLAUDE.md: Your team's DNA** (5 min)
   - What it is: persistent instructions the agent follows on every prompt
   - Three levels: user (`~/.claude/CLAUDE.md`), project (repo root), folder-level
   - What to put in it: tech stack, coding standards, architecture decisions, data contracts
   - Live example: David's personal CLAUDE.md and how adding one line changes behavior

3. **CLAUDE.md in action** (3 min)
   - Live demo: show a before/after — same prompt with and without CLAUDE.md
   - Highlight how the agent's output changes dramatically with good context

4. **CLAUDE.md scope levels** (2 min)
   - User-level: personal preferences, coding style
   - Project-level: tech stack, standards, architecture
   - Folder-level: module-specific rules (e.g., "all files in /pipelines use @dp.table")

**Key message:** _The best engineers will be those who can effectively direct AI agents. CLAUDE.md and PRDs are your leverage multipliers._

---

### 9:45–10:00 | Exercise: Write Your CLAUDE.md (15 min)

**Slide:** 15 (Exercise: Write Your CLAUDE.md)

**Task:** Each team uses the starter-kit CLAUDE.md template and customises it for their team's chosen angle.

**How it works:**

1. Teams open their Coding Agents terminal
2. Copy the starter-kit CLAUDE.md into their project
3. Customise it with their team angle, schema name, and any team-specific standards
4. The starter-kit prompt is exact copy-paste — no interpretation needed

**Prompt to give teams:**

> Open your Coding Agents terminal and run:
>
> _"Copy the starter-kit CLAUDE.md into our project. Customise it for our team:
> schema `workshop_vibe_coding.<team_schema>`, angle `<chosen_angle>`.
> Add our tech stack (PySpark, Lakeflow Declarative Pipelines, FastAPI,
> Tailwind CSS + htmx), our data standards (Unity Catalog, medallion architecture,
> date formats), and our testing standards (pytest, TDD, small test DataFrames)."_

**While teams work:** David circulates, helps teams refine their CLAUDE.md, answers questions.

---

### 10:00–10:10 | Break (10 min)

---

### 10:10–10:25 | TDD with Agents (15 min)

**Slides:** 16–19 (TDD Workflow, Why TDD is Exponentially More Powerful, Writing Tests That Guide, Best Practices — Verification & Planning)

**Concepts covered:** TDD workflow with agents, writing tests that guide, verification strategies

**Content:**

1. **TDD as the secret weapon** (5 min)
   - Tests are unambiguous specs that agents can verify against
   - The TDD + Agent workflow:
     1. Human writes test (the spec)
     2. Agent implements code to pass tests
     3. Agent runs tests, reads failures, fixes code
     4. Human reviews, adds edge cases
   - _"If you take one thing from today: write the tests first. Always."_

2. **Why TDD is exponentially more powerful with agents** (3 min)
   - Humans: tests catch bugs after the fact
   - Agents: tests define the target _before_ code exists
   - The agent reads the failure message and knows exactly what to fix
   - Compound effect: each passing test constrains the next implementation

3. **Writing tests that guide** (4 min)
   - Good test: specific, small DataFrame, exact expected output
   - Bad test: vague assertions, large datasets, "it should work"
   - Example: test for a silver transformation with 3 rows in, 3 rows out
   - Tests as documentation: the next developer (or agent) reads the tests first

4. **Best practices: verification & planning** (3 min)
   - Always verify before moving on: run tests, check outputs, inspect data
   - Plan in chunks: don't ask the agent to build everything at once
   - Use `ultrathink` / extended thinking for complex problems
   - Review agent output — trust but verify

**Key message:** _TDD + agents = deterministic outcomes. Tests ARE your spec._

---

### 10:25–10:30 | Tokens + Context Windows + Live Demo (5 min)

**Slides:** 20–22 (What Are Tokens, Managing Context Windows, Live Demo — TDD in Action)

**Content:**

1. **What are tokens?** (1 min)
   - The unit of "thought" for LLMs — roughly 4 chars per token
   - Context window = working memory (how much the agent can hold at once)

2. **Managing context windows** (2 min)
   - Why it matters: agent forgets things when context fills up
   - Strategies: keep prompts focused, use CLAUDE.md instead of repeating instructions, use `/compact`
   - Warning signs: agent starts contradicting itself, forgets earlier decisions

3. **Live demo: TDD in action** (2 min)
   - Quick demo: 3 failing tests → agent implements → green
   - Show the agent reading failure messages, fixing code, iterating

---

### 10:30–10:35 | Lab 1 Briefing + Practical Tips (5 min)

**Slides:** 23–25 (Section: Lab 1, Practical Tips, Lab 1 Briefing)

**Content:**

1. **Practical tips** (2 min)
   - Start with the starter-kit prompts — they're copy-paste ready
   - Run tests after every change
   - Use checkpoints if you fall behind — nobody gets stuck

2. **Lab 1 briefing** (3 min)
   - Walk through the four phases and timing
   - Explain the parallel task assignments (see below)
   - Remind teams about checkpoints
   - _"Your goal: Gold tables queryable by Show & Tell at 11:30."_

---

### 10:35–11:30 | Lab 1: Build Your Data Pipeline (55 min)

> **See track-specific instructions:** [LAB-1-DE.md](LAB-1-DE.md) | [LAB-1-DS.md](LAB-1-DS.md) | [LAB-1-ANALYST.md](LAB-1-ANALYST.md)
>
> All teams start with [LAB-0-GETTING-STARTED.md](LAB-0-GETTING-STARTED.md), then fork into their chosen track.

**Summary:** Teams fork into their chosen track after completing LAB-0 setup. DE teams build a Lakeflow pipeline (Bronze→Silver→Gold). DS teams build feature tables and run MLflow experiments. Analyst teams create Genie spaces and AI/BI dashboards.

**Time-boxed phases with parallel task assignments:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: Tests + Setup | 15 min | Write tests, explore data, set up project | — |
| Phase 2: Bronze Layer | 15 min | Ingest ABS APIs into raw tables | Checkpoint 1A: pre-loaded bronze tables |
| Phase 3: Silver + Gold | 20 min | Transform, enrich, create materialized views | Checkpoint 1B: pre-loaded silver+gold tables |
| Phase 4: Deploy | 5 min | Validate, deploy, query gold tables | Checkpoint 1C: complete pipeline code |

**Parallel Task Assignments — Lab 1:**

| Phase | Person A | Person B | Person C |
|-------|----------|----------|----------|
| **Phase 1** (Tests + Setup, 15 min) | Explore data sources in terminal (curl APIs, inspect responses) | Set up CLAUDE.md + project structure from starter-kit | Read test stubs and data source docs |
| **Phase 2** (Bronze, 15 min) | Build retail trade bronze ingestion | Build CPI food bronze ingestion | Verify UC schema access + prepare checkpoint fallback |
| **Phase 3** (Silver + Gold, 20 min) | Build silver retail transformations | Build silver CPI transformations | Monitor tests + prepare gold layer specs |
| **Phase 4** (Deploy, 5 min) | Validate pipeline + deploy with DABs | Verify tables appear in UC UI | Query gold tables for icebreaker prediction answers |

> **Note for teams of 2:** Combine Person B and Person C tasks. The driver handles
> Person A tasks; the navigator handles Person B + C tasks.

**Facilitator actions during lab:**
- Circulate every 10 min, check progress
- At 15 min: "You should have tests written — if not, grab Checkpoint 1A and skip to Silver"
- At 30 min: "Bronze should be working — if stuck, grab Checkpoint 1A"
- At 45 min: "Gold tables should exist — if not, grab Checkpoint 1B for Lab 2 readiness"

---

### 11:30–11:40 | Show & Tell + Prediction Reveal (10 min)

**Slide:** 26 (Show & Tell + Prediction Reveal)

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

### 11:40–12:10 | Lunch (30 min)

---

### 12:10–12:25 | Session 2: Skills, MCP, Genie & AI/BI Dashboards (15 min)

**Slides:** 27–31 (Section: Tools for Lab 2, Skills & MCP — Practical Tools, MCP on Databricks, Databricks Internal Demo, Genie + AI/BI Dashboards)

**Concepts covered:** Skills, MCP, Genie spaces, AI/BI dashboards

**Content:**

1. **Skills & MCP — practical tools** (5 min)
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

3. **Genie: natural language on your data** (3 min)
   - What it is: AI-powered Q&A interface on Unity Catalog tables
   - How it works: user asks a question → Genie generates SQL → returns results + visualization
   - Demo: create a Genie space on the workshop gold tables, ask a question live
   - Why it matters: business users can self-serve without knowing SQL

4. **AI/BI Dashboards** (3 min)
   - What they are: auto-generated dashboards that understand your data
   - Natural language to visualization: "show me monthly revenue by state as a line chart"
   - Connected to the same Unity Catalog tables
   - Complement to Genie: dashboards for recurring views, Genie for ad-hoc questions

**Key message:** _Skills and MCP extend what agents can do. Genie and AI/BI put data in the hands of business users._

---

### 12:25–12:30 | Lab 2 Briefing (5 min)

**Slides:** 32–33 (Section: Lab 2, Lab 2 Briefing)

**Content:**
- Walk through the four phases and timing
- Explain the parallel task assignments (see below)
- Emphasise: Person C starts Genie space in UI from Phase 1 — it runs in parallel
- Remind teams about checkpoints
- _"Your goal: app running, Genie answering questions, dashboard showing metrics by 13:25."_

---

### 12:30–13:25 | Lab 2: Build Your App & Dashboard (55 min)

> **See track-specific instructions:** [LAB-2-DE.md](LAB-2-DE.md) | [LAB-2-DS.md](LAB-2-DS.md) | [LAB-2-ANALYST.md](LAB-2-ANALYST.md)

**Summary:** Teams continue in their chosen track. DE teams add data quality, new sources, and scheduling. DS teams train models, deploy serving endpoints, and build a prediction app. Analyst teams build a FastAPI web app with embedded dashboards. Skills and MCP are used throughout.

**Time-boxed phases with parallel task assignments:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Phase 1: PRD + Tests + Genie | 10 min | Write PRD, API tests, start Genie space | — |
| Phase 2: Build | 25 min | Backend, frontend, AI/BI dashboard | Checkpoint 2A: basic app skeleton |
| Phase 3: Wire + Polish | 15 min | Deploy app, test Genie, polish dashboard | Checkpoint 2B: Genie space instructions |
| Phase 4: Demo Prep | 5 min | Prepare 3-minute team demo | Checkpoint 2D: complete solution |

**Parallel Task Assignments — Lab 2:**

| Phase | Person A | Person B | Person C |
|-------|----------|----------|----------|
| **Phase 1** (PRD + Tests, 10 min) | Write PRD for the app (use starter-kit template) | Write API tests (use starter-kit test stubs) | Start Genie space in UI (select gold tables, add descriptions) |
| **Phase 2** (Build, 25 min) | Build FastAPI backend (endpoints, data connection) | Build frontend (HTML/Tailwind/htmx) | Create AI/BI dashboard in UI (charts, filters, layout) |
| **Phase 3** (Wire + Polish, 15 min) | Deploy app to Databricks Apps | Test Genie space + refine instructions/descriptions | Polish dashboard + get embed URL |
| **Phase 4** (Demo Prep, 5 min) | All: prepare 3-minute demo | All: pick best Genie question | All: rehearse narrative |

> **Note for teams of 2:** Person A handles backend + deployment. Person B handles
> frontend + Genie + dashboard (Genie and dashboard are UI tasks that run in parallel).

**Facilitator actions during lab:**
- At 10 min: "PRD and tests should be done — agent should be implementing"
- At 25 min: "Backend should be working — start on Genie space even if frontend isn't perfect"
- At 40 min: "Genie space should be created — start AI/BI dashboard if not already"
- At 50 min: "Start preparing your 3-minute demo!"

---

### 13:25–13:35 | Break (10 min)

---

### 13:35–13:55 | Team Demos, Voting & Retro (20 min)

**Slide:** 34 (Team Demos & Voting)

**Team Demos (12 min):** Each team gets 3 minutes to demo:
- Their pipeline (what data, what transformations)
- Their app (show it running, ask the AI a question)
- Their Genie space (ask a natural language question)
- One thing that surprised them

**Voting (3 min):** Each person votes for the best team (can't vote for yourself). Criteria:

| Criteria | Weight |
|----------|--------|
| End-to-end completeness (pipeline → app → Genie) | 40% |
| Insight quality (interesting findings, good visualizations) | 30% |
| Creativity (unique features, clever AI use) | 20% |
| Best use of agent (TDD, CLAUDE.md, steering) | 10% |

**Retro (5 min):** Quick group discussion:
- What was the most valuable technique you learned today?
- What will you take back to your daily work on Monday?
- Where do you see the biggest opportunity for your team?

---

### 13:55–14:00 | Key Takeaways + Next Steps + Closing (5 min)

**Slides:** 35–37 (Key Takeaways, Next Steps, Closing)

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

## Track System

After the shared theory sessions, teams choose one of three tracks:

| Track | Lab 1 Focus | Lab 2 Focus | Key Tools |
|-------|------------|------------|-----------|
| **Data Engineering** | Lakeflow pipeline (Bronze→Silver→Gold) | Data quality, new sources, scheduling | Lakeflow, DABs, @dp.expect |
| **Data Science** | Feature engineering, MLflow experiments | Model training, serving, prediction app | MLflow, Model Serving, scikit-learn |
| **Analyst** | Genie spaces, AI/BI dashboards | FastAPI web app with embedded dashboards | Genie, AI/BI, FastAPI + htmx |

### Track Selection
- Teams self-select based on interest during the Lab 1 briefing
- Facilitator should recommend based on team composition (ML experience → DS, analyst background → Analyst)
- All tracks share the same gold tables via Checkpoint 0

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

1. **At project setup (Exercise: Write Your CLAUDE.md):** Copy the CLAUDE.md template and customise it
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
| **1B: Silver + Gold Tables** | Silver transformations not working at the 40-min mark | Pre-loaded `retail_turnover`, `food_price_index`, `retail_summary`, `food_inflation_yoy` |
| **1C: Complete Pipeline** | Want to focus on Lab 2; need the full pipeline code | Complete pipeline source code + databricks.yml + all tables |

### Lab 2 Checkpoints

| Checkpoint | When to Use | What You Get |
|-----------|-------------|-------------|
| **2A: App Skeleton** | Backend not working at the 25-min mark | Working FastAPI app with health endpoint, data connection, basic structure |
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
| **Agents / Vibe Coding** | Session 1 (9:15, demo + theory) | Both labs | Deep |
| **CLAUDE.md / PRDs** | Session 1 (9:30, theory + exercise) | Lab 1 (first thing teams write) | Deep |
| **TDD with Agents** | Session 1 (10:10, theory + demo) | Lab 1 (tests before pipeline) | Deep |
| **Tokens / Context Windows** | Session 1 (10:25, theory) | Both labs (context management) | Light |
| **Skills** | Session 2 (12:10, overview) | Both labs (using skills throughout) | Medium |
| **Lakeflow Pipelines** | Lab 1 Briefing (10:30) | Lab 1 (build full pipeline) | Deep |
| **MCP** | Session 2 (12:10, demo + tiers) | Lab 2 (Databricks docs MCP) | Medium |
| **Genie Spaces** | Session 2 (12:10, demo) | Lab 2 (create Genie space) | Medium |
| **AI/BI Dashboards** | Session 2 (12:10, demo) | Lab 2 (create dashboard) | Medium |

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

- If Session 1 runs long: compress Session 2 to 10 min (cut Databricks internal demo)
- If Lab 1 runs long: borrow 5 min from lunch, reduce Lab 2 to 50 min
- If teams are advanced: extend Lab 2, add bonus challenges (MCP server, custom skills)
- If environment issues: have David's laptop as backup with pre-recorded demos
- If teams finish early: bonus challenges in each lab guide, or help other teams

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
