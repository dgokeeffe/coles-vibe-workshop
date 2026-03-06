# Lab 2: Build & Deploy a Full-Stack App on Databricks

**Duration:** 75 minutes
**Goal:** Build a complete web application with AI features, deploy on Databricks Apps

---

## Scenario

You built a data pipeline in Lab 1 that produces daily store metrics. Now you need a dashboard app that:

1. Displays store performance data from your gold table
2. Lets users ask natural language questions about the data
3. Runs as a Databricks App accessible via browser

**You will direct the AI agent to build the entire stack.**

---

## Architecture

```
┌──────────────┐     HTTP      ┌──────────────────────┐
│              │  (htmx calls) │                      │
│   Browser    │──────────────▶│   FastAPI Backend     │
│  (Tailwind   │◀──────────────│   (app.py)           │
│   + htmx)    │  HTML / JSON  │                      │
│              │               │  GET /api/metrics     │
└──────────────┘               │  POST /api/ask        │
                               │  GET /                │
                               └──────┬───────┬───────┘
                                      │       │
                              SQL     │       │  LLM
                              queries │       │  prompt
                                      ▼       ▼
                               ┌────────┐ ┌──────────┐
                               │Databri-│ │Databricks│
                               │cks SQL │ │AI Gateway│
                               │Warehou-│ │(Found.   │
                               │se      │ │Model API)│
                               └────────┘ └──────────┘
```

---

## Step 1: Design (10 min)

### 1.1 Write your PRD

In your Coding Agents terminal, create a new project:

```
Create a new project called "store-dashboard" with this PRD:

## Store Performance Dashboard

### Overview
A web application that displays daily store metrics and allows
natural language querying of the data.

### User Stories
1. As a store manager, I want to see my store's daily revenue,
   transaction count, and average basket size in a clean dashboard.
2. As an analyst, I want to filter by date range and store.
3. As a business user, I want to ask questions in plain English
   like "which store had the highest revenue last week?"

### Technical Requirements
- Backend: FastAPI (Python)
- Frontend: HTML + Tailwind CSS + htmx (no npm/node required)
- Data source: workshop_vibe_coding.<your_schema>.daily_store_metrics
- AI feature: Natural language query using Databricks Foundation Model API
- Deployment: Databricks Apps

### API Endpoints
- GET /api/metrics?store_id=X&start_date=Y&end_date=Z
- POST /api/ask {"question": "which store performed best?"}
- GET / (serves the frontend)

### CLAUDE.md Rules
- Use FastAPI with Pydantic models for all endpoints
- Use databricks-sql-connector for database queries
- All API responses are JSON
- Frontend uses htmx for dynamic updates (no JavaScript frameworks)
- Include error handling for all endpoints
- Write tests for all API endpoints using pytest + httpx
```

### 1.2 Review and refine

Look at the generated CLAUDE.md and project structure. Add any team-specific standards.

---

## Step 2: Build with TDD (45 min)

### 2.1 Backend - Tests First

```
Write pytest tests for the FastAPI backend:

1. test_get_metrics:
   - Returns 200 with valid store_id and date range
   - Returns list of daily metric records
   - Each record has: store_id, transaction_date, total_revenue,
     transaction_count, avg_basket_size, unique_products
   - Filters correctly by store_id and date range
   - Returns 400 for invalid date format

2. test_ask_question:
   - Returns 200 with a valid question
   - Response includes: answer (string), sql_query (string),
     data (list of records)
   - Returns 400 for empty question

3. test_health:
   - GET /health returns 200 with {"status": "ok"}

Write ONLY the tests. Do NOT implement yet.
```

### Example Test Reference

If you're new to testing FastAPI with pytest, here's what a test looks like. Share this with the agent as a reference pattern:

```python
# tests/conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from app import app

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

# tests/test_api.py
import pytest

@pytest.mark.asyncio
async def test_health_endpoint(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_get_metrics_returns_records(client):
    response = await client.get("/api/metrics?store_id=S001&start_date=2024-01-01&end_date=2024-01-31")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "store_id" in data[0]
        assert "total_revenue" in data[0]
```

### 2.2 Backend - Implementation

```
Implement the FastAPI backend to pass all tests.

For the /api/ask endpoint:
- Use the Databricks Foundation Model API to convert natural language
  to SQL against the daily_store_metrics table
- Execute the generated SQL via databricks-sql-connector
- Return the results with the generated SQL for transparency

For database connectivity:
- Use the Databricks SQL Connector
- Connection details from environment variables
- Connection pooling for efficiency

Run tests after implementation.
```

### 2.3 Frontend

