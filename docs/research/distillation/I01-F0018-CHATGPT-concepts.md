# I01-F0018-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0018-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md)

## Source

- chat_id: `I01-F0018-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил исследование проверенных подходов и готовых решений для программного управления состоянием графа разработки, с учетом уже подготовленных v1/v2 материалов и текущей реализации (`raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4`).
2. Неявная цель запроса: перед масштабной имплементацией выбрать, какие части лучше взять готовыми (hooks/policy/workflow/state tooling), а какие оставить кастомными (`raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:22`).

## AI Response Summary

1. Агент собрал обзор production-подходов: hook managers (`pre-commit`, `lefthook`), hard enforcement через CI/protected branches, policy-as-code (`OPA/Conftest`), FSM/workflow tooling и durable execution практики (`C01`-`C06`).
2. Ответ закрепляет архитектурный принцип: pre-push как быстрый feedback слой, а обязательные правила должны дублироваться в CI (`C07`).
3. В практической части дан конкретный интеграционный каркас `v1 + pre-commit + conftest`: snapshot contract, структура `policy/`, Rego правила, пример guard config, pre-push scripts и skeleton guard runner (`C08`, `C09`, `C10`, `C11`).

## Extracted Concepts

### C01. Existing project direction already aligns with best practices

- Concept: Текущая модель `DDL + state + guards` с контекстами `pre_push/advance/CI` совпадает с архитектурой зрелых orchestration/policy систем.
- Why it matters: Подтверждает корректность исходного направления и снижает риск "ложного старта".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:33`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:37`

### C02. Hook management should be delegated to proven tools

- Concept: Для надежной кроссплатформенной работы хуков стоит использовать `pre-commit` или `lefthook`, а не поддерживать полностью самописный lifecycle хуков.
- Why it matters: Уменьшает инфраструктурный долг и edge-case риски.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:51`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:56`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:67`

### C03. CI branch protection is mandatory layer for must-rules

- Concept: Локальные hooks не дают жесткого контроля (`--no-verify`), поэтому must-guards должны закрепляться required checks в CI/protected branches.
- Why it matters: Делает enforcement технически обязательным и неподверженным локальным обходам.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:71`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:80`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:82`

### C04. Policy-as-code can externalize guard semantics

- Concept: Структурированные DDL/state/guards данные подходят для policy-as-code движков (`OPA/Conftest`) вместо полного кастомного evaluator.
- Why it matters: Позволяет сократить объем самописной логики и использовать зрелый policy runtime.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:94`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:101`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:106`

### C05. Workflow/state runtimes provide reusable semantics, not mandatory migration

- Concept: FSM libraries and standard DSLs (ASL/SCXML) полезны как опорная семантика/валидация, но для текущего SDLC-графа могут быть избыточны как полная замена.
- Why it matters: Подсказывает прагматичный путь постепенного заимствования без platform overkill.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:112`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:148`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:153`

### C06. Durable execution pattern: event history as primary truth

- Concept: Для устойчивости и аудита важен паттерн event history/replay, а не молчаливая перезапись состояния.
- Why it matters: Укрепляет design runtime history в SDLC state management.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:179`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:191`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:193`

### C07. Pre-push should validate pushed refs, not dirty workspace

- Concept: Проверки должны опираться на refs/SHA того, что реально пушится, иначе появляются фантомные расхождения между локальным и CI.
- Why it matters: Повышает предсказуемость и доверие к результатам guard checks.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:209`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:215`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:221`

### C08. Recommended stack: keep v1 core, add targeted external primitives

- Concept: Практический выбор — оставить свой DDL/state/guard-runner, подключить hook manager, CI required checks и при необходимости policy-as-code.
- Why it matters: Обеспечивает быстрый прогресс без потери контролируемости архитектуры.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:235`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:241`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:245`

### C09. Snapshot contract for conftest integration

- Concept: Для Rego-проверок нужен единый snapshot (`state`, `guards`, `context`, `repo`, `exec`) как input contract между runner и policy engine.
- Why it matters: Делает guard evaluation детерминированным и тестируемым.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4553`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4561`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4564`

### C10. Rego rules encode severity and applicability logic centrally

- Concept: Rego-слой должен централизованно обрабатывать `severity`, context selection, `when.branch_in`, `when.changed_files_any`, and violations per guard type.
- Why it matters: Исключает дублирование бизнес-логики в хуках и ad hoc скриптах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4608`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4637`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4703`

### C11. Pre-push orchestration requires deterministic script contract

- Concept: Практическая обвязка должна включать fail-closed `.venv` policy, refs-based changed files, environment propagation и ordered execution (`guards` before `notes sync`).
- Why it matters: Формирует надежный runtime контур, пригодный для ежедневной эксплуатации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4883`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4897`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4925`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md:4952`

## Unresolved Ambiguities

1. В источнике объединены исследование и расширенный implementation draft; требуется отдельная canonical boundary между "рекомендовано" и "принято к внедрению".
2. Не зафиксирован окончательный выбор между чистым `.githooks/pre-push` stdin-механизмом и pre-commit pre-push env-моделью как первичным источником refs.
