# I01-F0008-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0008-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил спроектировать простой, но достаточный SDLC-процесс для агентской разработки и стартовать процесс с текущими материалами.
2. [request] [U02] Пользователь уточнил желаемый план: meta-документация (`SDLC.md`, `AGENTS.md`, `README.md`), приложение с итерационной документацией и запуск MVP.

## AI Response Summary

1. [proposal] [A01] AI предложил не строить SDLC с нуля, а взять Lean-адаптацию IEEE 12207 с легкими baseline-контрольными точками в git.
2. [proposal] [A02] AI оформил итерационный цикл в стиле V-подхода: scope -> design -> implementation/integration -> verification -> validation -> learnings.
3. [proposal] [A03] AI зафиксировал агентский governance-контур: `AGENTS.md` как instruction chain, one-task-one-branch, draft PR для долгих задач, интегратор как единственная точка merge.
4. [proposal] [A04] AI дал boot-sequence и шаблоны для `README/SDLC/AGENTS` и Iteration Pack.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:6`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:8`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:18`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:20`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:49`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:51`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:58`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:64`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:65`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:82`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:127`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:135`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:137`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:140`
- A03: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:148`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:150`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:152`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:166`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:168`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:170`
- A04: `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:219`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:226`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:230`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:194`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:200`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:204`, `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:207`

## Extracted Concepts

### C01. Lean-12207: фазы как чек-лист типов работ, а не водопад

- Concept: 12-фазный каркас IEEE 12207 предлагается использовать как перечень обязательных типов активности в итерации, без жесткой последовательности.
- Why it matters: Сохраняет нормативную полноту и совместимость с итеративной/агентной разработкой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:49`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:51`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:58`

### C02. Walkthrough/Inspection и baselines как минимальные quality gates

- Concept: Walkthrough используется как быстрый дизайн-обзор, Inspection как строгий defect gate; baselines реализуются через git tags + signoff-чеклисты.
- Why it matters: Дает проверяемость и дисциплину без тяжелой бюрократии.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:64`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:65`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:82`

### C03. Встроенный V-цикл итерации (Design Input -> Design Output -> Verification/Validation)

- Concept: Итерация оформляется как замкнутый цикл с явными стадиями верификации и валидации, завершающийся обновлением глобального слоя знаний.
- Why it matters: Создает воспроизводимый learning loop для эволюционирующего проекта.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:127`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:135`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:137`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:140`

### C04. AGENTS.md как машиночитаемый governance-контракт для Codex

- Concept: AGENTS.md и его иерархия override определяют поведение агента; процесс проектируется от этого факта.
- Why it matters: Это ключ к управляемости агентной разработки в репозитории.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:148`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:150`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:152`

### C05. Параллелизм через rule set: one task = one branch = one PR

- Concept: Для долгих агентских задач рекомендованы отдельные ветки/PR (включая draft) и один человеческий интегратор как единственная точка merge.
- Why it matters: Ограничивает "LLM-chaos" и делает интеграцию предсказуемой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:166`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:168`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:170`

### C06. Iteration Pack как обязательный минимальный пакет артефактов

- Concept: Для каждой итерации фиксируется компактный набор документов: scope, architecture, acceptance, traceability, reviews.
- Why it matters: Обеспечивает структурированное движение от требований к проверяемой поставке.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:219`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:226`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:230`

### C07. Старт процесса через "front-door trio": README + SDLC + AGENTS

- Concept: Запуск SDLC начинается с трех входных meta-файлов, которые синхронизируют людей и агентов по источнику истины и правилам выполнения.
- Why it matters: Убирает рассинхрон структуры репо, документации и агентных инструкций.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:194`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:200`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:204`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0008-CHATGPT.md:207`

## Unresolved Ambiguities

1. Агент отмечает отсутствие части загруженных материалов (аудио/архив) в текущей сессии, поэтому рекомендации опираются на частичный входной корпус.
2. В тексте присутствуют ссылки вида `turnXviewY`/`turnXsearchY`; внешние источники не воспроизводимы в этом markdown без исходной среды чата.
