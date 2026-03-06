# Pre-Workshop Setup Guide

## For Coles Platform Team

### 1. Deploy Coding Agents Databricks App

Each workshop participant needs their own instance of the Coding Agents App.

**Repository:** https://github.com/dgokeeffe/coding-agents-databricks-apps

```bash
# Clone the repo
git clone https://github.com/dgokeeffe/coding-agents-databricks-apps.git
cd coding-agents-databricks-apps

# Follow docs/deployment.md for full instructions
# Key steps:
# 1. Configure app.yaml with your workspace details
# 2. Set AI Gateway endpoint
# 3. Deploy via databricks apps deploy
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

**Per-participant deployment:**
```bash
# Deploy app for each participant
for USER in user1 user2 user3; do
  databricks apps deploy \
    --name "vibe-workshop-${USER}" \
    --source-code-path ./
done
```

### 2. AI Gateway Setup

Create a route that provides access to the required models:

```bash
# Create AI Gateway route (if not already configured)
databricks api post /api/2.0/serving-endpoints \
  --json '{
    "name": "workshop-ai-gateway",
    "config": {
      "served_entities": [
        {
          "external_model": {
            "name": "claude-sonnet-4-6",
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

-- Create per-participant schemas
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.participant_01;
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.participant_02;
-- ... etc for each participant

-- Grant permissions
GRANT USE CATALOG ON CATALOG workshop_vibe_coding TO `workshop-participants`;
GRANT USE SCHEMA, CREATE TABLE, SELECT, MODIFY
  ON SCHEMA workshop_vibe_coding.participant_01
  TO `user1@coles.com.au`;
-- ... etc

-- Load synthetic dataset (David will provide this)
-- Pre-load into a shared read-only schema
CREATE SCHEMA IF NOT EXISTS workshop_vibe_coding.raw_data;
-- Tables will be loaded via provided notebook
```

### 4. Network Checklist

- [ ] Databricks App URLs accessible from conference room WiFi
- [ ] AI Gateway endpoints reachable (no ZScaler blocks on Anthropic/OpenAI)
- [ ] GitHub accessible (for cloning starter repos)
- [ ] WebSocket connections allowed (required for xterm.js terminal)

### 5. Testing End-to-End

```bash
# Test from a participant's perspective:
# 1. Open browser, navigate to app URL
# 2. Terminal loads with Claude Code available
# 3. Run: claude --version (should show version)
# 4. Run: claude "list tables in workshop_vibe_coding.raw_data"
# 5. Verify it can read data and generate code
```

---

## For Participants

### What You Need

1. **Laptop** with a modern web browser (Chrome, Edge, or Firefox)
2. **Databricks workspace access** - you should already have this
3. **No software installation required** - everything runs in the browser

### What to Bring

- A project idea you'd like to try building with an AI coding agent (optional but recommended)
- Curiosity and willingness to experiment

### What to Expect

- A full day of hands-on coding with AI agents
- You will build and deploy a working application by end of day
- All skill levels welcome - the AI agent helps bridge experience gaps
- The workshop is interactive - ask questions anytime

### Optional Pre-Reading

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Databricks Apps Overview](https://docs.databricks.com/en/apps/index.html)
- [What is Vibe Coding?](https://en.wikipedia.org/wiki/Vibe_coding) - The concept coined by Andrej Karpathy
