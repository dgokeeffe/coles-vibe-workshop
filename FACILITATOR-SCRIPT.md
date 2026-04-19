# Facilitator Script — The Great Grocery Data Challenge

**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Audience:** Coles Group — Data & AI Engineering Team
**Duration:** 7 hours (10:00 AM – 17:00 PM), 6 contact hours + lunch

---

## Before the Room Opens (09:30)

- Slides loaded on the projector (`slides.html`, tested with keyboard nav + press **N** for speaker notes overlay)
- **Pipeline + Dashboard pre-deployed** — reference-implementation pipeline running, AI/BI dashboard open in a browser tab, warehouse warm. Full checklist: `starter-kit/demos/pipeline-and-dashboard-demo.md`
- **Quiz-app deployed** — URL + QR code visible on Slide 9, admin view pre-logged-in on facilitator laptop. Test one submission end-to-end before doors open.
- Coding Agents (CODA) terminal tab open, claude logged in, skills loaded
- Backup recordings on laptop (mini-demo, pipeline demo, `/review` demo, commit-cadence demo) — see `starter-kit/demos/`
- Lab guides open in another tab: `LAB-0-GETTING-STARTED.md`, `LAB-1-DE.md`, `LAB-1-DS.md`, `LAB-1-ANALYST.md`, `LAB-2-*.md`
- Starter-kit distributed to each pair (CLAUDE.md template, test stubs, prompts, cheatsheet)
- Prize ready for quiz-app winner (announced at lunch) and demo winners (announced at close)
- Water bottle. You will be talking for six hours.

---

# BLOCK 1 — Opener (10:00–10:10)

> **Arc:** Set frame before any tool. Not "AI makes you 30% faster" — "verification is the new bottleneck." Tell YWS story as lived proof. Show the 6-hours-from-now destination.

---

## Slide 1: Title | 10:00 | 90 sec

**[CLICK]**

- Welcome — thanks to Farbod and Swee Hoe for organising. Introduce yourself briefly.
- Frame: 10:00–17:00, 6 contact hours, **pair programming** (not teams of 3), three tracks, one Grocery Intelligence Platform.
- Point at the compact agenda strip on the slide — "Opener, Demo, Quiz, Teach, Lunch, Lab 1, Lab 2, Demos."
- "You will leave with skills you can use on Monday — literally Monday."

**Transition:** "Before any theory — let me tell you what I was doing seven weeks ago."

---

## Slide 2: The AI Coding Moment | 10:01 | 90 sec

**[CLICK]**

- **ONE stat, ONE idea.** Point at `4h → 2m`. "Same task, same CTO, Claude Code. Higher quality output. MIT Tech Review." Do not read the source strip — just point at it.
- "Every major recent read agrees: the new bottleneck is **verification and coordination**, not code generation."
- **[ASK]** "Who has felt this inflection in your own work? Same task, different speed?" Expect 3–5 hands.
- "Today you learn the practices that put you on the leverage side."

**Transition:** "Here's what it looked like when I lived it."

> **NOTE:** The five-stat card walkthrough from the old deck is cut. If the room looks sceptical, keep the METR "felt 20% faster, were 19% slower" data point in reserve — do not open with it.

---

## Slide 3: Your Weekly Specials | 10:02 | 3 min

**[CLICK]**

- "This is Your Weekly Specials — a system I built for Coles. 4.5 million Flybuys members get 13 personalised grocery offers every week."
- Walk the four stat cards:
  - **4.5M members** · 13 personalised offers/week
  - **857 commits** · 37K lines, 4 product lines, 340+ tests
  - **7 weeks** · spare time, nights and weekends, one engineer
  - **R→Py** · Full migration from R on Azure Batch VMs to native Databricks
- **[LAND THE STORY]** "The agent was my **domain tutor, not my typist.** I'm not a data scientist. I knew almost nothing about this system. Claude read the legacy R, explained why the lag structures existed, helped me port it to PySpark, solved distributed LightGBM on Ray when the obvious approach blew up memory."
- "That's the shift. Not 'AI writes code.' Agent as domain tutor."

**[BACKUP: If YWS app is up, show 10 sec of the UI. If not, just the stats.]**

**Transition:** "Here's what today ships. Six hours from now."

---

## Slide 4: Six Hours From Now | 10:05 | 90 sec **[NEW]**

**[CLICK]**

- Three-pane teaser: DE pipeline graph, DS forecasting app, Analyst Genie + AI/BI + FastAPI.
- "Three tracks. One platform. You pick your slice after lunch."
- Walk each pane in one line — DE (Bronze → Silver → Gold + quality gates), DS (feature pipeline + MLflow + serving + prediction UI), Analyst (Genie + dashboard + embedded FastAPI).
- **[LAND]** "These aren't toys — production-shape. Tests, quality gates, governance, deployable. One team last quarter shipped a slice of this in an afternoon. Your turn."

**Transition:** "Before I teach anything — let me show you me working."

---

# BLOCK 2 — Internal Demo (10:10–10:25)

> **Arc:** Show credibility through the screen, not the slides. Live terminal, narrate R.V.P.I. without naming it. Then the full end-to-end pipeline loop. Two things the room must notice: (1) you're directing, not typing; (2) every step has a verification artifact.

---

## Slide 5: Coding Agents at Databricks | 10:10 | 60 sec **[NEW]**

**[CLICK]**

- "Before I teach anything, let me show you me working. First — what we use Claude Code for at Databricks, internally."
- Walk the four cards fast (15 sec each): **PR Review**, **Refactors at Scale** (22K-line changes merged responsibly), **Test Generation** (BDD + property tests), **Internal Tools** (skills, MCP servers, this deck).
- "This isn't theory. It's what the people who built the platform use day-to-day."

**Transition:** "Here's the stack it runs on, then you'll see me inside it."

---

## Slide 6: The Stack You'll Touch Today | 10:11 | 2 min

**[CLICK]**

- Walk the platform diagram bottom-up — open formats, Unity Catalog, data layer, Genie, apps.
- Call out the two callout cards: **MCP Servers** (connect any AI agent to every layer) and **Proprietary Model Serving** (Anthropic/OpenAI/Google through AI Gateway with guardrails).
- "Today you touch almost every layer — Lakeflow, UC, Genie, AI/BI, Custom Apps, MCP, Model Serving."

**[ASK]** "Has everyone accessed their CODA instance? Any issues?"

- Troubleshoot NOW — do not let anyone reach the quiz with broken access.

**Transition:** "OK — screen time. Watch me work."

---

## Slide 7: Watch First | 10:13 | ~2 min total

