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

## Slide 1: Title | 9:30 | 30 sec

**[CLICK]**

- Welcome — thanks to Farbod and Swee Hoe
- Six-and-a-half-hour hackathon, teams of 2-3, building a Grocery Intelligence Platform
- "Skills you can use on Monday — literally Monday"

**Transition:** "Before any of that — let's name what's actually happening in our industry right now."

---

## Slide 2: The AI Coding Moment | 9:30 | 3-4 min

**[CLICK]**

**[FRAMING]** "Before we do anything technical — I want to set the frame. This room is mixed. Some of you have been using Claude Code for months. Some of you opened it for the first time this week. This morning isn't about whether to use AI coding tools — that ship has sailed. It's about what the work actually looks like now."

**[Walk the five source cards, ~30 sec each. Emphasise these are all from the last 3 months and they all converge.]**

- **Pragmatic Engineer (Apr 13, 2026 — survey data)** — "Gergely surveyed practicing engineers. The finding: impact is uneven. Stronger engineers get more leverage from agents. Others produce output that still needs human cleanup. Team-level productivity is what matters — not feeling faster individually."

**[ASK the room]** — "Anyone here felt the 'faster individually but the team delivers the same' thing? When the day feels productive but the backlog hasn't moved?"

- Expect nods from the experienced segment. This is the hook.

- **Thoughtworks Macro Trends (Apr 14, 2026)** — "Thoughtworks places this inside a bigger shift: the industry is moving toward AI-native operating models. Their argument: orchestration and governance matter as much as model quality. Agents need structure — specs, reusable components, workflow controls — to be safe and useful."
- **Stack Overflow Blog (Mar 25, 2026 — team practices)** — "You now review code you didn't write. More cognitive load shifts to design, architecture, and review. Teams with strong conventions, linters, documented patterns benefit more. Teams with weak process hygiene get left behind."
- **CIO Magazine (Feb 19, 2026 — workflow)** — "CIO's framing: engineers are shifting from creators to curators. More time on architecture, guardrails, and validation. Agents act as first-pass executors across the SDLC."
- **Anthropic 2026 Agentic Coding Trends Report (Jan 20, 2026)** — "From the model-maker side: agentic coding has moved from isolated assistance to long-running, multi-step execution. Formerly uneconomic software projects become viable. Human role shifts toward orchestration, evaluation, strategy."

**[LAND THE SYNTHESIS — read it slowly, this is the thesis of the day:]**

- "They all agree: the new bottleneck is **verification and coordination**, not code generation. Architecture, tests, conventions, governance become central — not peripheral."
- "**Today you learn the practices that put you on the leverage side.**"

**[OPTIONAL — if the room looks skeptical, drop a data point:]**

- "METR published a controlled study in July 2025. Experienced open-source devs with AI tools: they FELT 20% faster, they were objectively 19% slower. Feeling fast isn't the same as being fast. That's the Pragmatic Engineer point, measured."

**Transition:** "Let me show you what it looks like when the technique lines up — from my own work at Coles."

---

## Slide 3: Your Weekly Specials — Built with Vibe Coding | 9:33 | 4 min

**[CLICK to show the YWS slide]**

- "This is a system I built for Coles. Your Weekly Specials. 4.5 million Flybuys members get 13 personalized grocery offers every week."

**[Walk through the four stat cards — keep it tight:]**

- **4.5M members** — "Every Flybuys member gets 13 personalized offers every week"
- **857 commits** — "37,000 lines of Python. 4 product lines. 340+ automated tests."
- **7 weeks** — "Spare time. Nights and weekends. One engineer, AI-assisted. That's the punchline."
- **R→Python** — "Full migration from R on Azure Batch VMs to native Databricks. 452 million training rows on Ray."

**[SHOW the YWS app if possible — open in browser, show the recommendation viewer]**

- "React frontend, FastAPI backend, querying Delta tables — built with the same patterns you'll learn today"

