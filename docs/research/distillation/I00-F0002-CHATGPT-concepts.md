# I00-F0002-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0002-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md)

## Source

- chat_id: `I00-F0002-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил собрать и кратко описать use-cases проекта из накопленного контекста, чтобы уместить ёмкую идею в компактный документ (`raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:4`).

## AI Response Summary

1. Агент явно зафиксировал ограничение контекста (видно только текущее сообщение) и предложил компенсирующий workflow: шаблон + черновой каталог кейсов + последующая доуточняющая итерация (`C01`, `C05`).
2. Даны практические артефакты: карточка use-case, универсальная таксономия кейсов по 6 блокам и схема приоритизации P0/P1/P2 (`C02`, `C03`, `C04`).
3. Ответ ориентирован на быстрый merge идей в системный список без дублей и “воды” (`C04`, `C05`).

## Extracted Concepts

### C01. Use-case extraction can start with a constrained-context bootstrap

- Concept: Даже без полного доступа к истории чатов можно начать с структурного шаблона и универсального каталога, затем уточнить на пользовательских заметках.
- Why it matters: Сохраняет скорость работы при неполном контексте и снижает блокировку процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:12`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:13`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:15`

### C02. Standardized use-case cards improve compressibility of complex project descriptions

- Concept: Кейсы оформляются короткими карточками (роль, действие, вход/выход, ценность), чтобы из них быстро собирать короткий project pitch.
- Why it matters: Даёт единый формат и убирает неоднородность формулировок.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:19`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:23`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:28`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:35`

### C03. Use-case taxonomy should cover full pipeline lifecycle, not only parsing core

- Concept: Каталог кейсов включает ingestion, core parsing, quality/HITL, output integrations, ops, and one-click product scenarios.
- Why it matters: Предотвращает перекос в сторону только обработки данных и фиксирует эксплуатационный слой.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:43`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:50`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:58`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:65`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:72`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:79`

### C04. Priority layering P0/P1/P2 is the minimal mechanism for scope control

- Concept: Быстрое разделение кейсов на core/booster/later позволяет зафиксировать MVP без потери расширяемости.
- Why it matters: Удерживает фокус команды и снижает риск scope creep на ранней стадии.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:91`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:92`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:93`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:95`

### C05. Final precision requires ingestion of raw user notes to remove guessing

- Concept: Для точного списка кейсов агенту нужен исходный материал пользователя (черновик, функции, буллеты), после чего делается dedup + normalization.
- Why it matters: Обеспечивает трассируемость кейсов к реальным задачам, а не к универсальному шаблону.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:104`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:106`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:114`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0002-CHATGPT.md:116`

## Unresolved Ambiguities

1. Не выбран доменно-специфичный набор P0 use-cases; предложен только универсальный каркас.
2. Не определены роли пользователей/агентов для финального сценарного каталога.
3. Не зафиксированы критерии “уникальности” кейсов при дедупликации.
