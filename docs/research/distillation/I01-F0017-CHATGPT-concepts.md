# I01-F0017-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0017-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь запросил план действий на основе уже подготовленных материалов (`agent-task-v1`, `agent-task-v2`, comparison, analysis, deep research, текущая сырая реализация) с логикой "зафиксировать процесс -> имплементировать код управления состоянием".
2. [request] [U02] Далее пользователь попросил зафиксировать принятые артефакты и перечислить критичные вопросы/решения, которые нужно закрыть сейчас; отдельно зафиксировал решение по runtime state: вариант A, один фиксированный путь, merge-конфликт как часть дизайна.

## AI Response Summary

1. [proposal] [A01] Агент собрал unified roadmap: закрепить архитектурные принципы, выбрать v1-базу для guards subsystem, внедрить pre-push enforcement, Mermaid-рендер и синхронизируемую документацию.
2. [proposal] [A02] В ответе зафиксированы принятые SoT-артефакты (DDL, runtime state A, guards config), исполняемый tooling-контур (compiler/runner/hooks/just/docs/tests) и контрольные DoD.
3. [decision] [A03] Агент выделил "дыры", требующие немедленных решений: state schema, merge policy для фиксированного state-файла, semantics `branch`, strict advance rules, version contract, command-guard policy, bypass policy, CI authority.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3978`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:11`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:16`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:22`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3776`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3829`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3868`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3964`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3780`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3806`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3814`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3831`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3840`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3848`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3983`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4000`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4002`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3996`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4003`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4006`
- A03: `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4062`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4068`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4124`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4133`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4139`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4144`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4155`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4159`, `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4169`

## Extracted Concepts

### C01. Planning from consolidated artifacts before coding

- Concept: План должен строиться из уже накопленного корпуса спецификаций, сравнений и исследований, а не с нуля.
- Why it matters: Снижает риск повторного проектирования и сохраняет эволюционную преемственность решений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:11`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:16`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:22`

### C02. V1-first implementation strategy with phased rollout

- Concept: Базовый путь внедрения — v1 архитектура guards-as-code (отдельный runner/config), поэтапно: runner -> pre-push -> render -> docs sync -> DX.
- Why it matters: Даёт быстрый запуск с контролируемой сложностью и последовательной интеграцией.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3776`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3829`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3868`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3964`

### C03. Guard runner as explicit enforcement subsystem

- Concept: Нужен отдельный guard runner (`process_guards.py`) с контекстами `pre_push`/`advance`, match `process_id/version`, changed-files filters и понятным PASS/FAIL/SKIP отчетом.
- Why it matters: Формализует enforcement и делает его переиспользуемым для hook/CLI/CI.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3780`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3806`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3814`

### C04. Pre-push fail-closed enforcement and changed-files optimization

- Concept: Pre-push должен выполнять guards до notes-sync, блокировать push при fail, и считать changed files по реальному push-диапазону.
- Why it matters: Обеспечивает реальный контроль качества без лишнего шума/затрат.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3831`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3840`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3848`

### C05. Runtime state variant A accepted as deliberate conflict surface

- Concept: Принят runtime state вариант A: один фиксированный путь в репозитории; merge-конфликты считаются осознанной частью дизайна.
- Why it matters: Упрощает локацию state и принуждает явное разрешение конкурентных изменений процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3983`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4000`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4002`

### C06. Source-of-truth artifact triad for process governance

- Concept: Core SoT триада: DDL процесса + runtime state + guards config, связанная одинаковым `process_id/version`.
- Why it matters: Формирует минимальный контракт согласованности для tooling и миграций.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:3996`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4003`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4006`

### C07. Immediate closure of architectural gaps before implementation

- Concept: Перед кодингом нужно закрыть критичные открытые решения: state schema, merge-policy, branch semantics, advance semantics.
- Why it matters: Без этого реализация будет нестабильной и неоднократно ломаться при рефакторинге.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4062`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4068`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4124`

### C08. Strict compatibility contract for process/state/guards versions

- Concept: Несовпадение `process_id/version` между артефактами должно приводить к hard fail.
- Why it matters: Предотвращает скрытую несогласованность и недостоверные проверки.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4133`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4139`

### C09. Command-guard security and runtime policy must be explicit

- Concept: Для guard-команд нужны ограничения и предсказуемый runtime (интерпретатор, timeout, whitelist/bounds).
- Why it matters: Уменьшает риски безопасности и зависания developer workflow.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4144`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4155`

### C10. Bypass must be traceable and reasoned

- Concept: Escape hatch допустим, но с обязательным reason и следом в истории/логах.
- Why it matters: Сохраняет управляемость и аудитируемость даже в emergency сценариях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4159`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0017-CHATGPT.md:4169`

## Unresolved Ambiguities

1. В источнике присутствует большая компиляция вложенных материалов; часть формулировок дублирует ранние документы и требует canonical dedup policy.
2. Не зафиксирован окончательный выбор формата Mermaid (stateDiagram-only или dual format со flowchart).
