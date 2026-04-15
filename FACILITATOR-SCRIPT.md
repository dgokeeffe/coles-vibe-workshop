# Facilitator Script — The Great Grocery Data Challenge

**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Audience:** Coles Group — Data & AI Engineering Team
**Duration:** 6.5 hours (9:30 AM - 4:00 PM)

---

## Before the Room Opens (9:00 AM)

- Slides loaded on the projector (slides.html, tested with keyboard nav)
- Coding Agents App instances up and verified (one per participant)
- Prediction cards printed (one per team)
- Scoreboard ready (whiteboard or shared doc)
- Starter-kit folder distributed to all teams (CLAUDE.md template, test stubs, prompts, cheatsheet, config)
- Backup demo recordings on laptop (in case of live demo failures)
- Lab guides open on your laptop: LAB-0-GUIDED-HANDS-ON.md, LAB-1-DATA-PIPELINE.md, LAB-2-APP-GENIE-DASHBOARD.md
- Water bottle. You will be talking for six and a half hours.

---

## Slide 1: Title | 9:30 | 2 min

**[CLICK]**

- Welcome, introductions — thanks to Farbod and Swee Hoe
- Six-and-a-half-hour hackathon, teams of 2-3, competing to build Grocery Intelligence Platform
- Using real Australian public data, directing AI agents
- "Skills you can use on Monday — literally Monday"

**Transition:** "Before any more slides — let me show you what this actually looks like in practice."

---

## Slide 2: Opening Demo — My Working Setup | 9:32 | 5 min

**[CLICK to show the setup slide, then SWITCH to live Claude Code terminal]**

- "This is my actual working setup — not a demo environment, this is what I use every day"
- Point at the slide stats: 7 MCP servers, 150+ skills, 12 plugins, hooks for guardrails

**[DEMO — Show each layer in the terminal:]**

- `/status` or show MCP connections — "Seven MCP servers: Slack, JIRA, Confluence, Chrome DevTools, Databricks Docs, Glean, DeepWiki"
- Show the CLAUDE.md briefly — "This is my onboarding doc for the agent — MCP routing rules, subagent patterns, context management"
- Show hooks in settings — "Two real hooks: PostToolUse runs ruff format and ruff check --fix every time the agent edits a Python file — deterministic, not AI. Stop hook runs verify-hint.sh so I never walk away without checking the output."

**[DEMO — Do something impressive (~90 sec). Pick ONE:]**

Option A (Slack + JIRA):
```
Check Slack for the latest message in #coles-workshop, then find the most recent JIRA ticket assigned to me and summarise both.
```

Option B (Databricks Docs + build):
```
Search the Databricks docs for how to create a Genie space via API, then scaffold a Python script that creates one pointing at workshop_vibe_coding.gold tables.
```

Option C (UC MCP query):
```
What tables are in the workshop_vibe_coding catalog? Show me the schema of the retail_trade table and write a quick analysis of the top 5 states by food retail turnover.
```

**[Narrate as it runs:]**
- "No context switching — Slack, JIRA, docs, code, all from one terminal"
- "Every tool call is logged, every action goes through guardrails"

**[PAUSE — let results land]**

- "By end of today, you'll understand every piece of this: CLAUDE.md, skills, MCP, hooks"
- "You won't have 150 skills by 4pm — but you'll have the patterns to build them"

**[BACKUP: If demo fails — stay on the slide, walk through the 4 stat cards verbally, say "trust me, it's impressive when the WiFi cooperates"]**

**Transition:** "Let's warm up with a quiz."

---

## Slide 3: Ice Breaker — Grocery Data Predictions | 9:37 | 8 min

**[CLICK]**

**[ENERGY]** Form teams — 2 min. Mix of experience levels. Team names. Assign Person A/B/C roles.

- 5 questions on screen, 30 seconds each, write on prediction cards
- No phones, no Googling — gut instinct only

**[Read each question aloud, 30 sec each:]**

1. Which state has highest monthly food retail turnover?
2. % increase in Australian food prices since Jan 2020?
3. Average Australian household weekly grocery spend?
4. What month do Australians spend most on retail?
5. Biggest price increase since 2020 — dairy, meat, fruit, or bread & cereals?

**[DO NOT reveal answers yet — save for Show & Tell]**

- Each team: share your boldest prediction
- Write boldest predictions on the scoreboard
- "The twist: Lab 1 builds the pipeline that ingests this exact data — we'll query your Gold tables for the real answers"

**[CHECKPOINT: Should be here by 9:45]**