```
Build the frontend with:

1. A header with "Store Performance Dashboard" title
2. Filter bar: store dropdown, date range pickers, "Apply" button
3. Metrics cards: Total Revenue, Transactions, Avg Basket Size
4. A data table showing daily metrics
5. An "Ask AI" section with a text input and response area
6. Use Tailwind CSS from CDN for styling
7. Use htmx for all dynamic interactions (no custom JavaScript)
8. Use Databricks brand colors: #FF3621 (red), #1B3139 (dark), #00A972 (green)

The frontend should call the FastAPI backend via htmx.
```

### 2.4 Wire it together

```
Create app.py that:
1. Serves the FastAPI app
2. Mounts static files for the frontend
3. Serves index.html at the root
4. Includes CORS middleware
5. Has proper error handling

Also create app.yaml for Databricks Apps deployment:
command: ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

And requirements.txt with all dependencies.
```

### 2.5 Test locally

```
Run the app locally and verify:
1. The homepage loads
2. The metrics API returns data
3. The ask endpoint generates SQL and returns results
4. Filters work correctly

Run all tests one final time.
```

---

## Pro Tips

> **Steering the agent effectively:**
>
> - If the agent goes off track, say **"stop, let's go back to the test failures"** to refocus it.
> - Use **"show me the test output"** to see exactly what's failing before the agent tries a fix.
> - If the frontend looks wrong, say **"take a screenshot"** or describe what you see and ask the agent to fix it.
> - For the AI query feature, test with simple questions first: *"what is the total revenue?"* before trying complex ones.
> - If the agent writes raw SQL string concatenation, say **"parameterize the SQL queries to prevent injection"**.
> - **If you're ahead of schedule**, try: *"add a Chart.js revenue trend line chart"* or *"add a CSV export button."*

---

## Step 3: Deploy to Databricks (15 min)

### 3.1 Create Databricks App config

```
Create a databricks.yml bundle that:
- Deploys this as a Databricks App
- Sets environment variables for database connection
- Configures the AI Gateway endpoint for LLM calls
- Has dev and prod targets
```

### 3.2 Deploy

```
Deploy the app to Databricks using:
databricks apps deploy --name store-dashboard-<your_name>

Show me the app URL when it's ready.
```

### 3.3 Verify

Open the app URL in your browser. Test:
- [ ] Dashboard loads with data
- [ ] Filters work
- [ ] "Ask AI" returns meaningful answers
- [ ] Data matches what's in your gold table

---

## Step 4: Share (5 min)

Give a 2-3 minute demo to the group:
- Show your app running
- Ask it a natural language question
- Share one thing that surprised you about the process

---

## Success Criteria

- [ ] FastAPI backend with tested endpoints
- [ ] HTML frontend with Tailwind CSS + htmx
- [ ] Natural language query feature using Foundation Model API
- [ ] Data sourced from Lab 1's gold table
- [ ] Deployed and running on Databricks Apps
- [ ] All tests passing

## Bonus Challenges (if time permits)

1. **Add a chart:** Use Chart.js (CDN) to add a revenue trend line chart
2. **Add authentication:** Use Databricks App built-in auth
3. **Add caching:** Cache frequent queries to reduce database load
4. **Add export:** CSV download of filtered data

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **htmx not loading / dynamic elements not working** | Check the `<script>` tag in your HTML `<head>`. It should be: `<script src="https://unpkg.com/htmx.org@2.0.4"></script>`. Open browser DevTools (F12) and check the Console for load errors. |
| **CORS errors in the browser console** | Ensure `CORSMiddleware` is added to your FastAPI app with `allow_origins=["*"]` (for dev). The agent sometimes forgets this — say **"add CORS middleware"**. |
| **SQL injection risk in /api/ask endpoint** | The AI-generated SQL should never include user input directly. Tell the agent: **"review the generated SQL for injection risks and parameterize any user inputs"**. Add table schema to the LLM system prompt so it generates valid SQL. |
| **App deploys but shows a blank page** | Check that static files are mounted correctly: `app.mount("/static", StaticFiles(directory="static"))`. Verify `index.html` exists at the expected path. Check Databricks App logs for errors. |
| **AI generates invalid SQL or hallucinates columns** | Add the table schema and column names to the LLM system prompt. Include 2-3 example queries. Say: **"add the table schema to the system prompt for the LLM"**. |
| **`databricks-sql-connector` import errors** | Ensure it's in `requirements.txt`. Run `uv pip install databricks-sql-connector`. On Apple Silicon, you may need: `uv pip install databricks-sql-connector --no-binary pyarrow`. |
| **App works locally but fails when deployed** | Check that all environment variables are set in `app.yaml`. Databricks Apps run in a container — local file paths won't work. Use relative paths for static files. |

---

## Reflection Questions

1. How did the PRD guide the agent's architecture decisions?
2. Where did htmx + server-side rendering simplify things vs. React/Vue?
3. How did the natural language to SQL feature work? Any hallucinations?
4. Could you deploy this to production as-is? What's missing?
