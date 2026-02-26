# I02-F0001-CHATGPT Concepts (Draft)

[Analyzed source: I02-F0001-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md)

## Source

- chat_id: `I02-F0001-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил найти практические мануалы по многочасовым сессиям Codex, поскольку агент "быстро выполняет задачи" и останавливается (`raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:4`).
2. Пользователь затем зафиксировал собственную проектную идею: построить с нуля набор документов/структурных файлов и state-код для long-running Codex сессий по правилам SDLC и с компактным контекстом задачи (`raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:77`).
3. После фиксации идеи пользователь запросил свежие материалы OpenAI/Anthropic/Google по AGENTS-style файлам и harness engineering, с целью создать новый репозиторий, где агент сам строит SDLC и ведет decision log, связанный с коммитами (`raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:133`).
4. Далее пользователь попросил сразу создать готовую структуру репозитория (все файлы на английском) для мгновенного старта в Codex Desktop на macOS (`raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:242`, `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:246`).
5. Финальный блок: уточнение semantics `facts` и связи с FSM (`raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3013`, `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3164`).

## AI Response Summary

1. Агент объяснил, что long-running режим в Codex чаще достигается process discipline (tmux, stop conditions, compaction/xhigh, app workflow), а не одной скрытой настройкой (`C01`, `C02`, `C03`).
2. Агент корректно зафиксировал пользовательскую формулировку "как есть" без добавления новых концептов, затем привязал её к map-style repository idea (`C04`).
3. Агент собрал источники по AGENTS-like context files и harness engineering, выделив принцип "AGENTS.md = map, docs = system of record" и plan-doc для многочасовых задач (`C05`, `C06`, `C07`).
4. В ответе дан готовый repo scaffold с state/docs/tools/tests и протоколом decision logging, после чего выполнен переход к facts-based state model как factorized FSM (`C08`, `C09`, `C10`, `C11`, `C12`).

## Extracted Concepts

### C01. Long-running Codex work is a workflow pattern, not a single setting

- Concept: Многочасовые сессии обычно строятся через явный цикл работы (continue/plan/stop-conditions), а не "один бесконечный ответ".
- Why it matters: Сдвигает фокус с поиска magic flag на дизайн операционного процесса.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:14`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:53`

### C02. Session durability requires terminal/session orchestration practices

- Concept: Практики `tmux/screen`, re-attach, параллельные панели и корректный session management — базовый operational слой long-running workflow.
- Why it matters: Обеспечивает устойчивость процесса к разрывам и длительной работе.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:30`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:34`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:39`

### C03. Quality-preserving long sessions need explicit stop conditions and planning

- Concept: Для длительной автономной работы нужны stop-conditions, stepwise execution plan, progress artifacts и сниженная chatter policy.
- Why it matters: Позволяет агенту работать долго без потери управляемости.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:53`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:55`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:57`

### C04. User vision centers on SDLC-governed context files for agent work

- Concept: Пользовательская целевая модель — набор project/iteration/task/history файлов + state-management code, чтобы агентная разработка шла по SDLC.
- Why it matters: Это определяет canonical artifact architecture репозитория.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:88`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:96`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:107`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:112`

### C05. AGENTS-style files should be map-oriented, not encyclopedic

- Concept: Harness-oriented best practice: AGENTS/CLAUDE/GEMINI files как короткая карта, а подробная "истина" в структурированных docs.
- Why it matters: Снижает контекстную энтропию и повышает поддерживаемость инструкций.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:148`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:173`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:195`

### C06. Plan artifact is required for multi-hour autonomous runs

- Concept: PLANS/ExecPlan документы должны быть обязательным механизмом управления многочасовыми агентными задачами.
- Why it matters: Обеспечивает непрерывность и контролируемый прогресс без ручного микроменеджмента.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:150`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:205`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:207`

### C07. Decision log must be commit-linked by design

- Concept: Лог решений должен включать decision id, rationale и явную привязку к commit hash как часть DoD.
- Why it matters: Делает решения аудируемыми и проверяемыми post-hoc.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:209`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:216`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:220`

### C08. Bootstrapped repository harness for immediate agent start

- Concept: Репозиторий должен включать минимальный каркас: AGENTS, docs layers, tasks/history/decisions, state JSON, validation/harness tooling, tests.
- Why it matters: Дает "ready-to-run" operating system для агентной SDLC разработки.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:257`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:265`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:287`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:293`

### C09. Facts model is boolean truth set (set semantics)

- Concept: `facts` — множество булевых строковых утверждений: присутствие = true, отсутствие = not asserted true; без value payload внутри fact.
- Why it matters: Формирует компактный и расширяемый state substrate.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3017`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3034`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3100`

### C10. Practical FSM decomposition: stage FSM + fact-state

- Concept: Полное состояние целесообразно задавать как `(run.stage, facts_set)`: маленький явный FSM + факторизованное наблюдаемое состояние.
- Why it matters: Избегает combinatorial explosion и сохраняет управляемость модели.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3211`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3221`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3223`

### C11. Operators (`preconds/add/delete`) are optional maturity layer

- Concept: Operator layer нужен только когда появляется потребность в формальной валидации/авто-next-actions/детерминированном planner.
- Why it matters: Предотвращает premature complexity в ранних итерациях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3195`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3252`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3326`

### C12. Fact hygiene requires strict naming and event-backed updates

- Concept: Надежность facts достигается через normalized names, XOR-pairs pass/fail, и обязательные event entries при каждом meaningful change.
- Why it matters: Устраняет semantic drift и облегчает auditability.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3106`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3112`
  - `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md:3119`

## Unresolved Ambiguities

1. В файле упоминается готовый zip-артефакт, но его содержимое не является частью репозитория и не верифицировано в данном проходе.
2. Не закреплена окончательная граница между facts-only core и operator-based DSL в production режиме.
