# Facilitator Script — The Great Grocery Data Challenge

**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Audience:** Coles Group — Data & AI Engineering Team
**Duration:** 5 hours (9:00 AM - 2:00 PM)

---

## Before the Room Opens (8:30 AM)

- Slides loaded on the projector (slides.html, tested with keyboard nav)
- Coding Agents App instances up and verified (one per participant)
- Prediction cards printed (one per team)
- Scoreboard ready (whiteboard or shared doc)
- Starter-kit folder distributed to all teams (CLAUDE.md template, test stubs, prompts, cheatsheet, config)
- Backup demo recordings on laptop (in case of live demo failures)
- Lab guides open on your laptop: LAB-1-DATA-PIPELINE.md, LAB-2-APP-GENIE-DASHBOARD.md
- Water bottle. You will be talking for five hours.

---

## Slide 1: Title | 9:00 | 2 min

**[CLICK]**

- Welcome, introductions — thanks to Farbod and Swee Hoe
- Five-hour hackathon, teams of 2-3, competing to build Grocery Intelligence Platform
- Using real Australian public data, directing AI agents
- "Skills you can use on Monday — literally Monday"

**Transition:** "Before any more slides — let me show you what this actually looks like in practice."

---

## Slide 2: Opening Demo — My Working Setup | 9:02 | 5 min

**[CLICK to show the setup slide, then SWITCH to live Claude Code terminal]**

- "This is my actual working setup — not a demo environment, this is what I use every day"
- Point at the slide stats: 7 MCP servers, 150+ skills, 12 plugins, hooks for guardrails

**[DEMO — Show each layer in the terminal:]**

- `/status` or show MCP connections — "Seven MCP servers: Slack, JIRA, Confluence, Chrome DevTools, Databricks Docs, Glean, DeepWiki"
- Show the CLAUDE.md briefly — "This is my onboarding doc for the agent — MCP routing rules, subagent patterns, context management"
- Show hooks in settings — "Safety guardrails: blocks dangerous commands, logs telemetry, cleans up sessions"

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
- "You won't have 150 skills by 2pm — but you'll have the patterns to build them"

**[BACKUP: If demo fails — stay on the slide, walk through the 4 stat cards verbally, say "trust me, it's impressive when the WiFi cooperates"]**

**Transition:** "Let's warm up with a quiz."

---

## Slide 3: Ice Breaker — Grocery Data Predictions | 9:07 | 8 min

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

**Transition:** "Let's look at the agenda."

---

## Slide 4: Agenda | 9:14 | 1 min

**[CLICK]**

**[CHECKPOINT: Should be here by 9:15]**

- Morning: specs, TDD, then Lab 1 (data pipeline)
- After lunch: tools briefing, then Lab 2 (app + Genie + dashboards)
- Finish with team demos and voting
- "Breaks are real breaks — ask questions anytime, don't save them"

**Transition:** "Quick look at Databricks today."

---

## Slide 5: Databricks Today | 9:15 | 2 min

**[CLICK]**

- Walk the platform stack bottom-up: open formats, Unity Catalog, data layer, Genie, applications
- Call out MCP servers (glue connecting agents to platform) and AI Gateway (routing to Claude Opus 4.6)
- "Today you'll touch almost every layer — Lakeflow, UC, Genie, AI/BI, Custom Apps, MCP"

**[ASK]** "Has everyone accessed their Coding Agents instance? Any issues?"

- Troubleshoot NOW — do not let anyone reach the exercise with broken access

**Transition:** "Now the paradigm shift that makes this possible."

---

## Slide 6: Section — The Paradigm Shift | 9:17 | 1 min

**[CLICK]**

**[PAUSE — let section title land]**

**[ASK]** "Show of hands — who's used an AI coding tool? ChatGPT? Copilot? Cursor? Claude?"

- Most hands up — note the range of usage
- "Today we take ad-hoc prompting to a repeatable, disciplined workflow"

---

## Slide 7: What is Vibe Coding | 9:18 | 3 min

**[CLICK]**

- Read Karpathy quote: "...fully give in to the vibes, embrace exponentials, forget the code exists"
- Real term: agentic software development
- Traditional: write every line, slow iteration. Agentic: you direct, agent implements, tight feedback loops
- "Amplification, not replacement — you still need to know good code, your data, your architecture"

