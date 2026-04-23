# Runbook: Live Bronze Build (Block 4, 10:55–12:00)

**When:** 10:55 AM, immediately after the Challenge Brief (10:50–10:55).
**Duration:** 65 minutes continuous.
**Style:** Live build in Coda against a real Databricks workspace. Slides are backdrop; the terminal and Coda pane are the show.
**Purpose:** Teach R.V.P.I., CLAUDE.md, Small Steps, Power Tools, BDD, Sycophancy, Context — *not* as separate demos, but as annotations on a single bronze-layer build. By 12:00, there is one working bronze table in the workspace plus a second half-started, and attendees have seen every theory concept applied to the challenge they're about to build.

---

## Why this structure

The old Block 4 taught theory first, then labs applied it. Two problems: (1) concepts landed abstractly; (2) 90-min labs started from zero momentum. This runbook inverts that. Every concept gets a concrete moment in a build attendees are about to do themselves. By lunch, the shape of the afternoon is already proven — *"you watched me do this in 65 min. Your pair has 90."*

The anchor claim: **tools automate V; platforms absorb V; you own the semantic V.** The runbook is designed to make attendees *see* each half of that claim, not just hear it.

---

## End state at 12:00

- `workshop_vibe_coding.david_demo.bronze_abs_retail_trade` — fully populated (14+ columns, most recent 12 months).
- `workshop_vibe_coding.david_demo.bronze_abs_cpi_food` — scaffolded, schema defined, one `@dp.expect` added, **deliberately left failing or incomplete** so Lab 1 pairs have something to finish.
- A `CLAUDE.md` in the working repo that was authored live at 10:55–11:05, audited at 11:50 (the sycophancy beat), corrected, and committed.
- A `features/bronze_retail_trade.feature` Gherkin file with 3 scenarios, implemented by Claude with step defs.
- A `.claude/settings.local.json` with the audit-log hook active.

---

## Pre-flight checklist

Same discipline as `pipeline-and-dashboard-demo.md` — the demo timing reality memory says pipelines take 35 min not 5, so nothing is built cold on the day.

### Day-before checklist

- [ ] Create a fresh git branch from `main` called `facilitator/block-4-live-build`. **All live-build work commits to this branch in front of the room.**
- [ ] Clean state: branch has an empty `src/bronze/` directory, no tests, no features. Just `databricks.yml`, `pyproject.toml`, and the starter-kit's `CLAUDE.md` template.
- [ ] **Pre-stage ONE false claim in `CLAUDE.md`** for the sycophancy beat. Suggested plant: under "Data Sources" table, state the ABS Retail Trade CSV has **8 columns** when the actual endpoint returns **14**. This is the claim Claude will build on until validated at 11:50. (Alternatives: wrong column name like `state_code` instead of `region_id`; wrong update cadence like "daily" instead of "monthly". Pick one, document which, stick to it.)
- [ ] `workshop_vibe_coding.david_demo` schema is empty of bronze tables (drop any leftovers from prior rehearsals).
- [ ] Confirm the ABS Retail Trade API endpoint is returning data — `curl "https://data.api.abs.gov.au/data/ABS,RT,1.0.0/..."` should succeed. If ABS is down, fall back to the cached CSV in `reference-implementation/data/abs_retail_trade_cached.csv`.
- [ ] Warm a serverless SDP pipeline — trigger one test run against an unrelated table so first-deploy latency is paid.
- [ ] Confirm the `databricks-docs` MCP is available in the Coda Claude Code session (`/mcp` should list it).
- [ ] Rehearse the full run in ≤50 min to leave headroom. Time the sycophancy beat specifically — it runs long in rehearsal.

### 30 minutes before

- [ ] Open Coda with the facilitator branch checked out, `src/bronze/` empty.
- [ ] Open a second Coda terminal running `tail -F /tmp/claude-audit.log` (for the hooks beat).
- [ ] Open the Databricks workspace pipeline UI for `grocery-intelligence-demo` (fallback).
- [ ] Open the R.V.P.I. slide on the projector (Slide 11). It's the backdrop for the opening 5 min.
- [ ] Touch `/tmp/claude-audit.log` so `tail -F` doesn't error.
- [ ] Restart Claude Code once — hooks from `.claude/settings.local.json` load at startup.

### Fallback scripts (on your laptop, not projected)

