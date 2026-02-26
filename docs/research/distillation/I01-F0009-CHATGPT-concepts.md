# I01-F0009-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0009-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md)

## Source

- chat_id: `I01-F0009-CHATGPT`
- source_path: `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь предложил идею: фиксировать запросы репозиториев как отдельные артефакты с пояснениями, назначением и трассировкой использования (`raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:4`).
2. Затем пользователь запросил исследование: есть ли устоявшийся концепт и название для такого подхода (`raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:59`).
3. Далее пользователь последовательно попросил: сложное эссе, выверку, переход к двухуровневой модели документации (стандарт + skill), разработку `STANDARD.md`, валидацию + `SKILL.md`, и prompt для Codex по интеграции (с фиксированным стандартом `docs/_meta/QC-STANDARD.md`) (`raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:161`, `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:537`, `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:913`, `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1480`, `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1642`, `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:2723`).

## AI Response Summary

1. AI определил ближайшую терминологию: `Named Queries`, `Query Catalog/Registry`, `SQL-as-code`, `living documentation + lineage`, и runtime-корреляция через sqlcommenter/OTel (`C01`, `C03`).
2. AI оформил концепт Query Catalog как архитектурный слой операций над данными (не data dictionary), с требованиями к контракту, безопасности, транзакционности, ownership и lifecycle (`C02`, `C04`).
3. AI предложил двухуровневую документацию: нормативный стандарт + короткий operational skill, связанных атомарными правилами `QC-xx` (`C04`, `C05`).
4. AI добавил механический контур внедрения: schema + semantic rules + drift checks, CI-gates и map-first entrypoints; затем сформировал интеграционный prompt для Codex с привязкой к `docs/_meta/QC-STANDARD.md` (`C05`, `C06`, `C07`).

## Extracted Concepts

### C01. Идентификация концепта в индустриальной терминологии

- Concept: Идея пользователя уже существует как связка `Named Queries` + `Query Catalog/Query Registry` + `SQL-as-code`.
- Why it matters: Снимает неопределенность названия и дает терминологический каркас для стандартизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:67`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:81`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:100`

### C02. Query Catalog как first-class архитектурный артефакт

- Concept: Запрос рассматривается как самостоятельная единица архитектуры с именем, purpose, контрактом, контекстом использования и затрагиваемыми данными.
- Why it matters: Переносит контроль поведения системы на уровень операций над данными, а не только кода репозиториев.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:197`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:205`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:208`

### C03. Двуединая трассировка: статическая и рантайм

- Concept: Для Query Catalog необходимы оба контура: статическая связь use-case/call-site и runtime-корреляция через observability (sqlcommenter/OTel/APM).
- Why it matters: Обеспечивает не только проектную объяснимость, но и эксплуатационную диагностику.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:117`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:121`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:473`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:485`

### C04. Двухслойная документация как pattern agent-first SDLC

- Concept: Нормативный слой (`STANDARD`) хранит полный смысл и правила, а прикладной слой (`SKILL/Playbook`) дает короткие чек-листы и команды для агента/CI.
- Why it matters: Снижает токеновую нагрузку на агента, сохраняя полноту знаний в репозитории.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:547`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:563`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:579`

### C05. Атомарные правила QC-xx и машиночитаемый Registry

- Concept: Правила стандарта должны быть атомами с ID (`QC-01...`), связанными с машиночитаемым форматом (`yaml/json`) для автоматической проверки и ссылок в skill.
- Why it matters: Делает правила адресуемыми, трассируемыми и пригодными для CI enforcement.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:583`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:621`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1102`

### C06. Mechanical enforcement: validation stack + CI gates

- Concept: Внедрение строится на трех слоях валидации (schema, semantic rules, drift signals), policy-уровне строгости и обязательном CI job.
- Why it matters: Переводит качество каталога из "договоренности" в проверяемый процесс.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1506`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1515`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1525`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:1586`

### C07. Map-first интеграция в репозиторий для Codex

- Concept: Интеграционный prompt задает map-first подход: краткие entrypoints, ссылки на стандарт как source-of-truth, минимально-инвазивная интеграция schema/validator/skill/policy и CI.
- Why it matters: Согласует агентную работу с принципом "короткая карта + глубокие источники в репо".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:2658`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:2691`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:2735`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0009-CHATGPT.md:2783`

## Unresolved Ambiguities

1. Источник содержит смешанные данные: диалог, вставки распарсенной статьи OpenAI и пример чужого `SKILL`-документа; часть контента не является исходным авторским утверждением этой беседы и требует маркировки происхождения в дальнейшей синтезации.
2. Большая часть ссылок оформлена как `turnXsearchY`/`filecite`; без исходной среды чата внешние подтверждения ограниченно воспроизводимы.
