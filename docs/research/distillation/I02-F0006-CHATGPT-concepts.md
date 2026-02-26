# I02-F0006-CHATGPT Concepts (Draft)

## Source

- chat_id: `I02-F0006-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил разложить, как AJTBD (по Замесину) детально встраивается в SDLC, с опорой на документы проекта, INCOSE и старый анализ.
2. [request] [U02] Далее пользователь запросил конкретную матрицу соответствия AJTBD и SDLC.
3. [next_step] [U03] Затем пользователь попросил перейти к следующему шагу внедрения.

## AI Response Summary

1. [proposal] [A01] Агент оформил AJTBD как сквозной слой SDLC: источник needs/requirements, архитектурных драйверов, testability и структуры документации, а не только discovery-активность.
2. [proposal] [A02] Была дана фазовая встройка в 12-фазную модель с gate/baseline и отдельным акцентом на ранние UDD/TVPL и W-model shift-left.
3. [proposal] [A03] В ответе предложены практические механики внедрения: requirement attributes, трассировка jobs->requirements->tests->docs, review-checklist и change seam.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:522`
- U03: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:319`
- A01: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:8`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:10`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:12`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:279`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:50`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:56`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:58`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:59`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:296`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:101`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:103`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:126`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:157`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:249`
- A02: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:76`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:78`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:87`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:89`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:284`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:101`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:103`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:126`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:157`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:249`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:267`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:273`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:391`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:395`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:397`
- A03: `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:63`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:64`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:66`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:281`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:176`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:177`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:184`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:187`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:283`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:168`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:295`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:496`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:556`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:560`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:510`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:511`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:512`, `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:513`

## Extracted Concepts

### C01. AJTBD should be treated as a cross-lifecycle layer, not a single discovery stage

- Concept: AJTBD формирует сквозной слой underlying analysis, который подпитывает требования, архитектуру, V&V и пользовательские артефакты по всему циклу.
- Why it matters: Это меняет место AJTBD в SDLC с разового исследования на управляемый инженерный контур.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:12`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:279`

### C02. AJTBD is the formal input for transformation into needs and design input requirements

- Concept: AJTBD выступает сырьем для формальной трансформации в Integrated Set of Needs и далее в Design Input Requirements по INCOSE.
- Why it matters: Обеспечивает совместимость discovery-данных с системной инженерией и governance требований.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:41`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:43`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:44`

### C03. Requirement-expression attributes are directly supported by AJTBD artifacts

- Concept: Job graph/evidence/outcomes покрывают ключевые атрибуты требования (rationale, trace to source, success criteria, method).
- Why it matters: Позволяет из AJTBD сразу формировать testable and traceable requirements.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:50`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:56`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:59`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:296`

### C04. Job graph acts as supporting model while requirements remain solution-free

- Concept: Job graph/CJM используется как supporting model, а сами требования удерживаются на уровне intent, без привязки к реализации.
- Why it matters: Снижает premature design lock-in и улучшает переносимость требований между решениями.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:63`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:64`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:66`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:281`

### C05. ISO 12207 constraints legitimize AJTBD outputs via traceability, baselining, and testability

- Concept: Требования 12207 к stakeholder needs baselining, traceability и анализу testability делают AJTBD-пакет официально релевантным инженерным входом.
- Why it matters: Даёт стандартную основу для институционализации AJTBD в процесс и аудит.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:76`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:78`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:87`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:89`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:284`

### C06. AJTBD must be mapped to specific SDLC phases, gates, and baselines

- Concept: Встройка AJTBD задается через 12 фаз, gate reviews и baseline points, а не через абстрактные рекомендации.
- Why it matters: Обеспечивает операционную привязку: где, когда и чем проверяется AJTBD-driven intent.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:101`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:103`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:126`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:157`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:249`

### C07. Early UDD/TVPL linkage is the key seam from jobs to docs and tests

- Concept: На фазе архитектуры ПО job flows/CJM должны сразу конвертироваться в UDD структуру и TVPL интеграционный план.
- Why it matters: Делает shift-left практическим и предотвращает отрыв документации/тестов от пользовательских работ.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:176`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:177`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:184`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:187`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:283`

### C08. Mandatory trace chain should be enforced as definition-of-done

- Concept: Нужно жестко поддерживать цепочку evidence -> job node -> SRS -> SRD -> design -> tests -> docs.
- Why it matters: Даёт механическую проверяемость полноты и снижает скрытый requirements debt.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:168`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:295`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:496`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:556`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:560`

### C09. AJTBD should continue in operations and maintenance, not stop at requirements

- Concept: Job-модель применима для acceptance support, training, incident classification и maintenance prioritization после релиза.
- Why it matters: Поддерживает непрерывную связь между реальными пользовательскими работами и lifecycle updates.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:267`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:273`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:391`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:395`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:397`

### C10. Incremental adoption pattern: pilot subsystem with minimal end-to-end trace

- Concept: Практический старт через один модуль и минимальную трассу job node -> requirements -> E2E tests -> user docs.
- Why it matters: Уменьшает стоимость внедрения и позволяет быстро проверить жизнеспособность шва AJTBD-SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:510`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:511`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:512`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0006-CHATGPT.md:513`

## Unresolved Ambiguities

1. Не зафиксирован единый формат идентификаторов для AJTBD job nodes/evidence в матрице следов.
2. Не определено, где именно хранить “source of truth” матрицу трассировки (MD/таблица/StrictDoc/другое).
3. Не задан policy, кто владелец обновлений A26 Stability/Volatility при требованиях и job-level изменениях.
