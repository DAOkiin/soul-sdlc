# I00-F0004-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0004-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md)

## Source

- chat_id: `I00-F0004-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил как системный архитектор структурировать полный pre-development пакет для гибкой parsing системы: кейсы, доменная модель, event model, стек, архитектура, DDL/модель данных и тестируемая симуляция до кода (`raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:4`).
2. Пользователь уточнил, что речь именно про DDL (а не IDL): заранее описать SQL схемы/вставки/запросы и тестировать модель данных до реализации сервисов (`raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:186`).
3. Пользователь запросил перепроверку обсуждённого через материалы крупных компаний и платформенных блогов, затем углублённый поиск по scraping pipeline architecture с event-driven фокусом (`raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:302`, `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:478`).

## AI Response Summary

1. Агент предложил SDLC-структуру артефактов и порядок работ до старта разработки с явными “пробелами, которые стоит закрыть” (`C01`, `C02`, `C03`, `C04`).
2. После уточнения акцент сместился в DDL-first: schema-as-contract, SQL queries library, fixtures, SQL-level tests, state-machine и schema evolution (`C05`, `C06`, `C07`, `C10`).
3. Углублённый ресёрч закрепил event-driven паттерны scraping/crawling: frontier/state/topics/contracts/retries/idempotency и decoupled raw snapshots (`C08`, `C09`).

## Extracted Concepts

### C01. Pre-code SDLC should be artifact-driven for parsing platform design

- Concept: До реализации кода формируется полный набор проектных артефактов (scope, use cases, domain/event models, architecture, contracts, data model, test/simulation plan).
- Why it matters: Снижает архитектурную неопределённость и делает этап реализации более детерминированным.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:15`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:155`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:167`

### C02. Use-case catalog needs operational fields beyond business narrative

- Concept: Каждый parsing кейс должен фиксировать trigger/source/content/change detection/rules/output/constraints.
- Why it matters: Превращает кейсы в executable design inputs для domain/event/data моделей.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:31`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:39`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:41`

### C03. Domain model and event model should be explicit, glossary-backed, and invariant-aware

- Concept: Нужны не только сущности/связи, но и инварианты, события, producers, payloads, handlers, guarantees, плюс единый глоссарий терминов.
- Why it matters: Обеспечивает консистентность терминов и корректную декомпозицию системы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:53`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:64`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:70`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:77`

### C04. Component architecture must include clear ownership boundaries and communication modes

- Concept: Архитектурный слой фиксирует компонентный состав, ответственность, границы и типы коммуникации без преждевременной детализации.
- Why it matters: Позволяет принять стек и контрактные решения на устойчивой основе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:83`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:90`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:93`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:97`

### C05. DDL (not IDL) is the intended source-of-truth contract before coding

- Concept: База проектируется через DDL как первичный контракт, к которому заранее пишутся SQL operations и тесты.
- Why it matters: Делает data layer верифицируемой до появления бизнес-логики сервисов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:186`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:190`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:213`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:224`

### C06. Data model should be split into bounded sub-schemas with query library

- Concept: Модель делится на Auth, Ingestion, Scheduling, Execution, Storage, Dedup, Rules/Notifications и сопровождается набором эталонных SQL-запросов.
- Why it matters: Упрощает эволюцию схемы и реализацию прикладного кода через стабильные SQL-контракты.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:200`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:203`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:207`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:230`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:237`

### C07. SQL-level test harness is a first-class pre-development deliverable

- Concept: До кода создаются fixtures и DB-tests в 3 слоях: DDL invariants, scenario tests (Given/When/Then), query behavior/idempotency tests.
- Why it matters: Поддерживает симуляцию работы системы и раннее выявление ошибок модели.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:245`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:254`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:259`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:265`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:274`

### C08. Event-driven scraping architectures converge on frontier/state/topic contracts and retry semantics

- Concept: Across researched systems recurring primitives are URL frontier, resource status model, topic contracts, duplicate/retry handling, and host politeness controls.
- Why it matters: Это минимальный набор архитектурных invariants для масштабируемых crawling pipelines.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:494`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:495`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:516`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:528`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:617`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:619`

### C09. Decoupling raw capture from extraction enables replay and resilient downstream modeling

- Concept: Снимки сырого HTML/контента хранятся отдельно, extraction выполняется независимо и может переигрываться.
- Why it matters: Улучшает воспроизводимость и упрощает testability data pipeline.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:587`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:593`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:595`

### C10. Two governance add-ons are mandatory: lifecycle state machines and schema evolution rules

- Concept: Для долгоживущей DDL-first архитектуры обязательны state machine ключевых сущностей и явные правила эволюции схемы.
- Why it matters: Без этого схема-контракт быстро деградирует при миграциях и ретраях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:294`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:295`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:435`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0004-CHATGPT.md:463`

## Unresolved Ambiguities

1. Не зафиксирована итоговая минимальная схема событий (event types + payload contracts) для MVP.
2. Не выбран конкретный путь миграций/версионирования DDL (tooling/process policy).
3. Не определено, какие внешние архитектурные паттерны войдут в baseline, а какие останутся исследовательскими референсами.
