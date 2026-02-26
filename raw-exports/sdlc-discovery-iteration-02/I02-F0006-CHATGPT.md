# AJTBD в SDLC

<user>
Как AJTBD от замесина ложится на SDLC? Понимаю, что это этап дискавери, что оно касается формирования требований и другой документации. Разберись где точки соприкосновения и как AJTBD детально вписывается в цикл. Полагайся на файлы в проекте. Так же прикладываю документ описывающий как incose видит управление требованиями. Так же прикладываю старую версию подобного анализа, но она делалась на неполных документах по процессу SDLC. 

</user>
<agent>
Согласно документам проекта (AJTBD.md, SDLC\_12207\_Synthesis.md, CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md и INCOSE GtWR v4 Summary Sheet, загруженным 23.02.2026), AJTBD разумнее «класть» на SDLC не как *один* этап дискавери, а как **сквозной слой**:

- **на входе** — даёт *underlying analysis* (граф работ, барьеры, контексты, outcomes, evidence), из которого формально получаются needs/requirements;
- **в середине** — питает архитектуру/дизайн (allocation, интерфейсы, NFR/constraints);
- **на выходе** — становится «хребтом» для верификации/валидации, тест‑планирования и пользовательской документации.

Это прямо совпадает с тем, как INCOSE описывает роль needs/requirements: они «сквозная нить» всех артефактов жизненного цикла; после верификации/валидации needs — все последующие артефакты валидируются относительно needs, а после верификации/валидации design input requirements — все последующие артефакты верифицируются относительно них【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】. И INCOSE отдельно подчёркивает: *underlying analysis*, из которого получено need/requirement, «настолько же важно», как и качество формулировки самого statement【126:17†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L83-L84】 — это буквально «легитимизирует» AJTBD‑артефакты как часть управляемой системы требований.

Ниже — сначала точки соприкосновения, потом «как по фазам» (по 12‑фазной интерпретации SDLC/12207 из SDLC\_12207\_Synthesis).

---

## 1) Что именно из AJTBD “ложится” на SDLC

В AJTBD центральная работа — построение **графа работ** (work/job graph): список «работ/действий» плюс ограничения и контекст выполнения, а также работа с барьерами/ограничениями; при этом метод в значительной мере опирается на интервью и имеет ограничения (например, синхронные интервью не выявляют бессознательное)【88:0†AJTBD.md†L1-L18】.

Если перевести на язык системной инженерии и SDLC:

- **Job graph / critical sequence / сценарные маршруты** → будущие «use cases / operational scenarios» → архитектурные драйверы и E2E‑сценарии.
- **Барьеры и ограничения** → constraints / quality requirements (надёжность, безопасность, наблюдаемость, UX‑ограничения и т.п.) → архитектурные решения и тесты на «края».
- **Outcomes / “что значит успех”** → измеримые success criteria → acceptance criteria → критерии валидации.
- **Evidence** (ссылки на интервью/наблюдения/данные) → Trace to Source + Rationale (почему требование существует).

---

## 2) Мостик через INCOSE: как AJTBD превращается в управляемые требования

INCOSE формализует, что:

- **Need statement** — это результат формальной трансформации источников/концептов в согласованное ожидание【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L16-L17】.
- **Requirement statement** — результат формальной трансформации источников/needs/требований более высокого уровня в согласованное обязательство【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L18-L20】.
- И need/requirement “expression” — это statement + атрибуты управления【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L36-L37】.

То есть AJTBD — это не «требования сами по себе», а **сырьё для формальной трансформации** в:

- **Integrated Set of Needs** (структурированный набор согласованных needs, задающий объём валидации)【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L25-L29】;
- **Design Input Requirements** (структурированный набор требований, относительно которых система верифицируется)【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L30-L33】.

### 2.1. Какие атрибуты требований AJTBD закрывает “нативно”

INCOSE даёт «минимальный набор» атрибутов требований (отмечены \* в документе), среди них:

- A1 Rationale\*, A2 Trace to Parent\*, A3 Trace to Source\*;
- A6 Success Criteria\*, A7 Strategy\*, A8 Method\*;
- A15 Unique Identifier\*, A17 Originator/Author\*, A19 Owner\*, A34 Priority\*, A26 Stability/Volatility и др.【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L47】.

AJTBD идеально ложится именно на это:

- **Rationale (A1)** = “какой job/прогресс закрываем и почему это важно” (из job graph + интервью).
- **Trace to Source (A3)** = ссылка на evidence (интервью/наблюдение/данные).
- **Success Criteria (A6)** = outcomes/метрики “что значит успех”.
- **Method (A8)** = как это проверяем (тест/инспекция/анализ/демо) — это можно и нужно задавать уже на уровне требований (см. ниже про testability и W‑model).

### 2.2. Важные правила INCOSE, которые помогают “вшить” AJTBD

- **Solution Free (R31)**: требование не должно «тащить» конкретную реализацию【126:16†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L34-L35】.
- **Supporting Diagram/Model (R23)**: допускается/рекомендуется опираться на диаграммы/модели как поддерживающий артефакт【126:16†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L26-L27】.

Job graph как раз выступает **supporting model**, а jobs/outcomes помогают удержать требования «solution‑free» (про intent/ценность, а не про кнопки/эндпоинты).

---

## 3) Мостик через ISO/IEC/IEEE 12207: почему AJTBD “официально уместен” внутри SDLC