**[PEPPER]** "A brilliant intern joined your team — writes code at incredible speed but doesn't know your systems. How you onboard them determines how useful they are."

**Transition:** "Let me show you the platform."

---

## Slide 8: Platform Architecture | 9:20 | 2 min

**[CLICK]**

- Walk through architecture left-to-right: browser terminal, Flask app, AI agent, AI Gateway
- 39 pre-built skills from AI Dev Kit, MCP for tool access, MLflow tracing for observability

**Transition:** "Now let me show you where we're going today."

---

## Slide 9: What We're Building — End State | 9:22 | 3 min

**[CLICK]**

- "Before I teach you any techniques — let me show you WHERE we're going"
- Walk through the four quadrants:
  - **Data Pipeline** — Lakeflow ingesting ABS retail and food price data, Bronze to Silver to Gold
  - **Web Application** — FastAPI + Tailwind with dashboards, filters, AI-powered query feature
  - **Genie Space** — Business users type questions in English, get instant answers
  - **AI/BI Dashboard** — Auto-generated visualisations from your gold tables
- Point at the flow at the bottom: Pipeline -> App -> Genie -> Dashboard = Grocery Intelligence Platform
- **"By 2pm, every team will have all four of these running."**
- "Now that you can see the destination, the techniques I'm about to teach you will make a lot more sense"

**Transition:** "Let's look at the challenge details."

---

## Slide 10: Today's Challenge | 9:25 | 5 min

**[CLICK]**

- Real ABS data: retail trade + food price indices
- Stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + Tailwind + htmx, DABs
- Lab 1 = pipeline (Bronze/Silver/Gold), Lab 2 = app + Genie + dashboard
- Teams pick their angle (or invent their own)
- Briefly show the starter-kit folder and what's inside
- "The CLAUDE.md you write in the next 15 min will guide both labs — make it count"

**Transition:** "The skill that matters most."

---

## Slide 11: Section — Specs & TDD | 9:30 | 30 sec

**[CLICK]**

- "The skill that matters most: your ability to specify what you want"
- "In this section we cover both specs and TDD — two sides of the same coin"

---

## Slide 12: Why Specs Matter | 9:30 | 5 min

**[CLICK]**

- "Garbage in, garbage out — but now at 100x speed"
- Anthropic mental model: "brilliant new employee who lacks context on your norms"
- Two tools: PRD (acceptance criteria, constraints, data contracts, examples) and CLAUDE.md (coding standards, architecture, testing, tool preferences)
- A good spec = clear acceptance criteria + constraints + example inputs/outputs

**Transition:** "Let me show you a CLAUDE.md."

---

## Slide 13: CLAUDE.md in Action | 9:35 | 3 min

**[CLICK]**

- Point at code example: PySpark not pandas, UC namespace, DATE type YYYY-MM-DD, pytest with small DataFrames
- One file, three scope levels — add one line, change all future output
- "Highest-ROI activity you can do with an AI agent"

**[PEPPER]** "I have 'always use uv run' in mine — one line, never have to remind the agent."

---

## Slide 14: CLAUDE.md Scope Levels | 9:38 | 2 min

**[CLICK]**

- User-level: personal prefs (home dir, applies everywhere)
- Repo-level: team standards (committed to git, shared)
- Project-level: module-specific rules (subdirectory, scoped)
- Cascade like CSS — more specific overrides general

**[ASK]** "What would you put at each level? Personal vs team standard?"

- Take 2-3 quick answers — primes them for the exercise

**Transition:** "Time to write your own."

---

## Slide 15: Exercise — Write Your CLAUDE.md | 9:40 | 15 min

**[CLICK]**

**[TIMER: 15 min]**

- Open Coding Agents terminal as a team
- **Copy the starter-kit CLAUDE.md** into your project — customise it for your team angle
- Ask agent to fill in: tech stack, data standards, testing preferences
- Review output, add team-specific rules

> "Copy the starter-kit CLAUDE.md into our project. Customise it for our team: schema `workshop_vibe_coding.<team_schema>`, angle `<chosen_angle>`. Add our tech stack (PySpark, Lakeflow Declarative Pipelines, FastAPI, Tailwind CSS + htmx), our data standards (Unity Catalog, medallion architecture, date formats), and our testing standards (pytest, TDD, small test DataFrames)."

