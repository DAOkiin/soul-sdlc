# Programmatic state and transition management for AI agents in 2025–2026

## Problem framing and what “state” means in your example

Your “work3” example is less about “chat memory” and more about **a durable, programmatically-controlled execution process**: an agent enters a well-defined stage, initializes stage-specific state on first entry, mutates that state over time, and then performs an explicit transition (e.g., “ready to merge to main”) with cleanup (“delete work3”). This is the same core problem that workflow engines and state-machine orchestration libraries have solved for years—now reappearing in the “agentic” world because LLMs make control-flow more dynamic and tool calls more failure-prone. citeturn1search23turn3search0turn3search1

A useful way to decompose “state” for agentic systems (and to map directly to your “work3” branch analogy) is:

- **Workflow/process state**: “Which step/stage am I in, what are the guard conditions to move, what is the next step?” This is what makes transitions explicit and machine-checkable. citeturn1search23turn3search12turn1search5  
- **Execution history / audit trail**: “What happened, in what order, and what exactly was decided?” This is what lets the agent (or an operator) answer “what’s going on?” in a couple of commands—by querying history snapshots or an event log. citeturn3search1turn7search0turn7search9  
- **Working memory / knowledge memory**: facts and summaries carried across steps (short-term) or across runs (long-term). This is helpful, but by itself rarely guarantees correct transitions or resumability after failure. citeturn7search24turn2search2turn1search11  
- **Artifact state**: files, patches, test outputs, PRs/branches—i.e., the concrete objects produced while “work3” is active. In software engineering workflows, Git and PR tooling often become the artifact state store. citeturn1search10turn1search30turn1search22  

The recent popularity of “agents that actually do things” (for example OpenClaw) is one reason this topic is becoming urgent: these systems commonly need to pause, resume, branch, and keep careful track of tool outputs, credentials, and decisions. citeturn6news35turn6search0turn6search6

## Explicit state-machine and graph workflow orchestrators

A major cluster of “stateful agent” projects solves your exact concern—**programmatic transitions plus persistent state**—by modeling execution as a **graph/state machine** where a **state object** is carried across nodes/steps and can be checkpointed.

### LangGraph-style checkpointed state graphs

LangGraph describes itself as orchestration for long-running, stateful agents, and its core mechanism for “state” is a **persistence layer** implemented via **checkpointers**. When configured, the checkpointer saves a checkpoint of graph state at every “super-step,” storing checkpoints under a “thread” concept so you can access state after execution. This directly enables features like **human-in-the-loop**, **fault tolerance**, and **time travel** (forking from prior checkpoints). citeturn0search13turn3search0turn3search13

Two details are especially relevant to your “work3 creates state on first entry, persists through the stage” requirement:

- **Interrupt/pause semantics**: execution can pause at defined points, save state, and wait indefinitely until resumed—making “stage gates” a first-class construct rather than ad hoc “if” statements. citeturn3search7turn3search0turn3search21  
- **Queryable history**: you can retrieve full state history for a thread via `get_state_history`, which returns ordered snapshots (practically: “show me what’s going on” as a simple query). citeturn7search0turn7search8turn3search13  

LangGraph’s ecosystem increasingly treats “state” as something you can persist in standard backends (e.g., Redis integrations for checkpoint persistence, or other external stores), which matters if you want state survivable across deploys and crashes. citeturn0search17turn3search5turn3search30

### Microsoft Agent Framework workflows and sessions

Microsoft’s newer Agent Framework explicitly positions **Workflows** as graph-based orchestration with **type-safe routing**, **checkpointing**, and human-in-the-loop support, and combines this with **session-based state management** and observability. citeturn3search2turn2search30turn7search23

The “session” concept is very close to what you describe as “work3 state that appears on first entry”: when a workflow is converted into an agent, the framework creates a **session to manage conversation state and checkpoints**, routes input messages through the start executor, and translates workflow events into agent responses. citeturn3search16turn3search2turn3search12

This is also part of a broader shift in the Microsoft stack: the migration materials emphasize that Agent Framework centers on a typed, graph-based workflow model compared to message-centric orchestration in earlier AutoGen patterns. citeturn2search1turn0search7turn2search30