В 12207‑подходе (в тексте CAN/CSA ISO/IEC/IEEE 12207:2018) есть два особенно важных момента:

1. На уровне работы со стейкхолдерами процесс требует:

- определить stakeholder needs/requirements и operational concept;
- установить и поддерживать трассируемость;
- **забейзлайнить** stakeholder needs/requirements и operational concept【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L4】.

Это почти прямое описание того, что вы получаете на выходе AJTBD (needs + evidence + контекст/ops‑логика), если оформить это как baseline‑артефакт.

2. Требования **не должны подразумевать конкретную реализацию** (“should not imply any specific implementation”)【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L40-L44】 — это совпадает с INCOSE R31 (solution‑free) и поддерживает «job‑формулировки» как правильный источник intent.

3. На уровне software requirements стандарт требует:

- трассировать software requirements к system requirements;
- анализировать требования на корректность и **testability**, feasibility, compliance, completeness, consistency【110:6†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L5】.

То есть если AJTBD даёт outcomes и контексты, вы буквально повышаете testability требований (и проще проходите анализ требований на “testability”).

4. Верификация в 12207 охватывает не только “готовый продукт”, но и **промежуточные артефакты** (требования, архитектуру, дизайн, пользовательскую документацию и т.д.), а методы включают inspection, analysis, demonstration и test【110:1†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L47-L59】. Это делает AJTBD‑слой полезным не только “до кодинга”, но и в ревью/инспекциях артефактов.

---

## 4) Почему здесь очень к месту W‑model и “shift‑left”

W‑model (в вашем w-model.md) усиливает идею: тест‑планирование начинается сразу после определения требований; тестовая активность идёт параллельно каждой стадии разработки; а на каждой стадии есть reviews/inspections, позволяющие ловить дефекты раньше【92:1†w-model.md†L1-L21】. Это напрямую совпадает с тем, что SDLC\_12207\_Synthesis показывает как обязательные walkthrough/inspection и ранний старт UDD/TVPL (см. ниже).

---

## 5) Как AJTBD детально вписывается в 12‑фазный SDLC (по SDLC\_12207\_Synthesis)

В SDLC\_12207\_Synthesis жизненный цикл разложен на 12 фаз【126:14†SDLC\_12207\_Synthesis.md†L5-L16】 с gate‑review’ами и baseline‑точками (Functional Baseline, Allocated Baseline, Developmental Configuration, Test Baselines, Product Baselines и т.д.)【126:15†SDLC\_12207\_Synthesis.md†L15-L27】.

Ниже — практическая «встройка» AJTBD по фазам.

---

### Фаза 0. До формального SDLC: AJTBD‑discovery как “baseline источника”

Хотя в 12 фазах явно не выделено «discovery», ISO 12207 ожидает, что вы определите и забейзлайните stakeholder needs/requirements и operational concept【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L4】.

Как это сделать минимально жизнеспособно:

- Создайте **AJTBD‑пакет** как управляемый артефакт (в репо/Confluence, но с версионированием):
  - job graph (v0),
  - evidence‑каталог (ссылки на интервью/данные),
  - список outcomes и контексты (conditions of use),
  - список барьеров/ограничений.
- Этот пакет становится “Trace to Source” для требований (INCOSE A3) и «поддерживающей моделью» (INCOSE R23)【126:16†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L26-L27】.

---

### Фаза 1. System Requirements Analysis → SRS + SRR + Functional Baseline

По SDLC синтезу: на фазе 1 есть gate **System Requirements Review**, baseline **Functional Baseline** и record SYRER【126:14†SDLC\_12207\_Synthesis.md†L20-L23】.

**Как AJTBD вкладывается в SRS:**

1. **Jobs → capability requirements** (что система должна позволять сделать).
2. **Барьеры/ограничения → constraints / quality requirements**.
3. **Outcomes → success criteria (A6) и стратегия/метод проверки (A7/A8)**【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L14-L18】.
4. **Evidence → Trace to Source (A3) и Rationale (A1)**【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L9】.

**Что проверять на SRR (практический чек):**

- покрыта ли критическая последовательность работ (нет ли «дырок» в job graph → requirements);
- каждое ли требование “solution‑free” (INCOSE R31 и ISO “не подразумевать реализацию”)【126:16†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L34-L35】【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L40-L44】;
- у каждого ли требования есть success criteria + метод проверки (A6/A8)【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L14-L18】.

---

### Фаза 2. System Architectural Design → SARAD + SDR

На фазе 2 gate — **System Design Review** и record SYAER【126:14†SDLC\_12207\_Synthesis.md†L22-L23】.

**Как AJTBD помогает SARAD:**

- job graph показывает, **какие шаги работы** автоматизируются системой, какие остаются на человеке/процессе (allocation);
- критическая последовательность работ превращается в **сквозные системные сценарии**, которые архитектура обязана поддерживать;
- барьеры становятся архитектурными драйверами (наблюдаемость, аудит, безопасность, восстановление, целостность и т.п.).

---

### Фаза 3. Software Requirements Analysis → SRD + SSR + Allocated Baseline

На фазе 3 gate — **Software Specification Review**, baseline — **Allocated Baseline**, record SORER【126:14†SDLC\_12207\_Synthesis.md†L23-L25】.

**Как AJTBD вкладывается в SRD:**

- вы «переупаковываете» intent из job‑уровня в software behavior/data/interface requirements, *но сохраняете трассировку*:
  - SRD requirement → (Trace to Parent) system requirement → (Trace to Source) AJTBD evidence/job node.

