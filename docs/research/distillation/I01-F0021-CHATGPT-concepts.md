# I01-F0021-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0021-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md)

## Source

- chat_id: `I01-F0021-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь спросил про реальные альтернативы Microsoft Agent Framework и зафиксировал требование FSM+DSL для SDLC-автоматизации (`raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:4`).
2. Затем пользователь уточнил workflow-engine-centered подход и попросил разложить ответственности/порядок внедрения под мир "Nick + Codex agent", ограниченный human attention (`raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:190`).
3. Пользователь дал на анализ внешний проект и попросил определить прямую релевантность его целям (`raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1348`).
4. Финально пользователь запросил описать DSL для General Problem Solver (`raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1469`).

## AI Response Summary

1. Агент подтвердил силу MAF, но предложил оценивать по роли: agent SDK vs workflow engine; перечислил рабочие альтернативы по категориям (`C01`, `C02`, `C03`).
2. В workflow-first ответе агент описал слой ответственности: DSL/FSM, policy/autonomy, idempotent activities, Codex integration contract, state/event protocol и phased adoption (`C04`, `C05`, `C06`, `C07`).
3. По внешнему `paip-python` проекту дан вывод: прямого SDLC-фундамента нет, но `gps.py` и `emycin.py` полезны как референсы планирования и explainable policy (`C08`, `C09`).
4. Отдельно зафиксирован формальный GPS DSL (facts/state/goals/operators, transition semantics, invariants, STRIPS-like model) и возможные расширения для SDLC-case (`C10`, `C11`, `C12`).

## Extracted Concepts

### C01. MAF is strong, but architecture choice depends on control-plane needs

- Concept: Выбор не должен быть "framework-first"; нужно разделять задачу agent SDK и задачу workflow/FSM runtime.
- Why it matters: Предотвращает неправильную центровку архитектуры на LLM-слое вместо детерминированного процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:13`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:14`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:16`

### C02. Practical alternative map for agent frameworks

- Concept: Реальные альтернативы MAF включают LangGraph, OpenAI Agents SDK, PydanticAI, CrewAI, Google ADK и managed платформы (Bedrock/Vertex).
- Why it matters: Дает пространство выбора исполнителя агентного слоя без vendor lock-in на одном SDK.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:33`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:66`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:80`

### C03. For SDLC FSM+DSL, workflow engine should be primary layer

- Concept: При требовании детерминированного SDLC через FSM/DSL workflow engine (Temporal/Step Functions/Durable/Camunda) часто является более правильным центром, чем чисто агентный SDK.
- Why it matters: Обеспечивает audit/retries/approvals/timeouts независимо от качества LLM.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:107`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:111`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:179`

### C04. Codex should operate as step executor under deterministic workflow

- Concept: В workflow-centric дизайне Codex — worker/executor шага, а контур управления (переходы/лимиты/гейты) должен быть отделен и детерминирован.
- Why it matters: Позволяет автоматизировать SDLC, сохраняя управляемость при ошибках агента.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:217`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:233`

### C05. Codex integration can leverage existing non-interactive contracts

- Concept: Для orchestration пригодны `codex exec` + JSON/Schema outputs, AGENTS.md contracts и sandbox/approval controls.
- Why it matters: Ускоряет внедрение без построения собственного agent runtime с нуля.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:227`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:229`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:230`

### C06. Responsibility stack for workflow-centered SDLC

- Concept: Обязательные слои: process DSL, autonomy policy, idempotent activities, agent integration, state/history, human intervention protocol.
- Why it matters: Структурирует внедрение от MVP к production без пропуска критичных control функций.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:237`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:241`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:259`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:276`

### C07. Minimal local SDLC loop via state/event protocol

- Concept: Даже без полного workflow engine можно вести управляемый цикл через `.sdlc/state.yaml`, `events.jsonl`, `report`, `needs_human`, `run.next_actions`.
- Why it matters: Позволяет запустить контролируемую автоматизацию немедленно и эволюционировать позже.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1284`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1289`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1318`

### C08. External `paip-python` repo is not direct SDLC foundation

- Concept: Исследованный проект не содержит готового SDLC DSL/state/event architecture для задачи пользователя.
- Why it matters: Предотвращает неверный pivot на нерелевантный базовый код.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1352`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1357`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1361`

### C09. Reusable conceptual primitives from PAIP: planning + explainability

- Concept: `gps.py` релевантен как формальное планирование операторов, `emycin.py` — как explainable rule/policy reasoning.
- Why it matters: Эти примитивы можно использовать как теоретическую основу plan/policy подсистем, не перенимая весь проект.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1369`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1387`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1404`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1416`

### C10. GPS DSL formal core is STRIPS-like

- Concept: Базовый DSL GPS: facts, start/finish states, operators with `preconds/add/delete`, transition semantics `S' = (S-delete) ∪ add`.
- Why it matters: Обеспечивает детерминированное plan generation вместо ad hoc агентного планирования.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1475`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1507`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1522`

### C11. GPS DSL invariants are necessary for predictable planning

- Concept: Нужны инварианты корректности (`add/delete` disjoint, no duplicates, goal addability, normalized facts) для предотвращения циклов/нерешаемых доменов.
- Why it matters: Поддерживает стабильность планировщика в практическом использовании.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1548`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1555`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1558`

### C12. SDLC mapping: deterministic planner + Codex operator executor

- Concept: GPS DSL может служить форматом `plan.yaml`, где Codex исполняет операторы, а план вычисляется детерминированно.
- Why it matters: Соединяет формальное планирование с агентным исполнением без потери контроля.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1657`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md:1658`

## Unresolved Ambiguities

1. В этом файле не закреплен окончательный выбор workflow engine backend для целевой системы (Temporal vs cloud-native alternatives).
2. Не зафиксировано, будет ли GPS DSL использоваться напрямую в SDLC runtime, или только как conceptual layer для planner модуля.
