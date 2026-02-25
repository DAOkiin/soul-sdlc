# План действий для проекта

#### You:
Я разрабатываю процесс и код для управления состояним разработки в репозитории при помощи ИИ-агента OpenAI Codex. Я решил сделать програмное управление состоянием графа разработки. Изучи материалы, которые я уже подготовил и сформируй план действий. Я думаю, что следующий шаг – зафиксировать процесс, а затем имплементировать весь код для управления состоянием разработки. Вот материалы, которые я уже подготовил:


---

### Контекст проекта

- `<agent-task-v1>`: Первый вариант DDL с базовыми гейтами и переходами, оптимизированный для быстрого запуска и итераций.
- `<agent-task-v2>`: Второй вариант DDL с более формализованными правилами и встроенными guards, оптимизированный для строгой консистентности.
- `<agent-task-comparison>`: Сравнение v1 и v2, анализ плюсов и минусов каждого подхода, рекомендации по выбору.
- `<agent-task-analysis>`: Анализ и выводы из сравнения, практические рекомендации по выбору и адаптации DDL для проекта.
- `<deep-research-report>`: Анализ статей и практик в области harness engineering, выводы о том, как они соотносятся с выбором между v1 и v2.
- `<implementation-project-sdlc>`: Текущая реализация процесса SDLC в виде DDL и кода для управления состоянием разработки. Сырая и недоработанная, требует доработки и рефакторинга.

---

#### ChatGPT:
Понял: я изучу твой текущий DDL/state/CLI и черновые спецификации v1/v2, затем соберу единый план “зафиксировать процесс → имплементировать управление состоянием” с приоритетами, этапами, DoD и рисками/миграцией.


#### Plugin (file_search):
Make sure to include fileciteturn0file0 in your response to cite this file, or to surface it as a link.

<agent-task-v1>

Ниже — готовая **задача (prompt) для твоего агента**, уже с выбранным дизайном и конкретными deliverables. Можно копипастить как есть.

---

# Задача: SDLC Guards + Pre‑push Gate + Визуализация state machine + Markdown‑шаблон

## Контекст (где это живёт сейчас)

В репозитории уже есть:

* Process DDL: `docs/_meta/process/sdlc-task-flow.ddl.yaml`
* Runtime state: `docs/_meta/process/sdlc-task-flow.state.yaml`
* Компилятор/CLI: `src/paip/process_compiler.py` (команды `compile/init/advance/show`)
* Текущий pre-push hook: `.githooks/pre-push` (синхронизация git notes)
* Команды качества: `just test`, `just qc-validate-ci` (см. `justfile`)
* Проектный cockpit: `scripts/print_project_state.py`

Нужно добавить **guards** (проверяемые условия/команды), которые можно запускать:

1. вручную,
2. автоматически в `pre-push` (и блокировать push при fail),
3. использовать в документации (видно, какие гейты есть).

---

## Цель (что должно получиться)

Сделать минимальную, расширяемую систему “process-as-code + guards-as-code”:

1. **Guards** описываются в отдельном конфиге (данные), без захардкоживания логики в хуках.
2. **pre-push hook** запускает guards и **падает (exit != 0)** при ошибках.
3. Есть **инструмент генерации диаграммы** state machine из DDL (Mermaid).
4. Есть **Markdown‑шаблон/док** процесса с пояснениями + встроенной диаграммой (Mermaid) + кратким списком guards.
5. Всё работает без новых прод‑зависимостей (только stdlib + то, что уже есть). Конфиги — **JSON‑совместимый YAML** (как текущий DDL).

---

## Дизайн (выбранный подход)

### Почему не встраиваем guards в DDL

DDL уже валидируется pydantic-моделями. Добавление полей “guards” в DDL быстро превратит DDL в “всё обо всём”. Лучше держать:

* DDL = граф,
* Guards = проверки/политики исполнения.

### Формат guards-конфига

Новый файл:

* `docs/_meta/process/sdlc-task-flow.guards.yaml` (JSON‑compatible YAML)

Схема (v0):

* `process_id`, `version` (должны совпасть с DDL)
* `contexts`:

  * `pre_push`: список guards, которые запускаются перед push
  * `advance`: mapping `step_id -> список guards`, которые должны проходить **перед advance** с этого шага (дополнительно, но очень желательная связка)

Guard (минимальный набор типов):

* `command`: выполнить shell‑команду (например `just test`)
* `require_branch`: требовать, чтобы `state.branch` был установлен (A/B/C)
* `glob_exists`: требовать существование файлов по glob (например ADR)

У guard есть:

* `id` (строка)
* `title` (строка)
* `severity`: `error|warn` (warn не блокирует pre-push, но печатается)
* `when`: условия выполнения:

  * `branch_in`: `["A","B","C"]` (опционально)
  * `changed_files_any`: список glob‑паттернов; запускать guard только если **хотя бы один** изменённый файл совпал
    (нужно для скорости, особенно для QC)

Важно: список изменённых файлов должен приходить из `pre-push` (по диапазону пуша), и пробрасываться в runner и в QC-скрипт через env `QC_CHANGED_FILES`.

---

## Deliverables (что реализовать)

### 1) Guard runner (CLI tool)

Добавить модуль:

* `src/paip/process_guards.py`

CLI:

* `python -m paip.process_guards check --context pre_push --ddl <...> --state <...> --guards <...> [--changed-files-file <...>]`
* `python -m paip.process_guards check --context advance --ddl ... --state ... --guards ...`
  (в этом режиме runner должен брать guards для `current_step` и проверять readiness “можно ли advance”)
* (опционально, но рекомендую) `python -m paip.process_guards advance --ddl ... --state ... --guards ... [--to <step>] [--branch <A|B|C>] [--reason "..."]`
  → делает guard‑check для контекста `advance` и **только потом** вызывает логику advance и сохраняет state.

Поведение runner’а:

* Загружает DDL + state + guards config, проверяет совпадение `process_id/version`.
* Определяет `branch` из `state.branch`.
* Загружает changed files (если есть) из:

  * `--changed-files-file` (каждая строка — путь), иначе из env `PAIP_CHANGED_FILES` (если задан).
* Для каждого guard:

  * проверяет `when` (branch, changed_files),
  * исполняет guard,
  * пишет результат в человекочитаемом виде (✓ / ✗ / ! skipped),
  * аккуратно печатает хвост stdout/stderr при падении команды (например последние 30–50 строк).
* Exit code:

  * `0`, если нет `severity=error` failure,
  * `1`, если есть хотя бы один error failure.
  * Warn failures не блокируют, но отмечаются.

При выполнении `command` guards:

* пробрасывай env:

  * `PAIP_CHANGED_FILES` (newline-separated)
  * `QC_CHANGED_FILES` (тот же список) — чтобы `scripts/qc_validate_ci.sh` мог скипать/ранить.

### 2) Guards config (v0) под текущий процесс

Создать файл:

* `docs/_meta/process/sdlc-task-flow.guards.yaml`

Рекомендованный стартовый набор:

**pre_push**:

* `require_branch` (error) — если branch не выбран, блокировать push (иначе процесс не управляет ничем).
* `just test` (error) — всегда.
* `just qc-validate-ci` (error) — если:

  * `branch_in: ["B"]` **или**
  * changed_files_any включает `query-catalog/**` или `src/**` или `scripts/qc_validate*` или `docs/_meta/QC-STANDARD.md`
* (опционально, warn) `just readme-links-check` — если менялись `README.md` или `docs/**`

**advance** (по шагам):

* `scope_gate`: require_branch (error)
* `query_catalog_gate`: qc-validate-ci (error)
* `adr_gate`: glob_exists `docs/adr/ADR-*.md` min_count=1 (error)
* `code_only_path`: just test (error)
* `validation_gate`: just test (error) (на всякий)

*(Да, `advance` контекст формально не обязателен по твоему запросу, но он делает систему “guards как настоящие guard conditions”, а не просто “хуковая проверка”.)*

### 3) Обновить pre-push hook

Изменить `.githooks/pre-push`:

Требования:

* **Сначала** запускаем guards, **потом** синхронизацию git notes (чтобы не пушить notes, если основной push будет заблокирован).

* Добавить env bypass:

  * `PAIP_SKIP_GUARDS=1` → пропустить guard checks (только emergency).
  * существующий `PAIP_SKIP_NOTES_PUSH=1` оставить как есть (но он не должен скипать guards).

* Вычислить changed files по диапазону пуша:

  * читать stdin строки формата: `local_ref local_sha remote_ref remote_sha`
  * для каждой строки собрать `git diff --name-only remote_sha..local_sha` (если remote_sha = 0000.. → diff от empty tree)
  * объединить в уникальный список
  * сохранить во временный файл (предпочтительнее, чем env), передать в runner через `--changed-files-file`.

* Вызов guard runner должен использовать python из venv:

  * если `.venv/bin/python` существует → использовать его
  * иначе печатать понятную ошибку “run just setup / hooks-install” и **блокировать push** (exit 1), чтобы контроль не отключался молча.

Команда запуска guards (примерно):

```bash
"${python_bin}" -m paip.process_guards check \
  --context pre_push \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state docs/_meta/process/sdlc-task-flow.state.yaml \
  --guards docs/_meta/process/sdlc-task-flow.guards.yaml \
  --changed-files-file "$tmp_changed"
```

### 4) Инструмент визуализации графа (Mermaid)

Расширить `src/paip/process_compiler.py`:

* добавить функцию рендера Mermaid: `render_mermaid_state_diagram(ddl) -> str`
* добавить CLI subcommand, например:

  * `python -m paip.process_compiler render --ddl <...> [--out <file>] [--format mermaid]`

Mermaid-формат: **stateDiagram-v2**, с:

* стартом: `[*] --> <initial>`
* концом: `<terminal> --> [*]`
* для каждого шага: объявление `state "..." as <id>`

  * label должен включать `step_id`, `type`, `title` (чтобы по диаграмме можно было работать)
* переходы с label:

  * если у transition есть `label` (A/B/C) — рендерить как подпись ребра
  * иначе без подписи или использовать `description` (коротко, без простыней)

Выход должен быть детерминированным (стабильный порядок шагов/edges).

### 5) Markdown‑шаблон/док процесса с диаграммой

Создать файл:

* `docs/_meta/process/sdlc-task-flow.md`

Содержимое:

* краткое описание, что это за процесс
* какие файлы являются source of truth (DDL/state/guards)
* как пользоваться CLI (`init/show/advance`, и новый guard runner)
* как работает pre-push (что блокирует, как bypass)
* секции с автогеном (через маркеры), чтобы диаграмма не дрейфовала:

Маркеры:

* `<!-- BEGIN SDLC DIAGRAM -->` … `<!-- END SDLC DIAGRAM -->`
* `<!-- BEGIN SDLC GUARDS -->` … `<!-- END SDLC GUARDS -->`

Внутри DIAGRAM — fenced block:

````
```mermaid
...generated...
```
````

Внутри GUARDS — таблица (генерируемая из guards.yaml):

* Guard ID
* Severity
* When (branch + patterns)
* Command / check type

### 6) Sync tool для обновления md (рекомендовано)

Добавить скрипт:

* `scripts/sync_process_docs.py`

Он должен:

* читать DDL + guards config,
* генерировать Mermaid,
* генерировать guard-table,
* вставлять/заменять только содержимое между маркерами в `docs/_meta/process/sdlc-task-flow.md`.

*(Это сильно снижает вероятность, что документация устареет.)*

---

## Обязательные тесты

Добавить `tests/test_process_guards.py` (минимум):

* корректная загрузка guards config и матч `process_id/version`
* `require_branch` падает, если `state.branch` пустой
* `changed_files_any` реально скипает/ранит guard
* `command` guard:

  * success через `python -c "import sys; sys.exit(0)"`
  * fail через `python -c "import sys; sys.exit(1)"`

Все тесты должны проходить: `just test`.

---

## Не‑цели (чтобы не разрасталось)

* Не строить универсальный workflow engine.
* Не делать UI.
* Не тянуть Graphviz как зависимость (Mermaid достаточно).
* Не усложнять guards условиями “changed_files_all/regex” — только `branch_in` + `changed_files_any` (v0).

---

## Definition of Done (acceptance criteria)

* `python -m paip.process_guards check --context pre_push ...` возвращает:

  * `0` если всё ок
  * `1` если хотя бы один error guard упал
* `.githooks/pre-push`:

  * блокирует push при fail guards
  * уважает `PAIP_SKIP_GUARDS=1`
  * сохраняет прежнюю функциональность синка git notes
* `python -m paip.process_compiler render --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml` печатает валидный Mermaid stateDiagram-v2
* `docs/_meta/process/sdlc-task-flow.md` существует и содержит:

  * объяснения
  * Mermaid‑диаграмму
  * список guards
* `just test` зелёный

---

Если хочешь — следующим шагом можно добавить “quality-of-life”:

* показать статусы guards в `scripts/print_project_state.py` (например, “pre-push guards: PASS/FAIL”),
* сделать `just guards` / `just process-docs-sync` и обновить `docs/_meta/JUST-COMMANDS.md`.

Но это **optional**, делай только если остаётся время и не ломает текущий DX.

</agent-task-v1>

<agent-task-v2>

Ниже — готовая **задача (ticket/spec)** для твоего агента. Я заложил дизайн так, чтобы это было “process-as-code” и работало одинаково для: **advance**, **pre-push**, и **документации** (diagram-as-code), без новых зависимостей.

---

# Задача: Guards + pre-push enforcement + визуализация SDLC state machine (process-as-code)

## Контекст

В репозитории уже есть:

* DDL процесса: `docs/_meta/process/sdlc-task-flow.ddl.yaml`
* Runtime state: `docs/_meta/process/sdlc-task-flow.state.yaml`
* Компилятор/CLI: `src/paip/process_compiler.py`
* Git hook: `.githooks/pre-push` (сейчас пушит git-notes)
* QC валидатор: `scripts/qc_validate.py` + `just qc-validate`
* Итерационные чеклисты: `docs/iterations/<ITER>/reviews.md` (checkbox + Sign-off)

Цель: сделать SDLC действительно **agent-enforced**:

1. Guards формализованы в DDL и могут запускаться как проверки.
2. `pre-push` запускает guards и **ломает push**, если must-guards не выполнены.
3. Есть инструмент, который генерирует **Mermaid-диаграмму** графа и Markdown-док (по шаблону).

## Итоговые артефакты (deliverables)

1. Поддержка **guards** в DDL и их исполнение:

   * оценка guards для текущего state/step/branch,
   * блокировка `advance`, если must-guards не пройдены (с возможностью bypass).
2. Обновлённый `.githooks/pre-push`:

   * сначала запускает guard-check (и падает при fail),
   * затем выполняет текущую логику sync git-notes (как сейчас).
3. Инструмент визуализации графа:

   * генерация Mermaid (flowchart предпочтительно),
   * генерация Markdown-документа по шаблону (вставляет диаграмму + метаданные).
4. Markdown-шаблон документа процесса (template):

   * пояснения, как читать/использовать,
   * место для диаграммы,
   * (опционально) таблица шагов/guards.
5. Обновления docs + тесты:

   * обновить `docs/_meta/process/compiler.md` (описать guards + новые команды),
   * добавить/обновить тесты в `tests/test_process_compiler.py` (guard-engine, when-фильтры, fail behavior).

---

## Дизайн (обязательный)

### 1) Схема guards в DDL

Добавить поддержку guards на 2 уровнях:

* **process-level guards** (общие правила для всего процесса)
* **step-level guards** (требования для конкретного шага)

Минимально достаточно step-level, но process-level даёт сильный выигрыш для pre-push (например, всегда требовать зелёные тесты).

#### Предлагаемый формат GuardDef (JSON-compatible YAML)

Guard — объект с полями:

* `id`: string (уникальный в рамках списка)
* `title`: string (коротко “что проверяем”)
* `level`: `"must"` | `"should"` (default: `"must"`)
* `phase`: список фаз, где guard должен выполняться: `["advance"]`, `["push"]`, `["ci"]`, или `["any"]`
* `kind`: `"command"` | `"file_exists"` | `"file_glob"` | `"markdown_checklist"`
* `when`: опциональный фильтр применимости:

  * `branch_in`: `["A","B","C"]`
  * `step_in`: `["scope_gate", ...]`
  * `status_in`: `["in_progress","blocked","done"]`
* параметры по kind:

  * `command`: `cmd` (string), опционально `timeout_sec`, `cwd`
  * `file_exists`: `path`
  * `file_glob`: `glob` (string) ИЛИ `globs` (list)
  * `markdown_checklist`: `path`, `section`, `require_all_checked` (bool), `require_signoff` (bool)

#### Тэмплейтинг (важно)

Поля `cmd`, `path`, `glob` должны поддерживать подстановки через `.format_map()`:

* `{branch}` (из state.branch)
* `{current_step}` (из state.current_step)
* `{status}` (state.status)
* `{iteration}` (автоматически найденная “текущая итерация” = последняя папка в `docs/iterations/`)
* любые ключи `state.memory` доступны как `{<key>}` (например `{adr_path}`)

Если placeholder не найден — guard должен **fail** с понятным сообщением (это обычно дефект состояния/конфига).

### 2) Где и как исполнять guards

Добавить в `src/paip/process_compiler.py`:

* pydantic-модели для GuardDef/GuardWhen
* функции:

  * `collect_applicable_guards(ddl, state, step_id, phase) -> list[GuardDef]`
  * `run_guards(...) -> list[GuardResult]`
  * `format_guard_report(results) -> str`
* `GuardResult` (dataclass или pydantic):

  * `id`, `title`, `ok`, `level`, `phase`, `details` (строка), `stdout`, `stderr` (для command)

**Exit semantics**:

* если есть хоть один `must` guard с `ok=False` → exit code `1`
* `should` guard:

  * по умолчанию не валит процесс (но печатает WARN),
  * опция `--strict` превращает should в “как must” (exit 1).

### 3) Интеграция с `advance`

`python -m paip.process_compiler advance ...` должен:

* перед сменой шага запускать guards для `phase=advance` на **текущем шаге**
* если fail → не менять state и вернуть ошибку

Добавить флаг bypass:

* `--no-guards` (или `--force`) чтобы позволить “продавить” переход (но печатать предупреждение).

---

## CLI изменения (обязательные команды)

В `src/paip/process_compiler.py` добавить сабкоманды:

### A) `guards` (или `check`)

Пример:

```bash
PYTHONPATH=src python -m paip.process_compiler guards \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state docs/_meta/process/sdlc-task-flow.state.yaml \
  --phase push
```

Опции:

* `--phase` (default: `advance`)
* `--strict`
* `--json` (машиночитаемый вывод)
* `--root` (default `"."`) — для относительных путей/итераций/выполнения команд

### B) `render` (диаграмма)

Генерит Mermaid диаграмму в stdout или в файл:

```bash
PYTHONPATH=src python -m paip.process_compiler render \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --out docs/_meta/process/sdlc-task-flow.mmd
```

Фичи:

* формат: Mermaid **flowchart** (предпочтительно)
* shape по типам шагов:

  * gate: decision `{{ }}`
  * action: process `[ ]`
  * terminal: `(( ))`
* подписи на ребрах: `label` + `description` (склеить компактно)
* если передан `--state`, подсветить `current_step` (через `classDef`/`class`)

### C) `render-doc` (Markdown по шаблону)

```bash
PYTHONPATH=src python -m paip.process_compiler render-doc \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state docs/_meta/process/sdlc-task-flow.state.yaml \
  --template docs/_meta/process/process-doc.template.md \
  --out docs/_meta/process/sdlc-task-flow.md
```

* заполняет placeholders: `$PROCESS_ID`, `$VERSION`, `$DDL_PATH`, `$STATE_PATH`, `$GENERATED_AT`, `$MERMAID`
* (опционально) генерит `$STEPS_TABLE` и `$GUARDS_TABLE`/`$GUARDS_SECTION`

---

## Pre-push hook (обязательное поведение)

Файл: `.githooks/pre-push`

Требования:

1. Сохранить существующую логику синка `refs/notes/commits`.
2. Добавить запуск guard-check **до** пуша notes:

   * если guards fail → печатаем отчёт и `exit 1` (push должен упасть)
