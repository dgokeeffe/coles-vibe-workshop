# Lab 1: Build Your Data Pipeline (Data Engineering Track)

**Duration:** 55 minutes
**Goal:** Build, test, and deploy a Lakeflow Declarative Pipeline using an AI coding agent
**Team Size:** 2–3 people

> Complete `LAB-0-GETTING-STARTED.md` first, then return here.

---

## The Mission

Your team needs a data pipeline that ingests public Australian retail data, transforms it through a medallion architecture, and produces analytics-ready gold tables. You'll use **TDD** to guide the agent and **Lakeflow Declarative Pipelines** to define your tables.

**You will NOT write this code yourself.** You will direct an AI agent to build it.

---

## Your Data Sources

| Source | API Endpoint | What It Contains |
|--------|-------------|-----------------|
| **ABS Retail Trade** | `https://data.api.abs.gov.au/data/ABS,RT,1.0.0/...` | Monthly retail turnover by state & industry since 2010 |
| **ABS Consumer Price Index** | `https://data.api.abs.gov.au/data/ABS,CPI,2.0.0/...` | Quarterly food price indices by state since 2010 |

Both APIs return CSV data via the SDMX standard. The agent will handle the API calls and parsing.

---


---

> **The Small Steps Principle**
>
> Every prompt in this lab is designed to be **1–3 minutes of agent work** with a **verification moment** at the end. If you catch yourself about to send a big "build me X, Y, and Z" prompt — **stop and split it**. The pattern you're learning today is: one prompt → one change → one verification → next prompt.
>
> **While the agent is running, one of you should:** (a) read the previous output critically, (b) pre-write the next prompt, (c) update CLAUDE.md with a learning. No one ever just waits.

---

## Phase 1: Explore + Set Up (10 min)

> **Team Tasks**
> - **Person A (Terminal):** Run prompts 1.1–1.3 below
> - **Person B (Terminal):** Copy `starter-kit/CLAUDE.md` to project root, customize team name/schema; while Person A's agent runs, read outputs critically
> - **Person C (Databricks UI):** Verify Unity Catalog schema exists, check checkpoint tables are accessible; during waits, pre-write Phase 2 prompts

> **Remember:** Tests are your spec. Write them BEFORE any implementation. And keep each prompt tight.

### 1.1 Explore the retail trade data (2 min)

```
Fetch the first 5 rows of the ABS Retail Trade API:
https://data.api.abs.gov.au/data/ABS,RT,1.0.0/M1.20+41+42+43+44+45.20.1+2+3+4+5+6+7+8.M?format=csv&startPeriod=2024-01&endPeriod=2024-03

Show me the columns, data types, and the 5 sample rows. Don't save anything — just print.
```

**Verify before moving on:** You can name the columns and their meaning.

### 1.2 Explore the CPI data (2 min)

```
Now fetch the first 5 rows of the ABS CPI Food API:
https://data.api.abs.gov.au/data/ABS,CPI,2.0.0/1.10001+20001.10.1+2+3+4+5+6+7+8.Q?format=csv&startPeriod=2024-Q1&endPeriod=2024-Q4

Show me the columns and 5 sample rows. No file saves.
```

**Verify:** You can spot the REGION and INDEX columns.

### 1.3 Create the repo skeleton (2 min)

```
Create the project skeleton with empty placeholder files:
- src/bronze/abs_retail_trade.py  (empty, just a module docstring)
- src/bronze/abs_cpi_food.py  (same)
- src/silver/  (create dir)
- src/gold/  (create dir)
- tests/conftest.py  (with a SparkSession fixture, no test functions yet)
- resources/  (create dir)

No logic yet. Just the structure.
```

**Verify:** You can see the files exist and the conftest has the fixture.

---

## Phase 2: Build ONE Bronze Table — Retail Trade (15 min)

> **Why one at a time:** You'll build `abs_retail_trade.py` end-to-end first (write → test → fix → quality rule). Then in Phase 3 you'll repeat the pattern for CPI — faster this time because you know the shape.

> **Team Tasks**
> - **Person A (Terminal):** Drive prompts 2.1–2.4
> - **Person B (Terminal):** Read every agent output, flag anything using pandas or skipping PySpark; pre-write prompts for Phase 3
> - **Person C (Databricks UI):** Watch Unity Catalog for the new table; prepare checkpoint fallback

### 2.1 Write ONE schema test (2 min)

```
In tests/test_bronze_retail_trade.py, write a single pytest test named
`test_bronze_has_required_columns`. It should:

- Create a small DataFrame with 3 sample rows in retail-trade shape
  (TIME_PERIOD, OBS_VALUE, REGION, INDUSTRY columns)
- Assert the schema has these 4 columns
- Assert no row has null TIME_PERIOD or OBS_VALUE

Do NOT write the bronze function yet. Just the test.
Use the spark fixture from conftest.py.
```

**Verify:** Read the test. Does it capture "bronze ingests the raw schema with required fields non-null"? If no, ask the agent to adjust.

### 2.2 Implement the bronze table (2 min)

