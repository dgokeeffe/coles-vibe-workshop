# Facilitator Script — The Great Grocery Data Challenge

**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Audience:** Coles Group — Data & AI Engineering Team
**Duration:** 5 hours (10:00 AM - 3:00 PM)

---

## Before the Room Opens (9:30 AM)

- Slides loaded on the projector (slides.html, tested with keyboard nav)
- Coding Agents App instances up and verified (one per participant)
- Prediction cards printed (one per team)
- Scoreboard ready (whiteboard or shared doc)
- Backup demo recordings on laptop (in case of live demo failures)
- Lab guides open on your laptop: LAB-1-DATA-PIPELINE.md, LAB-2-APP-GENIE-DASHBOARD.md
- Water bottle. You will be talking for five hours.

---

## Slide 1: Title — 10:00 AM

**[CLICK]**

- Welcome, introductions — thanks to Farbod and Swee Hoe
- Five-hour hackathon, teams of 2-3, competing to build Grocery Intelligence Platform
- Using real Australian public data, directing AI agents
- "Skills you can use on Monday — literally Monday"

**[TRANSITION]** "Before any more slides — let me show you what this actually looks like in practice."

---

## Slide 1b: Opening Demo — My Working Setup — 10:02 AM

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

- "By end of today, you'll understand every piece of this: CLAUDE.md, skills, MCP, hooks, subagents"
- "You won't have 150 skills by 5pm — but you'll have the patterns to build them"

**[BACKUP: If demo fails — stay on the slide, walk through the 4 stat cards verbally, say "trust me, it's impressive when the WiFi cooperates"]**

**[TRANSITION]** "Let's warm up with a quiz."

---

## Slide 2: Ice Breaker — Grocery Data Predictions — 10:07 AM

**[CLICK]**

**[ENERGY]** Form teams — 2 min. Mix of experience levels. Team names.

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

**[TRANSITION]** "Let's look at the agenda."

---

## Slide 3: Agenda — 10:14 AM

**[CLICK]**

**[CHECKPOINT: Should be here by 10:15]**

- Morning: fundamentals (specs, TDD) then Lab 1 (data pipeline)
- Afternoon: advanced tools (MCP, subagents, Genie) then Lab 2 (full app)
- Finish with team demos and voting
- Breaks are real breaks — ask questions anytime, don't save them

**[TRANSITION]** "Before techniques — let me set the scene on Databricks today."

---

## Slide 4: Databricks Today — 10:15 AM

**[CLICK]**

- Walk the platform stack bottom-up: open formats, Unity Catalog, data layer, Genie, applications
- Call out MCP servers (glue connecting agents to platform) and AI Gateway (routing to Claude Opus 4.6)
- "Today you'll touch almost every layer — Lakeflow, UC, Genie, AI/BI, Custom Apps, MCP"

**[TRANSITION]** "Now the paradigm shift that makes this possible."

---

## Slide 5: Section — The Paradigm Shift — 10:18 AM

**[CLICK]**

**[PAUSE — let section title land]**

**[ASK]** "Show of hands — who's used an AI coding tool? ChatGPT? Copilot? Cursor? Claude?"

- Most hands up — note the range of usage
- "Today we take ad-hoc prompting to a repeatable, disciplined workflow"

---

## Slide 6: What is Vibe Coding — 10:19 AM

**[CLICK]**

- Read Karpathy quote: "...fully give in to the vibes, embrace exponentials, forget the code exists"
- Real term: agentic software development
- Traditional: write every line, slow iteration. Agentic: you direct, agent implements, tight feedback loops
- "Amplification, not replacement — you still need to know good code, your data, your architecture"

**[PEPPER]** "A brilliant intern joined your team — writes code at incredible speed but doesn't know your systems. How you onboard them determines how useful they are."

**[TRANSITION]** "Let me show you the platform."

---

## Slide 7: Coding Agents Databricks App — 10:22 AM

**[CLICK]**

- Walk through architecture left-to-right: browser terminal, Flask app, AI agent, AI Gateway
- 39 pre-built skills from AI Dev Kit, MCP for tool access, MLflow tracing for observability

**[ASK]** "Has everyone accessed their Coding Agents instance? Any issues?"

- Troubleshoot NOW — do not let anyone reach the exercise with broken access

**[TRANSITION]** "Session 1 — the single most important skill."

---

## Slide 8: Section — Thinking in Specs — 10:24 AM

**[CLICK]**

**[CHECKPOINT: Should be 10:15-10:25 — on track]**

- "The skill that matters most: your ability to specify what you want"
- Better specs = better output, full stop

---

## Slide 9: Why Specs Matter More with AI — 10:25 AM