**[CLICK]** Slide stays up for ~30 sec.

- Read the Karpathy line off the slide, but lightly — "forget that the code even exists." Frame comes next block.
- Mention CODA in one sentence: "Claude Code on a Databricks App, 39 skills pre-loaded. You'll use it all day."

**[FLIP TO TERMINAL — CODA tab already open]** ~90 sec.

- Run ONE tight prompt. Suggested: `claude "Open reference-implementation/src/bronze/abs_retail_trade.py and describe what it does in 3 bullet points."`
- **Narrate R.V.P.I. without naming it yet** — "Watch: it's reading the file first [Research], skimming to confirm what's there [Validate], I didn't ask for a plan on this one because the task is small [Plan collapses], now it's producing the output [Implement]."
- When it responds: "That's a small task. Now the bigger one — the full loop, end-to-end."

> **BACKUP:** If CODA is slow or the prompt fails, skip to Slide 8 demo. Do NOT try to fix live. Say: "You'll see it work plenty today."

---

## Slide 8: Live Demo — Pipeline + Dashboard | 10:15 | 4–5 min

**[CLICK]** Slide stays up ~30 sec.

- "Pipeline already running. Dashboard already open. I'm going to add one new metric, BDD-style, and you'll see it flow all the way through."
- Point at the diagram row — Test → Implement → Deploy → Dashboard.

**[FLIP TO BROWSER — AI/BI dashboard]** ~30 sec.

- "This is `gold_retail_summary`. ABS retail data, monthly turnover by state. Refreshed this morning. No share-of-national column yet — let me add one. *&lsquo;Share of national retail&rsquo; — per-state percentage of the monthly total. Tells you instantly who the biggest markets are.*"

**[FLIP TO TERMINAL — CODA, reference-implementation loaded]**

**Prompt 1 — test (~45 sec):**

```
Write ONE pytest test in tests/test_gold_retail_summary.py named
test_gold_has_state_share_of_national. Build a 6-row DataFrame: 2 states
(NSW, VIC, QLD) × 3 months. Turnover values in month 1: NSW=100, VIC=60,
QLD=40 (total 200). Assert a state_turnover_pct column exists; NSW month 1
is 50.0, VIC month 1 is 30.0, QLD month 1 is 20.0. Also assert that shares
sum to ~100 for any given month.

Do NOT implement yet. Just the test.
```

- Read the test aloud when it lands. "Six rows, numbers you can check in your head — 100 of 200 is 50%. That's the spec."

**Prompt 2 — run red (~15 sec):** `Run that test. Show me the failure.` → Red. Good.

**Prompt 3 — implement (~45 sec):**

```
Add a state_turnover_pct column to src/gold/retail_summary.py:
turnover_millions / sum(turnover_millions) over (partition by month_date) * 100

One window function. No LAG. No date arithmetic. Nothing else.
```

- Re-run test → green. "Two prompts."

**Prompt 4 — deploy + dashboard (~90 sec):**

```
databricks bundle deploy -t demo && databricks bundle run grocery-intelligence-demo -t demo
```

- Narrate while it runs: "Pipeline materialising the new column — about a minute."
- When done, **[FLIP TO DASHBOARD]**, refresh, show the new `state_turnover_pct` column. NSW ~35%, VIC ~26%, QLD ~20% — land it: *"that's Australia's retail map in one column."*
- **[LAND]** "Four prompts. One metric. End-to-end in under five minutes. Two things I want you to notice: first, I didn't *type* most of that — I directed it. Second, every step had a verification artifact. Test green, deploy succeeds, dashboard renders. **No verification, no trust.** We come back to that all day."

> **Key rule from `starter-kit/demos/pipeline-and-dashboard-demo.md`:** if the deploy takes >90 sec, skip the dashboard flip. Move on. Do not wait live.

**Transition:** "Enough of me talking. Your turn."

---

# BLOCK 3 — Quiz-App Icebreaker (10:25–10:40)

> **Arc:** Audience active before theory lands. The quiz itself is a build demo — this app was shipped in one weekend with Claude Code. Predictions come back at Show & Tell from their own Gold tables.

---

## Slide 9: Quiz-App Icebreaker | 10:25 | ~15 min total **[NEW — replaces prediction cards]**

**[CLICK]**

**[ENERGY]** "Open the QR code on your phone. Pick a team name. You've got 60 seconds."

- Project the slide — QR code, short URL `quiz.coles-vibe.app`, team-name hint.
- 60 sec join window. Watch admin view for team names appearing.

**[Run quiz — 8–10 min of live play.]**

- Questions mix grocery domain knowledge with **prediction questions** that map to Lab 1 Gold tables (household spend, state with highest retail turnover, CPI food increase, fastest-rising category, peak retail month).
- Live scoring. Banter between questions — call out clever team names.

**[After the game — flip to admin view, tease:]**

- "Three things to know before we go on. **One:** this app was built in one weekend by me and Claude Code — start to deploy. **Two:** the prediction questions — household spend, which state buys the most — those are the same questions your **Lab 1 Gold tables will answer**. We're coming back to this at Show & Tell to see who was closest. **Three:** this is the *smallest* thing you'll see shipped today. By 5 PM you'll have shipped something bigger."
- Prize at lunch for leading team; final prize for closest-to-actual at Show & Tell.

**[CHECKPOINT: wrap by 10:40]**

**Transition:** "Break — 10 minutes. Back at 10:50 for the technique."

---

*--- BREAK: 10 min (10:40 – 10:50) ---*

---

# BLOCK 4 — Get-to-Know-Claude (10:50–12:00)

> **Pressure block: 70 min, ~18 slides, guided demo style.** Drive from the terminal, slides are backdrop. **Name R.V.P.I. early and return to it at every sub-section boundary.** Everything else in this block is a specialisation of one R.V.P.I. phase.

---

## Slide 10: Techniques (Section Divider) | 10:50 | 30 sec

**[CLICK]**

**[PAUSE — let the title land]**

- "Everything I'm about to teach fits inside one loop. Let me name it first, then we specialise."

---

## Slide 11: R.V.P.I. Framework | 10:51 | 5 min **[NEW — the meta-framework]**

**[CLICK]**

**[FRAMING]** "Most AI-coding advice teaches R.P.I. — Research, Plan, Implement. V is missing. Today we add it."

- Walk the four phases left to right:
  - **Research** (teal) — gather context: read codebase, recall past decisions, pull docs. No opinions yet.
  - **Validate** (lava, highlighted) — **the missing letter.** Audit what Research returned. Three questions: *Is this current? Is this consistent? Is this trustworthy?*
  - **Plan** (amber) — design the change on top of *validated* context. Success criteria explicit.
  - **Implement** (green) — execute mechanically. Small steps. Verify after each.