```
In src/bronze/abs_retail_trade.py, implement the @dp.table function
that fetches the ABS Retail Trade CSV (same URL as Phase 1.1) and returns
the DataFrame as-is. No transformations, no quality rules yet.

Target: workshop_vibe_coding.<team_schema>.bronze_retail_trade.
Use spark.read.csv() with header=True, inferSchema=True.
```

**Verify:** You can read the function end-to-end in <30 seconds. No pandas.

### 2.3 Run the test — fix if it fails (3 min)

```
Run tests/test_bronze_retail_trade.py. Show me the output.
Fix ONLY if the test fails. Don't change anything else.
```

**Verify:** Test is green. The agent should not have touched other files.

### 2.4 Add ONE quality rule (2 min)

```
Add a single @dp.expect("valid_time_period", "TIME_PERIOD IS NOT NULL")
decorator to the bronze retail trade table. Nothing else.
Re-run the test to confirm it still passes.
```

**Verify:** One decorator added. Test still green.

> **Stuck at 15 min?** Grab **Checkpoint 1A**: pre-loaded bronze tables in `workshop_vibe_coding.checkpoints`. Tell the agent: *"Use the pre-loaded table `checkpoints.bronze_retail_trade` — copy it to our schema instead of calling the API."*

---

## Phase 3: Repeat Pattern — CPI Bronze (10 min)

> **Now you know the shape.** Same pattern, different table. Aim for 10 min total — the pattern should feel automatic.

> **Team Tasks**
> - Rotate the driver: whoever was reading becomes Person A
> - Keep each prompt tight (1–3 min)

### 3.1 Test, implement, quality rule — one-shot each

```
Mirror what we did for retail trade, now for CPI food:

Prompt 1 (run this first):
"In tests/test_bronze_cpi_food.py, write a single test named
test_bronze_cpi_has_required_columns with 3 sample rows (TIME_PERIOD,
OBS_VALUE, REGION, INDEX), asserting schema and non-null values."

Prompt 2 (after test is written):
"Implement src/bronze/abs_cpi_food.py as @dp.table fetching the CPI CSV
(URL from Phase 1.2). Return as-is."

Prompt 3 (after implementation):
"Run the CPI test. Fix only if it fails."

Prompt 4 (after test passes):
"Add @dp.expect('valid_time_period', 'TIME_PERIOD IS NOT NULL')."
```

> **The point:** Four tight prompts, four verification moments. Never more than 3 minutes of agent work without a human checkpoint.

---

## Phase 3: Build Silver + Gold (20 min)

> **Team Tasks for This Phase**
> - **Person A (Terminal):** Build silver retail_turnover and gold retail_summary
> - **Person B (Terminal):** Build silver food_price_index and gold food_inflation
> - **Person C (Databricks UI):** Monitor test output, review gold table data as it appears, prepare icebreaker answers
>
> *Teams of 2: Person A takes Terminal tasks, Person B takes Terminal + UI tasks.*

### 3.1 Build silver transformations

## Phase 4: Silver Layer — One Table at a Time (12 min)

> **Same small-steps pattern as bronze.** Test → implement → run → fix, one table at a time.

### 4.1 Write ONE silver test for retail_turnover (2 min)

```
In tests/test_silver_retail_turnover.py, write a single pytest test
named test_silver_decodes_state_codes. It should:

- Create a small bronze-shape DataFrame with 3 rows using REGION codes 1, 2, 3
- Assert that the silver transformation decodes them to
  "New South Wales", "Victoria", "Queensland" in a state_name column

Do NOT write the silver function yet.
```

**Verify:** Test captures the "code → state name" decode. Nothing else.

### 4.2 Implement silver retail_turnover (2 min)

```
Create src/silver/retail_turnover.py as @dp.table. Read from
workshop_vibe_coding.<team_schema>.bronze_retail_trade.

Only do these transformations:
- Decode REGION (1=New South Wales, 2=Victoria, 3=Queensland, 4=South Australia,
  5=Western Australia, 6=Tasmania, 7=Northern Territory,
  8=Australian Capital Territory) → state_name column
- Rename OBS_VALUE to turnover_millions

Don't decode INDUSTRY or parse dates yet. Just these two.
```

**Verify:** Read the function. Two transformations, nothing else.

### 4.3 Run test, then add INDUSTRY decode (3 min)

```
Run tests/test_silver_retail_turnover.py. Show me the output.
If it passes, add a second test for INDUSTRY decoding (code 20 → "Food retailing"),
then extend the silver function to decode INDUSTRY.
```

**Verify:** Two tests green. Each added behaviour has its own test.

### 4.4 Repeat for silver food_price_index (5 min)

```
Same pattern for CPI:
1. Write test_silver_food_price_decodes_state_codes (small DataFrame, asserts decode).
2. Implement src/silver/food_price_index.py with ONLY state decode + OBS_VALUE → cpi_index rename.
3. Run test. Fix if it fails.
4. Add test for INDEX code decoding (10001 → "All groups CPI", 20001 → "Food and non-alcoholic beverages"), then extend the function.
```

> **Stuck?** Grab **Checkpoint 1B-silver** (pre-loaded silver tables).

