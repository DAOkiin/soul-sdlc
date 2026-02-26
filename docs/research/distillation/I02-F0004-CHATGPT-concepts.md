# I02-F0004-CHATGPT Concepts (Draft)

[Analyzed source: I02-F0004-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md)

## Source

- chat_id: `I02-F0004-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил подробно разобрать, как AJTBD Замесина стыкуется с SDLC, особенно в формировании требований и документации, и как это вписывается в цикл (`raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4`).

## AI Response Summary

1. Агент связал AJTBD и SDLC через артефакты: job graph/value/barriers/outcomes превращаются в requirement rationale, traceability и V&V критерии (`C01`, `C02`, `C03`).
2. Ответ детально маппит AJTBD на IEEE 12207 фазы и документы (SRS/SRD/SAD/UDD/TVPL), включая раннее shift-left планирование (`C04`, `C05`, `C06`).
3. Подчеркнуты операционные практики: матрица следов, lightweight change handling, структурированное хранение knowledge в репозитории и seed-дизайн на базе доменных знаний (`C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. AJTBD provides requirement intent layer (job/value/barrier/outcome)

- Concept: AJTBD дает причинно-следственную основу требований: работа пользователя, барьеры, ценность и измеримый прогресс.
- Why it matters: Делает требования обоснованными и связными с реальной пользовательской задачей.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:24`

### C02. AJTBD naturally fills INCOSE requirement attributes

- Concept: AJTBD-артефакты напрямую маппятся на requirement attributes типа rationale, trace-to-source, success criteria, method.
- Why it matters: Ускоряет переход от discovery к формальной инженерной спецификации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:48`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:61`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:229`

### C03. Work graph/CJM becomes backbone for tests and user docs

- Concept: Проекция job graph на время (CJM) может служить основой для E2E сценариев и структуры пользовательской документации.
- Why it matters: Создает единый язык между product discovery, тестированием и docs.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:69`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:72`

### C04. IEEE 12207 phases can host AJTBD outputs end-to-end

- Concept: AJTBD можно системно встроить в IEEE 12207 по фазам: discovery -> SRS -> SRD -> SAD -> coding/testing -> acceptance docs.
- Why it matters: Устраняет разрыв между product research и formal SDLC execution.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:93`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:113`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:144`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:207`

### C05. Early UDD/TVPL planning aligns with AJTBD shift-left

- Concept: Пользовательская документация и test/validation planning должны стартовать уже на архитектурной стадии, а не после кодинга.
- Why it matters: Повышает testability и качество UX-артефактов на ранних этапах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:38`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:165`

### C06. Requirements should remain solution-free unless justified

- Concept: Формулировки требований желательно держать solution-free, чтобы не зашивать реализацию без необходимости.
- Why it matters: Снижает преждевременную фиксацию дизайна и повышает адаптивность решения.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:183`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4531`

### C07. Traceability matrix is key bridging mechanism

- Concept: Нужна механическая матрица следов `jobs -> epics -> requirements -> tests -> user docs`.
- Why it matters: Обеспечивает сквозную верифицируемость и impact analysis при изменениях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:154`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4502`

### C08. Stability/volatility split should be explicit in requirements

- Concept: Job-level intent обычно стабилен, а solution/UI реализация волатильна; это нужно явно маркировать в requirement metadata.
- Why it matters: Помогает управлять change churn без ломки процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:87`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:89`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4434`

### C09. AJTBD knowledge must live as structured repo knowledge, not slideware

- Concept: Для работы в агентном SDLC AJTBD-артефакты должны храниться в структурированном репозитории с индексом и проверками связей/владения.
- Why it matters: Делает knowledge machine-readable и пригодным для автоматизации агентом.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:257`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:261`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4605`

### C10. Seed design question: deterministic automation vs evolutionary system

- Concept: При проектировании первого SDLC seed критичен выбор между строго детерминированной автоматизацией и эволюционной системой с множественными траекториями.
- Why it matters: Это определяет архитектуру guardrails, расширяемость и степень автономности агентов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4326`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0004-CHATGPT.md:4336`

## Unresolved Ambiguities

1. В источнике несколько повторных/вариативных формулировок одного mapping-блока; требуется canonical dedup при последующей синтезации.
2. Не выбран окончательный формат хранения AJTBD-графа (diagram-first vs structured schema-first) в SDLC репозитории.
