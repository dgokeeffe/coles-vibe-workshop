# Harnesses Are Everything — Alex Ker

**Source:** https://x.com/thealexker/status/2045203785304232162
**Author context:** Contributes to Roo Code, DeepAgent CLI, HumanLayer.
**Saved:** 2026-04-19 as reference material for the Coda Vibe Coding Workshop.

---

## Thesis

*"Engineers used to argue about IDEs, now we argue about harnesses."*

**If the model is the source of intelligence, the harness is what makes that intelligence useful.** A harness is scaffolding that manages context (sessions, compression) and makes tool calls / I/O / guardrails work around the stateless LLM. Think `while (have next message) do {tool}`.

Three surfaces separate harnesses that compound your output from ones that compound your mistakes. All three still require human judgment.

## 1. Keep config files lean and human-written

- **Instruction budget** (Kyle @ HumanLayer): frontier LLMs can follow only a few hundred instructions before entering the *"dumb zone"* where they miss relevant ones amidst the bloat. Too many instructions = functionally encouraging hallucination.
- **Human-written CLAUDE.md beats LLM-generated.** ETH research: LLM-generated system prompts degrade performance *and* cost ~20% more in inference.
- Every token in CLAUDE.md fights for its place — it's injected globally on every session.
- Minimal requirements: what the project is, who the end users are. That's it.

### Progressive disclosure

Don't front-load everything. Let the agent pull context when needed, and let it know what exists via descriptive file names.

- **CLIs**: models already know `kubectl` or `gh` from training. The real test is the internal tool nobody outside your company has used. Put a single line in CLAUDE.md: *"use uv for Python package management, run `uv --help` to discover subcommands before assuming syntax."* Don't paste the whole reference.
- **Skills**: the whole industry has converged here. At session start only the name and description of each skill loads; the full SKILL.md body is read only when the agent decides it's relevant. Write clear descriptions → the agent can match without ever reading the body.
- **MCP tools**: this is where harnesses diverge.
  - **Claude Code** ships with built-in MCP tool search — lightweight index at start, full schemas on demand. Anthropic reports 85%+ context reduction.
  - **Codex / OpenCode** load all configured MCP tool definitions at session start. OpenCode's docs warn users to limit enabled servers because context fills fast.
  - If your harness doesn't index for you, be selective per project, write specific keyword-rich tool descriptions, disconnect irrelevant MCPs.

## 2. R.P.I. framework — work at a higher abstraction

Every prompt should do exactly **one** of three things:

| Step | What it does |
|---|---|
| **Research** | Give the agent the problem statement; let it explore the codebase (prior art, function definitions, file relationships). **No action taken.** |
| **Plan** | Agent writes a step-by-step execution plan. Human reviews and verifies. *"Outsourcing thinking or being lazy at this step will cost you dearly later."* |
| **Implement** | Execute the approved plan in a new context window. Use subagents for any subtask whose intermediate state doesn't need to live in the main window. |

> *"Operating a harness is leading it to behave the way the best staff engineers approach problem-solving: break problems into subproblems, plan before implementing, get a second set of eyes on the plan. The abstraction has shifted from line-by-line code to prompts; the discipline has not changed."*

### R.V.P.I. — the missing validation step (extension by David O'Keeffe, 2026-04-19)

> **Deeper treatment of this idea:** see `rvpi-validate-step.md` in this folder. That note covers the three failure modes (stale / conflicting / poisoned context), four practical mechanisms (trust-weighted retrieval, canonical state auditing, circuit breakers, immutable audit logging), and the security-posture reframe: *"retrieved memory should be treated as untrusted input until validated."*

R.P.I. has a gap between Research and Plan: **the retrieved context itself is never validated**. The agent researches, pulls memory from past sessions, retrieves files. But before planning on top of it — is that retrieved memory still accurate? Stale, conflicting, or poisoned context makes the best plan worthless.

| Step | What it does | Distinct from... |
|---|---|---|
| **Research** | Gather everything potentially relevant. Exploratory. | |
| **Validate** *(new)* | Adjudicate the retrieved context. Is it still true? Are sources consistent? Does memory match current code? | Research (gather ≠ audit); Plan (critical review ≠ constructive synthesis) |
| **Plan** | Synthesize validated inputs into a step-by-step plan. | |
| **Implement** | Execute in a fresh context; delegate to subagents where summaries suffice. | |

**Where Validate matters most:**

| Input | V-step check |
|---|---|
| Retrieved memory from past sessions | Still current? Or written against a schema that's since changed? |
| CLAUDE.md | Has the project drifted from what this says? |
| Skill descriptions | Does the skill's body still match its description? |
| Agent-generated docs in the repo | Contradicting each other? About to cite a prior hallucination? |
| RAG / semantic search results | Top-k is genuinely relevant, or just superficially similar? |

**The failure mode this catches:** an agent researches, pulls stale/poisoned context, plans on top of it, and produces a perfectly structured plan built on a lie. The plan looks great. The implementation runs. The outcome is subtly wrong. Nobody can point to which step broke — because the broken step wasn't in R.P.I.