---

## Phase 5: Gold Materialized Views — Small Steps (10 min)

### 5.1 Write ONE gold test — rolling average (2 min)

```
In tests/test_gold_retail_summary.py, write test_gold_has_3_month_rolling_avg.
Given 12 months of silver retail data (one state, simple numeric turnover),
assert that a 3-month rolling average column (turnover_3m_avg) is computed.

Just the test. Small fixture.
```

### 5.2 Implement gold retail_summary — rolling avg only (3 min)

```
Create src/gold/retail_summary.py as @dp.materialized_view. Read from silver
retail_turnover. Add ONLY a 3-month rolling average (turnover_3m_avg).

Do NOT add 12-month average or YoY growth yet.
```

### 5.3 Test passes, then add remaining metrics (3 min)

```
Run the gold test. If green, add two more tests + transformations:
- turnover_12m_avg (12-month rolling)
- yoy_growth_pct (year-over-year %)

Add the test first for each metric, then the code.
```

### 5.4 Gold food_inflation (2 min)

```
src/gold/food_inflation.py — @dp.materialized_view from silver food_price_index
with just yoy_change_pct. Write the test first.
```

> **Stuck at 40 min total?** Grab **Checkpoint 1B**: full silver+gold pre-loaded.

---

## Phase 6: Verify Your Data (3 min)

```
Query the gold tables and show me:
1. Top 5 states by food retail turnover (latest month)
2. Year-over-year food price inflation by state (latest quarter)
3. The state with the highest retail growth rate
```

**This is where you check your ice breaker predictions!**

---

## Phase 7: Deploy with DABs (5 min)

> **Team Tasks**
> - **Person A (Terminal):** Run 7.1–7.2
> - **Person B (Databricks UI):** Watch the pipeline appear in the Workflows tab
> - **Person C:** Query gold tables to check icebreaker prediction answers

### 7.1 Generate pipeline.yml + databricks.yml (2 min)

```
Create resources/pipeline.yml for a Lakeflow Declarative Pipeline:
- Name: grocery-intelligence-<team_name>
- Serverless: true
- Libraries: all src/ notebooks
- Catalog: workshop_vibe_coding, schema: <team_schema>

Also create databricks.yml with a dev target using our catalog/schema
and including the pipeline resource. Don't deploy yet.
```

**Verify:** Read the YAML. Syntax sensible?

### 7.2 Validate, then deploy (3 min)

```
Run: databricks bundle validate
If clean, run: databricks bundle deploy -t dev
Then: databricks bundle run grocery-intelligence-<team_name> -t dev
```

**Verify:** Pipeline appears in Workflows tab. Tables in Unity Catalog.

> **Stuck?** Grab **Checkpoint 1C**: complete pipeline code and databricks.yml.

---

## Pro Tips

> **Steering the agent effectively:**
>
> - If the agent uses pandas instead of PySpark, say **"use PySpark, not pandas"** and add it to CLAUDE.md
> - If the agent writes implementation before you have tests, say **"stop — write the tests first"**
> - If the agent goes off track, say **"stop, let's go back to the failing tests"**
> - Use **"show me the test output"** to see exactly what's failing
> - Say **"explain what this function does"** to verify the agent's logic
> - **Rotate the driver** every 20 min so everyone gets hands-on time
> - Use skills: try **`/commit`** to commit your work with a good message

---

## Success Criteria

- [ ] Tests written BEFORE implementation
- [ ] All tests pass (bronze, silver, gold)
- [ ] Pipeline uses `@dp.table` and `@dp.materialized_view` decorators
- [ ] Data quality expectations with `@dp.expect()`
- [ ] Gold tables have rolling averages and YoY metrics
- [ ] Deployed as a Lakeflow pipeline via DABs
- [ ] Can answer the ice breaker prediction questions from the data!

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **ABS API returns errors or times out** | The APIs can be slow. Grab **Checkpoint 1A** (pre-loaded bronze tables) and skip the API ingestion. |
| **Agent uses pandas instead of PySpark** | Add to CLAUDE.md: "Always use PySpark, never pandas". Remind the agent explicitly. |
| **Tests fail with SparkSession errors** | Ensure conftest.py creates a local SparkSession: `SparkSession.builder.master("local[*]").getOrCreate()` |
| **@dp.table decorator not found** | Make sure the import is: `import dlt` (for older runtimes) or `import databricks.declarative_pipelines as dp` |
| **Can't write to Unity Catalog** | Check your schema: `workshop_vibe_coding.<team_schema>`. Run `databricks auth status` to verify access. |
| **Pipeline deploy fails** | Validate first: `databricks bundle validate`. Check databricks.yml for syntax errors. |
| **Agent rewrites working code** | Say: "Don't change functions that are already passing tests. Only fix the failing ones." |
| **Running out of time** | Grab the next checkpoint. No shame — the goal is to have data for Lab 2 and a demo at the end. |

---

## Reflection Questions (for Show & Tell)

1. How much code did you write vs. the agent?
2. Where did TDD help the most?
3. What was your most interesting data insight?
4. Were your ice breaker predictions right?