Это совпадает с требованием 12207: software requirements трассируются к system requirements и анализируются на корректность/testability и т.д.【110:6†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L5】.

**Ключевая механика, чтобы AJTBD не “умер”:**

- делаете трассировку «job node → system req → software req → тесты/валидация → доки» (см. ниже).

---

### Фаза 4. Software Architectural Design → SAD + ранние UDD/TVPL + PDR

Это одна из главных точек соприкосновения. В SDLC\_12207\_Synthesis прямо указано, что уже на фазе 4 появляются:

- SAD, SIDD, DDD,
- **UDD (Preliminary)**,
- **TVPL (Soft‑Int)**【104:1†SDLC\_12207\_Synthesis.md†L3-L6】,

а gate — **Preliminary Design Review** и baseline — **Developmental Configuration**【126:14†SDLC\_12207\_Synthesis.md†L24-L25】.

**Как сюда “вшивается” AJTBD:**

- В старой версии анализа у вас очень точная формулировка: CJM/маршрут работ — это *проекция графа работ на временную ось*, которая превращается в сценарии, acceptance criteria, E2E‑тесты и структуру пользовательской документации【126:1†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】.
- Это идеально совпадает с тем, что SDLC ожидает на фазе 4:
  - **UDD (Preliminary)** = каркас документации строится по «как пользователь делает работу»;
  - **TVPL (Soft‑Int)** = план интеграционных проверок строится по ключевым сквозным сценариям jobs + проверкам барьеров.

---

### Фаза 5. Software Detailed Design → SDD/DIDD + обновления UDD/TVPL + CDR

По work‑products: на фазе 5 есть SDD, DIDD, **UDD (Update)**, **TVPL (Soft‑Unit)** и **TVPL (Soft‑Int‑Update)**【104:1†SDLC\_12207\_Synthesis.md†L4-L6】. Gate‑логика CDR в схеме SDLC также присутствует【126:3†SDLC\_12207\_Synthesis.md†L7-L8】.

**Роль AJTBD на этом уровне:**

- AJTBD уже не «генератор требований», а **контроль соответствия детализации** ключевым работам и барьерам:
  - дизайн не должен “сломать” критический маршрут,
  - барьеры должны быть закрыты конкретными механизмами (и иметь тест‑проверки),
  - UDD обновляется так, чтобы документация поддерживала выполнение работ.

---

### Фаза 6. Software Coding and Testing → Unit/DB + TVPR/TVRR (Unit) + обновления

По work‑products: Software Unit, Database, TVPR/TVRR (Soft/DB‑Unit), UDD Update, TVPL (Soft‑Int‑Update)【104:1†SDLC\_12207\_Synthesis.md†L5-L7】.

**Роль AJTBD:**

- привязка unit‑тестов и проверок БД к требованиям, которые трассируются к jobs/outcomes;
- барьеры → негативные/краевые тесты (ошибки, отмены, повторы, недоступность, ограничения прав и т.д.).

---

### Фаза 7. Software Integration → SOIP + TVRR (Soft‑Int) + STRR + Test Baseline (Soft‑Int)

Gate — **Software Test Readiness Review**, baseline — **Test Baseline (Soft‑Int)**【104:0†SDLC\_12207\_Synthesis.md†L2-L4】; work‑products включают SOIP, TVRR (Soft‑Int), UDD Update, TVPR (Soft‑Qual)【104:1†SDLC\_12207\_Synthesis.md†L7-L8】.

**Где AJTBD особенно полезен:**

- строите интеграционный набор тестов как «прохождение ключевых работ» (сквозные сценарии) + проверки барьеров;
- закрываете “testability” требований: outcomes → измеримые проверки (время/ошибки/полнота результата).

---

### Фаза 8. Software Qualification Testing → TVRR (Qualification) + SFQR + Software Product Baseline + FCA/PCA

Gate — **Software Formal Qualification Review**, baseline — **Software Product Baseline**【104:0†SDLC\_12207\_Synthesis.md†L3-L5】; в фазе есть FCA/PCA‑аудиты с SIAR【126:15†SDLC\_12207\_Synthesis.md†L6-L13】.

**Роль AJTBD:**

- квалификационные проверки удобно строить как “валидацию работ”: достигли ли outcomes в реальных conditions of use (A12);
- evidence из AJTBD помогает обосновать, что вы тестируете именно «правильные вещи» (а не случайный набор сценариев).

---

### Фаза 9. System Integration → SYRR + Test Baseline (Sys‑Int)

Gate — **System Test Readiness Review**, baseline — **Test Baseline (Sys‑Int)**【104:0†SDLC\_12207\_Synthesis.md†L5-L6】; work‑products включают TVRR (Sys‑Int) и TVPR (Sys‑Qual)【104:1†SDLC\_12207\_Synthesis.md†L9-L11】.

**Роль AJTBD:**

- те же jobs‑сценарии, но уже на уровне всей системы/подсистем, включая интеграции «наружу» и организационные шаги.

---

### Фаза 10. System Qualification Testing → System Product Baseline + формальная приёмка

Gate — **System Formal Qualification Review**, baseline — **System Product Baseline**【104:0†SDLC\_12207\_Synthesis.md†L6-L7】.

**Роль AJTBD:**

- финальная валидация относительно Integrated Set of Needs (INCOSE‑логика: “Are we building the right thing?”)【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L55-L56】.