- **[LAND THE CHEAPEST-INTERVENTION POINT]** Read the callout slowly: *"The cheapest place to catch a problem is between V and P. Stale CLAUDE.md? Drifted API reference? Free to fix before the plan. Expensive to fix after 20 implementation steps built around a wrong assumption."*
- "Every technique in this block — CLAUDE.md, Small Steps, Skills, MCP, BDD, Sycophancy, Context — is a specialisation of one R.V.P.I. phase. I'll call the loop back at every boundary."

**Transition:** "Concrete: what does each phase look like in Claude Code?"

---

## Slide 12: R.V.P.I. In The Terminal | 10:56 | 5 min **[NEW]**

**[CLICK]**

- Walk the four-phase mapping:
  - **Research** = `/init`, grep, read files, load a skill. Usually 30–60 sec of the agent reading.
  - **Validate** = re-read the CLAUDE.md, check a test still passes, ask *"is this file still how I remember it?"* This is the step everyone skips.
  - **Plan** = `/plan` or `ExitPlanMode`, or writing a Gherkin feature. You approve before code.
  - **Implement** = small steps with tests. Verify after each prompt.
- **[PEPPER]** "Human oversight happens twice — after V (correct the retrieved context), after P (approve the plan). If you don't have two oversight points per task, you're missing one."

**Transition:** "V's most important artifact is CLAUDE.md. Let's start there."

---

## Slide 13: Why Specs Matter | 11:01 | 3 min

**[CLICK]**

- "Garbage in, garbage out — now at 100× speed."
- Anthropic mental model: "brilliant new employee who lacks context on your norms."
- Two tools: **PRD** (acceptance criteria, constraints, data contracts, examples) and **CLAUDE.md** (coding standards, architecture, testing, tool preferences).
- A good spec = clear acceptance criteria + constraints + example inputs/outputs.

**Transition:** "Let me show you a CLAUDE.md."

---

## Slide 14: CLAUDE.md Example | 11:04 | 3 min

**[CLICK]**

- Point at the code example: PySpark not pandas, UC namespace, DATE type `YYYY-MM-DD`, pytest with small DataFrames.
- One file, three scope levels — add one line, change all future output.
- **[R.V.P.I. CALLBACK]** "This is the artifact Validate audits. CLAUDE.md was right yesterday — is it still right today? That's a V question."
- "Highest-ROI activity you can do with an AI agent."

**[PEPPER]** "I have 'always use uv run' in mine — one line, never have to remind the agent."

---

## Slide 15: CLAUDE.md Scope Levels | 11:07 | 2 min

**[CLICK]**

- **User-level**: personal prefs (`~/.claude/CLAUDE.md`), applies everywhere.
- **Repo-level**: team standards, committed to git, shared.
- **Project-level**: module-specific rules, scoped to a subdirectory.
- Cascades like CSS — more specific overrides general.

**[ASK]** "What would you put at each level? Personal vs team standard?" Take 2–3 quick answers.

**Transition:** "Your turn to write one."

---

## Slide 16: Rule #1 Exercise | 11:09 | 10 min **[COMPRESSED — pair-friendly]**

**[CLICK]**

**[TIMER: 10 min]**

- "Rule #1 of vibe coding: you literally just say what you want. Don't hand-write a config file — have a conversation."
- **Pair-friendly version:** driver types the prompt, navigator reads the output and challenges. Switch after 5 min.

> "I'm building a grocery intelligence platform on Databricks. Tech stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + React, DABs. Data sources: ABS SDMX APIs, FSANZ web scraping, ACCC PDF ingestion via UC Volumes. Unity Catalog namespace: workshop_vibe_coding.<team_schema>. Set up the project and create a CLAUDE.md."

**[WALK — circulate all 10 min. Watch for:]**

- Pairs hand-writing CLAUDE.md → redirect: "Just tell Claude what you want."
- Pairs not reviewing what the agent produced → "Navigator, read it out loud. Is anything wrong?"
- The "aha" moment when they realise they can just *type* what they want.

**[At 5 min]** "Swap driver and navigator."

**[At 10 min]** "Hands up if Claude created your CLAUDE.md. Good. Notice — you didn't write a single config file by hand. And the navigator had something to verify. That's the loop."

**Transition:** "Now the secret weapon — BDD with agents."

---

## Slide 17: BDD Workflow | 11:19 | 3 min

**[CLICK]**

- "Rule #1 said: just say what you want. BDD is the same idea applied to testing."
- Four-step flow: (1) human writes Gherkin features (Given/When/Then), (2) agent generates step definitions, (3) run `behave` and iterate, (4) human reviews.
- **KEY POINT — separate prompts:** Prompt 1 writes the Gherkin features. Prompt 2 implements the step definitions. If the same prompt does both, the agent writes steps that trivially pass rather than testing real behavior.

**Transition:** "Why is this exponentially more powerful than ad-hoc testing?"

---

## Slide 18: Why BDD Works with Agents | 11:22 | 3 min

**[CLICK]**

- **Plain-English specs** — anyone on the team can validate a feature file. Not just developers.
- **Self-correcting loop** — agent runs `behave`, reads failures, fixes step definitions. No human in between.
- **Guardrails** — feature files define the acceptance boundary. Agent can't claim success unless all scenarios pass.
- **[PEPPER]** "I've seen agents write beautiful, well-documented functions that are fundamentally wrong. A Gherkin scenario would've caught it in seconds."

**Transition:** "Let's look at Gherkin that actually guides the agent."

---

## Slide 19: Writing Gherkin That Guides | 11:25 | 3 min

**[CLICK]**

- Walk the Given-When-Then example on the left: given 10 rows (2 invalid), when clean, then 8 rows, no negatives.
- Right column — four principles: declarative steps, concrete values, one behavior per scenario, use Backgrounds for shared setup.
- **[ASK]** "Who's seen Gherkin before?" Usually a few hands. "Even if you haven't written code, you can write these specs. That's the whole point."

**Transition:** "Your toolkit. Quick tour."

---

## Slide 20: Power Tools — Subagents, Skills, Hooks, Plugins | 11:28 | 3 min

**[CLICK]**

**[FRAMING]** "This is the 'what's in your toolkit' slide. Quick orientation, not deep dive. All four are ways to automate V — catch drift, enforce policy, split cognition."

