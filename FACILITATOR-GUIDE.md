# Facilitator's Guide: Vibe Coding Workshop

This is the facilitator's companion for the Coles Vibe Coding Workshop (The Great Grocery Data Challenge). Read it the night before to feel prepared. It covers every slide with timing, speaker notes, pitfalls to watch for, and practical facilitation advice. It also includes lab facilitation notes, discussion answer guides, and a timing buffer plan.

---

## Pre-Workshop Checklist

Complete these **the day before** and verify again **30 minutes before start**:

- [ ] **Databricks workspace access** -- every attendee can log in and see the `workshop_vibe_coding` catalog
- [ ] **Coding Agents terminals** -- each team's browser-based terminal is running and responsive (test a simple command)
- [ ] **Unity Catalog namespace** -- `workshop_vibe_coding.<team_schema>` exists for every team; confirm with `SHOW SCHEMAS IN workshop_vibe_coding`
- [ ] **Checkpoint data loaded** -- `workshop_vibe_coding.checkpoints` contains pre-loaded bronze, silver, and gold tables so no team gets permanently stuck
- [ ] **SQL Warehouse running** -- the workshop warehouse is started and sized appropriately (teams will query concurrently)
- [ ] **ABS APIs reachable** -- test both API endpoints from a Databricks notebook: Retail Trade (`data.api.abs.gov.au/data/ABS,RT,...`) and CPI Food (`data.api.abs.gov.au/data/ABS,CPI,...`)
- [ ] **AI Gateway / Model Serving** -- Claude Opus 4.6 (or whichever model) is routed and responding through AI Gateway
- [ ] **MCP servers configured** -- Databricks MCP server available in Claude Code settings; Databricks Docs MCP reachable
- [ ] **Prediction cards printed** -- one per team, with the 5 ice breaker questions
- [ ] **Timer visible** -- a projected countdown timer (browser tab or phone) for exercises and labs
- [ ] **Backup demo recording** -- pre-record the TDD live demo in case of network or API issues
- [ ] **Room setup** -- teams of 2-3 at shared screens/tables, power strips, Wi-Fi tested
- [ ] **Slide deck loaded** -- open `slides.html` in a browser, test keyboard navigation (arrow keys) and speaker notes (press N)
- [ ] **Genie permissions** -- attendees have CREATE GENIE SPACE permission on the workshop catalog
- [ ] **Databricks Apps permissions** -- attendees can deploy apps

---

## Slide-by-Slide Guide

### Slide 1: Title
- **Time:** 10:00 AM
- **Duration:** ~2 min
- **Key Message:** Set the tone -- this is a 5-hour competitive hackathon, not a lecture. You will leave with skills you can use Monday.
- **Speaker Notes:**
  - Welcome everyone to The Great Grocery Data Challenge
  - Introduce yourself: David O'Keeffe, Solutions Architect at Databricks
  - Thank the Coles Data & AI Engineering team for hosting
  - Set the tone: teams of 2-3 will compete to build the best Grocery Intelligence Platform using real Australian public data
- **What to Watch For:** Latecomers -- have someone greet them and seat them with a team. Energy level -- if the room is quiet, use a louder, more energetic opening.
- **Facilitator Tips:** Stand centre-stage, make eye contact around the room. Keep the intro brief -- people want to get going. Don't linger on logistics yet; save that for the agenda slide.

---

### Slide 2: Ice Breaker -- Grocery Data Predictions
- **Time:** 10:00 AM (immediately after title)
- **Duration:** ~12 min total (including team formation)
- **Key Message:** These predictions connect directly to the data pipeline you will build -- the answers come from querying your own Gold tables later.
- **Speaker Notes:**
  - Hand out prediction cards (one per team)
  - Each team discusses and writes down best guesses -- 30 seconds per question
  - No phones, no Googling! These are about real Australian retail data from the ABS
  - The twist: in Lab 1 they will build the pipeline that ingests this exact data
  - During Show & Tell we will query their Gold tables to reveal the actual answers
  - Teams get scored on accuracy
- **What to Watch For:**
  - Teams that haven't formed yet -- help stragglers find a group
  - Teams spending too long on one question -- keep the pace brisk (30 sec each)
  - Anyone confused about what "ABS data" means -- briefly explain it is Australian Bureau of Statistics public data
- **Facilitator Tips:**
  - Use this as the team formation moment: "Find 1-2 other people, grab a prediction card, you are now a team"
  - Walk around and check teams are writing answers, not just chatting
  - After 5 min of predictions, do a quick round: "Any team want to share a bold prediction?" -- gets energy up
  - The click-to-reveal answers on the slide are for Show & Tell later, not now

**Prediction Card Questions & Answers** (for your reference -- do NOT reveal yet):
1. **Q1:** Which Australian state has the highest monthly food retail turnover? **A:** New South Wales -- ~$3.5B/month
2. **Q2:** By what percentage have Australian food prices (CPI) increased since Jan 2020? **A:** Approximately 25-30%, biggest spike in 2022-23
3. **Q3:** How much does the average Australian household spend on groceries per week? **A:** Around $200-$220/week, up from ~$160 pre-pandemic
4. **Q4:** What month of the year do Australians spend the most on retail? **A:** December -- Christmas shopping spike
5. **Q5:** Which food category has seen the largest price increase since 2020? **A:** Dairy & eggs -- up over 30%

---

### Slide 3: Agenda
- **Time:** ~10:12 AM
- **Duration:** ~2 min
- **Key Message:** This is a 5-hour hackathon with 3 theory sessions and 2 hands-on labs. Teams compete to build the best platform.
- **Speaker Notes:**
  - Walk through the day structure
  - Morning: foundations (paradigm shift, specs, TDD) and pipeline building
  - Afternoon: advanced tools (MCP, subagents, Genie, AI/BI) and app building
  - Breaks are real breaks -- encourage people to step away from screens
  - Encourage questions throughout
- **What to Watch For:** People looking overwhelmed by the agenda -- reassure them that checkpoints exist at every phase so nobody gets permanently stuck.
- **Facilitator Tips:** Point to both columns (Morning and Afternoon) but don't read every item. Highlight the two labs and the demo/voting at the end as the fun parts. Mention breaks explicitly -- people need to know they exist.

---

### Slide 4: Databricks Today
- **Time:** ~10:14 AM
- **Duration:** ~3 min
- **Key Message:** Databricks is no longer just Spark notebooks -- it is the most integrated Data + AI platform. Today you will touch almost every layer.
- **Speaker Notes:**
  - Walk through the platform stack bottom-up: Open formats (Delta Lake, Iceberg, Postgres) -> Unified Governance (Unity Catalog) -> Data layer (Lakehouse, Lakebase, Lakeflow) -> AI with Enterprise Context (Genie) -> Applications (Agent Bricks, AI/BI, Custom Apps)
  - Call out what is NOT in the image: MCP servers are the glue connecting external agents to every layer
  - Proprietary Model Serving routes to Anthropic, OpenAI, Google etc. through AI Gateway
  - Today we are using Claude Opus 4.6 via this exact path
  - Coles callout: today you will use Lakeflow, Unity Catalog, Genie, AI/BI, Custom Apps, MCP, and Model Serving
