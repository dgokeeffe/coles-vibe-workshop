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
4. Use **skills**, **subagents**, and **plugins** to extend agent capabilities
5. Connect agents to external tools via **MCP** (Model Context Protocol)
6. Create **Genie spaces** and **AI/BI dashboards** for natural language analytics
7. Ship a working end-to-end application on Databricks

---

## Workshop Rhythm

Every block follows the same pattern for maximum engagement:

```
📖 Theory (15–20 min)  →  🔨 Exercise (10–70 min)  →  💬 Discussion (5–15 min)
```

Short, punchy teaching → hands-on practice in teams → share learnings with the group.

---

## Agenda Overview

| Time | Duration | Block | Type |
|------|----------|-------|------|
| **0:00** | 15 min | Ice Breaker: Grocery Data Predictions | Engage |
| **0:15** | 20 min | Session 1: Vibe Coding Fundamentals | Theory |
| **0:35** | 15 min | Exercise: Write Your Team's CLAUDE.md | Exercise |
| **0:50** | 5 min | Share: CLAUDE.md Highlights | Discussion |
| **0:55** | 10 min | Break | |
| **1:05** | 15 min | Session 2: TDD, Skills & Lakeflow Pipelines | Theory |
| **1:20** | 65 min | Lab 1: Build Your Data Pipeline | Exercise |
| **2:25** | 10 min | Show & Tell: Pipeline Results + Prediction Reveal | Discussion |
| **2:35** | 30 min | Lunch | |
| **3:05** | 20 min | Session 3: MCP, Subagents, Plugins, Genie & AI/BI | Theory |
| **3:25** | 65 min | Lab 2: Build Your App, Genie Space & Dashboard | Exercise |
| **4:30** | 10 min | Break | |
| **4:40** | 20 min | Team Demos, Voting & Retro | Discussion |
| **5:00** | — | End | |

**Time breakdown:** 55 min theory · 145 min hands-on · 35 min discussion · 15 min ice breaker · 50 min breaks/lunch

---

## Detailed Agenda

### 0:00–0:15 | Ice Breaker: Grocery Data Predictions (15 min)

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

### 0:15–0:35 | Session 1: Vibe Coding Fundamentals (20 min)

**Concepts covered:** Agents, vibe coding basics, CLAUDE.md, PRDs

**Content:**

1. **What is vibe coding?** (3 min)
   - The shift from writing code to directing AI agents (Andrej Karpathy, Feb 2025)
   - "You see stuff, you say stuff, you run stuff, and you vibe"
   - Not replacing developers — amplifying them 10x
   - Tool-agnostic: Claude Code, Cursor, Windsurf, GitHub Copilot, OpenCode — the patterns transfer

2. **Live demo: Zero to pipeline in 5 minutes** (7 min)
   - David live-builds a simple data transformation using Claude Code
   - Show the core loop: **Describe → Generate → Test → Refine**
   - Highlight how the agent reads files, writes code, runs tests, fixes errors

3. **CLAUDE.md: Your team's DNA** (5 min)
   - What it is: persistent instructions the agent follows on every prompt
   - Three levels: user (`~/.claude/CLAUDE.md`), project (repo root), folder-level
   - What to put in it: tech stack, coding standards, architecture decisions, data contracts
   - Live example: David's personal CLAUDE.md and how adding one line changes behavior

4. **PRDs for agents** (3 min)
   - Why specs matter MORE with AI (garbage in, garbage out at 100x speed)
   - A good PRD = clear acceptance criteria + constraints + example inputs/outputs
   - The agent treats the PRD as its "definition of done"

5. **Quick tour of the Coding Agents App** (2 min)
   - Open the browser-based terminal
   - Show where Claude Code, OpenCode, and Codex are available
   - Verify everyone can access their instance

**Key message:** _The best engineers will be those who can effectively direct AI agents. CLAUDE.md and PRDs are your leverage multipliers._

---

### 0:35–0:50 | Exercise: Write Your Team's CLAUDE.md (15 min)

**Task:** Each team opens their Coding Agents App and creates a CLAUDE.md for the challenge.

**Prompt to give teams:**

> Open your Coding Agents terminal and tell the agent:
>
> _"Create a project called grocery-intelligence with a CLAUDE.md that includes:
> our tech stack (PySpark, Lakeflow Declarative Pipelines, FastAPI, Tailwind CSS + htmx),
> our data standards (Unity Catalog namespace workshop_vibe_coding.\<team_schema\>,
> medallion architecture, date formats), our testing standards (pytest, TDD, small
> test DataFrames), and our deployment target (Databricks Asset Bundles)."_
>
> Review what the agent generates. Add anything specific to your team's chosen angle.

**While teams work:** David circulates, helps teams refine their CLAUDE.md, answers questions.

---

### 0:50–0:55 | Discussion: CLAUDE.md Highlights (5 min)

**Quick round-robin:** Each team shares one thing from their CLAUDE.md they think will help the agent most. David highlights patterns and anti-patterns.

**Discussion prompts:**
- What standards did you include? Why?
- Did the agent generate anything you didn't expect?
- What's the most important rule for YOUR project?

