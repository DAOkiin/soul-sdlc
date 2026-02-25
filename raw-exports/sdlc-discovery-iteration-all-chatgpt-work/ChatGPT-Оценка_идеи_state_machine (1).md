# Оценка идеи state machine

#### You:
я придумал как управлять процессом разработки через state machine. Насколько я изобретаю велосипед по шкалам инновационность\оправданность и стоящее фокуса?

#### ChatGPT:
Если говорить честно: **сама идея “управлять разработкой через state machine” — это скорее “давно известный приём”, чем новая концепция.** Почти любой workflow (Jira/GitHub Projects/CI gates/BPMN) — это по сути конечный автомат со статусами и переходами.

Но по тому, что у тебя уже сделано (я посмотрел на структуру и файлы процесса у тебя в репе): **ты не просто “придумал статусы”, ты сделал “process-as-code”** — DDL процесса + runtime state + скрипт, который выводит “где мы и что дальше”, и привязал это к артефактам качества (QC/ADR/итерационные документы). Это уже ощутимо полезнее, чем “ещё одна доска со статусами”.

## Оценка по шкалам (0–10)

### 1) Инновационность: **3/10**

- **2/10** — сама мысль “workflow = state machine” стандартная.
- **+1 балл** — то, что ты держишь процесс *в репозитории* в машиночитаемом виде (DDL + state), и можешь автоматизировать проверки/подсказки, — это уже “process-as-code” подход (практичный, но не революционный).

**Когда может стать 6–7/10:** если ты доведёшь до уровня “guarded transitions” (переходы разрешены только если выполнены проверки/наличие артефактов), и это реально будет управлять CI/quality gates, а не просто документировать.

---

### 2) Оправданность: **7/10** (в твоём текущем формате)

Почему высокая:

- Ты держишь автомат **очень маленьким**: gate “A/B/C” и дальше короткий путь до “validation complete”. Это выглядит как **минимальная бюрократия ради максимальной ясности**.
- Ветка **B** у тебя явно включает **Query Catalog validation**, а ветка **C** — **ADR gate**. Это прям “high-leverage” правило: *по типу изменений подключаем нужный уровень контроля*.
- Есть **history с timestamp/reason** и **memory** (контекстные файлы, next\_gate) — это помогает не терять контекст между сессиями/участниками/агентами.

**Когда оправданность падает до 3–4/10:** если это начнёт требовать ручных обновлений состояния чаще, чем реально помогает (люди перестают обновлять state → он становится мусором).

---

### 3) Стоящее фокуса: **5/10** (как отдельный “продукт”), **8/10** (как “тонкий слой” для качества)

Тут главный вопрос не “круто ли”, а “окупается ли”.

**Если твоя цель — сделать PAIP (продукт/МVP) быстрее**, то фокус на state machine должен быть **ограниченным**:

- держать 3–7 шагов,
- фокусироваться только на “дорогих ошибках” (DB изменения без QC, контракт без ADR, отсутствие acceptance evidence),
- максимум — автоматизировать “подскажи что дальше” и “проверь готовность”.

**Если твоя цель — строить агентно-управляемую разработку (LLM/агенты),** то это прям **очень стоящее фокуса**, потому что агентам нужна:

- формальная стадия,
- допустимые переходы,
- список ожидаемых артефактов,
- предсказуемое “следующее действие”.

В этом сценарии state machine — не “велосипед”, а **интерфейс управления**.

---

## Где ты реально “не изобретаешь велосипед”, а делаешь полезную вещь

В твоём варианте ценность не в “state machine”, а в трёх вещах:

1. **Scope Gate A/B/C** — это хорошая “классификация изменения”\
   Это похоже на risk-based процесс: чем рискованнее изменение, тем больше обязательных проверок.

2. **Интеграция с артефактами качества** (QC/ADR/итерационные baseline-чеклисты)\
   Это уже не “статусы ради статусов”, а управление качеством и трассируемостью.

3. **CLI/скрипт, который выдаёт контекст и next actions**\
   Это превращает процесс в помощника, а не в регламент “на бумаге”.

---

## Главные риски (куда обычно уезжает “велосипедостроение”)

1. **Слишком подробная модель реальности**\
   Если начнёшь моделировать “кодинг → ревью → фиксы → ревью2 → QA → …” до 30 состояний, ты построишь мини-Jira, только хуже.

2. **Дрейф состояния**\
   Если обновление state не встроено в естественный поток (PR/CI/hooks), люди будут забывать → автомат станет недостоверным.