- **Subagents** — "Parallel workers with isolated context. `/review` spawns one. Useful when you want fresh-context judgment unpolluted by your current session."
- **Skills** — "Reusable slash commands from the marketplace (`/commit`, `/review`, `/ship`, `/test`). Don't reinvent what's already there. Databricks has `fe-vibe`."
- **Hooks** — "Deterministic guardrails. PreToolUse blocks bad tool calls. PostToolUse enforces policy. Stop refuses to finish until state is clean. **This is V automated** — check *before* the plan, not after the code."
- **Plugins** — "Package skills + agents + hooks for teams. One install, shared conventions."
- **[POINTER]** "Deep dive slides in the appendix — Subagents vs Teams, Skills for BDD, MCP architecture."

**Transition:** "Now — the core question every prompt should answer."

---

## Slide 21: Anthropic Best Practices | 11:31 | 3 min

**[CLICK]**

- "The core question every prompt should answer: **How will Claude PROVE this worked?** Not 'I think it works' — proof."
- Walk the six verification patterns on the left fast: BDD gates, separate prompts (tests vs implementation), `@dp.expect` data-quality constraints, schema contracts, full-suite regression, negative testing.
- Right column: explore first, plan, then code. **Cheap to course-correct in planning, expensive in code.**
- **[LAND]** "The difference between an agent that *thinks* it did the work and one that *proves* it did. That's the whole game."

**Transition:** "Now the uncomfortable truth about what skipping V costs you."

---

## Slide 22: The Sycophancy Problem | 11:34 | 3 min

**[CLICK — dark slide, let the stats land]**

- "Stanford published in Science this month: 11 production LLMs, 2,000+ real advice prompts."
- **49% more agreement than humans.** Killer stat: when the user was 100% wrong, AI still agreed **51% of the time**.
- Karpathy: spent 4 hours refining an argument with an LLM. Thought it was solid. Asked the same model to argue the opposite — it demolished his argument. His comment: *LOL*.
- "This is NOT a bug. RLHF trained for agreement. Models that weren't likable got deprecated."
- Four defenses on screen:
  1. **Karpathy Test** — ask it to argue the opposite before trusting any analysis.
  2. **"Wait a minute..."** — two words that measurably improve critical evaluation.
  3. **BDD** — structural verification; code passes or it doesn't.
  4. **Separate prompts** — one writes tests, another implements.
- **[R.V.P.I. CALLBACK]** "Sycophancy has two modes. The agent agrees with you when you're wrong now. Or the agent agrees with **itself from a past session** when the past session was wrong. Both need the same defense: validate your inputs before you plan on them. That's V."
- Code Rabbit data: AI-authored code has **1.7× more major issues, 2.7× more security vulnerabilities**.

**Transition:** "The engineering reframe that makes this stick."

---

## Slide 23: Memory As Untrusted Input | 11:37 | 3 min **[NEW]**

**[CLICK]**

- "You already treat external API responses as untrusted — you validate, type-check, handle failures. **Retrieved memory deserves the same posture.**"
- Why: memory is accumulated text with no principled write path. A badly-formatted tool output, a hallucinated memory write, an auto-accepted suggestion that was wrong — they all persist across sessions and influence every future recall.
- Four posture shifts on screen: logged writes, provenance metadata, surfaced conflicts, governance-layer human-in-the-loop.
- **[LAND]** "This is R.V.P.I.'s V-step articulated as a security posture. Your job as the engineer is to be Claude's librarian — catalogue, check out, retire when stale, flag when conflicting."

**Transition:** "Small Steps is how Implement stays honest **after** V has done its job."

---

## Slide 24: Small Steps — The Central Technique | 11:40 | 3 min

**[CLICK]**

**[SYNTHESIS FRAMING]** "This is THE mantra of the workshop. The single biggest difference between ChatGPT users and Claude Code power users."

**[Walk the LEFT column — Big Bang, the ChatGPT habit:]**

- Read the red prompt aloud ("build me the entire bronze layer").
- "What happens: agent sits for 15 minutes generating files. You sit there. No visibility. Eventually you get a pile of code you didn't watch. Multiple failures hit at once."
- "This is the sycophancy trap on steroids. You can't challenge a 15-minute monologue — you just trust it."

**[Walk the RIGHT column — Small Steps:]**

- Read the five green prompts: skeleton → table → test → run → quality rule.
- "Each one is 1–3 minutes. After each, you verify. If it drifted, you catch it in 90 seconds, not 15 minutes."
- "You see the agent reason. You can disagree. You stay in the loop."

**[LAND THE HEURISTIC — read slowly off the slide:]**

- *"After this prompt finishes, will I KNOW whether it worked?"*
- "If the answer is 'I'll have to trust it and check later' — the prompt is too big. Split it."
- **[R.V.P.I. CALLBACK]** "Every prompt is one R.V.P.I. loop in miniature. Small Steps is how Implement stays honest."

**[WORKSHOP-LEVEL CALLOUT]** "The labs are built on this cadence. If you catch yourself about to send a giant prompt — stop. Split it."

**Transition:** "One more reason small steps matter — context windows."

---

## Slide 25: What Are Tokens | 11:43 | 3 min

**[CLICK]**

- Token ≈ ¾ of a word, ~4 characters. Not exactly words, not exactly characters.
- Walk the examples: sentence (~8 tokens), 200-line Python file (~2–3K), Harry Potter (~110K).
- **Two limits that matter today:**
  - **200K context window** — how much the agent sees at once. Fills up, older stuff gets forgotten.
  - **~1M tokens/min rate limit** — shared across all pairs through AI Gateway.
- **[PEPPER]** "If five pairs all ask the agent to read every file in the repo at once, everyone slows down. Be specific."

**Transition:** "So how do you manage this finite resource?"

---

## Slide 26: Managing Context Windows | 11:46 | 4 min

**[CLICK]**

- Context window = agent's working memory. Claude's is ~200K tokens, roughly a medium novel.
- Fills up fast: every file read, every tool result, every conversation turn. Auto-compaction fires → agent forgets earlier details.
- Four strategies:
  - Keep CLAUDE.md lean (~50 lines, loaded every turn).
  - Plan before building (`/plan`).
  - Parallelise with subagents (each gets its own context).
  - Start new conversations for new tasks.
- **[R.V.P.I. CALLBACK]** "V prevents drift. Drift is why context management matters in the first place. Fresh context with a validated CLAUDE.md beats a bloated context carrying stale assumptions."
- **[PEPPER]** "Think of it like RAM. Manage it, or the OS starts swapping."

**[CHECKPOINT: should be here by 11:50]**

**Transition:** "Today's challenge — the thing you'll build."

---

## Slide 27: Today's Challenge | 11:50 | 3 min

**[CLICK]**