---

### 0:55–1:05 | Break (10 min)

---

### 1:05–1:20 | Session 2: TDD, Skills & Lakeflow Pipelines (15 min)

**Concepts covered:** TDD with agents, skills, Lakeflow Declarative Pipelines

**Content:**

1. **TDD as the secret weapon** (5 min)
   - Tests are unambiguous specs that agents can verify against
   - The TDD + Agent workflow:
     1. Human writes test (the spec)
     2. Agent implements code to pass tests
     3. Agent runs tests, reads failures, fixes code
     4. Human reviews, adds edge cases
   - Live demo: 3 failing tests → agent implements → green in 2 minutes
   - _"If you take one thing from today: write the tests first. Always."_

2. **Skills: reusable agent capabilities** (3 min)
   - Built-in: `/commit`, `/review`, `/test`
   - Databricks AI Dev Kit skills (pre-installed): pipeline scaffolding, DABs templates
   - Custom skills: encode your team's patterns as repeatable commands
   - Demo: show a skill in action

3. **Lakeflow Declarative Pipelines** (5 min)
   - What they are: Python-native pipeline definitions using `@dp.table` and `@dp.materialized_view`
   - Data quality expectations with `@dp.expect()`
   - Automatic dependency resolution — just declare your tables, Lakeflow figures out the DAG
   - Deploy with Databricks Asset Bundles
   - Quick code walkthrough: bronze ingestion → silver transformation → gold materialized view

4. **Checkpoint system explained** (2 min)
   - Pre-loaded data at every stage in Unity Catalog
   - If you fall behind, grab the checkpoint and keep going — nobody gets stuck
   - Checkpoints are a safety net, not a shortcut!

**Key message:** _TDD + agents = deterministic outcomes. Tests ARE your spec. Lakeflow makes pipelines declarative and deployable._

---

### 1:20–2:25 | Lab 1: Build Your Data Pipeline (65 min)

> **See [LAB-1-DATA-PIPELINE.md](LAB-1-DATA-PIPELINE.md) for full instructions.**

**Summary:** Teams build a Lakeflow Declarative Pipeline that ingests public Australian data through Bronze → Silver → Gold, with TDD and DABs deployment.

**Time-boxed phases:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Write tests first | 15 min | Define pipeline tests before any implementation | — |
| Build Bronze layer | 15 min | Ingest ABS APIs into raw tables | Checkpoint 1A: pre-loaded bronze tables |
| Build Silver + Gold | 20 min | Transform, enrich, create materialized views | Checkpoint 1B: pre-loaded silver+gold tables |
| Deploy with DABs | 10 min | Create databricks.yml, deploy pipeline | Checkpoint 1C: complete pipeline code |
| Buffer | 5 min | Catch up, explore data, prepare for show & tell | — |

**Facilitator actions during lab:**
- Circulate every 10 min, check progress
- At 15 min: "You should have tests written — if not, grab Checkpoint 1A and skip to Silver"
- At 30 min: "Bronze should be working — if stuck, grab Checkpoint 1A"
- At 45 min: "Gold tables should exist — if not, grab Checkpoint 1B for Lab 2 readiness"

---

### 2:25–2:35 | Show & Tell: Pipeline Results + Prediction Reveal (10 min)

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

### 2:35–3:05 | Lunch (30 min)

---

### 3:05–3:25 | Session 3: MCP, Subagents, Plugins, Genie & AI/BI (20 min)

**Concepts covered:** MCP, subagents, plugins, Genie spaces, AI/BI dashboards

**Content:**

1. **MCP: "USB for AI"** (5 min)
   - Open protocol for agents to call external tools
   - Three tiers:
     - **Managed:** Built into Databricks (Unity Catalog, DBSQL, Vector Search)
     - **External:** Community-built (Slack, JIRA, GitHub, Confluence, Databricks Docs)
     - **Custom:** You build them (internal APIs, data tools, monitoring)
   - Demo: Use the Databricks Docs MCP to search documentation live
   - _"Without MCP, the agent guesses. With MCP, it knows."_

2. **Subagents: parallel work, isolated context** (4 min)
   - What they are: spawned agents that run in their own context window
   - Why: keeps the main conversation lean, enables parallel work
   - Types: Explore (fast codebase search), Plan (architecture), general-purpose
   - Demo: spawn an Explore agent to search the codebase while continuing to work
   - When to use: research tasks, multi-file reads, verification — anything that's "go find out X"

3. **Subagents vs Agent Teams: choosing the right paradigm** (4 min)
   - Most people reach for multi-agent the moment a task feels complex — almost always wrong
   - The right question: _"What kind of coordination does this task actually need?"_
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
   - For Lab 2: subagents for parallel frontend/backend exploration is the sweet spot

5. **Plugins: packaging for teams** (3 min)
   - Plugins = skills + agents + hooks, packaged for reuse
   - Skills: repeatable commands (e.g., `/deploy-pipeline`, `/run-data-quality`)
   - Agents: specialized sub-agents for specific tasks
   - Hooks: automatic actions on events (e.g., lint on save, test on commit)
   - Building blocks for a team-wide "agent toolkit"