**Memory governance specifically:** the poisoning mode where an agent adds a wrong rule to CLAUDE.md → follows it forever → every future session inherits the poison. No amount of R or P or I fixes that without a V. Connects to the Sycophancy slide's "Reproducibility — lock the inputs" defence, but V is broader: reproducibility locks inputs *after* you've validated them; V is the step where you decide what's worth locking.

## 3. Use subagents to maintain clean context

**Core heuristic:** use a subagent when a *summary* of the work is sufficient for your main agent. If you'll want to ask *"how does this connect to what I looked at earlier"*, keep it in the primary window.

### Two patterns

| Pattern | When | How it works |
|---|---|---|
| **Parallel fan-out** | Investigation / research (breadth) | Agent generates 3 candidate theories for a root cause, spins up one subagent per theory, gets back 3 summaries, synthesizes — main context never sees the logs. Also useful when you want outputs from multiple models concurrently. |
| **Pipelines** | Multi-perspective evaluation (depth) | Push a feature through sequential roles — UX designer, architect, devil's advocate. Each stage takes the previous output and adds analysis. Main agent gets layered evaluation without holding all three lenses in context at once. |

> Bonus: use a frontier model as a judge to consolidate the pipeline's responses and raise confidence.

## 4. Commit to one harness

Temptation when a harness fails: switch harnesses. Resist.

- Every harness has different constraints, context strategies, tool routing logic.
- Constantly switching = lose the institutional knowledge encoded in your config files; restart the failure-case log from zero.
- **Pick the harness that covers the majority of your team's use case, then treat every failure as a data point.** What broke, at which step, under what conditions. Add that to your .md files; iterate prompting strategies accordingly.
- *"The best harness is the one you have customized and iterated on with human engineering."*

## The one-sentence takeaway

*"The harness, not just the model, is where your engineering judgment makes a difference."*

---

## Connection to this workshop

This article reframes what the workshop is teaching: we're not just teaching how to prompt — we're teaching attendees to **own their harness**.

| Article concept | Workshop slide / artifact |
|---|---|
| Instruction budget / "dumb zone" | Slide 24 What Are Tokens + Slide 25 Context Windows (indirectly) |
| Human-written CLAUDE.md > LLM-generated | Slide 14 CLAUDE.md in Action — *this is not currently named as a rule* |
| Progressive disclosure via descriptive names | Not explicitly named — but the skills pattern is in Slide 17 Power Tools |
| R.P.I. framework (Research → Plan → Implement) | Slide 19 Small Steps + Slide 18 Verification Patterns (related but not the same framing) |
| Subagents: fan-out vs pipelines | Slide 17 Power Tools + Appendix slide on Subagents |
| Commit to one harness; log failures to .md | **Missing** — no guidance on iterating CLAUDE.md over time |

**Ideas to consider for next iteration:**

1. **Rename Slide 17 "Power Tools" → "Harness Components"** — reframes the four items (subagents, skills, hooks, plugins) as *parts of a system you tune*, not features. Matches the article's mental model.
2. **Add one line to the CLAUDE.md slide**: *"Human-written beats LLM-generated. ETH study: LLM-generated prompts degrade performance AND cost 20% more."* Cheap, credible, immediately actionable.
3. **Add "treat failures as data, commit them to CLAUDE.md"** as a post-lab reflection prompt. Currently labs end at "it works"; the article's thesis is that the *real* compounding happens between sessions, in what you add to your config files.
4. **R.P.I. is a better-named version of the Small Steps principle.** Consider whether slides 18/19 could be consolidated under the R.P.I. rubric — *Research, Plan, Implement, and each prompt does one of these.* More memorable than the current "small steps" mantra.
5. **Parallel fan-out / pipelines** as named subagent patterns — would slot into Power Tools slide 17 or an appendix deep-dive. Attendees probably won't use them Monday but the names stick.

## Cross-reference to the Eric/Anthropic talk (`vibe-coding-in-prod-talk.md`)

Both articles independently converge on:

- **Spend time before prompting** — Eric: 15–20 min of context-gathering; Alex: R.P.I. with genuine Research and Plan phases
- **Subagents keep main context clean** — Eric: verify via abstractions you don't read; Alex: use subagents when a summary is sufficient
- **Instruction / specification > brute force prompting** — Eric: be Claude's PM; Alex: own the harness config

The convergence is useful: the workshop isn't building theory on a single source — it aligns with independent senior-practitioner guidance from both Anthropic (Eric) and the open-source harness community (Alex Ker / HumanLayer).

## The missing workshop concept: "own the harness"

Neither the Eric talk nor this article uses "harness" the same way, but both arrive at the same conclusion: **the config files + tool choices + subagent patterns you iterate on are the real asset**, not the prompts themselves.

The workshop currently teaches prompt-level technique (Small Steps, Verification, Sycophancy defences) but stops short of teaching attendees to *own their config* over time. A single closing-block slide like *"Your real asset is the CLAUDE.md + skills + hooks you iterate on — the prompts are ephemeral"* would be the missing piece.
