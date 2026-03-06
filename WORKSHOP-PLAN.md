# Vibe Coding Workshop: Agentic Software Development with Databricks

## Workshop Overview

**Client:** Coles Group - Data & AI Engineering Team
**Facilitator:** David O'Keeffe, Solutions Architect, Databricks
**Format:** Full Day (9:00 AM - 5:00 PM), Onsite at Coles SSC
**Pilot Size:** 5-10 engineers
**Platform:** Coding Agents Databricks App (browser-based terminal)

### Learning Objectives

By end of day, participants will be able to:

1. Write effective PRDs and specification documents that guide AI coding agents
2. Create and maintain CLAUDE.md / agents.md files that encode team standards
3. Use TDD to dramatically improve agentic code generation accuracy
4. Know when to steer the agent vs. let it work autonomously
5. Build, test, and deploy a working application on Databricks using agentic tools
6. Apply these patterns to their daily work (data pipelines, ML, web apps, CI)

### Target Audience

Mixed engineering team (~145 total, 5-10 for pilot):
- Data Engineers
- Data Scientists
- Software Engineers
- ML Engineers
- Analysts

### Platform & Tools

| Tool | Purpose |
|------|---------|
| [Coding Agents Databricks App](https://github.com/dgokeeffe/coding-agents-databricks-apps) | Browser-based terminal with Claude Code, OpenCode, Codex |
| Databricks AI Gateway | Routes all LLM calls, model switching, rate limits, cost tracking |
| MLflow Tracing | Auto-traces every agent session for observability |
| Unity Catalog | Data governance & access control |
| Databricks Asset Bundles (DABs) | CI/CD deployment |
| Databricks Apps | Hosting the built applications |
| [AI Dev Kit Skills](https://github.com/databricks-solutions/ai-dev-kit/tree/main/databricks-skills) | Pre-built Databricks-specific agent skills |

> **Tool-Agnostic Note:** While this workshop uses Claude Code as the primary agentic tool, the patterns and methodology taught here -- PRDs, CLAUDE.md/agents.md, TDD-driven development, context management -- apply equally to Cursor, Windsurf, GitHub Copilot Workspace, and other agentic coding tools. The key differentiator is the methodology, not the tool. Teams should adopt whichever agent fits their workflow, but the discipline of specs, tests, and structured context transfers across all of them.

---

## Agenda

### Morning Block: Foundations (9:00 AM - 12:30 PM)

#### 9:00 - 9:25 | Welcome & The Paradigm Shift (25 min)

**Content:**
- Welcome, introductions, logistics
- "What is Vibe Coding?" - The shift from writing code to directing AI agents
- Live demo: David builds something useful in 5 minutes using Claude Code
- Brief tour of the Coding Agents Databricks App (each participant's environment)
- Verify everyone can access their app instance

**Key Message:** This isn't about replacing developers. It's about amplifying them 10x. The best engineers will be those who can effectively direct AI agents.

#### 9:25 - 10:00 | Session 1: Thinking in Specs (35 min)

**Topic:** Creating PRDs, specifications, and the art of prompting for code

**Content:**
- Why specs matter MORE with AI (garbage in, garbage out at 100x speed)
- Anatomy of a good PRD for agentic development:
  - Clear acceptance criteria (the agent's "definition of done")
  - Constraints & non-functional requirements
  - Data contracts and interfaces
  - Example inputs/outputs
- CLAUDE.md and agents.md files:
  - What they are and why they're your team's "institutional memory"
  - Repository-level vs project-level vs user-level instructions
  - Encoding coding standards, architectural decisions, testing patterns
  - How to evolve them over time based on agent behavior
- Live coding: David shows his personal CLAUDE.md setup and how it shapes agent behavior

**Exercise (10 min):** Each participant writes a CLAUDE.md for one of their current projects. Share and discuss.

**David's Real-World Examples:**
- Show your personal `~/.claude/CLAUDE.md` with Python/git/testing preferences
- Show a project-level CLAUDE.md with architecture decisions
- Demo how adding a single line to CLAUDE.md changes agent behavior

#### 10:00 - 10:15 | Break (15 min)

#### 10:15 - 10:50 | Session 2: TDD-Driven Agentic Development (35 min)

**Topic:** Test-Driven Development as the secret weapon for AI code generation

**Content:**
- Why TDD is exponentially more powerful with AI agents:
  - Tests are unambiguous specifications the agent can verify against
  - The agent runs tests, reads failures, fixes code - a tight feedback loop
  - Tests prevent the agent from "going off the rails"
- The TDD + Agent workflow:
  1. Human writes test (the spec)
  2. Agent implements code to pass tests
  3. Agent runs tests, iterates until green
  4. Human reviews, adds edge case tests
  5. Agent handles edge cases
- Strategies to improve success rates:
  - Start small: one test, one function
  - Provide examples in tests, not just assertions
  - Use descriptive test names as documentation
  - Pin critical behavior with snapshot/approval tests
  - When to break the loop and intervene
- Where human input is still required:
  - Architecture and design decisions
  - Security-sensitive code review
  - Performance optimization strategy
  - Business logic validation
  - Edge cases the agent hasn't seen

**Live Demo:** Write 3 failing tests, then let Claude Code implement the solution. Show the iterative cycle.

#### 10:50 - 11:05 | Session 2.5: Context & Trust (15 min)

**Topic:** How agents use context, and how to calibrate your trust

**Content:**
- **Context management -- the hidden skill:**
  - How agents use context windows: every message, file read, and tool result consumes tokens
  - Why long conversations degrade: the agent "forgets" early instructions, contradicts itself, loses focus
  - When to start fresh vs. continue: new task = new session; related follow-up = same session
  - Rules of thumb for context health:
    - Compact when the agent starts repeating itself or missing obvious things
    - Use subagents for expensive research to protect the main context window
    - Break large tasks into smaller pieces with clear handoff points
    - One concern per session keeps quality high
- **The trust spectrum:**
  - **Verify everything** (new to agents): Read every line, run every test manually, approve every change
  - **Trust but verify** (building confidence): Let the agent work, review diffs, run tests
  - **Delegate and spot-check** (experienced): Give broad instructions, review outcomes not process
  - **Full autonomy** (well-tested patterns): CI runs tests, agent handles the rest
  - How to calibrate: trust more for boilerplate/CRUD, trust less for security/business logic/architecture
  - The cost of over-verification vs. under-verification
- **The core vibe coding loop:**
  1. **Describe** -- Write a clear spec or PRD (what, not how)
  2. **Generate** -- Let the agent implement
  3. **Test** -- Run tests, review output, check behavior
  4. **Refine** -- Provide feedback, add constraints, iterate
  - This loop is the fundamental workflow regardless of tool or language

**Key Message:** Context management is what separates productive agent users from frustrated ones. Learn to feel when the context is degrading and act on it.

#### 11:05 - 12:30 | Lab 1: Build a Data Pipeline with Vibe Coding (85 min)

**Hands-On Exercise:**

Each participant uses their Coding Agents App to build a data pipeline:

1. **Setup** (10 min): Clone a starter repo, review the CLAUDE.md, understand the data schema
2. **Write specs** (15 min): Create a PRD and tests for a data transformation pipeline
3. **Build with agent** (40 min): Use Claude Code / OpenCode to implement:
   - Read raw data from Unity Catalog
   - Apply transformations (cleaning, joins, aggregations)
   - Write to a silver/gold table
   - Add data quality checks (Great Expectations or custom)
4. **Deploy** (20 min): Package as a Databricks Job using DABs

**Starter data:** Use a provided Coles-relevant synthetic dataset (e.g., store transactions, inventory movements) pre-loaded in Unity Catalog.

**Success criteria:** Pipeline runs, tests pass, data quality checks pass, deployed as a scheduled job.

### 12:30 - 1:30 | Lunch (60 min)

### Afternoon Block: Advanced Patterns & Full-Stack Build (1:30 PM - 5:00 PM)

#### 1:30 - 2:15 | Session 3: The Human-AI Partnership (45 min)

**Topic:** When to steer vs. delegate, and advanced agentic patterns

**Content:**
- The spectrum of human involvement:
  - **Full delegation:** "Build me a REST API for X" (agent does everything)
  - **Guided delegation:** "Build X, use FastAPI, follow this pattern" (agent implements within constraints)
  - **Pair programming:** Working side-by-side, reviewing each step
  - **Review mode:** Agent generates, human reviews and requests changes
- AI for different activities:
  - **Code generation:** Best for boilerplate, CRUD, standard patterns, glue code
  - **Code review:** Agent finds bugs, suggests improvements, checks standards
  - **Testing:** Agent writes tests from specs, generates edge cases, runs test suites
  - **Documentation:** Agent generates docs from code, keeps them in sync
  - **Refactoring:** Agent handles mechanical refactors, pattern migrations
  - **Debugging:** Agent reads logs, traces issues, suggests fixes
- Advanced patterns:
  - Multi-agent workflows (Claude Code + MCP servers)
  - Using skills to encode domain-specific knowledge
  - Workspace sync: code in browser, deploy to Databricks
  - MLflow tracing for agent observability

**David's Real-World Demo:**
- Show how you use agents for day-to-day SA work:
  - Reading customer emails, researching questions, drafting responses
  - Building demos and POCs at speed
  - Creating slide decks and documentation
  - Querying internal systems (Salesforce, JIRA, Slack)
- Show the "vibe" plugin marketplace and how skills encode expertise

#### 2:15 - 3:00 | Session 4: Production Patterns & Governance (45 min)

**Topic:** Taking agentic development from experiments to production

**Content:**
- **AI Gateway as the control plane:**
  - The 3-tier MCP model:
    - **Managed MCP:** Databricks-hosted connectors (Unity Catalog, DBSQL, Vector Search) -- zero config
    - **External MCP:** Third-party services (Slack, JIRA, GitHub) -- configure endpoints and auth
    - **Custom MCP:** Team-built servers for internal systems -- full flexibility
  - Model routing with fallback chains: primary model (Claude Sonnet 4) -> fallback (GPT-4o) -> cost-optimized (Haiku) for different task types
  - Guardrails configuration: input/output content filters, PII detection, topic restrictions, custom safety rules
  - Pay-per-token vs. provisioned throughput: when to use each, cost modeling for team-wide adoption
  - Rate limiting per user/team
  - Cost tracking and budgets with per-project attribution
  - Audit logging of all LLM interactions
- **MLflow Tracing:**
  - Every Claude Code session auto-traced end-to-end
  - MLflow 3 features for agent observability:
    - Auto-tracing agent sessions with full tool call lineage
    - Span-level metadata: latency, token counts, model used, cost per call
    - Comparing token usage across approaches (e.g., TDD vs. freeform prompting)
  - Debugging hallucinations via trace inspection: identify where the agent went wrong, what context it had, what it missed
  - Building evaluation datasets from traced sessions
  - Measuring and optimizing cost per task type
- **Unity Catalog + Agents:**
  - Agents respect UC permissions -- an agent can only access data the user can access
  - Lineage tracking for AI-generated tables: trace which agent session created or modified a table
  - Function-level governance: agent-callable functions registered in UC with access controls
  - Data classification propagation: sensitivity labels flow through agent-created assets
- CI/CD with DABs:
  - Agent generates code -> human reviews PR -> DABs deploy
  - Testing in the loop: agents run tests before PR
  - Asset bundles for reproducible deployments
- Team adoption strategy:
  - Start with champions (the people in this room)
  - Build shared CLAUDE.md files for team standards
  - Create skill libraries for common patterns
  - Measure: velocity, quality, developer satisfaction

#### 3:00 - 3:15 | Break (15 min)

#### 3:15 - 4:30 | Lab 2: Build & Deploy a Full-Stack App (75 min)

**Hands-On Exercise:**

The capstone challenge - build and deploy a complete application:

1. **Design** (10 min): Write a PRD for a Databricks App that:
   - Has a React/HTML frontend
   - FastAPI/Flask backend
   - Reads from the Unity Catalog tables created in Lab 1
   - Displays data in a dashboard/interactive view
   - Includes at least one AI-powered feature (e.g., natural language query, summary generation)

2. **Build with agent** (45 min):
   - Use the Coding Agents App to build the frontend, backend, and data layer
   - Apply TDD: write tests first, let the agent implement
   - Use CLAUDE.md to enforce patterns and standards
   - Leverage pre-installed Databricks skills for common tasks

3. **Deploy** (15 min):
   - Package as a Databricks App using DABs
   - Deploy to the Coles Databricks workspace
   - Verify it runs and is accessible

4. **Share** (5 min): Brief demo to the group

**Success criteria:** Working app deployed on Databricks, accessible via browser, demonstrates data from Lab 1 pipeline.

#### 4:30 - 5:00 | Wrap-Up & Next Steps (30 min)

**Content:**
- Gallery walk: Each participant demos their app (2-3 min each)
- Reflection: What worked? What surprised you? Where did you get stuck?
- Key takeaways:
  1. Specs and CLAUDE.md are your leverage multipliers
  2. TDD + agents = deterministic outcomes
  3. Know when to steer and when to let go
  4. Start small, iterate, build confidence
- Next steps:
  - Roll out to wider team (full workshop)
  - Establish team CLAUDE.md and coding standards
  - Set up shared skill libraries
  - Farbod & Swee Hoe as internal champions
  - David available for follow-up support
- Q&A

---

## Day 2 (Optional): Going Deeper

For teams that want to extend the workshop or schedule a follow-up session, the following topics build on Day 1 foundations.

### CI/CD Integration (90 min)
- PR review workflows with agents: automated code review on every pull request
- Automated test generation in CI: agents write missing tests as a pipeline step
- Branch-based agent workflows: agent opens PR, runs tests, requests review
- DABs + GitHub Actions / Azure DevOps integration patterns

### Production Readiness (90 min)
- Security review checklist for agent-generated code: OWASP top 10, dependency scanning, secrets detection
- Performance testing: load testing agent-built APIs, query optimization review
- Monitoring and alerting: tracking agent-deployed services in production
- Incident response: debugging production issues with agent assistance

### Custom Skills & Plugins (90 min)
- Building team-specific agent skills for Coles patterns (e.g., standard data pipeline templates, naming conventions)
- Packaging skills for reuse across the team
- Skill versioning and distribution via internal registries
- Domain-specific skills: retail analytics, supply chain, inventory management

### Advanced MCP (90 min)
- Building custom MCP servers for internal Coles systems
- Deploying MCP servers on Databricks Apps
- Connecting agents to internal APIs, databases, and tools
- Security considerations: authentication, authorization, audit trails for MCP connections

---

## Pre-Workshop Requirements

### For Coles Platform Team (Farbod & Swee Hoe)

**Must be completed BEFORE workshop day:**

1. **Deploy Coding Agents Databricks App** for each participant:
   - Follow deployment guide at `docs/deployment.md` in the repo
   - Each participant gets their own app instance
   - Configure AI Gateway endpoint with appropriate models (Claude Sonnet 4, GPT-4o, etc.)
   - Set rate limits per user
   - Verify MLflow tracing is working

2. **Unity Catalog setup:**
   - Create a workshop catalog: `workshop_vibe_coding`
   - Create schemas per participant: `workshop_vibe_coding.<username>`
   - Grant CREATE TABLE, SELECT, MODIFY on their schema
   - Pre-load synthetic dataset (provided by David)

3. **Network / ZScaler:**
   - Ensure the Databricks App URLs are accessible from conference room WiFi
   - Whitelist any necessary endpoints for AI Gateway
   - Test end-to-end: browser -> Databricks App -> AI Gateway -> model endpoint

4. **Git integration:**
   - Each participant needs a Git repo (can be personal or shared)
   - Databricks Git integration configured
   - PAT or OAuth setup for workspace sync

### For Participants

**Before the day:**
- Laptop with a modern browser (Chrome recommended)
- Access to their Coles Databricks workspace
- Basic familiarity with Python (any level of data engineering/science/ML is fine)
- Optional: Think of a project they'd like to try building with an agent

**No software installation required** - everything runs in the browser via the Coding Agents App.

---

## Facilitation Notes

### Key Principles

1. **Show, don't tell.** Every concept is demonstrated live before participants try it.
2. **Real data, real problems.** Use Coles-relevant scenarios wherever possible.
3. **Fail forward.** When the agent gets something wrong, use it as a teaching moment about human oversight.
4. **Inclusive of all skill levels.** Data scientists and analysts should feel as welcome as software engineers.

### Timing Flex

- If Lab 1 runs long, compress Session 3 to 30 min
- If participants are advanced, extend Lab 2 and reduce lecture time
- If environment issues arise, have a backup demo ready on David's laptop

### Materials to Prepare

- [ ] Synthetic dataset pre-loaded in Unity Catalog
- [ ] Starter repo with CLAUDE.md template and test scaffolding
- [ ] Slide deck for presentation sections
- [ ] Printed quick-reference cards (CLAUDE.md syntax, common prompts, keyboard shortcuts)
- [ ] Backup: Pre-recorded demos in case of connectivity issues

---

## Post-Workshop

### Immediate (Same Week)
- Share workshop materials and recordings with participants
- Collect feedback survey
- Debrief with Yass, Swee Hoe, Farbod on what to refine

### Short-Term (2-4 Weeks)
- Refine content based on pilot feedback
- Schedule full team workshop (end of March / early April)
- Help Coles establish team-wide CLAUDE.md standards

### Long-Term
- Support Coles in building internal skill libraries
- Monthly office hours for agentic development questions
- Track adoption metrics: developer velocity, code quality, satisfaction