6. **Genie: natural language on your data** (4 min)
   - What it is: AI-powered Q&A interface on Unity Catalog tables
   - How it works: user asks a question → Genie generates SQL → returns results + visualization
   - Demo: create a Genie space on the workshop gold tables, ask a question live
   - Why it matters: business users can self-serve without knowing SQL

7. **AI/BI Dashboards** (4 min)
   - What they are: auto-generated dashboards that understand your data
   - Natural language to visualization: "show me monthly revenue by state as a line chart"
   - Connected to the same Unity Catalog tables
   - Demo: create an AI/BI dashboard from the gold tables
   - Complement to Genie: dashboards for recurring views, Genie for ad-hoc questions

**Key message:** _MCP extends what agents can do. Subagents and plugins scale how your team works. Genie and AI/BI put data in the hands of business users._

---

### 3:25–4:30 | Lab 2: Build Your App, Genie Space & Dashboard (65 min)

> **See [LAB-2-APP-GENIE-DASHBOARD.md](LAB-2-APP-GENIE-DASHBOARD.md) for full instructions.**

**Summary:** Teams build a FastAPI web app on their pipeline data, set up a Genie space, and create an AI/BI dashboard. MCP and subagents are used throughout.

**Time-boxed phases:**

| Phase | Duration | What | Checkpoint Available |
|-------|----------|------|---------------------|
| Write PRD + tests | 10 min | Design the app, write API tests | — |
| Build backend + frontend | 25 min | FastAPI + HTML/Tailwind/htmx | Checkpoint 2A: basic app skeleton |
| Set up Genie space | 10 min | Create Genie space on gold tables | Checkpoint 2B: Genie space instructions |
| Create AI/BI dashboard | 10 min | Build dashboard from gold tables | Checkpoint 2C: dashboard template |
| Deploy + polish | 10 min | Deploy app to Databricks Apps | Checkpoint 2D: complete solution |

**Facilitator actions during lab:**
- At 10 min: "PRD and tests should be done — agent should be implementing"
- At 25 min: "Backend should be working — start on Genie space even if frontend isn't perfect"
- At 40 min: "Genie space should be created — start AI/BI dashboard"
- At 55 min: "Start preparing your 3-minute demo!"

---

### 4:30–4:40 | Break (10 min)

---

### 4:40–5:00 | Team Demos, Voting & Retro (20 min)

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

**Closing:**
- Key takeaways:
  1. _CLAUDE.md and PRDs are your leverage multipliers_
  2. _TDD + agents = deterministic outcomes_
  3. _MCP extends agents from code to systems_
  4. _Genie + AI/BI puts data in everyone's hands_
- Next steps: roll out to wider team, establish team CLAUDE.md, build shared skill libraries
- David available for follow-up support

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
| **Agents / Vibe Coding** | Session 1 (demo + theory) | Both labs | Deep |
| **CLAUDE.md / PRDs** | Session 1 + CLAUDE.md exercise | Lab 1 (first thing teams write) | Deep |
| **TDD with Agents** | Session 2 (demo + theory) | Lab 1 (tests before pipeline) | Deep |
| **Skills** | Session 2 (overview + demo) | Both labs (using skills throughout) | Medium |
| **Lakeflow Pipelines** | Session 2 (code walkthrough) | Lab 1 (build full pipeline) | Deep |
| **Subagents** | Session 3 (demo) | Lab 2 (parallel frontend + backend) | Medium |
| **Plugins** | Session 3 (overview) | Lab 2 (optional extension) | Light |
| **MCP** | Session 3 (demo + tiers) | Lab 2 (Databricks docs MCP) | Medium |
| **Genie Spaces** | Session 3 (demo) | Lab 2 (create Genie space) | Medium |
| **AI/BI Dashboards** | Session 3 (demo) | Lab 2 (create dashboard) | Medium |

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

- If Lab 1 runs long: compress Session 3 to 15 min, reduce Lab 2 to 55 min
- If teams are advanced: extend Lab 2, add bonus challenges (MCP server, custom skills)
- If environment issues: have David's laptop as backup with pre-recorded demos
- If teams finish early: bonus challenges in each lab guide, or help other teams

### Materials to Prepare

- [ ] Prediction cards (printed, 1 per team — grocery data questions for Show & Tell reveal)
- [ ] Scoreboard (whiteboard or shared Google Sheet)
- [ ] Checkpoint data pre-loaded in Unity Catalog (`workshop_vibe_coding.checkpoints.*`)
- [ ] Checkpoint code in shared Git repo
- [ ] Coding Agents App instances deployed and tested
- [ ] Slides for theory sessions (slides.html)
- [ ] Quick-reference cards (printed, 1 per person) (quick-reference.html)
- [ ] Backup: pre-recorded demos on David's laptop

### Team Formation Tips

- Balance skill levels (1 experienced + 1-2 newer engineers per team)
- Mix roles if possible (data engineer + analyst, or DE + DS)
- One person drives the agent, others steer/review — rotate driver every 20 min

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
