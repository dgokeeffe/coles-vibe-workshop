# Workshop Transcript — Vibe Coding @ Coda

> **Format:** Hybrid — 1st-person prose for each block's arc, then terse slide-level cues.
> **Timing:** 10:00–17:00, lunch at 12:00 (6 contact hours).
> **Slides:** ~48 (down from 53). New/edited/cut deltas marked in each block.
> **Voice:** This reads like David talking on the day. When you see **[DEMO]**, the screen shifts from slide to terminal/app.

---

## Block 1 — Opener (10:00–10:10)

### Prose arc

"Good morning. Before I introduce myself or this workshop, a quick frame on where the industry is right now.

The pitch you're about to hear isn't "AI will make you 30% faster." It's different. The bottleneck in software is no longer typing. Every senior engineer I talk to — at Databricks, at Anthropic, in the Pragmatic Engineer surveys — says the same thing: **the new scarce resource is verification and coordination, not code generation.** The people who win are the ones who learn how to direct an agent, not race it.

Today you won't just write code with Claude. You'll ship a Grocery Intelligence Platform — pipeline, dashboard, app — in six hours. Three tracks. You pick one after lunch. Here's what you'll walk out with." **[Show teaser: Gold tables, AI/BI dashboard, FastAPI app with Genie embed.]** "One team last quarter built something I'd have budgeted six weeks for. I want that for you today."

### Slide cues

- **Slide 1 (Title — EDIT)**: Update time to 10:00. Add compact agenda strip: Opener · Demo · Teach · Lab 1 · Lab 2 · Close. Remove standalone agenda slide.
- **Slide 2 (The AI Coding Moment — EDIT)**: Lead with ONE stat — Pragmatic Engineer's "verification is the bottleneck." Drop 3-of-5 stat cards to appendix. 90-second slide, not 3-4 min.
- **Slide 3 — End-Output Teaser**: 3-pane screenshot mosaic: pipeline graph (DE), UC model card + predictions chart (DS), Genie dashboard + FastAPI app with Genie embed (Analyst). One-liner: *"Six hours from now."*

---

## Block 2 — Internal Demo (10:10–10:25)

### Prose arc

"Before I teach you anything, I want to show you me working. Not a slide. An actual terminal. Because if I tell you vibe coding works and then show you a polished deck, you won't believe me — and you shouldn't. **[Open terminal.]** This is my Claude Code setup. Let me show you what I've been using it for the last month. **[Quick tour: git log, skills directory, CLAUDE.md, a couple of recent PRs.]** I'll open one file and walk Claude through it — watch what I *ask*, and more importantly, watch what I *verify* after the answer comes back."

**[Live mini-demo: 60–90 sec. Open one silver-layer file (e.g., `reference-implementation/src/silver/retail_turnover.py`). Ask Claude *"explain what this does and why"* — narrate Validate out loud (*"that matches my memory, but let me open the file too..."*). Then one tiny Implement: *"add a docstring capturing that summary."* Shows Read + Validate + minimal Implement.]**

"That was tiny. Now let me show you the full loop Claude Code does when I'm building the kind of thing you're going to build today. **[Flip to browser — reference-implementation app.]** This app has been running for three weeks. KPI cards, monthly trend, recalls table, and — *here* — a natural-language query box. Watch."

**[Type into NL box: *"which Australian state had the highest retail turnover last month?"* — app returns NSW. Pause.]**

"That works because `gold_retail_summary` has state-level turnover. But I want something richer — each state's *share* of national retail. Percentages, not just totals. I won't touch the app. I'll add one column to the gold table — BDD style — and then come back and ask the same app again."

**[Execute the 8-beat demo from `starter-kit/demos/pipeline-and-dashboard-demo.md`. Four prompts: write test → run red → implement window function → deploy. Then flip back to the app and ask: *"what percentage of national retail does each state account for this month?"* → app generates SQL against the fresh column, returns NSW ~35%, VIC ~26%, QLD ~20%.]**

"Two things I want you to notice before we go on. First: I didn't write most of that code, and I didn't touch the app at all. I shipped one column and the app — which has no idea what my gold schema looks like — answered a question it couldn't answer five minutes ago. Second: every step had a way for me to verify it worked — tests, schema contracts, a natural-language round trip. No verification, no trust. We'll return to that idea all day."

### Slide cues

