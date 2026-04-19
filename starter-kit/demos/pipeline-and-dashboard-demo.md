# Demo: Pipeline + App End-to-End (Block 2 climax, Slide 8)

**When:** 10:15 AM, immediately after Slide 7 (Watch First mini-demo).
**Duration:** 4–5 minutes live.
**Style:** Live (but heavily pre-deployed — see checklist).
**Purpose:** Show the full R.V.P.I. loop — Research → Validate → Plan → Implement — compressed into one flow that ends with the reference-implementation app answering a natural-language question against the column we just shipped. Attendees see the 90-min lab loop in 5 min, and they see the app shape Analyst pairs will build in Lab 2.

---

## Pre-Deploy Checklist (day before, and 30 min before workshop)

Per the **demo timing reality** memory: pipeline + app took 35 min last time. Pre-deploy is non-negotiable.

### Day-before checklist

- [ ] Reference-implementation pipeline deployed to a `david_demo` schema (NOT a team schema)
  - `cd reference-implementation && databricks bundle deploy -t demo`
  - `databricks bundle run grocery-intelligence-demo -t demo`
  - Confirm bronze + silver + gold tables populated
- [ ] **Reference-implementation app deployed to Databricks Apps**, pointed at `workshop_vibe_coding.david_demo`
  - `cd reference-implementation/app && databricks apps deploy grocery-intelligence-demo`
  - Confirm KPI cards load, `POST /api/ask` responds, first NL query returns data
- [ ] **Deliberately leave out a state-share-of-national column** on `gold_retail_summary` — this is what the demo adds
- [ ] Pre-test both NL queries (Beat 1 and Beat 7 below) against current data — note the expected answers
- [ ] Test that `databricks bundle deploy` + `run` cycle takes < 90 seconds when warm
- [ ] Save CODA terminal session with reference-implementation already cloned

### 30 minutes before workshop

- [ ] Open CODA terminal tab (warm)
- [ ] Open the **reference-implementation app** in a browser tab, already scrolled to the NL-query box
- [ ] Open Databricks workspace with the pipeline UI tab for `grocery-intelligence-demo` (fallback if app fails)
- [ ] Run `databricks bundle validate` in the terminal to warm credentials
- [ ] Trigger one test pipeline run so compute is hot
- [ ] Verify the app loads in < 2 seconds and `/api/ask` responds to a warm-up question

---

## The Demo Script (4–5 minutes, 8 beats)

### Beat 1 — Show the running app + first NL query (45 sec)

Flip projector to the **app tab** (reference-implementation).

> *"This is the app I built three weeks ago. KPI cards, monthly trend, recall table. Nothing fancy. What I want you to notice is the question box — it takes plain English, generates SQL via the Foundation Model API, runs it against my gold tables."*

Type into the NL query:

```
Which Australian state had the highest retail turnover last month?
```

Wait for the answer (~2–3 sec). It returns NSW with a number.

> *"NSW. That works because `gold_retail_summary` has state-level turnover. Totals. But I want something richer — each state's SHARE of national retail. Percentages, not just totals. Let me add that."*

### Beat 2 — Frame the change (15 sec)

Flip to terminal.

> *"I won't touch the app. I'll just add one column to the gold table — BDD-style. Test first, implementation second, deploy third. Then we come back to this app and ask again."*

### Beat 3 — Write the test (~45 sec)

Type into Claude Code:

```
Write ONE pytest test in tests/test_gold_retail_summary.py named
test_gold_has_state_share_of_national. Build a 6-row sample DataFrame:
3 states (NSW, VIC, QLD) × 2 months. Turnover in month 1: NSW=100,
VIC=60, QLD=40 (total 200). Turnover in month 2: NSW=110, VIC=70,
QLD=45 (total 225).

Assert the gold transformation adds a state_turnover_pct column.
Assert NSW month 1 is 50.0, VIC month 1 is 30.0, QLD month 1 is 20.0.
Assert shares sum to approximately 100 for each month.

Do NOT implement yet. Just the test.
```

Read the generated test aloud for ~5 seconds.

> *"Six rows. Numbers you can check in your head — 100 of 200 is 50%. That's the spec."*

### Beat 4 — Run red (15 sec)

```
Run tests/test_gold_retail_summary.py::test_gold_has_state_share_of_national.
Show me the failure.
```

Test fails — column doesn't exist yet.

> *"Red. Good. Now green."*

### Beat 5 — Implement (~45 sec)

```
Add a state_turnover_pct column to src/gold/retail_summary.py:

  turnover_millions / sum(turnover_millions) over (partition by month_date) * 100

One window function. No LAG. No date arithmetic. Nothing else.
```

