# I01-F0004-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0004-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md)

## Source

- chat_id: `I01-F0004-CHATGPT`
- source_path: `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил найти неочевидные, потенциально важные связи в документации, которые прямо не сформулированы (`raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:4`).
2. Фокус запроса: скрытые инсайты на пересечении подходов, а не пересказ явных положений (`C01`, `C02`, `C03`).

## AI Response Summary

1. AI предложил мета-фреймворк из трех слоев: AJTBD (ценность и мотивация), W-Model (ранний и непрерывный контроль качества), ISO 12207 (процессный инженерный каркас) (`C01`).
2. AI вывел четыре прикладных механизма: автогенерация ранних тестов из графа работ, переопределение validation через экономику найма/увольнения решения, value-driven архитектура по оси стабильность/волатильность, и приоритизация дефектов по job friction (`C02`-`C05`).
3. Итоговая линия ответа: полная трассируемость от пользовательского триггера до коммита/тест-кейса (`C06`).

## Extracted Concepts

### C01. Трехслойный мета-фреймворк AJTBD + W-Model + ISO 12207

- Concept: Эти подходы трактуются как единая система: AJTBD формализует ценность, W-Model задает непрерывный quality-loop, ISO 12207 обеспечивает процессный backbone.
- Why it matters: Дает интеграционную рамку для управления SDLC сквозь продукт, качество и инженерные процессы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:31`

### C02. AJTBD-граф как вход для раннего тест-дизайна (left shift)

- Concept: Граф работ AJTBD может быть преобразован в машиночитаемый источник для тестовой базовой линии и acceptance criteria еще до кода.
- Why it matters: Уменьшает неоднозначность ранних требований и усиливает левый сдвиг тестирования по W-Model.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:14`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:16`

### C03. Validation через метрику «увольнения старого решения»

- Concept: Валидация измеряется не субъективной «нравится/не нравится», а фактом, что новое решение снижает трение и вытесняет прежний способ выполнения задачи.
- Why it matters: Делает acceptance testing сравнимым и экономически интерпретируемым.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:19`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:20`

### C04. Value-Driven Architecture по оси «стабильность/волатильность»

- Concept: Стабильные «работы» AJTBD должны определять ядро архитектуры, а волатильные UI-решения выноситься в заменяемые оболочки.
- Why it matters: Снижает технический долг и повышает адаптивность при продуктовых пивотах.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:23`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:24`

### C05. Дефектный триаж через Job Friction

- Concept: Приоритет багов и изменений рассчитывается по ущербу критическому пути пользовательской работы, а не только по технической тяжести.
- Why it matters: Сдвигает управление изменениями в сторону защиты пользовательской ценности и конкурентоспособности.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:27`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:28`

### C06. Сквозная трассируемость «триггер -> коммит -> тест-кейс»

- Concept: Совместное применение AJTBD, W-Model и ISO 12207 формирует прозрачную цепочку от мотивации пользователя до инженерных артефактов.
- Why it matters: Это операционное основание для управляемого AI-driven SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0004-CHATGPT.md:31`

## Unresolved Ambiguities

1. В тексте присутствуют ссылки-маркеры в виде двойных обратных кавычек без явных source anchors; часть утверждений опирается на подразумеваемые внешние материалы.
2. Инсайты сформулированы как синтез/гипотезы и требуют эмпирической валидации на проектных данных перед нормализацией в обязательные процессные правила.