**[CLICK]**

- "Garbage in, garbage out — but now at 100x speed"
- Anthropic mental model: "brilliant new employee who lacks context on your norms"
- Two tools: PRD (acceptance criteria, constraints, data contracts, examples) and CLAUDE.md (coding standards, architecture, testing, tool preferences)

**[TRANSITION]** "Let me show you a CLAUDE.md."

---

## Slide 10: CLAUDE.md in Action — 10:27 AM

**[CLICK]**

- Point at code example: PySpark not pandas, UC namespace, DATE type YYYY-MM-DD, pytest with small DataFrames
- One file, three scope levels — add one line, change all future output
- "Highest-ROI activity you can do with an AI agent"

**[PEPPER]** "I have 'always use uv run' in mine — one line, never have to remind the agent."

---

## Slide 11: CLAUDE.md Scope Levels — 10:29 AM

**[CLICK]**

- User-level: personal prefs (home dir, applies everywhere)
- Repo-level: team standards (committed to git, shared)
- Project-level: module-specific rules (subdirectory, scoped)
- Cascade like CSS — more specific overrides general

**[ASK]** "What would you put at each level? Personal vs team standard?"

- Take 2-3 quick answers — primes them for the exercise

---

## Slide 12: Today's Challenge — Grocery Intelligence Platform — 10:31 AM

**[CLICK]**

- Real ABS data: retail trade + food price indices
- Stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + Tailwind + htmx, DABs
- Lab 1 = pipeline (Bronze/Silver/Gold), Lab 2 = app + Genie + dashboard
- "The CLAUDE.md you write in the next 15 min will guide both labs — make it count"

**[TRANSITION]** "Open your terminals."

---

## Slide 13: Exercise — Write Your CLAUDE.md — 10:33 AM

**[CLICK]**

**[TIMER: 15 min]**

- Open Coding Agents terminal as a team
- Create project "grocery-intelligence"
- Ask agent to create CLAUDE.md (tech stack, data standards, testing)
- Review output, add team-specific rules
- Prompt template on screen — use as starting point

**[WALK — Circulate full 15 min. Watch for:]**

- Rules too vague — push for specificity ("Use PySpark, not pandas" not "use good practices")
- Teams not reviewing output — remind them to read and edit
- People writing code instead of CLAUDE.md — redirect

**[At 12 min]** "Two minutes left — pick one highlight to share."

**[At 15 min]** Quick round-robin: "What's one rule in your CLAUDE.md that'll help the agent most?"

- Highlight patterns: specific tech choices, naming conventions, testing standards
- Call out anti-patterns: vague rules, missing UC namespace

**[CHECKPOINT: Should be ~10:50 AM. Break until 11:00 or 11:05.]**

---

*--- BREAK: 10 min ---*

---

## Slide 14: Section — TDD + Agents — 11:05 AM

**[CLICK]**

**[CHECKPOINT: Should be here by 11:05]**

- "If you take one thing from today — write the tests first"

---

## Slide 15: TDD Workflow — 11:06 AM

**[CLICK]**

- Four steps: human writes test, agent implements, run/iterate, human reviews + edge cases
- Key insight: the test IS the spec — no ambiguity
- Agent reads test, sees "correct", writes code, verifies own work — tight feedback loop

---

## Slide 16: Why TDD is Exponentially More Powerful — 11:08 AM

**[CLICK]**

- Unambiguous specs — "correct" = green tick
- Self-correcting loop — run, read failure, fix, repeat (no human in between)
- Guardrails — prevents agent from confidently producing elegant but wrong code

**[PEPPER]** "I've seen agents write beautiful, well-documented functions that are fundamentally wrong. A test would've caught it in seconds."

---

## Slide 17: Writing Tests That Guide the Agent — 11:10 AM

**[CLICK]**

- Given-When-Then structure: given 10 rows (2 null), when clean, then 8 rows, no negatives
- Concrete values ("10 rows, 2 invalid" not "some rows")
- Descriptive names — test name IS the documentation
- Multiple assertions — schema, row counts, specific values

**[ASK]** "Who currently writes tests as part of their workflow?"

- Show of hands — either way: "Same skill, just applied to directing an agent"

---

## Slide 18: Anthropic's #1 Best Practice — 11:12 AM

**[CLICK]**

- #1: Give Claude a way to verify its work — tests, screenshots, expected outputs
- #2: Explore first, plan, then code — use /plan mode
- "Cheap to course-correct in planning, expensive in code"

---

## Slide 18b: What Are Tokens — 11:11 AM

**[CLICK]**