- [ ] `facilitator/block-4-fallback-bronze-complete` branch — a pre-built version of what we're trying to build. If live build derails, `git checkout`, `databricks bundle deploy`, keep teaching.
- [ ] Screen recording of a working rehearsal — last resort if Coda/workspace is fully down.

---

## The run — minute-by-minute

### 0:00 – 0:05 · R.V.P.I. Intro (Slide 11)

**On screen:** R.V.P.I. Framework slide. You are talking, not typing.

**Say:**

> "The next hour is a live build. You'll watch me build a bronze layer of the Grocery Intelligence Platform — the same shape your pair will build after lunch. I'm going to narrate every phase. Research → Validate → Plan → Implement. The V is the letter most people skip. By 12:00, there will be one working table in the workspace, one half-done, and you'll have seen eight things: R.V.P.I., CLAUDE.md, Small Steps, power tools, BDD, Sycophancy, how Databricks absorbs a lot of the V for free, and context management. Each of those happens *inside* the build, not as a separate demo."

**Transition:** Flip to Coda. Terminal open, `src/` empty.

---

### 0:05 – 0:15 · CLAUDE.md + Rule #1 (Slides 13–16)

**Concept focus:** CLAUDE.md is the artifact Validate audits. Rule #1: you don't hand-write it — you have a conversation.

**Paste into Claude (prompt 1):**

```
Generate a CLAUDE.md for this repo. Context: we're building the bronze layer of the Grocery Intelligence Platform. Data sources: ABS Retail Trade, ABS CPI Food. Stack: PySpark, Lakeflow Declarative Pipelines (`import databricks.declarative_pipelines as dp`), @dp.table + @dp.expect decorators. Catalog: workshop_vibe_coding, schema: david_demo.

Do not write any code yet. Just write CLAUDE.md.
```

**While it's generating, say:**

> "Notice I didn't hand-write this. I'm having a conversation. CLAUDE.md is markdown — it's config, not code. If you want to change how Claude behaves, you change this file. No restart, no deploy."

**When it's done:**

```
Now review it. What's missing? What might be wrong? Read it like a new teammate would.
```

**Pair exercise (5 min, 10:10–10:15):** *"Turn to the person next to you. Driver reads the CLAUDE.md aloud. Navigator points at one line they'd question. You have five minutes. Go."*

**After 5 min, seed the plant:** Open `CLAUDE.md` manually, add one line under Data Sources: *"ABS Retail Trade CSV has 8 columns."* (This is the pre-staged drift. It will surface at 0:55.)

**Transition:** *"CLAUDE.md is in place. Now let's start building — small steps."*

---

### 0:15 – 0:25 · Small Steps (Slide 25)

**Concept focus:** Each prompt is one verifiable step.

**Paste into Claude (prompt 2 — Research phase, intentionally narrow):**

```
Research only — do not write code. What does the ABS Retail Trade API return? Fetch a sample row (curl or requests), and tell me: what columns, what types, what the first 3 rows look like. One page of output.
```

**Narrate as Claude runs:**

> "That's R in R.V.P.I. Notice I said *research only, no code*. I want to see what I'm dealing with before I plan."

**Paste (prompt 3 — Validate):**

```
Before we plan the bronze table, validate the CLAUDE.md I wrote earlier. Does it match what you just saw from the API? Any discrepancies?
```

**Expected behaviour:** Claude may or may not catch the 8-vs-14 columns plant. *If it catches it now*, you get an early sycophancy-averted win — use it: *"that's V working. If we'd skipped this step, we'd plan on wrong column count."* Fix CLAUDE.md, continue. *If it misses it*, let it ride — you'll catch it at 0:55 when the sycophancy beat lands harder.

**Paste (prompt 4 — Plan):**

```
Plan only — do not implement. Design a single @dp.table function for bronze_abs_retail_trade. List: inputs, outputs (column list with types), one @dp.expect quality rule, one edge case to handle. Keep the plan to 10 lines.
```

**Paste (prompt 5 — Implement, one step):**

```
Implement step 1 only: write the `@dp.table` function skeleton. No tests yet. No quality rules yet. Just the decorator, signature, docstring, and a TODO where the body goes. 15 lines maximum.
```

**Say while it runs:**

> "Will I know after this prompt whether it worked? Yes — the file exists, the decorator's there, I can read it. That's the Small Steps heuristic. Compare to 'build the whole bronze layer' — I'd be sitting here for 15 minutes not knowing."

**Paste (prompt 6 — Implement, step 2):**

