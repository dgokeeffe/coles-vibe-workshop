# Grocery Intelligence Platform

An end-to-end Databricks demo built in a single session:
**ABS public data → Lakeflow pipeline → Unity Catalog gold tables → FastAPI app deployed on Databricks Apps.**

Designed as a reference for a customer workshop — "what you can build on the Databricks Data Intelligence Platform in an afternoon."

## What it does

Ingests two live public datasets from the Australian Bureau of Statistics:

1. **Retail Trade** (RT 1.0.0) — monthly seasonally-adjusted turnover by state × industry
2. **Consumer Price Index** (CPI 2.0.0) — quarterly food-category price index across 8 capital cities

Turns them into 4 business-ready gold tables, and serves them through a polished dashboard with filters and live charts.

## Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                  ABS SDMX-CSV API (HTTPS)                     │
│          Retail Trade   +   Consumer Price Index              │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
      ┌────────────────────────────────────────────────┐
      │  Lakeflow Declarative Pipeline (classic)       │
      │                                                │
      │   bronze_*_raw     →  @dp.table (HTTP ingest)  │
      │   silver_*         →  @dp.materialized_view    │
      │                       decode codes, type cast, │
      │                       @dp.expect quality rules │
      │   gold_*           →  @dp.materialized_view    │
      │                       YoY windows, aggregations│
      └────────────────────┬───────────────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
    Unity Catalog                   Pro SQL Warehouse
    grocery_intel_demo_catalog.grocery.*
            │                             │
            ▼                             ▼
    ┌─────────────────────────────────────────────────┐
    │  Databricks Apps: FastAPI + htmx + Chart.js    │
    │  (databricks-sql-connector, parameterized SQL) │
    └─────────────────────────────────────────────────┘
                           │
                           ▼
                    Dashboard in browser
```

## Gold-table contract

The app depends on exactly these column names/types:

| Table | Columns |
|---|---|
| `gold_retail_summary`      | `state`, `month`, `total_turnover`, `yoy_growth_pct` |
| `gold_retail_turnover`     | `state`, `industry`, `month`, `turnover` |
| `gold_food_inflation`      | `category`, `quarter`, `index_value` |
| `gold_food_inflation_yoy`  | `state`, `category`, `quarter`, `yoy_change_pct` |

## Project layout

```
grocery-intel-demo/
├── databricks.yml            # Bundle config + variables
├── resources/
│   ├── pipeline.yml          # Lakeflow pipeline (classic)
│   └── app.yml               # Databricks App + warehouse binding
├── pipeline/
│   ├── bronze.py             # ABS HTTP ingest → bronze tables
│   ├── silver.py             # Decode codes, cleanse, quality rules
│   └── gold.py               # 4 business-ready tables
├── app/
│   ├── app.py                # FastAPI backend (4 endpoints)
│   ├── app.yaml              # Databricks Apps runtime config
│   ├── requirements.txt
│   └── static/index.html     # Single-page UI (Tailwind + Chart.js + htmx)
└── tests/
    ├── test_pipeline.py      # Pipeline module smoke tests
    └── test_app.py           # FastAPI endpoint tests (mocked SQL)
```

## Deploy it yourself

### 1. Prereqs
- Databricks workspace with Unity Catalog (classic, for Pro SQL warehouse support)
- Databricks CLI ≥ 0.240.0
- A Pro SQL warehouse (Small is enough)
- A Unity Catalog you own — defaults to `grocery_intel_demo_catalog` (override with `BUNDLE_VAR_catalog`)

### 2. Authenticate
```bash
databricks auth login <workspace-url> --profile <your-profile>
export DATABRICKS_CONFIG_PROFILE=<your-profile>
```

### 3. Configure
Edit `databricks.yml` → `targets.dev.workspace.host` to your workspace URL.

Create the Pro warehouse (or reuse one) and capture its ID:
```bash
databricks warehouses create --json '{
  "name": "grocery-intel-wh", "cluster_size": "Small",
  "warehouse_type": "PRO", "enable_photon": true,
  "enable_serverless_compute": false, "auto_stop_mins": 30,
  "min_num_clusters": 1, "max_num_clusters": 1
}'
export BUNDLE_VAR_warehouse_id=<id-from-above>
```

Create the schema (catalog is assumed to already exist):
```bash
databricks schemas create grocery grocery_intel_demo_catalog
```

### 4. Deploy the pipeline + run it
```bash
databricks bundle validate
databricks bundle deploy --target dev
databricks bundle run grocery_intel_pipeline --target dev
```

Verify gold tables exist:
```bash
databricks api post /api/2.0/sql/statements --json '{
  "warehouse_id":"'$BUNDLE_VAR_warehouse_id'",
  "statement":"SELECT COUNT(*) FROM grocery_intel_demo_catalog.grocery.gold_retail_summary",
  "wait_timeout":"30s"
}'
```

### 5. Deploy the app
```bash
databricks bundle run grocery_intel_app --target dev
```

### 6. ⚠️ Grant Unity Catalog permissions to the app's service principal

**This step is required — without it the app returns 500 with `INSUFFICIENT_PERMISSIONS` on the first query.**

Databricks Apps run as an auto-provisioned workspace service principal. Fetch its client ID, then grant:

```bash
SP=$(databricks apps get grocery-intel-demo | jq -r .service_principal_client_id)

for stmt in \
  "GRANT USE CATALOG ON CATALOG grocery_intel_demo_catalog TO \`$SP\`" \
  "GRANT USE SCHEMA ON SCHEMA grocery_intel_demo_catalog.grocery TO \`$SP\`" \
  "GRANT SELECT ON SCHEMA grocery_intel_demo_catalog.grocery TO \`$SP\`"; do
  databricks api post /api/2.0/sql/statements --json "{
    \"warehouse_id\":\"$BUNDLE_VAR_warehouse_id\",
    \"statement\":\"$stmt\",
    \"wait_timeout\":\"30s\"
  }"
done
```

### 7. Open the app
The app URL prints from step 5. Filters drive the three charts live.

**First-query latency:** the warehouse auto-stops after 30 min idle. The first query after a restart takes ~30s; subsequent queries are fast. Click "Apply" on the filter bar to warm the endpoint before showing it to anyone.

## Tests

```bash
uv pip install -r app/requirements.txt pytest
pytest -v
```

- **`test_pipeline.py`** — asserts every gold-table function exists (breaks fast if someone renames a contract), verifies silver has `@dp.expect` rules, checks YoY window is 12 months.
- **`test_app.py`** — mocks `databricks.sql` and checks all 4 endpoints return the right shape with parameterized SQL wiring.

## Data sources

- **ABS Retail Trade**: https://data.api.abs.gov.au/data/ABS,RT,1.0.0/M1..20..M
- **ABS CPI**: https://data.api.abs.gov.au/data/ABS,CPI,2.0.0/1.20001+1144+30001+30002+30003+114120.10.1+2+3+4+5+6+7+8.Q

Both returned as SDMX-CSV with `Accept: application/vnd.sdmx.data+csv;version=1.0.0`.