- Token ≈ 3/4 of a word, ~4 characters — not exactly words, not exactly characters
- Walk through the examples: sentence (~8), Python file (~2-3K), Harry Potter (~110K)
- **Two limits that matter today:**
  - **200K context window** — how much the agent can "see" at once. Fills up, older stuff gets forgotten.
  - **~1M tokens/min rate limit** — shared across ALL teams through AI Gateway
- **[PEPPER]** "If all 5 teams ask the agent to read every file in the repo at the same time, everyone slows down. Be specific."
- Practical tip: small focused requests = faster responses for everyone

**[TRANSITION]** "So how do we manage this finite resource?"

---

## Slide 19: Managing Context Windows — 11:14 AM

**[CLICK]**

- Context window = agent's working memory (~200K tokens, fills fast)
- CLAUDE.md, file reads, tool results, conversation turns all consume tokens
- Auto-compaction = agent forgets earlier details

**[Four strategies:]**

- Keep CLAUDE.md lean (~50 lines, loaded every turn)
- Offload exploration to subagents (isolated context)
- Plan before building (/plan)
- Use team members for parallel work (each gets own context)

**[PEPPER]** "Think of it like RAM. Manage it, or the OS starts swapping."

---

## Slide 20: Live Demo — TDD in Action — 11:17 AM

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

---

## Slide 21: Section — Lab 1 — 11:22 AM

**[CLICK]**

**[ENERGY]** "Lab 1! Sixty-five minutes. Make sure terminals are open — flag access issues now."

---

## Slide 22: Practical Tips for the Labs — 11:23 AM

**[CLICK]**

- **Overengineering:** Claude loves extra files/abstractions — add "Keep solutions minimal. Do not add features beyond what is requested" to CLAUDE.md
- **Hallucinations:** Never trust claims about unread code — add "Never speculate about code you have not opened"
- **Course-correct early:** Check in every 2-3 tool calls — "stop, let's rethink this approach"

---

## Slide 23: Lab 1 Briefing — 11:25 AM

**[CLICK]**

**[TIMER: 65 min — Lab 1 starts now]**

- Mission: Lakeflow Declarative Pipeline, ABS data, Bronze/Silver/Gold, TDD
- Phase 1: write tests (15 min)
- Phase 2: bronze layer (15 min)
- Phase 3: silver + gold (20 min)
- Phase 4: deploy with DABs (10 min) + 5 min buffer
- Two sources: ABS Retail Trade API, ABS CPI Food API
- Silver decodes region/industry codes, parses dates; Gold adds rolling averages, YoY growth
- Checkpoints available at every phase — no shame, goal is every team has data for Lab 2

**[WALK — Circulate every 10 min:]**

- **15 min (11:40):** "Should have tests. If not, grab Checkpoint 1A, skip to silver."
- **30 min (11:55):** "Bronze should work. If stuck, grab Checkpoint 1A."
- **45 min (12:10):** "Gold tables should exist. If not, grab Checkpoint 1B."
- **55 min (12:20):** "Five minutes. Start preparing Show and Tell."

**[Common issues:]**

- Agent using pandas — "Add 'Always use PySpark, never pandas' to CLAUDE.md"
- ABS API timeout — "Grab Checkpoint 1A"
- Agent rewriting working code — "Say: don't change passing functions"
- SparkSession errors — "Check conftest.py creates a local SparkSession"

---

## Slide 24: Show & Tell + Prediction Reveal — 12:25 PM (7 min)

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

- Take 2-3 answers, reinforce Session 2 concepts

**[TRANSITION]** "Great work. Lunch — back at 1:05."

---

*--- LUNCH: ~35-40 min ---*

---

## Slide 25: Section — Beyond the Basics — 1:05 PM

**[CLICK]**

**[ENERGY — Post-lunch, start interactive]**

**[ASK]** "What worked well in Lab 1? What surprised you?"

- Take 3-4 answers
- Ground Session 3 in their experiences ("agent went off track — subagents help", "context got heavy — we'll cover that")
- "This session: MCP, subagents, skills, hooks, plugins, Genie, AI/BI dashboards"

---

## Slide 26: Subagents, Skills, Hooks & Plugins — 1:08 PM

**[CLICK]**

- **Subagents:** parallel workers, isolated context — build frontend while you do backend
- **Skills:** slash commands encoding domain knowledge (/commit, /review, custom /deploy-pipeline)
- **Hooks:** event-driven guardrails — pre-commit linting, post-edit formatting — deterministic, not AI
- **Plugins:** package skills + agents + hooks for your team — distributable, versioned

---

## Slide 27: Skills in Action — TDD Skill Chain — 1:12 PM

**[CLICK]**

