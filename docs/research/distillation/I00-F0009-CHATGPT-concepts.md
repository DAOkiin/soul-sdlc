# I00-F0009-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0009-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md)

## Source

- chat_id: `I00-F0009-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил разобраться в системных требованиях Temporal Server (self-hosted) (`raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:4`).
2. Пользователь запросил точные цифры скорости на сложном pipeline-кейсе (сбор твитов, NER, тренды, аналитика) (`raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:85`, `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:87`).
3. Пользователь попросил сравнить скоростные метрики Temporal и Dagster (`raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:212`).

## AI Response Summary

1. Агент описал системные зависимости и эксплуатационные требования Temporal: persistence/visibility, сетевую изоляцию и масштабируемые серверные сервисы (`C01`-`C06`).
2. Агент дал практическую модель latency/throughput и пример расчёта для сложного workflow с акцентом на вклад оркестрации и activity-runtime (`C07`, `C08`).
3. Агент предложил benchmarking-подход для точных цифр и выполнил сравнительное позиционирование Temporal vs Dagster по классу задержек и единице оркестрации (`C09`, `C10`).

## Extracted Concepts

### C01. Temporal Server requires a persistence database as a hard dependency

- Concept: Self-hosted Temporal не работает без persistence DB; поддержка включает Postgres, MySQL, Cassandra, SQLite (dev-focused).
- Why it matters: Определяет минимальную инфраструктуру и технологические ограничения deployment.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:12`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:14`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:16`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:19`

### C02. Visibility architecture is a separate design axis with Elasticsearch preference at scale

- Concept: Для расширенного поиска и роста нагрузки visibility-store нужно проектировать отдельно; Advanced Visibility с Cassandra ограничен, а Elasticsearch рекомендуется для нагрузочных сценариев.
- Why it matters: Влияет на query capabilities, масштабируемость и ресурсный профиль кластера.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:21`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:25`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:26`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:28`

### C03. Temporal hosts should be treated as protected infrastructure, not public endpoints

- Concept: Temporal infrastructure должна быть сетево изолирована как критичный сервис уровня БД.
- Why it matters: Это security baseline для production и требования к network perimeter.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:32`

### C04. Temporal server sizing is service-topology dependent, not a single machine spec

- Concept: Сервер Temporal состоит из 4 independently scalable сервисов (frontend/history/matching/worker), поэтому “системные требования” считаются по компонентам плюс DB/visibility.
- Why it matters: Направляет capacity planning от монолитного хоста к сервисной модели.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:41`

### C05. Bottlenecks usually come from persistence latency and history-intensive load profile

- Concept: Ключевые ограничения производительности чаще всего в DB IO/latency, history-service нагрузке, visibility-store и shard configuration; для small production указан ориентир 512 shards вместо dev-default.
- Why it matters: Помогает фокусировать performance tuning и risk mitigation в правильных узлах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:52`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:55`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:56`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:57`

### C06. Public resource numbers are baseline examples, not production guarantees

- Concept: Упомянутые CPU/RAM значения в гайдах и туториалах являются стартовыми ориентирами для dev/PoC, а не фиксированными production minimums.
- Why it matters: Снижает риск ошибочного capacity planning на основе несопоставимых reference-values.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:43`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:45`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:48`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:50`

### C07. Workflow latency must be decomposed into orchestration overhead plus activity runtime

- Concept: Скорость workflow определяется суммой orchestration latency Temporal, latency внешних activity-сервисов и задержек DB/сети; нижняя граница orchestration-latency описана порядком около 100ms.
- Why it matters: Формирует корректную модель SLA и диагностики задержек.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:91`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:97`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:101`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:116`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:170`

### C08. Throughput is highly infrastructure-dependent and can reach thousands of flows per second

- Concept: Публичные кейсы указывают на диапазоны порядка 1500-4000 flows/sec при масштабировании Cassandra-кластера, что демонстрирует высокую ceiling throughput.
- Why it matters: Даёт ориентир класса производительности при корректной архитектуре и capacity.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:121`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:123`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:127`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:206`

### C09. Exact performance numbers require benchmark-driven calibration in target environment

- Concept: Для “точных цифр” нужен workload-specific benchmark на целевой инфраструктуре с maru (throughput/устойчивость) и benchmark-latency (чистая orchestration latency).
- Why it matters: Отделяет переносимые принципы от неподтверждённых оценок и делает прогнозы операционными.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:129`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:131`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:181`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:185`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:188`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:189`

### C10. Temporal and Dagster represent different latency classes and orchestration units

- Concept: Temporal ориентирован на low-latency event/task orchestration (десятки-сотни ms), тогда как Dagster в типовом режиме run-centric и чаще работает в секундно-минутной гранулярности из-за tick/run-launch overhead.
- Why it matters: Влияет на выбор платформы под near-real-time vs batch/asset-oriented use cases.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:216`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:218`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:241`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:245`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:253`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:285`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md:286`

## Unresolved Ambiguities

1. Не зафиксированы целевые workload параметры (объём событий/мин, latency NER/activity), без которых невозможно финализировать sizing и SLA.
2. Не выбран окончательный persistence stack (Postgres/MySQL/Cassandra + visibility backend), что влияет на производительность и эксплуатационную сложность.
3. Не определён требуемый latency-класс продукта (near-real-time vs batch windows), от которого зависит выбор Temporal vs Dagster для оркестрационного ядра.
