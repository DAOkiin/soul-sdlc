# I01-F0013-CHATGPT-DR Concepts (Draft)

[Analyzed source: I01-F0013-CHATGPT-DR.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md)

## Source

- chat_id: `I01-F0013-CHATGPT-DR`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. В этом экспорте нет явных пользовательских сообщений; файл содержит готовый русскоязычный deep research отчет (`raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:1`).

## AI Response Summary

1. Ответ фиксирует многослойную модель state (process, history, memory, artifact) и связывает ее с lifecycle `work3` (`C01`, `C02`).
2. Для надежных переходов предложены графовые/типизированные workflow-подходы с checkpointing, pause/resume и queryable history (`C03`, `C04`, `C05`).
3. Durable execution (Temporal и аналоги) описан как инфраструктурный источник истины для replay, retries и recovery (`C06`, `C07`).
4. Во фреймворках отдельно подчеркнуто различие process-state и memory; message-centric схемы без durable state обозначены как ограниченные (`C08`, `C09`).
5. Для coding agents рекомендован Git/PR lifecycle с явными guard conditions и security controls поверх персистентного состояния (`C10`, `C11`, `C12`).

## Extracted Concepts

### C01. Отчет как перевод с сохранением технической структуры

- Concept: Русскоязычный документ позиционируется как полный перевод англоязычного отчета с сохранением структуры, ссылок и терминов.
- Why it matters: Позволяет использовать те же SDLC-концепты и архитектурные решения без потери контекста между языками.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:5`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:9`

### C02. State в agentic SDLC должен быть многослойным

- Concept: Для проектирования агента state нужно разделять на workflow state, execution history, working memory и artifact state.
- Why it matters: Это позволяет отдельно управлять переходами, наблюдаемостью, памятью и инженерными артефактами.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:15`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:20`

### C03. Graph/state-machine orchestration как базовый механизм переходов

- Concept: Явные переходы и персистентное состояние реализуются через графы/машины состояний с переносом state-объекта между шагами.
- Why it matters: Делает процесс контролируемым и machine-checkable для сложных agent workflows.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:38`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:42`

### C04. Checkpointing + pause/resume обеспечивают stage lifecycle

- Concept: Checkpointers, interrupt/pause semantics и thread history создают устойчивую модель длительных стадий.
- Why it matters: Обеспечивает корректное возобновление и контроль ворот стадий без ручной реконструкции контекста.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:46`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:47`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:49`

### C05. Typed sessions/workflows и визуальные state machines

- Concept: Session-based typed workflows (Microsoft Agent Framework) и облачные state machines (Step Functions) повышают явность маршрутизации и аудируемость переходов.
- Why it matters: Упрощает операционное понимание текущей стадии и снижает неоднозначность поведения агента.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:53`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:55`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:61`

### C06. Durable execution как источник истины состояния

- Concept: Event History + replay в durable engines (Temporal) дают детерминированное восстановление и непрерывность выполнения.
- Why it matters: Состояние и прогресс не зависят от повторной генерации LLM и сохраняют воспроизводимость.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:79`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:81`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:86`

### C07. Экосистема durable runtimes расширяется

- Concept: Restate, DBOS, Resonate и Inngest формируют общий класс платформ с journaled state, retries и step-level recovery.
- Why it matters: Это снижает vendor lock-in и подтверждает зрелость подхода "state as infrastructure".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:92`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:97`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:99`

### C08. Framework-local persisted context ускоряет внедрение

- Concept: LlamaIndex `Context` и CrewAI `@persist` дают встроенные механизмы сохранения workflow-state между шагами и запусками.
- Why it matters: Позволяет начать со stateful-процессов даже без отдельного внешнего workflow runtime.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:109`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:117`

### C09. Memory не заменяет process-state

- Concept: Message-centric orchestration (AutoGen/Swarm) без durable state ведет к "растеканию" контекста и ограниченной резюмируемости.
- Why it matters: Подчеркивает необходимость структурированного state-объекта и явных переходов для надежных SDLC-пайплайнов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:123`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:130`

### C10. Git/PR как artifact state machine для coding agents

- Concept: Branch/PR lifecycle моделирует состояния "в работе", "готово к merge" и "завершено".
- Why it matters: Делает работу агента наблюдаемой и совместимой с существующим инженерным процессом ревью/интеграции.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:134`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:139`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:150`

### C11. Transition contract: init -> query -> guard -> cleanup

- Concept: Рекомендуемый контракт переходов включает явную инициализацию `work3` state, query-доступ к статусу, guard checks перед merge и зафиксированный cleanup.
- Why it matters: Обеспечивает повторяемый и проверяемый lifecycle агентной задачи.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:163`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:175`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:182`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:184`

### C12. Security and reproducibility as first-class constraints

- Concept: Persisted agent state несет security risks, а исследовательский фокус смещается к FSM generation, managed state layers и replay-auditable execution.
- Why it matters: Архитектура state-layer должна одновременно покрывать надежность, безопасность и доказуемость действий.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:190`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:197`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:199`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md:203`

## Unresolved Ambiguities

1. Источник содержит только переводной deep research текст, без явного сырого диалога user/assistant для верификации исходной формулировки запроса.
2. Утверждения опираются на внешние URL-цитаты внутри документа; содержимое первичных источников в этот файл не встроено.
