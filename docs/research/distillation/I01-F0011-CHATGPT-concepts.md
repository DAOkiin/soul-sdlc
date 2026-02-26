# I01-F0011-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0011-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь запросил исследование проектов по агентам, которые программно управляют состоянием и переходами (state transitions) в процессе работы.
2. [request] [U02] В запросе описан целевой сценарий: отдельный worktree-состояние инициализируется при старте задачи, живет в течение task lifecycle, затем изменения вливаются в main, а временный worktree удаляется.
3. [request] [U03] Пользователь дополнительно попросил перевод документа на русский.

## AI Response Summary

1. [proposal] [A01] Ответ агента в этом источнике отсутствует; зафиксированы только пользовательские сообщения.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`
- U03: `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:8`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:1`

## Extracted Concepts

### C01. Stateful agent orchestration как целевая capability

- Concept: Пользователь ищет системы, где агент управляется через явные состояния и программируемые переходы между ними.
- Why it matters: Это формулирует необходимость state-machine уровня в agentic SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`

### C02. Worktree-scoped state lifecycle

- Concept: Состояние должно быть локализовано в отдельном рабочем контуре (worktree/task context), существовать на протяжении задачи и завершаться контролируемым merge+cleanup.
- Why it matters: Описывает практический lifecycle агентной единицы работы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`

### C03. Fast situational awareness через минимальный набор команд

- Concept: Требуется способ, чтобы агент "в паре команд" быстро понимал текущее состояние процесса и контекста.
- Why it matters: Это требование к наблюдаемости и операционной эффективности multi-agent среды.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`

### C04. Research-first подход к выбору архитектуры

- Concept: Перед внедрением пользователь хочет найти существующие проекты/попытки и опереться на практики, а не проектировать в вакууме.
- Why it matters: Снижает риск изобретения неустойчивых решений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0011-CHATGPT.md:4`

## Unresolved Ambiguities

1. В источнике нет ответа агента: нет подтвержденных внешних проектов, терминов и сравнений решений.
2. Запрос "переведи документ на русский" не содержит ссылки/вложения документа, который нужно переводить.