- **What to Watch For:** People who are unfamiliar with newer Databricks features (Genie, AI/BI, Apps) -- they may have only used notebooks and jobs. Acknowledge this is a lot of new surface area.
- **Facilitator Tips:** Use the image as a visual anchor. Don't try to explain every box -- hit the highlights and say "we will touch most of these today." The Coles callout at the bottom is a good moment to connect the abstract platform to their concrete work.

---

### Slide 5: Section -- The Paradigm Shift
- **Time:** 10:00 AM (section header says 10:00 AM but this is the section marker for the theme)
- **Duration:** ~1 min
- **Key Message:** Software development is changing from writing code to directing agents.
- **Speaker Notes:**
  - Pause briefly at this section divider
  - Ask the room: "Who has used an AI coding tool? ChatGPT? Copilot? Claude?"
  - Get a sense of experience levels
- **What to Watch For:** If almost nobody raises their hand, you will need to go slower on the next few slides. If most people raise their hand, you can move faster.
- **Facilitator Tips:** This is a calibration moment. The show-of-hands tells you how to pitch the next 20 minutes. If the room is experienced, lean into advanced tips. If they are new, spend more time on fundamentals.

---

### Slide 6: What is Vibe Coding
- **Time:** ~10:17 AM
- **Duration:** ~3 min
- **Key Message:** "Vibe coding" is casual shorthand for agentic software development. It is amplification, not replacement -- you still need to know what good code looks like.
- **Speaker Notes:**
  - Read the Karpathy quote aloud
  - Explain: vibe coding is the casual term, but what we are really talking about is agentic software development
  - Key contrast: traditional dev has humans writing every line; agentic dev has humans directing and agents implementing
  - Emphasise: this is amplification, not replacement
- **What to Watch For:** Scepticism -- some engineers may feel threatened or dismissive. Acknowledge both reactions: "It is natural to feel uncertain. Today is about seeing it firsthand and deciding for yourself."
- **Facilitator Tips:** The two-column comparison (Traditional vs. Agentic) is the visual anchor. Linger on "10x amplification, not replacement" -- this is the most important framing for an engineering audience.

---

### Slide 7: Platform Architecture
- **Time:** ~10:20 AM
- **Duration:** ~3 min
- **Key Message:** Everything runs in the browser via a Databricks App -- no local installation required. The architecture is Browser -> Databricks App -> AI Agents -> AI Gateway.
- **Speaker Notes:**
  - Walk through the architecture left to right
  - Browser terminal connects to a Databricks App running Flask
  - The app hosts AI agents (Claude Code / OpenCode)
  - All LLM calls go through AI Gateway for routing, rate limiting, and tracing
  - Mention: 39 pre-built skills, MCP servers for tool access, MLflow for observability
- **What to Watch For:** Questions about security -- "Does the AI have access to our real data?" Clarify that this is a workshop sandbox with public ABS data only.
- **Facilitator Tips:** This is a good moment to say "If you haven't opened your terminal yet, do it now -- we will use it in about 15 minutes."

---

### Slide 8: Section -- Session 1: Thinking in Specs
- **Time:** 10:15 AM
- **Duration:** ~30 sec
- **Key Message:** The skill that matters most with AI agents is your ability to specify what you want.
- **Speaker Notes:**
  - Section divider for Session 1
  - Key message: the better your specs, the better the output
- **What to Watch For:** Nothing specific -- this is a brief transition.
- **Facilitator Tips:** Quick beat. One sentence: "The single most important skill with AI agents is specification. Let me show you why."

---

### Slide 9: Why Specs Matter
- **Time:** ~10:16 AM
- **Duration:** ~3 min
- **Key Message:** Garbage in, garbage out -- but now at 100x speed. Clear specs are your highest-leverage activity.
- **Speaker Notes:**
  - Open with the Anthropic framing: think of Claude as a brilliant but new employee with no context on your norms, workflows, or standards
  - The more precisely you explain what you want, the better the result
  - Adding context or motivation behind instructions helps Claude understand your goals
  - A good PRD has acceptance criteria, constraints, data contracts, examples
  - CLAUDE.md encodes standards, architecture, testing, and tool preferences
  - Four scope tags at bottom show scope levels
- **What to Watch For:** People nodding but not internalising -- they will default to vague prompts in the lab. Plant the seed now and reinforce during the exercise.
- **Facilitator Tips:** The "brilliant but new employee" metaphor lands well. Pause after saying it and let people picture it. Then connect: "So what do you do with a brilliant new hire? You give them a really good onboarding doc."

---

### Slide 10: CLAUDE.md in Action
- **Time:** ~10:19 AM
- **Duration:** ~3 min
- **Key Message:** A single file shapes every line the agent writes. Add one rule, change all future output. This is the highest ROI activity.
- **Speaker Notes:**
  - Walk through the code example on the right: tech stack, data standards, testing approach
  - On the left, explain the three scope levels: repo, project, user
  - The exercise box previews the upcoming hands-on exercise
  - Mention: add one rule, change all future output
- **What to Watch For:** People who are already mentally drafting their CLAUDE.md -- that is the ideal state. People who look confused about what a CLAUDE.md is -- point back to the code example.
- **Facilitator Tips:** Read a few of the rules aloud from the code block: "Use PySpark for all data processing. All functions must have type hints. Date columns: DATE, YYYY-MM-DD." This makes it concrete.

---

### Slide 11: CLAUDE.md Scope Levels
- **Time:** ~10:22 AM
- **Duration:** ~2 min
- **Key Message:** Instructions cascade like CSS: user-level -> repo-level -> project-level. More specific rules override general ones.
- **Speaker Notes:**
  - Three levels cascade like CSS
  - User-level: personal prefs (git style, tool choices) at `~/.claude/CLAUDE.md`
  - Repo-level: team standards committed to git at `./CLAUDE.md`
  - Project-level: module-specific rules at `./src/CLAUDE.md`
  - Ask: "What would you put at each level?"
- **What to Watch For:** Confusion about how the levels interact -- use the CSS analogy: "Just like CSS, the most specific rule wins."
- **Facilitator Tips:** Quick interactive moment: "Quick show of hands -- who would put 'always use PySpark' at repo level? User level?" Gets people thinking about the design choice.

---

### Slide 11b: Today's Challenge -- Grocery Intelligence Platform
- **Time:** ~10:24 AM
- **Duration:** ~3 min
- **Key Message:** This is the through-line for the whole day. Lab 1 builds the data pipeline, Lab 2 builds the app and dashboards. The CLAUDE.md they write next will guide them through both labs.
- **Speaker Notes:**
  - Introduce the challenge before the CLAUDE.md exercise so teams know what they are writing specs for
  - The data is real -- Australian Bureau of Statistics retail trade and food price data
  - Walk through the three columns: data sources, tech stack, what they will build
  - Emphasise: same CLAUDE.md they write now will guide them through both labs
- **What to Watch For:** Teams not understanding what they are building -- this slide is critical context for the exercise. Make sure they grasp: "You are building a data pipeline, then an app on top of it."
- **Facilitator Tips:** Point to the "What You'll Build" column and say: "Lab 1 is the bottom half -- Bronze through Gold. Lab 2 is the top half -- the app and dashboards. Your CLAUDE.md needs to cover both."

---

