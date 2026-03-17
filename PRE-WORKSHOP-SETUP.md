# Pre-Workshop Setup Guide

## For Coles Platform Team (Farbod & Swee Hoe)

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
  TO `team1-user1@coles.com.au`, `team1-user2@coles.com.au`;
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
```

### 8. Workshop Materials Checklist

- [ ] Prediction cards printed (1 per team, 5 questions each)
- [ ] Scoreboard ready (whiteboard or projected Google Sheet)
- [ ] Quick-reference cards printed (1 per person)
- [ ] Slides loaded and tested on projector
- [ ] Backup demos on David's laptop (pre-recorded)
- [ ] Post-workshop feedback survey prepared (3 questions, keep it short)

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