**[KEY MESSAGE — keep brief, we're tight on time:]**

- "I'm not a data scientist. I knew almost nothing about YWS before I started. The agent helped me learn the domain. I steered. 857 commits, 7 weeks, spare time."
- "That's card 3 from the previous slide — in my own work. The techniques you're about to learn are the ones that produced this."

**[BACKUP: If app is unavailable — walk through the 4 stat cards, reference the pipeline architecture]**

**Transition:** "Here's the shape of the day."

---

## Slide 4: Agenda | 9:37 | 1 min

**[CLICK]**

- Morning: theory (specs, TDD), then Lab 0 (guided hands-on together), then theory (tools), then Lab 1 (track-specific)
- After lunch: Lab 2 (track-specific), then team demos and voting
- "Breaks are real breaks — ask questions anytime, don't save them"

**Transition:** "Let's warm up with a quiz."

---

## Slide 5: Ice Breaker — Grocery Data Predictions | 9:38 | 7 min

**[CLICK]**

**[ENERGY]** Form teams — 1 min. Mix of experience levels. Team names. Assign Person A/B/C roles.

- 3 questions on screen, 45–60 seconds each, write on prediction cards
- No phones, no Googling — gut instinct only

**[Read each question aloud:]**

1. Which state has highest monthly food retail turnover?
2. % increase in Australian food prices since Jan 2020?
3. Biggest price increase since 2020 — dairy, meat, fruit, or bread & cereals?

**[DO NOT reveal answers yet — save for Show & Tell]**

- Each team: share your boldest prediction (~1 min total)
- Write boldest predictions on the scoreboard
- "The twist: Lab 1 builds the pipeline that ingests this exact data — we'll query your Gold tables for the real answers"

**[CHECKPOINT: Should be wrapping at 9:45]**

**Transition:** "Quick look at Databricks today."

---

## Slide 6: Databricks Today | 9:45 | 2 min

**[CLICK]**

- Walk the platform stack bottom-up: open formats, Unity Catalog, data layer, Genie, applications
- Call out MCP servers (glue connecting agents to platform) and AI Gateway (routing to Claude Opus 4.6)
- "Today you'll touch almost every layer — Lakeflow, UC, Genie, AI/BI, Custom Apps, MCP"

**[ASK]** "Has everyone accessed their Coding Agents instance? Any issues?"

- Troubleshoot NOW — do not let anyone reach the exercise with broken access

**Transition:** "Now the paradigm shift that makes this possible."

---

## Slide 7: Section — The Paradigm Shift | 9:47 | 1 min

**[CLICK]**

**[PAUSE — let section title land]**

**[ASK]** "Show of hands — who's used an AI coding tool? ChatGPT? Copilot? Cursor? Claude?"

- Most hands up — note the range of usage
- "Today we take ad-hoc prompting to a repeatable, disciplined workflow"

---

## Slide 8: Watch First (Paradigm-Shift Demo) | 9:48 | ~2 min total

**[CLICK]** Slide stays up for 30 seconds.

- Read the Karpathy quote off the slide: *"...fully give in to the vibes, embrace exponentials, forget that the code even exists."*
- Frame: *"I'm not going to define 'coding agent' with more slides. I'll show you one. Then we teach the technique. Then you use it yourselves."*
- Mention CODA in ONE sentence: *"Environment's called CODA — Claude Code on a Databricks App, 39 skills pre-loaded. You'll use it all day."*

**[FLIP TO TERMINAL — CODA tab already open]** ~60-90 seconds.

- Run ONE demo prompt. Suggested: `claude "Open reference-implementation/src/bronze/abs_retail_trade.py and describe what it does in 3 bullet points."`
- Watch Claude open the file, reason about it, respond.
- No commentary while it runs. Let the interface speak.
- When it responds: *"That's what we mean when we say 'coding agent'. Now — how to direct one well."*

**Transition:** → Slide 9 (Specs & Testing section divider).

> **BACKUP:** If the terminal is slow or the prompt fails, skip the demo. Just say: *"You'll see it work plenty today. For now — how to direct one well."* Do NOT try to fix live.

> **NOTE:** Cut slides for this section (previously 8 "What is Vibe Coding", 9 "Platform Architecture", 8B "CODA"): too many concept slides for what a 60-second demo conveys better. CODA gets mentioned in one sentence on slide 8.

> **NOTE:** "What We're Building" (old static slide) has been REPLACED with a live Pipeline + Dashboard demo at slide 24. Today's Challenge moves to slide 25. See their new entries below, just before the Lab 0 section divider.

---

## Slide 9: Section — Specs & Testing | 9:50 | 30 sec

**[CLICK]**

- "The skill that matters most: your ability to specify what you want"
- "In this section we cover both specs and TDD — two sides of the same coin"

---

## Slide 13: Why Specs Matter | 10:01 | 5 min

**[CLICK]**

- "Garbage in, garbage out — but now at 100x speed"
- Anthropic mental model: "brilliant new employee who lacks context on your norms"
- Two tools: PRD (acceptance criteria, constraints, data contracts, examples) and CLAUDE.md (coding standards, architecture, testing, tool preferences)
- A good spec = clear acceptance criteria + constraints + example inputs/outputs

**Transition:** "Let me show you a CLAUDE.md."

---

## Slide 14: CLAUDE.md in Action | 10:06 | 3 min

**[CLICK]**

- Point at code example: PySpark not pandas, UC namespace, DATE type YYYY-MM-DD, pytest with small DataFrames
- One file, three scope levels — add one line, change all future output
- "Highest-ROI activity you can do with an AI agent"

**[PEPPER]** "I have 'always use uv run' in mine — one line, never have to remind the agent."

---

## Slide 15: CLAUDE.md Scope Levels | 10:09 | 2 min

**[CLICK]**

- User-level: personal prefs (home dir, applies everywhere)
- Repo-level: team standards (committed to git, shared)
- Project-level: module-specific rules (subdirectory, scoped)
- Cascade like CSS — more specific overrides general

**[ASK]** "What would you put at each level? Personal vs team standard?"

- Take 2-3 quick answers — primes them for Lab 0

---

## Slide 16: TDD Workflow | 10:11 | 3 min

**[CLICK]**

- "Rule #1 said: just say what you want. BDD is the same idea applied to testing."
- "You describe what should happen. The agent writes the test. Because it's Given/When/Then, you can actually read it back."
- Four steps: describe behavior, agent writes test, run/iterate, human reviews
- Key insight: the agent writes the code AND the tests — but you can verify the tests because they're plain English

---

## Slide 17: Why TDD is Exponentially More Powerful | 10:14 | 3 min

**[CLICK]**

- "The agent writes the tests, but you can read them. That's why this works."
- Unambiguous specs — "correct" = green tick
- Self-correcting loop — run, read failure, fix, repeat (no human in between)
- Guardrails — prevents agent from confidently producing elegant but wrong code

**[PEPPER]** "I've seen agents write beautiful, well-documented functions that are fundamentally wrong. A test would've caught it in seconds."

---

## Slide 18: Writing Tests That Guide the Agent | 10:17 | 3 min

**[CLICK]**

- Given-When-Then structure: given 10 rows (2 null), when clean, then 8 rows, no negatives
- Concrete values ("10 rows, 2 invalid" not "some rows")
- Descriptive names — test name IS the documentation
- Multiple assertions — schema, row counts, specific values

**[ASK]** "Who currently writes tests as part of their workflow?"

- Show of hands — either way: "Same skill, just applied to directing an agent"

---

## Slide 19: Anthropic Best Practices | 10:20 | 2 min

**[CLICK]**

- #1: Give Claude a way to verify its work — tests, screenshots, expected outputs
- #2: Explore first, plan, then code — use /plan mode
- "Cheap to course-correct in planning, expensive in code"

---

## Slide 20: Power Tools — Subagents, Skills, Hooks, Plugins | 10:21 | 3 min

**[CLICK]**

**[FRAMING FOR MIXED ROOM]** "This slide is for the experienced segment. If you've been using Claude Code for months, these are your leverage multipliers. If you're new, don't worry — these are things to know EXIST, not master today."

**[Walk each card 30–45 sec:]**

- **Subagents** — "Parallel workers with fresh context. Use them when you want an unbiased second opinion. `/review` spawns one. `Agent` tool launches one for specific tasks."
- **Skills** — "Reusable slash commands. `/commit`, `/review`, `/ship`, `/test`. Don't reinvent what's already in the marketplace. The Databricks plugin marketplace is `fe-vibe`."
- **Hooks** — "Deterministic guardrails. PreToolUse blocks bad tool calls. PostToolUse enforces policy. Stop refuses to finish until state is clean. We have an MCP auth guard hook running in this session right now."
- **Plugins** — "Package skills + agents + hooks for teams. Share via marketplace. One install, shared team conventions."

**[KEY MESSAGE]** "The gap between a one-shot prompt and a hooks-guarded skill-driven workflow is the same gap as cards 2 and 3 on the opening slide. Technique, not tool."

**[POINTER]** "Deep dive slides in the appendix (Subagents vs Teams, Skills for BDD, MCP architecture) — available if we have time at the end."

**Transition:** "Now the honest problem with working with AI agents."

---

## Slide 19B: The Sycophancy Problem | 10:24 | 3 min

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

## Slide 21: Small Steps Beat Big Bang | 10:27 | 3 min **[NEW — central technique]**

**[CLICK]**

**[SYNTHESIS FRAMING]** "Everything we've talked about so far — Verification, Sycophancy, Writing Tests — lands on one technique. Every prompt you send is one verifiable step. That's it."

**[Walk the LEFT column — Big Bang, the ChatGPT habit:]**

- "This is what people do when they bring ChatGPT habits to Claude Code." Read the red prompt aloud.
- "What happens: agent sits for 15 minutes generating files. You sit there. No visibility into what it's doing. Eventually you get a pile of code you didn't watch. Multiple failures hit at once. You debug blindly."
- "And this is the sycophancy trap on steroids. You can't challenge the agent on a 15-minute monologue — you just trust it."

**[Walk the RIGHT column — Small Steps:]**

- Read the five green prompts aloud: skeleton → table → test → run → quality rule.
- "Each one is 1-3 minutes. After each, you verify — test output, schema, one decorator added. If it drifted, you catch it in 90 seconds, not 15 minutes."
- "You see the agent reason. You can disagree. You stay in the loop."

**[LAND THE HEURISTIC — read it slowly off the slide:]**

- *"After this prompt finishes, will I KNOW whether it worked?"*
- "If the answer is 'I'll have to trust it and check later' — the prompt is too big. Split it."

**[WORKSHOP-LEVEL CALLOUT]** "The labs today are built on this cadence. If you catch yourself about to send a giant prompt in the lab — stop. Split it. That's the technique."

**Transition:** "Now let's talk about one more thing that makes small steps even more important — context windows."

---

## Slide 22: What Are Tokens | 10:30 | 2 min

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

## Slide 22: Managing Context Windows | 10:24 | 2 min

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

## Slide 23: Live Demo — TDD in Action | 10:26 | 3 min

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

## Slide 24: Live Demo — Pipeline + Dashboard End-to-End | 10:25 | ~4-5 min **[ARC D CLIMAX]**

**[CLICK]** Slide stays up for ~30 seconds while you frame.

- *"You've just learned the technique. Now watch it work end-to-end on a real pipeline."*
- *"This isn't a pre-recorded demo. The pipeline is running on my instance right now. The dashboard is already open. I'm going to add one new metric, BDD-style, and you'll see it flow through."*

**[FLIP TO BROWSER — AI/BI dashboard tab already open]** ~30 seconds.

- *"This is gold_retail_summary. ABS retail data, monthly turnover by state, rolling averages. Refreshed this morning."*
- Pause, let them read the charts.
- *"Notice there's no year-over-year column. Let me add one."*

**[FLIP TO TERMINAL — CODA, reference-implementation loaded]**

**[PROMPT 1 — the test] (~45 sec)**

```
Write ONE pytest test in tests/test_gold_retail_summary.py named
test_gold_has_yoy_growth. 24-month sample DataFrame for NSW,
turnover_millions increasing 5% MoM. Assert a yoy_growth_pct column
exists and month 13's value is approximately 79.6%.

Do NOT implement yet. Just the test.
```

- Read the test aloud.
- *"There's the spec. Sample data, expected value, one column."*

**[PROMPT 2 — run red] (~15 sec)**

```
Run that test. Show me the failure.
```

- *"Red. Good."*

**[PROMPT 3 — implement] (~45 sec)**

```
Add a yoy_growth_pct column to src/gold/retail_summary.py using a
window function partitioned by state ordered by month_date, comparing
each row's turnover_millions to the row 12 months prior. Percentage
change. Nothing else.
```

- *"Re-run the test."* → Green.
- *"Green. Two prompts."*

**[PROMPT 4 — deploy + dashboard refresh] (~90 sec)**

```
databricks bundle deploy -t demo && databricks bundle run grocery-intelligence-demo -t demo
```

- While pipeline runs, narrate: *"The pipeline's materialising the new column. This takes about a minute."*
- When done, **[FLIP TO DASHBOARD]**, refresh.
- Point at the new `yoy_growth_pct` column visible in the data.
- **"Four prompts. One metric. End-to-end in under five minutes. That's what Lab 1 looks like."**

**Transition:** *"Quick look at what your team's building, then we start."*

> **FULL PRE-DEPLOY CHECKLIST + FALLBACKS:** `starter-kit/demos/pipeline-and-dashboard-demo.md`
>
> Key rule from the demo doc: **if the deploy takes >90 sec, skip the dashboard flip**. Move on to Today's Challenge. Do not wait live.

> **NOTE:** This replaces the old static "What We're Building — End State" slide. Showing the end state *live* is stronger than describing it.

---

## Slide 25: Today's Challenge | 10:28 | 1 min **[MOVED from early theory]**

**[CLICK]**

- Real ABS data: retail trade + food price indices + FSANZ recalls
- Stack: PySpark, Lakeflow, FastAPI, DABs
- Lab 0 = guided setup (all together), Labs 1–2 = track-specific
- Teams pick their angle (Retail Performance, Food Inflation, Food Safety, Market Intelligence)
- "The CLAUDE.md you write in Lab 0 guides both labs — make it count"

**Transition:** "Let's go. Lab 0."

---

## Slide 26: Section — Lab 0: Guided Hands-On | 10:44 | 30 sec

**[CLICK]**

**[ENERGY]** "Welcome back! Lab 0 — everyone together, hands on keyboards. This is guided — I'll walk you through each step."

---

## Slide 25: Lab 0 Briefing | 10:44 | 2 min

**[CLICK]**

**[TIMER: 45 min — Lab 0 runs 10:45 to 11:30]**

- "This is a guided session — everyone does the same three things before we split into tracks"
- Three milestones:
  1. **Rule #1: Just Say What You Want** (15 min) — tell Claude about your project, it initializes everything
  2. **Write your first test** (15 min) — TDD workflow, write a failing test, let the agent implement
  3. **Build bronze ingest** (15 min) — first Lakeflow table from ABS Retail Trade API
- "By 11:30, every team has an initialized project, a passing test, and data landing in bronze"
- "This is the foundation — Labs 1 and 2 build on top of this"

**Transition:** "Open your terminals. Let's go."

---

## Lab 0, Phase 1: Just Say What You Want | 10:47 | 15 min

**[TIMER: 15 min]**

**[PROJECT on screen — show Rule #1 slide]**

- "Rule #1 of vibe coding: you literally just say what you want. Don't write a file — have a conversation."
- "Open your terminal. Tell Claude about your project. Watch what happens."

> "I'm building a grocery intelligence platform on Databricks. Tech stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + React, DABs. Data sources: ABS SDMX APIs, FSANZ web scraping, ACCC PDF ingestion via UC Volumes. Unity Catalog namespace: workshop_vibe_coding.<team_schema>. Set up the project and create a CLAUDE.md."

**[WALK — Circulate full 15 min. Watch for:]**

- Teams trying to hand-write CLAUDE.md — redirect: "Just tell Claude what you want"
- Teams not reviewing output — remind them to read and refine through conversation
- Missing UC namespace — "Tell Claude your catalog and schema"
- The "aha" moment — when they realise they can just type what they want and it happens

**[At 12 min]** "Two minutes left — your project should be initialized."

**[At 15 min]** Quick check: "Hands up if Claude created your CLAUDE.md and project structure. Good. Notice — you didn't write a single config file by hand."

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

## Slide 26: Section — Tools for Labs 1 & 2 | 11:29 | 1 min

**[CLICK]**

**[ASK]** "Quick show — what worked well in Lab 0? What surprised you about TDD with the agent?"

- Take 2-3 answers
- "This next section is a focused tools briefing: Skills, MCP, Genie, AI/BI dashboards — everything you need for Labs 1 and 2"

---

## Slide 27: Practical Tips | 11:30 | 3 min

**[CLICK]**

- Start with the **default workflow callout** at top: "Start every non-trivial task with /plan. Even better — ask Claude to interview you about requirements before building."
- **Overengineering:** Claude loves extra files/abstractions — add "Keep solutions minimal. Do not add features beyond what is requested" to CLAUDE.md
- **Hallucinations:** Never trust claims about unread code — add "Never speculate about code you have not opened"
- **Course-correct early:** Check in every 2-3 tool calls — "stop, let's rethink this approach"
- **Challenge Claude:** After it implements, demand proof — "show me the git diff", "prove to me this works", "grill me on these changes". Then try: "knowing everything you know now, scrap this and implement the elegant solution" — second pass often produces cleaner code
- **Commit as checkpoints:** Every 15-20 minutes, use `/commit`. Commits are your safety net — if the agent goes off-rails, Esc-Esc to cancel, then rewind with git. [ASK] "Who has lost work by not committing? Don't let it happen today."
- **Use the starter-kit prompts** — they're copy-paste ready, no interpretation needed

---

## Slide 28: Skills & MCP — Practical Tools | 11:32 | 5 min

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

**Curation message (tie back to Rule #1):**
- "Skills are the curation step. Rule #1 says just say what you want. When you find yourself saying the same thing 3 times, save it as a skill — it's literally just a markdown file."
- "Same with tools — you don't always need an MCP server. Sometimes the tool is just an instruction: 'run this CLI command.' The agent reads the instruction and executes it."

- **[CALLOUT]** "There's a site called deathbyclawd.com — it scans SaaS products and tells you which ones can be replaced by a single Claude skill. A markdown file. That's how powerful this pattern is."

**Transition:** "Let me show you MCP on Databricks specifically."

---

## Slide 29: MCP on Databricks | 11:37 | 3 min

**[CLICK]**

- **Built-in/Managed:** UC functions, tables, volumes, Vector Search, Genie — zero config
- **Proxy/External:** third-party services (GitHub, Slack, Glean, Jira) routed through Databricks — UC Connections manage auth
- **Custom:** build your own, host on Databricks Apps — wrap internal APIs
- All secured through Unity Catalog
- "For Coles: wrap internal APIs, data tools, monitoring behind MCP servers — every agent gets access"

---

## Slide 30: Demo — Databricks Internal Claude Setup | 11:40 | 4 min

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

## Slide 31: Open Lakehouse — Managed Iceberg in UC | 11:44 | 4 min

**[CLICK]**

**[CALLBACK]** "Remember the Open Formats row on the platform-stack slide this morning? This is what it means in practice."

**[Walk the code block on the left:]**

- `CREATE OR REPLACE TABLE workshop.gold.retail_summary_iceberg USING ICEBERG CLUSTER BY (state, month_date) AS SELECT ...`
- "Three things to notice: `USING ICEBERG` not `DELTA`, `CLUSTER BY` not `PARTITIONED BY`, and no `LOCATION` clause — UC owns the physical layout."

**[Key rules — quick hit:]**

- **No `LOCATION`** — UC picks the path. You don't bring your own bucket.
- **No `PARTITIONED BY`** — liquid clustering only. Consistent with our SDP guidance.
- Everything else you know about UC still applies: ACLs, lineage, tags, sharing.

**[The payoff — this is the key message:]**

- "Once you've written to a managed Iceberg table in UC, external engines — Snowflake, Trino, DuckDB, BigQuery via BigLake — can read it through the Iceberg REST Catalog URL. **Zero copy.** Same governance."
- "For a retailer like Coles, this matters: it lets downstream teams consume your gold tables in whatever tool they already use, without exporting data or building replication pipelines."

**[When to pick which:]**

- **Iceberg when**: external engines read your tables, multi-cloud story, vendor-neutral requirement
- **Delta when**: deepest Databricks feature set (CDF, deletion vectors, identity columns), mostly-Databricks reads. Plus: UniForm gives you Iceberg-read from a Delta table for free.

**[POINTER]** "The DE track has this as an optional Lab 2 stretch goal — teams that finish early can publish their gold table as Iceberg and demo it at the end."

**Transition:** "Now Genie."

---

## Slide 32: Genie + AI/BI Dashboards | 11:48 | 7 min

**[CLICK]**

- **Genie:** natural language to SQL on UC tables — create space, point at gold tables, business users ask in plain English
- **AI/BI Dashboards:** auto-generated visualisations — describe what you want, get interactive dashboard
- Both connect to the gold tables from Lab 1

**[PEPPER]** "Dashboards for recurring views execs check weekly. Genie for ad-hoc questions in a meeting."

---

## Slide 33: Track Briefing — Choose Your Track | 11:55 | 10 min

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

## Slide 34: Section — Lab 1 | 12:05 | 30 sec

**[CLICK]**

**[ENERGY]** "Lab 1! Track-specific — you know your path. Make sure you have the right lab guide open."

---

## Slide 35: Lab 1 Briefing | 11:59 | 3 min

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

**[WALK + DEMO SIDEBARS — choreographed rhythm, not reactive:]**

- **12:15 (15 min):** Walk the room. "Should have first deliverable working. If not, grab a checkpoint."
- **12:25 (~20 min):** **[DEMO SIDEBAR — Model Mix Bake-Off, 90 sec]** See `starter-kit/demos/model-mix-bakeoff.md`. Terminal side-by-side: `claude --model haiku-4-5 "fix typo..."` (3 sec) vs `claude --model sonnet-4-6 "generate pytest fixture..."` (15-20 sec). Key message: pick the right tool for the task.
- **12:35 (30 min):** Walk. "Halfway. How's the track going? Any blockers?" Identify one team with clean silver/gold code for the next demo.
- **12:45 (~40 min):** **[DEMO SIDEBAR — `/review` on a team's code, 90 sec]** See `starter-kit/demos/review-subagent-demo.md`. Pre-selected team (asked consent during the 12:35 walk). Run `/review src/silver/...` on their code on the big screen. Demonstrates subagents in practice; one team gets real feedback.
- **12:50 (50 min):** "Ten minutes. Start wrapping up current phase."
- **13:00 (60 min):** "Stop building — prepare your Show & Tell. 2 min pitch, one interesting finding."

**[Common issues:]**

- Agent using pandas — "Add 'Always use PySpark, never pandas' to CLAUDE.md"
- ABS API timeout — "Grab a checkpoint"
- Agent rewriting working code — "Say: don't change passing functions"
- SparkSession errors — "Check conftest.py creates a local SparkSession"

---

## Slide 36: Show & Tell + Prediction Reveal | 12:59 | 15 min

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

## Slide 37: Section — Lab 2 | 13:59 | 30 sec

**[CLICK]**

**[ENERGY — Post-lunch, start interactive]**

**[ASK]** "What worked well in Lab 1? What surprised you?"

- Take 3-4 answers
- Ground this session in their experiences ("agent went off track — we covered tools that help", "context got heavy — we talked about that")
- "Lab 2 — same tracks, 60 more minutes. Use everything from today — CLAUDE.md, TDD, skills, MCP. This is where it all comes together."

---

## Slide 38: Lab 2 Briefing | 13:59 | 3 min

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

**[WALK + DEMO SIDEBARS — choreographed rhythm:]**

- **14:15 (15 min):** Walk the room. "Core build underway? Any blockers?"
- **14:20 (~20 min):** **[DEMO SIDEBAR — Small-Steps Save, 90 sec, PRE-RECORDED]** See `starter-kit/demos/small-steps-save.md`. Play the video — big-bang prompt hanging vs small-step prompts succeeding. Intro: *"Halfway through Lab 2 — this is the moment I'd warn my past self about."* No live demo; pre-recorded is safer.
- **14:30 (30 min):** Walk. "Halfway. How's the integration going? Any Genie/dashboard decisions needed?"
- **14:40 (~40 min):** **[DEMO SIDEBAR — Commit Cadence, 60 sec, LIVE]** See `starter-kit/demos/commit-cadence.md`. Quick live demo: run a test green, then `/commit` — skill generates the message. Key message: *"Green test → /commit. Every time. Don't lose work."*
- **14:50 (50 min):** "Ten minutes of building left. Wrap up current work."
- **14:55 (55 min):** "Stop building! Spend the last 5 min on your demo pitch."

**[Common issues:]**

- htmx not loading — check script tag in HTML head
- CORS errors — add CORSMiddleware to FastAPI
- Can't create Genie space — check permissions, help navigate UI
- Running out of time — "Working deliverable > perfect deliverable. Grab checkpoints."

---

## Slide 39: Team Demos & Voting | 14:59 | 30 min

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

## Slide 40: Key Takeaways | 15:29 | 5 min

**[CLICK]**

- **Specs are your leverage** — PRDs + CLAUDE.md multiply output tenfold
- **TDD + agents = deterministic outcomes** — write test, agent converges
- **Skills + MCP extend reach** — connect to external tools, Genie puts data in everyone's hands
- **Start small, iterate** — one function, one test, one deploy, then scale

**[ASK]** "Which resonated most with you today?"

---

## Slide 41: Next Steps | 15:34 | 5 min

**[CLICK]**

- **This week:** share learnings, set up team CLAUDE.md, try on one real task — start small
- **Coming soon:** broader team workshop, shared skill libraries, Genie on production data
- **Champions:** Farbod and Swee Hoe (internal), david.okeeffe@databricks.com (Databricks)

---

## Slide 42: Closing | 15:39 | 5 min

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