### Slide 12: Rule #1 -- Just Say What You Want
- **Time:** 10:35 AM
- **Duration:** ~20 min total (15 min exercise + 5 min discussion)
- **Key Message:** Rule #1 of vibe coding: you literally type what you want and it happens. Don't write config files -- have a conversation.
- **Speaker Notes:**
  - 15-minute team exercise
  - Each team opens their Coding Agents terminal and tells Claude about their project
  - Claude creates the CLAUDE.md, project structure, and initial config
  - Walk around the room, help anyone stuck
  - The "aha" moment: they realise they can just type what they want
  - After 15 min, ask 2-3 teams what surprised them
  - 5 min discussion after
- **What to Watch For:**
  - Teams that cannot access their terminal -- help them immediately, this is their first hands-on moment
  - Teams trying to hand-write CLAUDE.md -- redirect: "Just tell Claude what you want"
  - Teams not reviewing Claude's output -- remind them to refine through conversation
  - Teams that finish early -- encourage them to modify through conversation: "Tell Claude to add a rule about X"
- **Facilitator Tips:**
  - Set a visible timer for 15 minutes
  - Walk the room continuously. Spend ~90 seconds with each team
  - Have the prompt ready to paste for teams that are stuck starting
  - For the share-back, ask: "What did Claude get right? What did you correct by just saying so?"
  - The key teaching point: this is agentic engineering -- you engineer the harness through conversation

**Discussion Questions & Suggested Talking Points:**
1. *What did Claude get right without you specifying it?* -- Often gets project structure, basic rules, but misses team-specific standards
2. *What did you correct by just saying so?* -- This demonstrates Rule #1 in action: want to change something, just say it
3. *How is this different from hand-writing config?* -- Faster, iterative, conversational, and Claude brings knowledge you might miss
4. *What Coles-specific standards would you add through conversation?* -- Data governance rules, approved libraries, naming conventions

---

### Slide 13: Section -- Session 2: TDD + Agents
- **Time:** 11:05 AM (after break)
- **Duration:** ~30 sec
- **Key Message:** TDD is not just good practice -- it is exponentially more powerful with AI agents because tests are unambiguous specs.
- **Speaker Notes:**
  - Section divider for Session 2
- **What to Watch For:** Post-break energy dip -- open with an energetic "Welcome back! Now the real magic starts."
- **Facilitator Tips:** If energy is low, ask a quick question: "Did anyone's CLAUDE.md already save them time? Anyone experiment during the break?"

---

### Slide 14: TDD Workflow
- **Time:** ~11:06 AM
- **Duration:** ~3 min
- **Key Message:** The TDD + Agent workflow is a 4-step loop: Human writes test -> Agent implements -> Run & iterate -> Human reviews. The test IS the spec.
- **Speaker Notes:**
  - Walk through the 4-step flow
  - The key insight: the test IS the spec. No ambiguity
  - The agent reads the test, writes code to pass it, runs the test, reads failures, fixes code
  - Tight feedback loop
- **What to Watch For:** Engineers who say "I already do TDD" -- great, validate them and explain this is the same skill applied differently. Engineers who never do TDD -- frame it as "the agent makes TDD free."
- **Facilitator Tips:** Use the step cards as a visual walk-through. Point to each one in sequence. Emphasise step 3 (Run & Iterate) -- "This is where the magic happens. The agent reads the error, understands what went wrong, and fixes it without you doing anything."

---

### Slide 15: Why TDD Works with Agents
- **Time:** ~11:09 AM
- **Duration:** ~3 min
- **Key Message:** Three reasons TDD is exponentially better with agents: unambiguous specs, self-correcting loop, and guardrails.
- **Speaker Notes:**
  - Unambiguous specs: no interpretation needed
  - Self-correcting loop: agent runs tests, reads failures, fixes code -- no human needed in between
  - Guardrails: tests prevent the agent from going off the rails
  - Pro tips: start small, descriptive names, pin critical behavior
- **What to Watch For:** Questions about "what if the agent writes bad tests?" -- clarify that HUMANS write the tests, the agent writes the implementation.
- **Facilitator Tips:** Read the pro tips callout aloud: "Start small -- one test, one function. Use descriptive test names as documentation. Pin critical behavior with specific value assertions." These are practical and actionable.

---

### Slide 16: Writing Tests That Guide
- **Time:** ~11:12 AM
- **Duration:** ~3 min
- **Key Message:** Good tests follow Given-When-Then structure with concrete values, descriptive names, and multiple assertions.
- **Speaker Notes:**
  - Walk through the code example: concrete test data (10 rows, 2 invalid), specific assertions (count==8, no negatives)
  - Four principles: Given-When-Then structure, concrete values, descriptive names, multiple assertions
  - Ask: "Who currently writes tests?"
- **What to Watch For:** People glazing over at the code -- read it aloud and explain each section. "GIVEN: 10 rows, 2 with null amounts. WHEN: we clean the data. THEN: 8 rows remain, all positive."
- **Facilitator Tips:** This is the last conceptual slide before the demo. Make sure people understand the test structure because they will write similar tests in Lab 1.

---

### Slide 16b: Anthropic Best Practices
- **Time:** ~11:15 AM
- **Duration:** ~2 min
- **Key Message:** Anthropic's #1 best practice: give Claude a way to verify its work. #2: explore first, then plan, then code.
- **Speaker Notes:**
  - These two principles come straight from Anthropic's official Claude Code best practices
  - First: give Claude a way to verify its work -- tests, screenshots, expected outputs
  - Second: explore first, then plan, then code -- use /plan mode to align on approach before burning context
  - This prevents solving the wrong problem fast
- **What to Watch For:** People eager to jump into coding without planning -- this slide is the antidote. Reference it during the labs: "Remember: explore, plan, then code."
- **Facilitator Tips:** The quote at the bottom is powerful. Read it: "Give Claude a way to verify its work. This is the single highest-leverage thing you can do." Pause. Let it land.

---

### Slide 17: Managing Context Windows
- **Time:** ~11:17 AM
- **Duration:** ~4 min
- **Key Message:** The context window is the agent's working memory (~200K tokens). It fills up fast, and when it does, auto-compaction fires and the agent forgets earlier details.
- **Speaker Notes:**
  - Context window is like RAM -- manage it or the OS starts swapping
  - The status bar visualisation shows how context fills up: CLAUDE.md, file reads, conversation turns, agent responses
  - When the bar fills, auto-compaction fires and the agent forgets earlier details
  - Four strategies: keep CLAUDE.md lean (50 lines not 500), offload to subagents, plan before building (/plan), use teams for parallel work
- **What to Watch For:** This is an abstract concept. Watch for confused faces. If people look lost, use the analogy: "Imagine you have a whiteboard with limited space. Every time the agent reads a file, it writes on the whiteboard. Eventually you run out of space and have to erase something."
- **Facilitator Tips:** The context bar visualisation is the star of this slide. Walk through each coloured segment. Point to the "COMPACTION" danger zone. This visual will stick with people during the labs when their agent starts forgetting things.

---

### Slide 18: Live Demo Preview
- **Time:** ~11:20 AM
- **Duration:** ~5 min demo
- **Key Message:** Watch the full TDD cycle in action: write failing tests, let the agent implement, iterate to green.
- **Speaker Notes:**
  - DEMO SLIDE
  - Open Coding Agents terminal
  - Write 3 failing tests: clean_data, join_tables, aggregate
  - Ask Claude Code to implement
  - Watch the agent read tests, write code, run tests, see failures, fix code
  - Point out: agent reads test expectations BEFORE writing code; self-corrects on failures; converges in 2-5 iterations
  - Have backup recording ready in case of issues