**Transition:** "Let's look at the agenda."

---

## Slide 4: Agenda | 9:45 | 1 min

**[CLICK]**

- Morning: theory (specs, TDD), then Lab 0 (guided hands-on together), then theory (tools), then Lab 1 (track-specific)
- After lunch: Lab 2 (track-specific), then team demos and voting
- "Breaks are real breaks — ask questions anytime, don't save them"

**Transition:** "Quick look at Databricks today."

---

## Slide 5: Databricks Today | 9:46 | 2 min

**[CLICK]**

- Walk the platform stack bottom-up: open formats, Unity Catalog, data layer, Genie, applications
- Call out MCP servers (glue connecting agents to platform) and AI Gateway (routing to Claude Opus 4.6)
- "Today you'll touch almost every layer — Lakeflow, UC, Genie, AI/BI, Custom Apps, MCP"

**[ASK]** "Has everyone accessed their Coding Agents instance? Any issues?"

- Troubleshoot NOW — do not let anyone reach the exercise with broken access

**Transition:** "Now the paradigm shift that makes this possible."

---

## Slide 6: Section — The Paradigm Shift | 9:48 | 1 min

**[CLICK]**

**[PAUSE — let section title land]**

**[ASK]** "Show of hands — who's used an AI coding tool? ChatGPT? Copilot? Cursor? Claude?"

- Most hands up — note the range of usage
- "Today we take ad-hoc prompting to a repeatable, disciplined workflow"

---

## Slide 7: What is Vibe Coding | 9:49 | 3 min

**[CLICK]**

- Read Karpathy quote: "...fully give in to the vibes, embrace exponentials, forget the code exists"
- Real term: agentic software development
- Traditional: write every line, slow iteration. Agentic: you direct, agent implements, tight feedback loops
- "Amplification, not replacement — you still need to know good code, your data, your architecture"

**[PEPPER]** "A brilliant intern joined your team — writes code at incredible speed but doesn't know your systems. How you onboard them determines how useful they are."

**Transition:** "Let me show you the platform."

---

## Slide 8: Platform Architecture | 9:52 | 2 min

**[CLICK]**

- Walk through architecture left-to-right: browser terminal, Flask app, AI agent, AI Gateway
- 39 pre-built skills from AI Dev Kit, MCP for tool access, MLflow tracing for observability

**Transition:** "Now let me show you where we're going today."

---

## Slide 9: What We're Building — End State | 9:54 | 3 min

**[CLICK]**

- "Before I teach you any techniques — let me show you WHERE we're going"
- Walk through the four quadrants:
  - **Data Pipeline** — Lakeflow ingesting ABS retail and food price data, Bronze to Silver to Gold
  - **Web Application** — FastAPI + Tailwind with dashboards, filters, AI-powered query feature
  - **Genie Space** — Business users type questions in English, get instant answers
  - **AI/BI Dashboard** — Auto-generated visualisations from your gold tables
- Point at the flow at the bottom: Pipeline -> App -> Genie -> Dashboard = Grocery Intelligence Platform
- **"By 4pm, every team will have all four of these running."**
- "Now that you can see the destination, the techniques I'm about to teach you will make a lot more sense"

**Transition:** "Let's look at the challenge details."

---

## Slide 10: Today's Challenge | 9:57 | 5 min

**[CLICK]**

- Real ABS data: retail trade + food price indices
- Stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + Tailwind + htmx, DABs
- Lab 0 = guided setup (all together), Lab 1 = pipeline (track-specific), Lab 2 = app + Genie + dashboard (track-specific)
- Teams pick their angle (or invent their own)
- Briefly show the starter-kit folder and what's inside
- "The CLAUDE.md you write in Lab 0 will guide both labs — make it count"

**Transition:** "The skill that matters most."

---

## Slide 11: Section — Specs & TDD | 10:02 | 30 sec

**[CLICK]**

- "The skill that matters most: your ability to specify what you want"
- "In this section we cover both specs and TDD — two sides of the same coin"

---

## Slide 12: Why Specs Matter | 10:02 | 5 min

**[CLICK]**

- "Garbage in, garbage out — but now at 100x speed"
- Anthropic mental model: "brilliant new employee who lacks context on your norms"
- Two tools: PRD (acceptance criteria, constraints, data contracts, examples) and CLAUDE.md (coding standards, architecture, testing, tool preferences)
- A good spec = clear acceptance criteria + constraints + example inputs/outputs

**Transition:** "Let me show you a CLAUDE.md."

---

