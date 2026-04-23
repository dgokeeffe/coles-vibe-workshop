# Lab 2: Data Quality, New Sources & Scheduling (Data Engineering Track)

**Duration:** 80 minutes
**Goal:** Add data sources, implement data quality rules, and set up pipeline scheduling
**Team Size:** Pairs (two-person teams)

> Complete `LAB-0-GETTING-STARTED.md` and `LAB-1-DE.md` first.

---

## Pair Programming

Same pattern as Lab 1 — keep the loop tight.

- **Driver:** types prompts, runs tests, commits.
- **Navigator:** reads, verifies in the Databricks UI, challenges at the **V** step of R.V.P.I.
- **Swap every 15 min** — set a timer.
- **Escalation rule:** if a task doesn't fit R.V.P.I. in 15 min, split it.

Before you start, re-read your CLAUDE.md. Is it still current after Lab 1?

---

## The Mission

Your pipeline handles ABS retail and CPI data. Now make it production-grade: add a new data source (FSANZ food recalls), implement data quality rules across all tables, and set up automated scheduling.

---

> **The Small Steps Principle (continued from Lab 1)**
>
> Every prompt below is 1–3 min of agent work. If something feels like a "do it all" prompt, split it. Each prompt should end with a verification moment: *"after this, will I know whether it worked?"*
>
> **While the Driver is running the agent, the Navigator should:** read the previous output critically, pre-write the next prompt, or update CLAUDE.md with a learning.

---

## Phase 1: Add FSANZ Food Recalls — Bronze (8 min)

> **Pair Tasks**
> - **Driver:** Drive 1.1–1.3.
> - **Navigator:** Read every output for quality and flag web-scraping gotchas. Have the checkpoint fallback URL ready, and watch for the table to appear in Unity Catalog.

### 1.1 Write ONE schema test (2 min)

```
In tests/test_bronze_food_recalls.py, write ONE test named
test_bronze_food_recalls_has_required_columns.

Sample 3 rows with columns: product, category, issue, date, state, url.
Assert the schema contains all 6 columns, and product/date are non-null.
```

### 1.2 Implement bronze fsanz (3 min)

```
Create src/bronze/fsanz_food_recalls.py as @dp.table.
Data source: https://www.foodstandards.gov.au/food-recalls/recalls
If the site is blocked, read workshop_vibe_coding.checkpoints.fsanz_food_recalls
and copy rows as-is.

No silver transformations yet — just ingest.
```

**Verify:** Read the function. Simple ingest, no extras.

### 1.3 Run test, fix if needed (3 min)

```
Run tests/test_bronze_food_recalls.py. Show me the output.
Fix ONLY the bronze file if the test fails.
```

> **Stuck?** Grab **Checkpoint DE-2A** (FSANZ bronze pre-loaded). Tell the agent: *"Use `checkpoints.fsanz_food_recalls` directly."*

---

## Phase 2: Silver food_recalls — Small Steps (8 min)

### 2.1 Test for date parsing (1 min)

```
In tests/test_silver_food_recalls.py, write ONE test named
test_silver_parses_date_strings. Sample DataFrame with date strings
like "2024-01-15". Assert the silver layer returns proper DATE type.
```

### 2.2 Implement silver with ONLY date parsing (2 min)

```
Create src/silver/food_recalls.py as @dp.table reading from bronze.
Only transformation: parse `date` column from string to DATE. Nothing else.
```

### 2.3 Run test. Then add state normalization (2 min)

```
Run the silver test. If green, add test_silver_normalizes_state_names
(maps "NSW" → "New South Wales", "VIC" → "Victoria"), then extend
the silver function to match.
```

### 2.4 Verify in Unity Catalog (30 sec)

**Navigator:** run `SELECT * FROM workshop_vibe_coding.<team_schema>.silver_food_recalls LIMIT 5` in a SQL editor tab. Confirm the dates and state names look right.

---

## Phase 3: Data Quality Rules — One Tier at a Time (10 min)

> **The pattern:** add expectations to ONE table, re-run its test, then move on. Don't batch.

### 3.1 Bronze expectations (3 min)

```
Add these expectations to our existing bronze tables. Apply one at a time,
running the relevant test after each to confirm nothing breaks:

Prompt 1: "Add @dp.expect('valid_time_period', 'TIME_PERIOD IS NOT NULL')
to bronze_retail_trade and bronze_cpi_food. Run their tests."

Prompt 2: "Add @dp.expect('valid_obs_value', 'OBS_VALUE IS NOT NULL') to both.
Run tests again."
```

### 3.2 Silver expectations — one hard failure (2 min)

```
Add @dp.expect_or_fail("valid_state",
  "state_name IN ('New South Wales','Victoria','Queensland','South Australia',
   'Western Australia','Tasmania','Northern Territory','Australian Capital Territory')")
to silver_retail_turnover.

This is expect_or_fail (not just expect) — pipeline fails on invalid state.
Run its test to confirm it still passes.
```

### 3.3 Gold sanity bounds (2 min)

```
Add @dp.expect("valid_yoy", "yoy_growth_pct BETWEEN -100 AND 500")
to gold_retail_summary. Run its test.
```

