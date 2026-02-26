# I01-F0020-CHATGPT-DR Concepts (Draft)

## Source

- chat_id: `I01-F0020-CHATGPT-DR`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] В этом DR-файле нет отдельного диалога; он представляет итоговый исследовательский отчет по OSS-экосистеме для SDLC-оркестрации, agent workflow и plan/run/apply архитектуры.

## AI Response Summary

1. [proposal] [A01] Отчет фиксирует, что единого OSS-инструмента, полностью закрывающего весь стек Process DSL + Policy + Triggers + Exec + State/History + Render, практически нет; нужен composable stack и адаптерная архитектура.
2. [proposal] [A02] Даны два приоритетных стека: durable workflow-first (Temporal) и k8s CI-first (Tekton + Triggers + Results), плюс pragmatic CI-first вариант (Jenkins + OPA/Conftest + pre-commit).
3. [proposal] [A03] Исследование предлагает стабильный IR-контракт (`ProcessSpec`, `CheckSpec`, `CheckResult`, `Event`, `StateSnapshot`) и migration path через plan/run/apply с adapter backends.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:1`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:5`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:12`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:18`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:25`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:7`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:8`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:100`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:9`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:77`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:101`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:11`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:12`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:91`
- A03: `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:68`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:158`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:165`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:108`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:109`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:112`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:181`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:156`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:173`, `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:183`

## Extracted Concepts

### C01. No single OSS tool covers the full target architecture end-to-end

- Concept: Целевой стек SDLC-оркестрации (DSL+Policy+Triggers+Executors+State/History+Render) обычно собирается из нескольких систем.
- Why it matters: Сразу задает правильную стратегию composability вместо поиска "единственного идеального продукта".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:5`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:12`

### C02. Target architecture should be explicitly layered

- Concept: Архитектура должна явно выделять 6 слоев: Process DSL, Policy checks, Triggers, Executors, State/history, Renderers.
- Why it matters: Это облегчает разделение ответственности и независимую эволюцию компонентов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:18`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:25`

### C03. Temporal-first stack for durable plan/run/apply

- Concept: Для воспроизводимого event-driven исполнения с богатой историей один из лучших фундаментов — Temporal.
- Why it matters: Снижает стоимость построения долговременного orchestration/state runtime с нуля.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:7`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:8`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:100`

### C04. Tekton stack as k8s-native orchestration alternative

- Concept: Tekton Pipelines + Triggers + Results закрывают execution/triggers/history для k8s-центричных организаций.
- Why it matters: Дает enterprise-ready CI/workflow основу с нативной интеграцией в Kubernetes.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:9`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:77`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:101`

### C05. Pragmatic low-friction baseline: Jenkins + OPA/Conftest + pre-commit

- Concept: Для быстрого боевого старта с минимумом кастомного кода pragmatic путь — CI pipeline backend + policy-as-code + local hooks.
- Why it matters: Позволяет начать с малого и постепенно мигрировать к более сложному orchestration ядру.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:11`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:12`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:91`

### C06. Stable IR contract is the future-proof boundary

- Concept: Нужно закрепить стабильный промежуточный контракт (`ProcessSpec`, `CheckSpec`, `CheckResult`, `Event`, `StateSnapshot`) и строить backends как адаптеры.
- Why it matters: Новый инструмент добавляется как adapter, не ломая доменную модель процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:68`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:158`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:165`

### C07. Core mismatch: FSM domain model vs DAG pipeline engines

- Concept: Большинство CI/workflow движков нативно DAG/steps-oriented; доменную FSM приходится компилировать/надстраивать.
- Why it matters: Это главная причина, почему отдельный Process DSL слой должен оставаться canonical.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:108`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:109`

### C08. Decision history must be captured as domain events

- Concept: Логи джобов недостаточны; отдельно нужна история решений о переходах и срабатывании guards.
- Why it matters: Обеспечивает explainability и реплей причинно-следственных цепочек.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:112`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:181`

### C09. Migration path: keep adapters swappable

- Concept: Рекомендуется начинать с conftest/pre-commit adapters и затем подложить stronger backend (Temporal/Tekton), сохранив неизменным DSL/IR.
- Why it matters: Позволяет эволюцию без архитектурных "переписать все".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:156`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:173`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:183`

### C10. Agent runtimes should stay plugin executors, not core governance

- Concept: Agent platforms (OpenHands/Continue/Codex-like executors) логично включать как executor plugins поверх governance DSL.
- Why it matters: Сохраняет deterministic guardrails и предотвращает перенос критической логики в недетерминированный агентный слой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:14`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:192`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0020-CHATGPT-DR.md:195`

## Unresolved Ambiguities

1. Для целевого контекста не выбран единый primary backend (Temporal-first vs Tekton-first vs Jenkins-first).
2. Не зафиксирован canonical формат доменного event log (schema, retention, correlation IDs).
