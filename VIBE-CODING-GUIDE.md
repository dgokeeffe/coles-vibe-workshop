# Vibe Coding Best Practices

**Coles x Databricks Vibe Coding Workshop**
A Guide to Agentic Software Development with Claude

---

## 1. What is Vibe Coding?

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
>
> — Andrej Karpathy, February 2025

### Traditional vs Agentic Development

| | Traditional Development | Agentic Development |
|---|---|---|
| **Who writes code** | Human writes every line of code | Human specifies intent via tests, specs, and CLAUDE.md |
| **Implementation** | Human handles all implementation details | Agent implements code to match the specification |
| **Debugging** | Human debugs, refactors, and iterates manually | Agent self-corrects by reading test failures |
| **Speed bottleneck** | Speed limited by typing and cognitive load | Speed limited by quality of direction, not typing |

**Your job shifts from WRITING code to DIRECTING an exceptionally capable engineer.**

---

## 2. The "Brilliant New Employee" Mental Model

Think of Claude as a **brilliant but brand-new employee** who just joined your team today:

1. **Deep Technical Skills** — Knows Python, PySpark, SQL, FastAPI, React, and hundreds of frameworks — but has zero context on *your* norms, naming conventions, or architecture decisions.

2. **Excels With Clear Direction** — Given a precise spec, produces excellent code. Given a vague request, produces plausible-looking code that misses the mark.

3. **Needs Explicit Context** — Won't infer your team's standards. Needs to be told: "Always PySpark, never pandas." "Snake_case for all columns." "Tests before code."

4. **Benefits From Guardrails** — Concrete examples, test cases, and constraints prevent the agent from over-engineering or going off-track.

**Reframe: You are a TECH LEAD managing a talented engineer through specs, tests, and feedback. Invest time in specs upfront, not in writing code.**

---

## 3. Why Specs Matter — "Garbage In, Garbage Out at 100x Speed"

With AI agents, ambiguous specs don't just waste time — they waste time at **agent velocity**. A vague requirement might be implemented 10 different ways in seconds, all wrong.

### What Makes a Good Spec

1. **Acceptance Criteria** — What must be true when done? Exact expected outputs, not vague descriptions.
2. **Constraints** — What can't be changed? What's off-limits? "Don't modify passing tests." "Use PySpark only."
3. **Data Contracts** — Input/output shapes, types, and examples. Column names, date formats, value ranges.
4. **Test Cases** — Concrete test cases with real values — not prose descriptions of expected behaviour.

> **Tip:** A vague requirement might be implemented 10 different ways in seconds, all wrong. A precise spec produces the right answer on the first try.

---

## 4. CLAUDE.md — Your Team's Operating Manual

CLAUDE.md is a **persistent instruction file** that encodes your team's standards. The agent reads it automatically at the start of every session — no need to repeat yourself.

### Three Scope Levels

| Level | Path | Purpose |
|---|---|---|
| **User-Level** | `~/.claude/CLAUDE.md` | Personal preferences, coding style, editor habits. Applies to all your projects. |
| **Repo-Level** | `./CLAUDE.md` | Team standards, tech stack, architecture decisions. Overrides user-level. Checked into git. |
| **Module-Level** | `./src/CLAUDE.md` | Module-specific rules (e.g., "all files here use `@dp.table`"). Overrides repo-level. |

### Why It Works

- **Self-correcting:** Agent re-reads it each session — no drift
- **Searchable:** Agent can reference specific sections on demand
- **Maintainable:** One file to update, entire team benefits
- **Scoped:** Different rules for different parts of the codebase

### Template Structure

```markdown
# CLAUDE.md — Grocery Intelligence Platform

## Team
- Team Name: TEAM_NAME
- Schema: workshop_vibe_coding.TEAM_SCHEMA

## Project
A data platform that ingests Australian retail
and food price data through a medallion architecture.

## Tech Stack
- Data processing: PySpark (never pandas)
- Pipeline: Lakeflow Declarative Pipelines
- Web backend: FastAPI with Pydantic models
- Deployment: Databricks Asset Bundles

## Data Standards
- Architecture: Bronze → Silver → Gold
- Date columns: YYYY-MM-DD, stored as DATE
- Naming: snake_case for all tables/columns

## Rules
- Always use PySpark, never pandas
- Write tests BEFORE implementation
- Keep solutions minimal

## Project Structure
(directory tree)

## Data Sources
(table with API endpoints)

## Code Mappings
(region codes, industry codes)
```