- /prd-writer: interviews you, generates PRD with machine-verifiable criteria
- /test-generator: reads PRD, generates failing tests (one per criterion)
- /implementer: writes code to make all tests pass
- Key: skills generate tests from success criteria, not from code — define "done" before implementation

---

## Slide 27b: Subagents vs Agent Teams — 1:14 PM

**[CLICK]**

- Most people reach for multi-agent the moment things feel complex — almost always wrong instinct
- Right question: "what kind of coordination does this task need?"
- **Subagents = fire-and-forget** — like delegating focused questions to researchers
  - Isolated context, one job, result returns to parent
  - Can't talk to each other — that's a feature, keeps it predictable
  - Key benefit: **compression** — vast exploration → clean signal
  - Use when: embarrassingly parallel (research, exploration, lookups)
- **Agent Teams = ongoing coordination** — like a team in the same room
  - Long-running, peer-to-peer messaging, shared task list with `blockedBy`
  - Key benefit: **negotiation** — discovery in one thread changes another
  - Use when: agents must reconcile outputs before proceeding
- **[PEPPER]** "For Lab 2, subagents for parallel frontend/backend is the sweet spot. Don't overcomplicate it."
- **Design principle:** Start with one agent. Push it until it breaks. That tells you what to add.
- **Warning:** Parallel agents writing code make incompatible assumptions — subagents should explore, not write code simultaneously

**[TRANSITION]** Now how do agents connect to external tools?

---

## Slide 28: What is MCP — 1:18 PM

**[CLICK]**

- "The USB-C of AI agents"
- Before: custom integration per model per tool (3x3 = 9 connectors, scales to 200)
- After: one standard protocol — build once, every agent connects (Anthropic open-sourced late 2024)
- For Coles: build the MCP server once, any agent (Claude, Cursor, ChatGPT) can connect

---

## Slide 29: How MCP Works — 1:18 PM

**[CLICK]**

- Client-server: clients = AI agents, servers expose tools over JSON-RPC
- Agent discovers available tools, calls via protocol, gets structured responses
- Build once connect everywhere; structured not ad-hoc
- For Coles: wrap UC, internal APIs, Genie behind MCP servers — every agent gets access
- "MCP handles wiring. Skills handle knowledge. Agent orchestrates both."

---

## Slide 30: MCP on Databricks — 1:21 PM

**[CLICK]**

- **Built-in:** managed by Databricks — UC functions, tables, volumes, Vector Search, Genie — zero config
- **Proxy:** external services (GitHub, Slack, Glean, Jira) routed through Databricks — UC Connections manage auth
- **Custom:** build your own, host on Databricks Apps — wrap internal APIs
- All secured through Unity Catalog

---

## Slide 31: MCP Architecture on Databricks — 1:23 PM

**[CLICK]**

- Left: Databricks-served agents connect to custom/managed/third-party MCP servers
- Right: external agents (like your Claude Code today) connect to same servers
- Bottom: AI Gateway routes to model serving
- "Coles sits on the right today — external agent connecting via MCP, same security and governance"

---

## Slide 32: AI Dev Kit — 1:25 PM

**[CLICK]**

- **Skills:** 25+ skill packs (pipelines, dashboards, UC, Genie, MLflow) — knowledge layer
- **MCP Server:** 50+ tools (SQL, clusters, jobs, apps) — action layer
- **Tools Core:** Python library underneath — extend with your own
- **Builder App:** web chat UI — what you've been using today

**[PEPPER]** "For Coles: fork this repo, add custom skills — /run-data-quality, /deploy-pipeline, /check-lineage"

---

## Slide 33: How Databricks Uses Claude — LIVE DEMO — 1:28 PM

**[CLICK]**

**[DEMO — ~8 min]**

- Walk through Databricks internal setup on screen:
  - CLAUDE.md with company-wide standards — approved patterns, forbidden actions
  - Hooks: pre-commit linting/security, post-edit formatting — deterministic guardrails
  - Skills + MCP: custom slash commands, UC/Genie/internal service connections
  - settings.json: hooks config, MCP server config

**[Switch to live terminal, type:]**

```
Search the Databricks docs for how to create a Genie space programmatically.
```

- Point out: discovers tool, calls it, gets structured results
- "No copy-pasting from a browser — agent asked the docs directly"

**[BACKUP: If demo fails, walk through the settings.json on the slide.]**

- "This is reproducible — set up the same at Coles: CLAUDE.md, hooks, skills"

---

## Slide 34: Genie + AI/BI Dashboards — 1:36 PM

**[CLICK]**

- **Genie:** natural language to SQL on UC tables — create space, point at gold tables, business users ask in plain English
- **AI/BI Dashboards:** auto-generated visualisations — describe what you want, get interactive dashboard

