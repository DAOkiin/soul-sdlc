# I01-F0019-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0019-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь запросил исследование проверенных и готовых решений для управления состоянием SDLC-процесса в agentic-разработке перед фиксацией процесса и полной имплементацией.
2. [request] [U02] Позже пользователь задал архитектурный вопрос о появляющемся DSL (Policy Evaluator, Trigger/Runners, states/transitions).
3. [request] [U03] В конце пользователь отдельно спросил, существуют ли уже готовые открытые решения для агентной SDLC-разработки или верифицированные человеческие SDLC-процессы.

## AI Response Summary

1. [proposal] [A01] Ответ собрал карту проверенных подходов и инструментов: hooks, CI enforcement, policy-as-code, FSM/workflow стандарты, durable execution паттерны и их маппинг на `DDL/state/guards` (-).
2. [proposal] [A02] Агент предложил конкретный интеграционный каркас: v1-basis + `pre-commit`/`lefthook` + CI required checks + Conftest policy backend + Mermaid/state artifacts.
3. [proposal] [A03] Отдельно развернут DSL-дизайн как IR с компиляторами/адаптерами, разделением на Process/Checks/Bindings/Toolchain, декларативной моделью и extension points для будущих инструментов.
4. [proposal] [A04] Финальный пользовательский вопрос о готовых open solutions в этом файле без ответа агента.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4899`
- U03: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:5191`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:33`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:35`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:37`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4748`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4755`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4765`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:235`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:243`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:254`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4553`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4561`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4608`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4727`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4733`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4739`
- A03: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4952`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4958`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4965`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4968`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4974`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4979`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4920`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:5127`, `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:5135`
- A04: `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:1`

## Extracted Concepts

### C01. Layered architecture is the core invariant

- Concept: Архитектура должна разделять graph/process spec, policy checks и runtime state/history.
- Why it matters: Это повышает управляемость изменений и переносимость процесса между раннерами.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:33`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:35`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:37`

### C02. Local hooks are feedback, CI is enforcement

- Concept: Pre-push полезен как ранний UX feedback, но must-контроль должен жить в CI/protected branches.
- Why it matters: Устраняет ложное ощущение гарантии от локально отключаемых хуков.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:71`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:80`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:210`

### C03. Policy-as-code backend for structured SDLC artifacts

- Concept: `DDL/state/guards` как structured data хорошо компонуются с OPA/Conftest.
- Why it matters: Позволяет вынести инварианты в декларативные policy rules и сократить custom evaluator.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:94`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:101`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:205`

### C04. Verify what is pushed, not incidental workspace state

- Concept: Guard checks должны опираться на refs/SHA диапазон пуша, а не случайное текущее состояние рабочей директории.
- Why it matters: Снижает расхождения локальных и CI результатов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:209`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:215`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:221`

### C05. Reuse proven runtimes selectively, avoid full replacement too early

- Concept: Стандарты/движки (ASL/SCXML/FSM libs/durable execution) полезны как доноры механизмов, но не обязательно как immediate full-stack migration.
- Why it matters: Сохраняет скорость внедрения и снижает архитектурный overkill на раннем этапе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:148`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:153`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:225`

### C06. Event history is a first-class SDLC state primitive

- Concept: Помимо текущего state необходимо вести событийную историю для audit/replay/analytics.
- Why it matters: Делает процесс объяснимым и пригодным для долгоживущих агентных сценариев.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4748`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4755`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4765`

### C07. Practical integration baseline: v1 + proven adapters

- Concept: Рекомендована связка: оставить свой DDL/state core, добавить hook manager, CI gates и data-driven guards.
- Why it matters: Дает баланс между скоростью разработки и эксплуатационной надежностью.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:235`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:243`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:254`

### C08. Conftest integration requires explicit snapshot contract

- Concept: Между runner и policy evaluator нужен стабильный snapshot contract (`state`, `guards`, `context`, `repo`, `exec`).
- Why it matters: Упрощает тестирование и заменяемость policy backend.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4553`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4561`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4608`

### C09. Versioned schemas + migration path are mandatory

- Concept: DSL artifacts (`ddl/state/checks`) должны иметь schema version и миграционный механизм.
- Why it matters: Позволяет безопасно эволюционировать процесс и воспроизводить historical behavior.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4727`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4733`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4739`

### C10. DSL should be treated as IR with exporters

- Concept: Доменный DSL должен описывать намерение, а конкретные toolchains (pre-commit, CI, policy backend) — быть компиляторами/экспортерами из IR.
- Why it matters: Делает систему переносимой на новые инструменты без переписывания доменной модели.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4952`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4958`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4965`

### C11. Keep DSL declarative and bounded

- Concept: DSL должен оставаться декларативным (данные + простые `when` условия) без procedural logic.
- Why it matters: Предотвращает превращение DSL во "второй язык программирования" с высоким maintenance cost.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4968`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4974`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4979`

### C12. Domain DSL and toolchain config must be separate artifacts

- Concept: Process/Checks/Bindings — доменная часть; Toolchain — адаптерная часть (policy backend, task runner, trigger runner).
- Why it matters: Позволяет менять инфраструктуру выполнения, не ломая процессную спецификацию.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:4920`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:5127`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md:5135`

## Unresolved Ambiguities

1. Финальный вопрос пользователя о готовых открытых комплексных решениях в этом источнике остался без ответа агента.
2. Источник агрегирует несколько вложенных спецификаций и черновых патчей; нужна отдельная дедупликация canonical требований vs исследовательских заготовок.
