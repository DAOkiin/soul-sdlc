# I01-F0003-CHATGPT Concepts (Draft)

## Source

- chat_id: `I01-F0003-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь поставил задачу проверить `SDLC_12207_Synthesis.md` по документу стандарта.
2. [request] [U02] Фокус запроса: верификация корректности синтеза относительно актуальной нормативной базы (`C01`, `C02`).

## AI Response Summary

1. [proposal] [A01] AI дал общий вывод о высокой корректности синтеза и отсутствии критических противоречий с 12207:2017.
2. [proposal] [A02] AI проверил совпадение по структуре процесса: 4 группы, 30 процессов, иерархия process/activity/task, ненормативность фиксированной фазовой модели.
3. [proposal] [A03] AI разделил strict conformance и полезные расширения синтеза (исторические сравнения, baseline-термины, L1/L2/L3, 12-фазная схема), отмечая что они практические, а не обязательные нормы стандарта.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:4`
- U02: `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:1`
- A01: `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:10`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:12`
- A02: `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:18`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:19`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:20`
- A03: `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:21`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:30`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:32`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:33`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:34`, `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:35`

## Extracted Concepts

### C01. Итог верификации: соответствие без критичных расхождений

- Concept: Проверяемый `SDLC_12207_Synthesis.md` признан корректным относительно CAN/CSA-ISO/IEC/IEEE 12207:2017.
- Why it matters: Фиксирует базовый статус источника как пригодного для дальнейшей дистилляции.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:12`

### C02. Строгое ядро соответствия: 4 группы, 30 процессов, P-A-T

- Concept: Верифицировано совпадение по четырем группам процессов, полному списку 30 процессов и декомпозиции Process -> Activity -> Task.
- Why it matters: Это структурный каркас стандарта, на котором строится корректная процессная карта SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:19`

### C03. Стандарт процессный, не фазово-директивный

- Concept: ISO/IEC 12207 определяет набор процессов и не предписывает единственную модель жизненного цикла или строгий порядок выполнения.
- Why it matters: Допускает адаптацию под контекст проекта, сохраняя нормативные outcomes.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:20`

### C04. Гармонизация с системной инженерией как критерий современности

- Concept: Синтез корректно отражает сближение 12207:2017 с 15288 и усиление системного контекста.
- Why it matters: Помогает отсекать устаревшие, изолированные программные трактовки SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:21`

### C05. Граница между нормативом и практическими дополнениями

- Concept: Историческое сравнение с 1995, детализация baseline-терминов, L1/L2/L3 и 12-фазная архитектура полезны, но не являются обязательными требованиями стандарта 2017.
- Why it matters: Разводит обязательное соответствие и расширяющие практические интерпретации.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:32`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:33`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:35`

### C06. Терминологическая корректность ключевых ролей и V&V

- Concept: Подтверждена корректность трактовок Acquirer/Supplier и различения Verification vs Validation.
- Why it matters: Эти определения критичны для требований, контрактов и приемки результата.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:25`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0003-CHATGPT.md:26`

## Unresolved Ambiguities

1. В источнике отсутствуют прямые цитаты из самого текста стандарта, приведены только пересказ и ссылки на пункты; факт-чекинг зависит от точности пересказа в данном чате.
2. Ссылка на проверяемый `CAN_CSA_ISO_IEC_IEEE_12207-18.md` присутствует как упоминание, но сам файл не приведен в теле этого источника.
