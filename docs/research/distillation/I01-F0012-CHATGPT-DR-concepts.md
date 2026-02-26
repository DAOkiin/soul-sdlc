# I01-F0012-CHATGPT-DR Concepts (Draft)

[Analyzed source: I01-F0012-CHATGPT-DR.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md)

## Source

- chat_id: `I01-F0012-CHATGPT-DR`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. В данном экспорте пользовательские сообщения отсутствуют; файл содержит только текст готового deep research отчета (`raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:1`).

## AI Response Summary

1. Отчет задает многослойную модель состояния агента: workflow/process state, execution history, working memory и artifact state, привязывая это к lifecycle рабочего контекста (`C01`, `C02`).
2. Для программируемых переходов рекомендованы graph/state-machine orchestration подходы с checkpointing, pause/resume и history query (`C03`, `C04`, `C05`).
3. Отдельно выделен durable execution слой (Temporal и аналоги), где event history и replay становятся источником истины для resumability (`C06`, `C07`).
4. В сравнении framework-подходов отмечено разделение process-state и memory, а также ограничения message-centric оркестрации без durable state (`C08`, `C09`).
5. Для coding agents предложено трактовать branch/PR как artifact state machine и управлять merge/cleanup через guard conditions, observability и security controls (`C10`, `C11`, `C12`).

## Extracted Concepts

### C01. Multi-layer state model for agentic SDLC

- Concept: Состояние агентной системы нужно декомпозировать на process state, execution history, working memory и artifact state.
- Why it matters: Это устраняет смешение "памяти чата" и реального управления жизненным циклом задач.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:7`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:12`

### C02. Explicit transitions over inferred behavior

- Concept: Критичные переходы должны быть кодо-определенными и machine-checkable, а не выведенными из свободного контекста.
- Why it matters: Это делает процесс предсказуемым и проверяемым при ошибках и handoff-сценариях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:9`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:128`

### C03. Checkpointed state graphs for long-running agents

- Concept: Graph orchestration с checkpointer обеспечивает persisted state на каждом супер-шаге.
- Why it matters: Даёт fault tolerance, human-in-the-loop и восстановление после пауз/сбоев.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:20`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:22`

### C04. Stage gates via pause/resume semantics

- Concept: Interrupt/pause точки превращают этапные переходы в first-class workflow primitives.
- Why it matters: Позволяет формально управлять lifecycle этапа вместо ad hoc условий.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:26`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:156`

### C05. Queryable state history for situational awareness

- Concept: Статус должен получаться через запросы к checkpoint/event history, а не через повторную интерпретацию логов LLM.
- Why it matters: Обеспечивает быстрый и воспроизводимый "что происходит сейчас" интерфейс.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:27`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:149`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:152`

### C06. Durable execution as authoritative state layer

- Concept: В durable engines (например, Temporal) event history + replay формируют authoritative record прогресса.
- Why it matters: Резюме после крашей не зависит от "повторного мышления" модели и сохраняет детерминизм исполнения.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:53`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:55`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:73`

### C07. Workflow runtimes are converging on durable primitives

- Concept: Restate/DBOS/Resonate/Inngest предлагают сходные примитивы журналирования, checkpoint/replay, step retries и long waits.
- Why it matters: Это подтверждает рыночный сдвиг к "state as infrastructure" для агентных систем.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:66`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:71`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:75`

### C08. Framework-level persisted context patterns

- Concept: LlamaIndex и CrewAI реализуют workflow-context/state внутри фреймворка, включая сохранение между запусками.
- Why it matters: Это упрощает внедрение stateful-процессов без внешнего workflow runtime на старте.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:83`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:91`

### C09. Memory is not process-state

- Concept: Фактовая память агента и контроль переходов workflow являются разными слоями и не взаимозаменяемы.
- Why it matters: Разделение снижает риск "state spill" в сообщения и хрупкую оркестрацию.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:93`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:97`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:104`

### C10. Git artifacts as state machine boundaries for coding agents

- Concept: Для coding agents branch + PR выступают наблюдаемыми состояниями выполнения задачи.
- Why it matters: Это дает естественные границы "in progress / ready to merge / completed" и прозрачный аудит.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:108`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:113`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:124`

### C11. Recommended transition contract: init, guard, merge, cleanup

- Concept: Переходы должны включать явную инициализацию state, guard checks перед merge и зафиксированный cleanup как финальный шаг.
- Why it matters: Делает lifecycle задачи воспроизводимым, проверяемым и безопасно ретраябельным.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:137`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:156`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:158`

### C12. Security and research gaps in stateful agent execution

- Concept: Persisted agent state увеличивает security surface, а исследовательский фронт смещается к автоматической генерации FSM и managed state runtimes.
- Why it matters: Проектирование state layer должно учитывать не только функциональность, но и контроль рисков и воспроизводимость.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:162`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:169`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0012-CHATGPT-DR.md:171`

## Unresolved Ambiguities

1. В источнике нет явного пользовательского вопроса и критериев приоритизации, поэтому выделены концепты на уровне отчета, а не intent-to-answer mapping.
2. Цитаты в формате `turn*search*` указывают на внешние источники, но сами первоисточники в файле не включены, поэтому верификация опирается только на текст отчета.
