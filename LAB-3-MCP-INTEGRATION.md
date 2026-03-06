# Lab 3: Supercharge Your Agent with MCP Servers

**Duration:** 45 minutes
**Goal:** Connect Claude Code to external tools via Model Context Protocol (MCP) servers

---

## Scenario

You've built a data pipeline (Lab 1) and a dashboard (Lab 2). But your AI agent is still isolated — it can only read and write code. What if it could also query Databricks documentation, look up table schemas, run SQL queries, and interact with your team's tools — all from natural language?

That's what **MCP (Model Context Protocol)** enables. MCP is an open protocol that gives AI agents "hands" to interact with external systems. In this lab, you'll connect your agent to existing MCP servers and build your own.

**You will direct the AI agent to build and configure everything.**

---

## Step 1: Understanding MCP (10 min)

### 1.1 What is MCP?

MCP (Model Context Protocol) is an open standard that lets AI agents call external tools. Think of it like USB for AI — a universal way to plug in capabilities.

Without MCP, your agent can only:
- Read and write files
- Run shell commands

With MCP, your agent can also:
- Search documentation
- Query databases
- Post to Slack
- Create JIRA tickets
- ...anything you can build an API for

### 1.2 Three tiers of MCP servers

| Tier | Description | Examples |
|------|-------------|----------|
| **Managed** | Built into your platform | Databricks-native tools |
| **External** | Community-built, install yourself | Slack, JIRA, GitHub, Confluence |
| **Custom** | You build them | Your team's internal tools |

### 1.3 Check your current MCP servers

In the terminal, ask Claude Code:

```
Run "claude mcp list" to show me what MCP servers are currently configured.
```

This shows you the servers already available. Note how each server exposes a set of **tools** that the agent can call.

### 1.4 How it works

When you add an MCP server, the agent gains new tools. When you ask a question that matches a tool's capability, the agent automatically calls it. You don't need to specify which tool to use — the agent figures it out from your natural language request.

---

## Step 2: Connect a Databricks MCP Server (15 min)

### 2.1 Add the Databricks Docs MCP server

Ask the agent:

```
Add a new MCP server called "databricks-docs" with this configuration:

Command: npx
Args: -y @anthropic/databricks-docs-mcp-server

Use "claude mcp add" to register it.
```

Verify it's registered:

```
Run "claude mcp list" and confirm databricks-docs appears.
```

### 2.2 Search Databricks documentation

Now test it with real queries. Ask the agent:

```
Search the Databricks docs for how to create a Lakeview dashboard.
```

Notice how the agent calls the MCP server's search tool, retrieves relevant documentation, and synthesizes an answer — all automatically.

### 2.3 Try more queries

```
What Terraform resources are available for Unity Catalog?
```

```
Search the Databricks docs for best practices on medallion architecture.
```

```
What's new in the latest Databricks release notes?
```

### 2.4 Why this matters

Without MCP, the agent would make up answers or ask you to look it up. With the Databricks docs MCP server, it pulls from authoritative sources. This is the difference between a chatbot and a knowledgeable assistant.

---

## Step 3: Build a Custom MCP Server (15 min)

### 3.1 Create the project

Ask the agent:

```
Create a new Python project called "data-tools-mcp" with:
- A server.py file that implements an MCP server
- A pyproject.toml with the "mcp" package as a dependency
- A CLAUDE.md with these rules:
  - Use the mcp Python package (FastMCP) to build the server
  - Use databricks-sql-connector for database queries
  - Connection details come from environment variables
```

### 3.2 Build the MCP server

Ask the agent to implement the server:

```
Build an MCP server in server.py using FastMCP that exposes three tools:

1. get_table_schema(table_name: str) -> str
   - Connects to Databricks SQL
   - Runs DESCRIBE TABLE on the given table
   - Returns the schema as a formatted string
   - Example: get_table_schema("workshop_vibe_coding.raw_data.store_transactions")

2. run_sql_query(query: str) -> str
   - Executes a read-only SQL query against Databricks
   - Returns results as a formatted table (max 50 rows)
   - IMPORTANT: Only allow SELECT statements (reject INSERT, UPDATE, DELETE, DROP)
   - Example: run_sql_query("SELECT * FROM workshop_vibe_coding.raw_data.store_transactions LIMIT 5")

3. get_data_quality_report(table_name: str) -> str
   - Gets row count, column names, null counts per column,
     and min/max for numeric columns
   - Returns a formatted data quality summary
   - Example: get_data_quality_report("workshop_vibe_coding.raw_data.store_transactions")

Use environment variables for connection:
- DATABRICKS_HOST
- DATABRICKS_HTTP_PATH
- DATABRICKS_TOKEN

The server should use stdio transport (the default for Claude Code).
```

### 3.3 Review the code

Read through the generated server. Check:
- Are SQL injection risks handled? (parameterized queries, statement validation)
- Is the `run_sql_query` tool properly restricted to SELECT statements?
- Are errors handled gracefully?

Ask the agent to fix any issues you spot.

### 3.4 Register the MCP server

```
Register this MCP server with Claude Code using:

claude mcp add data-tools \
  --scope project \
  -- uv run python /path/to/data-tools-mcp/server.py

Set these environment variables when adding:
- DATABRICKS_HOST=<your_workspace_url>
- DATABRICKS_HTTP_PATH=<your_sql_warehouse_path>
- DATABRICKS_TOKEN=<your_token>
```

### 3.5 Test your custom MCP server

Restart Claude Code to pick up the new server, then try:

```
Check the schema of the workshop_vibe_coding.raw_data.store_transactions table.
```

```
Run a query to show the top 5 stores by total transaction amount.
```

```
Generate a data quality report for my daily_store_metrics table.
```

Watch the agent use YOUR custom tools to interact with Databricks. This is your MCP server in action.

---

## Step 4: Wrap-up (5 min)

### 4.1 Reflection

Think about what you just did:
- You gave your AI agent the ability to query live databases
- You built a custom tool server in minutes
- The agent automatically knew when and how to use your tools
- No UI, no API gateway, no deployment pipeline — just a Python script and a registration command

### 4.2 Ideas for your team

MCP servers your team could build:
- **Incident response:** Query PagerDuty alerts, check runbooks, post updates to Slack
- **Data catalog:** Search for datasets, check lineage, find table owners
- **CI/CD:** Trigger deployments, check pipeline status, roll back releases
- **Internal APIs:** Wrap any internal REST API as an MCP tool
- **Monitoring:** Query Grafana dashboards, check system health, pull metrics

---

## Success Criteria

- [ ] Databricks Docs MCP server added and working
- [ ] Successfully queried Databricks documentation via the agent
- [ ] Custom MCP server built with three tools
- [ ] Custom MCP server registered with Claude Code
- [ ] Agent successfully used custom tools to query live data
- [ ] SQL injection protection in place for the query tool

## Bonus Challenges (if time permits)

1. **Add a fourth tool:** `compare_tables(table_a, table_b)` that compares schemas and row counts between two tables
2. **Add caching:** Cache schema lookups so repeated calls are instant
3. **Add a Slack MCP server:** Connect the Slack MCP server and have the agent post your data quality report to a channel
4. **Chain it together:** Ask the agent to "check data quality on my gold table and if there are any issues, search the Databricks docs for how to add data quality constraints"

## Reflection Questions

1. How does MCP change what's possible with an AI coding agent?
2. What internal tools would benefit most from MCP integration?
3. What security considerations arise when giving an agent access to live databases?
4. How does the custom MCP server compare to building a traditional API?