- **What to Watch For:**
  - Network issues during live demo -- switch to backup recording immediately, do not debug live
  - The demo taking too long -- if the agent is slow, narrate what would happen: "It would now read the error message, identify the fix, and update the function"
  - Audience not being able to see the terminal -- zoom in on the font size
- **Facilitator Tips:**
  - Have the backup recording loaded in another tab before starting the demo
  - Narrate as you go: "See how it reads the test first? It knows what 'done' looks like before writing any code."
  - If the demo goes perfectly, celebrate it: "That was 3 functions implemented and tested in under 3 minutes. That is what TDD + agents gives you."
  - If the demo hits errors, celebrate that too: "This is actually perfect -- watch how the agent reads the error and self-corrects."

---

### Slide 19: Section -- Lab 1
- **Time:** 11:20 AM
- **Duration:** ~30 sec
- **Key Message:** 65 minutes hands-on. Build a Lakeflow Declarative Pipeline with real Australian data.
- **Speaker Notes:**
  - Remind everyone to have their Coding Agents terminal ready
  - If anyone has access issues, flag them NOW
- **What to Watch For:** Teams that still do not have terminal access -- this is urgent. Help them immediately or pair them with another team temporarily.
- **Facilitator Tips:** "Hands on keyboards. You have 65 minutes. The lab guide is in LAB-1-DATA-PIPELINE.md. Start with Phase 1: Write Tests First. Go!"

---

### Slide 19b: Practical Tips for the Labs
- **Time:** Just before lab starts
- **Duration:** ~2 min
- **Key Message:** Three practical patterns that will save time: watch for overengineering, prevent hallucinations, course-correct early.
- **Speaker Notes:**
  - (1) Overeagerness: Claude tends to overengineer -- extra files, unnecessary abstractions. Tell it to keep solutions minimal. Add a line to your CLAUDE.md.
  - (2) Hallucination prevention: never trust claims about code Claude has not read. Add the investigate_before_answering instruction.
  - (3) Course-correct early: do not let it run for 10 minutes unchecked. Check in every 2-3 tool calls.
- **What to Watch For:** Teams that skip this slide and dive in -- that is fine, but you may need to remind them of these tips during the lab when they hit issues.
- **Facilitator Tips:** Read the three CLAUDE.md additions aloud and say: "Add these to your CLAUDE.md right now, before you start Lab 1." This takes 30 seconds and saves 10 minutes of frustration.

---

### Slide 20: Lab 1 Briefing
- **Time:** ~11:22 AM
- **Duration:** ~3 min briefing, then 65 min lab
- **Key Message:** Build a Lakeflow Declarative Pipeline: Write Tests (15 min) -> Bronze (15 min) -> Silver + Gold (20 min) -> Deploy with DABs (10 min).
- **Speaker Notes:**
  - Teams compete to build the best pipeline
  - Data is from the Australian Bureau of Statistics -- real retail trade and food price data
  - Each phase has a checkpoint in Unity Catalog so no team gets stuck
  - Encourage TDD approach from Session 2
  - Walk around and help during the 65 min lab time
- **What to Watch For:**
  - Teams skipping tests and going straight to implementation -- gently redirect: "Remember, tests first"
  - Teams stuck on API calls -- direct them to Checkpoint 1A immediately, do not let them waste 20 min debugging network issues
  - Teams falling behind at 40 min -- point them to Checkpoint 1B (pre-loaded silver/gold)
- **Facilitator Tips:**
  - Set a visible timer for 65 minutes
  - Do a room check every 15 minutes: walk to each team, ask "What phase are you on? What's blocking you?"
  - At the 40-minute mark, announce: "If you are still on Bronze, grab Checkpoint 1B now. You need gold tables for Lab 2."
  - At the 55-minute mark, announce: "10 minutes left. Start wrapping up. Make sure you can query your gold tables."

---

### Slide 21: Show & Tell + Prediction Reveal
- **Time:** 12:25 PM
- **Duration:** ~10 min
- **Key Message:** Each team shows their pipeline and shares one insight. Then reveal the ice breaker answers using the Gold tables they just built.
- **Speaker Notes:**
  - Quick demos from each team (2 min each): show pipeline DAG, share one interesting insight from Gold data
  - Then reveal ice breaker answers using actual data from the pipelines they just built
  - Score the prediction cards
  - Award bragging rights to the most accurate team
- **What to Watch For:**
  - Teams with nothing to show -- let them use checkpoint data and still present what they learned
  - Demos running long -- be strict with the 2-minute timer
  - The prediction reveal falling flat -- build excitement: "Let us see who was RIGHT about NSW..."
- **Facilitator Tips:**
  - Use the click-to-reveal answers on Slide 2 for the prediction reveal
  - Have a team (or yourself) run the SQL queries live against the Gold tables: "SELECT state, SUM(turnover_millions) FROM retail_summary GROUP BY state ORDER BY 2 DESC LIMIT 1"
  - Scoring: give 1 point for each correct (or close) prediction. Announce the winning team. This creates a fun energy transition into lunch.

**Discussion Questions & Suggested Answers:**
- *Where did TDD help the agent stay on track?* -- Tests caught schema mismatches, wrong column names, missing transformations. The agent self-corrected without human help.
- *Where did the agent go off-rails?* -- Common: building unnecessary abstractions, using pandas instead of PySpark, creating extra helper files. The CLAUDE.md rules helped prevent this.

---

### Slide 22: Section -- Session 3: Beyond the Basics
- **Time:** 1:05 PM (after lunch)
- **Duration:** ~1 min
- **Key Message:** MCP, Subagents, Genie & AI/BI Dashboards -- the advanced tools that multiply agent effectiveness.
- **Speaker Notes:**
  - Post-lunch session -- energy might be lower
  - Start with an interactive question: "What worked well in Lab 1? What surprised you?"
  - Use their experiences to ground Session 3 concepts
- **What to Watch For:** Post-lunch energy dip. This is the hardest transition of the day.
- **Facilitator Tips:** Do NOT start with slides. Start with a 2-minute discussion: "Quick round -- one thing that surprised you in Lab 1." This gets people talking and reconnects them to the material. Then transition: "Now let me show you tools that would have made Lab 1 even faster."

---

### Slide 23: Subagents, Skills, Hooks & Plugins
- **Time:** ~1:07 PM
- **Duration:** ~5 min
- **Key Message:** Four concepts that extend agent capabilities: Subagents (parallel workers), Skills (slash commands), Hooks (deterministic guardrails), Plugins (packaged toolkits).
- **Speaker Notes:**
  - Subagents: spawn parallel workers with isolated context
  - Skills: slash commands that encode domain knowledge (built-in: /commit, /review; custom: /deploy-pipeline)
  - Hooks: shell commands that fire on events -- pre-commit linting, post-edit formatting, notification logging. Deterministic guardrails around the AI.
  - Plugins: package skills + agents + hooks for teams