## Slide 13: CLAUDE.md in Action | 10:07 | 3 min

**[CLICK]**

- Point at code example: PySpark not pandas, UC namespace, DATE type YYYY-MM-DD, pytest with small DataFrames
- One file, three scope levels — add one line, change all future output
- "Highest-ROI activity you can do with an AI agent"

**[PEPPER]** "I have 'always use uv run' in mine — one line, never have to remind the agent."

---

## Slide 14: CLAUDE.md Scope Levels | 10:10 | 2 min

**[CLICK]**

- User-level: personal prefs (home dir, applies everywhere)
- Repo-level: team standards (committed to git, shared)
- Project-level: module-specific rules (subdirectory, scoped)
- Cascade like CSS — more specific overrides general

**[ASK]** "What would you put at each level? Personal vs team standard?"

- Take 2-3 quick answers — primes them for Lab 0

---

## Slide 15: TDD Workflow | 10:12 | 3 min

**[CLICK]**

- "If you take one thing from today — write the tests first"
- Four steps: human writes test, agent implements, run/iterate, human reviews + edge cases
- Key insight: the test IS the spec — no ambiguity
- Agent reads test, sees "correct", writes code, verifies own work — tight feedback loop

---

## Slide 16: Why TDD is Exponentially More Powerful | 10:15 | 3 min

**[CLICK]**

- Unambiguous specs — "correct" = green tick
- Self-correcting loop — run, read failure, fix, repeat (no human in between)
- Guardrails — prevents agent from confidently producing elegant but wrong code

**[PEPPER]** "I've seen agents write beautiful, well-documented functions that are fundamentally wrong. A test would've caught it in seconds."

---

## Slide 17: Writing Tests That Guide the Agent | 10:18 | 3 min

**[CLICK]**

- Given-When-Then structure: given 10 rows (2 null), when clean, then 8 rows, no negatives
- Concrete values ("10 rows, 2 invalid" not "some rows")
- Descriptive names — test name IS the documentation
- Multiple assertions — schema, row counts, specific values

**[ASK]** "Who currently writes tests as part of their workflow?"

- Show of hands — either way: "Same skill, just applied to directing an agent"

---

## Slide 18: Anthropic Best Practices | 10:21 | 2 min

**[CLICK]**

- #1: Give Claude a way to verify its work — tests, screenshots, expected outputs
- #2: Explore first, plan, then code — use /plan mode
- "Cheap to course-correct in planning, expensive in code"

---

## Slide 19B: The Sycophancy Problem | 10:21 | 3 min

**[CLICK — dark slide, let the stats land]**

- "Before we move on — this is the uncomfortable truth about working with AI agents."
- Stanford published in Science this month: tested 11 production LLMs against 2,000 real advice prompts
- **49% more agreement than humans** — the AI tells you what you want to hear
- **The killer stat:** when the user was 100% wrong — zero human agreement — the AI still agreed 51% of the time

**[CLICK — Karpathy experiment]**

- Karpathy spent 4 hours refining an argument with an LLM. Was genuinely convinced it was solid.
- Then asked the same model to argue the opposite — it demolished his argument completely
- "The model was never reasoning toward truth. It was a rhetorical engine."

**[CLICK — Defenses]**

- "This is NOT a bug. RLHF training selected for agreement. Models that weren't likable got deprecated."
- Walk through the four defenses:
  1. **Karpathy Test** — ask it to argue the opposite before trusting any analysis
  2. **"Wait a minute..."** — two words that measurably improve critical evaluation
  3. **TDD** — structural verification, code passes or it doesn't. Code Rabbit data: 1.7x more issues, 2.7x more security vulns in AI code
  4. **Separate prompts** — one writes tests, another implements
- **[LAND THE POINT]** "This is WHY we teach TDD first. This is WHY we say 'prove it worked, don't ask if it worked.'"
- Chollet's framing: "Are you using AI to extend your thinking, or replace it?"

---

## Slide 20: What Are Tokens | 10:24 | 2 min

**[CLICK]**

- Token = 3/4 of a word, ~4 characters — not exactly words, not exactly characters
- Walk through the examples: sentence (~8), Python file (~2-3K), Harry Potter (~110K)
- **Two limits that matter today:**
  - **200K context window** — how much the agent can "see" at once. Fills up, older stuff gets forgotten.
  - **~1M tokens/min rate limit** — shared across ALL teams through AI Gateway
- **[PEPPER]** "If all 5 teams ask the agent to read every file in the repo at the same time, everyone slows down. Be specific."
- Practical tip: small focused requests = faster responses for everyone