Agent edits the file.

```
Re-run the test.
```

Green.

> *"Green. One column. Two prompts."*

### Beat 6 — Deploy pipeline (~60–90 sec)

```
databricks bundle deploy -t demo && databricks bundle run grocery-intelligence-demo -t demo
```

While the pipeline runs, narrate:

> *"Four prompts total — test, failed run, implementation, deploy. The pipeline's materialising the new column in gold right now. The app doesn't know it exists yet — it'll find out when we ask."*

### Beat 7 — Second NL query, same app (30 sec)

When `bundle run` completes, flip back to the **app tab**. Clear the previous answer. Type:

```
What percentage of national retail does each state account for this month?
```

Wait ~2–3 sec. The app generates SQL that selects `state_turnover_pct` from the freshly-updated `gold_retail_summary` and returns a table:

```
NSW:  ~35%
VIC:  ~26%
QLD:  ~20%
WA:   ~10%
SA:    ~6%
TAS:   ~2%
```

> *"Four prompts, one new column, and the app I built three weeks ago just answered a question it couldn't answer five minutes ago. That's the loop you'll run in the labs."*

### Beat 8 — Land it (15 sec)

> *"Two things I want you to notice. First, I didn't touch the app — I only touched the data. Second, every step had a verification artifact: test green, deploy succeeds, NL query returns real numbers. No verification, no trust. We come back to that all day."*

→ Transition to Slide 9 (Quiz-App Icebreaker).

---

## Fallback plan — if anything takes too long

### If Beat 3/5 (prompts) are slow

Wait it out — up to 45 sec each is fine. These usually complete in 15–25 sec.

### If Beat 6 (deploy + run) takes > 90 sec

Do NOT wait for it to finish. After ~60 seconds of waiting:

> *"The pipeline's deploying in the background — the app will pick it up in a minute. Trust me, it works. The point was: four prompts got you from zero to a new metric. That's the loop."*

Skip Beat 7. Jump to Beat 8, then Slide 9.

### If Beat 7 (second NL query) returns bad SQL or an error

The NL-to-SQL layer can be flaky. If it errors or returns wrong columns:

> *"The NL layer is doing its best. Let me just query it directly."*

Open a terminal tab with databricks-sql-connector or a SQL editor warmed up, run:

```sql
SELECT state, state_turnover_pct
FROM workshop_vibe_coding.david_demo.gold_retail_summary
WHERE month_date = (SELECT MAX(month_date) FROM workshop_vibe_coding.david_demo.gold_retail_summary)
ORDER BY state_turnover_pct DESC;
```

Same payoff. Then transition.

### If the deploy fails live

Don't try to fix on stage. Fall back to:

> *"Demo gods are unkind today. Here's what would have happened — [describe the app returning state shares]. The point: this loop works and you're about to do it for real in Lab 1."*

Move on to Slide 9.

### If Claude Code is rate-limited / slow / down

Pre-recorded video as ultimate fallback. Record the full demo once the week before and keep a copy on the presentation laptop. Start with: *"Let me play a 4-minute recording of this exact demo — ran this on Tuesday."*

---

## What this demo teaches (facilitator mental model)

- **The R.V.P.I. loop in compressed form.** Research = read current gold schema. Validate = test fixture proves the expected arithmetic. Plan = one window function, no join. Implement = small steps, one prompt each.
- **It previews every slide that came before:** Specs (test fixture), BDD (red → green), Small Steps (4 prompts not 1 mega-prompt), Deploy (DABs), Sycophancy defence (test assertion can't bluff).
- **It primes every track.** DE pairs see the pipeline + tests + deploy flow. Analyst pairs see the exact app shape they'll build. DS pairs see the gold table being extended — which is where their features come from.
- **It uses the app as both evidence and preview.** The NL-query round-trip answers *"does Claude actually connect to real data?"* and shows Analyst track's finish line.

---

## What NOT to do

- Don't narrate every prompt character as you type — makes the demo feel slow and over-rehearsed
- Don't add extra flourish ("let me also add a log statement while I'm here") — scope creep kills timing
- Don't promise the app will update at a specific time — network/compute variance will embarrass you
- Don't let the demo extend past 5 minutes even if everything works — you're eating the icebreaker
- Don't demo the app's UI chrome (the chart, the recalls table) — stay on the NL-query box; the visual change happens inside that one component

## The one success criterion

Attendees leave Block 2 thinking: *"that was really four prompts? And the app just… picked it up?"* If one attendee asks you *"wait, was that actually live?"* — you won. The demo's job is to make the thing feel real and achievable, not impressive.
