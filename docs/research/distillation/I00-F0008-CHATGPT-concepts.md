# I00-F0008-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0008-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md)

## Source

- chat_id: `I00-F0008-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил исследование актуальных open-source решений для сервиса парсинга в формате data pipelines с адаптерами под разные источники (`raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:4`, `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:8`, `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:10`, `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:12`).
2. Пользователь уточнил предпочтения: open-source, желательно свежие решения, желательно Python (`raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:28`).
3. Пользователь запросил отдельный поиск архитектурных материалов (Medium/dev.to и др.) про Python-системы сбора информации с Temporal и парсерами (`raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:120`).
4. Пользователь попросил структурированные компонентные описания найденных сервисов, затем запросил гайды по применению Temporal в агентских сценариях у OpenAI и других успешных компаний (`raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:280`, `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:387`).

## AI Response Summary

1. Агент собрал широкий обзор OSS-экосистемы (scraping frameworks, ingestion/connectors, orchestrators) и вывел композиционный подход вместо “единого продукта” (`C01`-`C05`).
2. Затем подготовил структурные разборы reference-архитектур из статей с выделением компонентов и ответственности (`C06`, `C07`, `C08`).
3. В финале дан curated набор ресурсов по Temporal для agentic workflows (OpenAI docs, Temporal cookbook, community demos, case studies, observability), с акцентом на long-running/HITL use cases (`C10`).

## Extracted Concepts

### C01. Target system is an adapter-based multi-source parsing pipeline

- Concept: Базовая архитектурная идея - единый pipeline, куда добавляются новые источники как адаптеры.
- Why it matters: Определяет extensibility model и декомпозицию компонентов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:4`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:41`

### C02. Scrapy is treated as the primary Python extraction engine for web-heavy workloads

- Concept: Scrapy выделяется как зрелое ядро для crawling/parsing с spider + pipeline архитектурой и высокой кастомизируемостью.
- Why it matters: Даёт production-grade web ingestion foundation для MVP.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:43`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:45`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:47`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:49`

### C03. Orchestration and extraction are separate concerns with different trade-offs

- Concept: Инструменты orchestration (Airflow/Temporal/Prefect и т.д.) не заменяют extraction layer; extraction frameworks не закрывают надежную orchestration out-of-box.
- Why it matters: Предотвращает выбор “одного серебряного молотка” и задаёт layered architecture.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:56`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:61`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:75`

### C04. Temporal is positioned for durable long-running workflows with retry/state guarantees

- Concept: Temporal используется как слой надежной оркестрации для сложных многосервисных и долгоживущих процессов.
- Why it matters: Закрывает failures/retries/state persistence, критичные для регулярного data collection.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:77`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:79`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:81`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:95`

### C05. Practical recommendation is hybrid composition, not monolithic platform selection

- Concept: Для реальной системы предлагается Temporal backbone + source-specific Python adapters/tooling.
- Why it matters: Максимизирует гибкость при контролируемом инфраструктурном оверхеде.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:95`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:99`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:103`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:107`

### C06. Component-level architecture descriptions require explicit responsibility boundaries

- Concept: Архитектурные описания сервисов структурируются по уровням: orchestration core, workers/queues, workflows, activities, storage, observability.
- Why it matters: Делает сравнительный анализ систем практичным для проектных решений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:280`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:284`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:292`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:307`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:322`

### C07. High-volume data processing pattern uses hierarchical workflows plus bounded concurrency

- Concept: Для масштабных batch-сценариев применяются Main->Partition->Batch workflows и sliding-window control.
- Why it matters: Позволяет эффективно управлять throughput и внешними лимитами.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:338`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:349`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:355`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:358`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:379`

### C08. Agentic Temporal architecture maps role-agents to activities and orchestration patterns

- Concept: Агентские системы выражаются через workflow orchestration (sequential/parallel/multi-agent), где activities реализуют tools/role steps, а queries/signals дают контроль.
- Why it matters: Даёт operational template для long-running AI workflows.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:390`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:405`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:408`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:463`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:467`

### C09. Key architectural risks: idempotency of side effects, external API constraints, and operational complexity

- Concept: Надежность оркестрации не устраняет риски дублирования внешних действий, некачественных данных и роста эксплуатационной сложности.
- Why it matters: Эти риски определяют обязательные design guardrails (idempotency, rate limits, monitoring).
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:271`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:273`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:274`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:275`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:482`

### C10. Strong Temporal learning path for agent scenarios centers on OpenAI+Temporal resources

- Concept: Качественный старт для agentic workflows требует связки официальных OpenAI guides (HITL/long-running) с Temporal cookbook/tutorials, demos, case studies и observability stack.
- Why it matters: Ускоряет adoption и снижает риск архитектурных ошибок на ранней стадии.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:391`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:396`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:404`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:413`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:523`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0008-CHATGPT.md:531`

## Unresolved Ambiguities

1. Не определено, какой “reference stack” утверждается как baseline (минимальный набор компонентов для MVP).
2. Не зафиксирован policy выбора между платформами коннекторов и кастомными адаптерами по типам источников.
3. Не выбрана единая observability стратегия (Temporal-only vs Temporal + external tracing/analytics stack).