**[PEPPER]** "Dashboards for recurring views execs check weekly. Genie for ad-hoc questions in a meeting."

**[TRANSITION]** "Time to build."

---

## Stretch Break — 1:37 PM

**[CLICK]**

- 5-min break — get people standing
- Post-lunch energy dip is real
- "Lab 2 is the capstone — everything you've learned comes together. Grab a coffee."

---

## Slide 35: Section — Lab 2 — 1:42 PM

**[CLICK]**

**[ENERGY]** "Lab 2 — the capstone. Sixty-five minutes. App, Genie, AI/BI dashboards. Use everything from today — CLAUDE.md, TDD, subagents, MCP. This is where it all comes together."

---

## Slide 36: Lab 2 Briefing — 1:40 PM

**[CLICK]**

**[ENERGY]** "This is the capstone — everything comes together"

- "Pick your tier — not every team needs to build the same thing"
- **Quick (20 min):** FastAPI + embedded AI/BI dashboard via iframe — polished with minimal code
- **Medium (35 min):** FastAPI + React with Recharts or Observable Plot — custom interactive charts
- **Stretch (55 min):** Full React app + embedded dashboard + Genie + NL query — the works
- "If you're unsure, start with Quick — you can always upgrade"
- Genie space is a 2-min win regardless of tier

**[TIMER: 55 min — Lab 2 starts now]**

- Phase 1: PRD + tests (10 min)
- Phase 2: backend + frontend (25 min) — pick your viz approach
- Phase 3: Genie + AI/BI dashboard (15 min) — create, publish, embed
- Phase 4: demo prep (5 min) — stop building, prepare pitch
- Use subagents for parallel work — one backend, one frontend
- **Embed tip:** Publish dashboard → Share → Embed → iframe in your app
- Bonus: build an MCP server wrapping your retail analytics

**[WALK — Circulate:]**

- **10 min (1:50):** "PRD and tests done? Agent should be implementing."
- **25 min (2:05):** "Backend working? Start Genie even if frontend isn't perfect."
- **40 min (2:20):** "Genie created? Start AI/BI dashboard."
- **50 min (2:30):** "Stop building! Spend last 5 min on your demo pitch."
- **55 min (2:35):** "Start preparing your 3-min demo!"

**[Common issues:]**

- htmx not loading — check script tag in HTML head
- CORS errors — add CORSMiddleware to FastAPI
- Can't create Genie space — check permissions, help navigate UI
- Running out of time — "Working app > perfect app. Grab checkpoints."

---

*--- BREAK: 10 min (2:30 - 2:40 PM) ---*

---

## Slide 37: Team Demos & Voting — 2:40 PM

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

## Slide 38: Key Takeaways — 2:52 PM

**[CLICK]**

- **Specs are your leverage** — PRDs + CLAUDE.md multiply output tenfold
- **TDD + agents = deterministic outcomes** — write test, agent converges
- **Subagents + MCP extend reach** — parallelise work, connect to external tools, Genie puts data in everyone's hands
- **Start small, iterate** — one function, one test, one deploy, then scale

**[ASK]** "Which resonated most with you today?"

---

## Slide 39: Next Steps — 2:55 PM

**[CLICK]**

- **This week:** share learnings, set up team CLAUDE.md, try on one real task — start small
- **Coming soon:** broader team workshop, shared skill libraries, Genie on production data
- **Champions:** Farbod and Swee Hoe (internal), david.okeeffe@databricks.com (Databricks)

---

## Slide 40: Closing — 2:58 PM

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

**[END — 3:00 PM]**

---

## Emergency Playbook

| Situation | Response |
|-----------|----------|
| **WiFi goes down** | Switch to phone hotspot for demos. Teams can work offline on tests/code, reconnect later. |
| **Coding Agents App crashes** | Restart the app. If persistent, pair affected person with another team member. |
| **Live demo fails** | "Live demos — always an adventure." Play the backup recording from your laptop. |
| **A team falls way behind** | Walk them to the checkpoint. "Grab Checkpoint 1B, get your gold tables loaded, and focus on Lab 2." |
| **One person dominates the team** | "Great energy — let's rotate the driver so everyone gets a turn." |
| **Post-lunch energy crash** | Start Session 3 with the interactive question. Stand up, walk around. Move quickly to Lab 2 to get hands back on keyboards. |
| **Running over time** | Compress Session 3 to 15 min. Cut Lab 2 to 55 min. Keep demos to 2 min each. |
| **Running under time** | Extend Lab 2. Add the bonus MCP server challenge. Let teams polish their demos. |