3. **Отсутствие “гардов” (preconditions)**\
   Сейчас переходы — это в основном “описание пути”. Максимальный буст ценности появляется, когда переход **нельзя сделать**, пока не выполнены условия (тесты, QC, ADR, заполнены ссылки на AT/evidence).

---

## Что бы я сделал, чтобы это стало “точно стоит фокуса”, но без раздувания

Если хочешь максимальный ROI, 3 улучшения (в порядке отдачи):

1. **Guards на переходах**\
   В DDL добавить что-то вроде `requires: ["just test", "qc-validate"]` или ссылки на артефакты (`docs/iterations/.../acceptance.md` содержит AT-ids).\
   И `advance` должен уметь:
   - либо проверять и блокировать переход,
   - либо хотя бы печатать “переход запрещён: не выполнено X”.

2. **Автосинхронизация с реальностью**\
   Минимум: CI job, который проверяет “если ветка B — QC валидируется”.\
   И/или pre-push hook, который напоминает.

3. **Визуализация графа**\
   Автоматически генерить Mermaid диаграмму из compiled edges → это резко повышает понятность команде.

---

## Итог в одной фразе

- **Велосипед (концепт): да, частично.** Это известная идея.
- **Велосипед (реализация под твою задачу): нет, это нормальная инженерная “маленькая колесная база”.**
- **Фокус:** стоит держать, но **как “тонкий quality-gate слой”**, а не как отдельный большой продукт, *если твоя главная цель — MVP PAIP*. Если цель — агентная разработка/управление качеством в репе, то можно смело развивать.

Если хочешь, я могу дать более точную оценку “стоит/не стоит” именно **по твоим целям** (MVP скорость vs качество/аудит vs агентность) — но даже без этого: текущий размер автомата у тебя выглядит здоровым и не “перебюрократизированным”.


#### You:
я действительно строю  агентно-управляемую разработку. напиши задачу для моего агента чтобы он создал guards, pre-push hook который проверяет и падает если проверка провалена, написал инструмент для визуализации графа и шаблон markdown файла с пояснениями и самой диаграммой состояния. И ещё сам подумай, что ему реализовать и какой выбрать дизайн.

#### ChatGPT:
Ниже — готовая **задача (ticket/spec)** для твоего агента. Я заложил дизайн так, чтобы это было “process-as-code” и работало одинаково для: **advance**, **pre-push**, и **документации** (diagram-as-code), без новых зависимостей.

---

# Задача: Guards + pre-push enforcement + визуализация SDLC state machine (process-as-code)

## Контекст

В репозитории уже есть:

- DDL процесса: `docs/_meta/process/sdlc-task-flow.ddl.yaml`
- Runtime state: `docs/_meta/process/sdlc-task-flow.state.yaml`
- Компилятор/CLI: `src/paip/process_compiler.py`
- Git hook: `.githooks/pre-push` (сейчас пушит git-notes)
- QC валидатор: `scripts/qc_validate.py` + `just qc-validate`
- Итерационные чеклисты: `docs/iterations/<ITER>/reviews.md` (checkbox + Sign-off)

Цель: сделать SDLC действительно **agent-enforced**:

1. Guards формализованы в DDL и могут запускаться как проверки.
2. `pre-push` запускает guards и **ломает push**, если must-guards не выполнены.
3. Есть инструмент, который генерирует **Mermaid-диаграмму** графа и Markdown-док (по шаблону).

## Итоговые артефакты (deliverables)

1. Поддержка **guards** в DDL и их исполнение:
   - оценка guards для текущего state/step/branch,
   - блокировка `advance`, если must-guards не пройдены (с возможностью bypass).
2. Обновлённый `.githooks/pre-push`:
   - сначала запускает guard-check (и падает при fail),
   - затем выполняет текущую логику sync git-notes (как сейчас).
3. Инструмент визуализации графа:
   - генерация Mermaid (flowchart предпочтительно),
   - генерация Markdown-документа по шаблону (вставляет диаграмму + метаданные).
4. Markdown-шаблон документа процесса (template):
   - пояснения, как читать/использовать,
   - место для диаграммы,
   - (опционально) таблица шагов/guards.
5. Обновления docs + тесты:
   - обновить `docs/_meta/process/compiler.md` (описать guards + новые команды),
   - добавить/обновить тесты в `tests/test_process_compiler.py` (guard-engine, when-фильтры, fail behavior).

---

## Дизайн (обязательный)

