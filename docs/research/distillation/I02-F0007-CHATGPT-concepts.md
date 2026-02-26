# I02-F0007-CHATGPT Concepts (Draft)

## Source

- chat_id: `I02-F0007-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. [request] [U01] Пользователь попросил проверить консистентность документации в связке W-model + SDLC + AJTBD и валидность рассуждений/выводов.

## AI Response Summary

1. [proposal] [A01] Агент подтвердил логическую совместимость базовых тезисов (AJTBD определения, ранний старт UDD/TVPL, shift-left и traceability) с SDLC/W-model/12207.
2. [risk] [A02] Найдены точечные несостыковки: источник тезиса про CJM, неединый минимум INCOSE-атрибутов (A7), риск смешения viewpoint и стандарта, терминологические разрывы.
3. [proposal] [A03] Финальный вывод: методология в целом корректна, требуется набор небольших правок формулировок и crosswalk между лексиконами гейтов.

## Summary Evidence Map

- U01: `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:4`
- A01: `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:18`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:19`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:21`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:22`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:26`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:28`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:30`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:36`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:37`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:39`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:40`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:46`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:50`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:51`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:53`
- A02: `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:65`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:67`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:68`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:73`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:82`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:83`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:85`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:87`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:97`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:99`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:101`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:103`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:105`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:109`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:119`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:125`
- A03: `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:134`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:140`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:143`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:145`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:151`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:154`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:157`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:160`, `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:162`

## Extracted Concepts

### C01. Core AJTBD semantics remain consistent in AJTBD-SDLC integration

- Concept: Определения jobs/job graph/value из AJTBD корректно перенесены в AJTBD-SDLC без смыслового конфликта.
- Why it matters: Сохраняет семантическую целостность между источником метода и интеграционным документом.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:19`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:21`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:22`

### C02. Early documentation and test planning claims are supported by SDLC phase artifacts

- Concept: Тезис о раннем старте UDD/TVPL подтверждается фазой Software Architectural Design в SDLC_12207_Synthesis.
- Why it matters: Поддерживает shift-left практику документально, а не только риторически.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:26`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:28`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:30`

### C03. AJTBD-SDLC process seam is coherent with W-model shift-left

- Concept: Testability review и ранняя подготовка test strategy/plans в AJTBD-SDLC согласуются с принципами W-model.
- Why it matters: Создаёт процессный мост между требованиями и V&V активностями до кодирования.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:39`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:40`

### C04. Traceability chain jobs -> requirements -> tests -> docs is standards-aligned

- Concept: Практика матрицы следов в AJTBD-SDLC согласуется с 12207 требованиями к traceable/verifiable requirements и linked verification methods.
- Why it matters: Делает “traceability as control” формально проверяемой частью процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:46`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:50`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:51`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:53`

### C05. CJM-as-projection claim must be explicitly marked as interpretation or sourced

- Concept: Тезис “CJM = проекция job graph на временную ось” в текущем виде выглядит как несформализованное допущение, а не подтвержденный первоисточником факт.
- Why it matters: Иначе рушится граница между source-grounded фактами и авторской инженерной интерпретацией.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:65`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:67`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:68`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:73`

### C06. Minimal INCOSE attribute set is inconsistent regarding A7 Strategy

- Concept: В тексте одновременно используется тройка A6/A7/A8 как минимум и отдельный минимум A1/A3/A6/A8 без A7.
- Why it matters: Нужна единая policy для обязательных атрибутов требований в шаблонах и ревью.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:82`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:83`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:85`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:87`

### C07. 12-phase model must be explicitly labeled as viewpoint, not normative structure

- Concept: Нужно повторно маркировать 12-фазную схему как инженерный viewpoint/интерпретацию, чтобы не читать ее как “структуру стандарта”.
- Why it matters: Снижает методологические и юридические ошибки при ссылках на ISO/IEC/IEEE 12207.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:97`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:99`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:101`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:103`

### C08. Terminology and gate lexicon crosswalk is required for consistency

- Concept: CJM должен быть формализован в словаре, а W-model quality gates должны иметь явный crosswalk к 12207 review gates.
- Why it matters: Убирает двуязычие процесса и повышает понятность для новых участников.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:105`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:109`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:119`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:125`

### C09. Overall methodology is valid; issues are local wording/governance gaps

- Concept: Итоговый контур AJTBD -> requirements -> tests/docs признан корректным; выявленные дефекты носят точечный характер.
- Why it matters: Подсказывает, что нужен не redesign, а targeted tightening of claims and terminology.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:134`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:140`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:143`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:145`

### C10. Highest-priority hardening actions are concretely enumerated

- Concept: Указан минимальный набор правок: маркировка интерпретации, синхронизация A7, viewpoint disclaimer, CJM term, gate crosswalk.
- Why it matters: Даёт короткий executable plan улучшения консистентности без смены базовой модели.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:151`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:154`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:157`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:160`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0007-CHATGPT.md:162`

## Unresolved Ambiguities

1. Не принято окончательное решение: A7 Strategy обязателен в minimum set или optional.
2. Не утверждено каноническое определение CJM и его связь с job graph в корпусе терминов.
3. Не зафиксирована официальная таблица соответствия W-model gates и 12207 reviews.