3. Добавить bypass:

   * `PAIP_SKIP_GUARDS_PUSH=1` → пропускаем guard-check
   * текущий `PAIP_SKIP_NOTES_PUSH=1` оставить как есть

Технически:

* определить repo root: `git rev-parse --show-toplevel`
* выбрать python:

  * если есть `.venv/bin/python` → использовать
  * иначе `python3`
* запуск:

  ```bash
  PYTHONPATH="$ROOT/src" "$PY" -m paip.process_compiler guards \
    --phase push \
    --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
    --state docs/_meta/process/sdlc-task-flow.state.yaml
  ```

---

## Обновить DDL: добавить реальные guards (обязательные минимальные)

Файл: `docs/_meta/process/sdlc-task-flow.ddl.yaml`

Минимальный набор (предложение):

1. **Process-level** (phase=push): тесты зелёные

   * `kind=command`, `cmd="just test"`
2. Step `query_catalog_gate` (phase=advance + push): QC валидация

   * `cmd="just qc-validate"`
3. Step `adr_gate` (phase=advance): ADR существует по указателю из memory

   * `kind=file_exists`, `path="{adr_path}"`
   * `when.branch_in=["C"]`
   * (и в описании: “agent обязан записать state.memory.adr_path”)
4. Опционально, но очень полезно для “done”: Validation baseline в reviews.md

   * `kind=markdown_checklist`
   * `path="docs/iterations/{iteration}/reviews.md"`
   * `section="Validation Baseline"`
   * `require_all_checked=true`, `require_signoff=true`
   * `when.step_in=["validation_gate"]`
   * `level="should"` (или must, если хочешь “только зелёные pushes после done”)

---

## Markdown template (создать новый файл)

Создать: `docs/_meta/process/process-doc.template.md`

Содержание (скелет):

* заголовок (process_id/version)
* “как пользоваться” (команды guards/advance/render-doc)
* “где лежит state”
* Mermaid блок (placeholder `$MERMAID`)
* (опционально) список шагов/guards

Плейсхолдеры использовать через `string.Template`:

* `$PROCESS_ID`
* `$VERSION`
* `$DDL_PATH`
* `$STATE_PATH`
* `$GENERATED_AT`
* `$MERMAID`
* `$STEPS_TABLE` (если сделаешь)
* `$GUARDS_SECTION` (если сделаешь)

Также сгенерировать и закоммитить готовый документ:

* `docs/_meta/process/sdlc-task-flow.md` (через render-doc)

---

## Тесты (обязательные)

Расширить `tests/test_process_compiler.py`:

* `test_guards_command_pass`:

  * guard `command` с `python -c "exit(0)"` → PASS
* `test_guards_command_fail_blocks_advance`:

  * guard `command` с `python -c "exit(1)"` → advance должен падать
* `test_when_filters`:

  * guard с `when.branch_in=["B"]` не должен запускаться при branch A
* `test_template_render_includes_edges`:

  * render mermaid содержит основные ноды и ребра

(Важно: тесты не должны зависеть от `just` и внешних бинарей — в тестах используй `python -c`.)

---

## Документация (обязательные правки)

Обновить `docs/_meta/process/compiler.md`:

* добавить раздел “Guards”
* описать schema guard’ов
* примеры запуска `guards`, `advance`, `render`, `render-doc`
* описать поведение pre-push (и переменные bypass)

---

## Definition of Done

* `python -m paip.process_compiler guards ...` работает и даёт понятный отчёт.
* `advance` блокируется must-guards, есть bypass флаг.
* `.githooks/pre-push` валит push при must-fail (и сохраняет notes-sync).
* `render` генерит Mermaid flowchart, `render-doc` генерит Markdown из template.
* DDL обновлён и содержит хотя бы 2–3 реальных guards.
* Все тесты зелёные: `just test`.

---

## Доп. рекомендации (если останется время)

1. Сделать `--json` вывод стабильно пригодным для CI (массив результатов + summary).
2. Добавить “короткий режим” в `guards`: `--quiet` (только ошибки).
3. В отчёте guards печатать “как починить” (remediation hints) для типовых fail:

   * “нет .venv → запусти just setup”
   * “не установлены QC deps → just qc-setup”
4. (Опционально) обновить `scripts/print_project_state.py`, чтобы он дополнительно показывал **guard status** для текущего шага (без дублирования тяжелых команд).

---

Если хочешь, я могу сразу предложить конкретный **патч-стиль пример** для DDL (с guards) и пример содержимого `process-doc.template.md` — но даже в текущем виде агенту достаточно, чтобы реализовать целиком без уточнений.

</agent-task-v2>

<agent-task-comparison>

Ниже — сравнение **agent-task-v1.md** и **agent-task-v2.md** по смыслу, архитектуре и конкретным deliverables.




---

## Что общего (сходства)

Оба документа описывают одну и ту же “сверх‑цель”: сделать SDLC/процесс **реально исполняемым** (process‑as‑code) через формализованные проверки, которые:

* можно запускать вручную (CLI),
* автоматически выполняются в **pre-push** и **блокируют push** при провале обязательных проверок,
* синхронизируются с процессом **advance** (переход по шагам/стейт‑машине),
* и всё это документируется (генерация Mermaid‑диаграммы + Markdown‑док/шаблон).

Общие элементы, которые повторяются в обоих:

* есть существующие источники правды: **DDL процесса** (`docs/_meta/process/sdlc-task-flow.ddl.yaml`) и **runtime state** (`docs/_meta/process/sdlc-task-flow.state.yaml`);
* pre-push должен **сначала** прогонять проверки, и **только потом** выполнять текущую логику синка `git notes`;
* нужно добавить генерацию Mermaid‑диаграммы процесса;
* нужны тесты, которые проверяют **pass/fail‑семантику** guards (в тестах — через `python -c ...`, без зависимости от `just`);
* в обоих есть чёткие **Definition of Done**.

---

## Ключевое расхождение №1: где живут guards

### v1: guards — отдельный конфиг (отдельно от DDL)

**agent-task-v1.md** сознательно разделяет:

* **DDL = граф/структура процесса**,
* **Guards = политика/проверки исполнения**.

То есть создаётся отдельный файл вроде:

* `docs/_meta/process/sdlc-task-flow.guards.yaml`

И именно он управляет тем, что запускается в `pre_push` и перед `advance`.

**Причина в v1 сформулирована прямо**: не “раздувать” DDL и не превращать его в “всё обо всём”.

### v2: guards встраиваются прямо в DDL

**agent-task-v2.md** предлагает обратное: расширить DDL, добавив guards:

* на **process-level** (общие проверки),
* на **step-level** (требования конкретного шага).

Это делает DDL “центральным” местом, где одновременно описаны и граф, и требования/гейты.

**Итог:** это принципиально разные архитектуры. В v1 guards — “рядом” с процессом; в v2 guards — “внутри” процесса.

---

## Ключевое расхождение №2: насколько “богатая” модель guards

### Модель guards в v1 — минимальная и практичная

В v1 набор намеренно небольшой (v0), с упором на pre-push performance и простоту:

* **типы**: `command`, `require_branch`, `glob_exists`
* **важность**: `severity: error|warn`
* **условия запуска**:

   * `branch_in: ["A","B","C"]`
   * `changed_files_any: [glob...]` (оптимизация по изменённым файлам)
* **контексты**:

   * `pre_push: [guards...]`
   * `advance: { step_id: [guards...] }`

Плюс важная деталь: список изменённых файлов вычисляется в хуке и прокидывается в runner (и в QC через env).

### Модель guards в v2 — более “движковая”

Во v2 модель заметно шире:

* **важность**: `level: must|should` + режим `--strict`, превращающий should в must
* **фазы**: `phase: ["advance"|"push"|"ci"|"any"]`
* **типы**: `command`, `file_exists`, `file_glob`, `markdown_checklist`
* **when-фильтры**: `branch_in`, `step_in`, `status_in`
* **тэмплейтинг** через `.format_map()`:

   * `{branch}`, `{current_step}`, `{status}`
   * `{iteration}` (автоопределение “последней итерации” в `docs/iterations/`)
   * ключи из `state.memory` как `{adr_path}` и т.п.

**Итог:** v2 закладывает гораздо более общий “guard engine” (с подстановками, фазами, чеклистами), в то время как v1 — лёгкая система “политики + runner” с минимальными условиями и упором на changed-files.

---

## Ключевое расхождение №3: где исполняется логика (архитектура кода и CLI)

### v1: отдельный guard runner модуль

В v1 добавляется отдельный модуль:

* `src/paip/process_guards.py`

И отдельная CLI-команда `python -m paip.process_guards check ...` (контексты `pre_push` и `advance`), плюс опциональная команда `advance`, которая сначала прогоняет guards, потом делает переход.

Это подчёркивает независимость guards от компилятора процесса.

### v2: всё в `process_compiler.py`

В v2 логика guards добавляется прямо в:

* `src/paip/process_compiler.py`

Появляются функции вроде `collect_applicable_guards`, `run_guards`, `format_guard_report` и новая сабкоманда:

* `python -m paip.process_compiler guards --phase push|advance`

**Итог:** v1 делает отдельный “guards subsystem”; v2 расширяет существующий compiler/CLI, делая его “one tool to rule them all”.

---

## Pre-push: сходство в намерении, различие в деталях

### Общее

И там и там:

* guard-check запускается **до** синка `git notes`;
* есть переменная bypass для emergency;
* `PAIP_SKIP_NOTES_PUSH=1` остаётся отдельным переключателем, не отключающим guards.

### Различия

* **Имя bypass переменной**:

   * v1: `PAIP_SKIP_GUARDS=1`
   * v2: `PAIP_SKIP_GUARDS_PUSH=1`
* **changed files**:

   * v1: hook вычисляет `git diff --name-only ...` по диапазону пуша, дедуплицирует и передаёт в runner (и далее в QC);
   * v2: такой механики нет — hook просто запускает `process_compiler guards --phase push`.
* **выбор python**:

   * v1: если нет `.venv/bin/python` — это **ошибка и блокировка push** (чтобы контроль не “молча отключился”).
   * v2: если нет `.venv/bin/python` — используется `python3` (то есть более мягкая деградация).

---

## Диаграмма Mermaid: state machine vs flowchart

* **v1** требует Mermaid **stateDiagram-v2**:

   * явно рисуется старт `[*] --> initial` и терминал `terminal --> [*]`,
   * ноды объявляются как `state "..." as <id>`,
   * рендер должен быть детерминированным (стабильный порядок шагов/рёбер).

* **v2** предпочитает Mermaid **flowchart**:

   * разные формы по типам шагов (gate/action/terminal),
   * подписи на рёбрах: `label + description`,
   * опциональная подсветка `current_step`, если передан `--state`.

**Итог:** v1 ближе к “чистой” конечной автоматике, v2 — к более “презентабельной” блок‑схеме.

---

## Документация: маркеры синхронизации vs шаблон

### v1: один Markdown + маркеры + отдельный sync script

* Создаётся `docs/_meta/process/sdlc-task-flow.md`
* Вставки диаграммы и таблицы guards делаются между маркерами:

   * `<!-- BEGIN SDLC DIAGRAM --> ... <!-- END SDLC DIAGRAM -->`
   * `<!-- BEGIN SDLC GUARDS --> ... <!-- END SDLC GUARDS -->`
* Для обновления предлагается `scripts/sync_process_docs.py`, который читает DDL + guards config и обновляет только эти секции.

### v2: template + render-doc

* Создаётся template:

   * `docs/_meta/process/process-doc.template.md`
* Команда `render-doc` генерирует итоговый документ по шаблону:

   * placeholder’ы `$PROCESS_ID`, `$VERSION`, `$MERMAID`, и т.д.
* Дополнительно v2 требует обновить `docs/_meta/process/compiler.md` (описать guards и новые команды).

**Итог:** v1 ориентирован на “частично‑ручной документ с автосекциями”, v2 — на “полностью генерируемый документ из template”.

---

## Тесты: разные точки приложения

* **v1** добавляет отдельный тестовый файл под runner:

   * `tests/test_process_guards.py`
   * фокус: загрузка guards config, `require_branch`, when-фильтры по changed files, `command` pass/fail.

* **v2** расширяет существующие тесты компилятора:

   * `tests/test_process_compiler.py`
   * фокус: guard-engine внутри compiler, when-фильтры (branch), блокировка advance, render mermaid содержит ключевые ноды/рёбра.

---

## Ещё заметные различия (контекст/термины)

* Команды QC различаются:

   * v1: `just qc-validate-ci` / упоминание CI‑валидации,
   * v2: `scripts/qc_validate.py` + `just qc-validate`.
* v2 явно вводит guard вида `markdown_checklist` и привязку к итерационным ревью (`docs/iterations/<ITER>/reviews.md`), чего нет в v1.
* Терминология:

   * v1: **context** (`pre_push`, `advance`) + `severity error|warn`,
   * v2: **phase** (`push`, `advance`, `ci`, `any`) + `level must|should`.

---

## Сводная таблица различий (коротко)

| Аспект                    | v1                               | v2                                            |              |                    |
|---------------------------|----------------------------------|-----------------------------------------------|--------------|--------------------|
| Где описаны guards        | Отдельный `*.guards.yaml`        | Прямо в DDL (`*.ddl.yaml`)                    |              |                    |
| Исполнение                | Новый модуль `process_guards.py` | Встроено в `process_compiler.py`              |              |                    |
| Семантика важности        | `severity: error                 | warn`                                         | `level: must | should`+`--strict` |
| Условия применимости      | `branch_in`, `changed_files_any` | `branch_in`, `step_in`, `status_in`           |              |                    |
| Changed-files оптимизация | Да, обязательная часть дизайна   | Нет                                           |              |                    |
| Mermaid                   | `stateDiagram-v2`                | `flowchart` (+ формы, подсветка)              |              |                    |
| Док генерация             | Один md + маркеры + sync-скрипт  | template + `render-doc`                       |              |                    |
| Интеграция с advance      | Опциональна (рекомендована)      | Обязательна (advance блокируется must-guards) |              |                    |
| Pre-push bypass           | `PAIP_SKIP_GUARDS=1`             | `PAIP_SKIP_GUARDS_PUSH=1`                     |              |                    |

</agent-task-comparison>

<agent-task-analysis>

Для **быстрого развития** (быстро получить работающий контур + быстро менять правила без риска сломать базовую механику процесса) **я бы выбрал v1 как базу**, а из v2 **позаимствовал несколько идей, но не весь дизайн целиком**.

Ниже — почему так, если смотреть через призму “harness engineering” и практики ускорения агентной разработки.

---

## Почему v1 быстрее разгоняет скорость (time-to-velocity)

### 1) Меньше связности → быстрее итерации

В v1 guards вынесены в отдельный конфиг и прямо объясняется, почему: DDL уже валидируется моделями, и “запихивание” guards в DDL быстро превращает DDL в “всё обо всём”; предлагается держать **DDL = граф**, **Guards = политика/проверки исполнения**.

**Для скорости это критично**: правила (guards) обычно меняются чаще, чем граф процесса. Если каждый тюнинг гейтов требует правки DDL и связанных pydantic-моделей/валидаторов — цикл “поменял → проверил → откатил” становится дороже и рискованнее.

Это хорошо ложится на мысль из harness engineering: когда агенту “не хватает среды”, прогресс замедляется, и правильная реакция — **достроить недостающую capability, сделать её “legible and enforceable”** (а не усложнять основную систему). ([OpenAI][1])

### 2) v1 прямо оптимизирует throughput pre-push

v1 вводит `changed_files_any` и жёстко требует прокидывать список изменённых файлов из pre-push, чтобы тяжёлые проверки (QC и т.п.) запускались **только когда это оправдано**.【36:5†agent-task-v1.md†L45-L50】

Это — чистытки умирает не от отсутствия правил, а от **дорогой/шумной обратной связи**. Быстрый цикл = меньше лишних прогонов.

В v2 эта оптимизация отсутствует как “первоклассная” часть дизайна (hook просто вызывает guards по фазе).【36:1†agent-task-v2.md†L33-L45】

### 3) v1 сI

В v1 guards реализуются отдельным модулем/CLI (`process_guards.py`), а не “разрастают” `process_compiler.py`.【36:13†agent-task-v1.md†L29-L39】

Для быстроно быстро править runner, формат репорта, семантику скипов/падений — не боясь задеть компилятор процесса (который уже используется).

---

## Где v2 может оказаться “быстрее” (но это другая скорость)

v2 делает ставку на **единый source of truth**: guards “формализованы в DDL”, единая команда `process_compiler guards`, и `advance` обязано блокироваться must-guards.【36:0†agent-task-v2.md†L18-L33】【36:2†agent-tньше файлов/мест, куда смотреть, и меньше шансов “забыть подключить guards” в каком-то сценарии.

Но цена:

* расширение DDL + модели + тесты компилятора;
* рост сложности “я хотел добавить один guard — тронул половину системы”.

Для ранней стадии (когда вы ещё нащупываете правильный набор гейтов) это часто **замедляет**, а не ускоряет.

---

## Что говорит harness engineering и как это мапится на выбор

Я бы вынес 3 “прикладных” принципа из статьи OpenAI и привязал их к решению:

### A) “Enforce invariants, not micromanage implementations”

OpenAI подчёркивают: документация сама по себе не удерживает систему цельной; нужно **механически enforce инварианты**, но не микроменеджить реализации. ([OpenAI][1])

**Вывод для вас:** и v1, и v2 подходят, но v1 легче начать с **малого набора “золотых” инвариантов** (tests pass, QC pass, branch выбран), не превращая DDL в комбайн.

### B) “Strict boundaries and predictable structure enable speed without decay”

В статье прямо говорится, что агенты эффективнее в среде со строгими границами и предсказуемой структурой, и что **ограничения — ранняя предпосылка скорости без дрейфа**. ([OpenAI][1])

**Вывод:** строгая граница “граф процесса” (DDL) полезна сама по себе. Встраивание guards в DDL эту границу размывает. Поэтому для “быстрого развития” (в смысле “не разнесло через 2 недели”) v1 мне кажется более устойчивым.

### C) “Entropy happens; encode golden principles”

OpenAI описывают дрейф/энтропию и то, что они начали **кодировать “golden principles” как механические правила** и регулярно чистить отклонения. ([OpenAI][1])

**Вывод:** вам важно, чтобы guards было:

* легко добавлять/менять,
* легко понимать,
* легко “убирать мусор” (устаревшие гейты).

Это снова толкает к v1 как к более дешёвому в эволюции.

---

## Мой практический вердикт

### Если цель: “запустить быстро и начать ускорять работу уже завтра”

**Берите v1** как базовый каркас. Он прямо заточен под минимальную систему, быстрые итерации и оптимизацию pre-push через changed-files.【36:5†agent-task-v1.md†L29-L50】

### Если цель: “жёсткая консистентность и один файл-истина даже ценой сложности”

Тогда v2 может быть оправдан, но я бы выбирал его **позже**, клся.

---

## Что стоит позаимствовать из v2, не переходя на v2 полностью

Вот набор “самых окупаемых” идей v2, которые реально усиливают v1 и соответствуют harness-подходу:

### 1) `must|should` + `--strict` режим

В v2 это формализовано как `level: must|should` и `--strict`, превращающий should в must.【36:3†agent-task-v2.md†L7-L16】【36:2†agent-task-v2.md†L23-L30】

**Почему это ускоряет:** на раннем этапе вы почти всегда хотите вводить новые правила как “should” (не блокируют)сделать “must”. Это снижает трение и флейк-страдания.

> В терминах v1 это можно сделать как расширение `severity: warn|error` + флаг “treat_warn_as_error”.

### 2) Тэмплейтинг путей/команд из state (`state.memory`)

В v2 подробно описан `.format_map()` с `{branch}`, `{current_step}`, `{iteration}`, и ключами `state.memory` вроде `{adr_path}`.【36:3†agent-task-v2.md†L24-L34】

**Почему это ускоряет:** вы перестаёте “зашивать” конкретные пути в guards и можете делать правила вроде “ADR должен существовать по пути, котоy”. Это делает процесс более **agent-legible** и уменьшает ручную склейку.

