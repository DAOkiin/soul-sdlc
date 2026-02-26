# I01-F0001-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0001-CHATGPT`
- source_path: `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил аудит файла `SDLC_12207_Synthesis.md` по официальному документу стандарта (`raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:4`).
2. Пользователь подтвердил запуск проверки (`raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:16`).
3. Ключевой фокус пользовательских запросов: верификация соответствия SDLC нормативной модели (`C01`, `C03`, `C04`).

## AI Response Summary

1. AI зафиксировал эталон проверки: ISO/IEC/IEEE 12207:2017 и канадскую адаптацию CAN/CSA (`C01`).
2. AI описал метод проверки через PRM и полное покрытие outcomes, а не через фиксированную модель разработки (`C03`).
3. AI развернул контрольную архитектуру по 30 процессам и 4 группам, с акцентом на обязательность нетехнических групп (`C04`, `C05`).
4. AI подчеркнул итеративно-рекурсивный характер технических процессов и совместимость с Agile/DevOps при сохранении требований стандарта (`C06`, `C07`).

## Extracted Concepts

### C01. Нормативный эталон проверки

- Concept: Верификация строится на ISO/IEC/IEEE 12207:2017 и идентичной канадской адаптации CAN/CSA-ISO/IEC/IEEE 12207:18.
- Why it matters: Это задает версию стандарта и исключает смешение с устаревшими редакциями.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:551`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:557`

### C02. Эволюционный сдвиг 2008 -> 2017

- Concept: Редакция 2017 гармонизирована с ISO/IEC/IEEE 15288; количество процессов уменьшено с 43 до 30, программно-специфичные процессы интегрированы в общие инженерные.
- Why it matters: Это главный маркер, по которому выявляется устаревшая структура SDLC в проверяемом документе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:557`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:559`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:563`

### C03. PRM и проверка по outcomes

- Concept: ISO 12207 задает Process Reference Model, не навязывает конкретный SDLC-паттерн и требует полного соответствия ожидаемым результатам процессов.
- Why it matters: Проверка должна оценивать достижение требуемых outcomes, даже если команда использует Scrum/Agile.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:567`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:569`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:573`

### C04. Полная процессная архитектура (30 процессов, 4 группы)

- Concept: Эталонная проверка должна покрывать все 30 процессов в 4 группах: Agreement, Organizational Project-Enabling, Technical Management, Technical.
- Why it matters: Частичное покрытие (только техпроцессы) не дает нормативного соответствия.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:577`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:601`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:616`

### C05. Критичность нетехнических групп процессов

- Concept: Пропуск Agreement и Organizational Project-Enabling процессов трактуется как критичная ошибка соответствия.
- Why it matters: SDLC-документ должен отражать не только код/тесты, но и контрактно-организационный контур.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:581`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:661`

### C06. Не-каскадная интерпретация техпроцессов

- Concept: Технические процессы в ISO 12207:2017 выполняются конкурентно, итеративно и рекурсивно, а не как жесткий Waterfall.
- Why it matters: Это определяет корректную методологическую интерпретацию SDLC_синтеза.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:618`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:652`

### C07. Сквозная трассируемость и совместимость Agile/DevOps

- Concept: Трассируемость задается как сквозной результат между требованиями, архитектурой, кодом и верификацией; Agile/DevOps совместимы со стандартом, если обеспечивают требуемые outcomes и управленческие контуры.
- Why it matters: Концепт связывает инженерную гибкость процесса и нормативную управляемость результата.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:648`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:650`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0001-CHATGPT.md:652`

## Unresolved Ambiguities

1. Блок `<agent-thoughs>` содержит большое число повторяющихся промежуточных формулировок; для дистилляции опорным принят итоговый структурированный отчет (раздел после `:547`).
2. Ссылки на внешние источники перечислены, но исходные PDF/стандарты не приложены в репозитории; полнота факт-чекинга по первоисточнику ограничена содержимым самого чата.
