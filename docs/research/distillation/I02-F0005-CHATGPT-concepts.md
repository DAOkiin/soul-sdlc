# I02-F0005-CHATGPT Concepts (Draft)

## Source

- chat_id: `I02-F0005-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил проверить и усилить документальную концепцию на базе файлов проекта, с приоритетом заполнения уже существующих разделов.
2. [request] [U02] Дополнительное требование: изучить модель Болдачёва и встроить ее как неизменяемый слой архитектуры, поверх которого агенты смогут менять остальное.
3. [request] [U03] В исходном тексте пользователь зафиксировал North Star, enforcement-principles, requirements-as-code/StrictDoc traceability, двойной граф (FSM + artifact graph), TODO и идеи SDLC simulation/open-garden стратегии.

## AI Response Summary

1. [proposal] [A01] Агент подтвердил согласованность core-концепции с harness engineering и ISO/IEEE 12207: human-steering, docs as SoR, remediable linting, traceability as operational control.
2. [constraint] [A02] Предложено встроить Boldsea как immutable ontology/kernel (event DAG + constraints + engine/query/subscription), а policy/FSM/linters оставить mutable layer для агентной эволюции.
3. [proposal] [A03] В ответе даны точечные усиления существующих разделов: intent как артефакт, information-quality invariants, traceability invariants, W-model logic в PR-циклах, artifact catalog/glossary templates.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4`
- U03: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:8`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:58`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:98`
- A01: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:10`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:20`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:127`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:21`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:27`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:131`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:134`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:37`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:54`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:140`
- A02: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:60`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:66`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:70`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:117`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:163`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:165`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:177`
- A03: `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:157`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:182`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:189`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:144`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:146`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:147`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:149`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:263`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:272`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:275`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4326`, `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4336`

## Extracted Concepts

### C01. North Star aligns with agent-first SDLC governance

- Concept: Человек проектирует среду/intent/feedback loops, агенты выполняют PR-циклы, а система должна быть механически проверяемой.
- Why it matters: Это центральная operational philosophy проекта.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:20`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:127`

### C02. Docs-as-SoR requires measurable context quality and remediation-friendly enforcement

- Concept: Knowledge quality должна контролироваться через freshness/coverage/ownership/cross-links и lint/CI с remediation-oriented error messages.
- Why it matters: Делает агентную работу воспроизводимой без ручного контекстного “договаривания”.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:21`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:27`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:131`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:134`

### C03. Traceability is evolution control, not documentation overhead

- Concept: Traceability между requirements/design/tests/evidence/code должна выступать механизмом управления изменениями и visible debt.
- Why it matters: Позволяет автоматически выявлять незакрытые последствия изменения требований.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:140`

### C04. Dual-graph model: process FSM over artifact graph

- Concept: FSM процесса должен выполнять guards и effects как функции над графом требований/артефактов.
- Why it matters: Формализует связь process-state и knowledge-state.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:60`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:66`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:70`

### C05. Boldsea fits as immutable execution ontology

- Concept: Boldsea-kernel (event DAG, state as projection, dataflow conditions/causes, constraints) может выступать неизменяемой “конституцией” системы.
- Why it matters: Дает стабильный semantic foundation при изменяемых доменных политиках сверху.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:117`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:163`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:165`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:177`

### C06. Layering rule: immutable core, mutable policy/execution surface

- Concept: Event/constraint ontology фиксируется как immutable, а доменные модели, FSM-policies, linters/CI и визуализации остаются эволюционно изменяемыми через PR.
- Why it matters: Балансирует стабильность платформы и скорость агентных улучшений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:157`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:182`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:189`

### C07. Intent should be materialized as versioned artifact

- Concept: Понятие intent нужно перевести из концепта в артефактную форму (concept of operations/intent spec) с трассируемыми связями.
- Why it matters: Без этого agents и humans теряют общий референс "почему делаем".
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:144`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:146`

### C08. Information quality can be elevated to enforceable invariant set

- Concept: Атрибуты качества информации (unambiguous, complete, verifiable, consistent, modifiable, traceable, presentable) должны стать проверяемыми invariants контекста.
- Why it matters: Формирует objective baseline для качества документов в agent-first SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:147`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:149`

### C09. W-model logic can be embedded into PR cycles as mini-W

- Concept: Каждый PR может трактоваться как mini-W: ранние проверки артефактов, реализация, верификация/evidence, defect loop.
- Why it matters: Делает W-model practically executable в современном git-based workflow.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:263`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:272`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:275`

### C10. Seed strategy hinges on deterministic vs evolutionary path choice

- Concept: Первый SDLC seed должен явно определить режим: строго детерминированная автоматизация или эволюционная система с несколькими траекториями.
- Why it matters: Это определяет архитектуру правок, симуляций и governance.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4326`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0005-CHATGPT.md:4336`

## Unresolved Ambiguities

1. В источнике нет окончательно зафиксированной границы того, какие элементы Boldsea-kernel считаются “неизменяемыми” на уровне репозитория.
2. Не определен конкретный минимальный artifact catalog v0, который должен быть имплементирован первым в коде и линтерах.
