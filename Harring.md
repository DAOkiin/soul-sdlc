# Harring.md

Selected direct quotes on harness engineering from one source file, kept in narrative order so context is preserved.

## Source
- File: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md`
- Source block: parsed fragment of OpenAI article "Harness engineering: leveraging Codex in an agent-first world"

## Quotes (Harring)

### Q-001 — Environment as bottleneck
> Early progress was slowerthan we expected, not because Codex was incapable, but because the environment was underspecified. The agent lacked the tools, abstractions, and internal structure required to make progress toward high-level goals. The primary job of our engineering team became enabling the agents to do useful work.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1716`

### Q-002 — Capability gap framing
> When something failed,the fix was almost never “try harder.” Because the only way to make progress was to get Codex to do the work, human engineers always stepped into the task and asked: “what capability is missing, and how do we make it both legible and enforceable forthe agent?”

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1723`

### Q-003 — Human constraint
> Because the fixed constraint has been human time and attention, we’ve worked to add more capabilities to the agent by making things like the application UI, logs, and app metrics themselves directly legible to Codex.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1739`

### Q-004 — Long-running agent loops
> We regularly see single Codex runs work on a single task for upwards of six hours (often while the humans are sleeping).

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1773`

### Q-005 — Map, not manual
> Context management is one ofthe biggest challenges in making agents effective at large and complex tasks. One ofthe earliest lessons we learned was simple: give Codex a map, not a 1,000-page instruction manual.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1777`

### Q-006 — Why monolithic AGENTS fails
> Context is a scarce resource. A giant instruction file crowds out the task,the code, and the relevant docs—so the agent either misses key constraints or starts optimizing forthe wrong ones.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1781`

### Q-007 — Verification requirement
> It’s hard to verify. A single blob doesn’t lend itselfto mechanical checks (coverage,freshness, ownership, cross-links), so drift is inevitable.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1790`

### Q-008 — AGENTS as table of contents
> So instead oftreating AGENTS.md as the encyclopedia, we treat it as the table of contents. The repository’s knowledge base lives in a structured docs/ directory treated as the system of record.A short AGENTS.md (roughly 100 lines) is injected into context and serves primarily as a map, with pointers to deeper sources of truth elsewhere.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1792`

### Q-009 — Mechanical enforcement + doc-gardening
> We enforce this mechanically. Dedicated linters and CI jobs validate that the knowledge base is up to date, cross-linked, and structured correctly.A recurring “doc-gardening” agent scans for stale or obsolete documentation that does not reflect the real code behavior and opens fix-up pull requests.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1846`

### Q-010 — Repo-local visibility rule
> From the agent’s point of view, anything it can’t access in-context while running effectively doesn’t exist. Knowledge that lives in Google Docs, chat threads, or people’s heads are not accessible to the system. Repository-local, versioned artifacts (e.g., code, markdown, schemas, executable plans) are all it can see.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1858`

### Q-011 — Invariants over micromanagement
> Documentation alone doesn’t keep a fully agent-generated codebase coherent. By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1913`

### Q-012 — Speed without decay
> This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it’s an early prerequisite: the constraints are what allows speed without decay or architectural drift.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1928`

### Q-013 — Remediable lint feedback
> Because the lints are custom, we write the error messages to inject remediation instructions into agent context.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1956`

### Q-014 — Central boundaries, local autonomy
> organization: enforce boundaries centrally, allow autonomy locally. You care deeply about boundaries, correctness, and reproducibility. Within those boundaries, you allow teams—or agents—significant freedom in how solutions are expressed.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:1962`

### Q-015 — Autonomy still needs scaffolding
> This behavior depends heavily on the specific structure and tooling ofthis repository and should not be assumed to generalize without similar investment—at least, not yet.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:2034`

### Q-016 — Entropy control via golden principles
> Instead, we started encoding what we call “golden principles” directly into the repository and built a recurring cleanup process. These principles are opinionated, mechanical rules that keep the codebase legible and consistent forfuture agent runs.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:2044`

### Q-017 — Continuous debt paydown
> This functions like garbage collection. Technical debt is like a high-interest loan: it’s almost always betterto pay it down continuously in small increments than to let it compound and tackle it in painful bursts.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:2054`

### Q-018 — Where discipline moved
> What’s become clear: building software still demands discipline, but the discipline shows up more in the scaffolding ratherthan the code. The tooling, abstractions, and feedback loops that keep the codebase coherent are increasingly important.

Source: `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-Описание_запросов_в_репозиториях.md:2068`