### Tips for Effective CLAUDE.md

- **Keep it lean:** Aim for ~50 lines. CLAUDE.md consumes context tokens — every line counts.
- **Be specific:** "Always PySpark, never pandas" beats "Use appropriate tools." Concrete rules get followed.
- **Include code mappings:** Region codes, industry codes, enum values — anything the agent needs for lookups.

> **Warning:** Don't dump everything in. CLAUDE.md is not documentation. It's a set of standing orders. If a rule isn't referenced often, it belongs in a separate doc the agent can read on demand.

### What NOT to Include

- Long explanations or tutorials
- Full API documentation (link to it instead)
- Implementation details that change frequently
- Anything already in your test suite

### Exercise: Write Your Team's CLAUDE.md

Open your Coding Agents terminal and paste the prompt below. Replace `<team_schema>` with your assigned schema name.

```text
Create a CLAUDE.md for a grocery intelligence platform.

Tech stack: PySpark, Lakeflow Declarative Pipelines, FastAPI + React,
Databricks Asset Bundles (DABs).

Data sources: ABS SDMX APIs, FSANZ web scraping, ACCC PDF ingestion
via UC Volumes.

Unity Catalog namespace: workshop_vibe_coding.<team_schema>.

Include:
- Team name and schema
- Tech stack with explicit constraints (PySpark not pandas)
- Data standards (medallion architecture, date formats, naming)
- Rules (TDD, minimal solutions, don't change passing tests)
- Project structure (src/bronze, src/silver, src/gold, tests/, app/)
- Data sources table with API endpoints
- Code mappings for region and industry codes
```

**This is the most important 5 minutes of the workshop — everything else builds on this.**

> **After generating:** Read through the CLAUDE.md and edit anything that doesn't match your team's preferences. Add your team's chosen angle (Retail Performance, Food Inflation, etc.) to the Project section.

---

## 5. Test-Driven Development with Agents

### The TDD + Agent Workflow

```
STEP 1              STEP 2              STEP 3              STEP 4
Human writes    →   Agent implements →   Run & iterate   →   Human reviews
the test            code to pass         (agent self-        & accepts
                                         corrects)
```

**The Test IS the Spec.** Unlike prose specs, a test is executable, unambiguous, and either passes or fails.

### Why This Works

- **Step 1 (Human writes test):** You define "done" in code, not prose. No interpretation debate.
- **Step 2 (Agent implements):** Agent has a clear, unambiguous target to code against.
- **Step 3 (Run & iterate):** Agent reads failure messages, fixes code, re-runs — no human review bottleneck.
- **Step 4 (Human reviews):** You review working, tested code — not speculative drafts.

### The Compound Effect

Each passing test **constrains** the next implementation. The agent can't break existing tests while adding new features.

This creates a **ratchet effect**: quality only goes up, never down. Every green test is permanent progress.

> **If you take one thing from today:** write the tests first. Always.

### Why TDD Is Exponentially More Powerful With Agents

1. **Unambiguous Specifications** — A test says exactly what the code must do. No room for interpretation, no "I thought you meant..." The agent reads the assertion and knows the target.
2. **Self-Correcting Loop** — The agent reads the failure message, understands what went wrong, and fixes it automatically. No waiting for human review on each iteration.
3. **Guardrails** — Existing passing tests prevent the agent from accidentally rewriting working code. New code must pass new tests *without* breaking old ones.
4. **Faster Iteration** — The agent can run tests, fix, and re-run in seconds. No human bottleneck for the first pass. You review working code, not speculative drafts.

### Writing Tests That Guide — Given / When / Then

