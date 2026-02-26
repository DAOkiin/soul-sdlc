# I00-F0006-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0006-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md)

## Source

- chat_id: `I00-F0006-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь описал видение сервиса: NL-запрос -> определение источников через ИИ -> задачи в БД -> обработка результатов -> правила -> уведомления, с примерами скидок и GitHub search (`raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:4`, `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:6`, `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:8`).
2. Пользователь добавил кейс агрегатора событий Бангкока/Таиланда с дедупликацией (`raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:73`).
3. Пользователь добавил кейс сбора корпуса эссе философов с темами и графом концептов (`raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:120`).
4. Пользователь попросил категоризировать типы кейсов, найти релевантные научные классификации, а затем сформировать структурированный список use-cases (`raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:174`, `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:189`, `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:233`).

## AI Response Summary

1. Агент сначала оформил базовую архитектуру мониторингового сервиса: сущности, пайплайн, болевые точки и MVP-чеклист (`C01`, `C02`, `C03`).
2. Затем расширил модель до index/search режима с canonical entities и entity resolution (`C04`, `C05`).
3. Для исследовательского кейса предложена этапная структура корпусного сбора и семантической разметки (`C06`).
4. По итогам “научного” слоя и финального запроса агент собрал иерархическую типологию use-cases полного цикла данных до синдикации (`C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. Core product is a monitoring service driven by NL intent and rule-triggered notifications

- Concept: Система превращает пользовательское NL-намерение в наблюдаемые источники и регулярные парсинг-циклы с downstream rules/events/notifications.
- Why it matters: Это базовый operating model, объединяющий ingestion, processing и user-facing реакцию.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:20`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:21`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:25`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:26`

### C02. Minimal data model includes intent-source-run-state-rule-event-notification chain

- Concept: Набор сущностей охватывает весь жизненный цикл: monitor intent, source/adapters, runs, raw artifacts, normalized entities, snapshots, rules, events, notifications.
- Why it matters: Даёт основу для DDL и трассировки причинно-следственной цепочки.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:28`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:39`

### C03. Parsing pipeline must explicitly include dedup/diff semantics before rule evaluation

- Concept: После ingestion и normalization требуется сравнение с snapshot (dedup + diff), иначе “новое/изменение” не определимо корректно.
- Why it matters: Это ключевой механизм для сигналов и уведомлений без шумовых дублей.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:41`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:48`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:49`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:54`

### C04. One platform should support two product modes: monitoring and index/search

- Concept: Monitoring mode (“следи и уведомляй”) и index/search mode (“собери, дедуплицируй, покажи”) используют общий ingestion core, но разные выходы.
- Why it matters: Позволяет масштабировать платформу в новые домены без дублирования ядра.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:81`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:83`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:84`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:86`

### C05. Canonical entity layer is required for multi-source event aggregation

- Concept: Для event search нужны `Canonical Event`, `Event Occurrence`, `Source Listing` и отдельный entity resolution компонент.
- Why it matters: Делает возможными dedup, update propagation и корректный пользовательский поиск.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:90`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:92`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:98`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:106`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:108`

### C06. Corpus-building case follows a four-stage pipeline: candidate curation, collection, labeling, concept graphing

- Concept: Кейсы “собрать эссе” требуют отдельной стадии отбора субъектов, затем сбора корпуса, тематической разметки и построения концептуального графа.
- Why it matters: Показывает, что платформа должна поддерживать research-oriented workflows, не только мониторинг алертов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:126`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:130`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:139`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:147`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:154`

### C07. Final use-case taxonomy spans full information lifecycle, not only scraping

- Concept: Структурированный список охватывает monitoring, change tracking, aggregation, dedup, semantic labeling, concept structures, trend tracking, insight extraction, reaction triggers, and syndication.
- Why it matters: Формирует полноту продуктового scope и предотвращает пропуск ключевых сценариев.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:241`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:258`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:276`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:293`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:338`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:383`

### C08. “Ongoing monitoring / standing query” is a distinct academic case class

- Concept: Регулярный, повторяющийся сбор информации по постоянной потребности выделяется в отдельную категорию непрерывного поиска/фильтрации.
- Why it matters: Поддерживает теоретическое обоснование monitoring-mode архитектуры.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:200`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:202`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:204`

### C09. Narrative/trend tracking maps to formal detection tasks (known topic tracking + new event detection)

- Concept: Отслеживание нарративов включает одновременно сопровождение известных тем и обнаружение новых событий/трендов.
- Why it matters: Уточняет алгоритмические цели trend analysis подсистемы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:206`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:208`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:210`

### C10. End-to-end value requires downstream content synthesis from collected signals

- Concept: Сбор и анализ информации завершаетcя синдикацией: дайджесты, аналитические тексты, видео/скрипты.
- Why it matters: Определяет конечный business outcome и формат выходных продуктов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:212`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:214`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:217`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:383`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0006-CHATGPT.md:394`

## Unresolved Ambiguities

1. Не определено, какие блоки типологии входят в MVP, а какие в последующие версии.
2. Не зафиксированы единые критерии дедупликации/канонизации для разных типов объектов (events/news/essays/repos).
3. Не определены метрики качества для narrative tracking и insight extraction.