```
Now fill the body. Fetch the CSV from the ABS API, parse it into a Spark DataFrame, return it. Don't add quality rules — that's the next step. Don't handle errors beyond what dp.table gives us for free.
```

**Quick deploy-and-check:**

```bash
databricks bundle validate
databricks bundle deploy -t dev
databricks bundle run grocery-bronze-live -t dev --no-wait
```

**Say:** *"I'm not going to wait for the full run. The point is it validates. That's I in R.V.P.I. — implement and verify, small, visible."*

---

### 0:25 – 0:40 · Power Tools (Slides 20, 28, 29, 30)

**Concept focus:** Skills, MCPs, hooks, subagents — all V-automation.

#### Skills beat (3 min)

**Paste (prompt 7):**

```
Use the /bdd-features skill to draft a Gherkin feature file for bronze_abs_retail_trade. Three scenarios: the happy path, one missing column, one malformed row. Save to features/bronze_retail_trade.feature.
```

**Say:** *"Skills are just reusable prompts with rails. `/bdd-features` is in the marketplace. I didn't reinvent it."*

#### MCP beat (3 min)

**Paste (prompt 8):**

```
Use the databricks-docs MCP to confirm the exact syntax for `CREATE OR REFRESH STREAMING TABLE` and validate that our @dp.table decorator compiles to the correct SQL. I want to see the authoritative doc, not your recollection.
```

**Say:** *"This is V-automation. I'm not trusting Claude's memory of Databricks syntax — I'm going to the docs MCP. Ground truth lives there."*

#### Hooks beat (5 min)

**Add to `.claude/settings.local.json` live:**

```json
"hooks": {
  "PostToolUse": [{
    "matcher": "Edit|Write|MultiEdit",
    "hooks": [{
      "type": "command",
      "command": "echo \"[$(date '+%H:%M:%S')] $CLAUDE_TOOL_NAME -> $CLAUDE_FILE_PATHS\" >> /tmp/claude-audit.log"
    }]
  }]
}
```

Restart Claude Code. Flip to terminal 2 showing `tail -F /tmp/claude-audit.log`.

**Paste (prompt 9):**

```
Add a docstring to bronze_abs_retail_trade and to the feature file. One line each.
```

**[Point at terminal 2 — two lines scroll past.]**

> *"That's not Claude. That's my shell. The harness forced it to run. Swap `echo` for `ruff format`, you auto-format every edit. Swap for `pytest`, you test every edit. Hooks are deterministic V."*

#### Subagent beat (4 min)

**Paste (prompt 10):**

```
Launch an Explore subagent to scan reference-implementation/ and report: what patterns did the reference bronze layer use that we haven't used yet? Two-paragraph report, not a full dump.
```

**Say:** *"Subagent has isolated context. I get a report, not 2000 lines of code in my main window. Context preserved, parallel work done."*

---

### 0:40 – 0:55 · BDD (Slides 17–19)

**Concept focus:** BDD is verification inside Implement.

**Paste (prompt 11):**

```
Separate prompt pattern: I already have features/bronze_retail_trade.feature. Now write the step definitions in features/steps/bronze_retail_trade_steps.py. Do not modify the feature file. Implement the steps so the happy-path scenario passes against our current bronze_abs_retail_trade table. Don't make the failing scenarios pass yet — leave them red so I can see BDD catching real behaviour.
```

**Run:**

```bash
behave features/bronze_retail_trade.feature
```

**Expected:** 1 passes, 2 fail. Show the red output.

**Say:** *"Perfect. BDD is doing its job. The Gherkin is a spec I can show a stakeholder. The red tests are a to-do list. Compare to the ChatGPT pattern — generate 200 lines and hope."*

**Paste (prompt 12):**

```
Make the "one missing column" scenario pass. Do not touch the "malformed row" scenario — I want to see what you do with it later. Minimum edit to the bronze table code to satisfy that scenario.
```

**Run `behave` again.** 2 pass, 1 fail.

> *"Now I have a spec, a passing test for the column-handling case, and a documented failing case. My pair would know exactly where to pick this up."*

---

### 0:55 – 1:05 · Sycophancy + Memory-As-Untrusted (Slides 22–23)

**Concept focus:** Skipping V = agent building on stale or wrong context. Memory is untrusted input.

**This is the pay-off for the 0:07 plant.** You claimed 8 columns in CLAUDE.md. The API has 14. Claude has been building around this for 45 minutes.