**[WALK — Circulate full 15 min. Watch for:]**

- Rules too vague — push for specificity ("Use PySpark, not pandas" not "use good practices")
- Teams not reviewing output — remind them to read and edit
- People writing code instead of CLAUDE.md — redirect

**[At 12 min]** "Two minutes left — pick one highlight to share."

**[At 15 min]** Quick round-robin: "What's one rule in your CLAUDE.md that'll help the agent most?"

- Highlight patterns: specific tech choices, naming conventions, testing standards
- Call out anti-patterns: vague rules, missing UC namespace

**[CHECKPOINT: Should be ~9:55 AM. Break at 10:00.]**

---

*--- BREAK: 10 min (10:00 - 10:10) ---*

---

## Slide 16: TDD Workflow | 10:10 | 3 min

**[CLICK]**

**[CHECKPOINT: Should be here by 10:10]**

- "If you take one thing from today — write the tests first"
- Four steps: human writes test, agent implements, run/iterate, human reviews + edge cases
- Key insight: the test IS the spec — no ambiguity
- Agent reads test, sees "correct", writes code, verifies own work — tight feedback loop

---

## Slide 17: Why TDD is Exponentially More Powerful | 10:13 | 3 min

**[CLICK]**

- Unambiguous specs — "correct" = green tick
- Self-correcting loop — run, read failure, fix, repeat (no human in between)
- Guardrails — prevents agent from confidently producing elegant but wrong code

**[PEPPER]** "I've seen agents write beautiful, well-documented functions that are fundamentally wrong. A test would've caught it in seconds."

---

## Slide 18: Writing Tests That Guide the Agent | 10:16 | 3 min

**[CLICK]**

- Given-When-Then structure: given 10 rows (2 null), when clean, then 8 rows, no negatives
- Concrete values ("10 rows, 2 invalid" not "some rows")
- Descriptive names — test name IS the documentation
- Multiple assertions — schema, row counts, specific values

**[ASK]** "Who currently writes tests as part of their workflow?"

- Show of hands — either way: "Same skill, just applied to directing an agent"

---

## Slide 19: Anthropic Best Practices | 10:19 | 2 min

**[CLICK]**

- #1: Give Claude a way to verify its work — tests, screenshots, expected outputs
- #2: Explore first, plan, then code — use /plan mode
- "Cheap to course-correct in planning, expensive in code"

---

## Slide 20: What Are Tokens | 10:21 | 2 min

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

## Slide 21: Managing Context Windows | 10:23 | 2 min

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

## Slide 22: Live Demo — TDD in Action | 10:25 | 5 min

**[CLICK]**

**[DEMO — ~5 min. Open Coding Agents terminal, full screen.]**

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

- "That's the workflow for both labs: write test, agent implements, iterate to green"

**Transition:** "Lab time."

---

## Slide 23: Section — Lab 1 | 10:30 | 30 sec

**[CLICK]**

**[ENERGY]** "Lab 1! Make sure terminals are open — flag access issues now."

---

## Slide 24: Practical Tips | 10:30 | 2 min

**[CLICK]**

- **Overengineering:** Claude loves extra files/abstractions — add "Keep solutions minimal. Do not add features beyond what is requested" to CLAUDE.md
- **Hallucinations:** Never trust claims about unread code — add "Never speculate about code you have not opened"
- **Course-correct early:** Check in every 2-3 tool calls — "stop, let's rethink this approach"
- **Use the starter-kit prompts** — they're copy-paste ready, no interpretation needed

---

## Slide 25: Lab 1 Briefing | 10:32 | 3 min

**[CLICK]**

**[TIMER: 55 min — Lab 1 starts at 10:35]**

- Mission: Lakeflow Declarative Pipeline, ABS data, Bronze/Silver/Gold, TDD
- Two sources: ABS Retail Trade API, ABS CPI Food API
- Silver decodes region/industry codes, parses dates; Gold adds rolling averages, YoY growth
- "Your goal: Gold tables queryable by Show & Tell at 11:30"
- Checkpoints available at every phase — no shame, goal is every team has data for Lab 2

**[Read the parallel task assignments:]**