- **What to Watch For:** People confusing hooks with skills -- clarify: "Hooks are deterministic shell commands that always run. Skills are AI-powered workflows."
- **Facilitator Tips:** The code blocks in each card are concrete examples. Read the subagent example aloud: "Spawn a subagent to build the frontend while I work on the backend API." This is exactly what they should do in Lab 2.

---

### Slide 23b: Skills in Action -- TDD Skill Chain
- **Time:** ~1:12 PM
- **Duration:** ~3 min
- **Key Message:** Skills automate the TDD workflow: /prd-writer generates a PRD, /test-generator generates failing tests, /implementer makes them pass.
- **Speaker Notes:**
  - Connect Session 2's TDD concepts with Session 3's skills
  - Walk through the flow: /prd-writer interviews you, /test-generator reads the PRD and generates failing tests, /implementer makes them pass
  - Key insight: writing hundreds of test cases by hand is painful -- skills automate this
  - Tests should initially FAIL -- that is expected and correct
  - Encourage teams to try this in Lab 2
- **What to Watch For:** People thinking this is too good to be true -- show them the code block and say "Try /test-generator in Lab 2 and see what happens."
- **Facilitator Tips:** This slide bridges theory (Session 2) and practice (Lab 2). Say: "In Lab 1, you wrote tests by hand. In Lab 2, try using /test-generator and see if it saves time."

---

### Slide 24: What is MCP
- **Time:** ~1:15 PM
- **Duration:** ~4 min
- **Key Message:** MCP is the USB-C of AI. Before MCP: N x M custom connectors. After MCP: N + M standardised connections.
- **Speaker Notes:**
  - Before MCP, every AI model needed custom integration code for every tool. 10 models x 10 tools = 100 custom connectors
  - Same problem USB had before USB-C
  - MCP: build the connector once, every agent can use it
  - Anthropic open-sourced MCP in late 2024 and it has become the industry standard
  - For Coles: dozens of internal tools -- without MCP you would write custom code for each one
- **What to Watch For:** The "before" diagram with the spaghetti lines should get a reaction. If it does not, point at it explicitly: "This is what tool integration looks like without a standard. Every line is custom code someone has to maintain."
- **Facilitator Tips:** The USB-C analogy is the most important metaphor on this slide. Say: "Remember when every phone had a different charger? MCP is the USB-C moment for AI agents."

---

### Slide 25: How MCP Works
- **Time:** ~1:19 PM
- **Duration:** ~4 min
- **Key Message:** Client-server architecture with JSON-RPC. MCP handles wiring, skills handle knowledge, the agent orchestrates both. For Coles: one protocol wraps Unity Catalog, internal APIs, and Genie.
- **Speaker Notes:**
  - Walk through the client-server architecture image
  - Clients are AI agents (Claude Code, Cursor). Servers expose tool capabilities over JSON-RPC
  - Having MCP tools is not enough -- you also need Skills (procedural knowledge) that tell agents WHEN and HOW to use tools
  - For Coles: an MCP server wrapping Unity Catalog means every agent in the org can query tables without custom code
- **What to Watch For:** People asking "Can we build our own MCP server?" -- great question, point them to the bonus challenge in Lab 2.
- **Facilitator Tips:** The formula at the bottom is memorable: "MCP = tool connectivity. Skills = procedural knowledge. Agent = orchestrator." Say it, then say it again.

---

### Slide 26: MCP on Databricks
- **Time:** ~1:23 PM
- **Duration:** ~5 min
- **Key Message:** Three flavours of MCP servers on Databricks: Built-in/Managed, Proxy/External, Custom. All secured through Unity Catalog.
- **Speaker Notes:**
  - Built-in/Managed: UC functions, tables, volumes, Vector Search, Genie -- zero config
  - Proxy/External: third-party services (GitHub, Slack, Glean) via UC Connections -- no credentials exposed
  - Custom: host your own on Databricks Apps
  - All secured through Unity Catalog
  - Coles callout: in Lab 2 you will connect your app to Genie via a managed MCP server
- **What to Watch For:** Questions about security/credentials -- emphasise UC Connections manage auth tokens, no credentials are exposed to clients.
- **Facilitator Tips:** Three cards, three flavours. Quick summary: "Managed = Databricks gives you. Proxy = connect third-party. Custom = build your own." The Coles callout at the bottom connects this to Lab 2.

---

### Slide 27: MCP Architecture -- Full Picture
- **Time:** ~1:28 PM
- **Duration:** ~3 min
- **Key Message:** Full architecture diagram showing how Databricks-served and external agents connect to the same MCP servers, secured by Unity Catalog and AI Gateway.
- **Speaker Notes:**
  - Left side: Databricks-served agent with Orchestration Framework connects to three MCP server types
  - Right side: Externally-served agents (Claude Code, Cursor) connect to the same MCP servers
  - Bottom: AI Gateway routes to Model Serving (self-hosted) or SaaS LLM (Anthropic, OpenAI)
  - MLflow Tracing captures everything
  - Coles would be on the right side today -- an external agent connecting into Databricks via MCP
- **What to Watch For:** Information overload -- this is a dense diagram. Do not try to explain every box. Hit the two sides (Databricks-served vs. external) and the AI Gateway at the bottom.
- **Facilitator Tips:** Say: "You do not need to memorise this. The key insight is: whether the agent runs inside Databricks or outside, it connects through the same MCP protocol and the same security layer."

---

### Slide 28: AI Dev Kit
- **Time:** ~1:31 PM
- **Duration:** ~4 min
- **Key Message:** The AI Dev Kit packages everything -- skills, MCP server, Python tools, and a web builder app -- into one installable toolkit. This is what you are using today.
- **Speaker Notes:**
  - Four components: Skills layer (25+ skill packs), MCP Server (50+ tools), Tools Core (Python library), Builder App (web interface)
  - Architecture flow: You type a prompt -> Agent reads Skills -> Calls MCP tools -> Databricks executes
  - Coles callout: fork the AI Dev Kit and add custom skills (/run-data-quality, /deploy-pipeline, /check-lineage)
- **What to Watch For:** People wanting to try specific skills right now -- encourage them to use them in Lab 2.
- **Facilitator Tips:** Point to the Builder App card: "This is what you are using right now in the browser. It is not magic -- it is an open-source Databricks App."

---

### Slide 29: Demo -- How Databricks Uses Claude
- **Time:** ~1:35 PM
- **Duration:** ~8 min live demo
- **Key Message:** Databricks internally configures Claude Code with CLAUDE.md, hooks, skills, and MCP servers. This setup is reproducible for Coles.
- **Speaker Notes:**
  - LIVE DEMO showing Databricks' internal Claude Code configuration
  - Walk through: (1) CLAUDE.md -- company-wide rules. (2) Hooks -- pre-commit lint/security, post-edit auto-format. (3) Skills -- custom /deploy, /validate. (4) MCP servers -- connected to UC, Genie, internal tooling.
  - Key insight: this is reproducible. Coles can set up the same structure.
- **What to Watch For:**
  - Demo fatigue -- this is the second demo. Keep it brisk and focused.
  - Questions about "Can we see the actual CLAUDE.md?" -- show the settings.json code block on the slide if you cannot show the real one.
- **Facilitator Tips:** This demo should feel like a "peek behind the curtain." Say: "This is not theoretical. This is how a 7,000-person engineering org actually uses AI agents." Then show the config and explain each piece.

---

