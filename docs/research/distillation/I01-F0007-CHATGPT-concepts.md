# I01-F0007-CHATGPT Concepts (Draft)

[Analyzed source: I01-F0007-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md)

## Source

- chat_id: `I01-F0007-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь запросил исследование практик "хорошего git-flow" для AI-агентов (Codex/Claude/Gemini) по Medium, Dev.to и корпоративным блогам минимум 10 компаний (`raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:4`).
2. Затем пользователь попросил сформировать практический Git Flow playbook на английском (`raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:155`).

## AI Response Summary

1. AI собрал обзор источников и вывел консенсусные паттерны агентной разработки через PR-centric процесс и изоляцию задач (`C01`, `C02`).
2. AI сформировал детальный playbook: branch/worktree policy, commit/PR discipline, CI gates, human review, agent guardrails, merge/hotfix/dependency flows (`C03`-`C07`).
3. Рекомендуемый default — trunk-based с короткоживущими ветками и обязательным human-in-the-loop (`C01`, `C04`).

## Extracted Concepts

### C01. PR как базовая единица интеграции агентной работы

- Concept: Агентские изменения должны приходить как branch + PR с review/CI, а не прямыми пушами в `main`.
- Why it matters: Создает буфер безопасности, аудит изменений и управляемый merge-контур.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:87`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:91`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:290`

### C02. Изоляция параллельной агентной работы через worktrees

- Concept: Один агент = одна ветка/один worktree; параллельные задачи выполняются в отдельных рабочих копиях.
- Why it matters: Устраняет коллизии, гонки и "перетирание" контекста между агентами.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:93`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:95`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:245`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:247`

### C03. Trunk-based default и короткоживущие ветки

- Concept: Рекомендуется `main` (защищенный trunk) + короткоживущие task-ветки с жестким запретом direct commit в main.
- Why it matters: Снижает интеграционную сложность и ускоряет безопасный цикл поставки.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:190`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:194`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:200`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:204`

### C04. Обязательный human-in-the-loop в agentic SDLC

- Concept: Агенты предлагают изменения, человек принимает решение о merge после технической и риск-оценки.
- Why it matters: Ограничивает автономные ошибки и сохраняет архитектурные инварианты.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:181`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:182`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:136`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:137`

### C05. Малые диффы, чекпойнты и timeboxing как анти-энтропия

- Concept: Агентную работу нужно дробить на малые PR/коммиты, добавлять промежуточные остановки и лимиты автономного цикла.
- Why it matters: Предотвращает "giant diffs", снижает риск регрессий и облегчает ревью.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:103`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:105`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:420`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:421`

### C06. CI/branch protection как неотменяемый quality gate

- Concept: Для main обязательны PR-only merge, required checks, approvals, CODEOWNERS и security/dependency проверки.
- Why it matters: Делает интеграцию агентного кода воспроизводимой и защищенной.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:356`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:360`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:367`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:375`

### C07. Least privilege и ограниченная автономия агентов

- Concept: Агенты работают по принципу минимальных прав; критичные зоны (CI, IAM, auth, destructive ops, secrets) требуют ручного одобрения.
- Why it matters: Снижает операционные и security-риски в автономной разработке.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:185`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:186`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:410`
  - `raw-exports/sdlc-discovery-iteration-01/I01-F0007-CHATGPT.md:416`

## Unresolved Ambiguities

1. В первой части источника есть ссылки-цитаты вида `turnXsearchY`; без исходного окружения невозможно проверить релевантность каждого внешнего материала.
2. Playbook дан как универсальный baseline; для прямого внедрения нужны репо-специфичные параметры (CI stack, branching protection, CODEOWNERS зоны).