### Cloud state machines as explicit orchestration

If you want transitions to be *not just programmatic, but also auditable and visually inspectable*, cloud workflow services like AWS Step Functions remain relevant. Amazon explicitly frames Step Functions as a coordinator for multi-step generative AI workflows (including parallelizing model calls and integrating RAG patterns). citeturn1search5turn1search12

This is often attractive for “agent + process” systems because Step Functions state machines force you to name states and transitions, which creates built-in clarity (“what step are we in?”) even if the agent’s internal reasoning is messy. citeturn1search12turn1search5

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["LangGraph checkpointing state graph diagram","Microsoft Agent Framework workflow graph diagram","AWS Step Functions state machine diagram","Temporal event history workflow diagram"],"num_per_query":1}

## Durable execution engines as the “state layer” for agents

A second cluster of projects approaches your question from the opposite direction: instead of “agent framework adds state,” they say **state is an infrastructure primitive**. These systems typically provide a durable log/history, replay, retries, and long-lived pause/resume—so an agent becomes a workflow participant rather than the workflow runtime.

### Temporal: deterministic workflows + event history replay

Temporal’s model is built around **durable execution**: the system appends events to an **Event History** to track progress, enabling recovery after crashes and continuation without losing already-completed results. citeturn3search1turn7search9turn3search15

For agentic systems, Temporal emphasizes a key idea: when recovering from a crash, the workflow “replays” progress rather than asking the LLM to re-decide past decisions; the workflow uses Event History as a record of what already occurred, enabling the agent to resume exactly where it left off. citeturn3search4turn3search1turn7search13

Temporal also has a strong answer to your “a couple of commands to understand what’s going on” requirement:

- It treats a workflow like a **stateful service** that can receive messages (Queries, Signals, Updates), where Queries are used to read state and Signals/Updates can change behavior. citeturn7search2turn7search10turn7search25  
- Its documentation and messaging model explicitly connect “workflow state” to replayed history: query results should be based on deterministic replay of completed steps. citeturn7search17turn3search15turn7search9  

Several agent-focused integrations show how Temporal is being positioned as a practical “agent state engine.” For example, PydanticAI documents a `TemporalAgent` wrapper where I/O work (model requests, tool calls) is offloaded to activities while deterministic workflow code remains replayable. citeturn3search6turn3search23turn7search2

### Restate, DBOS, Resonate, Inngest: durable execution becomes a commodity

A notable 2024–2026 trend is the rise of multiple “durable execution” platforms beyond Temporal, explicitly marketing themselves as state/transition primitives for workflows and agents:

- **Restate** frames durable execution as a way to implement consistent state machines, session state, or agent context/memory; it emphasizes that state updates are journaled alongside execution steps and are scoped per workflow/object with a single-writer guarantee. citeturn4search0turn4search6turn4search4  
- **DBOS** documents a workflow model where interrupted execution is recovered from the last completed step, aiming to simplify resilient background tasks and AI agents. citeturn4search11  
- **Resonate** documents checkpoint/replay as the mechanism for durable execution (resume after the host process crashes/restarts). citeturn4search9turn4search24turn4search12  
- **Inngest** presents “durable functions” that replace queues/state management/scheduling; its multi-step functions support waits (hours to up to a year), step-level retries, and conditional execution, and it treats steps as discrete units that can be retried/debugged/recovered. It also uses step IDs specifically to memoize step state across versions. citeturn5search17turn5search5turn5search11turn5search13  

This category directly matches your intuition: if transitions and state are handled by a durable execution engine, an agent can be “aware” of where it is by reading the authoritative workflow state/history rather than reconstructing the world from chat logs.

A real tradeoff is that replay-based durability imposes constraints (e.g., deterministic workflow logic and careful handling of non-deterministic operations), which these engines address via patterns like isolating I/O into “activities/steps.” citeturn3search15turn4search4turn3search23

## In-framework “Flows/Workflows” with persisted context

A third cluster sits between “agent frameworks” and “workflow engines”: frameworks that explicitly add workflow state, persistence, and pause/resume inside the framework itself.