```python
def test_clean_retail_data(spark):
    # GIVEN: Raw data with 10 rows, 2 invalid
    raw_data = spark.createDataFrame([
        ("2024-01-15", 1000, "NSW"),
        ("2024-01-16", None, "VIC"),
        ("invalid",    2000, "QLD"),
        ("2024-01-17", 1500, "NSW"),
        ("2024-01-18", 900,  "VIC"),
        ("2024-01-19", 1100, "QLD"),
        ("2024-01-20", 1300, "NSW"),
        ("2024-01-21", None, "SA"),
        ("2024-01-22", 800,  "WA"),
        ("2024-01-23", 1200, "TAS"),
    ], ["date", "price", "state"])

    # WHEN: Clean function applied
    result = clean_transactions(raw_data)

    # THEN: Invalid rows removed
    assert result.count() == 8
    assert result.filter("price IS NULL").count() == 0
```

### Key Test Principles

- **Concrete Values** — Use real data: actual state codes, valid dates, realistic dollar amounts. Not mocks or abstract placeholders.
- **Small Datasets** — 5-10 rows per test. Enough to cover happy path + edge cases. Easy to reason about.
- **Descriptive Names** — `test_silver_decodes_region_codes` not `test_transform`. The name tells the agent what to build.
- **Multiple Assertions** — Check row count, column names, specific values, and null handling. Each assertion is a constraint.

---

## 6. Anthropic's Best Practices

### #1: Give Claude a Way to Verify Its Work

The agent needs a **feedback loop** — a way to check if its output is correct without asking you.

- **Tests:** pytest, unit tests, integration tests
- **Screenshots:** visual verification of UI changes
- **Expected outputs:** "this query should return 42"
- **Diff comparisons:** "output should match this template"

> **Self-correcting:** Agent reads failure, fixes, re-runs. Scales without human review bottleneck for each iteration.

> "Give Claude a way to verify its work."
>
> — Anthropic's #1 Best Practice for Agentic Development

### #2: Explore First, Plan, Then Code

Don't ask the agent to implement immediately. Follow a three-phase approach:

1. **Explore:** Read relevant code, understand existing patterns, check what's already there
2. **Plan:** Use `/plan` mode or `ultrathink` to align on approach before writing code
3. **Code:** Implement with full context — agent knows what exists, what to change, what to preserve

> **Why this works:** Prevents over-engineering and hallucinations. The agent builds on what exists rather than speculating about what might exist.

---

## 7. Understanding Context Windows

**Context Window = RAM.** When it fills up, older context gets evicted.

### What Are Tokens?

A **token** is the basic unit of text for an LLM — roughly 3/4 of a word, or about 4 characters. Everything the agent reads and writes is measured in tokens.

### Token Scale

| Content | Approximate Tokens |
|---|---|
| One sentence | ~8 tokens |
| Your CLAUDE.md (~50 lines) | ~500 tokens |
| 200-line Python file | ~2,500 tokens |
| Claude's context window | 200,000 tokens |
| Harry Potter series (all 7 books) | ~1,100,000 tokens |

Context window = RAM. It holds everything the agent can "remember" in one session. When it fills up, older context gets evicted (compacted) and the agent may forget earlier decisions.

> **Mental model:** If the Harry Potter series is ~1.1M tokens, Claude's context window holds roughly 1/5 of that — enough to hold the first two books. That's a lot, but it's not infinite. Every file read, every tool result, and every conversation turn consumes tokens.

### Managing Your Context Window

#### Context Budget Breakdown

| Category | Budget |
|---|---|
| CLAUDE.md & setup | ~20% |
| File reads & tool results | ~25% |
| Conversation turns | ~20% |
| Agent responses | ~20% |
| Safety margin | ~15% |

#### Four Strategies

1. **Keep CLAUDE.md Lean** — ~50 lines. Every line consumes tokens every session. Put verbose docs elsewhere.
2. **Be Specific** — "Fix the test in test_pipeline.py::test_silver" not "write some code." Target files, not vague asks.
3. **Plan Before Building** — Use `/plan` mode. Alignment upfront prevents expensive rework that wastes context.
4. **New Sessions for New Tasks** — Context is RAM. When switching tasks, start fresh with `/clear` or a new session.

---

## 8. Skills & MCP

### Skills — Slash Commands for Agents

Skills are **reusable agent capabilities** triggered by slash commands. They encode domain knowledge and multi-step workflows into a single invocation.

