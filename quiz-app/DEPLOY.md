# Deploying the Quiz-App as the Workshop Icebreaker

> **Role in the workshop:** Block 3 (10:25–10:40) live team-scoring quiz, with prediction reveal at Show & Tell (14:45) using Lab 1 Gold tables. Replaces the retired prediction-card icebreaker.

## Prerequisites

- Databricks CLI authenticated to the target workspace:
  ```bash
  databricks current-user me
  ```
- App-creation permission in the target workspace
- This folder (`quiz-app/`) checked out locally

## Option A — Deploy as a Databricks App (recommended for the workshop)

Databricks Apps gets you SSO, a stable URL, HTTPS, and a shareable link the room can hit from phones.

```bash
cd /Users/david.okeeffe/Repos/coles-vibe-workshop/quiz-app

# 1. Create the app (one-time, per workspace)
databricks apps create vibe-quiz \
  --description "Grocery Data Quiz — icebreaker for the vibe workshop"

# 2. Sync the source (re-run after any code change)
databricks sync . /Workspace/Users/$(databricks current-user me | jq -r .userName)/vibe-quiz \
  --full

# 3. Deploy
databricks apps deploy vibe-quiz \
  --source-code-path /Workspace/Users/$(databricks current-user me | jq -r .userName)/vibe-quiz

# 4. Grab the URL
databricks apps get vibe-quiz | jq -r '.url'
```

The URL will look like `https://vibe-quiz-<hash>.<region>.databricksapps.com`.

## Option B — Run locally, project the laptop screen

Faster but the room can't join from phones. Useful only if Option A fails on the day.

```bash
cd quiz-app
uv sync
uv run uvicorn app:app --host 0.0.0.0 --port 8000
```

The facilitator laptop projects to the room; teams shout answers.

## Day-of checklist

- [ ] App deployed (Option A) and URL opens in Chrome on a test phone — confirm SSO flow doesn't block external attendees (may need to switch app auth to `public` for the day)
- [ ] Generate a QR code pointing at the app URL. Any QR generator is fine; save the PNG to `slides.html`'s `images/` folder as `quiz-app-qr.png` (or base64-embed it into Slide 9)
- [ ] Replace the placeholder `<div style="background:white;...">QR CODE</div>` in Slide 9 with an `<img src="images/quiz-app-qr.png">` (or a data URI)
- [ ] Replace placeholder text `quiz.coles-vibe.app` with the real `vibe-quiz-<hash>.databricksapps.com` URL on Slide 9
- [ ] Pre-load 5–10 trivia questions aligned with what Lab 1 Gold tables will answer at Show & Tell. Keep the prediction questions (state with highest food turnover, CPI increase since 2020, peak retail month, fastest-rising food category) so Slide 36 (Show & Tell) can reveal from live Gold tables.
- [ ] Warm the app before the workshop: hit the URL, step through one round solo, confirm SSE live-updates work in Chrome

## Runtime during the workshop

- Project the quiz-app admin view on the main screen (use the `?admin=1` query parameter or keyboard shortcut — check `app.py` for the admin trigger)
- Teams join on their phones, pick a team name, play live
- At Show & Tell (14:45), run the Lab 1 Gold-table queries against the quiz prediction questions — reveal answers and highest-accuracy team wins

## Rollback / emergency

If the app fails at 10:25:
1. Skip the quiz-app slide (press arrow to Slide 10, Techniques divider)
2. Announce "quiz got eaten by DNS — we'll do prediction cards instead"
3. Fall back to the old prediction-card list (5 questions), verbally ask teams to raise hands — same prediction-reveal logic still works with Lab 1 Gold tables
4. Add a post-mortem TODO: redeploy the app and test SSO flow with a non-Databricks email

## What the quiz-app is (for the speaker notes on Slide 9)

- Built in one weekend with Claude Code
- FastAPI + Server-Sent Events for live score updates
- Zero external deps except FastAPI / uvicorn / sse-starlette
- Question bank in `app.py`; scoring state persists in-memory (restarts wipe it — don't redeploy during the game)
