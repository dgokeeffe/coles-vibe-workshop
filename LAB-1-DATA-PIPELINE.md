# Lab 1: Build a Data Pipeline with Vibe Coding

**Duration:** 75 minutes
**Goal:** Build, test, and deploy a data transformation pipeline using an AI coding agent

---

## Scenario

You're a Coles data engineer. Raw store transaction data lands daily in Unity Catalog. You need to build a pipeline that:

1. Reads raw transaction data
2. Cleans and validates it
3. Joins with product reference data
4. Computes daily store-level aggregations
5. Writes to a gold table for downstream analytics
6. Includes data quality checks

**You will NOT write this code yourself.** You will direct an AI agent to build it.

---

## Step 1: Setup (10 min)

### 1.1 Open your Coding Agents App

Navigate to your assigned app URL in the browser. You should see a terminal.

### 1.2 Create a project directory

In the terminal, type to Claude Code:

```
Create a new Python project called "store-pipeline" with:
- A src/ directory for pipeline code
- A tests/ directory for pytest tests
- A pyproject.toml with pyspark and pytest dependencies
- A CLAUDE.md with these rules:
  - Use PySpark for all data processing
  - All functions must have type hints
  - All tables use Unity Catalog: workshop_vibe_coding.<your_schema>
  - Follow medallion architecture (bronze/silver/gold)
  - Every transformation function must have a corresponding test
```

### 1.3 Review the CLAUDE.md

Open the generated CLAUDE.md. Does it capture your intent? Edit it to add:

```markdown
## Data Standards
- Date columns: use DATE type, format YYYY-MM-DD
- Currency columns: use DECIMAL(12,2)
- All tables must have a processing_timestamp column
- Partition gold tables by transaction_date

## Testing Standards
- Use pytest with pyspark test fixtures
- Test with small DataFrames (5-10 rows), not full datasets
- Assert on schema, row counts, and specific values
```

---

## Step 2: Write Specs & Tests First (15 min)

**This is the most important step.** You write the tests, the agent writes the code.

### 2.1 Ask the agent to explore the raw data

```
Explore the raw data in workshop_vibe_coding.raw_data.store_transactions.
Show me the schema, sample rows, row count, and any data quality issues.
```

### 2.2 Write your test specifications

Ask the agent:

```
Create pytest tests for a data pipeline with these transformations:

1. clean_transactions(df) -> DataFrame:
   - Remove rows where transaction_amount is null or negative
   - Standardize store_id to uppercase
   - Parse transaction_date to DATE type
   - Test: given 10 rows with 2 invalid, output should have 8 rows

2. enrich_with_products(transactions_df, products_df) -> DataFrame:
   - Left join transactions with products on product_id
   - Add product_name and category columns
   - Test: all original transaction rows preserved, product columns added

3. compute_daily_aggregations(df) -> DataFrame:
   - Group by store_id, transaction_date
   - Compute: total_revenue, transaction_count, avg_basket_size, unique_products
   - Test: 3 stores x 2 days = 6 output rows with correct aggregations

4. validate_output(df) -> bool:
   - No null values in key columns
   - total_revenue > 0 for all rows
   - transaction_count > 0 for all rows
   - Test: valid data returns True, invalid data raises assertion

Write ONLY the tests. Do NOT implement the functions yet.
```

### 2.3 Review the tests

Read through the generated tests. Do they capture your requirements? Adjust if needed.

---

## Step 3: Build with the Agent (35 min)

### 3.1 Let the agent implement

```
Now implement all the functions to make the tests pass.
Run the tests after each function to verify.
```

Watch the agent work. Notice:
- It reads the test expectations
- It writes code to satisfy them
- It runs tests, sees failures, and iterates
- It converges on a working solution

### 3.2 Add the pipeline orchestrator

```
Create a main pipeline function that:
1. Reads from workshop_vibe_coding.raw_data.store_transactions
2. Reads from workshop_vibe_coding.raw_data.products
3. Calls clean_transactions, enrich_with_products, compute_daily_aggregations
4. Calls validate_output on the result
5. Writes the gold table to workshop_vibe_coding.<your_schema>.daily_store_metrics
6. Uses MERGE (upsert) so it's idempotent on re-runs

Also write a test for the orchestrator using mock data.
```

### 3.3 Handle edge cases

```
Add tests for these edge cases:
- Empty input DataFrame (should produce empty output, not error)
- Duplicate transactions (should be deduplicated by transaction_id)
- Future-dated transactions (should be filtered out)

Then implement the fixes to pass these new tests.
```

### 3.4 Run the full pipeline

```
Run the full pipeline against the actual data in Unity Catalog.
Show me the output table schema and a sample of results.
```

---

## Step 4: Deploy with DABs (15 min)

### 4.1 Create a Databricks Asset Bundle

```
Create a databricks.yml for this pipeline that:
- Defines a job called "daily_store_metrics"
- Runs the pipeline daily at 6 AM AEST
- Uses a job cluster with 2-4 workers
- Targets the workshop_vibe_coding catalog
- Has dev and prod deployment targets
```

### 4.2 Validate and deploy

```
Validate the bundle configuration and deploy to the dev target.
Show me the job URL so I can verify it in the workspace.
```

---

## Success Criteria

- [ ] Tests written BEFORE implementation
- [ ] All tests pass
- [ ] Pipeline reads raw data from Unity Catalog
- [ ] Transformations applied correctly
- [ ] Gold table written with MERGE (idempotent)
- [ ] Data quality validation passes
- [ ] Deployed as a scheduled Databricks Job via DABs

## Reflection Questions

1. How much of the code did you write vs. the agent?
2. Where did the tests help the agent stay on track?
3. Where did you need to intervene and steer?
4. How long would this have taken without the agent?