---

### Фаза 11. Software Installation → SIP

Work‑product: SIP【104:1†SDLC\_12207\_Synthesis.md†L12-L13】.

**Роль AJTBD:**

- установка/ввод в эксплуатацию — часто часть «работы пользователя/оператора»; job graph помогает не забыть про реальные шаги внедрения, ограничения среды, обучение.

---

### Фаза 12. Software Acceptance Support → TVRR (Soft‑Acc) + Training

Work‑products: TVRR (Soft‑Acc) и Software Training【104:0†SDLC\_12207\_Synthesis.md†L8-L10】.

**Роль AJTBD:**

- acceptance support и обучение лучше всего строятся по «как выполнять работы» (jobs) и по типовым барьерам/ошибкам.

---

## 6) Самые важные точки соприкосновения “в одном списке”

1. **Formal transformation:** AJTBD = источники/анализ → need/requirement statements (INCOSE)【126:8†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L16-L20】.
2. **Traceability:** evidence из AJTBD закрывает A3 Trace to Source (INCOSE)【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L9】 и совпадает с требованием 12207 «установить и поддерживать трассируемость»【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L4】.
3. **Solution‑free требования:** jobs помогают писать требования без “как именно реализовать” (INCOSE R31 + ISO)【126:16†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L34-L35】【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L40-L44】.
4. **Testability / shift‑left:** outcomes → success criteria/method, а W‑model и 12207 поддерживают ранние ревью/инспекции и проверку промежуточных артефактов【92:1†w-model.md†L1-L21】【110:1†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L47-L59】.
5. **Ранние UDD/TVPL:** SDLC ожидает, что UDD (Preliminary) и TVPL (Soft‑Int) стартуют уже на архитектуре ПО【104:1†SDLC\_12207\_Synthesis.md†L3-L6】 — это прямое место, где CJM/job‑маршруты превращаются в структуру документации и тест‑план.
6. **Baseline‑управление:** SDLC фиксирует baseline‑точки (Functional/Allocated/Developmental/Test/Product)【126:15†SDLC\_12207\_Synthesis.md†L15-L27】, а 12207 требует baselining stakeholder needs/requirements【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L4】 — значит AJTBD‑артефакты нужно версионировать/управлять изменениями, иначе трассировка «поплывёт».
7. **Stability/volatility:** полезно явно отмечать стабильность job‑уровня и волатильность реализаций (UI и т.п.) — это напрямую поддерживается атрибутом A26 Stability/Volatility【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L37-L38】 (в старом анализе это уже отмечено как практическая идея)【126:6†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】.

---

## 7) Практический “шов”, чтобы AJTBD реально жил в SDLC

Если свести к минимальному набору механик:

1. **AJTBD‑пакет** (job graph + evidence + outcomes + barriers) — конфигурационно управляемый артефакт.
2. **Трассировка** (хотя бы таблица/ссылки):\
   evidence → job node → SRS requirement → SRD requirement → design element (SAD/SDD) → test case (TVPR/TVRR) → doc section (UDD).
3. **Каждое требование** храните как requirement expression (statement + атрибуты), минимум: A1/A3/A6/A8 + owner/priority/stability【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L18】【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L26-L38】.
4. На каждом gate‑review (SRR/SSR/PDR/STRR/…):
   - проверка покрытия критической последовательности jobs;
   - проверка testability (есть outcomes → критерии/метод);
   - проверка solution‑free.

---

## 8) Что принципиально “добавилось” по сравнению со старой версией анализа

В старом анализе уже правильно пойманы ключевые места (rationale/traceability, ранний старт UDD/TVPL, CJM→сценарии/тесты/доки)【126:1†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】. Новое, что становится яснее при опоре на полный SDLC\_12207\_Synthesis и CAN/CSA 12207:

- SDLC явно задаёт **baseline‑точки и gate‑review’ы** по фазам (включая STRR/SFQR/SYRR и тестовые baselines)【104:0†SDLC\_12207\_Synthesis.md†L2-L7】【126:15†SDLC\_12207\_Synthesis.md†L15-L27】 — значит AJTBD надо встроить и в change/baseline‑дисциплину.
- ISO 12207 формально «подтягивает» AJTBD к требованиям через **traceability + baselining stakeholder needs/requirements + testability анализа**【110:11†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L4】【110:6†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L1-L5】.
- А INCOSE даёт «контрактные» минимальные атрибуты требований (A1/A3/A6/A8 и др.)【126:9†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L18】, которые AJTBD закрывает естественным образом.

---

Если хочешь, я могу следующим шагом (не задавая дополнительных вопросов) предложить **конкретный шаблон** для хранения “AJTBD → SRS/SRD requirement expression” (поля + правила именования + как организовать трассировку в репозитории), строго на базе списка INCOSE‑атрибутов и набора work‑products из SDLC\_12207\_Synthesis.


</agent>
<user>
приступай к следующему шагу

</user>
<agent>
Готово — «следующий шаг» сделал: собрал обновлённую карту, **где AJTBD “вшивается” в SDLC** не только как discovery, но как **сквозной источник rationale/traceability/критериев успеха** для требований, тестов и доков — с привязкой к:

