# I00-F0007-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0007-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md)

## Source

- chat_id: `I00-F0007-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил исследование open-source Python решений для multi-source parsing service в pipeline формате, с приоритетом Temporal (или легкой интеграции) и low overhead (`raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:4`, `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:14`, `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:31`, `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:39`).
2. Пользователь попросил отдельный поиск архитектурных статей (Medium/dev.to и аналоги) про Python-системы сбора информации с Temporal и парсерами (`raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:120`).
3. Пользователь попросил структурированно описать каждый найденный сервис по компонентам и зонам ответственности без лишней информации (`raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:280`).

## AI Response Summary

1. Агент собрал landscape OSS-компонентов (scraping engines, connector/ingestion frameworks, orchestrators) и дал интеграционный вывод через Temporal-centric composition (`C02`, `C03`, `C04`, `C05`).
2. Далее агент разобрал несколько reference-архитектур из статей и представил компонентные схемы и trade-offs по каждой (`C06`, `C07`, `C08`, `C09`, `C10`).
3. В ответах явно закреплена мысль: “готового 1-box стека под все источники + Temporal нет; проект требует осознанной сборки из модулей” (`C02`, `C05`).

## Extracted Concepts

### C01. Tool selection criteria are explicit: Python OSS, adapter extensibility, Temporal-fit, low startup overhead

- Concept: Технологии оцениваются по четким ограничениям (источники, язык, open-source, оркестрация, overhead), а не по популярности.
- Why it matters: Ускоряет архитектурные решения и снижает риск неподходящего stack lock-in.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:12`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:14`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:35`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:39`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:41`

### C02. No turnkey Python OSS stack covers all target sources with native Temporal out-of-box

- Concept: Практический вывод исследования - готового универсального решения “web+RSS+YouTube+Twitter+Temporal” не найдено.
- Why it matters: Требует архитектурной композиции и явного интеграционного слоя.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:99`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:105`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:107`

### C03. Temporal is positioned as durable orchestration backbone for parsing pipelines

- Concept: Workflows/activities в Python, retry/schedule/state tracking/fault tolerance — ключевая функция Temporal в архитектуре.
- Why it matters: Снимает необходимость ручной реализации reliability primitives.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:75`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:77`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:78`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:79`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:97`

### C04. Source layer should combine web crawlers and connector-based ingestion, chosen per source type

- Concept: Web-heavy part закрывается scraper frameworks, API-heavy sources — connector/ELT libraries; всё остаётся в Python.
- Why it matters: Позволяет оптимизировать implementation effort и избежать переизобретения адаптеров.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:59`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:67`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:69`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:71`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:73`

### C05. Recommended architecture is hybrid: Temporal orchestration + modular Python adapters

- Concept: Temporal координирует pipeline, а source-specific adapters (scraping/API/feed) реализуются как activities/plugins.
- Why it matters: Дает минимальный overhead при расширении числа источников.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:89`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:91`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:95`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:107`

### C06. Baseline scraping architecture pattern: Workflow orchestration over fetch/parse/save activities

- Concept: Простая референс-схема: Temporal server + worker + task queue + crawl workflow + fetch/parse/save activities + observable event history.
- Why it matters: Является стартовым шаблоном для первого production-like pipeline.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:149`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:151`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:288`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:307`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:312`

### C07. Large-batch ingestion pattern uses hierarchical workflows with constrained parallel windows

- Concept: Для миллионов записей используется Main->Partition->Batch hierarchy и sliding-window concurrency control.
- Why it matters: Позволяет масштабировать throughput без перегрузки внешних систем.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:155`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:157`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:338`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:355`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:358`

### C08. Agentic orchestration pattern maps agents to activities and supports sequential/parallel composition

- Concept: Агентные роли реализуются как activity steps, а workflow задаёт порядок/параллельность и exposes queries for runtime state.
- Why it matters: Даёт reusable pattern для сложных multi-step decision pipelines.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:162`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:166`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:390`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:405`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:417`

### C09. Comparative file pipeline shows Temporal’s reliability primitives over plain flow orchestration

- Concept: Один и тот же file-processing pipeline можно выразить разными оркестраторами, но Temporal явно добавляет durable retries/timeouts/heartbeats/task-queue isolation.
- Why it matters: Помогает обоснованно выбрать orchestration core под reliability requirements.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:169`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:172`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:432`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:446`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:478`

### C10. Main architectural risks are infrastructure complexity and side-effect idempotency

- Concept: При росте системы ключевые риски — operational overhead, дубли side effects при retries, зависимость от внешних API/качества данных.
- Why it matters: Эти риски должны быть закрыты design policies до масштабирования.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:271`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:273`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:274`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:385`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0007-CHATGPT.md:482`

## Unresolved Ambiguities

1. Не закреплён финальный набор “ядро + опциональные компоненты” для первого релиза (Scrapy/dlt/другое).
2. Не определены обязательные idempotency-правила для side-effect activities (DB writes, notifications, external actions).
3. Не задан целевой операционный профиль Temporal-инфраструктуры (self-hosted vs cloud, минимальная эксплуатационная модель).
