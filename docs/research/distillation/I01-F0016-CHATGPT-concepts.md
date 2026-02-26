# I01-F0016-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0016-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил сравнить `agent-task-v1.md` и `agent-task-v2.md` по сходствам и различиям.
2. [request] [U02] Далее пользователь запросил практический выбор для быстрого развития, сослался на принципы OpenAI harness engineering и попросил понять, какой вариант лучше и что стоит заимствовать.

## AI Response Summary

1. [proposal] [A01] Первая часть ответа раскладывает архитектурные различия v1/v2: где хранить guards, насколько богатая модель, где исполнять логику, детализация pre-push, тип Mermaid-рендера, подход к docs и тестам (-).
2. [proposal] [A02] Во второй части агент рекомендует v1 как базу для скорости итераций и низкой связности, а из v2 взять отдельные усиливающие механики (`must/should`, templating, JSON output, strict advance gating).

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:234`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:17`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:20`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:22`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:188`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:193`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:241`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:253`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:269`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:294`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:302`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:308`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:333`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:339`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:380`, `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:383`

## Extracted Concepts

### C01. Shared baseline: process-as-code with enforced pre-push checks

- Concept: Оба варианта сходятся в цели сделать SDLC исполняемым: CLI/manual checks, pre-push blocking, advance integration, diagram/doc generation.
- Why it matters: Фиксирует общую инвариантную архитектурную цель независимо от выбора v1/v2.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:17`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:20`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:22`

### C02. Primary architecture fork: guard storage location

- Concept: V1 отделяет guards config от DDL, V2 встраивает guards в DDL (process + step level).
- Why it matters: Это ключевой выбор, определяющий связность системы, скорость изменений и сложность схемы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:45`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:53`

### C03. Guard-model complexity tradeoff

- Concept: V1 предлагает минимальную практичную модель (`error|warn`, `changed_files_any`), V2 — более общий guard engine (`must|should`, phases, templating, checklist).
- Why it matters: Определяет баланс между скоростью внедрения и долгосрочной выразительностью политик.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:68`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:85`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:94`

### C04. Execution topology: separate runner vs unified compiler

- Concept: V1 вводит независимый `process_guards.py`, V2 расширяет `process_compiler.py` и делает единый CLI.
- Why it matters: Влияет на модульность, риск регрессий и стоимость сопровождения core compiler.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:102`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:114`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:120`

### C05. Pre-push policy details impact throughput

- Concept: V1 делает changed-files filtering и строгий `.venv` fail-closed режим; V2 проще и мягче деградирует до `python3`.
- Why it matters: Это напрямую влияет на latency pre-push цикла и надежность enforcement.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:140`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:143`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:145`

### C06. Different diagram/documentation philosophies

- Concept: V1 ориентирован на `stateDiagram-v2` + маркеры и sync script, V2 — на flowchart + template/render-doc.
- Why it matters: Меняет формат legibility для команды и способ поддержания документации в актуальном состоянии.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:150`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:166`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:178`

### C07. Testing strategy tied to architecture choice

- Concept: V1 тестирует отдельный guard runner, V2 — guard engine внутри process compiler.
- Why it matters: Точка приложения тестов отражает границы ответственности и будущую эволюцию кода.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:188`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:193`

### C08. Recommendation for speed: choose v1 baseline

- Concept: Для быстрого развития агент рекомендует v1 как базу из-за низкой связности, более дешевых изменений политик и отдельного guard subsystem.
- Why it matters: Снижает cost-of-change на ранней стадии, когда гейты часто меняются.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:241`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:253`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:269`

### C09. Harness engineering alignment: enforce invariants with strict boundaries

- Concept: Выбор должен поддерживать механическое enforcement инвариантов и четкие границы системы, чтобы скорость не порождала энтропию.
- Why it matters: Создает методологическое основание для архитектуры guard/harness слоя.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:294`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:302`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:308`

### C10. Hybrid strategy: v1 architecture + selected v2 features

- Concept: Наилучший практический компромисс — оставить v1 основу и заимствовать из v2 точечные усиления (`must/should + strict`, templating, JSON, mandatory advance guards).
- Why it matters: Дает быстрый запуск и контролируемую эволюцию без архитектурного перегруза.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:333`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:339`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:380`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0016-CHATGPT.md:383`

## Unresolved Ambiguities

1. Не определен момент перехода от гибридной v1+ к полностью DDL-native модели (если проект вырастет).
2. Не зафиксирован единый набор терминов (`context/severity` vs `phase/level`) для окончательной спецификации.