### LlamaIndex Workflows: Context as state across steps and runs

LlamaIndex Workflows uses a `Context` object to maintain state within and between runs. Their documentation shows that you can create a Context for a workflow, pass it into `.run()`, and optionally save and restore it for persistence across runs. citeturn1search4turn1search11turn1search27

This aligns closely with your “work3 state created on first entry” idea: a Context can serve as the container for stage-specific data, counters, partial outputs, and “done/not done” flags that survive across step boundaries (and potentially across executions). citeturn1search11turn1search4

### CrewAI Flows: explicit flow state + persistence decorator

CrewAI’s Flow documentation makes state management an explicit concept: Flow state is described as “the backbone” for sophisticated workflows, letting you maintain context and share data between steps. citeturn2search0turn2search11

Crucially for your question, CrewAI includes an explicit persistence mechanism via an `@persist` decorator, described as enabling automatic state persistence across restarts or different workflow executions. citeturn2search3turn2search0

CrewAI also distinguishes “process/workflow state” from “memory” in the classic sense: when memory is enabled, the crew automatically extracts facts from task outputs and stores them, then recalls relevant context before each task. citeturn2search2turn2search11

### AutoGen and lightweight orchestration: state often “spills into messages”

Microsoft AutoGen popularized multi-agent orchestration via message passing, but the project’s own discussions highlight a limitation: once you introduce retries, conditional paths, or long-running tasks, the “context” winds up scattered across exchanged messages and application logic rather than concentrated in a single, structured state object. citeturn0search7turn0search18

This is exactly why many teams gravitate toward graph/state-machine models (LangGraph-like or Agent-Framework-like) when they care about programmatic transitions and robust checkpointing. citeturn2search1turn3search0turn3search12

### OpenAI Swarm: teaches handoffs, but not “durable state”

OpenAI’s Swarm repository states its goal as lightweight, controllable, testable coordination via Agents and handoffs. citeturn2search6turn2search9  
However, community discussions around Swarm explicitly note it is (almost) entirely client-side and does not store persistent state between calls, reinforcing that Swarm is mainly educational rather than a “state engine.” citeturn2search25turn2search9

## Coding agents and Git-style “work states” mapped to branches and PRs

Your “work3 → merge to main → delete work3” is also a natural fit for **developer-facing agents**, where Git becomes a first-class “artifact state machine.”

### GitHub-native agents and PR workflows

GitHub’s documentation for its coding agent describes a workflow where the agent creates a new branch based on a base branch, then pushes changes into a pull request targeting that branch. citeturn1search10  
GitHub’s own blog positions this as operating “directly within the pull request workflow,” automating branch creation, commits, and reviews, with steps logged and visible—i.e., externalizing agent execution into a workflow artifact that humans can inspect. citeturn1search30

### OpenHands and SWE-agent class tools

OpenHands provides GitHub workflow guides (e.g., PR review automation). Its GitHub workflow examples explicitly rely on Actions permissions that allow creating and approving pull requests—turning the PR itself into the boundary between “work in progress” and “ready to merge.” citeturn1search0turn1search6turn1search21

SWE-agent similarly positions itself around taking an issue and producing a pull request; even in demo pipelines, “inference” creates a PR and later steps evaluate it. citeturn1search14turn1search22  
AWS sample work also documents “remote SWE agents” that autonomously create pull requests, showing how common “branch/PR as state” has become. citeturn1search26

### Branching strategies for multiple agents

Some vendors now document explicit branching strategies for parallel agent work, such as a rolling integration branch with sub-branches per agent, then PRs into the integration branch before merging to main—again reflecting “stateful staged work” as a Git-native process. citeturn1search33

## A concrete architecture pattern for “work3 state → merge → cleanup”

Below is an implementation pattern that appears repeatedly across the projects above, expressed in the vocabulary of your example. The key idea is: **the agent should not infer transitions**. Transitions are **code-defined**, with state stored in a system designed for resumability and auditability.

### Define state as a typed object, not “implicit context”

