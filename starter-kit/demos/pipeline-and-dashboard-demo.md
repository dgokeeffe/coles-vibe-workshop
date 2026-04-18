# Demo: Pipeline + Dashboard End-to-End (Arc D Climax)

**When:** 9:45 theory block, Arc D slot — immediately before Lab 0 (~10:25 AM, slide 24)
**Duration:** 4–5 minutes live
**Style:** Live (but heavily pre-deployed — see checklist)
**Purpose:** Show the full BDD loop — test → implement → deploy → dashboard — in 5 minutes. Attendees see the 60-minute lab loop compressed into a single demo. This answers *"does this actually work?"* before theory fully concludes.

---

## Pre-Deploy Checklist (day before, and 30 min before workshop)

Per the **demo timing reality** memory: pipeline + app took 35 min last time. Pre-deploy is non-negotiable.

### Day-before checklist

- [ ] Reference-implementation pipeline deployed to a `david_demo` schema (NOT a team schema)
  - `cd reference-implementation && databricks bundle deploy -t demo`
  - `databricks bundle run grocery-intelligence-demo -t demo`
  - Confirm bronze + silver + gold tables populated
- [ ] AI/BI dashboard built on `workshop_vibe_coding.david_demo.gold_retail_summary`
  - Charts: turnover by state (line), rolling averages (bar), state comparison (geo or table)
  - **Deliberately leave out a year-over-year column** — this is what the demo adds
- [ ] Test that `databricks bundle deploy` + `run` cycle takes < 90 seconds when warm
- [ ] Save CODA terminal session with reference-implementation already cloned

### 30 minutes before workshop

- [ ] Open CODA terminal tab (warm)
- [ ] Open Databricks workspace with:
  - [ ] Pipeline UI tab for `grocery-intelligence-demo`
  - [ ] AI/BI dashboard tab for `gold_retail_summary`
- [ ] Run `databricks bundle validate` in the terminal to warm credentials
- [ ] Trigger one test pipeline run so compute is hot
- [ ] Verify dashboard loads in < 2 seconds

---

## The Demo Script (4–5 minutes, 6 beats)

### Beat 1 — Show the running system (30 sec)

Flip projector to the dashboard tab.

> *"This pipeline is running on my instance right now. ABS Retail Trade, CPI, FSANZ recalls — bronze to silver to gold, refreshed this morning. Here's the BI dashboard. Monthly turnover by state, rolling averages, the usual."*

Pause. Let them look at it for ~5 seconds.

### Beat 2 — Frame the change (20 sec)

Flip to terminal.

> *"I want to add a year-over-year growth column to the gold table. Not by hand — BDD-style. Test first, implementation second, watch it flow all the way through."*

### Beat 3 — Write the test (~45 sec)

Type into Claude Code:

```
Write ONE pytest test in tests/test_gold_retail_summary.py named
test_gold_has_yoy_growth. Use a 24-month sample DataFrame for ONE state
(NSW, turnover_millions increasing 5% month over month). Assert the
gold transformation adds a `yoy_growth_pct` column and that the value
at month 13 is approximately 79.6% (compound 12 months of 5%).

Do NOT implement yet. Just the test.
```

Read the generated test aloud for ~5 seconds.

> *"There's the spec. Sample data, expected value, one column. Now run it."*

### Beat 4 — Run red (15 sec)

```
Run tests/test_gold_retail_summary.py::test_gold_has_yoy_growth.
Show me the failure.
```

Test fails — column doesn't exist yet.

> *"Red. Good. Now let me make it green."*

### Beat 5 — Implement (~45 sec)

```
Add a yoy_growth_pct column to src/gold/retail_summary.py using a
window function partitioned by state ordered by month_date, comparing
each row's turnover_millions to the row 12 months prior. Percentage
change. Nothing else.
```

Agent edits the file.

```
Re-run the test.
```

Green.

> *"Green. One metric, two prompts."*

### Beat 6 — Deploy + dashboard refresh (~90 sec)

```
databricks bundle deploy -t demo && databricks bundle run grocery-intelligence-demo -t demo
```

While the pipeline runs (~60–90 sec), narrate:

> *"Four prompts total — test fixture, failed test run, implementation, deploy. The pipeline's materialising the new column in gold right now. Watch."*

When `bundle run` completes, flip to dashboard tab. Refresh.

Point at the new `yoy_growth_pct` column in the table or add it to an existing chart.

> *"There it is. New column in production gold, visible in the BI dashboard. Four prompts. One metric. End-to-end in five minutes."*

> *"That's what the next 60 minutes of Lab 1 looks like — tight prompts, visible verification, real deployed artifacts. Let's go."*

→ Transition to slide 25 (Today's Challenge), then Lab 0.

---

## Fallback plan — if anything takes too long

### If Beat 3/5 (prompts) are slow

Wait it out — up to 45 sec each is fine. These usually complete in 15–25 sec.

### If Beat 6 (deploy + run) takes > 90 sec

Do NOT wait for it to finish. After ~60 seconds of waiting:

> *"The pipeline's deploying in the background — it'll refresh the dashboard in a minute. Trust me, it works. The point was: **four prompts got you from zero to a new metric**. That's the loop."*

Flip to Today's Challenge slide. Skip the dashboard-refresh payoff. The teaching lands even without it.

### If the deploy fails live

Don't try to fix on stage. Fall back to:

> *"Demo gods are unkind today. Here's what would have happened — [describe the dashboard with the new column]. The point: this loop works and you're about to do it for real in Lab 1."*

Move on to Today's Challenge.

### If Claude Code is rate-limited / slow / down

Pre-recorded video as ultimate fallback. Record the full demo once the week before and keep a copy on the presentation laptop. Start with: *"Let me play a 4-minute recording of this exact demo — ran this on Tuesday."*

---

## What this demo teaches (facilitator mental model)

- **It's the paradigm shift in action.** Arc B was the setup — "watch first before we teach." Arc D is *the same demo principle* but with every piece of technique applied.
- **It previews every slide that came before:** Specs (test fixture), TDD (red → green), Small Steps (4 prompts, not 1 mega-prompt), Deploy (DABs).
- **It motivates Lab 1 directly.** What they saw in 5 min is the same loop they'll run for 60 min with their own data.

---

## What NOT to do

- Don't narrate every prompt character as you type it — makes the demo feel slow and over-rehearsed
- Don't add extra flourish ("let me also add a log statement while I'm here") — scope creep kills timing
- Don't promise the dashboard will update at a specific time — network/compute variance will embarrass you
- Don't let the demo extend past 5 minutes even if everything works — you're eating Lab 0 time

## The one success criterion

Attendees leave Arc D thinking: *"that was really four prompts? And it deployed?"* If one attendee asks you *"wait, was that actually live?"* — you won. The demo's job is to make the thing feel real and achievable, not impressive.