### 3.4 Verify expectations surface in the pipeline UI (3 min)

**Navigator:** open the pipeline in Workflows. Confirm you can see the expectation names and pass/fail counts after a run.

---

## Phase 4: Cross-Source Gold View (5 min)

### 4.1 Write ONE join test (2 min)

```
In tests/test_gold_grocery_insights.py, write test_join_retail_cpi_recalls.
Minimal fixtures: 2 months retail, 2 quarters CPI, 1 recall.
Assert the join produces columns: state, month, turnover_millions, yoy_growth_pct,
cpi_yoy_change, recall_count.
```

### 4.2 Implement grocery_insights.py (3 min)

```
Create src/gold/grocery_insights.py as @dp.materialized_view.
Join retail_summary (monthly) with food_inflation (quarterly) on state + quarter,
left join silver_food_recalls on state + month.

Start simple — get the join working. No derived metrics beyond what's listed.
```

**Verify:** Test passes. View exists in UC.

---

## Phase 5: Scheduling + Deploy (5 min)

### 5.1 Add the schedule (2 min)

```
Update databricks.yml — add a trigger to our pipeline resource:

trigger:
  cron:
    quartz_cron_expression: "0 0 6 * * ?"
    timezone_id: "Australia/Sydney"

Don't deploy yet. Just show me the diff.
```

**Verify:** Read the diff. Sensible?

### 5.2 Validate, deploy, confirm (3 min)

```
Run: databricks bundle validate
If clean, run: databricks bundle deploy -t dev
Open the pipeline in Workflows. Confirm the schedule shows "Daily at 6:00 AM (Australia/Sydney)".
```

---

## Phase 6: Verify + Prepare for Demo (4 min)

- Verify full pipeline with all sources in the Workflows UI
- Check data quality expectations are visible and passing
- Prepare 3-minute demo: pipeline DAG screenshot, quality metrics, cross-source view query, schedule

---

## Stretch Goal: Publish a Managed Iceberg Table (Optional)

> **Advanced — skip unless you're ahead of schedule.** This is the open-lakehouse story in practice: publish your gold table in Iceberg format so external engines (Snowflake, Trino, DuckDB, BigQuery) can read it via the Iceberg REST Catalog — zero copy, same Unity Catalog governance.

### Key rules for managed Iceberg in UC

- Format: `USING ICEBERG` (not `USING DELTA`)
- **No `LOCATION`** — UC owns the physical layout.
- **No `PARTITIONED BY`** — use liquid clustering instead: `CLUSTER BY (state, month)`.
- `REPLACE`, `NOT NULL`, and constraints are supported.

### Prompt for the agent

```
Create src/gold/retail_summary_iceberg.py that reads from our existing gold
retail_summary table and publishes it as a managed Iceberg table for
external-engine consumption.

Requirements:
- Table name: workshop_vibe_coding.<team_schema>.retail_summary_iceberg
- CREATE OR REPLACE TABLE ... USING ICEBERG AS SELECT ...
- CLUSTER BY (state, month_date) — no PARTITIONED BY
- Do NOT specify a LOCATION (UC manages the path)
- Include a test that queries the Iceberg table and confirms row count
  matches the source Delta table

Also show me:
1. The Iceberg REST Catalog URL for external engines (from the Databricks docs MCP)
2. A short note in the module docstring: when to pick Iceberg (multi-engine
   reads, vendor-neutral) vs Delta (deepest Databricks feature set)
```

### What "done" looks like

- `SELECT * FROM workshop_vibe_coding.<team_schema>.retail_summary_iceberg LIMIT 10` returns rows.
- Table appears in Unity Catalog with format = `iceberg`.
- Mention this in your demo: *"Same data, same governance, readable by Snowflake/Trino/DuckDB with zero copy."*

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **FSANZ website blocked** | Use checkpoint: `workshop_vibe_coding.checkpoints.fsanz_food_recalls` |
| **Web scraping errors** | Try RSS feed: `https://www.foodstandards.gov.au/rss/recalls` |
| **@dp.expect_or_fail stops pipeline** | Use `@dp.expect` (warn) first, upgrade after verifying |
| **Cross-source join duplicates** | Join on state + date range, not exact date (CPI is quarterly) |
| **Cron not triggering** | Check timezone_id and Quartz format. `?` is required for day-of-week. |
| **Pipeline too slow** | Use `spark.conf.set("spark.sql.shuffle.partitions", "4")` for workshop |
| **Running out of time** | Grab Checkpoint DE-2C (complete pipeline) or DE-2D (full solution) |

---

## Success Criteria

- [ ] FSANZ food recalls ingested (bronze + silver)
- [ ] Data quality expectations on all tables
- [ ] Cross-source gold view joining retail + CPI + recalls
- [ ] Pipeline scheduled with cron trigger
- [ ] All tests pass including new data source
- [ ] Ready for 3-minute demo

---

## Reflection Questions (for Demo)

1. How do data quality expectations change your confidence in the pipeline?
2. What challenges came with adding a new data source?
3. How would you monitor this pipeline in production?
4. What's the most interesting insight from the cross-source view?
