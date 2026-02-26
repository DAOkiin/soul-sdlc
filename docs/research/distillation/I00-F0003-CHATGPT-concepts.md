# I00-F0003-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0003-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md)

## Source

- chat_id: `I00-F0003-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил объяснить основные концепции AJTBD (`raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:4`).
2. Пользователь попросил повторно объяснить AJTBD на практическом кейсе поиска событий в Бангкоке/Таиланде с опорой на контекст parsing-проекта (`raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:90`).
3. Пользователь попросил помочь определить набор артефактов для итерационного цикла разработки (MVP), заменить персоны на AJTBD-артефакты, усилить трассируемость и перепроверить структуру документов без глубокого внешнего исследования (`raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:272`).

## AI Response Summary

1. Агент дал компактный каркас AJTBD: jobs as progress, job map, outcomes, forces of progress, segmentation by unmet outcomes (`C01`, `C02`, `C03`, `C04`).
2. На кейсе Thailand events AJTBD был приземлён в конкретный pipeline и сущностную модель (canonical events, source mentions, validation/monitoring) (`C05`, `C06`).
3. Для SDLC-контуров предложена AJTBD-first документационная архитектура: job catalog, iteration job pack, ADR слой, evidence-aware traceability chain (`C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. AJTBD models job as contextual progress, not task or feature

- Concept: Центральная единица AJTBD - движение из текущего состояния в желаемое в конкретной ситуации.
- Why it matters: Сдвигает фокус разработки с “списка фич” на реальный пользовательский прогресс.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:12`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:14`

### C02. Job Map is an 8-stage timeline where major innovation often lies before execution

- Concept: Работа раскладывается по стадиям define->locate->prepare->confirm->execute->monitor->modify->conclude; ценные улучшения часто в prepare/confirm/monitor.
- Why it matters: Помогает найти точки продуктового рычага за пределами “основного действия”.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:25`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:29`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:38`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:142`

### C03. Outcome statements must be measurable and solution-agnostic

- Concept: Outcomes формулируются как уменьшение/увеличение измеримых параметров (время, ошибки, уверенность, релевантность) без привязки к конкретной реализации.
- Why it matters: Делает связь discovery->requirements->acceptance проверяемой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:40`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:47`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:160`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:166`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:181`

### C04. Adoption dynamics are governed by push/pull/anxiety/habit forces

- Concept: Выбор решения объясняется балансом боли текущего состояния, привлекательности нового, тревоги изменений и силы привычки.
- Why it matters: Даёт operational рамку для product adoption strategy.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:49`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:53`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:183`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:189`

### C05. Thailand events pain translates into a canonical-event resolution objective

- Concept: Проблема “инфа размазана” преобразуется в цель: получить проверенный, дедуплицированный, actionable event list с планом действий.
- Why it matters: Превращает абстрактный pain в инженерно исполнимую целевую модель.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:90`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:102`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:104`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:148`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:263`

### C06. Rule-tool chain should explicitly implement extract/normalize/dedup/validate/rank/monitor

- Concept: AJTBD-ценность реализуется через последовательность специализированных правил обработки событий.
- Why it matters: Даёт прямое соответствие между outcome-болями и pipeline-функциями.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:212`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:216`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:227`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:232`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:238`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:242`

### C07. Personas can be replaced by job context cards without losing human relevance

- Concept: Вместо персон используется набор контекстов выполнения job (условия, ограничения, мотивации), привязанный к конкретному job.
- Why it matters: Лучше связывает пользовательские различия с требованиями и ранжированием, снижая абстракцию.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:372`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:382`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:386`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:390`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:397`

### C08. MVP development loop needs explicit job_pack and ADR artifacts as first-class inputs

- Concept: Итерация должна иметь baseline-набор артефактов: iteration README, job_pack, selected requirements, acceptance, traceability и отдельный ADR-слой.
- Why it matters: Делает процесс управляемым и объяснимым при изменениях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:403`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:417`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:432`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:446`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:466`

### C09. Traceability should run from evidence through outcomes to release learnings

- Concept: Рекомендуемая цепочка: Evidence->Job/Outcomes->Requirements->ADR->AC->Release/Learnings, с расширением ID-политики (`JOB/OUT/HYP/EVD`) и матрицы трассировки.
- Why it matters: Убирает разрыв между research и delivery-решениями.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:300`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:303`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:481`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:487`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:500`

### C10. Minimal structural patch enables AJTBD-first governance without heavy bureaucracy

- Concept: Достаточно добавить `docs/product/jobs`, `job_pack`, `adrs`, и lightweight evidence register, чтобы цикл стал AJTBD-first и traceable.
- Why it matters: Максимальный практический эффект при минимальных изменениях структуры.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:551`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:557`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:562`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:566`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0003-CHATGPT.md:577`

## Unresolved Ambiguities

1. Не принят окончательный выбор между “iteration pack only” и “canonical job catalog + iteration slices” (предложен компромисс).
2. Не зафиксирован точный шаблон `JOB`/`OUT`/`HYP`/`EVD` и governance правил для их обновления.
3. Не определено, как глубоко research должен участвовать в evidence links для каждого ADR на MVP-этапе.