**Transition:** "So how do we manage this finite resource?"

---

## Slide 20: Managing Context Windows | 10:25 | 2 min

**[CLICK]**

- Context window = agent's working memory (~200K tokens, fills fast)
- CLAUDE.md, file reads, tool results, conversation turns all consume tokens
- Auto-compaction = agent forgets earlier details

**[Four strategies:]**

- Keep CLAUDE.md lean (~50 lines, loaded every turn)
- Plan before building (/plan)
- Use team members for parallel work (each gets own context)
- Start new conversations for new tasks

**[PEPPER]** "Think of it like RAM. Manage it, or the OS starts swapping."

---

## Slide 21: Live Demo — TDD in Action | 10:27 | 3 min

**[CLICK]**

**[DEMO — ~3 min. Open Coding Agents terminal, full screen. Shorter than before — they'll do this hands-on in Lab 0.]**

- "Three failing tests, then ask the agent to implement"

**[Type:]**

```
Write three pytest tests for a data cleaning module:
1. test_clean_transactions: given 10 rows with 2 null amounts, result has 8 rows
2. test_join_with_lookup: given a transactions table and a stores lookup, result has store_name column
3. test_aggregate_by_state: given 20 transactions across 3 states, result has 3 rows with correct totals

Write ONLY the tests. Do NOT implement the functions yet.
```

**[Let agent write tests, then type:]**

```
Run the tests. They should fail. Then implement the functions to make them pass.
```

**[Narrate:]**

- "Tests run — all red"
- "Reading expectations... writing implementation... running again..."
- "One green, two red... fixing... running..."
- "All green — self-corrected, converged, ~2 min, no human intervention"

**[BACKUP: Play recording if demo fails.]**

- "That's the workflow — you're about to do this yourselves in Lab 0"

**[CHECKPOINT: Should be here by 10:30]**

**Transition:** "Break time — 15 minutes. When we come back, you'll be hands-on."

---

*--- BREAK: 15 min (10:30 - 10:45) ---*

---

## Slide 22: Section — Lab 0: Guided Hands-On | 10:45 | 30 sec

**[CLICK]**

**[ENERGY]** "Welcome back! Lab 0 — everyone together, hands on keyboards. This is guided — I'll walk you through each step."

---

## Slide 23: Lab 0 Briefing | 10:45 | 2 min

**[CLICK]**

**[TIMER: 45 min — Lab 0 runs 10:45 to 11:30]**

- "This is a guided session — everyone does the same three things before we split into tracks"
- Three milestones:
  1. **Write your CLAUDE.md** (15 min) — copy starter-kit template, customise for your team
  2. **Write your first test** (15 min) — TDD workflow, write a failing test, let the agent implement
  3. **Build bronze ingest** (15 min) — first Lakeflow table from ABS Retail Trade API
- "By 11:30, every team has a CLAUDE.md, a passing test, and data landing in bronze"
- "This is the foundation — Labs 1 and 2 build on top of this"

**Transition:** "Open your terminals. Let's go."

---

## Lab 0, Phase 1: Write Your CLAUDE.md | 10:47 | 15 min

**[TIMER: 15 min]**

**[PROJECT on screen — show the starter-kit CLAUDE.md template]**

- "Step 1: Copy the starter-kit CLAUDE.md into your project"

> "Copy the starter-kit CLAUDE.md into our project. Customise it for our team: schema `workshop_vibe_coding.<team_schema>`, angle `<chosen_angle>`. Add our tech stack (PySpark, Lakeflow Declarative Pipelines, FastAPI, Tailwind CSS + htmx), our data standards (Unity Catalog, medallion architecture, date formats), and our testing standards (pytest, TDD, small test DataFrames)."

**[WALK — Circulate full 15 min. Watch for:]**

- Rules too vague — push for specificity ("Use PySpark, not pandas" not "use good practices")
- Teams not reviewing output — remind them to read and edit
- People writing code instead of CLAUDE.md — redirect
- Missing UC namespace — "Add your catalog and schema"

**[At 12 min]** "Two minutes left — your CLAUDE.md should be saved."

**[At 15 min]** Quick check: "Hands up if your CLAUDE.md is committed. Good."

---

## Lab 0, Phase 2: Write Your First Test | 11:02 | 15 min

**[TIMER: 15 min]**

**[PROJECT on screen — show the TDD workflow slide]**

- "Step 2: Write a failing test, then let the agent make it pass"
- Walk through what to type:

> "Write a pytest test for a bronze ingest function: given a mock API response with 5 rows of ABS retail trade data, when we call ingest_retail_trade(), the result should be a DataFrame with 5 rows and columns: date, state, industry, turnover. Write ONLY the test — do NOT implement the function."

**[Let teams type and run. Then:]**

> "Run the test. It should fail. Now implement the function to make it pass."

**[WALK — Watch for:]**

- Agent implementing before test is written — "Stop! Test first."
- Tests too vague — "Add specific assertions: row count, column names, a known value"
- SparkSession errors — "Check conftest.py creates a local SparkSession"

**[At 12 min]** "Two minutes — you should have at least one green test."

**[At 15 min]** "Show of hands — green test? Great. That's the TDD loop. You'll use it all day."

---

## Lab 0, Phase 3: Build Bronze Ingest | 11:17 | 13 min

**[TIMER: 13 min]**

**[PROJECT on screen — show the pipeline architecture slide]**

- "Step 3: Build your first real Lakeflow table — bronze ingest from ABS Retail Trade API"
- "Use TDD — write a test for the bronze table, then let the agent build the pipeline"

> "Create a Lakeflow Declarative Pipeline that ingests ABS Retail Trade data from the API into a bronze table. Use @dlt.table decorator. The bronze table should store raw JSON responses. Write a test first, then implement."

**[WALK — Watch for:]**

- Agent using pandas — "Check your CLAUDE.md — PySpark only"
- ABS API timeout — "Use the sample data file from the starter-kit as fallback"
- Overengineering — "Bronze is raw data. Don't clean it yet — that's silver"

**[At 10 min]** "Three minutes — bronze table should exist in UC. Check the catalog explorer."

**[At 13 min]** "Time! If your bronze table is loaded, you're ready for Lab 1. If not, grab Checkpoint 0A."

**[CHECKPOINT: Should be here by 11:30]**

**Transition:** "Great work — everyone has a foundation. Now let's talk about the tools you'll need for the rest of the day."

---

## Slide 24: Section — Tools for Labs 1 & 2 | 11:30 | 1 min

**[CLICK]**

**[ASK]** "Quick show — what worked well in Lab 0? What surprised you about TDD with the agent?"

- Take 2-3 answers
- "This next section is a focused tools briefing: Skills, MCP, Genie, AI/BI dashboards — everything you need for Labs 1 and 2"

---

## Slide 25: Practical Tips | 11:31 | 3 min

**[CLICK]**

- Start with the **default workflow callout** at top: "Start every non-trivial task with /plan. Even better — ask Claude to interview you about requirements before building."
- **Overengineering:** Claude loves extra files/abstractions — add "Keep solutions minimal. Do not add features beyond what is requested" to CLAUDE.md
- **Hallucinations:** Never trust claims about unread code — add "Never speculate about code you have not opened"
- **Course-correct early:** Check in every 2-3 tool calls — "stop, let's rethink this approach"
- **Challenge Claude:** After it implements, demand proof — "show me the git diff", "prove to me this works", "grill me on these changes". Then try: "knowing everything you know now, scrap this and implement the elegant solution" — second pass often produces cleaner code
- **Commit as checkpoints:** Every 15-20 minutes, use `/commit`. Commits are your safety net — if the agent goes off-rails, Esc-Esc to cancel, then rewind with git. [ASK] "Who has lost work by not committing? Don't let it happen today."
- **Use the starter-kit prompts** — they're copy-paste ready, no interpretation needed

---

## Slide 26: Skills & MCP — Practical Tools | 11:33 | 5 min

**[CLICK]**

- Two-column layout — walk through each side:

**Skills (left column):**
- Slash commands that encode domain knowledge
- `/commit` — smart commit messages. `/test` — run and fix tests. `/review` — code review.
- Databricks skills: `/deploy-dab` — validate + deploy bundle
- "Type `/` in Claude Code to see what's available"
- You can chain skills together and build custom ones for your team

**MCP (right column):**
- "USB-C for AI agents" — one protocol, every tool connects
- Already in your terminal: Databricks Docs MCP server
- "Ask Claude to search the docs for anything you need during the lab"
- **"Without MCP, the agent guesses. With MCP, it knows."**

**Transition:** "Let me show you MCP on Databricks specifically."

---

## Slide 27: MCP on Databricks | 11:38 | 3 min

**[CLICK]**

- **Built-in/Managed:** UC functions, tables, volumes, Vector Search, Genie — zero config
- **Proxy/External:** third-party services (GitHub, Slack, Glean, Jira) routed through Databricks — UC Connections manage auth
- **Custom:** build your own, host on Databricks Apps — wrap internal APIs
- All secured through Unity Catalog
- "For Coles: wrap internal APIs, data tools, monitoring behind MCP servers — every agent gets access"

---

## Slide 28: Demo — Databricks Internal Claude Setup | 11:41 | 4 min

**[CLICK]**

**[DEMO — ~4 min]**

- Walk through Databricks internal setup on screen:
  - CLAUDE.md with company-wide standards — approved patterns, forbidden actions
  - Hooks: PostToolUse auto-formats Python with ruff on every edit, Stop hook runs verify-hint.sh — deterministic guardrails, not AI
  - Skills + MCP: custom slash commands, UC/Genie/internal service connections

**[Switch to live terminal, type:]**

```
Search the Databricks docs for how to create a Genie space programmatically.
```

- Point out: discovers tool, calls it, gets structured results
- "No copy-pasting from a browser — agent asked the docs directly"

**[BACKUP: If demo fails, walk through the settings.json on the slide.]**

- "This is reproducible — set up the same at Coles: CLAUDE.md, hooks, skills"

---

## Slide 29: Genie + AI/BI Dashboards | 11:45 | 2 min

**[CLICK]**

- **Genie:** natural language to SQL on UC tables — create space, point at gold tables, business users ask in plain English
- **AI/BI Dashboards:** auto-generated visualisations — describe what you want, get interactive dashboard
- Both connect to the gold tables from Lab 1

**[PEPPER]** "Dashboards for recurring views execs check weekly. Genie for ad-hoc questions in a meeting."

---

## Slide 30: Track Briefing — Choose Your Track | 11:50 | 10 min

**[CLICK]**

**[ENERGY]** "Now you choose your path for the rest of the day."

- Three tracks:
  - **Data Engineering** — Lakeflow pipelines, more data sources, advanced Silver/Gold transforms
  - **Data Science** — MLflow experiments, feature engineering, forecasting models
  - **Analyst** — Genie spaces, AI/BI dashboards, natural language analytics
- "All tracks build on the bronze table you just created in Lab 0"
- "Pick the track that matches your role or the one you most want to learn"
- Allow teams to split across tracks or stay together

**[Give teams 5 min to discuss and decide. Walk around to advise.]**

- Teams that can't decide — "What do you do day-to-day? Pick the adjacent skill."
- Mixed teams — "Split if you want breadth, stay together if you want depth."

**[At 8 min]** "Two minutes — confirm your track. Grab the right lab guide."

**[At 10 min]** "Locked in. Let's go."

**Transition:** "Lab 1 — 60 minutes, track-specific."

---

## Slide 31: Section — Lab 1 | 12:00 | 30 sec

**[CLICK]**

**[ENERGY]** "Lab 1! Track-specific — you know your path. Make sure you have the right lab guide open."

---

## Slide 32: Lab 1 Briefing | 12:00 | 3 min

**[CLICK]**

**[TIMER: 60 min — Lab 1 runs 12:00 to 13:00]**

- Mission: build on your Lab 0 foundation, go deep in your track
- "Your goal: working deliverables ready to show at Show & Tell at 13:00"
- Checkpoints available at every phase — no shame, goal is every team has results for Lab 2

**[Read the parallel task assignments:]**

> **Person A (Terminal):** Primary builder — follow your track's lab guide phases 1-3
>
> **Person B (Terminal):** Secondary builder — follow your track's lab guide, split tasks with Person A
>
> **Person C (Databricks UI):** Review and verify — check UC tables, monitor tests, validate outputs, prepare Show & Tell notes
>
> **Teams of 2:** Driver follows the lab guide. Navigator verifies in Databricks UI and prepares Show & Tell.

**[WALK — Circulate every 15 min:]**

- **12:15 (15 min):** "Should have first deliverable working. If not, grab a checkpoint."
- **12:30 (30 min):** "Halfway. How's the track going? Any blockers?"
- **12:45 (45 min):** "Fifteen minutes left. Start wrapping up current phase."
- **12:55 (55 min):** "Five minutes. Stop building — prepare your Show & Tell."

**[Common issues:]**

- Agent using pandas — "Add 'Always use PySpark, never pandas' to CLAUDE.md"
- ABS API timeout — "Grab a checkpoint"
- Agent rewriting working code — "Say: don't change passing functions"
- SparkSession errors — "Check conftest.py creates a local SparkSession"

---

## Slide 33: Show & Tell + Prediction Reveal | 13:00 | 15 min

**[CLICK]**

**[ENERGY]** "Time's up! Let's see what you've built."

- 3-4 teams volunteer (2 min each) — try to get one from each track
- Keep it tight, celebrate what worked
- Save time for prediction reveal

**[After volunteers present — reveal prediction answers:]**

1. Highest food retail turnover? **NSW** — ~$3.5B/month
2. Food price increase since Jan 2020? **~25-30%** (big spike in 22-23)
3. Average weekly grocery spend? **~$200-220** (up from ~$160 pre-pandemic)
4. Biggest retail month? **December** (Christmas)
5. Biggest food price increase category? **Dairy & eggs** — 30%+ since 2020

**[Score on the board. Announce leading team.]**

**[ASK]** "Where did TDD help the agent stay on track? Where did it go off the rails?"

- Take 2-3 answers, reinforce TDD concepts

**Transition:** "Great work. Lunch — back at 14:00."

---

*--- LUNCH: 45 min (13:15 - 14:00) ---*

---

## Slide 34: Section — Lab 2 | 14:00 | 30 sec

**[CLICK]**

**[ENERGY — Post-lunch, start interactive]**

**[ASK]** "What worked well in Lab 1? What surprised you?"

- Take 3-4 answers
- Ground this session in their experiences ("agent went off track — we covered tools that help", "context got heavy — we talked about that")
- "Lab 2 — same tracks, 60 more minutes. Use everything from today — CLAUDE.md, TDD, skills, MCP. This is where it all comes together."

---

## Slide 35: Lab 2 Briefing | 14:00 | 3 min

**[CLICK]**

**[TIMER: 60 min — Lab 2 runs 14:00 to 15:00]**

- "Get as far as you can — not every team will finish everything, and that's fine"
- Continue in your track — pick up where Lab 1 left off
- "Your goal: polished, demo-ready deliverables by 15:00"

**Phases:**
- Phase 1: Review Lab 1 output, plan Lab 2 scope (5 min)
- Phase 2: Build core deliverables (30 min)
- Phase 3: Polish, integrate, connect pieces (15 min)
- Phase 4: Demo prep (10 min) — stop building, prepare pitch

**[Read the parallel task assignments:]**

> **Person A (Terminal):** Primary builder — follow your track's Lab 2 guide
>
> **Person B (Terminal):** Secondary builder — split tasks, build in parallel
>
> **Person C (Databricks UI):** Create Genie space (select gold tables, add descriptions), create AI/BI dashboard (charts, filters, layout), get embed URL for the app
>
> **Teams of 2:** Person A handles primary build. Person B handles Genie + dashboard + demo prep.

**Embed tip:** Publish dashboard -> Share -> Copy embed code -> `<iframe>` in your app

**Bonus:** Build an MCP server wrapping your retail analytics — let any agent query your data

**[WALK — Circulate:]**

- **14:15 (15 min):** "Core build underway? Any blockers?"
- **14:30 (30 min):** "Halfway. Start thinking about Genie/dashboard if you haven't already."
- **14:45 (45 min):** "Fifteen minutes of building left. Wrap up current work."
- **14:50 (50 min):** "Stop building! Spend last 10 min on your demo pitch."

**[Common issues:]**

- htmx not loading — check script tag in HTML head
- CORS errors — add CORSMiddleware to FastAPI
- Can't create Genie space — check permissions, help navigate UI
- Running out of time — "Working deliverable > perfect deliverable. Grab checkpoints."

---

## Slide 36: Team Demos & Voting | 15:00 | 30 min

**[CLICK]**

**[ENERGY]** "Demo time! Three minutes per team."

- Show pipeline, app, Genie space, one surprise
- Set visible timer
- Quick applause after each, note creative/clever moments

**[After all demos — Voting:]**

- Can't vote for own team
- Criteria: completeness (40%), insight quality (30%), creativity (20%), best agent use (10%)
- Show of hands or paper vote — tally, announce winner

**[Five-minute retro:]**

**[ASK]** "Most valuable technique you learned today?"

- Take 3-4 answers

**[ASK]** "What will you take back to work on Monday — literally Monday?"

- Take 3-4 answers

**[ASK]** "Biggest opportunity for your team?"

- Take 2-3 answers

---

## Slide 37: Key Takeaways | 15:30 | 5 min

**[CLICK]**

- **Specs are your leverage** — PRDs + CLAUDE.md multiply output tenfold
- **TDD + agents = deterministic outcomes** — write test, agent converges
- **Skills + MCP extend reach** — connect to external tools, Genie puts data in everyone's hands
- **Start small, iterate** — one function, one test, one deploy, then scale

**[ASK]** "Which resonated most with you today?"

---

## Slide 38: Next Steps | 15:35 | 5 min

**[CLICK]**

- **This week:** share learnings, set up team CLAUDE.md, try on one real task — start small
- **Coming soon:** broader team workshop, shared skill libraries, Genie on production data
- **Champions:** Farbod and Swee Hoe (internal), david.okeeffe@databricks.com (Databricks)

---

## Slide 39: Closing | 15:40 | 5 min

**[CLICK]**

**[PAUSE — let the slide land]**

- "The best teams will be those who can effectively direct AI agents — together."

**[Make eye contact]**

- Thank the room — time, energy, willingness to experiment
- Congrats to Team [winner]
- "You built real working platforms in six and a half hours"
- Email on screen, here for follow-up
- Questions?

*[If none:]* "Go build something great this week."

---

*--- BUFFER / Q&A: 15 min (15:45 - 16:00) ---*

- Open floor for questions, 1:1 follow-ups, debugging help
- If no questions, let teams continue polishing or exploring
- Pack up by 16:00

**[END — 16:00]**

---

## Appendix Slides (if time permits or questions arise)

### Appendix A: Subagents, Skills, Hooks & Plugins

- **Subagents:** parallel workers, isolated context — build frontend while you do backend
- **Skills:** slash commands encoding domain knowledge (/commit, /review, custom /deploy-pipeline)
- **Hooks:** event-driven guardrails — PostToolUse auto-formats Python with ruff on every save, Stop hook runs verify-hint.sh — deterministic, not AI
- **Plugins:** package skills + agents + hooks for your team — distributable, versioned

### Appendix B: Skills in Action — TDD Skill Chain

- /prd-writer: interviews you, generates PRD with machine-verifiable criteria
- /test-generator: reads PRD, generates failing tests (one per criterion)
- /implementer: writes code to make all tests pass
- Key: skills generate tests from success criteria, not from code — define "done" before implementation

### Appendix C: Subagents vs Agent Teams

- **Subagents = fire-and-forget** — isolated context, one job, result returns to parent. Can't talk to each other — that's a feature. Key benefit: **compression** — vast exploration distilled to clean signal.
- **Agent Teams = ongoing coordination** — long-running, peer-to-peer messaging, shared task list with `blockedBy`. Key benefit: **negotiation** — discovery in one thread changes another.
- **Design principle:** Start with one agent. Push it until it breaks. That tells you what to add.
- **Warning:** Parallel agents writing code make incompatible assumptions — subagents should explore, not write code simultaneously.

### Appendix D: MCP Architecture Detail

- Left: Databricks-served agents connect to custom/managed/third-party MCP servers
- Right: external agents (like your Claude Code today) connect to same servers
- Bottom: AI Gateway routes to model serving
- "Coles sits on the right today — external agent connecting via MCP, same security and governance"

### Appendix E: AI Dev Kit

- **Skills:** 25+ skill packs (pipelines, dashboards, UC, Genie, MLflow) — knowledge layer
- **MCP Server:** 50+ tools (SQL, clusters, jobs, apps) — action layer
- **Tools Core:** Python library underneath — extend with your own
- **Builder App:** web chat UI — what you've been using today
- **For Coles:** fork this repo, add custom skills — /run-data-quality, /deploy-pipeline, /check-lineage

---

## Emergency Playbook

| Situation | Response |
|-----------|----------|
| **WiFi goes down** | Switch to phone hotspot for demos. Teams can work offline on tests/code, reconnect later. |
| **Coding Agents App crashes** | Restart the app. If persistent, pair affected person with another team member. |
| **Live demo fails** | "Live demos — always an adventure." Play the backup recording from your laptop. |
| **A team falls way behind** | Walk them to the checkpoint. "Grab a checkpoint, get your tables loaded, and focus on the next lab." |
| **One person dominates the team** | "Great energy — let's rotate the driver so everyone gets a turn." |
| **Post-lunch energy crash** | Start with the interactive question. Stand up, walk around. Move quickly to Lab 2 to get hands back on keyboards. |
| **Running over time** | Compress Tools briefing to 10 min (cut Databricks internal demo). Cut Lab 2 to 50 min. Keep demos to 2 min each. |
| **Running under time** | Extend Lab 2. Add the bonus MCP server challenge. Let teams polish their demos. |