- **INCOSE GtWR v4 (Summary Sheet)**: “needs & requirements” как общая нить жизненного цикла + требования как *statement + attributes*.【68:1†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】【68:1†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L34-L37】
- **SDLC\_12207\_Synthesis**: 12 фаз + гейты/базовые линии (SRR/SSR/PDR…; Functional Baseline/Allocated Baseline…).【68:2†SDLC\_12207\_Synthesis.md†L3-L26】【68:14†SDLC\_12207\_Synthesis.md†L15-L27】
- **CAN/CSA ISO/IEC/IEEE 12207-18**: процессы и типовые work products (requirements spec/change request, verification/validation procedures, operational procedures/user docs, problem report, maintenance requests и т.д.).【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

📄 Я оформил это отдельным документом:\
[Скачать AJTBD\_SDLC\_mapping\_v2.md](sandbox:/mnt/data/AJTBD_SDLC_mapping_v2.md)

---

## 1) Главный принцип стыка: AJTBD заполняет “почему” и “как проверяем”

INCOSE фиксирует, что needs/requirements связывают все артефакты SDLC, и предлагает мыслить **requirement expression = requirement statement + набор атрибутов** (rationale/traceability/успех V\&V и т.д.).【68:1†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】【68:1†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L34-L37】

AJTBD как раз производит “сырьё” для этих атрибутов:

- **Job graph** и контекст работ (что именно человек/роль пытается сделать),
- **evidence** (источник: интервью/наблюдение/данные),
- **outcomes** (что значит “успех”),
- **barriers** (почему не получается / ограничения).\
  И это хорошо совпадает с минимальным набором атрибутов требований у INCOSE (A1 Rationale, A3 Trace to Source, A6 Success Criteria, A8 Method и др.).【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L49-L76】

---

## 2) Точки соприкосновения AJTBD ↔ SDLC (самые “жёсткие стыки”)

### Точка A. Rationale + Traceability (почему требование существует)

- INCOSE требует минимум **A1 Rationale** и **A3 Trace to Source** (и вообще подчеркивает роль атрибутов).【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L49-L56】
- AJTBD даёт **job → evidence**, т.е. прямую “нитку” от требования к реальности.

Практический вывод: **job graph/evidence должны жить как конфигурационные элементы**, а не как “презентация” — иначе трассировка ломается на первой итерации.

---

### Точка B. V\&V (критерии успеха и метод проверки)

INCOSE делает V\&V частью атрибутной модели требований: **A6 Success Criteria, A7 Strategy, A8 Method**.【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L58-L64】

AJTBD “естественно” даёт:

- outcomes → **Success Criteria**
- барьеры → условия/ограничения проверки
- контекст/сегмент → **Condition of Use** (A12).【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L68-L69】

---

### Точка C. Сценарии, E2E тесты и структура пользовательской документации

В вашей старой версии анализа зафиксирована ключевая механика AJTBD:\
**“CJM с работами” = проекция job graph на временную ось** → это напрямую превращается в **сценарии**, **acceptance criteria**, **end‑to‑end тесты** и **структуру пользовательской документации**.【68:10†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】

Это важнейший “мост” от discovery к инженерке: из jobs получается не только “список хотелок”, а **сквозные потоки**, вокруг которых строится тестирование и docs.

---

### Точка D. Управление изменениями: “jobs стабильнее фич”

В старом анализе сформулирована полезная практика: **jobs чаще стабильнее фич, а реализации меняются быстрее** — это стоит отражать в требованиях через “стабильный job‑уровень” и “волатильную реализацию”.【68:16†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】\
INCOSE прямо имеет атрибут **Stability/Volatility (A26)**.【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L83-L84】

А в 12207-18 рядом лежит рабочий механизм: **Requirements Change Request** как типовой артефакт управления изменениями требований.【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

---

### Точка E. Эксплуатация и поддержка: AJTBD живёт после релиза

В 12207-18 отдельно выделены Operation/Maintenance артефакты: **Operational procedures (User documentation)**, **Problem Report**, **Customer Support Request**, **Maintenance Requests** и т.д.【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

Это означает: AJTBD не обязан “умирать” после discovery — job‑модель можно использовать для:

- классификации инцидентов (“какая работа ломается?”),
- приоритизации исправлений (какой job критичнее),
- проверки, “не уехали ли” требования от реального контекста.

---

## 3) Как AJTBD вписывается в ваш SDLC по 12 фазам и гейтам

В `SDLC_12207_Synthesis.md` цикл разложен на **12 фаз**【68:2†SDLC\_12207\_Synthesis.md†L3-L16】 и привязан к гейтам/базовым линиям.【68:2†SDLC\_12207\_Synthesis.md†L18-L26】【68:14†SDLC\_12207\_Synthesis.md†L15-L27】

Ниже — **где AJTBD реально “втыкается” в механизм**:

### 0) До формального SDLC: discovery / problem framing

Здесь создаёте:

- job graph (v0),
- segments/conditions,
- barriers,
- outcomes + критерии,
- evidence.

Это становится источником для A1/A3/A6/A8 (INCOSE‑атрибутов требований).【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L49-L64】

---

### 1) System Requirements Analysis → **System Requirements Review** → **Functional Baseline**

По мастер‑таблице: фаза 1 имеет gate **System Requirements Review** и baseline **Functional Baseline**.【68:2†SDLC\_12207\_Synthesis.md†L20-L23】

Что делает AJTBD здесь:

- job nodes → кандидаты в **capability requirements**,
- barriers/context → constraints/NFR,
- outcomes → success criteria + метод проверки.

---

