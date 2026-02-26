# I02-F0003-CHATGPT Concepts (Draft)

[Analyzed source: I02-F0003-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md)

## Source

- chat_id: `I02-F0003-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил структурировать идею проекта, цели и ментальные модели на основе большого накопленного контекста (`raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:4`).
2. В prompt встроен подробный материал по W-Model как методологической базе раннего тестирования, ролей и quality gates (`raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:6`).

## AI Response Summary

1. Агент предложил каркас проекта как "map, not monolith": северная звезда, ментальные модели, процессы, артефакты и словарь терминов (`C01`, `C02`, `C03`).
2. Ответ синтезирует три опоры: repo-as-system-of-record, W-Model SDLC discipline и event-centric ontology для state/policy reasoning (`C04`, `C05`, `C06`).
3. Даны операционная модель ролей/циклов, минимальный набор артефактов истины и требуемые outcomes (traceability, scalability, guardrails) (`C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. Project framing should start from North Star and control system intent

- Concept: Цель — агентно-управляемая разработка, где репозиторий является системой управления, а не только кодохранилищем.
- Why it matters: Задает критерии для структуры артефактов и автоматизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:395`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:399`

### C02. AGENTS should be a short map; docs should be source of truth

- Concept: AGENTS.md должен работать как TOC/карта, а детализация и истина процессов хранится в структурированном `docs/`.
- Why it matters: Снижает контекстную перегрузку и помогает поддерживать инструкции актуальными.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:414`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:418`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:420`

### C03. Mental models should be explicit artifacts

- Concept: Необходимо фиксировать отдельные ментальные модели проекта (миссия, loop, state/policy semantics), а не держать их неявно в переписке.
- Why it matters: Улучшает синхронизацию человека и агента при многосессионной работе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:391`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:412`

### C04. W-Model is used as SDLC discipline shape (artifact-first validation)

- Concept: W-Model здесь трактуется как дисциплина ранних проверок каждого артефакта с явной петлей test-fix-retest.
- Why it matters: Создает основу quality gates для агентной разработки.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:425`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:430`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:432`

### C05. Event-centric ontology supports explainable state transitions

- Concept: Состояние следует видеть как проекцию событийного графа, где переходы имеют причины и условия.
- Why it matters: Дает explainability и traceability для решений агента.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:436`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:444`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:445`

### C06. Integrated architecture: state + policy + mechanics + execution + feedback

- Concept: SDLC-control system складывается из state/facts, guard policies, enforcement mechanics (hooks/CI), agent execution and feedback loops.
- Why it matters: Позволяет проектировать систему как взаимосвязанные слои, а не набор разрозненных практик.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:451`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:455`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:460`

### C07. Human-agent operating model should define steering vs execution split

- Concept: Человек задает направление и правила, агент исполняет, а репозитория механика выступает неэмоциональным валидатором.
- Why it matters: Снижает операционную неоднозначность и нагрузку на владельца.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:469`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:471`

### C08. Decision log must be commit-linked artifact

- Concept: Решения должны фиксироваться с контекстом, альтернативами и ссылками на commit/PR.
- Why it matters: Обеспечивает воспроизводимость причинно-следственных связей в развитии проекта.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:509`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:512`

### C09. Shared glossary is required to prevent semantic drift

- Concept: Нужен единый словарь терминов (`fact`, `state`, `transition`, `guard`, `artifact`, `event graph`) для человека и агента.
- Why it matters: Уменьшает ошибки интерпретации и улучшает качество автоматизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:516`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:523`

### C10. Project outcomes should be stated as system requirements

- Concept: Цели проекта формулируются как требования к системе: единое состояние, guardrails, progressive context disclosure, traceability, scalability with parallel agents.
- Why it matters: Превращает vision в проверяемые engineering outcomes.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:529`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0003-CHATGPT.md:535`

## Unresolved Ambiguities

1. В ответе предложена высокоуровневая карта, но не зафиксирован минимальный machine-readable контракт state/policy для первой итерации.
2. Не определено, какие из предложенных моделей (W-Model vs event ontology) являются обязательными, а какие опциональными на старте.