### Slide 30: Genie + AI/BI Dashboards
- **Time:** ~1:43 PM
- **Duration:** ~5 min
- **Key Message:** Genie lets business users query data in English. AI/BI dashboards auto-generate charts. Both connect to your Gold tables from Lab 1.
- **Speaker Notes:**
  - Genie: create a Genie space, point at gold tables, ask questions in plain English, no code needed
  - AI/BI dashboards: point at tables, describe what you want, get interactive dashboards
  - Complement each other: dashboards for recurring views, Genie for ad-hoc questions
- **What to Watch For:** People thinking Genie replaces their custom AI query feature in the app -- clarify: "Your app gives you full control over the UX. Genie is a zero-code alternative for business users."
- **Facilitator Tips:** The code blocks showing example questions are powerful. Read them aloud: "Which Australian state had the highest food retail turnover in 2024?" -- then say "That is all a business user types. Genie does the rest."

---

### Slide 31: Section -- Lab 2
- **Time:** 1:25 PM
- **Duration:** ~30 sec
- **Key Message:** Capstone challenge. 65 minutes to build an app, connect Genie, and create AI/BI dashboards. Use everything from today.
- **Speaker Notes:**
  - Remind everyone: use everything from today -- CLAUDE.md, TDD, subagents, MCP
- **What to Watch For:** Teams that look overwhelmed by the scope -- reassure them: "You do not need to finish everything. A working app is better than a perfect app that is not done."
- **Facilitator Tips:** Energy boost: "This is the capstone. Everything you learned today comes together. Let's go!"

---

### Slide 32: Lab 2 Briefing
- **Time:** ~1:26 PM
- **Duration:** ~3 min briefing, then 65 min lab
- **Key Message:** Build a complete platform: web app (FastAPI + htmx), Genie space, and AI/BI dashboard. Use subagents for parallel work.
- **Speaker Notes:**
  - PRD + Tests (10 min) -> Backend + Frontend (25 min) -> Genie Space (10 min) -> AI/BI Dashboard (10 min) -> Deploy + Polish (10 min)
  - Encourage subagents: one on backend, one on frontend
  - Use MCP to query gold tables directly
  - Checkpoints available at every phase
  - Bonus challenge: build an MCP server for retail analytics
- **What to Watch For:**
  - Teams trying to do everything sequentially -- push them to divide and conquer: "One person on the app, one on Genie, one on the dashboard"
  - Teams spending too long on the app and not getting to Genie/Dashboard -- at 25 min, announce: "If your app is not working, grab Checkpoint 2A and move to Genie"
  - Teams stuck on htmx -- common issue, check the script tag
- **Facilitator Tips:**
  - Set a visible timer for 65 minutes
  - At 25 min: "Check-in! Move to Genie if you have not started."
  - At 45 min: "20 minutes left. Start your dashboard now if you have not."
  - At 55 min: "10 minutes. Prepare your 3-minute demo."

---

### Slide 33: Team Demos & Voting
- **Time:** 2:40 PM
- **Duration:** ~20 min total
- **Key Message:** Each team presents (3 min). Vote on Pipeline Quality, App Polish, Genie & AI/BI, and Creativity. Then 5-min retro.
- **Speaker Notes:**
  - Each team gets 3 minutes to demo their platform
  - Use a projected timer
  - After all demos, quick anonymous vote (show of hands or Google Form)
  - Announce winners
  - Then 5-min retro: What worked? What would you do differently? What will you use on Monday?
- **What to Watch For:**
  - Demos running over time -- be strict with the 3-minute limit
  - Teams with nothing to show -- let them present what they learned and what they would have built
  - Voting being awkward -- keep it light and fun, this is not a performance review
- **Facilitator Tips:**
  - Before demos start, remind teams: "Show pipeline, app, Genie, dashboard, one surprise. Three minutes. Go."
  - During voting, frame the four categories: "Raise your hand for the team with the best pipeline... best app... best Genie/dashboard... most creative."
  - The retro is critical for learning. Ask three questions: "What worked? What would you do differently? What will you take back to your daily work?"

---

### Slide 34: Key Takeaways
- **Time:** ~3:00 PM
- **Duration:** ~3 min
- **Key Message:** Four takeaways: (1) Specs are leverage, (2) TDD + Agents = deterministic, (3) Subagents & MCP extend reach, (4) Start small, iterate.
- **Speaker Notes:**
  - Walk through each card deliberately
  - Reference their experiences from the labs
  - Ask: "Which of these resonated most with you today?"
- **What to Watch For:** People zoning out at the end -- keep it energetic and reference specific moments from the day: "Remember when Team X's agent self-corrected on that test failure? That is takeaway #2."
- **Facilitator Tips:** Do not read the cards verbatim. Say: "If you remember nothing else from today, remember this: write clear specs, write tests, and start small." Then pause.

---

### Slide 35: Next Steps
- **Time:** ~3:03 PM
- **Duration:** ~3 min
- **Key Message:** Concrete actions: share learnings, set up a team CLAUDE.md, try it on a real task this week. Champions: Farbod, Swee Hoe (internal), David (Databricks).
- **Speaker Notes:**
  - Immediate: share learnings, set up team CLAUDE.md, try on a real task
  - Coming soon: broader team rollout, shared skill libraries, Genie spaces for real data
  - Champions: Farbod & Swee Hoe (internal), David O'Keeffe (Databricks)
  - Measure success: developer velocity, code quality, developer satisfaction
- **What to Watch For:** People looking for permission to use these tools -- give it explicitly: "You have everything you need to start using this on Monday."
- **Facilitator Tips:** Make the first action tangible: "Your homework is one thing: create a CLAUDE.md for your team's repo this week. That is all. Start there."

---

### Slide 36: Closing
- **Time:** ~3:06 PM
- **Duration:** ~2 min
- **Key Message:** "The best teams will be those who can effectively direct AI agents -- together." Go build something great.
- **Speaker Notes:**
  - Let the quote land
  - Thank them for their time, energy, and willingness to experiment
  - Congratulate the winning team one more time
  - Remind them of your email: david.okeeffe@databricks.com
  - Open the floor for any last questions
  - If no questions, close with: "Go build something great this week."
- **What to Watch For:** People wanting to ask questions but feeling the session is over -- explicitly invite questions: "We have a few minutes. Anything you want to ask?"
- **Facilitator Tips:** End strong. Stand centre-stage, make eye contact, deliver the closing line with conviction. Do not rush out -- be available for 10-15 minutes after for individual conversations.

---

## Ice Breaker Answers

These answers are revealed during Show & Tell (Slide 21) by querying the Gold tables that teams built in Lab 1. The click-to-reveal elements on Slide 2 also contain these answers.

| # | Question | Answer |
|---|----------|--------|
| Q1 | Which Australian state has the highest monthly food retail turnover? | **New South Wales** -- approximately $3.5B/month in food retailing |
| Q2 | By what percentage have Australian food prices (CPI) increased since January 2020? | **Approximately 25-30%**. The biggest spike hit in 2022-23 |
| Q3 | How much does the average Australian household spend on groceries per week? | **Around $200-$220/week** -- up from ~$160 pre-pandemic |
| Q4 | What month of the year do Australians spend the most on retail? | **December** -- Christmas shopping drives a massive spike across all categories |
| Q5 | Which food category has seen the largest price increase since 2020 -- dairy, meat, fruit, or bread & cereals? | **Dairy & eggs** -- up over 30% since 2020, outpacing all other food groups |

