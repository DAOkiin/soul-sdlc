# I01-F0014-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0014-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md)

## Source

- chat_id: `I01-F0014-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил оценить идею управления разработкой через state machine по шкалам инновационности, оправданности и приоритетности фокуса (`raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:4`).
2. После первой оценки пользователь запросил сформулировать задачу для агента: реализовать guards, pre-push блокирующую проверку, визуализацию графа и markdown-шаблон с диаграммой и пояснениями, плюс предложить дизайн решения (`raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:191`).

## AI Response Summary

1. Агент оценил саму идею как не новую, но отметил высокую прикладную ценность repo-first реализации с process-as-code, quality gates и автоматизацией (`C01`, `C02`, `C03`).
2. В ответе выделены риски: дублирование источника истины, merge-конфликты общего state-файла, избыточная ручная рутина и слишком линейная модель (`C04`, `C05`).
3. Агент выдал полный implementation task для SDLC guard-подсистемы: отдельный guards config, guard runner CLI, обновление pre-push hook, Mermaid-рендер, sync docs script, tests и DoD (`C06`, `C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. State machine for SDLC is classic pattern, value is in implementation

- Concept: Концепт FSM для процесса разработки сам по себе "велосипед", но ценность появляется в конкретной проверяемой реализации.
- Why it matters: Разделяет novelty идеи и practical ROI инженерной системы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:70`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:72`

### C02. Process-as-code + artifact-linked gates

- Concept: Процесс должен жить в репозитории рядом с артефактами и валидироваться через формальные правила графа и SDLC-чекпоинты.
- Why it matters: Повышает воспроизводимость и трассируемость переходов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:60`

### C03. Focus criterion: manage facts, not people

- Concept: FSM в SDLC должен управлять фактами готовности (checks, artifacts, DoD), а не бюрократическим ручным контролем статусов.
- Why it matters: Снижает процессный шум и риск обхода системы командой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:94`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:100`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:111`

### C04. Single source of truth and state-scope design risk

- Concept: Опасно держать конфликтующие версии состояния в tracker/state/CI; общий state-файл в командной разработке ведет к гонкам.
- Why it matters: Требует проектировать state per task/branch/PR или derived state.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:122`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:127`

### C05. Automation-first transitions

- Concept: Система эффективна, когда большинство переходов происходит автоматически от сигналов репозитория и CI.
- Why it matters: Убирает ручную рутину и поддерживает устойчивую эксплуатацию процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:130`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:131`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:145`

### C06. Guards-as-code separated from DDL graph

- Concept: Guard-политики следует хранить в отдельном конфиге, а не смешивать с DDL графа.
- Why it matters: Упрощает эволюцию схемы и предотвращает перегрузку процессного DDL.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:224`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:236`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:245`

### C07. Pre-push as enforcement gate with fail-fast behavior

- Concept: Pre-push hook должен запускать guard checks и блокировать push при `error`-провалах, с ограниченным bypass.
- Why it matters: Делает соблюдение процесса технически обязательным, а не декларативным.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:225`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:345`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:473`

### C08. Context-aware guard execution using changed files

- Concept: Guards должны условно запускаться по branch и changed file patterns, а список изменений передаваться в runner/env.
- Why it matters: Балансирует качество и скорость проверок для реального developer workflow.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:266`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:270`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:295`

### C09. State diagram and docs sync as operational observability

- Concept: Нужны автогенерируемые Mermaid-диаграммы процесса и синхронизируемая markdown-документация с guard-таблицей.
- Why it matters: Делает процесс прозрачным и уменьшает дрейф между спецификацией и документацией.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:372`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:396`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:430`

### C10. Guard system requires explicit tests and bounded scope

- Concept: Подсистема guards должна иметь минимальный набор тестов, четкий DoD и ограничения по scope (без разрастания в универсальный engine/UI).
- Why it matters: Поддерживает качество и удерживает фокус на полезном SDLC-результате.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:445`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:458`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0014-CHATGPT.md:467`

## Unresolved Ambiguities

1. В задаче не указан желаемый приоритет внедрения deliverables (что first-class для первой итерации).
2. Не зафиксировано, должен ли `advance`-контекст guards быть обязательным в MVP или допустим как опциональный модуль.
