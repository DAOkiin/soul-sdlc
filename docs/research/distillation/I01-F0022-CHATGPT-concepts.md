# I01-F0022-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0022-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md)

## Source

- chat_id: `I01-F0022-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил реальные альтернативы Microsoft Agent Framework и обсуждение FSM+DSL как основы SDLC-автоматизации (`raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:4`).
2. Пользователь уточнил workflow-engine-centered модель, описал целевую операционную картину ("Nick + Codex", ограниченное время внимания) и попросил порядок реализаций/ответственностей (`raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:190`).
3. Пользователь запросил уточнение по механике `facts` и связал это с FSM-мышлением, попросив понять, как искать набор фактов и переходы между ними (`raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3013`, `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3164`).

## AI Response Summary

1. Агент подтвердил ценность MAF, но обосновал workflow-first архитектуру для SDLC (control plane отдельно от agent plane) и перечислил реальные альтернативы по слоям (`C01`, `C02`, `C03`).
2. В ответе предложен порядок ответственности при workflow-centered дизайне: DSL/FSM, policy budgets, idempotent activities, Codex integration, state/event governance (`C04`, `C05`, `C06`).
3. Дальше агент "сдул" Iteration 1 до минимального core-контракта (`process.yaml`, `state.yaml`, `events.jsonl`, `AGENTS.md`) и объяснил эволюцию DSL от реальных задач (`C07`, `C08`).
4. По вопросу facts агент дал практическую модель: facts как boolean truth set, stage FSM + fact state (factorized FSM), без перечисления полного графа переходов; operators (`preconds/add/delete`) вводить только по мере зрелости (`C09`, `C10`, `C11`, `C12`).

## Extracted Concepts

### C01. MAF is not a universal default; role separation matters

- Concept: Даже при сильном MAF нужно разделять выбор agent SDK и выбор workflow/FSM engine.
- Why it matters: Правильная архитектура зависит от control-plane требований, а не от популярности конкретного SDK.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:13`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:14`

### C02. Viable alternatives should be selected by operation model

- Concept: LangGraph/OpenAI Agents SDK/PydanticAI/CrewAI/ADK/managed services применимы в разных сценариях, но не закрывают одинаковые обязанности.
- Why it matters: Позволяет избежать ложного сравнения "кто лучше вообще" и выбрать стек по ответственности.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:20`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:33`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:80`

### C03. For FSM+DSL SDLC, workflow engine should be core

- Concept: Если цель — детерминированный SDLC-контур, workflow engine (Temporal/Step Functions/Durable/Camunda) должен быть "в центре", а agent frameworks — вторым слоем.
- Why it matters: Сохраняет audit/retry/approval guarantees независимо от недетерминированности LLM.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:107`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:160`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:179`

### C04. Workflow-centered SDLC requires explicit responsibility layers

- Concept: Обязательные слои включают process DSL, autonomy policy, idempotent activities, Codex step integration и governance вокруг human attention.
- Why it matters: Дает операционный порядок внедрения вместо ad hoc автоматизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:217`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:237`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:280`

### C05. Use Codex as constrained execution backend

- Concept: Codex возможности (`exec`, JSON outputs, sandbox, AGENTS contracts) следует использовать как execution substrate, а не как источник process truth.
- Why it matters: Уменьшает объем самописной инфраструктуры и удерживает контроль процесса в workflow/state layer.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:227`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:229`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:230`

### C06. Idempotency and retry-safety are non-negotiable for activities

- Concept: Все activities (git/ci/pr/quality) должны быть идемпотентны, иначе workflow retries будут ломать процесс.
- Why it matters: Критично для надежной long-running автоматизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:280`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:288`

### C07. Minimal Iteration-1 core should stay thin

- Concept: Базовое ядро можно держать в 3 файлах + протокол (`process.yaml`, `state.yaml`, `events.jsonl`, `AGENTS.md`) без раннего усложнения.
- Why it matters: Ускоряет запуск и снижает риск преждевременной over-engineering.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:2961`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:2966`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:2972`

### C08. DSL should evolve from recurring task pressure

- Concept: Новые элементы DSL нужно переводить в core только когда они повторяются и реально нужны для gate/tooling.
- Why it matters: Защищает от раздувания языка и сохраняет адаптивность.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3000`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3004`

### C09. Facts are boolean truth set, not status replacement

- Concept: `facts[]` — это множество булевых утверждений, где присутствие = true, отсутствующее значение не утверждено как true.
- Why it matters: Формирует простую и расширяемую основу состояния без умножения специальных полей.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3017`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3023`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3034`

### C10. Full state is factorized as (stage, facts_set)

- Concept: Практическая модель — маленький явный stage FSM + растущий fact-state, а не перечисление всех комбинированных состояний.
- Why it matters: Предотвращает 2^N explosion и сохраняет управляемость.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3174`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3221`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3223`

### C11. Operators are optional and should be introduced on demand

- Concept: `preconds/add/delete` операторный слой нужен только для validation/autosuggestion/deterministic plan generation, не обязателен в Iteration 1.
- Why it matters: Удерживает MVP простым и вводит формализм только при реальной пользе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3195`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3252`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3326`

### C12. Fact hygiene rules are critical for reliability

- Concept: Нужны строгие правила именования, XOR-пары pass/fail, привязка facts к событиям, запрет значений внутри fact-строк.
- Why it matters: Иначе факт-модель быстро деградирует в невалидный и нетрассируемый слой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3100`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3112`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md:3119`

## Unresolved Ambiguities

1. В файле нет финальной фиксации, когда именно переходить от facts-only модели к operator-based planning в прод контуре.
2. Не закреплен canonical словарь стартовых facts на уровне общего стандарта (предложены варианты, но не утверждена версия).