- Real ABS data: retail trade + CPI food + FSANZ recalls (already in Bronze).
- Stack: PySpark, Lakeflow, FastAPI, DABs.
- Three tracks — DE / DS / Analyst. Lab 1 builds on Bronze, Lab 2 ships it.
- **[R.V.P.I. reminder]** "The CLAUDE.md you wrote in Rule #1 guides both labs. Re-read it before each lab starts — that's the cheapest V step."

**Transition:** "Two slides on the tool layer you'll actually use, then lunch."

---

## Slide 28: Skills and Tools | 11:53 | 3 min

**[CLICK]**

**Skills (left column):**

- Slash commands encoding domain knowledge — `/commit`, `/test`, `/review`, `/deploy-dab`.
- "Type `/` in Claude Code to see what's available."
- **Curation pattern:** "Rule #1 says just say what you want. When you find yourself saying the same thing three times — save it as a skill. It's literally a markdown file."

**Tools (right column):**

- You don't always need an MCP server. Sometimes the tool is just an instruction: "run this CLI command." Agent reads the instruction, executes it.
- **[CALLOUT]** "deathbyclawd.com — scans SaaS products and tells you which ones can be replaced by a single Claude skill. A markdown file. That's how powerful this pattern is."

**Transition:** "Now MCP — where skills meet systems."

---

## Slide 29: MCP on Databricks | 11:56 | 3 min

**[CLICK]**

- **Built-in/Managed:** UC functions, tables, volumes, Vector Search, Genie — zero config.
- **Proxy/External:** third-party services (GitHub, Slack, Glean, Jira) routed through Databricks. UC Connections manage auth.
- **Custom:** build your own, host on Databricks Apps — wrap internal APIs.
- All secured through Unity Catalog.
- "For Coles: wrap internal APIs, data tools, monitoring behind MCP servers — every agent gets access."

**Transition:** "One final demo, then lunch."

---

## Slide 30: Demo — Databricks Internal Claude Setup | 11:58 | 2 min

**[CLICK]**

**[If time-tight:** point at the slide, walk it verbally in 60 sec, skip live terminal.**]**

- CLAUDE.md with company-wide standards (approved patterns, forbidden actions).
- Hooks: PostToolUse auto-formats Python with ruff on every edit. Stop hook runs verify-hint.sh. **Deterministic, not AI.**
- Skills + MCP: custom slash commands, UC/Genie/internal service connections.
- **[R.V.P.I. FRAME]** "These are all V automation. Hooks check before the plan. Skills standardise the verified patterns. This is reproducible — set up the same at Coles."

> **FALLBACK:** If you're running long, cut this to 60 sec. Walk the settings.json on-slide, don't go live.

**Transition:** "Lunch. Back at 13:00. Quiz prize announced then."

---

*--- LUNCH: 60 min (12:00 – 13:00) ---*

> **Pre-lunch:** announce quiz-app leading team, hand out prize. Flag: "Come back at 13:00 — pair formation and Lab 1 briefing."

---

# BLOCK 5 — Challenge Brief + Pair Formation (13:00–13:15)

> **Arc:** Set the pair norms explicitly before the lab. Verification is cheaper with two pairs of eyes. Fifteen-minute driver swaps. Navigator is the V in R.V.P.I.

---

## Slide 31: Open Lakehouse — Managed Iceberg in UC | 13:00 | 3 min

**[CLICK]**

**[CALLBACK]** "Remember the Open Formats row on the platform stack this morning? This is what it means in practice."

- `CREATE OR REPLACE TABLE workshop.gold.retail_summary_iceberg USING ICEBERG CLUSTER BY (state, month_date) AS SELECT ...`
- Three things to notice: `USING ICEBERG` not `DELTA`, `CLUSTER BY` not `PARTITIONED BY`, no `LOCATION` — UC owns storage.
- **Payoff:** external engines (Snowflake, Trino, DuckDB, BigQuery via BigLake) read through Iceberg REST Catalog. Zero copy, same governance.
- **When to pick which:** Iceberg for external engines / multi-cloud / vendor-neutral. Delta for deepest Databricks feature set.
- **[POINTER]** "DE track Lab 2 has an optional Iceberg stretch goal — teams that finish early can publish their gold table and demo it."

**Transition:** "Genie and AI/BI — the Analyst track's centre of gravity."

---

## Slide 32: Genie and AI/BI Dashboards | 13:03 | 3 min

**[CLICK]**

- **Genie:** natural language to SQL on UC tables. Create space, point at gold tables, business users ask in plain English.
- **AI/BI Dashboards:** auto-generated visualisations — describe what you want, get an interactive dashboard.
- Both connect to the gold tables from Lab 1.
- **[PEPPER]** "Dashboards for recurring views execs check weekly. Genie for ad-hoc questions in a meeting."

**Transition:** "Lab 1 briefing — but first, how we work."

---

## Slide 33: Section — Lab 1 | 13:06 | 30 sec

**[CLICK]**

- "Lab 1. Track-specific. Ninety minutes. You're **pairing** — not teams of 3. Two people per keyboard. Driver/Navigator. Fifteen-minute swaps. Next slide: the norms."

---

## Slide 34: Pair Programming Norms | 13:07 | 2 min **[NEW]**

**[CLICK]**

- **Why pairs, not teams of 3:** shipping with AI is a verification problem. Verification is cheaper with a second pair of eyes. **Solo is slower, not faster** — you'll skip V steps you wouldn't skip with a navigator watching.
- **Driver** (lava): types prompts, runs tests, commits code. Keeps prompts small. Reads out loud when it matters. Switches off every 15 min — **set a timer**.
- **Navigator** (green): reads, verifies, challenges. Especially at the V step. *"Is what Claude just said still true of our code?"* *"Did we skip a verification we should run?"* Flag sycophantic agreement.
- Three sidebar rules:
  - **Escalation:** if a task doesn't fit R.V.P.I. in 15 min, **split it**.
  - **Odd-numbered:** one triad — driver + navigator + observer (notes surprises).
  - **Commit cadence:** every 15 min run `/commit`. Rollback is free, lost work is not.
- **[LAND]** "Navigator is the V in R.V.P.I. Don't sit passively. Trust me on this, or prove me wrong by 5 PM."

**Transition:** "Find your pair. Choose your track."

---

## Slide 35: Lab 1 Briefing | 13:09 | 5 min

**[CLICK]**

**[TIMER: 90 min — Lab 1 runs 13:15 to 14:45]**