**Scoring:** 1 point for each correct (or close) answer. Announce the winning team. This creates a fun transition into lunch.

**SQL queries to run live against Gold tables:**
```sql
-- Q1: Highest food retail turnover by state
SELECT state, SUM(turnover_millions) as total_turnover
FROM workshop_vibe_coding.<team>.retail_summary
WHERE industry = 'Food retailing'
GROUP BY state ORDER BY total_turnover DESC LIMIT 1;

-- Q4: Peak retail spending month
SELECT MONTH(period_date) as month, SUM(turnover_millions) as total
FROM workshop_vibe_coding.<team>.retail_summary
GROUP BY MONTH(period_date) ORDER BY total DESC LIMIT 1;

-- Q5: Fastest-rising food category (if CPI data includes subcategories)
SELECT index_name, MAX(yoy_change_pct) as max_inflation
FROM workshop_vibe_coding.<team>.food_inflation_yoy
GROUP BY index_name ORDER BY max_inflation DESC LIMIT 5;
```

---

## Lab 1: Facilitation Notes

### How to Help Teams That Get Stuck

| Stuck Point | What to Do |
|-------------|-----------|
| Cannot access terminal | Check Databricks App URL, clear browser cache, try incognito. If still broken, pair with another team. |
| Do not know where to start | Point them to Phase 1.1 in the lab guide: "Start by exploring the data. Paste the API URL and ask the agent to show you the columns." |
| Agent uses pandas instead of PySpark | Have them add to CLAUDE.md: "Always use PySpark, never pandas." Then tell the agent explicitly. |
| Tests are too vague | Ask: "What does 'correct' look like? How many rows? What columns? What values?" Push for specificity. |
| ABS API is slow or failing | Immediately direct to Checkpoint 1A. Do not let them waste more than 5 minutes on network issues. |
| Agent creates too many files | Add to CLAUDE.md: "Keep solutions minimal. Do not add features, abstractions, or files beyond what is requested." |
| SparkSession errors in tests | Check conftest.py: it needs `SparkSession.builder.master("local[*]").getOrCreate()` |
| @dp.table decorator not found | Import is `import databricks.declarative_pipelines as dp` (or `import dlt` on older runtimes) |
| Agent rewrites working code | Say: "Don't change functions that are already passing tests. Only fix the failing ones." |
| Running out of time at 40 min | Direct to Checkpoint 1B immediately. They need Gold tables for Lab 2. |

### Checkpoint Data Locations

| Checkpoint | What It Contains | Location |
|-----------|-----------------|----------|
| 1A | Pre-loaded Bronze tables (raw ABS data) | `workshop_vibe_coding.checkpoints.bronze_retail_trade`, `workshop_vibe_coding.checkpoints.bronze_cpi_food` |
| 1B | Pre-loaded Silver + Gold tables | `workshop_vibe_coding.checkpoints.retail_turnover`, `workshop_vibe_coding.checkpoints.food_price_index`, `workshop_vibe_coding.checkpoints.retail_summary`, `workshop_vibe_coding.checkpoints.food_inflation_yoy` |
| 1C | Complete pipeline code + databricks.yml | Shared repo/folder (provide URL) |

### What "Good" Looks Like at Each Phase

| Phase | Time | Good State |
|-------|------|-----------|
| Phase 1: Tests | 15 min | 6 test functions written, all FAILING (no implementation yet). Tests use PySpark fixtures with 5-10 rows each. |
| Phase 2: Bronze | 30 min | Bronze tests passing. Two tables ingested from ABS APIs (or checkpoints). Data quality expectations defined. |
| Phase 3: Silver + Gold | 50 min | All 6 tests passing. Silver tables have decoded region/industry names. Gold tables have rolling averages and YoY metrics. |
| Phase 4: Deploy | 60 min | Pipeline deployed via DABs. Tables visible in Unity Catalog. Can query Gold tables to answer ice breaker questions. |

### Common Errors and Fixes

| Error | Root Cause | Fix |
|-------|-----------|-----|
| `AnalysisException: Table not found` | Wrong catalog/schema path | Check the Unity Catalog path: `workshop_vibe_coding.<team_schema>.<table>` |
| `HTTP 429 Too Many Requests` on ABS API | Rate limiting | Wait 30 sec and retry, or use Checkpoint 1A |
| `ValueError: could not convert string to float` | ABS CSV has header rows the agent is not skipping | Tell agent to skip metadata rows: `spark.read.option("header", "true").csv(url)` |
| Tests pass locally but pipeline fails on deploy | Local tests use mock data; pipeline reads from real tables | Check that table names in pipeline match the schema convention |
| `PermissionDenied` on Unity Catalog | Missing USAGE or CREATE TABLE grants | Run: `GRANT USAGE ON SCHEMA workshop_vibe_coding.<team> TO <user>` |

---

## Lab 2: Facilitation Notes

### How to Help Teams That Get Stuck

| Stuck Point | What to Do |
|-------------|-----------|
| Do not know how to start the app | Point to Phase 1.1: "Start with the PRD. Paste it into the agent and ask it to create the project structure." |
| htmx not working | Check the script tag: `<script src="https://unpkg.com/htmx.org@2.0.4"></script>` must be in `<head>`. Check browser DevTools console for errors. |
| CORS errors | Agent sometimes forgets CORS middleware. Add `CORSMiddleware` to FastAPI with `allow_origins=["*"]`. |
| AI query generates invalid SQL | Add the full table schema + column descriptions to the LLM system prompt. Include 2-3 example queries. |
| Cannot create Genie space | Check permissions: user needs CREATE GENIE SPACE on the catalog. Grant if needed. |
| Dashboard queries are slow | Check SQL warehouse is running. Gold tables should be materialized views and should be fast. |
| App deploys but shows blank page | Check static files are mounted: `app.mount("/static", StaticFiles(directory="static"))`. Check Databricks App logs. |
| databricks-sql-connector errors | Ensure it is in requirements.txt. Check `DATABRICKS_HOST`, `DATABRICKS_HTTP_PATH`, `DATABRICKS_TOKEN` environment variables. |
| Not using subagents | Explicitly suggest: "Have one person tell the agent to use a subagent for the frontend while the main session works on the backend." |

### Checkpoint Data Locations

| Checkpoint | What It Contains | Location |
|-----------|-----------------|----------|
| 2A | Working app skeleton (health endpoint, DB connection, basic structure) | Shared repo/folder |
| 2B | Step-by-step Genie setup instructions with recommended table descriptions and sample questions | Shared doc |
| 2C | Pre-written SQL queries for common dashboard visualizations | Shared doc |
| 2D | Complete solution for reference | Shared repo/folder |

### How to Encourage Use of Skills, Subagents, MCP

- **Subagents:** Walk up to a team and say: "Your backend person and frontend person could work in parallel. Tell the agent: 'Spawn a subagent to build the frontend while I work on the API.'"
- **Skills:** Suggest: "Try `/commit` to save your work. Try `/test-generator` to auto-generate tests from your PRD."
- **MCP:** Suggest: "You can search Databricks docs without leaving the terminal. Ask: 'Search the Databricks docs for how to create a Genie space programmatically.'"