### 3) Software Requirements Analysis → **Software Specification Review** → **Allocated Baseline**

Фаза 3: gate **Software Specification Review**, baseline **Allocated Baseline**.【68:2†SDLC\_12207\_Synthesis.md†L23-L25】

Ключевая практика из старого анализа:

- держать трассу **SRD requirement ↔ job node ↔ evidence**
- вести матрицу следов: **jobs → epics → requirements → tests → user docs**.【68:18†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L4】

---

### 4) Software Architectural Design → **Preliminary Design Review**

Критичный момент “встраивания в цикл”: на PDR (фаза 4) у вас ревьюятся не только архитектурные доки, но и:

- **UDD (Preliminary) Review**
- **TVPL (Soft‑Int) Review**【68:17†SDLC\_12207\_Synthesis.md†L6-L7】

То есть AJTBD должен приходить сюда **не “как исследование”, а как источник пользовательских потоков и тест‑планирования**:

- CJM/job graph → основные пользовательские потоки (сквозные сценарии),
- outcomes/barriers → структура тест‑кейсов, критерии, проверки на отказ/ограничения.

---

### 7–10) Интеграции и квалификационные тесты → тестовые baselines

В SDLC‑синтезе видны отдельные **Test Baseline** на софт‑интеграции и системной интеграции, а также “product baselines” на квалификациях.【68:14†SDLC\_12207\_Synthesis.md†L24-L27】

AJTBD‑роль здесь: обеспечить “job coverage” (чтобы ключевые работы были покрыты требованиями и тестами) и чтобы E2E сценарии были не случайными, а построенными по критической последовательности работ (проекция job graph на время).【68:10†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L1】

---

## 4) Как AJTBD вписывается в ISO 12207-18 как процессы и work products

`CAN_CSA_ISO_IEC_IEEE_12207-18.md` даёт список типовых артефактов по процессам: requirements/spec/change request; architecture views/models; design artifacts; verification/validation procedures/records/reports; operational procedures (user documentation); problem report; maintenance requests…【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

Прямое “переложение” AJTBD:

- **System/Software Requirements Definition**\
  job graph/outcomes/evidence → System/Software requirements + Specification; изменения jobs/outcomes → Requirements Change Request.【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

- **Architecture Definition**\
  job flows → Architecture Views/Models; барьеры → требования к наблюдаемости/безопасности/аудиту; интерфейсы → Interface Definition (initial).【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

- **Verification/Validation**\
  outcomes → процедуры проверки/валидации + записи/отчёты.【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

- **Operation/Maintenance**\
  job‑структура → operational procedures/user docs; деградация outcomes → problem report / support request; улучшения → maintenance requests.【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

---

## 5) Практический “шов” внедрения: чтобы AJTBD не жил параллельно SDLC

То, что я предлагаю как реально работающий seam:

1. **Job graph как supporting model для требований**\
   INCOSE прямо рекомендует: когда требование про сложное поведение — ссылаться на supporting diagram/model/ICD (это и есть job graph/CJM).【72:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】

2. **Требования писать solution‑free (где можно)**\
   INCOSE: избегать описания реализации, если нет причины “зажать” дизайн.【72:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L27-L29】

3. **Трассировка “jobs → req → tests → docs” как обязательный DoD**\
   Это уже сформулировано в старом анализе как практическая матрица следов.【68:18†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L4】

4. **Где проверять**

- На SRR/SSR проверять: есть A1/A3/A6/A8 (минимум).【68:4†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L49-L64】
- На PDR обязательно проверять, что UDD/TVPL строятся вокруг jobs (у вас это прямо в составе PDR‑ревью).【68:17†SDLC\_12207\_Synthesis.md†L6-L7】

---

## 6) Что я предлагаю сделать “следующим шагом” уже в процессе (очень прикладное)

Если вы хотите перейти от анализа к внедрению:

1. Выберите **1 подсистему/модуль** и зафиксируйте **job graph v0 + outcomes + evidence**.
2. Протяните минимальную трассу: **job node → SYS req → SW req → 3–5 E2E tests → разделы user docs**.【68:18†52fb98c1-0407-40fc-8363-8209708f456e.md†L1-L4】
3. Встройте чеклист “job coverage + INCOSE‑атрибуты” в **SRR/SSR/PDR** (у вас гейты уже есть в SDLC).【68:2†SDLC\_12207\_Synthesis.md†L20-L26】【68:17†SDLC\_12207\_Synthesis.md†L6-L7】
4. Пропишите правило изменений: **изменился job/outcome → Requirements Change Request → обновление требований/тестов/доков** (это прямо в канве 12207-18).【72:8†CAN\_CSA\_ISO\_IEC\_IEEE\_12207-18.md†L4-L6】

---

Если хочешь, я могу в следующем шаге **сделать конкретную “матрицу соответствия”** (AJTBD артефакты ↔ конкретные SDLC артефакты/records из вашей мастер‑таблицы: SYRER/SORER/SOAER/…; TVPL/TVRR; UDD стадии) и чеклисты для SRR/SSR/PDR — но уже без уточняющих вопросов возьму структуру из `SDLC_12207_Synthesis.md`.


</agent>
<user>
да, сделай матрицу соотвествия

</user>
<agent>
Ниже — **матрица соответствия AJTBD ↔ SDLC** (скелет SDLC взят из 12‑фазной схемы IEEE 12207 в вашем `SDLC_12207_Synthesis.md`, а “как AJTBD встраивается по фазам” — из `52fb98c1-...md`).【53:12†SDLC\_12207\_Synthesis.md†L3-L16】【53:3†52fb98c1-0407-40fc-8363-8209708f456e.md†L5-L41】

