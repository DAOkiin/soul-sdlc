# I01-F0005-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0005-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md)

## Source

- chat_id: `I01-F0005-CHATGPT`
- source_path: `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил выявить неконсистентности в документации по AJTBD, W-Model и ISO 12207 (`raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:4`).
2. Пользователь уточнил целевой контекст: автономная самоулучшающаяся система, которая строит другие системы (`raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:48`).
3. Пользователь предложил архитектурную гипотезу про "душу" системы в репозитории, семантический слой ограничений и ядро на модели Болдачева (`raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:86`, `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:87`).

## AI Response Summary

1. AI выделил 5 ключевых неконсистентностей: фазовость vs процессность, поздний старт тестов vs W-model shift-left, пропуск stakeholder layer, тестирование vs отладка, риск устаревших интерпретаций (`C01`-`C05`).
2. AI предложил переход к графовой механике SDLC: асинхронные воркеры, триггеры от артефактов, debt flags и PR-циклы (`C06`).
3. AI дал правило двухслойной трассируемости Intent -> System Requirements и роль семантического enforcement (`C07`).
4. AI поддержал идею "души" и оформил ее через event graph, actors, permissions, causes и строгий semantic compiler перед записью событий в DAG (`C08`).

## Extracted Concepts

### C01. Неконсистентность "12 фаз" против процессной архитектуры ISO 12207:2017

- Concept: Жесткая 12-фазная интерпретация конфликтует с принципом ISO 12207:2017, где стандарт не предписывает единую фазовую модель и допускает итеративно-рекурсивное выполнение процессов.
- Why it matters: Это базовое методологическое расхождение, влияющее на весь дизайн SDLC.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:17`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:19`

### C02. Неконсистентность в сроках старта тестирования

- Concept: План тестирования на фазе архитектуры противоречит W-model, где тестовые артефакты должны формироваться с первого дня на уровне требований.
- Why it matters: Снижает качество раннего feedback loop и подрывает shift-left.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:23`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:25`

### C03. Пропуск слоя Stakeholder Needs перед System Requirements

- Concept: Прямой маппинг AJTBD-инсайтов в SRS/SRD перескакивает обязательный этап формализации нужд стейкхолдеров.
- Why it matters: Нарушает нормативную последовательность трансформации требований в ISO 12207:2017.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:29`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:31`

### C04. Терминологический разрыв Testing vs Debugging

- Concept: W-model жестко разводит тестирование и отладку, тогда как в ISO 12207 это распределено по verification/problem resolution/maintenance, а отдельного процесса debugging нет.
- Why it matters: Некорректное смешение ролей ломает ответственность и поток исправлений.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:37`

### C05. Риск методологической регрессии к устаревшим интерпретациям

- Concept: Использование каскадно-фазовой стыковки AJTBD-SDLC создает конфликт с современным гибким процессным ядром 12207:2017.
- Why it matters: Повышает риск проектировать автономную систему на неактуальном каркасе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:40`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:42`

### C06. Для автономности нужен event/state graph вместо линейных фаз

- Concept: Агентная SDLC-система должна работать как онтологический граф с триггерами от изменений артефактов, асинхронными операторами и автоматическим debt-flag orchestration.
- Why it matters: Это операционная модель, совместимая с автономными PR-циклами и непрерывной эволюцией.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:60`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:61`

### C07. Обязательное разделение Intent и System Requirements

- Concept: Требуется двухслойная структура: Layer 1 (Stakeholder Needs/Intent) и Layer 2 (System Requirements) с жесткой trace-back связью и mechanical enforcement консистентности.
- Why it matters: Блокирует галлюцинаторный переход от эмоций/барьеров сразу в технический дизайн.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:62`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:65`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:67`

### C08. "Душа" как event graph + семантический компилятор ограничений

- Concept: Идентичность системы хранится в файлах как система правил; агенты выступают акторами событий, а семантический слой валидирует permissions/causes и допускает изменения только после строгой проверки инвариантов.
- Why it matters: Это формализует безопасное сосуществование вероятностных LLM-агентов и детерминированного ядра.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:99`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:103`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:111`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0005-CHATGPT.md:116`

## Unresolved Ambiguities

1. "Модель Болдачева/Boldsea" упоминается концептуально, но нормативный/технический первоисточник модели в этом чате не приложен.
2. Ряд рекомендаций описан как архитектурные эвристики; для перевода в жесткие правила SDLC нужны формальные схемы данных и валидаторы.
