# I01-F0006-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0006-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md)

## Source

- chat_id: `I01-F0006-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил объяснение `North Star` в контексте документации глобального видения технического проекта (`raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:4`).
2. Затем пользователь попросил помочь определить North Star непосредственно из `global_vision.md` (`raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:55`).

## AI Response Summary

1. AI развел два смысла North Star: стратегический вектор (statement) и операциональная главная метрика (NSM) (`C01`).
2. AI предложил шаблон `North Star + NSM + input metrics + guardrails + decision rule` и связал North Star с OKR (`C02`, `C03`).
3. На основе `global_vision.md` AI вывел knowledge-centric North Star: проверяемое, типизированное, версионируемое знание и разграничение claim/fact (`C04`, `C05`).
4. Для измерения предложен главный кандидат NSM `Traceable Verified Output Rate` с supporting-метриками и guardrails (`C06`, `C07`).

## Extracted Concepts

### C01. Два корректных значения North Star

- Concept: North Star может означать либо устойчивое направление проекта (statement), либо единственную главную метрику ценности (NSM).
- Why it matters: Позволяет избежать смешения уровня смысла ("зачем") и уровня измерения ("чем мерим прогресс").
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:25`

### C02. NSM должен быть обрамлен деревом метрик и guardrails

- Concept: Для техпроекта одной NSM недостаточно; необходимы input metrics и защитные ограничения (качество/надежность/стоимость), иначе возникает gaming.
- Why it matters: Стабилизирует поведение системы и предотвращает локальную оптимизацию одной цифры.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:32`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:34`

### C03. Связка North Star и OKR

- Concept: North Star остается относительно стабильным ориентиром, а OKR выступают периодическими измеримыми шагами, выровненными с этим ориентиром.
- Why it matters: Формирует каскад управления от стратегии к тактическим целям.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:38`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:39`

### C04. Knowledge-first ось глобального видения

- Concept: Центральная идея vision: raw text/векторная похожесть не равны истинности; нужен семантический слой и независимость знания от LLM.
- Why it matters: Задает архитектурный приоритет в сторону проверяемого knowledge layer.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:67`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:68`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:69`

### C05. Claim vs Fact как управленческий инвариант

- Concept: Факт трактуется как verified claim; требуются provenance-атрибуты (источник, время, метод, confidence), конфликты и версии.
- Why it matters: Это основа трассируемости, аудита и безопасных агентных действий.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:70`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:71`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:83`

### C06. Рекомендуемый NSM: Traceable Verified Output Rate

- Concept: Главная метрика — доля ответов/действий, где существенные факты подтверждены verified claims и имеют source/time/version.
- Why it matters: Меряет конечную полезность системы как доверенной базы для решений людей и агентов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:109`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:111`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:129`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:144`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:145`

### C07. Практический metric stack для knowledge-платформы

- Concept: Для операционализации North Star нужен полный блок: leading indicators (метаданные claims, normalisation rate, claim->fact cycle time, conflict resolution) и guardrails (false verification, latency, cost, unsupported assertions).
- Why it matters: Делает North Star измеримым без "самообмана" и поддерживает управляемую эволюцию системы.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:147`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:152`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:154`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0006-CHATGPT.md:158`

## Unresolved Ambiguities

1. В первом ответе есть внутренние ссылки-цитаты (`turnXviewY`) без раскрытия в этом файле, поэтому проверка внешних источников требует исходного окружения чата.
2. `global_vision.md` не приведен дословно в источнике; выводы по North Star опираются на пересказ осевых тезисов внутри ответа агента.