Но: я бы внедрял это аккуратно (только для `file_exists`/`command`), и делал ошибки плейсхолдеров максимально понятными (v2 тоже требует fail с понятным сообщением).【36:2†agent-task-v2.md†L1-L7】

### 3) `markdown_checklist` как guard-тип (когда дорастёте)

v2 предлагает guard, который проверяет чеклист/сайн-офф в `docs/iterations/.../reviewL66-L73】

Это очень в духе идеи “repo knowledge as system of record” и механической проверяемости знания (а не “где-то в голове/в чате”). ([OpenAI][1])л после того, как базовые command/file guards уже живут и не бесят.

### 4) `--json` вывод

v2 предлагает `--json` для машинного потребления (CI/боты).【36:2†agent-task-v2.md†L61-L64】

Если у вас есть агенты/автоматизация, это ускоряет разбор результатов и позволяет делать умные реакции (например: “покажи remediation только для упавших must”).

### 5) Интеграция guards сциплина

v2 делает блокировку `advance`, если must-guards не прошли, и добавляет bypass флаг (`--no-guards/--force`).【36:2†agent-task-v2.md†L33-L41】

В v1 это уже предусмотрено как “очень желательная связка” через контекст `advance`.【36:5†agent-task-v1.md†L29-L31】 Я бы просто **сделал это обязательной практикой**, даже оставаясь в арфайлом).

---

## Итог: “лучшее из двух” для быстрого развития

Если собрать в одну фектуру хранения и развязки** (DDL отдельно, guards отдельно; отдельный runner; changed-files оптимизация).【36:5†agent-task-v1.md†L11-L16】【36:5†agent-task-v1.md†L45-L50】

* **Берём из v2 3–5 фич, которые усиливают feedback loops без усложнения ядра**:
  `must/should + --strict`, минимальный templating из state, `--json`, и “md†L23-L41】【36:3†agent-task-v2.md†L24-L34】

Так вы получите **быстрый старт + контролируемую эволюцию**, что очень созвучно тому, как OpenAI описывает harness engineering: строить среду/обратные связиобы скорость не превращалась в энтропию. ([OpenAI][1])

[1]: https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"

</agent-task-analysis>

<deep-research-report>

# Programmatic state and transition management for AI agents in 2025–2026

## Problem framing and what “state” means in your example

Your “work3” example is less about “chat memory” and more about **a durable, programmatically-controlled execution process**: an agent enters a well-defined stage, initializes stage-specific state on first entry, mutates that state over time, and then performs an explicit transition (e.g., “ready to merge to main”) with cleanup (“delete work3”). This is the same core problem that workflow engines and state-machine orchestration libraries have solved for years—now reappearing in the “agentic” world because LLMs make control-flow more dynamic and tool calls more failure-prone. citeturn1search23turn3search0turn3search1

A useful way to decompose “state” for agentic systems (and to map directly to your “work3” branch analogy) is:

- **Workflow/process state**: “Which step/stage am I in, what are the guard conditions to move, what is the next step?” This is what makes transitions explicit and machine-checkable. citeturn1search23turn3search12turn1search5  
- **Execution history / audit trail**: “What happened, in what order, and what exactly was decided?” This is what lets the agent (or an operator) answer “what’s going on?” in a couple of commands—by querying history snapshots or an event log. citeturn3search1turn7search0turn7search9  
- **Working memory / knowledge memory**: facts and summaries carried across steps (short-term) or across runs (long-term). This is helpful, but by itself rarely guarantees correct transitions or resumability after failure. citeturn7search24turn2search2turn1search11  
- **Artifact state**: files, patches, test outputs, PRs/branches—i.e., the concrete objects produced while “work3” is active. In software engineering workflows, Git and PR tooling often become the artifact state store. citeturn1search10turn1search30turn1search22  

The recent popularity of “agents that actually do things” (for example OpenClaw) is one reason this topic is becoming urgent: these systems commonly need to pause, resume, branch, and keep careful track of tool outputs, credentials, and decisions. citeturn6news35turn6search0turn6search6

## Explicit state-machine and graph workflow orchestrators

A major cluster of “stateful agent” projects solves your exact concern—**programmatic transitions plus persistent state**—by modeling execution as a **graph/state machine** where a **state object** is carried across nodes/steps and can be checkpointed.

### LangGraph-style checkpointed state graphs

LangGraph describes itself as orchestration for long-running, stateful agents, and its core mechanism for “state” is a **persistence layer** implemented via **checkpointers**. When configured, the checkpointer saves a checkpoint of graph state at every “super-step,” storing checkpoints under a “thread” concept so you can access state after execution. This directly enables features like **human-in-the-loop**, **fault tolerance**, and **time travel** (forking from prior checkpoints). citeturn0search13turn3search0turn3search13

Two details are especially relevant to your “work3 creates state on first entry, persists through the stage” requirement:

- **Interrupt/pause semantics**: execution can pause at defined points, save state, and wait indefinitely until resumed—making “stage gates” a first-class construct rather than ad hoc “if” statements. citeturn3search7turn3search0turn3search21  
- **Queryable history**: you can retrieve full state history for a thread via `get_state_history`, which returns ordered snapshots (practically: “show me what’s going on” as a simple query). citeturn7search0turn7search8turn3search13  

LangGraph’s ecosystem increasingly treats “state” as something you can persist in standard backends (e.g., Redis integrations for checkpoint persistence, or other external stores), which matters if you want state survivable across deploys and crashes. citeturn0search17turn3search5turn3search30

### Microsoft Agent Framework workflows and sessions

Microsoft’s newer Agent Framework explicitly positions **Workflows** as graph-based orchestration with **type-safe routing**, **checkpointing**, and human-in-the-loop support, and combines this with **session-based state management** and observability. citeturn3search2turn2search30turn7search23

The “session” concept is very close to what you describe as “work3 state that appears on first entry”: when a workflow is converted into an agent, the framework creates a **session to manage conversation state and checkpoints**, routes input messages through the start executor, and translates workflow events into agent responses. citeturn3search16turn3search2turn3search12

This is also part of a broader shift in the Microsoft stack: the migration materials emphasize that Agent Framework centers on a typed, graph-based workflow model compared to message-centric orchestration in earlier AutoGen patterns. citeturn2search1turn0search7turn2search30

### Cloud state machines as explicit orchestration

If you want transitions to be *not just programmatic, but also auditable and visually inspectable*, cloud workflow services like AWS Step Functions remain relevant. Amazon explicitly frames Step Functions as a coordinator for multi-step generative AI workflows (including parallelizing model calls and integrating RAG patterns). citeturn1search5turn1search12

This is often attractive for “agent + process” systems because Step Functions state machines force you to name states and transitions, which creates built-in clarity (“what step are we in?”) even if the agent’s internal reasoning is messy. citeturn1search12turn1search5

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["LangGraph checkpointing state graph diagram","Microsoft Agent Framework workflow graph diagram","AWS Step Functions state machine diagram","Temporal event history workflow diagram"],"num_per_query":1}

## Durable execution engines as the “state layer” for agents

A second cluster of projects approaches your question from the opposite direction: instead of “agent framework adds state,” they say **state is an infrastructure primitive**. These systems typically provide a durable log/history, replay, retries, and long-lived pause/resume—so an agent becomes a workflow participant rather than the workflow runtime.

### Temporal: deterministic workflows + event history replay

Temporal’s model is built around **durable execution**: the system appends events to an **Event History** to track progress, enabling recovery after crashes and continuation without losing already-completed results. citeturn3search1turn7search9turn3search15

For agentic systems, Temporal emphasizes a key idea: when recovering from a crash, the workflow “replays” progress rather than asking the LLM to re-decide past decisions; the workflow uses Event History as a record of what already occurred, enabling the agent to resume exactly where it left off. citeturn3search4turn3search1turn7search13

Temporal also has a strong answer to your “a couple of commands to understand what’s going on” requirement:

- It treats a workflow like a **stateful service** that can receive messages (Queries, Signals, Updates), where Queries are used to read state and Signals/Updates can change behavior. citeturn7search2turn7search10turn7search25  
- Its documentation and messaging model explicitly connect “workflow state” to replayed history: query results should be based on deterministic replay of completed steps. citeturn7search17turn3search15turn7search9  

Several agent-focused integrations show how Temporal is being positioned as a practical “agent state engine.” For example, PydanticAI documents a `TemporalAgent` wrapper where I/O work (model requests, tool calls) is offloaded to activities while deterministic workflow code remains replayable. citeturn3search6turn3search23turn7search2

### Restate, DBOS, Resonate, Inngest: durable execution becomes a commodity

A notable 2024–2026 trend is the rise of multiple “durable execution” platforms beyond Temporal, explicitly marketing themselves as state/transition primitives for workflows and agents:

- **Restate** frames durable execution as a way to implement consistent state machines, session state, or agent context/memory; it emphasizes that state updates are journaled alongside execution steps and are scoped per workflow/object with a single-writer guarantee. citeturn4search0turn4search6turn4search4  
- **DBOS** documents a workflow model where interrupted execution is recovered from the last completed step, aiming to simplify resilient background tasks and AI agents. citeturn4search11  
- **Resonate** documents checkpoint/replay as the mechanism for durable execution (resume after the host process crashes/restarts). citeturn4search9turn4search24turn4search12  
- **Inngest** presents “durable functions” that replace queues/state management/scheduling; its multi-step functions support waits (hours to up to a year), step-level retries, and conditional execution, and it treats steps as discrete units that can be retried/debugged/recovered. It also uses step IDs specifically to memoize step state across versions. citeturn5search17turn5search5turn5search11turn5search13  

This category directly matches your intuition: if transitions and state are handled by a durable execution engine, an agent can be “aware” of where it is by reading the authoritative workflow state/history rather than reconstructing the world from chat logs.

A real tradeoff is that replay-based durability imposes constraints (e.g., deterministic workflow logic and careful handling of non-deterministic operations), which these engines address via patterns like isolating I/O into “activities/steps.” citeturn3search15turn4search4turn3search23

## In-framework “Flows/Workflows” with persisted context

A third cluster sits between “agent frameworks” and “workflow engines”: frameworks that explicitly add workflow state, persistence, and pause/resume inside the framework itself.

### LlamaIndex Workflows: Context as state across steps and runs

LlamaIndex Workflows uses a `Context` object to maintain state within and between runs. Their documentation shows that you can create a Context for a workflow, pass it into `.run()`, and optionally save and restore it for persistence across runs. citeturn1search4turn1search11turn1search27

This aligns closely with your “work3 state created on first entry” idea: a Context can serve as the container for stage-specific data, counters, partial outputs, and “done/not done” flags that survive across step boundaries (and potentially across executions). citeturn1search11turn1search4

### CrewAI Flows: explicit flow state + persistence decorator

CrewAI’s Flow documentation makes state management an explicit concept: Flow state is described as “the backbone” for sophisticated workflows, letting you maintain context and share data between steps. citeturn2search0turn2search11

Crucially for your question, CrewAI includes an explicit persistence mechanism via an `@persist` decorator, described as enabling automatic state persistence across restarts or different workflow executions. citeturn2search3turn2search0

CrewAI also distinguishes “process/workflow state” from “memory” in the classic sense: when memory is enabled, the crew automatically extracts facts from task outputs and stores them, then recalls relevant context before each task. citeturn2search2turn2search11

### AutoGen and lightweight orchestration: state often “spills into messages”

Microsoft AutoGen popularized multi-agent orchestration via message passing, but the project’s own discussions highlight a limitation: once you introduce retries, conditional paths, or long-running tasks, the “context” winds up scattered across exchanged messages and application logic rather than concentrated in a single, structured state object. citeturn0search7turn0search18

This is exactly why many teams gravitate toward graph/state-machine models (LangGraph-like or Agent-Framework-like) when they care about programmatic transitions and robust checkpointing. citeturn2search1turn3search0turn3search12

### OpenAI Swarm: teaches handoffs, but not “durable state”

OpenAI’s Swarm repository states its goal as lightweight, controllable, testable coordination via Agents and handoffs. citeturn2search6turn2search9  
However, community discussions around Swarm explicitly note it is (almost) entirely client-side and does not store persistent state between calls, reinforcing that Swarm is mainly educational rather than a “state engine.” citeturn2search25turn2search9

## Coding agents and Git-style “work states” mapped to branches and PRs

Your “work3 → merge to main → delete work3” is also a natural fit for **developer-facing agents**, where Git becomes a first-class “artifact state machine.”

### GitHub-native agents and PR workflows

GitHub’s documentation for its coding agent describes a workflow where the agent creates a new branch based on a base branch, then pushes changes into a pull request targeting that branch. citeturn1search10  
GitHub’s own blog positions this as operating “directly within the pull request workflow,” automating branch creation, commits, and reviews, with steps logged and visible—i.e., externalizing agent execution into a workflow artifact that humans can inspect. citeturn1search30

### OpenHands and SWE-agent class tools

OpenHands provides GitHub workflow guides (e.g., PR review automation). Its GitHub workflow examples explicitly rely on Actions permissions that allow creating and approving pull requests—turning the PR itself into the boundary between “work in progress” and “ready to merge.” citeturn1search0turn1search6turn1search21

SWE-agent similarly positions itself around taking an issue and producing a pull request; even in demo pipelines, “inference” creates a PR and later steps evaluate it. citeturn1search14turn1search22  
AWS sample work also documents “remote SWE agents” that autonomously create pull requests, showing how common “branch/PR as state” has become. citeturn1search26

### Branching strategies for multiple agents

Some vendors now document explicit branching strategies for parallel agent work, such as a rolling integration branch with sub-branches per agent, then PRs into the integration branch before merging to main—again reflecting “stateful staged work” as a Git-native process. citeturn1search33

## A concrete architecture pattern for “work3 state → merge → cleanup”

Below is an implementation pattern that appears repeatedly across the projects above, expressed in the vocabulary of your example. The key idea is: **the agent should not infer transitions**. Transitions are **code-defined**, with state stored in a system designed for resumability and auditability.

### Define state as a typed object, not “implicit context”

In graph/state-machine orchestrators, the “work3 state” is a structured object carried between steps (nodes/executors) and checkpointed. LangGraph’s persistence model centers on checkpointing graph state per thread, and its time-travel patterns explicitly rely on retrieving checkpoint and state history by `thread_id`. citeturn3search0turn7search0turn7search8  
Microsoft Agent Framework emphasizes type safety and validation in workflows, which is effectively the same recommendation: transitions should move typed messages/state along edges, not free-form blobs. citeturn3search12turn3search2

### Make “first entry creates state” an explicit transition (initialization step)

In practice, you model “enter work3” as a transition that:

1. Creates the workflow session/thread (or uses an existing one).
2. Initializes `work3` fields in state (e.g., branch name, baseline commit SHA, acceptance criteria).
3. Records the transition in history (checkpoint or event log).

This is natural in checkpointed state graphs (checkpoint on node entry/exit) citeturn3search0turn3search14 and in durable execution engines (append an event / journal step that becomes replayable ground truth). citeturn3search1turn4search6turn4search4

### Provide “status in two commands” via history queries, not log scraping

Two robust, widely-used mechanisms:

- **Checkpoint history listing** (graph systems): LangGraph explicitly provides `get_state_history` to list snapshots for a thread, and time travel uses that history to find checkpoint IDs. citeturn7search0turn7search8turn3search13  
- **Stateful workflow queries** (durable engines): Temporal treats workflows like stateful services with Queries/Signals/Updates, and it maintains Event History as the authoritative record used for replay and state reconstruction. citeturn7search2turn7search9turn7search25  

In other words, “status” should be a query endpoint over the authoritative state (plus optionally a short summary derived from the most recent checkpoints/events), not an LLM prompt that re-interprets raw logs.

### Gate merge/cleanup with explicit guard conditions and optional human approval

If “merge to main” is a transition, it should be guarded by checks (tests pass, lint pass, acceptance criteria satisfied). In durable engines, the pattern is to pause workflows for human approval and then resume exactly where they stopped; Temporal and related material present pause/resume as first-class for human-in-the-loop. citeturn1search28turn3search23turn3search7

Then “cleanup” (delete the work branch/workspace) becomes a final transition that is recorded, so the system can prove it happened (or retry it safely). This “record transitions so they can be retried without ambiguity” is one of the core reasons durable execution logs exist. citeturn3search1turn4search6turn4search12

### Security note: persistent state often contains credentials and tool authority

Because agent state can include API keys, auth tokens, tool permissions, and local execution context, security teams have started treating agent deployments as high-risk. CrowdStrike specifically frames OpenClaw deployments as a new attack surface requiring visibility into process execution and tool usage, and other reporting highlights corporate bans due to cybersecurity concerns. citeturn6search6turn6news38turn6news41  
This matters for your design because “state” is not just a convenience feature; it is also sensitive data that must be protected if you persist it.

## Open gaps and active research directions

Despite many engineering solutions, several gaps remain—especially around agents that *programmatically* understand and respect transitions:

A lively research direction is **generating state machines for multi-agent systems automatically**. The ICML 2025 poster “MetaAgent” proposes constructing multi-agent systems using finite state machines, where the FSM controls actions and state transitions, and reports improved performance versus other automated design methods. citeturn2search12

On the systems side, new work is targeting **agent serving runtimes** that separate workflow specification from execution while offering managed state layers. For example, the 2026 “Nalar” paper describes a serving framework with a managed state layer that decouples logical state from physical placement and supports safe reuse/migration and consistent retry behavior—essentially formalizing “state as a runtime service.” citeturn3academia37

Another emerging theme is **reproducibility constraints**: in workflow-heavy domains, researchers are explicitly pushing for structured action schemas, deterministic execution policies, and provenance tracking to make actions auditable and replayable (e.g., R-LAM). citeturn4academia40

Finally, durable workflows introduce a persistent engineering tension that is directly relevant to your “agent remembers work3” requirement: replay-based durability can create immutability/determinism constraints and requires careful handling of non-deterministic operations (LLM calls, HTTP, randomness). Durable execution platforms document these constraints and promote splitting workflow logic from side-effectful activities/steps to keep the system replayable. citeturn4search4turn3search15turn3search23

</deep-research-report>

<implementation-project-sdlc>

<directory_structure>
docs/
  _meta/
    pr-notes/
      index.md
    process/
      compiler.md
      sdlc-task-flow.ddl.yaml
      sdlc-task-flow.state.yaml
    JUST-COMMANDS.md
    PR-NOTES.md
    QC-STANDARD.md
    sdlc.md
  iterations/
    2026-02-mvp/
      01_vision.md
      04_architecture.md
      acceptance.md
      reviews.md
      traceability.md
scripts/
  print_project_state.py
src/
  paip/
    process_compiler.py
AGENTS.md
justfile
SDLC.md
</directory_structure>

<files>
This section contains the contents of the repository's files.

<file path="scripts/print_project_state.py">
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from paip.process_compiler import (
    ProcessDDL,
    ProcessState,
    load_process_ddl,
    load_process_state,
    validate_state_against_process,
)

CHECKBOX_RE = re.compile(r"^- \[(?P<mark>[xX ])\]\s+")
SIGNOFF_RE = re.compile(r"^Sign-off:\s*(?P<who>.+?)\s+Date:\s*(?P<date>\d{4}-\d{2}-\d{2})\s*$")
REQ_ID_RE = re.compile(r"\b(?:US|UC|NFR)-\d+\b")
AT_ID_RE = re.compile(r"\bAT-\d+\b")


@dataclass
class ChecklistSection:
    title: str
    checked: int = 0
    total: int = 0
    signoff_who: str | None = None
    signoff_date: str | None = None

    @property
    def status(self) -> str:
        if self.total == 0:
            return "unknown"
        if self.checked == self.total:
            return "done"
        return "in_progress"


@dataclass
class TestResult:
    ok: bool
    summary: str
    output: str


def _run(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=False,
    )


def _git_branch(root: Path) -> str:
    proc = _run(root, "git", "rev-parse", "--abbrev-ref", "HEAD")
    if proc.returncode == 0:
        value = proc.stdout.strip()
        if value:
            return value
    return "unknown"


def _git_commit(root: Path) -> str:
    proc = _run(root, "git", "rev-parse", "--short", "HEAD")
    if proc.returncode == 0:
        value = proc.stdout.strip()
        if value:
            return value
    return "unknown"


def _git_status_lines(root: Path) -> list[str]:
    proc = _run(root, "git", "status", "--short")
    if proc.returncode != 0:
        return []
    return [line for line in proc.stdout.splitlines() if line.strip()]


def _detect_iteration(iterations_root: Path) -> tuple[str | None, list[str]]:
    candidates = sorted(
        path.name
        for path in iterations_root.iterdir()
        if path.is_dir() and not path.name.startswith(".") and not path.name.startswith("_")
    )
    if not candidates:
        return None, []
    if len(candidates) == 1:
        return candidates[0], candidates
    return candidates[-1], candidates


def _parse_checklists(reviews_path: Path) -> dict[str, ChecklistSection]:
    if not reviews_path.exists():
        return {}

    sections: dict[str, ChecklistSection] = {}
    current: ChecklistSection | None = None

    for raw in reviews_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            title = line[3:].strip()
            current = ChecklistSection(title=title)
            sections[title] = current
            continue

        if current is None:
            continue

        checkbox = CHECKBOX_RE.match(line)
        if checkbox:
            current.total += 1
            if checkbox.group("mark").lower() == "x":
                current.checked += 1
            continue

        signoff = SIGNOFF_RE.match(line)
        if signoff:
            current.signoff_who = signoff.group("who").strip()
            current.signoff_date = signoff.group("date").strip()

    return sections


def _parse_selected_requirements(vision_path: Path) -> list[str]:
    if not vision_path.exists():
        return []

    lines = vision_path.read_text(encoding="utf-8").splitlines()
    selected: list[str] = []
    collecting = False

    for raw in lines:
        line = raw.strip()
        if line == "### Selected Requirements":
            collecting = True
            continue
        if collecting and line.startswith("### "):
            break
        if collecting and line.startswith("- "):
            for token in REQ_ID_RE.findall(line):
                selected.append(token)

    return sorted(set(selected))


def _parse_acceptance_ids(acceptance_path: Path) -> list[str]:
    if not acceptance_path.exists():
        return []
    ids: list[str] = []
    for raw in acceptance_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        ids.extend(AT_ID_RE.findall(line))
    return sorted(set(ids))


def _parse_traceability_requirements(traceability_path: Path) -> list[str]:
    if not traceability_path.exists():
        return []
    requirements: list[str] = []
    for raw in traceability_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if not parts:
            continue
        first = parts[0]
        if first in {"Requirement", "---"}:
            continue
        if first.startswith("---"):
            continue
        if first:
            requirements.append(first)
    return requirements


def _summarize_test_output(output: str) -> str:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if not lines:
        return "no output"
    for line in reversed(lines):
        lowered = line.lower()
        if "passed" in lowered or "failed" in lowered or "error" in lowered:
            return line
    return lines[-1]


def _run_tests(root: Path) -> TestResult:
    proc = _run(root, "just", "test")
    output = (proc.stdout + ("\n" if proc.stdout and proc.stderr else "") + proc.stderr).strip()
    summary = _summarize_test_output(output)
    return TestResult(ok=proc.returncode == 0, summary=summary, output=output)


def _project_path(ddl: ProcessDDL, state: ProcessState, *, max_hops: int = 32) -> tuple[list[str], str]:
    current = state.current_step
    path: list[str] = [current]
    seen: set[str] = set()

    for _ in range(max_hops):
        step = ddl.steps[current]
        if step.type == "terminal":
            return path, "done"
        transitions = step.transitions
        if not transitions:
            return path, "blocked:no_transitions"

        if step.type == "gate":
            if not state.branch:
                return path, "blocked:branch_required"
            matches = [item for item in transitions if item.label == state.branch]
            if len(matches) != 1:
                return path, f"blocked:branch_{state.branch}_is_ambiguous"
            next_step = matches[0].to
        elif len(transitions) == 1:
            next_step = transitions[0].to
        else:
            return path, "blocked:multiple_transitions_require_explicit_to"

        if next_step in seen:
            path.append(next_step)
            return path, "blocked:cycle_detected"
        seen.add(current)
        path.append(next_step)
        current = next_step

    return path, "blocked:max_hops_exceeded"


def _print_repo_summary(root: Path) -> None:
    branch = _git_branch(root)
    commit = _git_commit(root)
    status_lines = _git_status_lines(root)

    print("== Repository")
    print(f"- root: {root}")
    print(f"- branch: {branch}")
    print(f"- commit: {commit}")
    if status_lines:
        print(f"- working_tree: dirty ({len(status_lines)} changed paths)")
        for line in status_lines[:10]:
            print(f"  {line}")
        if len(status_lines) > 10:
            print(f"  ... and {len(status_lines) - 10} more")
    else:
        print("- working_tree: clean")


def _print_iteration_summary(root: Path, iteration_id: str) -> None:
    iteration_root = root / "docs" / "iterations" / iteration_id
    reviews_path = iteration_root / "reviews.md"
    vision_path = iteration_root / "01_vision.md"
    acceptance_path = iteration_root / "acceptance.md"
    traceability_path = iteration_root / "traceability.md"

    sections = _parse_checklists(reviews_path)
    selected_requirements = _parse_selected_requirements(vision_path)
    acceptance_ids = _parse_acceptance_ids(acceptance_path)
    traceability_reqs = _parse_traceability_requirements(traceability_path)

    print("== Iteration SDLC Snapshot")
    print(f"- current_iteration: {iteration_id}")
    if selected_requirements:
        print(f"- selected_requirements ({len(selected_requirements)}): {', '.join(selected_requirements)}")
    else:
        print("- selected_requirements: not found")

    if acceptance_ids:
        print(f"- acceptance_ids ({len(acceptance_ids)}): {', '.join(acceptance_ids)}")
    else:
        print("- acceptance_ids: not found")

    if traceability_reqs:
        print(f"- traceability_requirements ({len(traceability_reqs)}): {', '.join(traceability_reqs)}")
    else:
        print("- traceability_requirements: not found")

    for title in (
        "Requirements Baseline (Design Input)",
        "Design Baseline (Design Output)",
        "Validation Baseline",
    ):
        section = sections.get(title)
        if section is None:
            print(f"- {title}: missing")
            continue
        signoff = f"{section.signoff_who} on {section.signoff_date}" if section.signoff_who else "n/a"
        print(
            f"- {title}: {section.status} ({section.checked}/{section.total} checklist items), sign-off={signoff}"
        )


def _print_process_state(ddl: ProcessDDL, state: ProcessState, state_path: Path) -> None:
    current = ddl.steps[state.current_step]
    projected_path, projection_status = _project_path(ddl, state)

    print("== Task State Machine")
    print(f"- process: {ddl.process_id}@v{ddl.version}")
    print(f"- state_file: {state_path}")
    print(f"- task: {state.task}")
    print(f"- current_step: {state.current_step} (type={current.type})")
    print(f"- status: {state.status}")
    print(f"- branch: {state.branch or 'n/a'}")
    next_gate = state.memory.get("next_gate")
    print(f"- memory.next_gate: {next_gate or 'n/a'}")

    if state.history:
        last = state.history[-1]
        print(f"- last_transition: step={last.step}, at={last.at}, reason={last.reason}")
    else:
        print("- last_transition: n/a")

    if current.transitions:
        print("- next_transitions:")
        for item in current.transitions:
            label = item.label if item.label is not None else "-"
            desc = item.description or "-"
            print(f"  - to={item.to}, label={label}, description={desc}")
    else:
        print("- next_transitions: none (terminal)")

    print(f"- projected_path_for_current_branch: {' -> '.join(projected_path)}")
    print(f"- projection_status: {projection_status}")

    initial = ddl.steps.get(ddl.initial_step)
    if initial is not None and initial.type == "gate":
        print(f"- initial_gate({ddl.initial_step}) options:")
        for item in initial.transitions:
            label = item.label if item.label is not None else "-"
            desc = item.description or "-"
            print(f"  - {label}: {item.to} ({desc})")

    print(
        "- note: docs/_meta/process/sdlc-task-flow.state.yaml documented as an example file; "
        "confirm team convention before treating it as the only runtime source."
    )


def _print_next_actions(state: ProcessState) -> None:
    print("== Recommended First Actions")
    print("1. Run `just print-project-state` at task start to synchronize SDLC context and state machine.")
    print("2. Confirm scope branch (A/B/C) before code changes and reflect it in task state.")

    if state.branch == "B":
        print(
            "3. Branch B selected: review `docs/_meta/QC-STANDARD.md` and include Query Catalog validation in plan."
        )
    elif state.branch == "C":
        print("3. Branch C selected: prepare ADR update before changing public contracts or architecture.")
    elif state.branch == "A":
        print("3. Branch A selected: keep changes code-only, avoid DB/query/contract changes.")
    else:
        print("3. Branch is not set: choose A/B/C at scope gate to avoid ambiguous transitions.")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print project SDLC context, current process state, and readiness checks."
    )
    parser.add_argument("--root", default=".", help="Repository root (default: current directory).")
    parser.add_argument(
        "--ddl",
        default="docs/_meta/process/sdlc-task-flow.ddl.yaml",
        help="Path to process DDL file.",
    )
    parser.add_argument(
        "--state",
        default="docs/_meta/process/sdlc-task-flow.state.yaml",
        help="Path to process state file.",
    )
    parser.add_argument(
        "--iterations-root",
        default="docs/iterations",
        help="Path to iterations root folder.",
    )
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="Skip `just test` execution.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    root = Path(args.root).resolve()
    ddl_path = (root / args.ddl).resolve()
    state_path = (root / args.state).resolve()
    iterations_root = (root / args.iterations_root).resolve()

    print("PAIP Project State")
    print(f"generated_at_utc: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}")
    print()

    _print_repo_summary(root)
    print()

    if not iterations_root.exists():
        print("== Iteration SDLC Snapshot")
        print(f"- ERROR: iterations root not found: {iterations_root}")
        return 1

    current_iteration, all_iterations = _detect_iteration(iterations_root)
    if current_iteration is None:
        print("== Iteration SDLC Snapshot")
        print(f"- ERROR: no iteration directories found under {iterations_root}")
        return 1

    print("== Iteration Discovery")
    print(f"- discovered_iterations ({len(all_iterations)}): {', '.join(all_iterations)}")
    print(f"- selected_iteration: {current_iteration}")
    print()

    _print_iteration_summary(root, current_iteration)
    print()

    if not ddl_path.exists():
        print("== Task State Machine")
        print(f"- ERROR: DDL file not found: {ddl_path}")
        return 1
    if not state_path.exists():
        print("== Task State Machine")
        print(f"- ERROR: state file not found: {state_path}")
        return 1

    ddl = load_process_ddl(ddl_path)
    state = load_process_state(state_path)
    validate_state_against_process(state, ddl)
    _print_process_state(ddl, state, state_path)
    print()

    failed = False
    if args.skip_tests:
        print("== Health Checks")
        print("- just test: skipped (--skip-tests)")
    else:
        test_result = _run_tests(root)
        print("== Health Checks")
        if test_result.ok:
            print(f"- just test: PASS ({test_result.summary})")
        else:
            failed = True
            print(f"- just test: FAIL ({test_result.summary})")
            print("- test_output:")
            for line in test_result.output.splitlines()[-20:]:
                print(f"  {line}")
    print()

    _print_next_actions(state)
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
</file>

<file path="docs/_meta/process/compiler.md">
# Process Compiler (DDL -> Runtime State)

This tool compiles a process graph from DDL and keeps runtime state in a YAML file.

Implementation:
- Module: `src/paip/process_compiler.py`
- DDL example: `docs/_meta/process/sdlc-task-flow.ddl.yaml`
- State example: `docs/_meta/process/sdlc-task-flow.state.yaml`

## DDL format

Required root fields:
- `process_id`
- `version`
- `initial_step`
- `steps` (map of step ids)

Step fields:
- `type`: `gate` | `action` | `terminal`
- `title`
- `transitions`: list of `{to, label?, description?}`

Validation done by compiler:
- `initial_step` exists.
- all transition targets exist.
- all steps are reachable from `initial_step`.
- at least one `terminal` exists.
- terminal steps have no outgoing transitions.

## State format

Required fields:
- `process_id`
- `version`
- `task`
- `current_step`

Optional fields:
- `status`: `in_progress|blocked|done`
- `branch` (used by `gate` transitions)
- `memory` (free-form map)
- `history[]` with `{step, at, reason}`

## CLI usage

Compile DDL to graph artifact:

```bash
python -m paip.process_compiler compile \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --out tmp/sdlc-task-flow.compiled.yaml
```

Initialize state:

```bash
python -m paip.process_compiler init \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state tmp/sdlc-task-flow.state.yaml \
  --task "Add web concept/domain extraction tool" \
  --branch B
