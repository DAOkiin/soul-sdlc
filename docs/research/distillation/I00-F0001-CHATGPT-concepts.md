# I00-F0001-CHATGPT Concepts (Draft)

## Source

- chat_id: `I00-F0001-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил собрать из чатов рабочий контекст для одного документа и подготовить план дня: use cases, стек, архитектура, настройка агентской разработки.
2. [request] [U02] Пользователь запросил фреймворк на один лист A4 для системного планирования сложного проекта.
3. [request] [U03] Пользователь попросил валидировать формулировку идеи системы ingestion+rules pipeline.
4. [request] [U04] Пользователь попросил переписать идею в точном техническом стиле для документа.
5. [request] [U05] Пользователь попросил найти идентичные open-source решения с готовыми правилами и инструментами.

## AI Response Summary

1. [goal] [A01] Агент собрал структурированный рабочий документ: цель, MVP-границы, use cases, DDL-first data model, event-driven architecture, стек и план на день.
2. [proposal] [A02] Для planning предложен A4-canvas (6 блоков + оборот с декомпозицией), адаптированный под pipeline-проект.
3. [risk] [A03] Валидация идеи подтвердила жизнеспособность, но выделила риски по режимам управления пайплайном и отсутствию минимального контракта правил.
4. [proposal] [A04] Сформирована техдок-версия концепции и сравнительный список OSS-референсов по модели adapters + pipelines + tools.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:227`
- U03: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:524`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:526`
- U04: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:715`
- U05: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:748`
- A01: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:36`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:37`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:44`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:553`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:559`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:97`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:99`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:115`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:120`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:124`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:126`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:131`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:135`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:147`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:54`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:60`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:66`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:78`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:90`
- A02: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:235`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:265`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:269`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:280`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:288`
- A03: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:624`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:630`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:631`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:638`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:642`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:646`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:650`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:657`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:659`
- A04: `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:606`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:607`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:733`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:734`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:752`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:756`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:782`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:792`, `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:806`

## Extracted Concepts

### C01. MVP should start with adapter-bounded web ingestion and staged source expansion

- Concept: Входной контур ограничивается источниками, для которых есть адаптеры; в MVP приоритет web/RSS, а YouTube/другие коннекторы выносятся после.
- Why it matters: Даёт управляемые границы релиза и расширяемость через plugin-модель.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:44`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:553`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:559`

### C02. Processing is defined as configurable rule pipelines selected by human or agent users

- Concept: Пайплайн строится из переиспользуемых правил (extraction, categorization, NER, signals) и выбирается пользователем-человеком или агентом.
- Why it matters: Формирует платформенную модель вместо одноразовых скриптов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:38`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:80`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:568`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:572`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:727`

### C03. Data layer is intentionally DDL-first and validated with executable insert/select scenarios

- Concept: До кода фиксируется схема БД и тестовые сценарии запросов/вставок, с автопроверкой миграций на временной БД.
- Why it matters: Снижает архитектурные ошибки в foundation-слое и ускоряет последующую разработку.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:97`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:99`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:115`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:120`

### C04. Target architecture is event-driven pipeline orchestration with explicit component boundaries

- Concept: Верхний слой включает source registry, orchestrator (Temporal), ingestion workers, extraction, enrichment, analytics, storage, API/query, syndication, observability.
- Why it matters: Делает систему композиционной и масштабируемой по сервисам/нагрузке.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:124`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:126`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:131`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:135`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:147`

### C05. Use-case map spans full value chain from source management to content syndication

- Concept: UC-декомпозиция покрывает источники, ingestion, versioning/diff, extraction, NLP/signal, analytics, and generated artifacts.
- Why it matters: Обеспечивает end-to-end coverage, а не локальный парсер.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:60`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:66`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:78`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:90`

### C06. One-page A4 canvas is used as operational planning artifact for project control

- Concept: Для сложной задачи применяется компактный канвас (цель, scope, use cases, architecture, stack, plan/risks) + обратная сторона под декомпозию.
- Why it matters: Снижает когнитивную нагрузку и удерживает системность при ежедневной работе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:235`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:265`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:269`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:280`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:288`

### C07. Human-controlled and autonomous pipeline modes must be separated in governance

- Concept: Режимы “человек собирает пайплайн” и “агент выбирает правила” требуют раздельной модели ответственности/логов/объяснимости.
- Why it matters: Без этого быстро ломаются безопасность и auditability системы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:624`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:630`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:631`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:638`

### C08. Rules can evolve during development, but require a minimal execution contract

- Concept: Даже при R&D-подходе правила должны иметь минимально формализованный интерфейс (input/output/side-effects/idempotency).
- Why it matters: Иначе оркестратор не сможет безопасно комбинировать и ретраить шаги.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:642`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:646`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:650`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:657`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:659`

### C09. System objective is structured knowledge availability for both humans and AI agents

- Concept: Конечный целевой артефакт — централизованное структурированное хранилище результатов мониторинга, пригодное для human+agent consumption.
- Why it matters: Выравнивает архитектуру вокруг полезности данных, а не вокруг конкретного инструмента.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:606`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:607`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:733`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:734`

### C10. OSS landscape suggests compositional reference architecture rather than identical out-of-box product

- Concept: Близкие open-source решения покрывают части модели (connectors/transforms/processors/scraping), но полноценный 1:1 стек требует композиции.
- Why it matters: Помогает строить pragmatic build-vs-adopt strategy.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:752`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:756`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:782`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:792`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:806`

## Unresolved Ambiguities

1. Не зафиксирован приоритет №1 для MVP-outcome: поиск/дашборд или автогенерация дайджестов (`raw-exports/sdlc-discovery-iteration-00/I00-F0001-CHATGPT.md:222`).
2. Нет формального стандарта интерфейса правил (contract schema/versioning/testing policy).
3. Не выбрана окончательная базовая OSS-стратегия (platform-first vs custom-core + selected components).
