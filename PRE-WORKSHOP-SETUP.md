# Pre-Workshop Setup Guide

## For the Platform Team (your champions)

All items must be completed and tested BEFORE workshop day.

### 1. Deploy Coding Agents App

Each participant needs their own instance of the Coding Agents App.

**Repository:** https://github.com/dgokeeffe/coding-agents-databricks-apps

```bash
# Clone and deploy
git clone https://github.com/dgokeeffe/coding-agents-databricks-apps.git
cd coding-agents-databricks-apps

# Deploy per participant (or per team if sharing)
for TEAM in team_01 team_02 team_03 team_04 team_05; do
  databricks apps deploy \
    --name "vibe-workshop-${TEAM}" \
    --source-code-path ./
done
```

**App Configuration (app.yaml):**
```yaml
command:
  - gunicorn
  - app:app
  - --bind
  - 0.0.0.0:8000
  - --timeout
  - "0"
  - --workers
  - "1"

env:
  - name: DATABRICKS_HOST
    value: "<your-workspace-url>"
  - name: AI_GATEWAY_ENDPOINT
    value: "<your-ai-gateway-route>"
```

### 2. AI Gateway Setup

```bash
# Create AI Gateway route with Claude Opus 4.6
databricks api post /api/2.0/serving-endpoints \
  --json '{
    "name": "workshop-ai-gateway",
    "config": {
      "served_entities": [
        {
          "external_model": {
            "name": "claude-opus-4-6",
            "provider": "anthropic",
            "anthropic_config": {
              "anthropic_api_key": "{{secrets/workshop/anthropic-key}}"
            }
          }
        }
      ]
    },
    "rate_limits": [
      {"key": "user", "renewal_period": "minute", "calls": 20}
    ]
  }'
```

### 2b. Data Science Track Infrastructure

The DS track needs additional permissions and infrastructure:

**MLflow Permissions:**
```sql
-- Teams need to create experiments and log runs
GRANT CREATE_EXPERIMENT ON WORKSPACE TO `workshop-participants`;
-- Teams need to register models in Unity Catalog
GRANT CREATE_MODEL ON SCHEMA workshop_vibe_coding.team_01 TO `team1-user1@coda.com.au`;
-- Repeat for each team schema...
```

**Unity Catalog Model Registry Permissions (DS track — critical):**
```sql
-- Pairs need CREATE MODEL on their schema to register UC-scoped models
GRANT CREATE_MODEL ON SCHEMA workshop_vibe_coding.pair_01 TO `pair1-user1@coda.com.au`;
-- Repeat for each pair schema. Without this, the agent's mlflow.register_model
-- call silently falls back to the workspace registry — which is the #1 support
-- question when DS pairs hit Lab 2 Phase 2.

-- Additional: pairs need EXECUTE on the fallback checkpoint model
GRANT EXECUTE ON MODEL workshop_vibe_coding.checkpoints.grocery_forecaster
  TO `account users`;
```

> **Model Serving is NOT used in Lab 2.** We deliberately skip it — DS pairs
> score predictions in a notebook (Tier 1) or via a Lakeflow batch job using
> `mlflow.spark_udf` (Tier 2 stretch). No serving permissions required.

**Pre-loaded Gold Tables (Checkpoint 0):**
All tracks depend on gold tables being available from minute one. Run the checkpoint loader to populate:
```sql
-- These must exist BEFORE the workshop
-- DS and Analyst tracks read from these immediately
-- DE track builds their own pipeline to produce the same tables
SELECT COUNT(*) FROM workshop_vibe_coding.checkpoints.retail_summary;  -- should be > 0
SELECT COUNT(*) FROM workshop_vibe_coding.checkpoints.food_inflation_yoy;  -- should be > 0
```

