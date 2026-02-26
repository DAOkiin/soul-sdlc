# I02-F0002-CHATGPT Concepts (Draft)

## Source

- chat_id: `I02-F0002-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь запросил полный англоязычный разбор SDLC W-Model: устройство процесса, части, роли/ответственности, важные нюансы, с опорой на первоисточники и экспертные материалы.

## AI Response Summary

1. [proposal] [A01] Ответ определяет W-Model как усиление V-Model через раннюю и параллельную тестовую работу по каждому артефакту разработки.
2. [proposal] [A02] Агент детализирует роли, гейты и циклы дефектов, подчеркивая разделение testing vs debugging и независимость проверки.
3. [risk] [A03] Отдельно разобраны ограничения и условия применимости: итеративность (multiple Ws), стоимость change churn, важность статических проверок и risk-based tailoring.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:4`
- A01: `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:16`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:22`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:30`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:69`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:75`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:83`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:87`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:93`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:99`
- A02: `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:105`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:153`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:142`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:144`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:157`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:163`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:185`
- A03: `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:196`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:199`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:205`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:213`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:218`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:220`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:224`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:255`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:285`, `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:298`

## Extracted Concepts

### C01. W-Model reframes testing as first-class from project start

- Concept: W-Model делает тестирование явным параллельным потоком с начала проекта, а не поздней фазой после кодинга.
- Why it matters: Снижает "test squeeze" и стоимость позднего обнаружения дефектов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:16`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:30`

### C02. Core invariant: each development artifact has a shadow test artifact

- Concept: Каждому work product разработки должен соответствовать ранний тестовый work product (criteria/plan/design/review evidence).
- Why it matters: Формирует системную трассируемость качества до этапа исполнения тестов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:69`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:75`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:83`

### C03. W-Model is a family (Herzlich- vs Spillner-oriented variants)

- Concept: В литературе W-Model имеет вариативность, но сохраняет инварианты: ранний test work, artifact verification, explicit retest loop.
- Why it matters: Позволяет адаптировать модель к контексту, не теряя сути.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:87`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:93`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:99`

### C04. Responsibility model must preserve perspective diversity

- Concept: Раннее сотрудничество dev+QA необходимо, но роли нельзя "смешивать" до потери независимого взгляда.
- Why it matters: Качество растет за счет различия perspectives, а не только за счет синхронизации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:105`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:153`

### C05. Testing and debugging are distinct lifecycle responsibilities

- Concept: Failures выявляются в тестировании, исправляются в отладке/разработке, затем подтверждаются повторным тестом.
- Why it matters: Разделение ownership критично для управляемого defect loop.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:142`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:144`

### C06. W-Model becomes operational via explicit quality gates

- Concept: Нужны entry/exit gates по ключевым фазам (requirements, architecture, detailed design, code complete, system-test readiness).
- Why it matters: Превращает модель из диаграммы в исполняемый процесс.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:157`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:163`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:185`

### C07. Iterative reality implies multiple overlapping mini-W cycles

- Concept: В итеративной разработке W-логика повторяется на каждом инкременте, а циклы могут накладываться во времени.
- Why it matters: Делает модель совместимой с современными sprint/release практиками.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:196`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:199`

### C08. Structural downside: early test asset churn under requirement volatility

- Concept: Раннее создание тестовых артефактов повышает стоимость изменений требований, если не управлять легковесностью и трассируемостью.
- Why it matters: Это главный practical tradeoff W-Model.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:205`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:213`

### C09. Static testing is mandatory, not auxiliary

- Concept: Ревью/инспекции/статанализ ранних артефактов — центральный механизм W-Model, а не optional add-on.
- Why it matters: Именно статические проверки дают дешёвое раннее предотвращение дефектов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:218`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:220`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:224`

### C10. Tailoring principle: W-Model is a communication framework, not rigid law

- Concept: Модель нужно адаптировать под контекст (risk, regulation, volatility), избегая буквального copy-paste диаграммы.
- Why it matters: Поддерживает применимость как в regulated, так и в fast-product средах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:255`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:285`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0002-CHATGPT.md:298`

## Unresolved Ambiguities

1. В источнике не выбрана конкретная адаптация W-Model под агентную SDLC-автоматизацию пользователя.
2. Не зафиксированы конкретные lightweight артефактные форматы для снижения change churn в high-volatility проектах.