Ключевой принцип INCOSE: **needs/requirements — “нить”, связывающая все артефакты жизненного цикла**, и удобно мыслить требования как *statement + набор атрибутов* (rationale/traceability/V\&V и т.д.).【53:7†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】【53:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L47】

---

## Матрица соответствия AJTBD ↔ SDLC по фазам IEEE 12207

> Справочно: *work products* по фазам (SRS/SARAD/SRD/SAD/SDD/TVPL/TVPR/TVRR/UDD/… ) — из `SDLC_12207_Synthesis.md`.【53:15†SDLC\_12207\_Synthesis.md†L5-L10】【49:10†SDLC\_12207\_Synthesis.md†L1-L10】【49:12†SDLC\_12207\_Synthesis.md†L5-L6】

| SDLC фаза                                                  | Основные SDLC‑артефакты (work products)                                                                                              | Что берём из AJTBD                                                                                                            | Как “переводится” в SDLC‑артефакты (что конкретно фиксировать)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0. Discovery / Problem framing** *(до формального SDLC)* | **AJTBD knowledge base**: research notes/evidence, job graph v0, outcomes                                                            | Уточняем: **граф работ**, **сегменты/контексты**, **барьеры**, **альтернативы**, **критерии успеха (outcomes)**, **evidence** | Это становится “Source of Truth” для **Trace to Source** и **Rationale** в требованиях (SRS/SRD), и дальше живёт как база для трассировки.【53:3†52fb98c1-0407-40fc-8363-8209708f456e.md†L9-L22】                                                                                                                                                                                                                                                                                                                                                              |
| **1. System Requirements Analysis**                        | **SRS**【53:15†SDLC\_12207\_Synthesis.md†L5-L10】                                                                                      | Узлы/под‑работы графа + барьеры/контекст + outcomes                                                                           | Узлы графа → кандидаты в **system capability requirements**; барьеры/контекст → **constraints / quality requirements**; outcomes → **acceptance criteria** и **методы V\&V**. Минимум атрибутов требования (INCOSE): **A1 Rationale, A3 Trace to Source, A6 Success Criteria, A8 Method (+ owner/priority/stability)**【53:3†52fb98c1-0407-40fc-8363-8209708f456e.md†L25-L41】【53:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L18】【53:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L26-L47】                                                                  |
| **2. System Architectural Design**                         | **SARAD**【53:15†SDLC\_12207\_Synthesis.md†L8-L10】                                                                                    | Граф работ + критическая последовательность + барьеры                                                                         | Граф работ помогает решить **что автоматизируем/что остаётся вручную/где интеграции**; критическая последовательность → **сквозные system scenarios**; барьеры → **арх. решения** (наблюдаемость, аудит, откаты, целостность, безопасность и т.д.).【53:3†52fb98c1-0407-40fc-8363-8209708f456e.md†L45-L53】                                                                                                                                                                                                                                                    |
| **3. Software Requirements Analysis**                      | **SRD**【53:15†SDLC\_12207\_Synthesis.md†L8-L10】                                                                                      | Системные требования “про job” + job nodes + evidence                                                                         | Декомпозиция “job‑требований” в **software requirements** (поведение/данные/интерфейсы) **с сохранением трассировки**: `SRD requirement ↔ job node ↔ evidence`. Практика: **“матрица следов”** `jobs → epics → requirements → tests → user docs` (чтобы traceability была механической, а не “на словах”).【53:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L23-L35】                                                                                                                                                                                             |
| **4. Software Architectural Design**                       | **SAD + SIDD/DDD (Top-Level) + UDD (Preliminary) + TVPL (Soft‑Int)**【49:10†SDLC\_12207\_Synthesis.md†L2-L4】                          | **Job graph + CJM** (проекция графа на время) + барьеры                                                                       | Здесь важно “раннее начало” доков и тест‑планирования: уже в этой фазе появляются **UDD (Preliminary)** и **TVPL (Soft‑Int)**.【49:10†SDLC\_12207\_Synthesis.md†L2-L4】【53:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L38-L52】<br>Как встраивается: job graph/CJM → **основные пользовательские потоки** (на них архитектура обязана быть устойчивой); барьеры → требования к устойчивости/наблюдаемости/UX‑ограничениям; ранний TVPL: сценарии как **“прохождение ключевых работ” + проверки барьеров**.【53:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L38-L52】 |
| **5. Software Detailed Design**                            | **SDD + SIDD/DDD (Detailed) + UDD (Update) + TVPL (Soft‑Unit) + TVPL (Soft‑Int‑Update)**【49:10†SDLC\_12207\_Synthesis.md†L4-L5】      | AJTBD уже не ведущий, но “контроль смысла”                                                                                    | AJTBD используется как проверка: не потеряли ли **rationale**, сохраняется ли **критерий успеха**, не “втащили” ли implementation‑детали туда, где они не обязаны быть (INCOSE отдельно подчёркивает *solution‑free*).【57:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L25-L34】                                                                                                                                                                                                                                                                                 |
| **6. Software Coding and Testing**                         | **Software Unit/Database + TVPR/TVRR (Soft/DB‑Unit) + UDD (Update) + TVPL (Soft‑Int‑Update)**【49:10†SDLC\_12207\_Synthesis.md†L5-L6】 | Outcomes + приоритизация jobs                                                                                                 | AJTBD проявляется через **acceptance criteria**, основанные на outcomes, и приоритизацию (сначала то, что улучшает выполнение ключевых jobs).【57:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L37-L43】                                                                                                                                                                                                                                                                                                                                                          |
| **7. Software Integration**                                | **SOIP + TVRR (Soft‑Int) + UDD (Update) + TVPR (Soft‑Qual)**【49:10†SDLC\_12207\_Synthesis.md†L6-L7】                                  | Критическая последовательность работ + привязка требований к job‑узлам                                                        | Интеграционные/E2E‑проверки строятся как проекция **критической последовательности**; плюс проще доказать покрытие: требования привязаны к job‑узлам → легче обеспечить покрытие по работам.【57:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L46-L54】                                                                                                                                                                                                                                                                                                           |
| **8. Software Qualification Testing**                      | **TVRR (Soft‑Qual) + UDD (Update) + SIAR (Soft‑Qual‑FCA/PCA)**【49:10†SDLC\_12207\_Synthesis.md†L7-L8】                                | Те же job‑узлы/сценарии, но как “доказательство соответствия требованиям”                                                     | В квалификационных тестах логика та же: тест‑кейсы/процедуры основаны на требованиях к ПО; AJTBD‑привязка к job‑узлам помогает держать покрытие и не терять “почему это проверяем”.【57:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L46-L54】                                                                                                                                                                                                                                                                                                                    |
| **9. System Integration**                                  | **TVRR (Sys‑Int) + TVPR (Sys‑Qual)**【49:10†SDLC\_12207\_Synthesis.md†L8-L9】                                                          | Сквозные job‑сценарии (end‑to‑end)                                                                                            | Переносим “хребет” сценариев на уровень системы: E2E тесты = критическая последовательность работ (проекция графа).【57:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L46-L54】                                                                                                                                                                                                                                                                                                                                                                                    |
| **10. System Qualification Testing**                       | **TVRR (Sys‑Qual) + SIAR (Sys‑Qual‑FCA/PCA)**【49:10†SDLC\_12207\_Synthesis.md†L9-L10】                                                | Outcomes и условия выполнения работы                                                                                          | Закрываем соответствие “система удовлетворяет intent”: проверяем outcomes/критерии успеха на системном уровне (через V\&V методы, заданные в требованиях). Логика “requirements thread” по INCOSE как раз про то, что дальше артефакты проверяются против design input requirements.【53:7†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L3-L5】                                                                                                                                                                                                                   |
| **11. Software Installation**                              | **SIP**【49:10†SDLC\_12207\_Synthesis.md†L10-L10】                                                                                     | Контексты/барьеры и “job‑to‑guide” логика                                                                                     | Инсталляция/ввод в эксплуатацию не должны ломать ключевые jobs: требования/инструкции/ограничения подсказываются контекстами и барьерами. *(AJTBD “подпитывает” и инсталляционные сценарии, и доки.)*【57:10†52fb98c1-0407-40fc-8363-8209708f456e.md†L25-L33】                                                                                                                                                                                                                                                                                                 |
| **12. Software Acceptance Support**                        | **TVRR (Soft‑Acc) + Software Training**【49:12†SDLC\_12207\_Synthesis.md†L5-L6】                                                       | Язык работ/прогресса + барьеры/риски/ошибки                                                                                   | **Структура документации/обучения = “как выполнить работу” (job‑to‑guide)**; акценты = барьеры/риски/ошибки; язык = язык работ и прогресса (понятный пользователю).【57:10†52fb98c1-0407-40fc-8363-8209708f456e.md†L25-L33】                                                                                                                                                                                                                                                                                                                                   |

