# Demo Sidebar: Fresh-Context `/review` on a Team's Code

**When:** Lab 1, approximately minute 40 (~12:45 PM)
**Duration:** 90 seconds
**Style:** Live (but pre-selected — see setup)
**Pre-flight:** Walk the room minutes 30–38, identify one team whose silver or gold transformation is complete, working, and the team seems comfortable being spotlighted. Ask them: *"Mind if I run `/review` on your silver layer on the big screen for 90 seconds as a demo?"*

---

## Purpose

Teach **subagents** by *using* one in front of the room. The Power Tools slide (21) describes subagents abstractly; this demo shows one running against code attendees just wrote. One team gets real feedback; the room learns what `/review` actually does.

---

## The Script (90 seconds)

### Opening (15 sec)

Walk to the spotlighted team's driver:

> "[Team name] just finished their silver transformation — mind if I borrow the screen for 90 seconds? I want to show the room something."

Switch projector to their terminal.

### Launch `/review` (15 sec)

> "Remember the Power Tools slide — subagents run in fresh context. I can ask one to review this code without polluting the main session. Watch."

```
/review src/silver/retail_turnover.py
```

### Narrate what happens (50 sec)

The subagent will output structured feedback. While it runs, explain:

> "This is a separate Claude instance. It doesn't know what this team prompted earlier, doesn't know their CLAUDE.md quirks, doesn't know where the agent got stuck. **It just reads the code cold.** That's the point — it can't rubber-stamp decisions it helped make."

When output arrives, read 2–3 findings aloud:

> "Look — it flagged the REGION code decoding is missing the null case. It noticed turnover_millions doesn't have a type hint. It's asking whether you considered using a broadcast join."
>
> "This team didn't ask it those questions — it asked on its own, because fresh context means fresh scrutiny."

### Key message (10 sec)

> "If your silver or gold feels 'done' — run `/review` before you move on. It's cheap, it's fast, and it catches the stuff the main agent agreed with you on. Back to your labs."

---

## Fallback — if the team declines or `/review` fails

Don't force it. Fall back to:

> "I was going to show `/review` on one of your silver transformations — [team] was my volunteer. Run it yourselves when you're ready: `/review src/silver/<your_file>.py`. It's a subagent with fresh context. It'll catch what the main agent didn't."

Then skip to Lab 2 normally — do NOT eat lab time trying to fix the demo.

---

## Why this demo

- Demonstrates subagents *concretely* — the slide described them, this shows them working
- Social proof — one team's real code gets real feedback
- Reinforces the Sycophancy defence — fresh context is how you get uncontaminated scrutiny
- Creates an immediate "I should do this" moment for the other teams

## What NOT to do

- Don't pick a team that's clearly struggling (feels like public shaming)
- Don't read every finding — pick 2–3, keep it fast
- Don't let it turn into a teaching session on what the findings mean — that's for Q&A later
- Don't skip asking consent — always check with the team first