A skill is a Markdown file that defines a multi-step workflow. When you type `/commit`, the agent:

1. Reads git status and diff
2. Analyzes changes and drafts a commit message
3. Stages files and creates the commit
4. Runs git status to verify success

#### Built-In Examples

```bash
# Common skills
/commit     # Smart git commit with message
/review-pr  # Review a pull request
/test       # Run tests intelligently

# Custom skills you can create
/deploy-dab # Validate + deploy DABs bundle
/check-data # Query tables, verify counts
```

#### Why Skills Matter

- **Automate Repetitive Patterns** — Workflows you do 10x/day become one command. No re-explaining each time.
- **Encode Team Conventions** — Your team's commit message format, deploy steps, and review checklist — codified once, used by everyone.
- **Reduce Context Usage** — A skill runs a pre-defined workflow without you needing to type out multi-step instructions each time.

> **Workshop tip:** You can create custom skills during the labs. Think about which multi-step workflows you repeat most often.

### MCP — "USB-C for AI"

**Model Context Protocol (MCP)** is a standard protocol for connecting AI agents to external tools and data sources. Instead of the agent guessing, it can call real APIs.

#### Three Types of MCP Servers

**Managed (Built-In)**
Pre-integrated with Databricks:
- Unity Catalog tables
- Vector Search
- Genie spaces
- DBSQL warehouses

**External (via Proxies)**
Community-built integrations:
- GitHub (PRs, issues)
- Slack (messages, channels)
- Glean (internal search)
- JIRA (tickets, sprints)
- Databricks Docs

**Custom (Org-Specific)**
You build them for internal tools:
- Internal APIs
- Data quality tools
- Monitoring systems
- Hosted on Databricks Apps

**Without MCP, the agent guesses. With MCP, it knows.**

> **Key benefit:** Agents access ANY tool through a standard protocol. Credentials stay secure in Unity Catalog — the agent never sees raw tokens or passwords.

---

## 9. Genie & AI/BI Dashboards

### Genie: Natural Language on Your Data

Business users ask questions in plain English. Genie generates SQL, runs it, and returns results with visualizations.

```sql
-- User asks:
-- "Which state had the highest food retail turnover in 2024?"

-- Genie generates:
SELECT state,
       SUM(turnover_millions) AS total
FROM gold.retail_summary
WHERE year = 2024
GROUP BY state
ORDER BY total DESC
LIMIT 1
```

**How to set up:** Point Genie at your gold tables, add column descriptions, and provide example queries in the instructions.

### AI/BI Dashboards

Auto-generated dashboards that understand your data. Describe a visualization in natural language and it generates the chart.

- "Show monthly revenue by state as a line chart"
- "Compare food CPI across states as a bar chart"
- "Display year-over-year growth as a heatmap"

**How they complement each other:**
- **Dashboards** = recurring views, standard KPIs, shared with stakeholders
- **Genie** = ad-hoc questions, exploration, self-serve analytics

Both feed from the same **gold tables** — the output of your data pipeline. Good gold tables = good Genie + dashboards.

---

## 10. Practical Tips — Preventing Common Pitfalls

### Overengineering

Agent generates a framework when you asked for one function. Adds features you didn't request.

- **Symptom:** "I asked for a function and got an entire module with abstract base classes."
- **Fix:** "Keep it minimal. Do not add features beyond what is requested. One function, not a framework."

### Hallucinations

Agent speculates about code it hasn't read. Invents API endpoints, column names, or function signatures.

- **Symptom:** "The agent used a column name that doesn't exist in the data."
- **Fix:** "Never speculate about code you have not opened. Read the file first, then make changes."

### Going Off-Rails

Agent runs unchecked for 10 minutes, making changes you didn't approve. Rewrites working code.

- **Symptom:** "I looked away for 5 minutes and the agent rewrote half the project."
- **Fix:** Check in every 2-3 tool calls. Steer early. "Don't change functions that already pass tests."

---

## 11. Agent Steering Phrases (Cheatsheet)

