# I01-F0002-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0002-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md)

## Source

- chat_id: `I01-F0002-CHATGPT`
- source_path: `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил синтез одного большого markdown-документа по SDLC из набора разнотипных источников без искажения смысла и с объединением пересекающихся знаний (`raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:4`).
2. Пользователь задал структурированный план: словарь терминов, сравнение версий стандартов (1995 vs 2017), извлечение таблиц артефактов/оценок, описание моделей ЖЦ, практический кейс и проектирование диаграмм Mermaid (`raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:8`, `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:16`).
3. Приоритет пользовательского запроса: одновременно полнота, точность и наглядная форма (таблицы + диаграммы) (`C03`, `C04`, `C06`).

## AI Response Summary

1. AI собрал единую теоретическую рамку: объектное представление (customer/project/product/process/resource) и историческая эволюция ISO 12207 (`C01`, `C02`).
2. AI выделил современную нормативную архитектуру: 30 процессов в 4 группах с акцентом на гармонизацию системной и программной инженерии (`C02`).
3. AI добавил микроуровень исполнения: 12 фаз, 35 артефактов, систему оценок/аудитов/baselines и связь с управлением изменениями (`C03`).
4. AI включил выбор моделей ЖЦ (waterfall/incremental/evolutionary), tailoring и правила качества требований (INCOSE) (`C04`, `C05`).
5. AI связал стандартную модель с эксплуатацией через трехуровневую техподдержку L1/L2/L3 в практическом кейсе (`C06`).

## Extracted Concepts

### C01. Object View как базовая рамка SDLC

- Concept: Программная инженерия описывается через 5 сущностей (Customer, Project, Product, Process, Resource), где процесс трансформирует ресурсы в продукт.
- Why it matters: Дает не список активностей, а системную модель взаимодействий и ответственности.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1184`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1197`

### C02. Гармонизация ISO 12207:2017 с системной инженерией

- Concept: Переход к версии 2017 трактуется как интеграция с 15288 и новая структура из 4 групп процессов; программные задачи встроены в общесистемный контур.
- Why it matters: Это критерий актуальности синтеза и фильтр устаревших представлений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1221`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1224`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1231`

### C03. Микроархитектура исполнения: 12 фаз и артефактный контур

- Concept: SDLC представлен как 12 фаз с 35 продуктами, 62 оценками, 17 записями, 4 аудитами и 9 baseline.
- Why it matters: Формирует операционный слой контроля качества и трассируемости, а не только концептуальный уровень.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1237`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1242`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1263`

### C04. Модели жизненного цикла как выбираемая стратегия

- Concept: Стандарт не диктует одну модель; выделяются waterfall, incremental, evolutionary с разным рисковым профилем.
- Why it matters: Позволяет обосновывать выбор модели по контексту проекта, а не применять шаблонно.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1274`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1278`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1281`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1283`

### C05. Tailoring и инженерная дисциплина формулирования требований

- Concept: Необходим формальный tailoring; качество требований задается проверяемыми характеристиками и строгими лингвистическими правилами (INCOSE).
- Why it matters: Без этого возникает uncontrolled tailoring, двусмысленность требований и рост дефектов на поздних этапах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1287`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1290`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1296`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1301`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1307`

### C06. Связка SDLC и эксплуатации через ITSM L1/L2/L3

- Concept: Практический контур эксплуатации связывает сопровождение стандарта с трехуровневой моделью поддержки (L1/L2/L3) и эскалацией инцидентов.
- Why it matters: Показывает перенос нормативной модели в реальную операционную практику.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1348`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1351`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1353`

### C07. Терминологическая локализация как часть качества синтеза

- Concept: Для кросс-язычной среды критична точная локализация терминов (`process/activity/task/firmware`) и модальности (`shall/will/should/may`).
- Why it matters: Снижает риск смысловых и контрактных ошибок в русско-английской документации SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1363`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1365`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1369`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0002-CHATGPT.md:1374`

## Unresolved Ambiguities

1. В источнике большой объем повторяющихся промежуточных блоков размышлений; опорным слоем для концептов приняты структурированные секции итогового отчета.
2. Часть ссылок в `Works Cited` и `Sources Read` ведет на агрегаторы/прокси (Google contribution links), что осложняет независимую проверку первоисточников вне контекста исходной сессии.