- **Slide 5 (Coding Agents at Databricks)**: High-level frame: "What we use Claude Code for internally." 3-4 bullet categories (PR review, refactors, test generation, compliance gates). 30-second slide.
- **Slide 6 (Stack You'll Touch Today)**: 2-min walk through what pairs will use today — call out MCP + Proprietary Model Serving as how Claude Code talks to the platform.
- **Slide 7 (Watch First)**: Terminal mini-demo (60–90 sec). One file, read + validate + minimal edit. Do not name R.V.P.I. yet.
- **Slide 8 (Live Demo — Pipeline + App)**: 4–5 min, 8 beats. Pre-deployed reference-implementation app + pipeline on `david_demo` schema, no `state_turnover_pct` column yet. Full script in `starter-kit/demos/pipeline-and-dashboard-demo.md`.

---

## Block 3 — Icebreaker: Live Quiz-App (10:25–10:40)

### Prose arc

"Enough of me talking. It's your turn to do something. **[Project quiz-app URL + QR code.]** Open this on your phone. Enter your name — *your* name, not a team name; you'll pair up for lab work after lunch, but this is individual. You've got 60 seconds. We're going to play a live grocery-data quiz — Australian retail, CPI food, behaviour patterns. It scores in real time. Winner gets a small prize at lunch.

**[Run quiz — 8–10 min of live play. Three icebreaker profile questions at join (persona, stack, Databricks familiarity) auto-aggregate into an audience breakdown on the facilitator screen. Then grocery-domain questions — the prediction ones will be revealed from Lab 1 Gold tables later.]**

"Three things to know before we go on. One: the app you just played with was built in one weekend by me and Claude Code. Start to deploy. Two: some of those questions — household spend, which state buys the most meat — those are the same questions your Lab 1 Gold tables will answer. We're coming back to your answers at Show & Tell to see who guessed closest. Three: this is the smallest example of what you'll ship today. By 5 PM you'll have shipped something bigger."

### Slide cues

- **Slide 9 (Quiz-App Icebreaker)**: Large QR code + short URL + "enter your name" hint. Per-player, not per-team. Minimal text — the app is the visual. "Play now. Prizes at lunch."

---

## Break (10:40–10:50)

---

## Block 4 — Get-to-Know-Claude (10:50–12:00)

> **This is the pressure block: 70 minutes, ~18 slides, guided demo style.** Drive from the terminal, slides are backdrop. Name **R.V.P.I.** early and return to it at every sub-section boundary.

### Prose arc

"Everything I'm about to teach fits inside one loop. Let me name it first, then we'll walk through it. **R.V.P.I. — Research, Validate, Plan, Implement.** Most people who've worked with AI agents have heard of R.P.I. — research, plan, implement. The missing letter is V. Before you plan on top of the research, you *audit* the research. Is it current? Is it consistent? Is it trustworthy? Because memory drifts. CLAUDE.md files rot. An agent's summary from yesterday can quietly contradict today's reality, and the agent will plan on top of that contradiction without flagging it.

But V doesn't stop there. It's not a gate you walk through once and you're done — it's a recurring habit. V appears at every transition: after Research (audit context before planning), after Plan (validate the plan before you write a single line of code — does this plan actually solve the problem?), and after every Implement step (did that step actually work?). Three checkpoints per loop. Your job — and the single biggest difference between a junior prompter and an experienced one — is to validate at every one of them.

Everything else I'm going to show you is a specialisation of one of these four phases. CLAUDE.md is the artifact Validate audits. Small Steps is how Implement stays honest — and forces V #3 after every step. Skills, MCP, and hooks are tools that automate V. BDD is verification *inside* Implement. Sycophancy is what happens when you skip V. Context windows are the reason V matters more over time. Keep the loop in your head; I'll call it back as we go."

**[Walk through each sub-section as a live demo. At each sub-section boundary, point back at the R.V.P.I. poster.]**

**Sub-section order (suggested timing):**
1. R.V.P.I. intro — name the loop, show the four-quadrant diagram (5 min)
2. CLAUDE.md scopes — Validate's artifact (10 min, includes Rule #1 hands-on)
3. Small Steps — Implement stays honest (10 min)
4. Power tools: Skills, MCPs, hooks, subagents — automating V (15 min, live demos)
5. BDD — verification inside Implement (15 min)
6. Sycophancy + memory-as-untrusted-input — what skipping V costs (10 min)
7. Context windows + tokens — why V's value compounds (5 min)

### Slide cues

- **Slide NEW — R.V.P.I. Framework Intro**: Four-phase horizontal diagram. Call out that V is a recurring habit at every transition — V #1 after R (audit context), V #2 after P (validate plan before coding), V #3 after each I step (verify it worked). The cheapest V is after R, but all three matter.
- **Slide NEW — R.V.P.I. In The Terminal**: Table with three explicit "Validate" checkpoints: V #1 (confirm/correct before planning), V #2 (validate plan before coding), V #3 (validate each step worked). Walk all three — don't skip V #2 and V #3.
- **Slide 10 (Section divider — RENAME)**: "Techniques" or "Directing Claude" — not "Specs & Testing" (too narrow for R.V.P.I. framing).
- **Slide 11 (Why Specs Matter — KEEP)**: No edit.
- **Slide 12 (CLAUDE.md Example — KEEP)**: Add R.V.P.I. callout: *"This is what Validate audits."*
- **Slide 13 (CLAUDE.md Scope Levels — KEEP)**: No edit. High-value slide.
- **Slide 14 (Rule #1 Hands-On Exercise — EDIT)**: Compress from 20 min to 10–12 min. Pair-friendly version: "Driver asks Claude for a CLAUDE.md about your role. Navigator reviews what it produces. Switch after 5 min."
- **Slide 21 (Small Steps — EDIT)**: Add R.V.P.I. crossover box: *"Small Steps is how Implement stays honest. Each prompt = one Research-Validate-Plan-Implement loop in miniature."*
- **Slide 18 (Power Tools — KEEP)**: No edit.
- **Slide 30 (Skills and Tools — KEEP, REPOSITION)**: Move into this block from current position 30.
- **Slide 31 (MCP on Databricks — KEEP, REPOSITION)**: Move into this block.
- **Slide 32 (Databricks Internal Claude Setup — REPOSITION)**: Bring forward into this block; becomes the "show-me tools-that-automate-V" demo. Currently at position 32.
- **Slide 15 (BDD Workflow — KEEP)**: No edit.
- **Slide 16 (Why BDD Works — KEEP)**: No edit.
- **Slide 17 (Writing Gherkin — KEEP)**: No edit.
- **Slide 19 (Anthropic Best Practices — KEEP)**: High-value. No edit.
- **Slide 20 (Sycophancy Problem — EDIT)**: Extend reproducibility card to cover *context poisoning* — agent agreeing with itself from a past session when the past session was wrong. One-line callback to V.
- **Slide NEW — Memory As Untrusted Input**: One-slide security framing from `notes/rvpi-validate-step.md` line 113–115. *"Retrieved memory should be treated as untrusted input, the same way external API responses are."* Engineering-intuition reframe.
- **Slide NEW — Where Databricks Absorbs V** (inserted as Slide 24, between Memory-As-Untrusted and Small Steps): The relief slide. Narrows the V surface. Two cards — platform-absorbed (UC, Lakeflow `@dp.expect`, Serverless SDP, bundle validate, Genie semantic layer, Model Serving, Lakebase, bundle targets) vs. residual (CLAUDE.md claims, past-session memory, cross-source consistency, intent correctness). Decision rule at the bottom: *"Before building a custom validator, check if the platform already does it deterministically."* The tools-automate-V vs. platforms-absorb-V contrast is the punchline. Source: see `notes/rvpi-validate-step.md` §"Where Platforms Absorb V".
- **Slide 22 (What Are Tokens — KEEP)**: No edit.
- **Slide 23 (Managing Context Windows — EDIT)**: Add one line: *"V prevents drift. Drift is why context management matters."*

---

## Lunch (12:00–13:00)

---

## Block 5 — Challenge Brief + Pair Formation (13:00–13:15)

### Prose arc

"Welcome back. You've eaten. You've been thinking about what you want to build. Here's the challenge. **[Slide 26.]** Grocery Intelligence Platform. Three data sources already in the bronze layer: Australian retail trade, CPI food, FSANZ recalls. Three tracks — pick one. Data Engineering builds the pipeline and dashboard. Data Science builds a forecasting model, registers it in Unity Catalog, and scores predictions in a notebook (optional stretch: batch inference via Lakeflow). Analyst builds Genie spaces and a FastAPI app that embeds them.

One change from how you might expect a hackathon to work: you're going to pair. Two people per keyboard. Fifteen-minute driver swaps. Navigator's job is to read, verify, suggest — not to sit passively. If you're odd-numbered, one triad forms with an observer who takes notes on what's surprising. **[Show pair-programming norms slide.]** Why pairs: shipping with AI is a verification problem, and verification is cheaper with a second pair of eyes. Solo is slower, not faster — you'll skip V steps you wouldn't skip with a navigator watching. Trust me on this, or prove me wrong by 5 PM.

Find your pair now. Choose your track. Open the lab guide matching your track. Go."

### Slide cues

- **Slide 26 (Today's Challenge — KEEP, REPOSITION)**: Move from current position 26 to here. Solid as-is.
- **Slide NEW — Pair Programming Norms**: 15-min driver swaps. Navigator duties: read, verify, steer. One-line escalation rule: *"If a task doesn't fit R.V.P.I. in 15 min, split it."*
- **Slide 36 (Lab 1 Briefing — EDIT)**: Update for pairs (not 2–3 teams). Track-specific lab file pointers. Merge in *Slide 33 (Iceberg)* and *Slide 34 (Genie)* as track-specific callouts here rather than separate slides.

---

## Block 6 — Lab 1 (13:15–14:45, 90 min)

### Prose arc

"Heads down. You're on your own — well, in your pair. I'll circulate. When you see me, expect one question: *have you validated your CLAUDE.md yet?* That's the whole game. Checkpoint at 30 min and 60 min — I'll call them on the mic. First checkpoint: you should have a test passing. Second: you should have one Gold table or equivalent. If you're not there, raise your hand."

*(Mostly silent for the facilitator. Slide is a section divider only.)*

### Slide cues

- **Slide 35 (Lab 1 Section Divider — KEEP)**: No edit.
- **Slide 27 (Lab 0 Section Divider — CUT)**: Lab 0 dissolves into Lab 1's opening phase given pair structure.
- **Slide 28 (Practical Tips — MERGE)**: Roll 5 practical patterns into Lab 1 Briefing as a sidebar, not a separate slide.
- **Slide 29 (Section: Capabilities for Your Track — CUT)**: Dissolved into Lab 1 Briefing.

---

## Block 7 — Show & Tell + Quiz-App Reveal (14:45–15:00)

### Prose arc

"Pencils down. We're going to do two things in fifteen minutes. First — one highlight per track. Not a full demo; just one thing you're proud of. Thirty seconds each. Second — we're going back to the quiz-app. Some of the questions you answered this morning map to Gold tables teams just built. **[Pull up quiz-app admin view.]** Let's reveal the actual numbers from your pipelines and see who was closest. Prize at the end."

### Slide cues

- **Slide 37 (Show and Tell — EDIT)**: Remove prediction-cards logic. Replace with: *"Quiz-app live reveal using Lab 1 Gold tables."* Keep the track-highlight-demo structure.

---

## Break (15:00–15:10)

---

## Block 8 — Lab 2 (15:10–16:30, 80 min)

### Prose arc

"Second half. Lab 2 builds on Lab 1 — you're taking what you have and making it real. DE track: data quality, scheduling, FSANZ ingest. DS track: train a forecaster, register it in Unity Catalog with a `@champion` alias, score a sample in a notebook (stretch goal for fast pairs: wire it into Lakeflow as a batch job using `mlflow.spark_udf`). Analyst track: FastAPI app with embedded Genie. Same pair structure. Same 15-min driver swaps. Same checkpoints. Same R.V.P.I. If you feel yourself writing a mega-prompt, pause — what would Research, Validate, Plan, Implement look like for this exact task?"

### Slide cues

- **Slide 38 (Lab 2 Section Divider — KEEP)**: No edit.
- **Slide 39 (Lab 2 Briefing — EDIT)**: Update for pairs. Include one R.V.P.I. reminder card: *"Before you start, re-read your CLAUDE.md. Is it still current?"*

---

## Block 9 — Team Demos + Close (16:30–17:00)

### Prose arc

"You have three minutes to show what you built. Not a pitch. Screen, code, result. One thing that surprised you — positively or negatively. Go." **[20 min of demos + voting.]**

"Before we close — one slide I want to land. **[Slide 41: Let Go of the Code.]** The most experienced engineers I work with who use Claude Code best have one thing in common: they care about the *system* more than they care about the *code*. They let the agent write the code and they focus on whether the system does what it should. Production identity lives at the interface, not the implementation. That's a skill. It takes practice. Today was practice. Monday morning is where the real practice starts.

**[Takeaways slide.]** Four things I want you to leave with. One: R.V.P.I. — name the loop, use it. Two: CLAUDE.md is an artifact that rots; validate it. Three: Small Steps every time. Four: verification is the new bottleneck — you own that, no one else does.

**[Next Steps + APJ Hackathon slides.]** Concrete actions. There's a hackathon in May — build on what you shipped today and win $68K in prizes. Details in the email tomorrow. Thanks for the day. Go build something."

### Slide cues

- **Slide 40 (Team Demos + Voting — KEEP)**: No edit.
- **Slide 41 (Let Go of the Code — KEEP)**: High-value emotional beat. No edit.
- **Slide 42 (Key Takeaways — EDIT)**: Swap one takeaway for R.V.P.I. reinforcement.
- **Slide 43 (Next Steps — KEEP)**: No edit.
- **Slide 44 (APJ Hackathon — KEEP)**: No edit.
- **Slide 45 (Closing — KEEP)**: No edit.

---

## Appendix (Reference — Unchanged)

Slides 46–53 stay as-is. Add Slide 7 (Rosetta Stone) here — it's useful cross-platform reference material but slowed the opener's momentum.

- **Slide 46 (Appendix Divider — KEEP)**
- **Slide 47 (Subagents, Skills, Hooks, Plugins — KEEP)**
- **Slide 48 (Skills for BDD — KEEP)**
- **Slide 49 (Subagents vs Agent Teams — KEEP)**
- **Slide 50 (What Is MCP — KEEP)**
- **Slide 51 (How MCP Works — KEEP)**
- **Slide 52 (MCP Architecture on Databricks — KEEP)**
- **Slide 53 (AI Dev Kit — KEEP)**
- **Slide 7 (Rosetta Stone — MOVE FROM OPENER TO APPENDIX)**

---

## Meta: Callbacks & Through-Lines

Three ideas need to land repeatedly, not just once, for the day to cohere:

1. **R.V.P.I.** — introduced in Block 4, referenced in Slide 20 (Sycophancy), Slide 21 (Small Steps), Slide 23 (Context Windows), Block 5 (pair norms), Block 6 checkpoints, Block 9 takeaways. Every lab checkpoint question goes through it.

2. **"The agent is your domain tutor, not your typist"** — introduced in Block 1, reinforced in Block 2 (internal demo), reinforced in Block 9 ("let go of the code"). This is the workshop's emotional through-line.

3. **"Verification is the new bottleneck"** — stat in Block 1, demonstrated in Block 2, taught in Block 4, lived in Labs, restated in Block 9.

---

## Delta Summary

| Category | Count | Notes |
|----------|-------|-------|
| Slides KEPT as-is | ~26 | Core teaching content unchanged |
| Slides EDITED (in place) | ~10 | R.V.P.I. cross-refs, pair structure, timing |
| Slides REPOSITIONED (moved, unchanged) | ~5 | Demos earlier, track-callouts folded into briefings |
| Slides CUT / MERGED | ~6 | Agenda, predictions, Lab 0 divider, capabilities divider, practical tips, live-demo preview |
| Slides NEW | ~8 | End-output teaser, coding-agents-at-Databricks, quiz-app, R.V.P.I. intro, R.V.P.I. in terminal, memory-as-untrusted-input, pair programming norms, (optional) facilitator R.V.P.I. checkpoint card |
| **Final count** | **~48** | Down from 53, tighter narrative |

---

## What's Next (After Transcript Approval)

1. Read this end-to-end. Mark anywhere the voice or story doesn't match how you'd actually deliver.
2. Flag any slide I've classified as CUT that you want to keep, or KEEP that you want to drop.
3. Decide whether Block 4's 70 minutes is realistic or needs to compress (Block 4 is the pressure point — if it over-runs, Lab 1 starts late).
4. Once approved: I start Phase B (rewrite `slides.html` against this transcript). That's a single large session. No slide edits happen until you sign off here.