### 1) Схема guards в DDL

Добавить поддержку guards на 2 уровнях:

- **process-level guards** (общие правила для всего процесса)
- **step-level guards** (требования для конкретного шага)

Минимально достаточно step-level, но process-level даёт сильный выигрыш для pre-push (например, всегда требовать зелёные тесты).

#### Предлагаемый формат GuardDef (JSON-compatible YAML)

Guard — объект с полями:

- `id`: string (уникальный в рамках списка)
- `title`: string (коротко “что проверяем”)
- `level`: `"must"` | `"should"` (default: `"must"`)
- `phase`: список фаз, где guard должен выполняться: `["advance"]`, `["push"]`, `["ci"]`, или `["any"]`
- `kind`: `"command"` | `"file_exists"` | `"file_glob"` | `"markdown_checklist"`
- `when`: опциональный фильтр применимости:
  - `branch_in`: `["A","B","C"]`
  - `step_in`: `["scope_gate", ...]`
  - `status_in`: `["in_progress","blocked","done"]`
- параметры по kind:
  - `command`: `cmd` (string), опционально `timeout_sec`, `cwd`
  - `file_exists`: `path`
  - `file_glob`: `glob` (string) ИЛИ `globs` (list)
  - `markdown_checklist`: `path`, `section`, `require_all_checked` (bool), `require_signoff` (bool)

#### Тэмплейтинг (важно)

Поля `cmd`, `path`, `glob` должны поддерживать подстановки через `.format_map()`:

- `{branch}` (из state.branch)
- `{current_step}` (из state.current\_step)
- `{status}` (state.status)
- `{iteration}` (автоматически найденная “текущая итерация” = последняя папка в `docs/iterations/`)
- любые ключи `state.memory` доступны как `{<key>}` (например `{adr_path}`)

Если placeholder не найден — guard должен **fail** с понятным сообщением (это обычно дефект состояния/конфига).

### 2) Где и как исполнять guards

Добавить в `src/paip/process_compiler.py`:

- pydantic-модели для GuardDef/GuardWhen
- функции:
  - `collect_applicable_guards(ddl, state, step_id, phase) -> list[GuardDef]`
  - `run_guards(...) -> list[GuardResult]`
  - `format_guard_report(results) -> str`
- `GuardResult` (dataclass или pydantic):
  - `id`, `title`, `ok`, `level`, `phase`, `details` (строка), `stdout`, `stderr` (для command)

**Exit semantics**:

- если есть хоть один `must` guard с `ok=False` → exit code `1`
- `should` guard:
  - по умолчанию не валит процесс (но печатает WARN),
  - опция `--strict` превращает should в “как must” (exit 1).

### 3) Интеграция с `advance`

`python -m paip.process_compiler advance ...` должен:

- перед сменой шага запускать guards для `phase=advance` на **текущем шаге**
- если fail → не менять state и вернуть ошибку

Добавить флаг bypass:

- `--no-guards` (или `--force`) чтобы позволить “продавить” переход (но печатать предупреждение).

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

- `--phase` (default: `advance`)
- `--strict`
- `--json` (машиночитаемый вывод)
- `--root` (default `"."`) — для относительных путей/итераций/выполнения команд

### B) `render` (диаграмма)

Генерит Mermaid диаграмму в stdout или в файл:

```bash
PYTHONPATH=src python -m paip.process_compiler render \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --out docs/_meta/process/sdlc-task-flow.mmd
```

Фичи:

- формат: Mermaid **flowchart** (предпочтительно)
- shape по типам шагов:
  - gate: decision `{{ }}`
  - action: process `[ ]`
  - terminal: `(( ))`
- подписи на ребрах: `label` + `description` (склеить компактно)
- если передан `--state`, подсветить `current_step` (через `classDef`/`class`)

### C) `render-doc` (Markdown по шаблону)

```bash
PYTHONPATH=src python -m paip.process_compiler render-doc \
  --ddl docs/_meta/process/sdlc-task-flow.ddl.yaml \
  --state docs/_meta/process/sdlc-task-flow.state.yaml \
  --template docs/_meta/process/process-doc.template.md \
  --out docs/_meta/process/sdlc-task-flow.md
```

- заполняет placeholders: `$PROCESS_ID`, `$VERSION`, `$DDL_PATH`, `$STATE_PATH`, `$GENERATED_AT`, `$MERMAID`
- (опционально) генерит `$STEPS_TABLE` и `$GUARDS_TABLE`/`$GUARDS_SECTION`