**DS Track Checkpoint Data:**
```sql
-- Pre-built feature table (Checkpoint DS-1B) — pairs whose Lab 1 stalls
CREATE TABLE IF NOT EXISTS workshop_vibe_coding.checkpoints.retail_features AS ...;

-- Pre-trained model registered to UC (Checkpoint DS-2A) — fallback if training
-- or registration fails in Lab 2 Phase 1/2. MUST be registered with the
-- @fallback alias so the escape-hatch prompts work:
--   mlflow.set_registry_uri("databricks-uc")
--   mlflow.register_model(..., name="workshop_vibe_coding.checkpoints.grocery_forecaster")
--   client.set_registered_model_alias(name=..., alias="fallback", version=1)
```
> **No Model Serving checkpoint.** Lab 2 doesn't deploy serving endpoints —
> if a pair is lost, they load `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`
> via `mlflow.pyfunc.load_model` in a notebook and keep moving.

### 3. Unity Catalog Setup

```sql
-- Create workshop catalog
CREATE CATALOG IF NOT EXISTS workshop_vibe_coding;

-- Create per-team schemas (teams of 2-3)
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.team_01;
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.team_02;
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.team_03;
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.team_04;
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.team_05;

-- Create checkpoints schema (read-only, pre-loaded data)
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.checkpoints;

-- Create raw data schema (shared volumes for API data)
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.raw_data;

-- Grant per-team permissions
GRANT USE CATALOG ON CATALOG workshop_vibe_coding TO `workshop-participants`;

-- Per-team write access
GRANT USE SCHEMA, CREATE TABLE, CREATE MATERIALIZED VIEW, SELECT, MODIFY
  ON SCHEMA workshop_vibe_coding.team_01
  TO `team1-user1@coda.com.au`, `team1-user2@coda.com.au`;
-- Repeat for each team...

-- Read-only access to checkpoints and raw data
GRANT USE SCHEMA, SELECT
  ON SCHEMA workshop_vibe_coding.checkpoints
  TO `workshop-participants`;
GRANT USE SCHEMA, SELECT
  ON SCHEMA workshop_vibe_coding.raw_data
  TO `workshop-participants`;
```

### 4. Pre-Load Checkpoint Data

**Critical:** Checkpoints ensure no team gets stuck. Run the checkpoint loader notebook
(provided by David) to populate:

**Checkpoint 1A — Bronze Tables:**
```sql
-- In workshop_vibe_coding.checkpoints
-- These are pre-ingested from the ABS APIs
-- abs_retail_trade_bronze: raw retail trade CSV data
-- abs_cpi_food_bronze: raw CPI food CSV data
```

**Checkpoint 1B — Silver + Gold Tables:**
```sql
-- retail_turnover: decoded state/industry names, parsed dates
-- food_price_index: decoded CPI categories
-- retail_summary: with rolling averages and YoY growth
-- food_inflation_yoy: with YoY CPI change percentages
```

**Checkpoint 2A — App Skeleton:**
- Pre-built FastAPI app with health endpoint and database connection
- Located in shared Git repo (David will provide)

**Checkpoint 2B/2C/2D:**
- Genie space setup instructions
- Dashboard SQL templates
- Complete reference solution

### 5. Genie + AI/BI Permissions

```sql
-- Teams need ability to create Genie spaces
GRANT CREATE GENIE SPACE ON CATALOG workshop_vibe_coding TO `workshop-participants`;

-- Teams need ability to create AI/BI dashboards
-- (Usually available by default, but verify)
```

### 6. Network Checklist

- [ ] Databricks App URLs accessible from conference room WiFi
- [ ] AI Gateway endpoints reachable (no ZScaler blocks on Anthropic)
- [ ] GitHub accessible (for cloning starter repos)
- [ ] WebSocket connections allowed (required for xterm.js terminal)
- [ ] ABS API accessible: `https://data.api.abs.gov.au` (for live data ingestion)
- [ ] FSANZ website accessible: `https://www.foodstandards.gov.au` (optional)

### 7. End-to-End Testing

Do this from the conference room WiFi on the day before:

