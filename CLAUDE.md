# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Workshop materials for a 5-hour Coles Group vibe coding hackathon. Teams of 2-3 build a Grocery Intelligence Platform using AI coding agents on Databricks.

## Repository Structure

- `slides.html` — Main presentation deck (single-file HTML with inline CSS/JS, scroll-snap slides)
- `slides-facilitator.html` — Same deck with visible speaker notes panels and timing badges (JS-injected from `data-notes` attributes)
- `WORKSHOP-PLAN.md` — Master plan: agenda, session details, lab phases, timing, discussion questions
- `FACILITATOR-SCRIPT.md` — Dot-point cue cards for the presenter (not prose — bullet points with stage directions)
- `FACILITATOR-GUIDE.md` — Reference guide: checklist, answers, timing buffers, lab facilitation notes
- `LAB-1-DATA-PIPELINE.md` — Lab 1 instructions: Lakeflow pipeline with TDD (Bronze → Silver → Gold)
- `LAB-2-APP-GENIE-DASHBOARD.md` — Lab 2 instructions: FastAPI + React app, Genie space, AI/BI dashboard
- `PRE-WORKSHOP-SETUP.md` — Infrastructure setup guide for Coles platform team
- `quick-reference.html` — Cheat sheet for participants

## Slide Deck Conventions

The deck is a single HTML file with no build step. Open `slides.html` directly in a browser.

**Slide structure:** Each slide is a `<section class="slide">` with:
- `aria-label` — slide title (used for navigation)
- `data-notes` — full speaker notes (consumed by facilitator JS and extracted into FACILITATOR-GUIDE.md)
- Theme class: `slide-dark` (navy bg), `slide-light` (oat bg), `slide-white` (white bg)
- Content wrapped in `<div class="reveal">` for entrance animations

**CSS theme variables:** Databricks brand colours defined in `:root` — use `var(--db-lava)`, `var(--db-navy)`, `var(--db-teal)`, `var(--db-green)`, `var(--db-oat)`. Coles red (`var(--coles-red)`) used sparingly for co-branding.

**Code blocks:** Use `<div class="code-block">` with `<span class="keyword|string|comment|function|type">` for syntax highlighting. The class has `white-space: pre` — preserve indentation in HTML source.

**Adding slides:** Insert a new `<section class="slide">` between existing ones. Include `aria-label` and `data-notes`. Follow the `<!-- SLIDE N: TITLE -->` comment convention. After adding to `slides.html`, also add to `slides-facilitator.html` and update `FACILITATOR-SCRIPT.md`.

## Content Alignment

The workshop references a working implementation at `~/Repos/coles-genie-demo` — a Databricks Asset Bundle with Lakeflow pipelines ingesting ABS Retail Trade, ABS CPI Food, FSANZ Food Recalls, and ACCC Grocery PDFs. Lab instructions, slide content, and pipeline flow diagrams must stay aligned with that repo's actual data sources, table names, and schemas.

## Four Files Must Stay In Sync

When changing workshop content, update all four:
1. `slides.html` — the deck attendees see
2. `slides-facilitator.html` — the deck with notes (same slides + JS overlay)
3. `FACILITATOR-SCRIPT.md` — dot-point cue cards per slide
4. `WORKSHOP-PLAN.md` — master plan with session details and timing

## Workshop Sessions

- **Session 1** (Thinking in Specs): CLAUDE.md, PRDs, "brilliant new employee" framing
- **Session 2** (TDD + Agents): TDD workflow, writing tests, context windows, subagents vs teams
- **Lab 1**: Build Lakeflow pipeline from 4 data sources (55 min)
- **Session 3** (Beyond the Basics): Skills, MCP, Genie, AI/BI dashboards
- **Lab 2**: FastAPI + React app, Genie space, AI/BI dashboard (55 min)
- **Appendix slides** exist after the closing slide for overflow topics (MCP architecture detail, AI Dev Kit)