**Paste (prompt 13 — false-premise trap):**

```
Based on everything in CLAUDE.md, write a summary table of the bronze layer's expected schema for a new joiner. One line per column.
```

**Expected outcome:** Claude produces a table with 8 columns (or hedges toward what CLAUDE.md says). This is the sycophancy. It's trusting the doc, not the code.

**Say:**

> "Look at that. Eight columns. Claude is confidently wrong — because CLAUDE.md says eight columns, and Claude trusted the doc. It's been planning against eight columns for the last hour. That's not Claude being stupid. That's Claude being sycophantic to *the retrieved context*. This is the failure mode that's hardest to catch, because it's not the user lying to the agent — it's the *artifact* lying to the agent."

**Paste (prompt 14 — the V fix):**

```
Before you answer again, grep the actual bronze_abs_retail_trade code and the ABS API response. Do not use CLAUDE.md as ground truth. What columns actually exist?
```

**Claude returns 14 columns.** Fix CLAUDE.md live.

**Run:**

```bash
git diff CLAUDE.md
```

**Say:**

> "That's memory governance. Memory is untrusted input — like an API response. You already validate API responses; validate memory too. Three knobs: provenance (where did the claim come from?), freshness (is it still true?), conflict (does it contradict something else?). V is where those three get checked."

**Commit:**

```bash
git add CLAUDE.md && git commit -m "fix(CLAUDE.md): correct column count 8→14 after live audit"
```

---

### 1:05 – 1:08 · Platforms Absorb V (Slide 24)

**Concept focus:** The platform has been doing V work for you throughout.

**No new prompt — this is retrospective.** Point at what just happened.

**Say:**

> "Look at what Databricks did for me in the last hour without me asking. Unity Catalog caught a permissions issue when I tried to write to the wrong schema — I didn't validate that, UC did. `databricks bundle validate` caught a YAML typo — I didn't validate that, the bundle did. `@dp.expect` flagged a bad row during the pipeline run — I didn't write a pytest for that, the decorator did. My V job shrunk to the things the platform *can't* see — the semantic claim in CLAUDE.md about column count. The platform can't tell me my doc lies. That's the V that's left for you, and it's small. Don't build custom validators for what the platform already catches deterministically. Spend your V budget on the claims no platform can see."

**Transition:** *"One more thing before lunch — why context management matters."*

---

### 1:08 – 1:13 · Context + Tokens (Slides 26–27)

**Concept focus:** You've watched me burn context for an hour. Look at the bar.

**Point at the context bar in Claude Code.** It should be amber or red at this point after 65 min of continuous build.

**Say:**

> "That's the session you just watched. Every file I read, every tool result, every prompt — in there. Claude's context window is ~200K tokens. At 90% it auto-compacts — earlier details get summarised, sometimes lossy. If I started Lab 1 in this session, I'd be working with a compressed memory of this morning. That's a setup for drift. Before your pair starts Lab 1 after lunch — `/clear`. Fresh context. CLAUDE.md is re-read from disk. You keep the artifact, you drop the conversation."

**Wrap:**

> "That's R.V.P.I., CLAUDE.md, Small Steps, power tools, BDD, Sycophancy, Platforms-Absorb-V, Context — eight beats in one build. By 12:00 we have a working bronze_abs_retail_trade table, a half-done bronze_abs_cpi_food, tests, CLAUDE.md audited. Your pair has 90 minutes after lunch to do the equivalent for your track. Go eat."

**Lunch.**

---

## Prompt library (copy-paste cheat sheet)

All 14 prompts from the run, in order. Keep this open in a scratchpad during delivery.

