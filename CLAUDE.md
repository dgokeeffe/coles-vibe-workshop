# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Workshop materials for a 7-hour Coda vibe coding workshop (10:00 AM – 5:00 PM, lunch 12:00–13:00). **Pairs** (driver/navigator, 15-min swaps — not teams of 2–3) build a Grocery Intelligence Platform using AI coding agents on Databricks. Three parallel tracks: Data Engineering, Data Science, and Analyst.

The workshop's meta-framework is **R.V.P.I.** — Research → Validate → Plan → Implement. The "V" is the step most other agent workflows skip: audit retrieved context (CLAUDE.md, past memory, research output) before planning on top of it. See `notes/rvpi-validate-step.md` for the full framework.

## Directory Guide (for coding agents)

This repo contains **three codebases**. When acting inside any of them, stay in that scope — do not cross-edit.

| Directory | Role | Who edits it |
|-----------|------|--------------|
| `reference-implementation/` | Facilitator answer key — the DE-track lab built out end-to-end. Also powers the 10:15 opener demo. | Facilitator only. Participants read but never modify. |
| `starter-kit/` | Participant scaffold — track-specific CLAUDE.md, prompts, test stubs. | Participants (this is what pairs work in during labs). |

All other top-level content is workshop material: slides (`slides.html`), track workbooks (`track-*.html`), lab briefs (`LAB-*.md`), and facilitator docs (`FACILITATOR-*.md`, `WORKSHOP-*.md`). Each codebase has its own `CLAUDE.md` with a scope banner — read it first on entry.

## Build & Export Commands

```bash
# Generate shareable PDFs from track HTML workbooks (requires Node.js)
npm install puppeteer pdf-lib --silent
cp ~/.claude/plugins/cache/fe-vibe/fe-html-slides/*/skills/html-slides/resources/export-pdf.js .
node export-pdf.js track-common.html   # → track-common.pdf
node export-pdf.js track-de.html       # → track-de.pdf
node export-pdf.js track-ds.html       # → track-ds.pdf
node export-pdf.js track-analyst.html  # → track-analyst.pdf

# Run reference implementation tests (requires PySpark)
cd reference-implementation && uv run pytest tests/test_pipeline.py -x --no-header -q
cd reference-implementation && uv run pytest tests/test_quality.py -x --no-header -q
cd reference-implementation && uv run pytest tests/test_app.py -x --no-header -q
```

## Workshop Schedule (10:00–17:00)

- **10:00** Opener — why this matters, end-output teaser (10 min)
- **10:10** Internal Demo — coding agents at Databricks + live pipeline/dashboard (15 min)
- **10:40** Break (10 min)
- **10:50** Get-to-know-Claude — R.V.P.I., CLAUDE.md, Small Steps, Power Tools, BDD, Sycophancy, Context (70 min)
- **12:00** Lunch (60 min)
- **13:00** Challenge brief + pair formation + Lab 1 briefing (15 min)
- **13:15** Lab 1 — track-specific, pairs (90 min)
- **14:45** Show & Tell (15 min)
- **15:00** Break (10 min)
- **15:10** Lab 2 — track-specific, pairs (80 min)
- **16:30** Team demos + Let Go + Takeaways + Hackathon + Close (30 min)

## Six Files Must Stay In Sync

When changing workshop content, update all six:
1. `WORKSHOP-TRANSCRIPT.md` — **single source of truth**: hybrid prose + slide cue bullets for the day's narrative. Added 2026-04-19; drives everything else.
2. `slides.html` — the deck attendees see. 53 slides, `aria-label="Slide N: ..."` format. Speaker notes in `data-notes` attributes; press **N** to toggle the overlay.
3. `FACILITATOR-SCRIPT.md` — dot-point cue cards per slide / per block
4. `WORKSHOP-PLAN.md` — master plan with session details and timing
5. `VIBE-CODING-GUIDE.md` — markdown version of common track theory content
6. `track-common.html` — HTML workbook version of the same content

> **Note:** `slides-facilitator.html` was previously a twin deck with JS-injected notes from `data-notes`. Removed 2026-04-19 — the same `data-notes` now live on `slides.html` and the press-N overlay covers the use case without the drift risk of maintaining two files. If you need a plain-text notes dump, grep `data-notes="` out of `slides.html`.

The three track HTMLs (`track-de.html`, `track-ds.html`, `track-analyst.html`) pull content from the corresponding lab markdown files (`LAB-1-DE.md`, `LAB-2-DE.md`, etc.) and must stay aligned with them.

## Slide Deck Conventions

Single HTML files with no build step. Open directly in a browser.

**Slide structure:** Each slide is a `<section class="slide">` with `aria-label` (title) and `data-notes` (speaker notes). Follow the `<!-- SLIDE N: TITLE -->` comment convention.

**CSS variables:** Databricks brand in `:root` — `var(--db-lava)` #FF3621, `var(--db-navy)` #1B3139, `var(--db-teal)` / `var(--db-green)` #00A972, `var(--db-oat)` #F9F7F4. Coda accent `var(--coda-red)` #DB2777 used sparingly.

**Code blocks:** `<div class="code-block">` with `<span class="keyword|string|comment|function|type|decorator">` for syntax highlighting. `white-space: pre` — preserve indentation in HTML source.

**PDF export:** Uses Puppeteer to screenshot each `.slide` section at 1920×1080 @2x, then pdf-lib stitches into PDF. This is why all exportable HTML files must use `<section class="slide">` elements.

## Track Workbook Conventions

The `track-*.html` files are slide-format workbooks (not presentation decks). Each uses the same `.slide` structure for PDF export compatibility but styled as document pages with:
- `.cover-slide` — dark themed title page
- `.divider-slide` — section dividers with timing badges
- `.page-slide` — white content pages with `.page-header`, `.page-content`, `.page-footer`

Track accent colors: DE = lava red (#FF3621), DS = purple (#7c3aed), Analyst = cyan (#0891b2), Common = green (#00A972).

## Three-Track System

After shared theory (10:50–12:00 Get-to-know-Claude block) and lunch, pairs choose one track at 13:00:

| Track | Badge Color | Lab 1 | Lab 2 | Lab Files |
|-------|------------|-------|-------|-----------|
| Data Engineering | Red | Lakeflow pipeline (Bronze→Silver→Gold) | Data quality, FSANZ source, scheduling | `LAB-1-DE.md`, `LAB-2-DE.md` |
| Data Science | Purple | Feature engineering, MLflow experiments | Model training, serving, prediction app | `LAB-1-DS.md`, `LAB-2-DS.md` |
| Analyst | Cyan | Genie spaces, AI/BI dashboards | FastAPI web app with embedded dashboards | `LAB-1-ANALYST.md`, `LAB-2-ANALYST.md` |

## Reference Implementation

`reference-implementation/` contains the complete DE track solution built following Anthropic best practices (CLAUDE.md → tests → implementation). It serves as the facilitator answer key and teaching artifact. 55 tests across three files: `test_pipeline.py` (bronze/silver/gold), `test_app.py` (FastAPI), `test_quality.py` (data validation). Pipeline uses `import databricks.declarative_pipelines as dp` with `@dp.table` decorators and `@dp.expect` / `@dp.expect_or_fail` quality rules.

## Content Alignment

The canonical working implementation lives in `reference-implementation/` — a Databricks Asset Bundle with Lakeflow pipelines ingesting ABS Retail Trade, ABS CPI Food, FSANZ Food Recalls, and ACCC Grocery PDFs. Lab instructions, slide content, and pipeline flow diagrams must stay aligned with that directory's actual data sources, table names, and schemas.