```

Advance state:

```bash
python -m paip.process_compiler advance \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state tmp/sdlc-task-flow.state.yaml \
  --reason "Scope gate selected"
```

Show current state and next transitions:

```bash
python -m paip.process_compiler show \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state tmp/sdlc-task-flow.state.yaml
```

## Notes

- Files use YAML with JSON-compatible syntax, so the tool works without extra dependencies.
- If `PyYAML` is installed, regular YAML syntax is also supported.
</file>

<file path="docs/_meta/process/sdlc-task-flow.ddl.yaml">
{
  "process_id": "sdlc_task_flow",
  "version": 1,
  "initial_step": "scope_gate",
  "steps": {
    "scope_gate": {
      "type": "gate",
      "title": "Scope Gate",
      "transitions": [
        {
          "to": "code_only_path",
          "label": "A",
          "description": "Code-only changes, no DB/query changes"
        },
        {
          "to": "data_access_path",
          "label": "B",
          "description": "DB/query changes require Query Catalog updates"
        },
        {
          "to": "architecture_contract_path",
          "label": "C",
          "description": "Public contract/architecture changes require ADR"
        }
      ]
    },
    "code_only_path": {
      "type": "action",
      "title": "Code and tests updates",
      "transitions": [
        {
          "to": "validation_gate",
          "description": "Run tests and collect evidence"
        }
      ]
    },
    "data_access_path": {
      "type": "action",
      "title": "Data-access updates",
      "transitions": [
        {
          "to": "query_catalog_gate",
          "description": "Run Query Catalog validation"
        }
      ]
    },
    "query_catalog_gate": {
      "type": "action",
      "title": "Query Catalog validation",
      "transitions": [
        {
          "to": "validation_gate",
          "description": "Proceed after QC validation"
        }
      ]
    },
    "architecture_contract_path": {
      "type": "action",
      "title": "Architecture and contract updates",
      "transitions": [
        {
          "to": "adr_gate",
          "description": "Add ADR and refresh iteration docs"
        }
      ]
    },
    "adr_gate": {
      "type": "action",
      "title": "ADR review gate",
      "transitions": [
        {
          "to": "validation_gate",
          "description": "Proceed after ADR review"
        }
      ]
    },
    "validation_gate": {
      "type": "terminal",
      "title": "Validation complete",
      "transitions": []
    }
  }
}
</file>

<file path="docs/_meta/process/sdlc-task-flow.state.yaml">
{
  "process_id": "sdlc_task_flow",
  "version": 1,
  "task": "Add web concept/domain extraction tool",
  "current_step": "scope_gate",
  "status": "in_progress",
  "branch": "B",
  "memory": {
    "context_files": [
      "AGENTS.md",
      "SDLC.md",
      "docs/_meta/QC-STANDARD.md",
      "src/paip/extractors.py",
      "src/paip/pipeline.py"
    ],
    "next_gate": "requirements"
  },
  "history": [
    {
      "step": "scope_gate",
      "at": "2026-02-19T00:00:00+00:00",
      "reason": "init"
    }
  ]
}
</file>

<file path="docs/_meta/JUST-COMMANDS.md">
# Just Command Reference

Source of truth for command behavior: `justfile`.

This page documents each `just` recipe with quick input/output contracts so it is clear what each command expects and returns.

## Conventions

- `just` loads variables from shell and `.env` (`set dotenv-load := true`).
- Most commands assume virtualenv already exists (`just setup`).
- Non-zero exit code means command failed and should be treated as blocking for CI/process.

## Recipes

### `just help`
- Input: no arguments.
- Output: prints available recipe names (equivalent to `just --list`).
- Side effects: none.

### `just setup`
- Input: no arguments.
- Output: creates `.venv` and installs project in editable mode with dev extras.
- Side effects: writes `.venv/` and installs Python dependencies.

### `just test`
- Input: no arguments.
- Output: runs `pytest -q` and prints test summary (`passed/failed`).
- Side effects: reads tests and may create local pytest cache.

### `just print-project-state`
- Input: no required arguments; optional env `PAIP_SKIP_TESTS=1` to skip running tests in this report.
- Output: prints consolidated project state snapshot:
  repository status, discovered iteration + baseline checklist state, SDLC process state machine context (current step/branch/next transitions/projection), and health-check summary.
- Side effects: runs `just test` by default (unless `PAIP_SKIP_TESTS=1`), so it executes the project test suite.

### `just qc-setup`
- Input: no arguments.
- Output: installs Query Catalog validator dependencies from `query-catalog/requirements-qc.txt`.
- Side effects: updates packages in `.venv`.

### `just qc-validate`
- Input: no arguments.
- Output: validates Query Catalog (`query-catalog/query-catalog.yaml`) against policy/template and prints `OK` or `ERROR`.
- Side effects: none (read-only validation).

### `just qc-validate-ci`
- Input: no arguments.
- Output: runs CI-equivalent QC validation flow and prints full validator output.
- Side effects: may install/confirm QC dependencies in `.venv`.

### `just hooks-install`
- Input: no arguments.
- Output: configures git hooks path and makes pre-push hook executable.
- Side effects: writes git config `core.hooksPath=.githooks`; changes file mode for `.githooks/pre-push`.

### `just notes-list`
- Input: no arguments.
- Output: lists git notes from `refs/notes/commits` as `<note_object_sha> <commit_sha>`.
- Side effects: none.

### `just notes-show SHA`
- Input: required `SHA` (commit hash that has a note).
- Output: prints markdown body of note attached to that commit.
- Side effects: none.

### `just notes-push REMOTE='origin'`
- Input: optional `REMOTE` (default `origin`).
- Output: pushes `refs/notes/commits` to selected remote.
- Side effects: updates remote notes ref.

### `just notes-registry-refresh`
- Input: no arguments.
- Output: regenerates markdown registry from git notes:
  `docs/_meta/pr-notes/index.md` and `docs/_meta/pr-notes/notes/*.md`.
- Side effects: rewrites generated files in `docs/_meta/pr-notes/`.

### `just notes-registry-lint`
- Input: no arguments.
- Output: checks consistency between `refs/notes/commits` and `docs/_meta/pr-notes/*`; prints `OK` or `ERROR`.
- Side effects: none (read-only).

### `just readme-links-check FILE='README.md'`
- Input: optional `FILE` (default `README.md`).
- Output: validates local markdown/map-first links and prints validation summary.
- Side effects: none (read-only).

### `just just-docs-check FILE='docs/_meta/JUST-COMMANDS.md'`
- Input: optional `FILE` path to command reference markdown.
- Output: verifies every recipe in `justfile` has a matching section with `Input/Output`; prints `OK` or `ERROR`.
- Side effects: none (read-only).

### `just monitor-add TITLE CITY TOPIC QUERY INTERVAL_MIN CHAT_ID`
- Input: required positional args:
  `TITLE`, `CITY`, `TOPIC`, `QUERY`, `INTERVAL_MIN`, `CHAT_ID`.
- Output: creates monitor and prints `Created monitor id=<id>`.
- Side effects: inserts row into monitors table in configured DB.

### `just monitor-list`
- Input: no arguments.
- Output: prints monitor rows (`id/title/city/topic/interval/enabled`) or `No monitors`.
- Side effects: none (read-only DB query).

### `just run-once MONITOR_ID`
- Input: required `MONITOR_ID`.
- Output: runs one pipeline iteration and prints JSON run result.
- Side effects: executes full pipeline (DB writes, network calls, optional Telegram send).

### `just run-scheduler`
- Input: no arguments.
- Output: starts blocking scheduler loop until interrupted.
- Side effects: repeatedly runs monitor pipelines by configured intervals.

### `just history MONITOR_ID LIMIT='20'`
- Input: required `MONITOR_ID`; optional `LIMIT` (default `20`).
- Output: prints notification/event history lines for monitor or `No history`.
- Side effects: none (read-only DB query).

### `just logs MONITOR_ID='1' LIMIT='20'`
- Input: optional `MONITOR_ID` (default `1`), optional `LIMIT` (default `20`).
- Output: same as `history` (alias to `paip history`), prints history lines.
- Side effects: none (read-only DB query).

### `just stats MONITOR_ID='1' LIMIT='10'`
- Input: optional `MONITOR_ID` (default `1`), optional `LIMIT` (default `10`), optional env `PAIP_DB_PATH`.
- Output: prints DB counters, recent runs/events/notifications for monitor.
- Side effects: none (read-only debug queries).

### `just telegram-preview MONITOR_ID='1' LIMIT='10' RUN_ID=''`
- Input: optional `MONITOR_ID`, `LIMIT`, optional `RUN_ID` (if empty, latest run with notifications is used).
- Output: prints rendered Telegram messages from stored notification payloads.
- Side effects: none (read-only debug queries).

### `just env-example`
- Input: no arguments.
- Output: prints required/optional environment variable template.
- Side effects: none.
</file>

<file path="docs/_meta/PR-NOTES.md">
# PR Notes

`git notes` are used to persist PR descriptions in markdown, bound to commit SHAs.

## Source of truth

- Git notes ref: `refs/notes/commits`
- Markdown registry index: `docs/_meta/pr-notes/index.md`
- One note per commit file: `docs/_meta/pr-notes/notes/<commit-sha>.md`

## Read notes

```bash
git notes show <sha>
git log --show-notes=commits --oneline -n 5
```

## Refresh markdown registry

```bash
just notes-registry-refresh
just notes-registry-lint
```

## Add/update a note

```bash
git notes add -f -F /tmp/pr_body.md <sha>
just notes-registry-refresh
```

## Push notes

```bash
git push <remote> refs/notes/commits:refs/notes/commits
```

When hooks are installed (`just hooks-install`), `pre-push` auto-syncs `refs/notes/commits` and blocks branch push if sync fails.

## Notes format

- Note body is free-form markdown.
- Registry keeps metadata and a file copy per commit for easy browsing.
</file>

<file path="docs/_meta/QC-STANDARD.md">
# STANDARD: Query Catalog / Query Registry

**Документ:** QC-STANDARD
**Версия:** 0.9 (Draft)
**Дата:** 2026‑02‑19
**Статус:** Черновик для внедрения и пилота
**Владельцы стандарта:** Архитектура / Платформенная команда (назначить)
**Область:** Backend‑сервисы, фоновые задачи, интеграции, которые обращаются к источникам данных
**Примечания:** Это черновик **STANDARD.md** в стиле “нормативного документа”: с областью применения, словарём, однозначными терминами, правилами уровня MUST/SHOULD/MAY, жизненным циклом, процессами и приложениями (шаблон записи, примеры, чек‑листы). Примечание о стиле: это именно “стандарт”, поэтому текст местами сухой и повторяет определения. Это нормально: цель — однозначность, проверяемость, пригодность для CI и для агента, который должен производить из него делать краткий `SKILL.md`.
---

## 0. Статус документа и правила чтения

### 0.1. Нормативная лексика

В документе используются слова **MUST / MUST NOT / SHOULD / SHOULD NOT / MAY** в нормативном смысле:

* **MUST / MUST NOT** — обязательное требование, нарушение считается дефектом процесса.
* **SHOULD / SHOULD NOT** — требование по умолчанию; отступление допускается при наличии обоснования и фиксации исключения.
* **MAY** — допустимая опция.

### 0.2. Что является “истиной”

* **Registry** (реестр) — **источник истины** в репозитории: машиночитаемые записи о запросах.
* **Catalog** (каталог) — человекочитаемое представление реестра: страницы/Markdown/сайт, генерируемые из Registry.

Если термины “Catalog” и “Registry” употребляются как синонимы, приоритет имеет смысл выше: **Registry = данные**, **Catalog = представление**.

---

## 1. Назначение

Query Catalog / Query Registry вводится, чтобы:

1. зафиксировать **полный перечень операций доступа к данным** (чтение/запись) в системе;
2. обеспечить однозначное понимание **что делает запрос** и **зачем** он существует;
3. дать трассируемость **use‑case → запрос → затронутые данные** (и, по возможности, к runtime‑трейсам);
4. повысить управляемость изменений схемы, производительности и безопасности.

---

## 2. Область применения и ограничения

### 2.1. Применяется к

Стандарт применяется ко всем компонентам, которые выполняют операции над данными:

* SQL БД (PostgreSQL/MySQL/…)
* NoSQL (MongoDB/…)
* поисковые хранилища (Elastic/…)
* кэши (Redis/…) — **если** через них читаются/пишутся бизнес‑значимые данные или кеш влияет на корректность

### 2.2. Не является целью (Non‑goals)

Стандарт **не** пытается:

* заменить документацию API;
* заменить описание модели данных (data dictionary / data catalog);
* регламентировать всю архитектуру домена;
* требовать описания каждой внутренней ORM‑операции, не влияющей на бизнес‑поведение.

### 2.3. Минимальная гранулярность

Записи в реестре должны соответствовать **операциям**, которые имеют самостоятельный смысл: “получить пользователя”, “создать заказ”, “списать баланс”.
Технические детали (например, “ORM сделал 3 запроса вместо 1”) относятся к оптимизации и наблюдаемости, но не обязаны становиться отдельными “Query ID”, если не меняют смысл.

---

## 3. Термины и определения

### 3.1. Основные термины

**Query (Запрос)**
Операция чтения/записи состояния из источника данных, выполняемая приложением, имеющая имя (Query ID) и контракт.

**Query ID**
Стабильный идентификатор запроса в рамках системы. Используется в реестре, документации, наблюдаемости и обсуждениях.

**Query Entry (Запись запроса)**
Структурированная запись в Registry, описывающая Query ID, назначение, контракт, затронутые данные, ограничения и жизненный цикл.

**Contract (Контракт запроса)**
Описание входных параметров, формы результата, кардинальности, сортировки/пагинации, ошибок и значимых гарантий.

**Cardinality (Кардинальность результата)**
Ожидаемое количество сущностей в результате: `1`, `0..1`, `0..N`, `1..N`.

**Use-case (Сценарий / прикладной кейс)**
Бизнес‑операция уровня приложения: “авторизоваться”, “оформить заказ”, “получить список транзакций”.

**Call site (Место вызова)**
Конкретная функция/метод/endpoint/job, откуда вызывается запрос.

**Repository method (Метод репозитория)**
Техническая точка доступа к данным в коде. Может соответствовать одному Query ID или агрегировать несколько запросов (см. “Composite operation”).

**Data source (Источник данных)**
Конкретное хранилище: `postgres.main`, `redis.cache`, `elastic.search` и т. п.

**Data objects (Объекты данных)**
Таблицы/коллекции/индексы/представления, затрагиваемые запросом.

**Hot path**
Путь исполнения, чувствительный к задержкам и частоте (например, синхронные API‑эндпоинты).

**Idempotency (Идемпотентность)**
Свойство операции: повторное выполнение с одинаковыми параметрами не меняет состояние сверх первого эффекта (или меняет предсказуемо и безопасно по правилам домена).

**PII (Персональные данные)**
Данные, позволяющие идентифицировать человека или относящиеся к нему по требованиям политики/закона.

**Tenant boundary (Граница арендатора)**
Гарантия, что данные разных арендаторов (клиентов) не смешиваются и недоступны друг другу.

**Observability correlation (Корреляция наблюдаемости)**
Связь между Query ID и runtime‑метриками/логами/трейсами (например, через теги в SQL‑комментариях, span attributes, лог‑поля).

### 3.2. Виды операций

**Read query**
Запрос, не изменяющий бизнес‑состояние (чтение).

**Write query**
Запрос, изменяющий бизнес‑состояние (запись).

**Composite operation**
Логическая операция, включающая несколько запросов (например, транзакция из нескольких statement’ов). Может иметь отдельный Query ID, если рассматривается как единый контракт.

---

## 4. Артефакты и требования к хранению

### 4.1. Registry MUST быть в репозитории

Registry MUST храниться в репозитории приложения/сервиса и версионироваться вместе с кодом.

### 4.2. Registry MUST быть машиночитаемым

Registry MUST иметь машиночитаемый формат: YAML/JSON/или иной формат, пригодный для валидации и генерации каталога.

Допустимы два варианта структуры:

* **Один файл на сервис**: `query-catalog.yaml`
* **Один файл на запрос**: `query-catalog/entries/<QueryID>.yaml`

Выбор фиксируется для репозитория и не меняется без ADR.

### 4.3. Catalog SHOULD генерироваться

Человекочитаемый каталог SHOULD генерироваться автоматически из Registry (Markdown/HTML). Ручная поддержка допускается только на пилоте.

---

## 5. Модель данных Registry

### 5.1. Обязательные поля (минимум)

Каждая запись Query Entry MUST содержать:

* `id` — Query ID
* `purpose` — назначение (1–3 предложения)
* `source` — источник данных
* `contract` — параметры и результат (включая кардинальность)
* `data_objects` — перечень затронутых объектов данных (read/write)
* `lifecycle.status` — состояние (active/deprecated/…)
* `owner` — владелец (команда/модуль)

### 5.2. Рекомендуемые поля

Каждая запись SHOULD содержать:

* `use_cases` или `call_sites` (хотя бы один)
* `security` (PII, tenant boundary, классификация)
* `consistency` (транзакционность, изоляция, идемпотентность)
* `performance` (ожидания, лимиты, требования к пагинации)
* `observability` (корреляция, метрики)

---

## 6. Нормативные требования (QC‑xx)

Ниже правила, подлежащие соблюдению. Для удобства они атомарны и имеют ID.

### QC‑01. Идентификатор Query ID

**Требование**

* Query ID MUST быть уникальным в рамках сервиса/системы (определить границу уникальности в разделе 9).
* Query ID MUST быть стабильным: после публикации в `active` он не переименовывается; при необходимости создаётся новый Query ID.
* Query ID SHOULD отражать доменную сущность и действие.

**Рекомендуемый формат**
`<DomainOrModule>.<Action>[.<Qualifier>]`

Примеры:

* `User.GetById`
* `Order.Create`
* `Ledger.PostTransfer`
* `Payment.ListForCustomer`
* `AuthSession.RevokeAll`

**Запрещено**

* технические имена вида `query1`, `getUsers2`
* имена, привязанные к структуре таблиц (`Users_SelectById`) — если это не оправдано контекстом

---

### QC‑02. Назначение (Purpose)

**Требование**

* `purpose` MUST объяснять смысл запроса на уровне системы: *что делает операция* и *зачем она нужна*.
* `purpose` MUST NOT повторять SQL/ORM‑формулировку (“делает SELECT из таблицы…”).

**Рекомендация**

* 1–3 коротких предложения, без воды.
* Допустимо указание сценария: “используется при …”.

---

### QC‑03. Контракт (Contract)

**Требование**
Контракт MUST включать:

1. параметры:

* имя, тип, обязательность;
* важные ограничения (диапазон, формат, допустимые значения).

2. результат:

* кардинальность (`0..1`, `0..N` и т. д.);
* форма результата (минимально: перечисление полей или ссылка на тип/DTO).

3. правила сортировки/пагинации:

* если возвращается список, MUST быть определён порядок (явный `order_by`) и стратегия пагинации.

4. ошибки/исключения:

* хотя бы на уровне категорий (например: “not_found”, “conflict”, “validation_failed”).

**Запрещено**

* “возвращает список” без лимита/пагинации для потенциально больших наборов данных (см. QC‑07).

---

### QC‑04. Затронутые данные (Data objects)

**Требование**

* Запись MUST перечислять затронутые объекты данных в разрезе чтения и записи:

  * `read`: таблицы/коллекции/индексы/представления
  * `write`: таблицы/коллекции/…
* Для composite‑операций MUST перечисляться все объекты, затронутые в рамках операции.

**Рекомендации**

* Если используется view/материализованное представление, указывать его как объект чтения.
* Если запрос зависит от конкретного индекса или constraint, это SHOULD быть отмечено в `performance` или `consistency`.

---

### QC‑05. Транзакционность, согласованность, идемпотентность

**Требование**
Каждая запись MUST указать:

* требуется ли транзакция: `required / optional / forbidden` (в зависимости от политики сервиса);
* идемпотентность: `true/false/conditional` и условия;
* для write‑операций SHOULD указать ожидаемое поведение при повторе/гонках.

**Рекомендации**

* Указывать уровень изоляции или блокировок только если это действительно значимо.
* Если операция может дедлокаться или конфликтовать по уникальности — отметить в `consistency`/`errors`.

---

### QC‑06. Безопасность и приватность

**Требование**
Каждая запись MUST иметь security‑раздел с минимумом:

* `pii: true/false` (или градацию, если принята);
* `tenant_boundary: enforced/not_applicable/unknown` (unknown запрещать после пилота);
* правила доступа: кто имеет право вызывать запрос (роль/контекст), если это применимо.

**Обязательные принципы**

* Запрос, читающий PII, MUST иметь явное указание на это.
* Для multi‑tenant систем запросы MUST подтверждать, как соблюдается граница арендатора (фильтр по tenant_id, row‑level security, отдельная БД и т. п.).

---

### QC‑07. Производительность и ограничения

**Требование**

* Любой запрос, возвращающий коллекцию, MUST иметь явный лимит и стратегию пагинации, если объём потенциально велик.
* Запросы hot path SHOULD иметь SLO/ожидания: “обычно < X мс при N‑объёме данных”.
* Для операций, способных сканировать большие объёмы, MUST быть явная отметка и условия безопасного использования.

**Запрещено (по умолчанию)**

* неограниченный список в синхронном API;
* сортировка без индекса на больших таблицах в hot path (допускается при ADR/исключении).

---

### QC‑08. Наблюдаемость и корреляция

**Требование**

* Query ID MUST быть доступен для корреляции с runtime‑наблюдаемостью хотя бы на уровне логов приложения (поле `query_id`).
* Для SQL источников SHOULD быть включена корреляция Query ID в SQL‑комментарии или в атрибутах trace span (если практикуется tracing).

**Рекомендации**

* Стандартизировать поля: `query_id`, `data_source`, `rows`, `duration_ms`, `error_code`.
* Для composite‑операций логировать как `operation_id`, а внутренние запросы — как `query_id` при наличии.

---

### QC‑09. Владение и ответственность

**Требование**

* У каждого Query Entry MUST быть `owner` (команда/модуль) и канал связи (например, GitHub team, группа, он‑колл).
* Владелец обязан:

  * отвечать за актуальность записи;
  * сопровождать изменения контракта и деприкации;
  * принимать решения по исключениям или эскалации.

---

### QC‑10. Жизненный цикл и совместимость

**Состояния**
`draft` → `active` → `deprecated` → `removed`

**Требования**

* Любой запрос MUST быть `draft` до первого слияния.
* `active` означает: контракт стабилен, запись полная по минимальным полям.
* `deprecated` MUST содержать:

  * причину деприкации,
  * ссылку на замену (replacement Query ID),
  * план удаления (дата/версия).
* `removed` означает, что запрос не используется и может быть удалён из кода и реестра (либо оставлен как историческая запись — политика выбирается отдельно).

**Правила изменения**

* Если меняется контракт результат/кардинальность/семантика — SHOULD создавать новый Query ID или версию (см. QC‑11), а старый депрекейтить.
* Мелкие изменения без влияния на контракт (например, оптимизация SQL) MAY не требовать нового Query ID, но SHOULD обновлять `performance`/`notes`.

---

### QC‑11. Версионирование контракта и правила “breaking change”

**Требование**
Сервис MUST определить одну из стратегий (зафиксировать в разделе 9 “Политики сервиса”):

**Стратегия A (рекомендуется): новый Query ID при breaking change**

* Breaking change → новый Query ID
* Старый → deprecated → removed

**Стратегия B: версия внутри Query ID**

* `id: User.GetById`, `contract.version: 2`
* Breaking change → bump version + миграционный план

**Определение breaking change**
Breaking change включает (не исчерпывающе):

* изменение кардинальности (`0..N` → `0..1`);
* изменение семантики фильтрации/доступа;
* изменение обязательности параметров;
* изменение состава результата так, что ломает потребителей (если потребители зависят от полей; определить политику).

---

### QC‑12. Тестирование и проверяемость

**Требование**

* Для write‑операций SHOULD быть тест, фиксирующий ключевую семантику и инварианты.
* Для запросов со сложной фильтрацией/сортировкой SHOULD быть тест на корректность.
* Для критичных запросов SHOULD быть нагрузочный/профилировочный сценарий (минимально — ручной профиль + план запроса), если команда практикует.

---

## 7. Процессы (Workflows)

### 7.1. Добавление нового запроса

Автор MUST:

1. выбрать/создать Query ID (QC‑01);
2. описать purpose и contract (QC‑02, QC‑03);
3. описать data_objects (QC‑04);
4. заполнить security/consistency/performance/observability по правилам (QC‑05..QC‑08);
5. добавить/обновить точки вызова (use_case / call_site) по выбранной политике;
6. обеспечить прохождение валидации Registry (CI‑гейт).

### 7.2. Изменение существующего запроса

Автор MUST:

* определить, является ли изменение breaking change (QC‑11);
* при необходимости создать новый Query ID/версию и запустить деприкацию (QC‑10);
* обновить contract/data_objects/performance/observability по факту изменений.

### 7.3. Деприкация и удаление

Владелец MUST:

* обозначить замену;
* обеспечить миграцию всех call sites;
* после миграции — удалить код и перевести запись в `removed` (или удалить из реестра — по политике сервиса).

---

## 8. Исключения и ADR

Любое отступление от MUST/MUST NOT возможно только через документированное исключение.

**Правило**

* Исключение MUST быть зафиксировано в ADR (Architecture Decision Record) с:

  * контекстом,
  * решением,
  * рисками,
  * сроком действия или условиями пересмотра.

---

## 9. Политики сервиса (service‑level policy appendix)

Каждый сервис, внедряющий стандарт, MUST зафиксировать:

1. границу уникальности Query ID (в рамках сервиса или всей системы);
2. формат Registry (один файл / много файлов);
3. стратегию версионирования (QC‑11 A или B);
4. минимальный набор observability (логи / tracing / SQL comments);
5. требования по безопасности (PII, tenant boundary, роли);
6. “порог каталога”: какие источники данных включаются (SQL‑только или все).

---

## Приложение A. Шаблон Query Entry (минимально рекомендуемый)

```yaml
id: User.GetById
status: active                 # draft|active|deprecated|removed
owner: team-identity

purpose: >
  Получить профиль пользователя по идентификатору для сценариев
  авторизации и отображения профиля.

source: postgres.main

contract:
  params:
    - name: user_id
      type: uuid
      required: true
  returns:
    cardinality: "0..1"
    shape: UserRow             # ссылка на тип/DTO/описание полей
  ordering: null
  pagination: null
  errors:
    - not_found
    - forbidden

data_objects:
  read:
    - users
  write: []

consistency:
  transaction: optional        # required|optional|forbidden
  idempotent: true
  isolation: default           # optional, only if meaningful

security:
  pii: true
  tenant_boundary: enforced
  access: "internal:auth, internal:profile"

performance:
  hot_path: true
  expected_latency_ms_p95: 30
  notes: "Требуется индекс users(id)."

observability:
  log_query_id: true
  trace: recommended
  sql_comment: recommended

links:
  use_cases:
    - Auth.Login
    - Profile.View
  call_sites:
    - "src/services/auth/AuthService.ts#loadUser"
    - "src/controllers/profile/ProfileController.ts#get"
```

---

## Приложение B. Чек‑лист ревью (ссылки на QC‑xx)

* [ ] QC‑01 Query ID корректный, уникальный, стабильный
* [ ] QC‑02 Purpose объясняет смысл, а не SQL
* [ ] QC‑03 Контракт полон: параметры, кардинальность, shape, пагинация/порядок
* [ ] QC‑04 Data objects перечислены корректно (read/write)
* [ ] QC‑05 Транзакционность/идемпотентность/ошибки описаны
* [ ] QC‑06 Security: PII/tenant boundary/доступ
* [ ] QC‑07 Производительность: лимиты, пагинация, hot path ожидания
* [ ] QC‑08 Наблюдаемость: query_id в логах, корреляция в трейсах/SQL (если принято)
* [ ] QC‑09 Owner указан
* [ ] QC‑10 Lifecycle корректен, деприкации оформлены
* [ ] QC‑11 Breaking changes обработаны по политике сервиса
* [ ] QC‑12 Тесты/проверки добавлены, где нужно

---

## Приложение C. Антипаттерны (коротко)

1. **“Каталог ради каталога”**: записи есть, но не используются в ревью, не валидируются CI.
2. **Размытые purpose**: “получить данные”, “обновить сущность”. Невозможно отличить запросы.
3. **Контракт без кардинальности**: потребители не знают, чего ожидать.
4. **Списки без лимитов**: медленно и опасно, особенно в hot path.
5. **PII без маркировки**: риск безопасности и аудита.
6. **Невидимость в runtime**: в APM видно SQL, но не видно смысл (Query ID отсутствует).
</file>

<file path="docs/_meta/sdlc.md">
# SDLC для PAIP

## 1) Назначение и границы

Этот документ — главный источник правил SDLC для PAIP. Он описывает процесс, терминологию и виды артефактов. Всё, что требует отдельного объёма, выносится в самостоятельные артефакты; всё компактное остаётся здесь.

Цели:

- Управляемая разработка по итерациям.
- Прозрачная трассируемость от потребностей до проверки результата.
- Минимум бюрократии при максимальной ясности решений.

Границы:

- Мы не ведём формальные «оборонные» записи IEEE 12207, если этого не требует контракт.
- Ops/installation/maintenance оформляем позже, ближе к первому деплою.

## 2) Принципы

- Требования выражаются через потребности пользователя и проверяемые outcomes.
- Трассируемость обязательна, но хранится в Markdown.
- Дизайн не должен существовать без связанного требования.
- У каждого выбранного требования есть проверка (acceptance).
- Решения фиксируются отдельно, чтобы не терять контекст компромиссов.

## 3) Глоссарий

| Термин               | Определение                                           | Примечание                      |
|----------------------|-------------------------------------------------------|---------------------------------|
| Need                 | Интегрированная потребность пользователя/стейкхолдера | Problem space                   |
| Job (AJTBD)          | Работа, которую пользователь пытается выполнить       | `JOB-###`                       |
| Outcome              | Наблюдаемый результат, который улучшает Job           | `OUT-###`                       |
| Requirement          | Требование к системе                                  | Через `US/UC/NFR`               |
| User Story (US)      | История пользователя в продуктовых терминах           | `US-###`                        |
| Use Case (UC)        | Возможность системы на уровне поведения               | `UC-###`                        |
| NFR                  | Нефункциональное требование                           | `NFR-###`                       |
| Design Input         | Выбранный scope итерации                              | `01_vision.md`                  |
| Design Output        | Архитектура, модели, спецификации                     | `03..06`                        |
| Verification         | Проверка «сделали правильно?»                         | Проверка дизайна/реализации     |
| Validation           | Проверка «сделали правильное?»                        | Acceptance/использование        |
| Acceptance Test (AT) | Продуктовый сценарий проверки                         | `AT-###`                        |
| Evidence (EVD)       | Фиксация источника/факта/исследования                 | `EVD-###`                       |
| ADR                  | Архитектурное решение                                 | `ADR-####`                      |
| Baseline             | Контрольная точка готовности                          | Requirements/Design/Validation  |
| Traceability         | Связь артефактов по цепочке                           | `OUT → US/UC/NFR → Design → AT` |

## 4) Общий жизненный цикл

1. Problem space: `Needs` и `Jobs/Outcomes`.
2. Requirements: `US/UC/NFR`.
3. Design Inputs: выбранный scope итерации.
4. Design Outputs: архитектура и модели.
5. Validation: acceptance‑сценарии и их покрытие.
6. Learnings: выводы и изменение будущих требований.

## 5) Итерационный процесс

### 5.1. Входы итерации (Design Input)

- Зафиксировать выбранные `OUT/US/UC/NFR`.
- Сформулировать IN/OUT, wedge‑сценарий и метрики.

### 5.2. Выходы дизайна (Design Output)

- Архитектура и модели обязаны ссылаться на требования.
- Все ключевые решения фиксируются отдельными `ADR`.

### 5.3. Валидация

- Для каждого выбранного `US` есть минимум один `AT`.
- Acceptance‑сценарии описывают проверяемое поведение.

## 6) Baselines и чеклисты

### 6.1. Requirements Baseline

Критерии:

- Выбранные `OUT/US/UC/NFR` указаны в `01_vision.md`.
- Coverage‑матрица заполнена.
- Нет противоречий между `OUT` и `US/UC`.

### 6.2. Design Baseline

Критерии:

- `03/04/05/06` заполнены и ссылаются на требования.
- Design Trace заполнен.
- Все ключевые архитектурные решения имеют `ADR`.

### 6.3. Validation Baseline

Критерии:

- `acceptance.md` покрывает все `US` в scope.
- `07_mvp_plan.md` ссылается на `AT`.

## 7) Виды артефактов

### 7.1. Global слой

| Артефакт          | Назначение                            | Расположение                          |
|-------------------|---------------------------------------|---------------------------------------|
| Vision            | North star и принципы                 | `docs/product/global_vision.md`       |
| Needs             | Интегрированная потребность и границы | `docs/product/needs.md`               |
| Jobs              | Каталог AJTBD‑job                     | `docs/product/jobs/`                  |
| Global US         | Реестр продуктовых историй            | `docs/product/global_user_stories.md` |
| Global UC         | Реестр системных возможностей         | `docs/product/global_use_cases.md`    |
| NFR               | Нефункциональные требования           | `docs/product/nfr.md`                 |
| Glossary          | Термины домена                        | `docs/product/glossary.md`            |
| Evidence Register | Реестр источников/исследований        | `docs/research/evidence_register.md`  |

### 7.2. Iteration слой

| Артефакт        | Назначение                                   | Расположение                              |
|-----------------|----------------------------------------------|-------------------------------------------|
| 01_vision       | Scope, IN/OUT, метрики, выбранные требования | `docs/iterations/<id>/01_vision.md`       |
| 02_use_cases    | Подмножество UC для итерации                 | `docs/iterations/<id>/02_use_cases.md`    |
| 03_domain_model | Доменные понятия и связи                     | `docs/iterations/<id>/03_domain_model.md` |
| 04_architecture | Архитектура и tradeoffs                      | `docs/iterations/<id>/04_architecture.md` |
| 05_event_model  | События и состояния                          | `docs/iterations/<id>/05_event_model.md`  |
| 06_data_model   | Модель данных                                | `docs/iterations/<id>/06_data_model.md`   |
| 07_mvp_plan     | План реализации                              | `docs/iterations/<id>/07_mvp_plan.md`     |
| job_pack        | Выбранные Jobs/Outcomes, гипотезы            | `docs/iterations/<id>/job_pack.md`        |
| traceability    | Матрицы покрытия и дизайн‑трейса             | `docs/iterations/<id>/traceability.md`    |
| acceptance      | Продуктовые `AT` сценарии                    | `docs/iterations/<id>/acceptance.md`      |
| reviews         | Чеклисты baselines                           | `docs/iterations/<id>/reviews.md`         |

### 7.3. Decision слой

| Артефакт | Назначение            | Расположение                  |
|----------|-----------------------|-------------------------------|
| ADR      | Архитектурные решения | `docs/adr/ADR-####-<slug>.md` |

## 8) Схема ID и ссылок

- `JOB-###` — AJTBD job.
- `OUT-###` — outcome внутри job.
- `US-###`, `UC-###`, `NFR-###` — требования.
- `AT-###` — acceptance‑сценарии.
- `ADR-####` — архитектурные решения.
- `EVD-###` — evidence/исследования.

Правило ссылок:

- В каждом артефакте указывать связанные ID явно в тексте.
- В design‑документах ссылки на требования обязательны.
- В acceptance‑сценариях ссылки на `US` обязательны.

## 9) Трассируемость

Минимальные обязательные связи:

- `OUT → US/UC/NFR`.
- `US → AT`.
- `Design Section → OUT/US/UC/NFR`.
- `ADR → OUT/US/NFR/EVD`.

Матрицы:

- Coverage: показывает, какие outcomes и требования входят в итерацию.
- Design Trace: связывает требования с архитектурой/моделями/AT.

## 10) Управление изменениями

- Любое изменение `OUT/US/UC/NFR` после Requirements Baseline требует пересмотра baseline и traceability.
- Любое изменение архитектуры, влияющее на требования, фиксируется через `ADR`.
- Все изменения фиксируются в итерационных документах, глобальные реестры остаются единым источником истины.

## 11) Definition of Done

### 11.1. Для артефакта

- Заполнены обязательные поля.
- Присутствуют ссылки на связанные требования.
- Нет противоречий с глобальными реестрами.

### 11.2. Для итерации

- Requirements/Design/Validation baselines закрыты.
- В `acceptance.md` покрыты все `US` из scope.
- Обновлена `traceability.md`.

## 12) Соответствие IEEE 12207 / INCOSE (подробное)

| IEEE/INCOSE термин        | Смысл                        | Наши артефакты/механики                                       |
|---------------------------|------------------------------|---------------------------------------------------------------|
| Stakeholder Needs         | Ожидания и цели пользователя | `needs.md`, `jobs/`, `OUT-###`                                |
| System Requirements       | Что должна уметь система     | `global_user_stories.md`, `global_use_cases.md`, `nfr.md`     |
| Design Input Requirements | Выбранный scope итерации     | `01_vision.md`, `job_pack.md`, Coverage matrix                |
| Architecture (SAD)        | Архитектура системы          | `04_architecture.md`, `ADR`                                   |
| Detailed Design (SDD)     | Детальный дизайн             | `03_domain_model.md`, `05_event_model.md`, `06_data_model.md` |
| Implementation            | Реализация                   | Код + `07_mvp_plan.md` как план                               | 
| Integration               | Сборка компонентов           | Описывается в `04_architecture.md` и acceptance‑сценариях     |
| Verification              | Проверка корректности        | `reviews.md`, traceability, тесты                             | 
| Validation                | Проверка ценности            | `acceptance.md`, user‑outcome метрики                         | 
| Reviews/Walkthroughs      | Контрольные проверки         | `reviews.md`                                                  |
| Configuration Management  | Управление изменениями       | git + ID‑политика + `traceability.md`                         |
| Records                   | Формальные записи            | Заменены `reviews.md` и git history                           |

## 13) Исключения и эскалация

- Если требуется формальная сертификация или контрактная отчётность, процесс расширяется отдельными record‑документами.
- Любое исключение из правил фиксируется в `reviews.md` и кратко описывается в итерационных документах.
</file>

<file path="src/paip/process_compiler.py">
from __future__ import annotations

import argparse
import json
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError, model_validator


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class TransitionDef(BaseModel):
    to: str = Field(min_length=1)
    label: str | None = None
    description: str | None = None


class StepDef(BaseModel):
    type: Literal["gate", "action", "terminal"] = "action"
    title: str = Field(min_length=1)
    transitions: list[TransitionDef] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_transitions(self) -> "StepDef":
        if self.type == "terminal" and self.transitions:
            raise ValueError("Terminal step must not have transitions")
        return self


class ProcessDDL(BaseModel):
    process_id: str = Field(min_length=1)
    version: int = Field(ge=1)
    initial_step: str = Field(min_length=1)
    steps: dict[str, StepDef]

    @model_validator(mode="after")
    def validate_graph(self) -> "ProcessDDL":
        if self.initial_step not in self.steps:
            raise ValueError(f"initial_step not found: {self.initial_step}")

        if not any(step.type == "terminal" for step in self.steps.values()):
            raise ValueError("Process must contain at least one terminal step")

        step_ids = set(self.steps.keys())
        for step_id, step in self.steps.items():
            for transition in step.transitions:
                if transition.to not in step_ids:
                    raise ValueError(
                        f"Unknown transition target: {step_id} -> {transition.to}"
                    )

        visited: set[str] = set()
        queue: deque[str] = deque([self.initial_step])
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            for transition in self.steps[current].transitions:
                queue.append(transition.to)

        unreachable = sorted(step_ids - visited)
        if unreachable:
            raise ValueError(
                "Unreachable steps from initial_step: " + ", ".join(unreachable)
            )

        return self


class StateHistoryItem(BaseModel):
    step: str = Field(min_length=1)
    at: str = Field(min_length=1)
    reason: str = Field(min_length=1)


class ProcessState(BaseModel):
    process_id: str = Field(min_length=1)
    version: int = Field(ge=1)
    task: str = Field(min_length=1)
    current_step: str = Field(min_length=1)
    status: Literal["in_progress", "blocked", "done"] = "in_progress"
    branch: str | None = None
    memory: dict[str, Any] = Field(default_factory=dict)
    history: list[StateHistoryItem] = Field(default_factory=list)


def _load_yaml_or_json_dict(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        yaml = None

    if yaml is not None:
        data = yaml.safe_load(text)
    else:
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "PyYAML is not installed. Use JSON-compatible YAML syntax or install PyYAML."
            ) from exc

    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def _dump_yaml_or_json_dict(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        yaml = None

    if yaml is not None:
        text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=False)
    else:
        text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")


def load_process_ddl(path: Path) -> ProcessDDL:
    return ProcessDDL.model_validate(_load_yaml_or_json_dict(path))


def load_process_state(path: Path) -> ProcessState:
    return ProcessState.model_validate(_load_yaml_or_json_dict(path))


def compile_process(ddl: ProcessDDL) -> dict[str, Any]:
    edges: list[dict[str, Any]] = []
    for step_id, step in ddl.steps.items():
        for transition in step.transitions:
            edges.append(
                {
                    "from": step_id,
                    "to": transition.to,
                    "label": transition.label,
                    "description": transition.description,
                }
            )

    return {
        "process_id": ddl.process_id,
        "version": ddl.version,
        "initial_step": ddl.initial_step,
        "steps": {
            step_id: {
                "type": step.type,
                "title": step.title,
                "transition_count": len(step.transitions),
            }
            for step_id, step in ddl.steps.items()
        },
        "edges": edges,
    }


def init_process_state(
    ddl: ProcessDDL,
    *,
    task: str,
    branch: str | None = None,
    memory: dict[str, Any] | None = None,
) -> ProcessState:
    state = ProcessState(
        process_id=ddl.process_id,
        version=ddl.version,
        task=task,
        current_step=ddl.initial_step,
        status="in_progress",
        branch=branch,
        memory=memory or {},
    )
    state.history.append(
        StateHistoryItem(step=ddl.initial_step, at=_utc_now_iso(), reason="init")
    )
    return state


def validate_state_against_process(state: ProcessState, ddl: ProcessDDL) -> None:
    if state.process_id != ddl.process_id:
        raise ValueError(
            f"State process_id={state.process_id} does not match ddl={ddl.process_id}"
        )
    if state.version != ddl.version:
        raise ValueError(f"State version={state.version} does not match ddl={ddl.version}")
    if state.current_step not in ddl.steps:
        raise ValueError(f"Unknown current_step in state: {state.current_step}")


def _select_transition(
    state: ProcessState,
    ddl: ProcessDDL,
    *,
    to_step: str | None = None,
    branch: str | None = None,
) -> TransitionDef:
    current = ddl.steps[state.current_step]
    if current.type == "terminal":
        raise ValueError(f"Step {state.current_step} is terminal; cannot advance")

    transitions = current.transitions
    if not transitions:
        raise ValueError(f"Step {state.current_step} has no outgoing transitions")

    if to_step:
        matches = [item for item in transitions if item.to == to_step]
        if len(matches) != 1:
            raise ValueError(
                f"No transition from {state.current_step} to {to_step}"
            )
        return matches[0]

    if current.type == "gate":
        branch_value = branch if branch is not None else state.branch
        if not branch_value:
            raise ValueError(
                f"Gate step {state.current_step} requires branch or explicit --to"
            )
        matches = [item for item in transitions if item.label == branch_value]
        if len(matches) != 1:
            raise ValueError(
                f"Gate step {state.current_step} has no unique transition for branch={branch_value}"
            )
        return matches[0]

    if len(transitions) == 1:
        return transitions[0]

    raise ValueError(
        f"Step {state.current_step} has multiple transitions; specify --to"
    )


def advance_process_state(
    state: ProcessState,
    ddl: ProcessDDL,
    *,
    to_step: str | None = None,
    branch: str | None = None,
    reason: str = "advance",
) -> ProcessState:
    validate_state_against_process(state, ddl)
    transition = _select_transition(state, ddl, to_step=to_step, branch=branch)

    if branch is not None:
        state.branch = branch

    state.current_step = transition.to
    target = ddl.steps[transition.to]
    state.status = "done" if target.type == "terminal" else "in_progress"
    state.history.append(
        StateHistoryItem(step=transition.to, at=_utc_now_iso(), reason=reason)
    )
    return state


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="process-compiler")
    sub = parser.add_subparsers(dest="command", required=True)

    cmd_compile = sub.add_parser("compile")
    cmd_compile.add_argument("--ddl", required=True)
    cmd_compile.add_argument("--out", required=True)

    cmd_init = sub.add_parser("init")
    cmd_init.add_argument("--ddl", required=True)
    cmd_init.add_argument("--state", required=True)
    cmd_init.add_argument("--task", required=True)
    cmd_init.add_argument("--branch")
    cmd_init.add_argument("--memory-json")

    cmd_advance = sub.add_parser("advance")
    cmd_advance.add_argument("--ddl", required=True)
    cmd_advance.add_argument("--state", required=True)
    cmd_advance.add_argument("--to")
    cmd_advance.add_argument("--branch")
    cmd_advance.add_argument("--reason", default="advance")

    cmd_show = sub.add_parser("show")
    cmd_show.add_argument("--ddl", required=True)
    cmd_show.add_argument("--state", required=True)

    return parser


def _parse_memory_json(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError("--memory-json must decode to object")
    return payload


def _run_cli(args: argparse.Namespace) -> int:
    if args.command == "compile":
        ddl = load_process_ddl(Path(args.ddl))
        compiled = compile_process(ddl)
        _dump_yaml_or_json_dict(Path(args.out), compiled)
        print(
            f"Compiled {ddl.process_id}@v{ddl.version}: {len(ddl.steps)} steps, {len(compiled['edges'])} edges"
        )
        return 0

    if args.command == "init":
        ddl = load_process_ddl(Path(args.ddl))
        memory = _parse_memory_json(args.memory_json)
        state = init_process_state(
            ddl,
            task=args.task,
            branch=args.branch,
            memory=memory,
        )
        _dump_yaml_or_json_dict(Path(args.state), state.model_dump(mode="json"))
        print(
            f"Initialized state for {ddl.process_id}@v{ddl.version} at step={state.current_step}"
        )
        return 0

    if args.command == "advance":
        ddl = load_process_ddl(Path(args.ddl))
        state_path = Path(args.state)
        state = load_process_state(state_path)
        state = advance_process_state(
            state,
            ddl,
            to_step=args.to,
            branch=args.branch,
            reason=args.reason,
        )
        _dump_yaml_or_json_dict(state_path, state.model_dump(mode="json"))
        print(f"Advanced to step={state.current_step} status={state.status}")
        return 0

    if args.command == "show":
        ddl = load_process_ddl(Path(args.ddl))
        state = load_process_state(Path(args.state))
        validate_state_against_process(state, ddl)
        current = ddl.steps[state.current_step]
        payload = {
            "process_id": state.process_id,
            "version": state.version,
            "task": state.task,
            "current_step": state.current_step,
            "step_type": current.type,
            "status": state.status,
            "branch": state.branch,
            "next": [
                {"to": item.to, "label": item.label, "description": item.description}
                for item in current.transitions
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    raise ValueError(f"Unsupported command: {args.command}")


def main() -> None:
    args = _build_parser().parse_args()
    try:
        raise SystemExit(_run_cli(args))
    except (ValidationError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
</file>

<file path="docs/_meta/pr-notes/index.md">
# PR Notes Registry

One-note-per-file markdown registry generated from `git notes`.

- Source ref: `refs/notes/commits`
- Generated at (UTC): `2026-02-19T10:32:58Z`
- Total notes: `3`

## Entries

| Commit | Subject | Note Title | Committer Date | Branch Hints | Note File |
|---|---|---|---|---|---|
| `c9a60fcf` | chore(notes): add markdown PR notes registry and hooks workflow | Motivation | `2026-02-19T17:32:14+07:00` | `codex/query-catalog-tooling` | [`notes/c9a60fcf59998539f5c34684b87d26e032f537a7.md`](notes/c9a60fcf59998539f5c34684b87d26e032f537a7.md) |
| `56332bc2` | feat(db): add pagination to list queries and align query registry | Motivation | `2026-02-19T16:21:56+07:00` | `codex/query-catalog-tooling` | [`notes/56332bc21c481559be320141f12a0a183eec758c.md`](notes/56332bc21c481559be320141f12a0a183eec758c.md) |
| `0524eb87` | feat(qc): register runtime and debug query ids | Motivation | `2026-02-19T16:06:35+07:00` | `codex/query-catalog-tooling` | [`notes/0524eb8700c2ca26b1dab9a38b78c4c602405728.md`](notes/0524eb8700c2ca26b1dab9a38b78c4c602405728.md) |
</file>

<file path="SDLC.md">
# SDLC (v0) — процесс разработки

Этот файл — «входная дверь». Подробный SDLC: docs/_meta/sdlc.md (или _meta/sdlc.md — см. README).

## Быстрый вход (1–2 шага для новой задачи)

### Шаг 1: Scope Gate (обязателен)
Определи ветку работ до начала изменений:
- **A / Code-only:** меняется только код/тесты, без изменения публичных контрактов и без новых DB/query-операций.
- **B / Data-access:** есть изменение DB/query-операций (обязательно подключается Query Catalog: `docs/_meta/QC-STANDARD.md`, `query-catalog/*`).
- **C / Architecture/Contract:** меняются публичные контракты/форматы или архитектурные решения (обязательно ADR + обновление итерационных артефактов).

### Шаг 2: Path State (память чата)
Зафиксируй выбранную ветку как состояние пути и обновляй при каждом смене направления:

```text
[SDLC-PATH]
task: <краткое имя задачи>
branch: A|B|C
context_files:
- <file1>
- <file2>
next_gate: requirements|design|validation
status: in_progress|blocked|done
[/SDLC-PATH]
```

Это состояние хранится в сообщениях чата (оперативная память работы). Для PR его можно продублировать через PR notes.

Опционально: это же состояние можно вести через process compiler:
- DDL: `docs/_meta/process/sdlc-task-flow.ddl.yaml`
- Guide: `docs/_meta/process/compiler.md`
- CLI: `python -m paip.process_compiler ...`

## Цели
- Итерационная разработка (MVP → расширение).
- Трассируемость: OUT → US/UC/NFR → Design → AT → Evidence.
- Максимум параллельности через агентов при сохранении качества через PR-гейты.

## Основные правила
1) Global требования живут отдельно от итераций.
2) Итерация — это “Design Input → Design Output → Validation”.
3) Все изменения кода проходят через PR + тесты.
4) Любое существенное архитектурное решение фиксируется ADR.

## Гейты (Baselines)
- Requirements Baseline: scope итерации + acceptance/traceability заполнены.
- Design Baseline: архитектура/модели/контракты готовы, traceability связывает дизайн с требованиями.
- Validation Baseline: AT определены/покрыты, есть план прогона.

## Роли (минимум)
- Maintainer/Integrator (человек): принимает scope, мерджит PR, закрывает baselines.
- Agents (Codex): выполняют задачи в ветках по правилам AGENTS.md.

## Приложение A — Iteration Pack v0 (обязательные файлы)
В каждой итерации создаётся папка: `docs/iterations/<id>/` и файлы:
- 01_vision.md
- 04_architecture.md
- acceptance.md
- traceability.md
- reviews.md
- 07_mvp_plan.md (опционально, но полезно)

Содержимое и шаблоны — см. ниже.
</file>

<file path="docs/iterations/2026-02-mvp/01_vision.md">
# 01 Vision — 2026-02-mvp

## Scope этой итерации

### Selected Requirements
- US-001
- UC-001, UC-002, UC-003, UC-005
- NFR-001, NFR-002, NFR-006

### In
- Один вертикальный сценарий US-001: мониторинг уникальных событий по городу/теме.
- Discovery источников: SearXNG через внешний endpoint (`SEARXNG_BASE_URL`).
- Extraction: Eventbrite-style adapter (MVP), формирование `EventClaim`.
- Event-level дедуп и резолв в `Event` (new/update/duplicate).
- Ручной и interval запуск (`run once`, `run scheduler`).
- Telegram уведомления по `new_event` и `event_updated`.
- История уведомлений в SQLite с event-level причиной.

### Out
- Temporal orchestration (следующий этап).
- Multi-tenant и авторизация.
- UI/дашборд.
- Near-duplicate и advanced entity resolution.
- Второй extractor beyond Eventbrite-style (следующий этап).

## Wedge

Пользователь добавляет монитор по Бангкоку/теме, запускает pipeline, получает сигналы по уникальным событиям, видит историю с причиной (`new_event`/`event_updated`) и источником.

## Метрики итерации

- E2E: `monitor add -> run once -> telegram notification -> history` проходит без правки кода.
- Event novelty: повторный запуск на тех же данных не отправляет дубли (`duplicates > 0`, `new_events = 0`).
- Event update: при изменении даты/venue для того же источника фиксируется `updated_events > 0`.
- Explainability: у каждого уведомления есть `source_name`, `source_url`, `reason`, `created_at`.
- Stability: ошибка SearXNG или Telegram фиксируется в истории run/notifications без падения scheduler.
</file>

<file path="AGENTS.md">
# AGENTS.md — инструкции для Codex/агентов в этом репозитории

Codex читает этот файл перед началом работы. Цель — чтобы изменения были предсказуемыми, тестируемыми и трассируемыми.

## Источник истины (обязательно читать перед работой)
1) Vision: docs/product/global_vision.md
2) Требования: docs/product/global_user_stories.md, docs/product/global_use_cases.md, docs/product/nfr.md
3) Глоссарий: docs/product/glossary.md
4) Текущая итерация: docs/iterations/<CURRENT>/ (01_vision.md, 04_architecture.md, acceptance.md, traceability.md, reviews.md)
5) SDLC: SDLC.md
6) Query Catalog standard: docs/_meta/QC-STANDARD.md
7) Query Catalog steward skill: skills/query-catalog-steward.md
8) PR notes process and registry: docs/_meta/PR-NOTES.md, docs/_meta/pr-notes/index.md

Если файлы лежат не в `docs/`, используй путь из README.md.

## Рабочие соглашения
- Одна задача = одна ветка = один PR (draft разрешён).
- Не меняй глобальные IDs (US/UC/NFR/AT/ADR) и их смысл без явного указания в задаче.
- Не меняй публичные контракты/схемы/форматы без ADR (docs/adr/ADR-####-*.md).
- Не добавляй новые прод-зависимости без явного разрешения (комментарий в PR/issue).
- Не делай “рефакторинг ради красоты”, если это не цель задачи.

## Перед началом
- Первым делом запусти `just print-project-state` и изучи отчёт:
  - текущая итерация и baseline-статусы;
  - текущее состояние SDLC state machine (шаг, ветка A/B/C, доступные переходы);
  - актуальный health-check (`just test`), если не отключён.
- Сделай git checkpoint (коммит/тег) перед значимыми изменениями, чтобы можно было откатиться.
- Убедись, что понимаешь acceptance критерии для US/AT.

## Обязательные проверки перед PR
Укажи в PR:
- Какие US/UC/NFR закрываешь (IDs)
- Какие AT покрываешь (IDs)
- Как запустить проверки

Запусти локально (подставь реальные команды проекта):
- `make lint` или `npm run lint`
- `make test` или `npm test`
- (если есть) `make typecheck`

## Формат результата (в конце PR-описания)
- Summary: 3–7 bullets
- Evidence: команды/логи тестов + что проверено
- Risks: что может сломаться
- Follow-ups: что НЕ сделано и почему
</file>

<file path="docs/iterations/2026-02-mvp/04_architecture.md">
# 04 Architecture — 2026-02-mvp (US-001 event slice)

## Контур

```text
MonitorSpec (CLI)
  -> APScheduler (manual/interval trigger)
    -> SearXNG client (source discovery)
      -> SourceHit
        -> Extractor registry
          -> Eventbrite-style extractor
            -> EventClaim validation
              -> Event resolver (new / updated / duplicate)
                -> SQLite (source_hits, event_claims, events, runs)
                  -> Telegram notifier
                    -> notifications + history
```

## Технические решения

- Язык/рантайм: Python.
- Хранилище: SQLite (`PAIP_DB_PATH`).
- Оркестрация: `APScheduler` в MVP; Temporal позже.
- Source discovery: SearXNG JSON API (`SEARXNG_BASE_URL`).
- Extraction: Eventbrite-style extractor (JSON-LD Event payloads).
- Уведомления: Telegram bot token (`TELEGRAM_BOT_TOKEN`), fallback в stdout.
- Локальный command runner: `justfile` (MVP dev workflow).

## Публичные контракты

- CLI:
  - `paip monitor add --title --city --topic --query --interval-min --chat-id`
  - `paip monitor list`
  - `paip run once --monitor-id`
  - `paip run scheduler`
  - `paip history --monitor-id --limit`

- ENV:
  - `PAIP_DB_PATH` (default `./tmp/paip.db`)
  - `SEARXNG_BASE_URL` (required)
  - `SEARXNG_API_KEY` (optional)
  - `TELEGRAM_BOT_TOKEN` (required для доставки)
  - `PAIP_LOG_LEVEL` (default `INFO`)

## Доменная модель MVP

- `EventClaim`: извлечённое утверждение из конкретного источника.
- `Event`: уникальная сущность события в рамках монитора.
- `Notification`: запись отправки по `event_id` с `reason` и `status`.

Обязательные поля `Event`: `title`, `city`, `venue`, `start_at|start_date`, `source_url`, `source_name`, `extracted_at`, `confidence`.

## Дедуп и резолв (v1)

- Event key v1: `normalize(title) + normalize(city) + normalize(venue) + start_date`.
- Полный матч ключа и без изменений атрибутов: `duplicate`.
- Совпадение по `source_url` с изменением атрибутов: `updated_event`.
- Новый ключ без существующего события: `new_event`.
- Unsupported domain: учитывается в `unsupported_sources`, run не падает.

## Run counters

`run once` возвращает:
- `fetched_sources`
- `claims_extracted`
- `new_events`
- `updated_events`
- `duplicates`
- `unsupported_sources`
- `status`, `error`

## Трассируемые решения

- UC-001: discovery + scheduler (`searx_client`, `pipeline`, `scheduler`).
- UC-002: нормализация в `EventClaim` и `Event`.
- UC-003: event-level dedup/resolution в `pipeline` + `events` unique key.
- UC-005: Telegram + `notifications` + event-level history query.
- NFR-001: history содержит `reason`, `source_name`, `source_url`, `created_at`.
- NFR-002: повторный run на тех же событиях не дублирует уведомления.
- NFR-006: все операции доступны через CLI/just workflow.
</file>

<file path="docs/iterations/2026-02-mvp/acceptance.md">
# Acceptance — 2026-02-mvp (US-001 event-level)

- **AT-001 (US-001):** пользователь создаёт монитор и выполняет `run once`; новые события приходят в Telegram и попадают в history.
- **AT-002 (US-001, UC-003):** повторный запуск с теми же событиями не отправляет дубль-уведомления (`new_events=0`, `duplicates>0`).
- **AT-003 (US-001, UC-001):** scheduler-trigger выполняет запуск без ручного вызова и фиксирует `trigger=interval`.
- **AT-004 (UC-001, NFR-002):** ошибка SearXNG (timeout/500) сохраняется как failed run; scheduler продолжает работу.
- **AT-005 (UC-005, NFR-001):** ошибка Telegram сохраняется в notifications со status `failed`; run/history сохраняются.
- **AT-006 (US-001, NFR-001):** `history` показывает event-level поля: title/city/venue/date/source/reason/time.
- **AT-007 (UC-002):** claim без обязательных полей не попадает в `events`.
- **AT-008 (UC-003):** изменение даты или venue для того же `source_url` фиксируется как `updated_event`.
- **AT-009 (UC-001):** unsupported source учитывается в `unsupported_sources`, run завершается `completed`.
- **AT-010 (NFR-006):** DX-команды (`just monitor-add/run-once/history/stats/telegram-preview`) выполняют E2E-path без ручного `source`.

## Способ прогона

- Автоматически: `just test`.
- Ручной smoke:
  1. `just monitor-add ...`
  2. `just run-once <id>`
  3. `just stats <id> 10`
  4. `just telegram-preview <id> 10`
  5. `just history <id> 20`
</file>

<file path="docs/iterations/2026-02-mvp/reviews.md">
# Reviews & Baselines — 2026-02-mvp

## Requirements Baseline (Design Input)
- [x] Выбранные US/UC/NFR перечислены в `01_vision.md`
- [x] Acceptance отражает event-level сценарии (`new_event`, `event_updated`, `duplicate`)
- [x] `traceability.md` заполнен по цепочке `US/UC/NFR -> Design -> AT`
- [x] Scope ограничен MVP без расширения global-требований

Sign-off: @codex  Date: 2026-02-19

## Design Baseline (Design Output)
- [x] `04_architecture.md` описывает event-centric контур и контракты
- [x] БД-схема в коде соответствует документации (`source_hits`, `event_claims`, `events`, `notifications`)
- [x] Дедуп/резолв формализован event key v1 + update по `source_url`
- [x] Local tooling зафиксирован: `justfile` для setup/test/run/history/stats

Sign-off: @codex  Date: 2026-02-19

## Validation Baseline
- [x] Acceptance покрывает event-level scope итерации
- [x] Unit/Pipeline тесты зелёные (`just test`)
- [x] Ручной smoke определён (`monitor-add -> run-once -> stats -> telegram-preview -> history`)
- [x] Evidence обновлён по текущей модели, без промежуточных narrative-артефактов

Evidence:
- `.venv/bin/pytest -q` -> `13 passed`
- `just test` -> `13 passed`
- smoke: `just monitor-add` -> monitor `id=1`, `just run-once 1` -> `new_events=36`, `duplicates=103`, `unsupported_sources=1`
- smoke inspect: `just stats 1 5`, `just logs 1 5`, `just telegram-preview 1 3`

Sign-off: @codex  Date: 2026-02-19
</file>

<file path="docs/iterations/2026-02-mvp/traceability.md">
# Traceability — 2026-02-mvp

| Requirement | Design (section/module) | Acceptance (AT) | Notes |
|---|---|---|---|
| US-001 | `/Users/daokiin/projects/daokiin/paip/docs/iterations/2026-02-mvp/04_architecture.md`, `/Users/daokiin/projects/daokiin/paip/src/paip/cli.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/pipeline.py` | AT-001, AT-002, AT-003, AT-006, AT-008 | Event-level monitoring + history |
| UC-001 | `/Users/daokiin/projects/daokiin/paip/src/paip/searx_client.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/pipeline.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/scheduler.py` | AT-001, AT-003, AT-004, AT-009 | Discovery + manual/interval run |
| UC-002 | `/Users/daokiin/projects/daokiin/paip/src/paip/extractors.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/models.py` (`EventClaim`, `Event`) | AT-007 | Event claim normalization and validation |
| UC-003 | `/Users/daokiin/projects/daokiin/paip/src/paip/pipeline.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/utils.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/db.py` (`events`) | AT-002, AT-008 | Event-level dedup/resolution |
| UC-005 | `/Users/daokiin/projects/daokiin/paip/src/paip/notifier.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/db.py` (`notifications`, `get_history`) | AT-001, AT-005, AT-006 | Notification delivery + history |
| NFR-001 | `/Users/daokiin/projects/daokiin/paip/src/paip/db.py`, `/Users/daokiin/projects/daokiin/paip/src/paip/cli.py` (`history`) | AT-005, AT-006 | Explainable signal history |
| NFR-002 | `/Users/daokiin/projects/daokiin/paip/src/paip/pipeline.py` error handling + deterministic event key | AT-002, AT-004, AT-009 | Predictable reruns and failures |
| NFR-006 | `/Users/daokiin/projects/daokiin/paip/src/paip/cli.py`, `/Users/daokiin/projects/daokiin/paip/justfile` | AT-010 | No-code operation via CLI/just |
</file>

<file path="justfile">
set shell := ["bash", "-cu"]
set dotenv-load := true

venv_python := ".venv/bin/python"
venv_pip := ".venv/bin/python -m pip"
venv_pytest := ".venv/bin/pytest"
venv_paip := ".venv/bin/paip"

help:
  just --list

setup:
  python -m venv .venv
  {{venv_pip}} install -e '.[dev]'

test:
  {{venv_pytest}} -q

print-project-state:
  PYTHONPATH=src {{venv_python}} scripts/print_project_state.py {{ if env_var_or_default("PAIP_SKIP_TESTS", "0") == "1" { "--skip-tests" } else { "" } }}

qc-setup:
  {{venv_pip}} install -r query-catalog/requirements-qc.txt

qc-validate:
  {{venv_python}} scripts/qc_validate.py --root . --policy query-catalog/policy.template.yaml

qc-validate-ci:
  bash scripts/qc_validate_ci.sh

hooks-install:
  git config core.hooksPath .githooks
  chmod +x .githooks/pre-push

notes-list:
  git notes --ref refs/notes/commits list

notes-show SHA:
  git notes --ref refs/notes/commits show "{{SHA}}"

notes-push REMOTE='origin':
  git push "{{REMOTE}}" refs/notes/commits:refs/notes/commits

notes-registry-refresh:
  {{venv_python}} scripts/pr_notes_registry.py sync --output-dir docs/_meta/pr-notes --notes-ref refs/notes/commits

notes-registry-lint:
  {{venv_python}} scripts/pr_notes_registry.py lint --output-dir docs/_meta/pr-notes --notes-ref refs/notes/commits

readme-links-check FILE='README.md':
  {{venv_python}} scripts/check_readme_links.py --root . --file "{{FILE}}"

just-docs-check FILE='docs/_meta/JUST-COMMANDS.md':
  {{venv_python}} scripts/check_just_docs.py --justfile justfile --docs "{{FILE}}"

monitor-add TITLE CITY TOPIC QUERY INTERVAL_MIN CHAT_ID:
  {{venv_paip}} monitor add --title "{{TITLE}}" --city "{{CITY}}" --topic "{{TOPIC}}" --query "{{QUERY}}" --interval-min "{{INTERVAL_MIN}}" --chat-id "{{CHAT_ID}}"

monitor-list:
  {{venv_paip}} monitor list

run-once MONITOR_ID:
  {{venv_paip}} run once --monitor-id "{{MONITOR_ID}}"

run-scheduler:
  {{venv_paip}} run scheduler

history MONITOR_ID LIMIT='20':
  {{venv_paip}} history --monitor-id "{{MONITOR_ID}}" --limit "{{LIMIT}}"

logs MONITOR_ID='1' LIMIT='20':
  {{venv_paip}} history --monitor-id "{{MONITOR_ID}}" --limit "{{LIMIT}}"

stats MONITOR_ID='1' LIMIT='10':
  PAIP_DB_PATH="${PAIP_DB_PATH:-./tmp/paip.db}" {{venv_python}} -m paip.debug --monitor-id "{{MONITOR_ID}}" --limit "{{LIMIT}}"

telegram-preview MONITOR_ID='1' LIMIT='10' RUN_ID='':
  PAIP_DB_PATH="${PAIP_DB_PATH:-./tmp/paip.db}" {{venv_python}} -m paip.debug --monitor-id "{{MONITOR_ID}}" --limit "{{LIMIT}}" --telegram-preview {{ if RUN_ID != "" { "--run-id " + RUN_ID } else { "" } }}

env-example:
  @printf '%s\n' \
    'Required:' \
    '  SEARXNG_BASE_URL=https://your-searxng.example' \
    '  TELEGRAM_BOT_TOKEN=<telegram-bot-token>' \
    '' \
    'Optional:' \
    '  PAIP_DB_PATH=./tmp/paip.db' \
    '  PAIP_LOG_LEVEL=INFO' \
    '  SEARXNG_API_KEY='
</file>

</files>

</implementation-project-sdlc>



#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Ниже — план действий, опирающийся на твои материалы (v1/v2, сравнение, анализ, deep‑research и текущую реализацию SDLC DDL/state + `process_compiler.py`/`pre-push`/`justfile`/`print_project_state.py`). fileciteturn0file0

## Ключевое решение перед кодом: что именно “фиксируем”

Твой следующий шаг “зафиксировать процесс” я бы оформил как **заморозку контрактов** (минимальный RFC/Spec), чтобы дальше код был просто имплементацией, а не продолжением дискуссии:

### 1) Source of Truth и границы ответственности

Зафиксировать 3 слоя (ровно как в твоих v1-идеях):

- **DDL (граф процесса)** — только структура шагов и переходов.
- **Runtime state (текущее состояние)** — текущий шаг/ветка/статус/память/история.
- **Guards (политики проверок)** — отдельно от DDL, чтобы часто менять правила без риска ломать граф.

Это прямо соответствует выбранному в твоих материалах направлению “v1 как база + точечные идеи из v2”.

### 2) Конвенция: где живёт runtime state на практике

Сейчас у тебя state “примерный” лежит в `docs/_meta/process/sdlc-task-flow.state.yaml`, но даже `print_project_state.py` явно предупреждает, что это может быть **пример**, а не единственный runtime-источник.

Нужно принять одно из решений (и зафиксировать как правило проекта):

- **Вариант A (простое внедрение):** state файл всегда по фиксированному пути в репо (как сейчас), и каждая ветка хранит свою копию (в PR может конфликтовать при мерже).
- **Вариант B (лучше для параллельной работы/агентов):** state — **локальный артефакт**, например `.paip/state/sdlc-task-flow.state.yaml` (в `.gitignore`), а в PR фиксируется краткое резюме (например через PR notes).\
  Тогда tooling (hook/CLI) берёт путь state из дефолта + допускает override через `--state`/env.

Я бы рекомендовал **B**, потому что иначе при параллельных ветках/агентах один state-файл будет либо конфликтовать, либо “шуметь” в истории.

### 3) Семантика guards: блокируют/не блокируют

Зафиксировать простую модель, совместимую с твоими v1 материалами:

- `severity: error|warn`
- exit code `1`, если есть хотя бы один **error** fail
- warn не блокирует, но печатается\
  Опционально (идея из v2, полезная): `--strict`, превращающий warn в blocking.

### 4) Контексты применения guards

Зафиксировать 2 контекста (это ключ к “управлению переходами”, а не просто хуку):

- `pre_push`: что проверяем перед push
- `advance`: что проверяем **перед переходом** со шага `current_step`\
  То есть guards становятся реальными “guard conditions” на рёбрах/узлах процесса.

### 5) Оптимизация по changed files

Если ты реально хочешь, чтобы pre-push не превращался в “вечное ожидание”, нужно зафиксировать правило:

- pre-push считает `changed files` по диапазону пуша,
- передаёт список в guard runner,
- guard runner умеет `changed_files_any` фильтровать тяжёлые проверки (QC и т.п.).

Это один из самых практичных элементов твоего v1.

---

## План реализации (по этапам, так чтобы каждую часть можно было отдельно принять)

### Этап 1. “Процесс зафиксирован” (док + контракты)

**Deliverable:** короткий документ “Process-as-code contract” (можно прямо в `docs/_meta/process/sdlc-task-flow.md`), где есть:

- какие файлы являются SoT: DDL/state/guards,
- где лежит runtime state (вариант A или B),
- как агент/человек делает: `init → show → (run guards) → advance`,
- как работает pre-push: что блокирует, как emergency bypass,
- политика версий: `process_id`/`version` должны совпадать между DDL/state/guards, иначе hard fail.

Сюда же стоит вписать “agent contract” на 5 строк:

- при старте задачи агент обязан `init`/установить `branch`,
- после каждого большого шага агент делает `advance` с reason,
- перед push агент прогоняет `guards pre_push` (это же сделает hook),
- любые исключения — только через bypass с явным следом (log/PR notes).

---

### Этап 2. Guards как отдельная подсистема (v1-база)

**2.1. Добавить guard runner модуль**

- Новый модуль: `src/paip/process_guards.py`
- Переиспользовать `load_process_ddl/load_process_state` из `process_compiler.py` (или вынести общие YAML/json функции в `src/paip/process_io.py`, чтобы не дублировать).

**2.2. Спека guards-конфига (v0)**
Файл: `docs/_meta/process/sdlc-task-flow.guards.yaml` (JSON-compatible YAML)

Структура как в твоём v1:

- `process_id`, `version`
- `contexts.pre_push: [guards...]`
- `contexts.advance: { step_id: [guards...] }`

Минимальные guard types для старта:

- `command` (выполнить команду)
- `require_branch` (branch в state обязателен)
- `glob_exists` (например ADR присутствует)

When-фильтры:

- `branch_in: ["A","B","C"]`
- `changed_files_any: ["src/**", "query-catalog/**", ...]`

**2.3. CLI**
Команда “ручного запуска” и “для hook”:

- `python -m paip.process_guards check --context pre_push --ddl ... --state ... --guards ... [--changed-files-file ...]`
- `python -m paip.process_guards check --context advance --ddl ... --state ... --guards ...`\
  (внутри: взять `state.current_step`, найти список guards для этого шага)
- (опционально, но сильно повышает целостность)\
  `python -m paip.process_guards advance ...` = `check advance` → затем вызвать `advance_process_state(...)` из `process_compiler.py`

Поведение runner:

- проверка `process_id/version` (DDL/state/guards) — **жёстко**
- печать отчёта: PASS/FAIL/SKIP
- на `command` — показывать “хвост” stdout/stderr (например последние 30–50 строк)
- env прокидывать: `PAIP_CHANGED_FILES`, `QC_CHANGED_FILES` (newline-separated)

**2.4. Тесты**
Файл: `tests/test_process_guards.py`:

- загрузка конфига + match version
- `require_branch` падает если `state.branch` пуст
- `changed_files_any` реально скипает/ранит
- `command` pass/fail на `python -c "import sys; sys.exit(...)"`

---

### Этап 3. Pre-push enforcement (без “магии”)

Обновить `.githooks/pre-push` так, чтобы порядок был:

1. guards check
2. только потом — существующий sync git notes

Требования (важные):

- bypass только для guards: `PAIP_SKIP_GUARDS=1` (или другое имя — главное зафиксировать)
- bypass notes остаётся отдельным: `PAIP_SKIP_NOTES_PUSH=1`
- python: **только `.venv/bin/python`**, иначе fail с понятным сообщением (не “молча выключить контроль”)
- changed files:
  - читать stdin строки `local_ref local_sha remote_ref remote_sha`
  - считать diff’ы `git diff --name-only remote_sha..local_sha`
  - для нового ref (remote\_sha из нулей) — diff от empty tree
  - дедуп, сохранить во временный файл
  - передать в runner `--changed-files-file`

**Acceptance:** push блокируется, если обязательные guards не прошли.

---

### Этап 4. Визуализация графа (Mermaid) + детерминизм

Расширить `src/paip/process_compiler.py`:

- функция `render_mermaid_state_diagram(ddl) -> str`
- subcommand `render` (stdout или `--out`)

Я бы начал с **Mermaid stateDiagram-v2** (как в твоём v1), потому что это буквально state machine:

- `[*] --> initial`
- `terminal --> [*]`
- объявления стейтов + переходы
- сортировка шагов/рёбер стабильная (детерминизм = меньше дрейфа в diffs)

(Flowchart-рендер из v2 можно добавить потом как второй формат, если нужно “красивее для людей”.)

---

### Этап 5. Док процесса + автосинк секций (чтобы не устаревало)

**5.1. Создать “живой” документ процесса**
`docs/_meta/process/sdlc-task-flow.md`:

- краткое описание процесса
- SoT (DDL/state/guards)
- примеры CLI
- pre-push поведение + bypass
- автосекции:
  - `<!-- BEGIN SDLC DIAGRAM --> ... <!-- END SDLC DIAGRAM -->`
  - `<!-- BEGIN SDLC GUARDS --> ... <!-- END SDLC GUARDS -->`

**5.2. Скрипт синка**
`scripts/sync_process_docs.py`:

- читает DDL + guards config
- генерит Mermaid
- генерит guards-table
- заменяет только содержимое между маркерами

---

### Этап 6. Заполнить guards.yaml под текущий SDLC

Стартовый набор (реально применимый к твоему репо и `justfile`):
**pre\_push**

- `require_branch` (error) — без выбранной ветки процесс не управляем
- `just test` (error) — всегда
- `just qc-validate-ci` (error) — только если:
  - `branch_in: ["B"]` **или**
  - изменены пути вроде `query-catalog/**`, `src/**`, `scripts/qc_validate*`, `docs/_meta/QC-STANDARD.md`
- `just readme-links-check` (warn) — если менялись `README.md`/`docs/**`

**advance** (по шагам)

- `scope_gate`: require\_branch
- `query_catalog_gate`: qc-validate-ci (или qc-validate)
- `adr_gate`: `glob_exists docs/adr/ADR-*.md` min\_count=1
- `code_only_path`: `just test`
- `validation_gate`: `just test` (на всякий)

---

### Этап 7. DX-полировка (опционально, но окупается)

- `just guards` → вызывает guard runner `check --context pre_push`
- `just process-docs-sync` → вызывает `scripts/sync_process_docs.py`
- обновить `docs/_meta/JUST-COMMANDS.md`
- (опционально) `scripts/print_project_state.py` дополнить лёгким статусом guards (только быстрые/без тяжёлых команд), или хотя бы подсказкой “запусти guards”.

---

## Контрольные критерии “готово”

То, что можно поставить как Definition of Done на этот этап:

1. `python -m paip.process_guards check --context pre_push ...`:

- exit `0` если всё ок
- exit `1` если есть error fail
- warn видны в отчёте

2. `.githooks/pre-push`:

- блокирует push при fail guards
- уважает `PAIP_SKIP_GUARDS=1`
- notes-sync остаётся, но выполняется **после** guards

3. `python -m paip.process_compiler render --ddl ...`:

- выдаёт валидный Mermaid (детерминированный)

4. `docs/_meta/process/sdlc-task-flow.md` существует и синхронизируется скриптом:

- диаграмма актуальна
- таблица guards актуальна

5. `just test` зелёный

---

## Что я бы заложил “следующим витком” (но не сейчас)

Когда базовый контур будет работать и не бесить:

- `--json` вывод guard runner (для CI/агентов)
- `--strict` режим (warn → blocking)
- templating из v2 (аккуратно): `{branch}`, `{current_step}`, ключи из `state.memory`
- `markdown_checklist` guard (проверять sign-off/checkboxes в `docs/iterations/<id>/reviews.md`) — это мощно, но лучше после стабилизации “tests/QC/ADR”

---

Если хочешь ориентир “как разрезать на PR’ы”, то оптимальная последовательность такая:

1. guards runner + тесты (без hook)
2. guards.yaml + ручной запуск
3. pre-push интеграция
4. mermaid render
5. docs + sync script
6. DX команды (just + print\_project\_state улучшения)

Вся логика и структура этого плана напрямую вытекает из твоих подготовленных материалов и текущего состояния репозитория. fileciteturn0file0


#### You:
1. Зафиксируй все артефакты с которыми я определился.

2. Проверь на какие вопросы и какие необходимые важные решения нужно сделать сейчас чтобы закрыть все важные сейчас дыры.

Вот одно из них:
- Рантайм стейт реализовать по варианту А.
- Один фиксированный путь, чтобы при мёрже был конфликт, это часть дизайна.

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Ок — фиксирую то, что уже “решено/принято”, и затем перечисляю **дыры** (вопросы/решения), которые нужно закрыть *сейчас*, чтобы дальше спокойно кодить без развилок.

---

## 1) Зафиксированные артефакты и договорённости

### A. Source of Truth (process-as-code)

1. **DDL процесса (граф)**
   - Файл(ы) с описанием шагов/переходов процесса SDLC/DDL (YAML/JSON-совместимый YAML).
   - Явно содержит `process_id` и `version` (обязательно).

2. **Runtime state — вариант A (принято)**
   - **Один фиксированный путь в репозитории** (state под версионным контролем).
   - **Конфликты при merge — намеренная часть дизайна**, их нужно резолвить осознанно.
   - State содержит минимум: `process_id`, `version`, `current_step`, `branch`, (опционально `memory`, `history`).

3. **Guards конфиг**
   - Отдельный файл `*.guards.yaml` (или аналог), привязанный к тому же `process_id`/`version`.
   - Разделение по контекстам:
     - `pre_push`
     - `advance` (проверки перед переходом шага)

---

### B. Исполняемый код (tooling)

4. **Process compiler / state engine**
   - Загрузка DDL + state
   - Проверка совместимости `process_id`/`version`
   - Команды:
     - `show/status` (показать текущее состояние)
     - `advance` (переход между шагами с reason)
     - `render` (визуализация графа)

5. **Guards runner**
   - Команда `check --context pre_push|advance`
   - Единый формат отчёта + exit codes:
     - `error` → блокирует (exit 1)
     - `warn` → не блокирует (exit 0, но печатает)
   - Поддержка `changed_files` для оптимизации тяжёлых проверок

6. **pre-push hook**
   - Запускает guards в контексте `pre_push`
   - Считывает диапазон пуша и вычисляет changed files
   - Поддерживает bypass через env-переменную (строго задокументированную)

7. **Justfile / команды разработчика**
   - Алиасы для:
     - `just test`
     - `just qc-validate` / `just qc-validate-ci` (если есть)
     - `just guards`
     - `just render-process` / `just process-status`

8. **Визуализация процесса**
   - Генерация Mermaid диаграммы (минимум один формат) из DDL

9. **Документация процесса**
   - 1 главный документ процесса, описывающий:
     - артефакты (DDL/state/guards)
     - правила переходов
     - поведение hooks/guards/bypass
     - как резолвить merge-конфликты state
   - (Опционально) sync-скрипт, который обновляет диаграмму/таблицу guards в доке

10. **Тесты**

- Unit-тесты на:
  - загрузку/валидацию process\_id/version
  - базовые guards
  - advance semantics (невалидный переход, terminal, etc.)

---

## 2) Вопросы и важные решения, которые нужно закрыть сейчас (чтобы не было “дыр”)

Ниже — список “дыр” в порядке приоритета. Если закрыть их сейчас, дальше код пойдёт линейно.

### 2.1. Schema и инварианты state (иначе всё станет зыбким)

**Решить и зафиксировать:**

1. **Какие поля обязательны** в state v0?\
   Рекомендую минимальный обязательный набор:
   - `process_id`, `version`, `current_step`, `branch`
2. Есть ли **`memory`** и какой формат? (map\<string, any>?)\
   Если да — правила изменения (только через CLI? агент может писать напрямую?)
3. Есть ли **`history`** переходов в state?\
   Вариант A (state в git) особенно выигрывает от истории: при конфликтах видно, кто/когда куда двигал.

**Почему это “дыра сейчас”**: пока schema не фиксирован, любая реализация `advance` и guards будет переезжать.

---

### 2.2. Правила резолва merge-конфликта state (раз это “часть дизайна”)

Ты принял “конфликт — норм”. Тогда нужно формализовать, **как правильно резолвить**.

**Решить и задокументировать:**

1. **Кто побеждает при конфликте `current_step`?**
   - “самый дальний шаг”?
   - “шаг из целевой ветки”?
   - “ручной выбор” (скорее всего да)
2. **Как объединять history**, если она есть?
   - merge по времени, dedupe по `(from,to,ts,actor)`?
3. Что делать, если конфликтует `branch`?
   - `branch` в state — это “какая ветка должна существовать” или “где сейчас работа идёт”?\
     Если второе — при merge в main он почти всегда бессмысленный.

**Очень практичный совет (без изменения варианта A):**\
Добавь в state поле вроде `state_owner` / `work_context` (agent/worktree id) или хотя бы `last_updated_by + ts` — чтобы конфликт решался быстрее.

---

### 2.3. Семантика `branch` в state (это источник будущих багов)

Сейчас `branch` фигурирует как важная штука. Нужно решить, что она означает:

Возможные трактовки:

- (A) “ветка, в которой *должна* происходить работа над задачей”
- (B) “ветка, в которой *сейчас* находится репо” (плохой вариант, почти всегда ломается)
- (C) “logical branch / workspace id” (не обязательно git branch)

**Решение сейчас:** выбери одну трактовку и зафиксируй.\
Я бы выбирал (A) или (C). Для Codex/worktree-параллелизма (C) часто даже лучше.

---

### 2.4. Advance: можно ли двигать state, если guards не пройдены?

Это фундаментальная развилка процесса.

**Решить:**

1. `advance` всегда делает `guards(check advance)` и блокирует при error? (рекомендую да)
2. Есть ли `advance --force`?\
   Если да — должен ли он:
   - писать “FORCED” в history
   - требовать reason
   - требовать отдельный env-флаг (чтобы агент случайно не использовал)

---

### 2.5. Контракт версий (process\_id/version) — строгий или мягкий

Ты не хочешь хаоса, значит:

**Решить:**

- Несовпадение `process_id/version` между DDL и state и guards = **hard fail** (рекомендую да).
- Поддержка “миграции state” (скрипт migrate) — не сейчас, но надо зафиксировать принцип: *либо мигрируем, либо вручную правим, но не игнорируем*.

---

### 2.6. Security/Integrity: guards типа `command`

Если guards умеют запускать команды, нужно закрыть дыру безопасности и предсказуемости.

**Решить:**

1. Разрешён ли `command` вообще? (вероятно да)
2. Ограничиваем ли команды whitelist’ом (`just ...`/`python -m ...`)?
3. Из какой среды запускаем?
   - только `.venv/bin/python`
   - shell = `bash -euo pipefail` (или аналог)
4. Таймауты для команд? (иначе pre-push можно повесить)

---

### 2.7. Bypass политика (без неё люди будут “ломать систему”)

Раз есть enforcement, должен быть легальный escape hatch.

**Решить:**

- Одна переменная `PAIP_SKIP_GUARDS=1` — ок.
- Но обязательно:
  - печать предупреждения
  - запись события в history state (или хотя бы в stdout + git notes, если используешь)
  - требование reason (минимум через `PAIP_BYPASS_REASON`)

---

### 2.8. CI: кто главный — локальный hook или CI?

Чтобы процесс реально работал, нужно понять:

**Решить сейчас:**

- Будет ли CI запускать те же guards (хотя бы subset)?\
  Если да — фиксируем команду `just guards-ci` или `python -m ... --context ci`.

---

## Итог: “закрыть дыры” минимальным набором решений

Если хочешь самый короткий список, который надо принять *сейчас*, чтобы всё остальное стало прямолинейным:

1. **State schema v0** (обязательные поля + есть/нет history/memory)
2. **Merge-policy для state** (как резолвить `current_step`, history, branch)
3. **Семантика branch**
4. **Advance semantics** (guards обязательны? есть ли force?)
5. **Строгий version contract** (hard fail при несоответствии)
6. **Bypass policy** (переменная + reason + след)
7. **Command guards policy** (whitelist/таймаут/интерпретатор)

Хочешь — в следующем сообщении я могу прямо предложить **конкретный state schema v0 + merge-policy в 5 правил** (в стиле “если конфликт — делай X/Y”), чтобы ты просто вставил это в процесс-док и пошёл имплементировать.