### What "Good" Looks Like at Each Phase

| Phase | Time | Good State |
|-------|------|-----------|
| Phase 1: PRD + Tests | 10 min | PRD written, 3-4 API test functions, all failing. |
| Phase 2: Backend + Frontend | 35 min | API tests passing. Frontend loads in browser. Filters work. "Ask AI" feature returns answers. |
| Phase 3: Genie Space | 45 min | Genie space created, pointed at Gold tables, answering natural language questions correctly. |
| Phase 4: AI/BI Dashboard | 55 min | Dashboard with at least 3 visualizations. Clean layout with a title. |
| Phase 5: Deploy + Polish | 65 min | App deployed to Databricks Apps. All components working. Demo prepared. |

### Common Errors and Fixes

| Error | Root Cause | Fix |
|-------|-----------|-----|
| `ModuleNotFoundError: databricks.sql` | Missing from requirements.txt | Add `databricks-sql-connector` to requirements.txt |
| App returns 500 on `/api/metrics` | SQL query error or missing env vars | Check DATABRICKS_HOST, DATABRICKS_HTTP_PATH, DATABRICKS_TOKEN are set |
| Tailwind styles not applying | CDN link missing or wrong version | Add `<script src="https://cdn.tailwindcss.com"></script>` to `<head>` |
| Genie gives wrong answers | Missing table/column descriptions | Add context: "This data contains Australian retail trade and food price data. States are Australian states. Turnover is in millions AUD." |
| Dashboard shows "No data" | Wrong table reference or warehouse not running | Verify the table path and that the SQL warehouse is started |

---

## Discussion Question Answer Guide

### Session 1: CLAUDE.md Exercise Discussion

**"What rules did you include that the agent would not know on its own?"**
- Unity Catalog namespace and naming convention (`workshop_vibe_coding.<team>`)
- PySpark over pandas preference (the agent defaults to pandas for small data)
- Specific date/currency formats (DATE type, DECIMAL(12,2))
- Testing patterns (pytest with PySpark fixtures, small DataFrames)
- Lakeflow Declarative Pipelines decorators (`@dp.table`, `@dp.materialized_view`)

**"What Coles-specific standards should be in a shared team CLAUDE.md?"**
- Data governance and classification rules
- Approved Python/PySpark libraries and versions
- Naming conventions for tables, columns, pipelines
- Security patterns (no hardcoded credentials, parameterized queries)
- Code review standards and testing coverage expectations
- Deployment patterns (DABs, CI/CD pipelines)

**"How would this change the agent's behaviour on your daily work?"**
- Consistent code style across all agent-generated code
- Fewer code review comments (agent follows standards from the start)
- Faster onboarding of the agent to new projects (CLAUDE.md provides context)
- Less time fixing agent output; more time reviewing and directing

**"What would you put at user-level vs repo-level?"**
- User-level: personal git preferences (commit message style, editor), preferred tools (uv vs pip), personal coding style quirks
- Repo-level: team architecture decisions, testing frameworks, approved dependencies, data conventions, deployment patterns

### Show & Tell Discussion

**"Where did TDD help the most?"**
- Catching schema mismatches early (wrong column names, missing columns)
- Preventing the agent from changing working code (tests caught regressions)
- Self-correcting loop: agent reads test failures and fixes without human intervention
- Providing clarity on what "done" looks like for each transformation

**"Where did the agent go off-rails?"**
- Creating unnecessary helper files and abstractions
- Using pandas instead of PySpark (if not specified in CLAUDE.md)
- Over-engineering error handling or adding features not requested
- Rewriting passing tests when told to fix failing ones
- Hallucinating API response formats instead of reading the actual data

### Session 3: Post-lunch Discussion

**"What worked well in Lab 1? What surprised you?"**
- Likely answers: speed of iteration, quality of generated tests, self-correcting behavior
- Surprises: how specific the CLAUDE.md needs to be, how fast context fills up, how good the agent is at PySpark when properly directed

### Lab 2 Reflection

**"How did the PRD guide the agent's decisions?"**
- The PRD defined the API contract (endpoints, request/response formats)
- User stories shaped the frontend layout
- Technical requirements constrained the tech stack (no npm, use htmx)

**"How does Genie compare to your custom AI query feature?"**
- Genie: zero code, instant setup, great for business users, limited customization
- Custom: full control over UX, can add context and guardrails, requires development time
- Both have value: Genie for quick ad-hoc queries, custom for production apps

**"What would you need to add to make this production-ready?"**
- Authentication and authorization
- Error handling and retry logic
- Monitoring and alerting
- Data refresh scheduling
- Input validation and SQL injection prevention (beyond parameterization)
- Load testing and performance optimization

**"Which approach is most useful for your team?"**
- This depends on the team -- facilitate a genuine discussion rather than pushing one answer
- Data engineers may prefer Genie for quick exploration
- App developers may prefer the custom app approach
- Business stakeholders will love AI/BI dashboards

### Final Retro

**"What will you use on Monday?"**
- Most common: CLAUDE.md for their team repo
- Advanced: TDD workflow, subagents for parallel tasks
- Aspirational: MCP servers for internal tools, Genie spaces for production data

---

## Timing Buffer Guide

### If Running Behind

| Cut This | Saves | Impact |
|----------|-------|--------|
| Slide 4 (Databricks Today) | 3 min | Low -- participants already know the platform |
| Slide 11 (CLAUDE.md Scope Levels) | 2 min | Low -- the concept is covered in Slide 10 |
| Slide 27 (MCP Architecture Full Picture) | 3 min | Low -- detailed diagram, covered conceptually in Slide 25 |
| Slide 29 (Databricks Internal Demo) | 5-8 min | Medium -- impressive but not essential for labs |
| Show & Tell demos | 5 min | Medium -- reduce to 1 min per team or only 2 teams present |
| CLAUDE.md exercise share-back | 3 min | Low -- skip the group discussion, have teams share during breaks |
| Lab 1 Phase 4 (Deploy) | 10 min | Medium -- teams can deploy after the workshop |
| Lab 2 Phase 4 (Dashboard) | 10 min | Medium -- prioritize app and Genie over dashboard |

**Emergency cut (15+ min behind):** Skip the TDD live demo (Slide 18) and use the backup recording during Lab 1 as teams work. Skip Slide 29 entirely.

### If Running Ahead

| Expand This | Adds | How |
|-------------|------|-----|
| Ice breaker discussion | 5 min | Have each team share their boldest prediction and reasoning |
| CLAUDE.md exercise | 10 min | Give teams 25 min instead of 15. Deeper discussion after. |
| TDD live demo | 5 min | Show a second example or take audience requests for what to test |
| Show & Tell | 10 min | Let every team present and have a longer discussion |
| Lab 2 bonus challenges | 15 min | Encourage the MCP server bonus challenge or Chart.js integration |
| Final retro | 10 min | Deeper discussion: "How would you roll this out to your broader team?" |
| Open Q&A | 10 min | Dedicate time for questions about production use cases, security, governance |

---

## Quick Reference: Keyboard Shortcuts for Slides

| Key | Action |
|-----|--------|
| Arrow Down / Right / Space | Next slide |
| Arrow Up / Left | Previous slide |
| N | Toggle speaker notes panel |

Speaker notes appear in a panel at the bottom of the screen when toggled on.
