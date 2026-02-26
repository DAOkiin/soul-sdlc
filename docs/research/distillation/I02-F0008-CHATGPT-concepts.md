# I02-F0008-CHATGPT Concepts (Draft)

[Analyzed source: I02-F0008-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md)

## Source

- chat_id: `I02-F0008-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил проверку консистентности документации по W-model SDLC и корректности рассуждений/выводов (`raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:4`).
2. Затем пользователь добавил набор нюансов из смежного исследования с пятью группами противоречий: фазность vs процессность, shift-left, stakeholder-level gap, терминология testing/debugging, риск устаревших интерпретаций (`raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:120`, `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:126`, `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:134`, `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:141`, `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:148`, `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:155`).

## AI Response Summary

1. Агент подтвердил, что базовый каркас (ISO как набор процессов + W-model как testing view) совместим, но требует строгого разведения уровней модели (`C01`, `C08`, `C10`).
2. Подтверждены и разложены конфликтные зоны из смежного исследования: старт тест-планирования, stakeholder-to-system мост, терминология debugging, риск waterfall-переинтерпретации 12207 (`C05`, `C06`, `C07`, `C09`).
3. Даны конкретные патчи: дисклеймеры для viewpoints, многослойный shift-left, trace AJTBD через stakeholder requirements, терминологический crosswalk и структурный чек-лист документации (`C04`, `C10`).

## Extracted Concepts

### C01. Normative anchor: ISO/IEC 12207 defines process sets, not a single phase model

- Concept: Нормативный слой должен оставаться процессным; фазовые схемы допустимы только как представления (viewpoints).
- Why it matters: Убирает ложное восприятие 12-фазной схемы как “официальной структуры стандарта”.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:173`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:180`

### C02. W-model semantics are internally consistent: early test stream + explicit re-test loop

- Concept: W-model сохраняет два потока (development/test), раннюю тест-подготовку и цикл test -> debug/change -> re-test.
- Why it matters: Это ключевая operational mechanics качества и предсказуемости дефект-цикла.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:16`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:27`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:28`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:271`

### C03. Gates and baselines should enforce test readiness of artifacts, not only test execution

- Concept: Quality gates валидируют готовность критериев, артефактов, среды и трассировки до запуска динамических тестов.
- Why it matters: Делает shift-left измеримым и уменьшает late-cycle quality debt.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:40`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:42`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:94`

### C04. Tailoring terminology must be split: practical model adaptation vs ISO Tailoring process

- Concept: Нужно явно различать “tailor W-model” как инженерную практику и “Tailoring process” как нормативный механизм conformance claim.
- Why it matters: Предотвращает нормативные ошибки при заявлении соответствия 12207.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:57`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:63`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:69`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:71`

### C05. Shift-left conflict is real and should be resolved by multi-horizon test planning

- Concept: W-model требует тест-активности с требований, но 12-фазный viewpoint называет TVPL лишь с архитектуры; нужен многоуровневый горизонт планирования тестов.
- Why it matters: Снимает внутреннее противоречие без отказа от любой из моделей.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:198`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:210`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:224`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:232`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:239`

### C06. AJTBD must map through stakeholder requirements before SRS/SRD

- Concept: AJTBD jobs/outcomes сначала должны формализоваться на stakeholder needs/requirements уровне, и только затем декомпозироваться в system/software requirements.
- Why it matters: Поддерживает корректную процессную архитектуру 12207 и требуемую traceability.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:247`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:252`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:258`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:262`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:336`

### C07. Testing/debugging distinction should be preserved but mapped to 12207 problem processes

- Concept: Разделение testing и debugging полезно, но в 12207-лексиконе debugging выражается через verification outputs + problem management/resolution artifacts.
- Why it matters: Согласует инженерный язык команды с терминологией стандарта.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:271`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:275`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:278`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:289`

### C08. Viewpoint sections need explicit labeling to prevent model-level leakage

- Concept: Каждый блок должен быть помечен как normative/informative viewpoint, иначе фазы, процессы и методы начинают смешиваться.
- Why it matters: Повышает управляемость документации и снижает риск ошибочных управленческих решений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:175`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:188`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:321`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:327`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:331`

### C09. Outdated waterfall interpretation risk persists despite explicit warnings

- Concept: Даже при оговорках 12-фазный артефакт может читаться как основная модель и конфликтовать с iterative/agile трактовкой 2017.
- Why it matters: Требует deliberate governance, чтобы viewpoint не стал de-facto norm.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:297`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:301`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:302`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:303`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:307`

### C10. Single reconciliation strategy: layered model + explicit crosswalks

- Concept: Противоречия снимаются через один слой модели: processes -> lifecycle model -> process views -> artifacts -> methods (AJTBD), плюс терминологические и трассировочные кроссвоки.
- Why it matters: Даёт системный способ удерживать консистентность при расширении corpus.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:315`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:321`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:325`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:333`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0008-CHATGPT.md:337`

## Unresolved Ambiguities

1. Не зафиксировано, какая именно формулировка shift-left станет канонической во всех связанных документах.
2. Не подтверждено цитатой из внутренних файлов утверждение о прямом маппинге AJTBD в SRS/SRD (агент указал отсутствие прямого текста).
3. Не определён mandatory формат viewpoint-disclaimer для всех документов корпуса.