| # | Beat | Prompt |
|---|------|--------|
| 1 | CLAUDE.md draft | `Generate a CLAUDE.md for this repo. Context: we're building the bronze layer of the Grocery Intelligence Platform. Data sources: ABS Retail Trade, ABS CPI Food. Stack: PySpark, Lakeflow Declarative Pipelines (import databricks.declarative_pipelines as dp), @dp.table + @dp.expect decorators. Catalog: workshop_vibe_coding, schema: david_demo. Do not write any code yet. Just write CLAUDE.md.` |
| 2 | Research | `Research only — do not write code. What does the ABS Retail Trade API return? Fetch a sample row, and tell me: what columns, what types, what the first 3 rows look like. One page of output.` |
| 3 | Validate CLAUDE.md | `Before we plan the bronze table, validate the CLAUDE.md I wrote earlier. Does it match what you just saw from the API? Any discrepancies?` |
| 4 | Plan | `Plan only — do not implement. Design a single @dp.table function for bronze_abs_retail_trade. List: inputs, outputs (column list with types), one @dp.expect quality rule, one edge case to handle. Keep the plan to 10 lines.` |
| 5 | Impl step 1 | `Implement step 1 only: write the @dp.table function skeleton. No tests yet. No quality rules yet. Just the decorator, signature, docstring, and a TODO where the body goes. 15 lines maximum.` |
| 6 | Impl step 2 | `Now fill the body. Fetch the CSV from the ABS API, parse it into a Spark DataFrame, return it. Don't add quality rules — that's the next step.` |
| 7 | Skill | `Use the /bdd-features skill to draft a Gherkin feature file for bronze_abs_retail_trade. Three scenarios: the happy path, one missing column, one malformed row. Save to features/bronze_retail_trade.feature.` |
| 8 | MCP | `Use the databricks-docs MCP to confirm the exact syntax for CREATE OR REFRESH STREAMING TABLE and validate that our @dp.table decorator compiles to the correct SQL. I want to see the authoritative doc, not your recollection.` |
| 9 | Hook trigger | `Add a docstring to bronze_abs_retail_trade and to the feature file. One line each.` |
| 10 | Subagent | `Launch an Explore subagent to scan reference-implementation/ and report: what patterns did the reference bronze layer use that we haven't used yet? Two-paragraph report, not a full dump.` |
| 11 | BDD steps | `Separate prompt pattern: I already have features/bronze_retail_trade.feature. Now write the step definitions in features/steps/bronze_retail_trade_steps.py. Do not modify the feature file. Implement the steps so the happy-path scenario passes against our current bronze_abs_retail_trade table. Don't make the failing scenarios pass yet.` |
| 12 | BDD progress | `Make the "one missing column" scenario pass. Do not touch the "malformed row" scenario. Minimum edit to the bronze table code.` |
| 13 | Sycophancy trap | `Based on everything in CLAUDE.md, write a summary table of the bronze layer's expected schema for a new joiner. One line per column.` |
| 14 | V fix | `Before you answer again, grep the actual bronze_abs_retail_trade code and the ABS API response. Do not use CLAUDE.md as ground truth. What columns actually exist?` |

---

## Fallback plan

### If the ABS API is down

Fall back to `reference-implementation/data/abs_retail_trade_cached.csv`. Adjust prompt 2: *"The API is down. Use the cached CSV at reference-implementation/data/abs_retail_trade_cached.csv."*

### If the bundle deploy fails

`git checkout facilitator/block-4-fallback-bronze-complete`. Keep teaching. Narrate the recovery: *"This is also V — when you deploy, you validate. We just found an issue in the live build. Good."*

### If Claude refuses to follow Small Steps (writes too much at once)

Interrupt. Ctrl-C. *"See what just happened? I asked for one step; it did four. That's a prompting failure, not a model failure. Let me re-prompt more tightly."* Re-issue the prompt with explicit constraints.

### If you run long

Cut the Subagent beat (0:35–0:40). It's the most skippable. Hooks and BDD must stay — they're the highest-leverage demos in the block.

### If you run short

Extend Rule #1 pair exercise from 5 min to 8 min. Let attendees argue about what's missing from the CLAUDE.md.

---

## Required upstream changes

This runbook implies edits to the other five workshop files. Once this runbook is validated, propagate:

- **`WORKSHOP-TRANSCRIPT.md`**: rewrite Block 4 prose arc, move Block 5 Challenge Brief to 10:50–10:55.
- **`slides.html`**: move Slide 27 (Today's Challenge) to before Slide 11 (R.V.P.I.). Update `data-notes` across theory slides to reference the matching beat in this runbook rather than standalone demos.
- **`FACILITATOR-SCRIPT.md`**: replace Block 4 cues with "follow `starter-kit/demos/live-bronze-build-runbook.md`" pointer + a 10-line minute-by-minute summary for at-a-glance cueing.
- **`WORKSHOP-PLAN.md`**: update the 10:50–12:00 schedule row.
- **`VIBE-CODING-GUIDE.md` / `track-common.html`**: add a "what you saw at 11am" sidebar referencing the bronze-build artifacts (CLAUDE.md, feature file, audit log) as pattern reference.