- "Pairs start with `LAB-0-GETTING-STARTED.md` — 10 min shared setup — then fork into your track."
- Walk the three track cards:
  - **Data Engineering** (lava) — Lakeflow pipeline (Bronze → Silver → Gold), `@dp.expect` quality rules, DABs deployment. Capability: managed Iceberg in UC. `LAB-1-DE.md` · `track-de.html`.
  - **Data Science** (purple) — feature engineering, MLflow experiment tracking, correlation analysis + EDA. Capability: MLflow + Model Serving. `LAB-1-DS.md` · `track-ds.html`.
  - **Analyst** (cyan) — Genie spaces (NL → SQL), AI/BI dashboards, column metadata tuning. Capability: Genie + AI/BI. `LAB-1-ANALYST.md` · `track-analyst.html`.

**[Walk the five-pattern sidebar — the practical-tips block, fold in fast:]**

- **Overeagerness:** tell Claude to keep solutions minimal; add to CLAUDE.md.
- **Hallucination prevention:** "never speculate about code you haven't opened."
- **Course-correct early:** check in every 2–3 tool calls. Don't let 10-min runs happen silently.
- **Challenge proof:** after implementation, demand `git diff` · argue the opposite · prove it works.
- **Commit cadence:** every 15 min `/commit`. Rollback is free, lost work is not.

**[LAND the R.V.P.I. reminder callout:]**

- "Before you start: re-read your CLAUDE.md. Is it still current? That's your first V step of the lab."

**Transition:** "Go."

---

# BLOCK 6 — Lab 1 (13:15–14:45, 90 min)

> **Arc:** Heads down. Facilitator circulates. One question every time you stop at a pair: *"Have you validated your CLAUDE.md yet?"* That's the whole game. Checkpoint callouts at 30 and 60 min.

---

## Lab 1 Facilitator Rhythm | 13:15 | 90 min

**[WALK the room from 13:15 — every 10–15 min:]**