> **Person A (Terminal):** Explore data sources, build retail bronze, build silver retail, validate + deploy
>
> **Person B (Terminal):** Set up CLAUDE.md from starter-kit, build CPI bronze, build silver CPI, verify tables in UC UI
>
> **Person C (Databricks UI):** Review test stubs and data source docs, verify UC schema, monitor tests + prepare gold specs, query gold tables for icebreaker answers
>
> **Teams of 2:** Combine Person B and C. Driver handles A, navigator handles B+C.

**[WALK — Circulate every 10 min:]**

- **10:50 (15 min):** "Should have tests. If not, grab Checkpoint 1A, skip to silver."
- **11:05 (30 min):** "Bronze should work. If stuck, grab Checkpoint 1A."
- **11:15 (40 min):** "Gold tables should exist. If not, grab Checkpoint 1B."
- **11:25 (50 min):** "Five minutes. Start preparing Show and Tell."

**[Common issues:]**

- Agent using pandas — "Add 'Always use PySpark, never pandas' to CLAUDE.md"
- ABS API timeout — "Grab Checkpoint 1A"
- Agent rewriting working code — "Say: don't change passing functions"
- SparkSession errors — "Check conftest.py creates a local SparkSession"

---

## Slide 26: Show & Tell + Prediction Reveal | 11:30 | 10 min

**[CLICK]**

**[ENERGY]** "Time's up! Let's see what you've built."

- 3 teams volunteer (90 sec each) — not every team presents
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

**Transition:** "Great work. Lunch — back at 12:10."

---

*--- LUNCH: 30 min (11:40 - 12:10) ---*

---

## Slide 27: Section — Tools for Lab 2 | 12:10 | 1 min

**[CLICK]**

**[ENERGY — Post-lunch, start interactive]**

**[ASK]** "What worked well in Lab 1? What surprised you?"

- Take 3-4 answers
- Ground this session in their experiences ("agent went off track — we'll cover tools that help", "context got heavy — we talked about that")
- "This is a focused tools briefing: Skills, MCP, Genie, AI/BI dashboards — everything you need for Lab 2"

---

## Slide 28: Skills & MCP — Practical Tools | 12:11 | 5 min

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

## Slide 29: MCP on Databricks | 12:16 | 3 min

**[CLICK]**

- **Built-in/Managed:** UC functions, tables, volumes, Vector Search, Genie — zero config
- **Proxy/External:** third-party services (GitHub, Slack, Glean, Jira) routed through Databricks — UC Connections manage auth
- **Custom:** build your own, host on Databricks Apps — wrap internal APIs
- All secured through Unity Catalog
- "For Coles: wrap internal APIs, data tools, monitoring behind MCP servers — every agent gets access"

---

## Slide 30: Demo — Databricks Internal Claude Setup | 12:19 | 4 min

**[CLICK]**

**[DEMO — ~4 min]**

- Walk through Databricks internal setup on screen:
  - CLAUDE.md with company-wide standards — approved patterns, forbidden actions
  - Hooks: pre-commit linting/security, post-edit formatting — deterministic guardrails
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

## Slide 31: Genie + AI/BI Dashboards | 12:23 | 2 min

**[CLICK]**

- **Genie:** natural language to SQL on UC tables — create space, point at gold tables, business users ask in plain English
- **AI/BI Dashboards:** auto-generated visualisations — describe what you want, get interactive dashboard
- Both connect to the gold tables from Lab 1

**[PEPPER]** "Dashboards for recurring views execs check weekly. Genie for ad-hoc questions in a meeting."

**Transition:** "Time to build."

---

## Slide 32: Section — Lab 2 | 12:25 | 30 sec

**[CLICK]**

**[ENERGY]** "Lab 2 — the capstone. App, Genie, AI/BI dashboards. Use everything from today — CLAUDE.md, TDD, skills, MCP. This is where it all comes together."

---

## Slide 33: Lab 2 Briefing | 12:25 | 5 min

**[CLICK]**

**[TIMER: 55 min — Lab 2 starts at 12:30]**

- "Get as far as you can — not every team will finish everything, and that's fine"
- **Pick your tier:**
  - **Quick (~20 min):** FastAPI + embedded AI/BI dashboard via iframe — polished with minimal code
  - **Medium (~35 min):** FastAPI + React with Recharts or Observable Plot — custom interactive charts
  - **Stretch (~55 min):** Full React app + embedded dashboard + Genie + NL query — the works
