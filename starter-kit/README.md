# Starter Kit

Everything you need to get started. Follow these steps in order.

## Setup (5 minutes)

1. **Copy CLAUDE.md** to your project root:
   ```bash
   cp starter-kit/CLAUDE.md ./CLAUDE.md
   ```
   Then edit `CLAUDE.md` and replace `TEAM_SCHEMA` with your team schema (e.g., `team_01`)

2. **Copy test files** to your tests directory:
   ```bash
   mkdir -p tests
   cp starter-kit/conftest.py tests/
   cp starter-kit/test_pipeline.py tests/
   ```

3. **Copy config templates**:
   ```bash
   cp starter-kit/databricks.yml.template ./databricks.yml
   cp starter-kit/app.yaml.template ./app.yaml
   ```
   Replace `TEAM_NAME` and `TEAM_SCHEMA` placeholders in both files.

## During the Labs

4. **Follow the prompts** in `starter-kit/prompts/` — they're numbered in order:
   - `01` through `05` = Lab 1 (Data Pipeline)
   - `06` through `11` = Lab 2 (App + Dashboard)
   - Each prompt is exact copy-paste into Claude Code

5. **If stuck**, check `starter-kit/cheatsheet.md` for quick fixes

## What's in Here

| File | What it is |
|------|-----------|
| `CLAUDE.md` | Project instructions for the AI agent — drop into project root |
| `conftest.py` | pytest fixtures with SparkSession and sample data |
| `test_pipeline.py` | Lab 1 test stubs (pipeline tests) |
| `test_app.py` | Lab 2 test stubs (API tests) |
| `databricks.yml.template` | Databricks Asset Bundle config |
| `app.yaml.template` | Databricks Apps deployment config |
| `cheatsheet.md` | Quick fixes for common problems |
| `prompts/01-11` | Exact copy-paste prompts for every lab step |