- **13:15 (start)** Announce on mic: "Timers on. Fifteen-minute driver swaps. Commit every 15 min. Navigator reads actively."
- **13:30 (15 min in)** Walk. Primary question: *"Have you re-read your CLAUDE.md? Is it still right?"* Expected: first deliverable worked on — structure, first test, or initial prompt to set up the track.
- **13:45 (30 min — FIRST CHECKPOINT)** On mic: *"Thirty-minute checkpoint. You should have a test passing or one prompt's worth of working code committed. If you're not there, raise your hand."* Note teams who raise hands, visit them first.
- **13:50 (~35 min)** **[DEMO SIDEBAR — Model Mix Bake-Off, 90 sec]** See `starter-kit/demos/model-mix-bakeoff.md`. Terminal side-by-side: `claude --model haiku-4-5 "fix typo..."` (3 sec) vs `claude --model sonnet-4-6 "generate pytest fixture..."` (15–20 sec). Message: pick the right tool for the task.
- **14:05 (50 min)** Walk. Identify one pair with clean Silver/Gold code (or clean feature pipeline / clean Genie tuning) — ask consent for the `/review` demo.
- **14:15 (60 min — SECOND CHECKPOINT)** On mic: *"Sixty-minute checkpoint. You should have one Gold table, or one MLflow experiment run, or one tuned Genie answer committed. If not, grab a checkpoint — don't fight it."*
- **14:20 (~65 min)** **[DEMO SIDEBAR — `/review` on a pair's code, 90 sec]** See `starter-kit/demos/review-subagent-demo.md`. Pre-selected pair (asked at 14:05). Run `/review src/silver/...` on the big screen. Demonstrates subagents in practice; one pair gets real feedback.
- **14:35 (80 min)** "Ten minutes. Start wrapping. Leave the last 5 for `/commit` and Show & Tell prep."
- **14:45 (90 min)** "Stop building. Close editors. Show & Tell in 30 seconds."

**[Common issues — watch for:]**

- Agent using pandas → "Add 'Always use PySpark, never pandas' to CLAUDE.md." (V step failure.)
- ABS API timeout → "Grab the sample data from starter-kit."
- Agent rewriting working code → "Tell it: don't change passing functions."
- SparkSession errors → "Check conftest.py creates a local SparkSession."
- Pair both looking at one screen but only driver typing → "Navigator, what's Claude about to do? Say it out loud first."

---

# BLOCK 7 — Show & Tell + Quiz-App Reveal (14:45–15:00)

> **Arc:** Two pieces in 15 min. One highlight per track (30 sec each — not a full demo). Then quiz-app admin reveal using their own Gold tables. Closes the morning's loop.

---

## Slide 36: Show and Tell + Quiz-App Reveal | 14:45 | 15 min

**[CLICK]**

**[ENERGY]** "Pencils down. Fifteen minutes. Two things."

**Piece 1 — Track highlights (~6 min):**

- One pair per track volunteers. Not a full demo — **one thing that surprised you**, positive or negative. Strict 30 sec.
- **Facilitator prompts** (use if volunteers run dry): *"Where did R.V.P.I. save you? Where did you skip V and regret it?"*

**Piece 2 — Quiz-app reveal (~8 min):**

- Flip to quiz-app admin view. "Some of the prediction questions from this morning map to the Gold tables you just built."
- Query Lab 1 Gold tables live (or pre-queried if warehouse is cold). Walk:
  - Highest food retail turnover by state?
  - Food CPI increase since 2020?
  - Peak retail spending month?
  - Fastest-rising food category?
- Score against quiz-app leaderboard. **Highest-accuracy team on the leaderboard wins the prize.**
- **[LAND]** "You predicted these this morning. You built the pipeline that answers them. Here's the truth — from your own data."

**Transition:** "Ten-minute break. Lab 2 at 15:10."

---

*--- BREAK: 10 min (15:00 – 15:10) ---*

---

# BLOCK 8 — Lab 2 (15:10–16:30, 80 min)

> **Arc:** Second half. Take what you have and make it real. Same pair structure. Same 15-min driver swaps. Same R.V.P.I. The big V question this time: *"Is the CLAUDE.md your Lab 1 created still current?"*

---

## Slide 37: Section — Lab 2 | 15:10 | 30 sec

**[CLICK]**

**[ENERGY — post-break, start interactive]**

- **[ASK]** "What worked well in Lab 1? What surprised you?" Take 2–3 answers. Ground this session in their experience.
- "Same tracks. Same pair structure. Same R.V.P.I. Eighty minutes."

---

## Slide 38: Lab 2 Briefing | 15:11 | 4 min

**[CLICK]**

**[TIMER: 80 min — Lab 2 runs 15:10 to 16:30]**

- Walk the three track cards:
  - **Data Engineering** — FSANZ food recalls source, data quality expectations, cross-source gold view, cron scheduling. `LAB-2-DE.md`.
  - **Data Science** — train forecasting model, register in MLflow, Model Serving endpoint, prediction web app. `LAB-2-DS.md`.
  - **Analyst** — FastAPI + Tailwind app, embedded AI/BI dashboards, NL query feature, deploy to Databricks Apps. `LAB-2-ANALYST.md`.

**[LAND the two callout cards — the most important thing on this slide:]**

- **R.V.P.I. reminder:** *"Re-read the CLAUDE.md your Lab 1 created. Is it still correct? Fix drift before you build on it."* This is the V step, literal.
- **Get as far as you can** — checkpoints at every phase. 80 min is not long.

**[LAND THE SYNTHESIS]** "If you feel yourself writing a mega-prompt, pause. What would Research, Validate, Plan, Implement look like for this exact task?"

**Transition:** "Go."

---

## Lab 2 Facilitator Rhythm | 15:15 | 80 min

**[WALK the room every 10–15 min:]**

- **15:15 (start)** On mic: "Timers on. Fifteen-minute swaps. Navigator actively reading. Commit every 15."
- **15:30 (15 min)** Walk. "Core build underway? Any blockers? **Did you re-read your CLAUDE.md before starting Lab 2?**"
- **15:35 (~20 min)** **[DEMO SIDEBAR — Small-Steps Save, 90 sec, PRE-RECORDED]** See `starter-kit/demos/small-steps-save.md`. Play the video — big-bang prompt hanging vs small-step prompts succeeding. Intro: *"Halfway through Lab 2 — this is the moment I'd warn my past self about."* Pre-recorded, not live.
- **15:50 (40 min)** Walk. "Halfway. How's the integration going? Any Genie / dashboard / serving decisions needed?"
- **15:55 (~45 min)** **[DEMO SIDEBAR — Commit Cadence, 60 sec, LIVE]** See `starter-kit/demos/commit-cadence.md`. Quick live demo: run a test green, then `/commit` — skill generates the message. Message: *"Green test → /commit. Every time. Don't lose work."*
- **16:10 (60 min)** "Twenty minutes of building left. Wrap up current work."
- **16:20 (70 min)** "Ten minutes. Stop starting new work — polish what you have and prep your demo."
- **16:25 (75 min)** "Stop building! Last 5 min on your demo pitch."
- **16:30 (80 min)** "Close editors. Demos start now."

**[Common issues:]**

- htmx not loading → check script tag in HTML head.
- CORS errors → add `CORSMiddleware` to FastAPI.
- Can't create Genie space → check permissions, help navigate UI.
- Running out of time → "Working deliverable > perfect deliverable. Grab a checkpoint."
- MLflow registry errors → confirm experiment path is absolute.

---

# BLOCK 9 — Team Demos + Close (16:30–17:00)

> **Arc:** Three minutes per pair. Not a pitch — screen, code, result, **one thing that surprised you** (positive or negative). Vote. Then the emotional beat: Let Go of the Code. Then practical takeaways. Then hackathon + close.

---

## Slide 39: Team Demos and Voting | 16:30 | 20 min

**[CLICK]**

**[ENERGY]** "Demo time. Three minutes per pair. Not a pitch — screen, code, result, one thing that surprised you."

- Set visible timer. Strict three minutes.
- Four voting criteria on screen: Pipeline Quality · App Polish · Genie & AI/BI · Creativity.
- Quick applause after each. Note creative / clever moments.

**[After all demos — voting:]**

- Can't vote for own pair.
- Show of hands or paper vote. Tally. Announce winner.

**[Two-minute retro — take 2–3 answers:]**

- **[ASK]** "Most valuable technique you learned today?"
- **[ASK]** "What will you take back to work on Monday?"

**Transition:** "One slide I need you to land before the practical stuff."

---

## Slide 40: Let Go of the Code | 16:50 | 2 min

**[CLICK]**

**[IMPACT SLIDE — walk it slowly, don't rush]**

- Open with past workshop feedback (reading off slide): *"We want to see the code."*
- "That's production-identity talking. The belief that typing the artifact **is** the work. **You still read the code. You still judge it.** But you don't have to type every line to own it."
- Read Karpathy's line off the slide: *"Fully give in to the vibes, embrace exponentials, forget the code exists."* "He meant more than he thought."
- "The agent writes the code. Your work is what you **ask for**, what you **refuse**, what you make **prove itself**, and **what you still take the time to read**."
- **[PEPPER]** Eric's line: *"Forget the code exists. Do not forget the product exists."*
- **[LAND, drop the mic]** "When production is cheap, **judgement** is what's left of you. That's the real skill today was about."

**Transition:** "Now — practical. What to take home."

---

## Slide 41: Key Takeaways | 16:52 | 3 min

**[CLICK]**

- **1. Name the Loop: R.V.P.I.** — Research, Validate, Plan, Implement. The single most portable thing from today. One prompt = one R.V.P.I. in miniature. **Validate before you plan.**
- **2. CLAUDE.md is an Artifact That Rots.** — Right yesterday, wrong today. Re-read at the start of every session. Cheapest V step.
- **3. Small Steps Every Time.** — If you can't say whether a prompt worked in 1–3 minutes, it's too big. Split it.
- **4. Verification is the New Bottleneck.** — You own that, no one else does. The career skill of this decade.

**[ASK]** "Which resonated most?"

**Transition:** "Concrete next steps."

---

## Slide 42: Next Steps | 16:55 | 2 min

**[CLICK]**

- **This week:** share learnings with your wider team, set up a team CLAUDE.md with your standards, try it on one real task — start small.
- **Coming soon:** broader team rollout, shared skill libraries for common Coles patterns, Genie spaces on your real production data.
- **Champions:** Farbod and Swee Hoe (internal), david.okeeffe@databricks.com (Databricks SA — available for follow-up).
- **Measure success:** developer velocity, code quality, developer satisfaction.

---

## Slide 43: APJ Hackathon | 16:57 | 2 min

**[CLICK]**

- "One concrete thing. APJ's biggest hackathon. **Building Intelligent Apps.**"
- Key dates: registration open now, build 1–22 May 2026, winners 17 June.
- Prizes: $700 USD credits to get started, up to **$68K USD in total prizes**. Certificates for all who submit.
- Same tech stack: Genie, Lakebase, Agent Bricks, Apps.
- "Build on what you shipped today. Link on screen — email going out tomorrow with the details."

---

## Slide 44: Closing | 16:59 | 90 sec

**[CLICK]**

**[PAUSE — let the slide land]**

- "The best teams will be those who can effectively direct AI agents — **together**."

**[Make eye contact]**

- Thank the room — time, energy, willingness to experiment.
- Congrats to winning pair [winner].
- "You built production-shape platforms in six hours. Imagine what your team does with a full week."
- Email on screen. Here for follow-up.
- Questions?

*[If none:]* "Go build something great on Monday."

**[END — 17:00]**

---

*--- BUFFER / Q&A: absorbs into close if running under ---*

- Open floor for questions, 1:1 follow-ups, debugging help.
- If no questions, let pairs continue polishing or exploring.
- Pack up by 17:15.

---

# Appendix Slides (if time permits or questions arise)

> **Note:** The Appendix now includes Slide 53 (Rosetta Stone) — moved from the opener so it didn't slow the morning's momentum. Useful if cross-platform attendees ask about mapping Claude Code concepts to other tools during labs.

---

## Slide 45: Appendix Divider

**[CLICK]** "Reference material — available if time allows or questions arise."

---

## Slide 46: Subagents, Skills, Hooks & Plugins

**[CLICK]** ~5 min if opened.

- **Subagents** — parallel workers, isolated context. Build frontend while you do backend. `/review` spawns one for fresh-context judgment.
- **Skills** — slash commands encoding domain knowledge. `/commit`, `/review`, custom `/deploy-pipeline`.
- **Hooks** — event-driven guardrails. PostToolUse auto-formats Python with ruff on every save, Stop runs verify-hint.sh. **Deterministic, not AI.** V automated.
- **Plugins** — package skills + agents + hooks for your team. Distributable, versioned.

---

## Slide 47: Skills for BDD

**[CLICK]** BDD skill chain.

- `/bdd-scaffold` — initialises Behave project structure wired to Databricks SDK.
- `/bdd-features` — generates feature files from requirements (Gherkin).
- `/bdd-steps` — implements step definitions for existing feature files.
- `/bdd-run` — executes Behave test suites with tag filtering / parallel / CI reporting.
- **Key:** chain generates tests from success criteria, not from code — define "done" before implementation.

---

## Slide 48: Subagents vs Agent Teams

**[CLICK]** Distinction matters for the DE / DS tracks.

- **Subagents = fire-and-forget** — isolated context, one job, result returns to parent. Can't talk to each other — that's a feature. Key benefit: **compression** — vast exploration distilled to clean signal.
- **Agent Teams = ongoing coordination** — long-running, peer-to-peer messaging, shared task list with `blockedBy`. Key benefit: **negotiation** — discovery in one thread changes another.
- **Design principle:** start with one agent. Push it until it breaks. That tells you what to add.
- **Warning:** parallel agents writing code make incompatible assumptions — subagents should explore, not write code simultaneously.

---

## Slide 49: What Is MCP

**[CLICK]** MCP = "USB-C of AI agents."

- Before: every agent hand-wires integrations to every tool. Combinatorial complexity.
- After: one protocol, every tool connects. Claude Code talks to UC / Genie / GitHub / Slack / custom servers through the same mechanism.

---

## Slide 50: How MCP Works

**[CLICK]** Client-server architecture.

- Client = your Claude Code session.
- Server = UC / Genie / custom Databricks App / third-party service.
- MCP + Skills + Agent compose: skill knows when to call the server; agent knows how to act on the response.

---

## Slide 51: MCP Architecture on Databricks

**[CLICK]** Full architecture.

- Left: Databricks-served agents connect to custom / managed / third-party MCP servers.
- Right: external agents (like your Claude Code today) connect to the same servers.
- Bottom: AI Gateway routes to model serving.
- "Coles sits on the right today — external agent connecting via MCP, same security and governance."

---

## Slide 52: AI Dev Kit

**[CLICK]** What enables all of this.

- **Skills:** 25+ skill packs (pipelines, dashboards, UC, Genie, MLflow) — knowledge layer.
- **MCP Server:** 50+ tools (SQL, clusters, jobs, apps) — action layer.
- **Tools Core:** Python library underneath — extend with your own.
- **Builder App:** web chat UI — what you've been using today (CODA).
- **For Coles:** fork this repo, add custom skills — `/run-data-quality`, `/deploy-pipeline`, `/check-lineage`.

---

## Slide 53: Rosetta Stone

**[CLICK]** Cross-platform reference — use if attendees ask during labs.

- Claude Code concepts mapped to Cursor, Cline, GitHub Copilot, Windsurf.
- **Key line:** *"You don't need to throw away what you know. You need to find the one-line mapping."*
- CLAUDE.md → `.cursorrules` / `.clinerules` / Copilot workspace. Skills → Cursor Composer agents. Hooks → Cursor rules / Cline auto-approval. MCP → same across all (open standard).

---

# Emergency Playbook

| Situation | Response |
|-----------|----------|
| **WiFi goes down** | Switch to phone hotspot for demos. Pairs can work offline on tests/code, reconnect later. |
| **CODA instance crashes** | Restart the app. If persistent, pair affected person with another pair — make a temporary triad. |
| **Live demo fails (Slide 7 or 8)** | "Live demos — always an adventure." Play the backup recording from your laptop. Do NOT try to fix live. |
| **Quiz-app fails during Block 3** | Fallback to a verbal 3-question prediction round (NSW turnover, CPI food %, fastest-rising category). Revisit at Show & Tell using Gold tables. |
| **Pipeline demo deploy takes >90 sec** | Skip the dashboard flip. Move on to Today's Challenge. See `starter-kit/demos/pipeline-and-dashboard-demo.md`. |
| **Pair falls way behind in Lab** | Walk them to a checkpoint. "Grab the checkpoint, get your tables loaded, focus on the next phase." |
| **Driver dominates, navigator passive** | "Navigator, tell me what Claude just did. Out loud." Force the V step manually. |
| **Post-lunch energy crash (Block 5)** | Start with the interactive question. Stand up, walk around. Move quickly to pair formation to get hands back on keyboards. |
| **Running over time** | Compress Block 4's Slide 30 demo to 60 sec (skip live terminal). Cut Lab 2 to 70 min. Keep team demos to 2.5 min each. |
| **Running under time** | Extend Lab 2 if pairs want it. Open appendix slides (46–53) for Q&A. Let pairs polish and demo extras. |
| **R.V.P.I. isn't landing** | At next checkpoint, stop the room and ask ONE pair to narrate their last task as R → V → P → I. Concrete beats abstract. |

---

*[TODO: confirm final quiz-app URL and QR code once deployed. Currently placeholder `quiz.coles-vibe.app` on Slide 9.]*

*[TODO: confirm managed-Iceberg stretch-goal instructions land in `LAB-2-DE.md` appendix — referenced on Slide 31.]*