- "If you're unsure, start with Quick — you can always upgrade"
- Genie space is a 2-min win regardless of tier
- "Your goal: app running, Genie answering questions, dashboard showing metrics by 13:25"

**Phases:**
- Phase 1: PRD + tests + start Genie (10 min)
- Phase 2: backend + frontend + AI/BI dashboard (25 min)
- Phase 3: wire up + polish + embed dashboard (15 min)
- Phase 4: demo prep (5 min) — stop building, prepare pitch

**[Read the parallel task assignments:]**

> **Person A (Terminal):** Write PRD (use starter-kit template), build FastAPI backend, deploy app to Databricks Apps
>
> **Person B (Terminal):** Write API tests (use starter-kit test stubs), build frontend (HTML/Tailwind/htmx), test + polish
>
> **Person C (Databricks UI):** Create Genie space (select gold tables, add descriptions), create AI/BI dashboard (charts, filters, layout), get embed URL for the app
>
> **Teams of 2:** Person A handles backend + deployment. Person B handles frontend + Genie + dashboard (Genie and dashboard are UI tasks that run in parallel).

**Embed tip:** Publish dashboard -> Share -> Copy embed code -> `<iframe>` in your app

**Bonus:** Build an MCP server wrapping your retail analytics — let any agent query your data

**[WALK — Circulate:]**

- **12:40 (10 min):** "PRD and tests done? Agent should be implementing."
- **12:55 (25 min):** "Backend working? Start Genie even if frontend isn't perfect."
- **13:10 (40 min):** "Genie created? Start AI/BI dashboard."
- **13:20 (50 min):** "Stop building! Spend last 5 min on your demo pitch."

**[Common issues:]**

- htmx not loading — check script tag in HTML head
- CORS errors — add CORSMiddleware to FastAPI
- Can't create Genie space — check permissions, help navigate UI
- Running out of time — "Working app > perfect app. Grab checkpoints."

---

*--- BREAK: 10 min (13:25 - 13:35) ---*

---

## Slide 34: Team Demos & Voting | 13:35 | 20 min

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

## Slide 35: Key Takeaways | 13:55 | 2 min

**[CLICK]**

- **Specs are your leverage** — PRDs + CLAUDE.md multiply output tenfold
- **TDD + agents = deterministic outcomes** — write test, agent converges
- **Skills + MCP extend reach** — connect to external tools, Genie puts data in everyone's hands
- **Start small, iterate** — one function, one test, one deploy, then scale

**[ASK]** "Which resonated most with you today?"

---

## Slide 36: Next Steps | 13:57 | 2 min

**[CLICK]**

- **This week:** share learnings, set up team CLAUDE.md, try on one real task — start small
- **Coming soon:** broader team workshop, shared skill libraries, Genie on production data
- **Champions:** Farbod and Swee Hoe (internal), david.okeeffe@databricks.com (Databricks)

---

## Slide 37: Closing | 13:59 | 1 min

**[CLICK]**

**[PAUSE — let the slide land]**

- "The best teams will be those who can effectively direct AI agents — together."

**[Make eye contact]**

- Thank the room — time, energy, willingness to experiment
- Congrats to Team [winner]
- "You built real working platforms in five hours"
- Email on screen, here for follow-up
- Questions?

*[If none:]* "Go build something great this week."

**[END — 14:00]**

---

## Appendix Slides (if time permits or questions arise)

### Appendix A: Subagents, Skills, Hooks & Plugins

- **Subagents:** parallel workers, isolated context — build frontend while you do backend
- **Skills:** slash commands encoding domain knowledge (/commit, /review, custom /deploy-pipeline)
- **Hooks:** event-driven guardrails — pre-commit linting, post-edit formatting — deterministic, not AI
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
| **A team falls way behind** | Walk them to the checkpoint. "Grab Checkpoint 1B, get your gold tables loaded, and focus on Lab 2." |
| **One person dominates the team** | "Great energy — let's rotate the driver so everyone gets a turn." |
| **Post-lunch energy crash** | Start with the interactive question. Stand up, walk around. Move quickly to Lab 2 to get hands back on keyboards. |
| **Running over time** | Compress Tools for Lab 2 to 10 min (cut Databricks internal demo). Cut Lab 2 to 50 min. Keep demos to 2 min each. |
| **Running under time** | Extend Lab 2. Add the bonus MCP server challenge. Let teams polish their demos. |