---

## Мини‑шаблон “сквозной матрицы следов” (то, что вы просили как матрицу соответствия на уровне трассировки)

В вашем анализе прямо предлагается делать **матрицу следов** `jobs → epics → requirements → tests → user docs`.【53:0†52fb98c1-0407-40fc-8363-8209708f456e.md†L33-L35】

Ниже — удобный формат (минимальный, но уже “механически трассируемый”):

| AJTBD job node | Evidence (Trace to Source) | Epic/Feature | SRS ReqID   | SRD ReqID  | Test (TVPL/TVPR) | Result (TVRR/SIAR) | UDD section |
| -------------- | -------------------------- | ------------ | ----------- | ---------- | ---------------- | ------------------ | ----------- |
| JOB‑…          | link…                      | EPIC‑…       | SYS‑JOB‑### | SW‑JOB‑### | …                | …                  | …           |

А чтобы требования были “INCOSE‑совместимыми”, можно прямо использовать предложенный в документе шаблон **requirement expression** (ReqID/Statement/Rationale/Trace/Condition/Success criteria/Method/Stability/Priority).【57:11†52fb98c1-0407-40fc-8363-8209708f456e.md†L25-L33】【53:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L7-L18】【53:6†incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf†L26-L47】

---

Если хочешь, следующим шагом могу:

- превратить эту матрицу в **Excel‑шаблон** (с выпадающими списками артефактов SDLC, полями INCOSE‑атрибутов и колонками для авто‑проверок “есть ли trace/success criteria/method”),
- или собрать **RACI / process‑шов** по ревью (куда именно вставить testability review и на каких гейтах SDLC).
</agent>