In graph/state-machine orchestrators, the “work3 state” is a structured object carried between steps (nodes/executors) and checkpointed. LangGraph’s persistence model centers on checkpointing graph state per thread, and its time-travel patterns explicitly rely on retrieving checkpoint and state history by `thread_id`. citeturn3search0turn7search0turn7search8  
Microsoft Agent Framework emphasizes type safety and validation in workflows, which is effectively the same recommendation: transitions should move typed messages/state along edges, not free-form blobs. citeturn3search12turn3search2

### Make “first entry creates state” an explicit transition (initialization step)

In practice, you model “enter work3” as a transition that:

1. Creates the workflow session/thread (or uses an existing one).
2. Initializes `work3` fields in state (e.g., branch name, baseline commit SHA, acceptance criteria).
3. Records the transition in history (checkpoint or event log).

This is natural in checkpointed state graphs (checkpoint on node entry/exit) citeturn3search0turn3search14 and in durable execution engines (append an event / journal step that becomes replayable ground truth). citeturn3search1turn4search6turn4search4

### Provide “status in two commands” via history queries, not log scraping

Two robust, widely-used mechanisms:

- **Checkpoint history listing** (graph systems): LangGraph explicitly provides `get_state_history` to list snapshots for a thread, and time travel uses that history to find checkpoint IDs. citeturn7search0turn7search8turn3search13  
- **Stateful workflow queries** (durable engines): Temporal treats workflows like stateful services with Queries/Signals/Updates, and it maintains Event History as the authoritative record used for replay and state reconstruction. citeturn7search2turn7search9turn7search25  

In other words, “status” should be a query endpoint over the authoritative state (plus optionally a short summary derived from the most recent checkpoints/events), not an LLM prompt that re-interprets raw logs.

### Gate merge/cleanup with explicit guard conditions and optional human approval

If “merge to main” is a transition, it should be guarded by checks (tests pass, lint pass, acceptance criteria satisfied). In durable engines, the pattern is to pause workflows for human approval and then resume exactly where they stopped; Temporal and related material present pause/resume as first-class for human-in-the-loop. citeturn1search28turn3search23turn3search7

Then “cleanup” (delete the work branch/workspace) becomes a final transition that is recorded, so the system can prove it happened (or retry it safely). This “record transitions so they can be retried without ambiguity” is one of the core reasons durable execution logs exist. citeturn3search1turn4search6turn4search12

### Security note: persistent state often contains credentials and tool authority

Because agent state can include API keys, auth tokens, tool permissions, and local execution context, security teams have started treating agent deployments as high-risk. CrowdStrike specifically frames OpenClaw deployments as a new attack surface requiring visibility into process execution and tool usage, and other reporting highlights corporate bans due to cybersecurity concerns. citeturn6search6turn6news38turn6news41  
This matters for your design because “state” is not just a convenience feature; it is also sensitive data that must be protected if you persist it.

## Open gaps and active research directions

Despite many engineering solutions, several gaps remain—especially around agents that *programmatically* understand and respect transitions:

A lively research direction is **generating state machines for multi-agent systems automatically**. The ICML 2025 poster “MetaAgent” proposes constructing multi-agent systems using finite state machines, where the FSM controls actions and state transitions, and reports improved performance versus other automated design methods. citeturn2search12

On the systems side, new work is targeting **agent serving runtimes** that separate workflow specification from execution while offering managed state layers. For example, the 2026 “Nalar” paper describes a serving framework with a managed state layer that decouples logical state from physical placement and supports safe reuse/migration and consistent retry behavior—essentially formalizing “state as a runtime service.” citeturn3academia37

Another emerging theme is **reproducibility constraints**: in workflow-heavy domains, researchers are explicitly pushing for structured action schemas, deterministic execution policies, and provenance tracking to make actions auditable and replayable (e.g., R-LAM). citeturn4academia40

Finally, durable workflows introduce a persistent engineering tension that is directly relevant to your “agent remembers work3” requirement: replay-based durability can create immutability/determinism constraints and requires careful handling of non-deterministic operations (LLM calls, HTTP, randomness). Durable execution platforms document these constraints and promote splitting workflow logic from side-effectful activities/steps to keep the system replayable. citeturn4search4turn3search15turn3search23