```bash
# 1. Open browser, navigate to app URL
# 2. Terminal loads with Claude Code available
# 3. Run: claude --version (should show version)
# 4. Test: Ask Claude to query a checkpoint table:
#    "SELECT * FROM workshop_vibe_coding.checkpoints.retail_summary LIMIT 5"
# 5. Test: Verify Genie space creation works
# 6. Test: Verify AI/BI dashboard creation works
# 7. Test: Verify DABs deployment works:
#    databricks bundle validate
# 8. Test DS track: Verify MLflow experiment creation works
# 9. Test DS track: Verify UC model registration works
#    - mlflow.set_registry_uri("databricks-uc"); mlflow.register_model(...)
#    - Confirm it appears under Catalog Explorer, NOT workspace Models
#    - Confirm client.set_registered_model_alias(..., "champion", 1) succeeds
# 10. Test DS track: Verify the @fallback checkpoint model loads:
#    mlflow.pyfunc.load_model("models:/workshop_vibe_coding.checkpoints.grocery_forecaster@fallback")
# 10. Test Analyst track: Verify Genie space creation works
```

### 8. Workshop Materials Checklist

- [ ] Prediction cards printed (1 per team, 5 questions each)
- [ ] Scoreboard ready (whiteboard or projected Google Sheet)
- [ ] Quick-reference cards printed (1 per person)
- [ ] Slides loaded and tested on projector
- [ ] Backup demos on David's laptop (pre-recorded)
- [ ] Post-workshop feedback survey prepared (3 questions, keep it short)
- [ ] Three-track lab instructions printed/available (DE, DS, Analyst)
- [ ] Starter-kit folder accessible from each terminal
- [ ] **Airgap-safe MLflow reference present:** `starter-kit/references/mlflow-uc.md` AND the bundled skill at `starter-kit/skills/databricks-mlflow-ml/` both ship in the repo. Confirm both landed on every pair's environment. The reference file is for in-prompt `@reference`; the skill is for Claude Code auto-trigger when DS pairs write MLflow code.
- [ ] **Install the DS skill into Claude Code** — run once per pair environment: `cp -R starter-kit/skills/databricks-mlflow-ml ~/.claude/skills/` (or use the AI Dev Kit `install_skills.sh` script once the upstream PR lands). Without this step, the skill won't auto-trigger.
- [ ] **UC volume for MLflow artifacts:** per pair schema, create `CREATE VOLUME IF NOT EXISTS workshop_vibe_coding.<pair_schema>.mlflow_artifacts;`. Required for experiment creation in UC-enforced workspaces — without it, `log_model` fails.
- [ ] Gold tables pre-loaded in checkpoints schema (Checkpoint 0)
- [ ] **UC model registry permissions** verified for each pair schema (`CREATE MODEL ON SCHEMA workshop_vibe_coding.<pair_schema>`) — §2 above
- [ ] **`@fallback` checkpoint model** registered at `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback` (loading it from a notebook succeeds in under 10 sec)
- [ ] MLflow experiments permissions verified for DS track
- [ ] ~~Model Serving permissions verified for DS track~~ — not needed, Lab 2 uses batch inference

---

## For Participants

### What You Need

1. **Laptop** with a modern web browser (Chrome recommended)
2. **Databricks workspace access** — you should already have this
3. **No software installation required** — everything runs in the browser

### What to Bring

- Curiosity and willingness to experiment
- A teammate or two (teams of 2-3, assigned at the start)

### What to Expect

- A 5-hour hands-on hackathon building with AI coding agents
- You'll build a complete data platform: pipeline, web app, and natural language interface
- Teams compete — best platform wins bragging rights!
- All skill levels welcome — the AI agent helps bridge experience gaps
- Checkpoints ensure nobody gets stuck

### Optional Pre-Reading

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Databricks Apps Overview](https://docs.databricks.com/en/apps/index.html)
- [What is Vibe Coding?](https://en.wikipedia.org/wiki/Vibe_coding)
- [Lakeflow Declarative Pipelines](https://docs.databricks.com/en/declarative-pipelines/index.html)
