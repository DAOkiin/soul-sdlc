# I01-F0010-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0010-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md)

## Source

- chat_id: `I01-F0010-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил инструкцию по `git worktree` для работы с Codex на macOS и параллельного запуска нескольких агентов в одном проекте (`raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:4`).
2. Пользователь уточнил, что нужны рекомендации и от официальных источников/опытных разработчиков (`raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:344`).

## AI Response Summary

1. AI дал базовый `git worktree` workflow: создание/листинг/удаление worktree, one-agent-one-branch и изоляция директорий (`C01`, `C02`).
2. AI дополнил это официальной моделью Codex app: режим Worktree, detached HEAD по умолчанию, `Create branch here` vs `Sync with local (Overwrite/Apply)`, хранение в `$CODEX_HOME/worktrees` (`C03`, `C04`).
3. AI зафиксировал operational guardrails: нельзя одновременно checkout одной ветки в двух worktree, нужен контроль cleanup/space, и выбор workflow зависит от локальной верификации (`C05`, `C06`).

## Extracted Concepts

### C01. `git worktree` как базовый механизм параллельной агентной разработки

- Concept: Один репозиторий может иметь несколько рабочих директорий с разными ветками без отдельного clone.
- Why it matters: Позволяет запускать несколько независимых агентных задач в одном проекте.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:16`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:21`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:31`

### C02. One-agent-one-worktree как основной safety-инвариант

- Concept: Для безопасного параллелизма каждый агент должен работать в отдельной ветке и отдельной директории; shared workspace запрещен.
- Why it matters: Исключает конкурентные конфликты и разрушение состояния рабочего каталога.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:177`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:182`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:281`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:283`

### C03. Официальный Codex app workflow: Worktree mode + detached HEAD

- Concept: В Codex app worktree создается в отдельном режиме; по умолчанию агент работает в detached HEAD, чтобы не занимать локальные ветки.
- Why it matters: Это снижает риск веточных коллизий и упрощает одновременные agent threads.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:358`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:362`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:433`

### C04. Два режима завершения агентной работы: branch-in-worktree vs sync-to-local

- Concept: Codex предлагает два официальных пути: либо создать ветку внутри worktree и вести PR оттуда, либо синхронизировать изменения в локальный checkout через Apply/Overwrite.
- Why it matters: Позволяет выбрать режим интеграции под ограничения проекта/локальной среды.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:366`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:373`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:378`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:441`

### C05. Ограничение Git: одна ветка не может быть checkout в двух worktree

- Concept: Одновременное использование одной и той же ветки в нескольких worktree запрещено; это фундаментальное ограничение модели.
- Why it matters: Определяет branch strategy для параллельных агентов и объясняет типичные ошибки синхронизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:371`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:463`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:487`

### C06. Операционный hygiene для масштабируемых worktree-практик

- Concept: Для стабильности нужны правила по location, cleanup/prune, контролю диска и корректному базированию веток от `origin/main`.
- Why it matters: Без hygiene параллельный режим быстро деградирует из-за мусора, конфликтов и устаревшей базы веток.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:252`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:264`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:384`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:389`

### C07. Выбор workflow определяется доступностью локальной проверки

- Concept: Если изменения можно валидировать прямо в worktree — предпочтителен branch-in-worktree; если окружение централизовано/тяжелое — Sync with local.
- Why it matters: Привязывает метод интеграции к реальным ограничителям верификации и CI-практики.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:440`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:441`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0010-CHATGPT.md:488`

## Unresolved Ambiguities

1. В источнике присутствуют ссылки-цитаты вида `turnXviewY` без самих страниц; внешняя проверка рекомендаций ограничена содержимым чата.
2. Документ дает обобщенные практики без привязки к конкретному стеку и CI-пайплайну проекта; для внедрения нужна локальная policy-спецификация веток и merge-гейтов.