---

## Pre-push hook (обязательное поведение)

Файл: `.githooks/pre-push`

Требования:

1. Сохранить существующую логику синка `refs/notes/commits`.
2. Добавить запуск guard-check **до** пуша notes:
   - если guards fail → печатаем отчёт и `exit 1` (push должен упасть)
3. Добавить bypass:
   - `PAIP_SKIP_GUARDS_PUSH=1` → пропускаем guard-check
   - текущий `PAIP_SKIP_NOTES_PUSH=1` оставить как есть

Технически:

- определить repo root: `git rev-parse --show-toplevel`
- выбрать python:
  - если есть `.venv/bin/python` → использовать
  - иначе `python3`
- запуск:
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
   - `kind=command`, `cmd="just test"`
2. Step `query_catalog_gate` (phase=advance + push): QC валидация
   - `cmd="just qc-validate"`
3. Step `adr_gate` (phase=advance): ADR существует по указателю из memory
   - `kind=file_exists`, `path="{adr_path}"`
   - `when.branch_in=["C"]`
   - (и в описании: “agent обязан записать state.memory.adr\_path”)
4. Опционально, но очень полезно для “done”: Validation baseline в reviews.md
   - `kind=markdown_checklist`
   - `path="docs/iterations/{iteration}/reviews.md"`
   - `section="Validation Baseline"`
   - `require_all_checked=true`, `require_signoff=true`
   - `when.step_in=["validation_gate"]`
   - `level="should"` (или must, если хочешь “только зелёные pushes после done”)

---

## Markdown template (создать новый файл)

Создать: `docs/_meta/process/process-doc.template.md`

Содержание (скелет):

- заголовок (process\_id/version)
- “как пользоваться” (команды guards/advance/render-doc)
- “где лежит state”
- Mermaid блок (placeholder `$MERMAID`)
- (опционально) список шагов/guards

Плейсхолдеры использовать через `string.Template`:

- `$PROCESS_ID`
- `$VERSION`
- `$DDL_PATH`
- `$STATE_PATH`
- `$GENERATED_AT`
- `$MERMAID`
- `$STEPS_TABLE` (если сделаешь)
- `$GUARDS_SECTION` (если сделаешь)

Также сгенерировать и закоммитить готовый документ:

- `docs/_meta/process/sdlc-task-flow.md` (через render-doc)

---

## Тесты (обязательные)

Расширить `tests/test_process_compiler.py`:

- `test_guards_command_pass`:
  - guard `command` с `python -c "exit(0)"` → PASS
- `test_guards_command_fail_blocks_advance`:
  - guard `command` с `python -c "exit(1)"` → advance должен падать
- `test_when_filters`:
  - guard с `when.branch_in=["B"]` не должен запускаться при branch A
- `test_template_render_includes_edges`:
  - render mermaid содержит основные ноды и ребра

(Важно: тесты не должны зависеть от `just` и внешних бинарей — в тестах используй `python -c`.)

---

## Документация (обязательные правки)

Обновить `docs/_meta/process/compiler.md`:

- добавить раздел “Guards”
- описать schema guard’ов
- примеры запуска `guards`, `advance`, `render`, `render-doc`
- описать поведение pre-push (и переменные bypass)

---

## Definition of Done

- `python -m paip.process_compiler guards ...` работает и даёт понятный отчёт.
- `advance` блокируется must-guards, есть bypass флаг.
- `.githooks/pre-push` валит push при must-fail (и сохраняет notes-sync).
- `render` генерит Mermaid flowchart, `render-doc` генерит Markdown из template.
- DDL обновлён и содержит хотя бы 2–3 реальных guards.
- Все тесты зелёные: `just test`.

---

## Доп. рекомендации (если останется время)

1. Сделать `--json` вывод стабильно пригодным для CI (массив результатов + summary).
2. Добавить “короткий режим” в `guards`: `--quiet` (только ошибки).
3. В отчёте guards печатать “как починить” (remediation hints) для типовых fail:
   - “нет .venv → запусти just setup”
   - “не установлены QC deps → just qc-setup”
4. (Опционально) обновить `scripts/print_project_state.py`, чтобы он дополнительно показывал **guard status** для текущего шага (без дублирования тяжелых команд).

---

Если хочешь, я могу сразу предложить конкретный **патч-стиль пример** для DDL (с guards) и пример содержимого `process-doc.template.md` — но даже в текущем виде агенту достаточно, чтобы реализовать целиком без уточнений.