| When the agent... | Say this |
|---|---|
| **Uses pandas instead of PySpark** | "Rewrite this using PySpark. We never use pandas in this project." |
| **Ignores your CLAUDE.md** | "Read CLAUDE.md first, then try again." |
| **Rewrites working code** | "Don't change functions that already pass tests. Only fix the failing ones." |
| **Writes code before tests** | "Stop. Write the tests first, then implement." |
| **Generates something too complex** | "Simplify. I just need [specific thing]. No extra features." |
| **Gets stuck in a loop** | "Stop. Let's try a different approach. [describe what you want]" |
| **Speculates about code** | "Read the file first. Don't guess what's in it." |
| **Goes silent / takes too long** | "What are you working on? Show me your current approach." |

**Healthy cadence:** Agent makes 2-3 tool calls → You review output → Steer if needed → Continue

> **The key habit:** Treat agent interaction like a code review conversation, not a fire-and-forget request. Short feedback loops produce better results than long unsupervised runs.

---

## 12. The Medallion Architecture

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│     Bronze        │     │     Silver        │     │      Gold        │
│   Raw Ingestion   │ ──→ │ Cleaned & Enriched│ ──→ │  Analytics-Ready │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### Bronze (Raw)

- Ingest data as-is from APIs and files
- No transformations applied
- Preserves original column names and types
- Acts as an immutable audit trail
- Use `@dp.table` with data quality expectations

### Silver (Cleaned)

- Decode codes to readable names
- Handle nulls and invalid rows
- Standardize date formats and types
- Rename columns to snake_case
- Use `@dp.table` reading from bronze

### Gold (Aggregated)

- Roll up and aggregate metrics
- Join across data sources
- Calculate KPIs (YoY growth, rolling averages)
- Ready for Genie and AI/BI dashboards
- Use `@dp.materialized_view`

> **Why medallion?** Separation of concerns. Each layer has one job. Bugs are easy to trace. Silver and gold can be rebuilt from bronze at any time.

---

## 13. Quick Reference

### Key Commands

```bash
# Check environment
databricks auth status
claude --version

# Run tests (always use -x for fail-fast)
pytest tests/ -x
pytest tests/test_pipeline.py -k "bronze" -x
pytest tests/test_pipeline.py -k "silver" -x
pytest tests/test_app.py -x

# Deploy with Databricks Asset Bundles
databricks bundle validate
databricks bundle deploy -t dev
databricks bundle run grocery-intelligence-TEAM -t dev

# Deploy web app
cd app && databricks apps deploy \
  --name grocery-app-TEAM \
  --source-code-path ./
```

### Key Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | Agent instructions (team standards) |
| `tests/conftest.py` | PySpark test fixtures |
| `src/bronze/` | Raw data ingestion |
| `src/silver/` | Cleaned transformations |
| `src/gold/` | Aggregated analytics |
| `app/app.py` | FastAPI web application |
| `databricks.yml` | DABs deployment config |

### Checkpoint Recovery

No shame in using checkpoints — the goal is a working demo!

Tell the agent:

```text
Copy the checkpoint tables from workshop_vibe_coding.checkpoints
into my schema workshop_vibe_coding.<team_schema>
```

### Recommended Agent Workflow

Explore data → Write tests → Implement → Run tests → Fix → Deploy. **Never skip the test step.**

---

## Key Takeaways

1. **Write clear specs** — CLAUDE.md, tests, and PRDs define what "done" looks like. The agent can only be as good as your specification.
2. **Use tests as executable specs (TDD)** — Tests are unambiguous. They pass or they fail. No interpretation required. Write them first, always.
3. **Give agents verification mechanisms** — Tests, screenshots, expected outputs. The agent needs a feedback loop to self-correct without human intervention.
4. **Manage context windows** — Keep CLAUDE.md lean (~50 lines), be specific with requests, use new sessions for new tasks.
5. **Steer early and often** — Review every 2-3 tool calls. Short feedback loops produce better results than long unsupervised runs.

**Think of yourself as a director, not a typist.**

> **Monday morning action:** Create a CLAUDE.md for your team's main repository. Start with tech stack, coding standards, and 5 rules. Iterate from there.

> **The discipline transfers:** These practices work with Claude Code, Cursor, Windsurf, GitHub Copilot, and any agentic coding tool. The discipline is the differentiator, not the tool.
