# Branch · Альтернативы Microsoft Agent Framework

#### You:
Какая сейчас есть реальная альтарнатива Microsoft Agent Framework? Кажется что это беспроигрышный выбор. Например, если я хочу построить систему автоматизации разработки, я обязан создать управление рабочими процессами через FSM. И FSM должна быть написана при участии DSL по моему SDLC.

#### ChatGPT:
Понял: я кратко сравню реальные альтернативы Agent Framework (по экосистемам и сценариям), и затем предложу архитектуру для “автоматизации разработки” с FSM + DSL, включая какие инструменты лучше подходят и почему.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Если под **Microsoft Agent Framework (MAF)** вы имеете в виду новый open‑source SDK/runtime из экосистемы Azure AI Foundry (преемник Semantic Kernel + AutoGen), то да — это сейчас очень сильный вариант. Причём **на 19 февраля 2026** он уже в статусе **Release Candidate** для **.NET и Python** (API стабилизирован, фичи для 1.0 завершены). citeturn13view0\
Но «беспроигрышность» зависит от того, что именно вы строите: **agent SDK** или **движок процессов (FSM/Workflow engine)**.

Ниже — реальные альтернативы “сегодня”, и как я бы увязал это с вашим тезисом про **FSM + DSL под SDLC**.

---

## 1) Реальные альтернативы MAF как *agent/orchestration framework* (open-source / code-first)

### LangGraph (LangChain ecosystem)

Если вам важно **явно описывать управление** (граф/состояния/переходы), а не “верить LLM”, LangGraph — одна из самых практичных альтернатив.

- Заточен под **долгоживущие stateful‑workflow/agent** сценарии: durable execution, human‑in‑the‑loop, память, дебаг/трассировка через LangSmith. citeturn4view2
- LangGraph 1.0 выпущен (стабильность интерфейсов до 2.0 заявлена командой). citeturn7view0

Когда подходит: вы хотите “оркестратор как граф”, где LLM — один из узлов, а не “главный диспетчер”.

---

### OpenAI Agents SDK (Python/TypeScript)

Если вам нужен **минималистичный SDK** с сильными примитивами и наблюдаемостью, который удобно встроить в свой контрол‑плейн.

- Примитивы: agents, handoffs (агент как tool для другого агента), guardrails, встроенный tracing. citeturn5view0turn4view1
- Есть **sessions** (память), **human‑in‑the‑loop**, и встроенная интеграция с **MCP tool calling**. citeturn5view0
- OpenAI прямо позиционирует как “production‑ready upgrade” поверх Swarm. citeturn5view0turn4view1

Когда подходит: вы хотите собрать свою архитектуру (FSM/Temporal/Step Functions), а Agents SDK использовать как “движок агентного шага”.

---

### PydanticAI (Python)

Если у вас в приоритете **типобезопасность/валидация/контракты** (что обычно критично для “автоматизации разработки”).

- Позиционируется как agent framework с упором на **type-safety**, model‑agnostic подход и удобную разработку. citeturn5view3
- Важное для SDLC‑автоматизации: есть механика **tool approval (human‑in‑the‑loop)** и заявлена **durable execution** для долгих сценариев. citeturn5view3

Когда подходит: вы хотите “LLM‑шаги строго по схеме”, много structured output и строгих контрактов.

---

### CrewAI (Python)

Хорошая альтернатива, если вы мыслите “команда ролей” + “управляющий flow”.

- CrewAI описывает **Flows** как “backbone”: event‑driven workflow, управление состоянием, ветвления/циклы и контроль исполнения. citeturn5view2

Когда подходит: быстро собирать multi-agent команды и поверх них иметь более детерминированный управляющий слой.

---

### Google ADK (Agent Development Kit) (Python/TS/…)

Реальная альтернатива, если вам важна **модульность и совместимость** и/или вы смотрите в сторону Google/Vertex.

- ADK — open‑source, **model‑agnostic** и **deployment‑agnostic**, задуман “как нормальная разработка ПО”, с оркестрацией от простых задач до сложных workflow. citeturn4view3
- В экосистеме Vertex AI Agent Builder: есть “Agent Garden” и разделение на готовые agents и tools, которые можно подключать в свои агенты через ADK. citeturn6view3
- Есть отдельный анонс ADK для TypeScript (code-first подход). citeturn12search3

Когда подходит: вы хотите “поставщика-нейтрально”, но с сильной опцией управляемого прод‑хостинга в GCP.

---

## 2) Альтернатива MAF как *managed agent service* (если вам нужен сервис, а не только SDK)

### AWS Bedrock Agents

Если вы в AWS и хотите управляемую оркестрацию с инструментами/KB.

- Оркестрация описана как цикл: модель выбирает действие (action group) или запрос к knowledge base, есть trace, сохраняется история сессии. citeturn4view4
- Action groups завязаны на **OpenAPI schema + Lambda** как исполнение операций. citeturn4view4
- Есть режим **custom orchestration** (если встроенной логики мало). citeturn1search7turn1search8

---

### Vertex AI Agent Builder / Agent Engine (Google)

Если вам нужен “платформенный” уровень (governance/scale/deploy) вокруг агентов. citeturn2search0turn2search4\
(Обычно в пару к этому берут ADK как SDK.)

---

## 3) Про ваш тезис: «для автоматизации разработки я обязан FSM + DSL»

Вы **не обязаны** писать FSM “вручную” как самописный интерпретатор. На практике лучше разделить:

- **Control plane (детерминированный процесс)**: FSM/Workflow engine, аудит, ретраи, компенсации, ожидания, approval.
- **Agent plane (интеллектуальные шаги)**: LLM/agents как *activities* внутри процесса.

Это ровно то, что (кстати) даже MAF подчёркивает концептуально:\
если шаги процесса хорошо определены — берите workflow; если можно написать обычную функцию — лучше функция, чем агент. citeturn4view0

### Если вам нужна “FSM + DSL” — вот прямые кандидаты (и это часто лучшая «альтернатива» любому agent framework):

- **AWS Step Functions**: “основан на state machines”, workflow описывается DSL **Amazon States Language (ASL)**. citeturn8search9
- **Azure Durable Functions**: пишете orchestrator functions, а платформа берёт на себя state/checkpoints/restarts. citeturn8search1
- **Temporal**: платформа для **durable execution** и долгоживущих workflow (дни/недели/месяцы). citeturn8search10turn8search3
- **Camunda / Zeebe**: workflow engine для процессов (часто с BPMN/DMN как “DSL для бизнеса”). citeturn8search5turn8search18

### Как это выглядит архитектурно для SDLC‑автоматизации

1. Вы описываете ваш SDLC в DSL (YAML/JSON/BPMN/ASL) как **граф состояний**: шаги, переходы, guard‑условия, точки “human approval”.
2. DSL компилируется в:
   - Step Functions state machine / Temporal workflow / Durable Functions orchestration\
     **или**
   - LangGraph/MAF workflow graph
3. Каждый state вызывает:
   - deterministic task (CI, линтер, сборка, деплой)
   - agentic task (план, генерация патча, анализ логов) через LangGraph/OpenAI Agents SDK/PydanticAI/MAF

Мини‑пример (идея DSL, не привязана к движку):

```yaml
states:
  plan:
    type: llm
    output_schema: PlanV1
    next: implement

  implement:
    type: tool
    action: create_branch_commit
    next: test

  test:
    type: tool
    action: run_ci
    on_success: open_pr
    on_failure: plan

  open_pr:
    type: tool
    action: create_pull_request
    next: approval

  approval:
    type: human
    next: merge

  merge:
    type: tool
    action: merge_and_tag
    next: done
```

Ключевая мысль: **FSM/Workflow — это “контур управления”, агент — это “исполнитель шага”**. Тогда вы сможете:

- менять agent framework без переписывания SDLC‑машины,
- держать audit trail, ретраи, таймауты, approval на уровне workflow engine,
- ограничивать agent’а рамками разрешённых переходов/инструментов.

---

## 4) Быстрый выбор “что брать вместо MAF” под вашу задачу

Если упростить до “что реально заменит MAF”:

- Хотите **явный граф, контроль, долговечность** (и вас устраивает Python/TS): **LangGraph**. citeturn4view2turn7view0
- Хотите **простые примитивы + трассировка + guardrails**, а control‑plane делаете сами: **OpenAI Agents SDK**. citeturn5view0turn4view1
- Хотите **строгую типизацию и валидацию** вокруг LLM‑шагов: **PydanticAI**. citeturn5view3
- Хотите “команда ролей + flow” из коробки: **CrewAI**. citeturn5view2
- Вы в GCP/хотите совместимость и code-first: **Google ADK (+ при желании Vertex Agent Builder/Engine)**. citeturn4view3turn2search0
- Вы в AWS и хотите managed: **Bedrock Agents**. citeturn4view4turn1search7

А если ваша главная потребность именно **FSM+DSL под SDLC**, то часто правильный “заменитель MAF” — это вообще **Temporal / Step Functions / Durable Functions / Zeebe**, а agent framework выбирается вторым слоем. citeturn8search9turn8search1turn8search10turn8search5

---

В качестве ориентира: MAF сейчас уже RC и действительно закрывает “agent + workflows” в одном месте (графовые workflows, checkpointing, human-in-the-loop, поддержка стандартов вроде MCP/A2A). citeturn13view0turn6view0 Но если вы заранее знаете, что SDLC‑процессы должны быть детерминированы DSL‑ом — **я бы ставил workflow engine в центр**, а агентные SDK держал взаимозаменяемыми.

navlistСвежие материалы про платформы для AI‑агентов и их эксплуатациюturn9news39,turn2news38,turn12news42,turn12news41


#### You:
если поставить workflow engine в центр, то какие отвественности я должен реализовать и в каком порядке?

Суть заключается в следующем:

# How I see the world
Я хочу зациклить разработку через Codex агента. Он должен будет брать задачу и самостоятельно проводить её по SDLC до момента, когда потребуется моё вмешательство.
## Environment
- macos
## Actors
- Nick
- Codex Agent
## Goals
- maximize SDLC automation 
## Resources
### Tools
- macbook
- all internet
### Human Attention
- Nick: Owner, Architect, Evangelist, Developer; 4h per day;

#### ChatGPT:
Понял: я предложу практичную схему “workflow engine в центре” именно для вашего кейса (Codex‑агент, macOS, 4 часа внимания в день): разложу ответственности по слоям, дам порядок внедрения (MVP → production), и покажу как организовать циклы SDLC с точками вашего вмешательства.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Если **workflow engine** в центре, то вы строите “контур управления” (deterministic control‑plane), а **Codex** становится **исполнителем шагов** (agent/worker). Тогда SDLC‑автоматизация получается устойчивой: LLM может ошибаться, но **процесс**, **гейты**, **ретраи**, **аудит**, **лимиты** — детерминированы.

Ниже — какие ответственности вам реально надо реализовать (вокруг движка) и **в каком порядке**. Я буду опираться на то, что вы хотите “зациклить” разработку через Codex (локально на macOS), и что у вас есть 4 часа внимания в день.

---

## 1) Что даёт Codex “из коробки” (чтобы не дублировать это в workflow)

Это важно, потому что часть “safety/execution” можно **не писать самим**:

- **Codex CLI** можно запускать локально: он умеет читать/менять/запускать код в выбранной директории (macOS/Linux), и он open‑source. citeturn1view1
- У Codex есть **песочница + политика подтверждений**: по умолчанию **сеть выключена**, запись ограничена рабочей папкой; опасные действия требуют подтверждения. citeturn1view0
- Для автоматизации есть **`codex exec` (non‑interactive)**: его можно вызывать из скриптов/CI, получать **JSONL‑стрим событий** (`--json`) и/или требовать **структурированный финальный ответ по JSON Schema** (`--output-schema`). citeturn3view0turn3view1
- Codex читает **AGENTS.md** (глобально и в проекте) — это отличный “мягкий DSL” для ваших SDLC‑соглашений (как тестировать, что считать DoD, когда спрашивать подтверждение). citeturn1view2
- Есть “Skills” (пакеты инструкций/скриптов), которые можно использовать как повторяемые шаги SDLC. citeturn1view3

Вывод: ваш workflow‑контур может опираться на Codex как на **sandboxed runner**, а сам фокусироваться на **оркестрации, политике и жизненном цикле SDLC**.

---

## 2) Ответственности при “workflow engine в центре” (что вы должны реализовать)

Я разделю на 7 слоёв. Это почти универсально для любого движка (Temporal/Step Functions/Durable/etc.).

### A) SDLC‑модель и DSL (истина процесса)

Это то, что превращает “agent что‑то делает” в управляемую фабрику.

Вам нужно:

1. **Модель состояния (FSM/HSM)**: стадии SDLC + события + переходы.\
   Минимум: `Intake → Plan → Implement → Test → PR → Review → Merge → Done/Abort`.
2. **DSL/спецификация workflow** (YAML/JSON/BPMN — неважно):
   - типы шагов: `tool`, `agent`, `human`, `wait(event)`, `choice`, `loop`
   - входы/выходы шагов (схемы), контракты
   - allowed‑tools/permissions per step
3. **Версионирование процесса**: `sdlc.workflow.v1`, `v2` и правила миграции (что делать с “in‑flight” задачами).

> Это “центр тяжести” вашей системы. Если он плохой — всё остальное будет разваливаться.

---

### B) Контур управления (policy + approvals + бюджеты)

Без него автоматизация быстро упрётся в риски и “бесконечные циклы”.

Вам нужно:

1. **Политика автономности (levels of autonomy)**:
   - что можно делать без Nick
   - что требует “OK” (план, сетевой доступ, новые зависимости, миграции, деплой и т. п.)
2. **Бюджеты/лимиты**: max итераций “почини тесты”, max минут на шаг, max токенов/стоимости, max файлов/строк за итерацию.
3. **Kill switch / circuit breaker**: остановить run, если: слишком много правок, подозрительные команды, нестабильность.

Codex сам по себе уже осторожный (сеть по умолчанию выключена и есть approvals). citeturn1view0\
Но именно workflow должен решать **когда** просить Nick и **когда** прекращать “пытаться ещё раз”.

---

### C) Исполнение шагов (workers / activities)

Workflow engine сам по себе не делает работу — он вызывает “активности”.

Вам нужно реализовать **набор idempotent‑активностей**:

- Git: clone/fetch, branch naming, commit, push, rebase
- CI/Test: run tests (локально или через CI), сбор логов, парсинг результата
- PR: создание PR, обновление, комментарии, запрос ревью
- Quality: линтеры, форматтеры, SAST/dep audit (минимум — запуск существующих скриптов репы)
- Release/Deploy (позже): version bump, changelog, staging deploy

Ключевой момент: **идемпотентность**. Любая активность должна уметь безопасно повториться (ретрай движка).

---

### D) Интеграция с Codex как с “agent step”

Тут у вас три реалистичных варианта интеграции (выбирайте любой; можно начать с простого):

1. **Shell‑интеграция через `codex exec`**\
   Плюсы: быстро, отлично для workflow. Можно получать JSONL‑события и схемы. citeturn3view0turn3view1
2. **Codex SDK (TypeScript)** — программно управлять thread’ами\
   Плюсы: больше контроля, чем у non‑interactive mode. citeturn5view2
3. **Codex как MCP‑server** — если вы строите оркестрацию через MCP‑клиента/агентную обвязку\
   Можно задавать sandbox/approval‑policy параметрами. citeturn4view1

В любом случае вам нужно определить:

- **шаблоны промптов/инструкций** (AGENTS.md + skills)
- **схемы выхода** (plan, change‑summary, risk‑report)
- **правила применения результата** (как применять diff/patch, как проверять, как откатывать)

Отдельно: `codex exec` обычно требует быть внутри git‑репозитория (как защита от разрушительных действий). citeturn3view0\
Это удобно: ваш workflow может требовать “workspace всегда git repo”.

---

### E) Execution environment (macOS) и безопасность

Вы хотите “all internet”, но это самый частый источник проблем (prompt injection, supply chain, утечки).

Вам нужно:

- **Стандартизированный workspace**: отдельная папка/пользователь/контейнер под каждую задачу
- **Политика сети**:
  - по умолчанию **без сети** (совпадает с дефолтом Codex) citeturn1view0
  - если сеть нужна — только через allowlist/approval (и логировать факт)
- **Секреты**: токены GitHub/Registry должны быть доступны **только** тем шагам, которым нужно, и не “утекать в промпты/логи”.

---

### F) Артефакты и наблюдаемость (то, что экономит Nick часы)

Если у вас 4 часа/день, самое ценное — **быстро понять**, что произошло и что нужно решить.

Вам нужно:

- **Артефакт‑store**: логи тестов, диффы, summary, plan, ссылки на PR, результаты анализаторов
- **Таймлайн run’а** (UI может быть даже CLI/Markdown):\
  “что сделано → что сломалось → что предложено → что нужно от Nick”
- **Единый “Inbox решений”**: список run’ов, где требуется вмешательство (approve plan, ответить на вопрос, сделать ревью)

Бонус: `codex exec --json` даёт поток событий (команды, изменения файлов, web‑search, план‑апдейты) — это удобно хранить как “протокол исполнения”. citeturn3view0turn3view1

---

### G) Evals/регрессии для вашей автоматизации

Иначе вы не поймёте, “стало лучше или хуже” после правок в навыках/промптах/политиках.

Вам нужно:

- набор типовых задач (5–20) как “контрольные”
- метрики: доля задач, дошедших до PR без Nick; доля задач, дошедших до merge; среднее число итераций “почини тесты”; сколько минут Nick тратит на run
- “красные флаги”: частота включения сети, новые зависимости, большие диффы

---

## 3) В каком порядке это внедрять (рекомендованная последовательность)

Ниже — порядок, который даёт максимальную отдачу и минимизирует риск/хаос.

### Шаг 0. Зафиксировать правила игры (1 файл + 1 таблица)

**Цель:** не дать агенту “выйти из берегов”.

Сделайте:

- **Autonomy policy**: что разрешено без Nick, что требует approval
- **Definition of Done** (DoD) в AGENTS.md: как тестировать, что считать “готово”, когда останавливаться citeturn1view2
- “запрещённые операции”: прямой push в main, деплой в prod, добавление зависимостей без approval, включение сети без approval, etc.

Почему сначала: потом вы будете автоматизировать быстрее и безопаснее.

---

### Шаг 1. “Скелет” workflow без Codex (чистая детерминированная труба)

**Цель:** проверить интеграции и модель процесса.

Мини‑workflow:

1. Intake (вручную: CLI команда “start task …”)
2. Create workspace + clone repo
3. Create branch
4. Run tests (или хотя бы `lint`)
5. Open PR “draft” (или создать патч/ветку без PR)

Это должно работать **на 100%** без LLM.\
Иначе при подключении Codex вы не поймёте, что ломается: агент или инфраструктура.

---

### Шаг 2. Артефакты + “Inbox решений”

**Цель:** сделать так, чтобы Nick тратил минуты, а не часы на понимание состояния.

Минимум:

- лог каждого шага
- ссылка на PR/ветку
- сводка: “что сделано / что не прошло / что требуется”

---

### Шаг 3. Подключить Codex только как *planner* (без правок кода)

**Цель:** начать получать ценность, но без риска.

Реализация:

- шаг `Plan` вызывает Codex (например через `codex exec`) и требует **структурированный план** (`--output-schema`) citeturn3view0turn3view1
- workflow создаёт approval‑шаг: Nick подтверждает план или уточняет требования

На этом этапе Codex не меняет код — он учится вашей SDLC‑логике и стилю.

---

### Шаг 4. Разрешить Codex “Implement” в песочнице + автотесты

**Цель:** первый настоящий автономный цикл.

- шаг `Implement` — Codex получает задачу + план + контекст
- шаг `Test` — запускаются тесты
- если тесты упали → loop: `Fix → Test` (с лимитом итераций/времени)

Здесь вам очень пригодится то, что у Codex есть sandbox/approval‑policy, и сеть по умолчанию выключена. citeturn1view0

---

### Шаг 5. PR‑пакет: summary, риск, что смотреть Nick

**Цель:** максимально разгрузить 4 часа/день.

Перед тем как попросить Nick о ревью:

- Codex генерирует PR‑summary (что поменялось, почему, какие риски, как тестировалось)
- workflow прикладывает артефакты (логи тестов, дифф‑стат)
- если риск низкий и все зелёное → можно настроить auto‑merge (позже)

---

### Шаг 6. Автономность повышается “по зонам”

**Цель:** не включать “полный автопилот” сразу.

Эскалация автономии:

- auto‑merge только для:
  - маленьких изменений
  - “низкорисковых” модулей
  - полностью зелёного CI
- деплой/прод — всегда с approval (как минимум сначала)

---

## 4) Как это выглядит как “контракт” между workflow и Codex (практично)

Вам выгодно стандартизировать agent‑шаги как функции вида:

**AgentStep(input) → AgentStepResult**

Где:

- `input`: task spec + current state + allowed tools + constraints + expected schema
- `result`:
  - `status`: ok/fail/needs\_human
  - `artifacts`: patch/branch/pr\_link/logs
  - `summary`: коротко для Nick
  - `requests_to_human`: конкретные вопросы/варианты

С `codex exec` это прям удобно:

- machine‑readable события (`--json`) и/или финальный объект по JSON Schema (`--output-schema`). citeturn3view0turn3view1

А SDLC‑соглашения вы кладёте в:

- `AGENTS.md` (глобально и в репе) citeturn1view2
- skills (повторяемые “процедуры”: “как делать релиз”, “как чинить CI”, “как писать миграции”) citeturn1view3

---

## 5) Как оптимизировать под Nick = 4 часа/день (самое важное)

Чтобы “максимизировать SDLC automation”, вам нужно минимизировать **два** типа человеческой работы:

1. **Понимание контекста**\
   Решение: обязать workflow всегда формировать “decision packet”:
   - 5–10 строк summary
   - what changed + why
   - как проверить локально
   - риск/impact
   - ссылку на PR и логи

2. **Рутинные решения**\
   Решение: правила‑гейты:
   - “новая зависимость?” → approval
   - “сетевой доступ?” → approval (или allowlist)
   - “касается auth/payment/infra?” → approval
   - “дифф > N строк?” → approval

Codex уже изначально осторожен с сетью и песочницей, но именно ваши workflow‑правила решают, что считать “опасным”. citeturn1view0

---

## Итоговая “очередь реализации” в 10 строк

Если совсем коротко, то порядок такой:

1. Autonomy policy + DoD (AGENTS.md) citeturn1view2
2. DSL/FSM модель SDLC и версии
3. Workspace sandbox (на macOS) + секреты/токены
4. Интеграции: git + tests/CI + PR
5. Артефакты + timeline + inbox решений
6. Codex как planner (структурированный output) citeturn3view0turn3view1
7. Codex как implementer (workspace‑write) + автотесты + loop с лимитами citeturn1view0
8. PR summary/risk пакет для Nick
9. Постепенный auto‑merge по правилам
10. Evals/метрики и hardening

---

Если хотите, я могу в следующем сообщении предложить **конкретный минимальный DSL** (YAML) под ваш SDLC (states + transitions + policies + schemas) так, чтобы Codex шаги вызывались через `codex exec` и возвращали структурированные результаты.


#### You:
Идея верная, но текущий вектор чуть другой. На текущем этапе я буду сам создавать workspaces и запускать агентов codex. Мне нужно чтобы у меня появился DSL, который поможет агенту и мне видеть состояние одинаково. Это то, что должно появиться в первой итерации.

#### ChatGPT:
Понял: в первой итерации делаем не движок, а **минимальный DSL “общего состояния”** для вас и Codex: единый формат задачи, текущего шага SDLC, артефактов, гейтов и следующих действий. Дам практичный YAML/JSON‑спек, примеры, правила переходов и шаблон AGENTS.md/промпта, чтобы Codex обновлял состояние.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Понял. Тогда в **итерации №1** вам нужен не “движок”, а **один канонический файл‑реестр (ledger)**: *DSL, который одновременно*

1. задаёт **ваш SDLC как FSM**, и
2. хранит **текущее состояние конкретной задачи** (что сделано, что дальше, где блокер, что нужно от Nick).

Codex и вы читаете/правите **один и тот же файл** → “состояние одинаково”, без догадок.

Ниже — вариант “минимально‑достаточно”, который реально работает уже сегодня в ручном режиме.

---

## 0) Ключевой принцип итерации №1

**Один источник правды:** `.sdlc/ledger.yaml`

- Вы: обновляете требования/ответы/разрешения, иногда вручную двигаете state.
- Codex: выполняет действия *и обязан* после каждого крупного шага обновлять ledger.
- Любая синхронизация происходит **через правку ledger**, а не “на словах”.

Чтобы Codex всегда начинал с правильного контекста, положите правила в `AGENTS.md` — Codex читает `AGENTS.md` перед началом работы. citeturn0search3

---

## 1) Что именно должен уметь ваш DSL (и что НЕ надо делать сейчас)

### DSL должен:

1. **Явно фиксировать текущий state** (FSM) и допустимые переходы
2. **Держать очередь next‑actions** (что агент делает дальше)
3. **Фиксировать блокеры/вопросы к Nick** в структурированном виде (варианты ответа + рекомендация)
4. **Хранить артефакты** (ветка, коммиты, команды тестов, ссылки на PR, краткие итоги)
5. **Иметь append‑only историю** (кто/когда/что сделал), чтобы не спорить “а было ли”.

### DSL НЕ должен (пока):

- исполнять шаги сам (это уже workflow engine),
- хранить секреты,
- пытаться описать весь мир (достаточно минимального контракта).

---

## 2) Файл `.sdlc/ledger.yaml` — готовый шаблон DSL (v0.1)

Скопируйте как есть в workspace (лучше в `.sdlc/ledger.yaml`). Это **ваш контракт**.

> Я специально сделал YAML “почти‑JSON” без сложных фич, чтобы агенту было трудно его сломать.

```yaml
spec: nick-sdlc-ledger/v0.1

context:
  environment: macos
  actors:
    owner: Nick
    agent: Codex
  goal: maximize_sdlc_automation
  constraints:
    owner_attention_hours_per_day: 4

task:
  id: "TBD"
  title: "TBD"
  repo_url: "TBD"
  workspace_path: "TBD"
  branch: "TBD"
  description: ""

policy:
  # "логические" разрешения. Даже если Codex технически может, он не должен, пока тут не разрешено.
  network_access: "ask"          # allow | deny | ask
  allow_dependency_changes: "ask" # allow | deny | ask
  max_fix_verify_loops: 3

process:
  name: "SDLC-lite"
  states: [intake, plan, implement, verify, deliver, waiting_human, done]
  transitions:
    intake: [plan]
    plan: [implement, waiting_human]
    implement: [verify, waiting_human]
    verify: [implement, deliver, waiting_human]
    deliver: [waiting_human, done]
    waiting_human: [plan, implement, done]
    done: []
  gates:
    verify:
      required_checks: [tests, lint]

run:
  state: intake                  # one of process.states
  status: ready                  # ready | doing | waiting_human | blocked | done
  iteration: 0                   # increment when looping implement<->verify
  next_actions: []               # list of action IDs in priority order
  updated_at: null               # ISO timestamp

actions: []                      # backlog for this task (agent + human)
# each action:
# - id: A1
#   type: agent | tool | human
#   title: "..."
#   status: todo | doing | done | blocked | skipped
#   notes: ""

checks:
  tests:
    command: "TBD"               # e.g. "make test" / "npm test" / ...
    status: na                   # na | pass | fail
    last_run: null
    evidence: ""
  lint:
    command: "TBD"
    status: na
    last_run: null
    evidence: ""

artifacts:
  commits: []                    # list of commit SHAs
  pr_url: null
  change_summary: ""             # short, reviewer-friendly
  logs: []                       # e.g. paths to log files

needs_human: []                  # structured questions/decisions
# each item:
# - id: H1
#   blocking: true
#   state_when_asked: implement
#   question: "..."
#   options: ["...", "..."]
#   recommendation: "..."
#   answer: null                 # Nick fills in
#   status: open                 # open | answered | obsolete
#   notes: ""

history: []                      # append-only event log
# each event:
# - seq: 1
#   ts: "2026-02-20T10:00:00+07:00"
#   actor: Nick | Codex
#   type: init | state_change | action_update | check_run | question | note
#   message: "..."
```

### Минимальные инварианты (чтобы “состояние было одинаковым”)

1. `run.state` всегда ∈ `process.states`
2. Переход state возможен только если `run.state -> new_state` ∈ `process.transitions[run.state]`
3. Если есть `needs_human` с `blocking: true` и `status: open`, тогда `run.status` **должен** быть `waiting_human` (и агент должен остановиться)
4. `history` — только дописываем (append), `seq` монотонно растёт.

---

## 3) `AGENTS.md` — “протокол поведения” для Codex (обязательно)

Codex читает `AGENTS.md` перед началом работы, так что это самый простой способ заставить его **всегда** синхронизироваться через ledger. citeturn0search3

Положите в корень workspace (рядом с репозиторием):

```md
# How to work in this workspace (must follow)

## Single source of truth
- The canonical task state is in: .sdlc/ledger.yaml
- Before doing anything: read .sdlc/ledger.yaml and summarize the current `run.state`, `run.status`, `next_actions`, and any open `needs_human`.

## State transitions
- You must only move `run.state` using allowed transitions from `process.transitions`.
- After any meaningful step, update:
  - run.state / run.status / run.updated_at
  - actions statuses (if relevant)
  - checks (if you ran them)
  - artifacts (commits, PR url, change_summary)
  - append one entry to `history`

## When to stop and ask Nick
- If any blocking `needs_human` item exists (status=open), set `run.status: waiting_human` and STOP.
- If you need network access or dependency changes and policy says "ask", create a blocking `needs_human` item with options + recommendation and STOP.
- Nick has 4h/day attention budget: consolidate questions, be concrete, offer options.

## Safety / scope
- Do not introduce unrelated refactors.
- Do not store secrets in ledger/history.
- Do not proceed if the ledger is inconsistent; instead, add a blocking `needs_human` item describing the inconsistency.
```

---

## 4) Как вы будете работать “вручную” уже на первой итерации (ритуал)

### Инициализация (делаете вы, 2–5 минут)

1. Создаёте workspace и кладёте:
   - `.sdlc/ledger.yaml` (шаблон)
   - `AGENTS.md` (протокол)
2. Заполняете в ledger:
   - `task.id`, `task.title`, `task.repo_url`, `task.workspace_path`, `task.branch`
   - `checks.tests.command` и `checks.lint.command` (если есть)
3. Добавляете первые actions, например:
   - `A1: уточнить acceptance criteria`
   - `A2: сделать план`
   - `A3: реализовать`
     И выставляете `run.next_actions: [A1, A2]`

### Запуск Codex (каждая “сессия”)

Вы даёте один и тот же высокий промпт (важно: **не рассказываете состояние в тексте**, оно в ledger):

- “Открой `.sdlc/ledger.yaml`, следуй `AGENTS.md`. Выполни `run.next_actions` по порядку. После каждого действия обнови ledger. Если нужен Nick — создай blocking `needs_human` и остановись.”

### Ваше вмешательство (только когда нужно)

Вы открываете ledger и:

- отвечаете в `needs_human[].answer`,
- при необходимости меняете `run.next_actions`,
- переводите `run.status` обратно в `ready`.

---

## 5) Нюанс про internet / sandbox (чтобы не было сюрпризов)

Даже если “ресурс — весь интернет”, **в Codex по умолчанию сеть может быть выключена** в sandbox‑режиме `workspace-write` (это нормально и безопасно). citeturn0search2turn0search11\
Поэтому в `policy.network_access` вы фиксируете “логическое разрешение”, а реально включать сеть (если нужно) — через конфиг Codex/настройки sandbox/approvals. citeturn0search6

В первой итерации можно вообще держать `network_access: ask` и включать только когда реально упёрлись.

---

## 6) Почему это точно “первая итерация” и хороший фундамент

- Вы уже получаете **общее состояние** (Nick ↔ Codex) без workflow engine.
- Позже вы сможете:
  - либо написать небольшой “runner”, который читает `.sdlc/ledger.yaml` и вызывает Codex/скрипты,
  - либо переехать на полноценный workflow engine, почти без изменения DSL (он станет его входом/выходом).

---

Если хотите, я сделаю следующий шаг без “движка”:\
дам **второй файл** `process.yaml` (описание FSM отдельно) + `run.yaml` (инстанс), чтобы Codex **никогда** не трогал определение процесса, а правил только состояние. Это ещё сильнее снижает риск “агент случайно поменял правила SDLC”.


#### You:
Спланируй заново, я подготовил исследование по ландшафту решений.

#### ChatGPT:
Ок — сейчас перечитаю ваш PDF и перепланирую “итерацию №1” вокруг DSL/IR так, чтобы он был future‑proof (plan/run/apply), но работал уже при ручных workspaces и ручном запуске Codex.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Ок, пересобираю план **от вашего исследования**: вы сами хорошо зафиксировали, что “одного OSS, закрывающего всё из коробки” почти нет, поэтому **правильная первая итерация — стабильный промежуточный контракт (IR/DSL) + plan/run/apply вокруг него**, а бэкенды (Temporal/Tekton/Jenkins/агенты) подключаются адаптерами. fileciteturn0file0

Ниже — новый план, где **Итерация №1 = DSL, который делает “состояние одинаковым” для вас и Codex**, при том что workspaces и запуск Codex вы делаете руками.

---

## Что меняется по сравнению с прошлым планом

1. **Не “ledger всё-в-одном”**, а **IR‑набор файлов** (ProcessSpec / CheckSpec / StateSnapshot / EventLog / ExecutionPlan).\
   Это прямо соответствует вашей “future‑proof” идее на стр. 3 (контракт IR + адаптеры), и снимает проблему “FSM ≠ DAG” (стр. 9): FSM живёт в ProcessSpec, а “что запускать” компилируется в ExecutionPlan. fileciteturn0file0

2. **Функции plan/run/apply** — даже если вы пока исполняете вручную.\
   Это даёт повторяемость и одинаковое понимание статуса (стр. 2 и стр. 11). fileciteturn0file0

3. **Decision history** вы логируете сами (append‑only events.jsonl), потому что “event history есть, а decision history — нет” повторяется почти у всех кандидатов (стр. 9 и стр. 12). fileciteturn0file0

---

## Итерация №1 (цель): DSL/IR как единая “правда” о процессе и состоянии

### Definition of Done для итерации №1

Считайте итерацию успешной, если:

- В любой момент, открыв `.sdlc/state.yaml`, вы и Codex **одинаково** отвечаете на вопросы:
  - *Где мы в SDLC?*
  - *Почему мы тут?* (есть event в `events.jsonl`)
  - *Что дальше?* (есть `next_actions` или `plan`)
  - *Нужно ли вмешательство Nick?* (есть `needs_human`, и это блокирует)
- Есть **формальная проверка консистентности** (validator): state ∈ states, переход ∈ transitions, блокеры не игнорируются.
- Есть **рендер процесса** (Mermaid диаграмма FSM) и **рендер текущего выполнения** (хотя бы линейный список шагов/событий).

---

## Порядок работ (конкретно и по шагам)

### Шаг 1. Зафиксировать IR: какие сущности существуют и какие файлы их хранят

Это почти 1:1 ваш список на стр. 11: ProcessSpec, CheckSpec, ExecutionPlan, CheckResult, ProcessEvent, StateSnapshot. fileciteturn0file0

**Минимальный набор файлов в репозитории/workspace:**

```
.sdlc/
  process.yaml      # ProcessSpec (FSM)
  checks.yaml       # CheckSpec (tool-agnostic)
  state.yaml        # StateSnapshot (текущее состояние задачи)
  plan.yaml         # ExecutionPlan (результат plan)
  report.yaml       # RunReport (результат run)
  events.jsonl      # append-only ProcessEvent log
  diagrams/
    process.mmd     # Mermaid FSM
    run.mmd         # Mermaid run graph/sequence (минимально)
AGENTS.md           # “протокол” для Codex
```

> Почему так: вы явно отделяете **спеку процесса** от **состояния конкретной задачи** и от **плана конкретного прогона** — это упрощает и валидацию, и будущую “подмену бэкенда”.

---

### Шаг 2. ProcessSpec: описываем FSM (но не “пайплайн”)

Это напрямую следует из вашего пункта “FSM ≠ DAG pipeline” (стр. 9). fileciteturn0file0

Пример минимального `process.yaml` (v0.1):

```yaml
spec: nick-sdlc/ProcessSpec/v0.1

states:
  - id: intake
  - id: plan
  - id: implement
  - id: verify
  - id: deliver
  - id: waiting_human
  - id: done

transitions:
  intake: [plan]
  plan: [implement, waiting_human]
  implement: [verify, waiting_human]
  verify: [implement, deliver, waiting_human]
  deliver: [waiting_human, done]
  waiting_human: [plan, implement, done]
  done: []
```

Пока **без сложного guard‑языка**. Guards вы добавите во 2‑й итерации, когда появится стабильная модель CheckResult/metrics. В итерации №1 важнее *общая карта* и *запрет нелегальных переходов*.

---

### Шаг 3. CheckSpec: “tool‑agnostic checks” как контракт

Вы сами отметили, что tool‑agnostic checks почти всегда “ваша ответственность” (стр. 9), и что conftest/OPA — хороший первый двигатель (стр. 7 и 11). fileciteturn0file0

Пример `checks.yaml`:

```yaml
spec: nick-sdlc/CheckSpecSet/v0.1

checks:
  - id: tests
    engine: command
    command: "make test"
    severity: error
    tags: [verify]

  - id: lint
    engine: command
    command: "make lint"
    severity: error
    tags: [verify]

  - id: policy
    engine: conftest
    target: "."
    policy_dir: ".policy"
    severity: error
    tags: [verify]
```

Важно: engine — это **тип адаптера**, а не конкретная тулза. Сегодня это `command`/`conftest`, завтра добавите `ai_check`/`continue_check`/`openhands_task`, не ломая остальное (ваша идея про адаптеры на стр. 12). fileciteturn0file0

---

### Шаг 4. StateSnapshot: состояние задачи, которое видите вы и Codex

Это ваш основной запрос (“одинаково видеть состояние”).

Пример `state.yaml`:

```yaml
spec: nick-sdlc/StateSnapshot/v0.1

task:
  id: "DEV-123"
  title: "Add retry to payment webhook handler"
  repo: "git@github.com:org/repo.git"
  workspace: "/Users/nick/ws/repo-DEV-123"
  branch: "nick/DEV-123-retry"

policy:
  network_access: ask            # allow|deny|ask
  dependency_changes: ask        # allow|deny|ask
  max_fix_verify_loops: 3

run:
  state: intake                  # must be in process.states
  status: ready                  # ready|doing|waiting_human|done|blocked
  iteration: 0
  next_actions: ["A1", "A2"]
  last_plan_ref: null
  last_report_ref: null

actions:
  - id: A1
    type: agent
    title: "Read code + уточнить AC"
    status: todo
  - id: A2
    type: agent
    title: "Propose plan.yaml"
    status: todo

needs_human: []                  # блокирующие вопросы

artifacts:
  commits: []
  pr_url: null
  summary: ""
```

---

### Шаг 5. EventLog: “почему мы приняли решение” (decision history)

Вы отмечаете, что даже при наличии execution history (Temporal/CI) **решения о переходах** обычно нужно логировать доменными событиями (стр. 9 и 12). fileciteturn0file0

Формат `events.jsonl` (1 событие = 1 строка JSON):

```json
{"ts":"2026-02-20T12:00:00+07:00","actor":"Nick","type":"init","message":"Initialized task DEV-123"}
{"ts":"2026-02-20T12:10:00+07:00","actor":"Codex","type":"state_change","from":"intake","to":"plan","because":"Read repo + clarified AC"}
{"ts":"2026-02-20T12:30:00+07:00","actor":"Codex","type":"plan_written","plan_ref":".sdlc/plan.yaml","because":"Computed checks/tests needed"}
```

---

### Шаг 6. ExecutionPlan (plan.yaml): компиляция FSM → “что запускать”

Это ровно ваша модель plan/run/apply (стр. 2 и 11). fileciteturn0file0\
**В итерации №1 plan.yaml можно делать простым и линейным.**

Пример `plan.yaml`:

```yaml
spec: nick-sdlc/ExecutionPlan/v0.1

based_on:
  process: ".sdlc/process.yaml"
  checks: ".sdlc/checks.yaml"
  state: ".sdlc/state.yaml"

steps:
  - id: S1
    kind: agent
    title: "Implement changes"
    expected_state_after: implement

  - id: S2
    kind: check
    check_id: lint
    expected_state_after: verify

  - id: S3
    kind: check
    check_id: tests
    expected_state_after: verify

  - id: S4
    kind: human_gate
    title: "Nick review + decide deliver/done"
    expected_state_after: waiting_human
```

---

### Шаг 7. RunReport (report.yaml): результат run‑фазы

Даже если “run” делаете вручную (вы запускаете команды/агента), **результат фиксируется одинаково**.

Пример `report.yaml`:

```yaml
spec: nick-sdlc/RunReport/v0.1

plan_ref: ".sdlc/plan.yaml"

check_results:
  - check_id: lint
    status: pass
    evidence: "logs/lint.txt"
  - check_id: tests
    status: fail
    evidence: "logs/tests.txt"
    suggested_fix: null

agent_results:
  - step_id: S1
    status: done
    summary: "Added retry w/ exponential backoff; updated unit tests"
```

---

### Шаг 8. “Протокол” для Codex: AGENTS.md + правило обязательного обновления state/events

Вы хотите, чтобы Codex и вы видели состояние одинаково — значит Codex должен быть обязан:

- всегда читать `.sdlc/state.yaml` и `.sdlc/process.yaml` перед работой,
- после каждого значимого шага обновлять `state.yaml`,
- добавлять событие в `events.jsonl`,
- если требуется ваше решение — писать `needs_human` и останавливать прогон.

Это критично, потому что агентный слой по определению недетерминирован (вы это отмечаете в обзоре OpenHands/агентов: им нужны “жёсткие rails” и контракты; стр. 6). fileciteturn0file0

---

## Как это будет работать “вручную” (ваш текущий режим)

### 1) Nick (вы)

- Создаёте workspace
- Заполняете `.sdlc/process.yaml`, `.sdlc/checks.yaml`, `.sdlc/state.yaml`, пустой `events.jsonl`
- Ставите `run.state=intake`, `next_actions=[A1,A2]`

### 2) Codex

- Делает A1 → обновляет `state.yaml`, пишет событие
- Делает A2 → пишет `plan.yaml`, обновляет `state.yaml`, пишет событие
- Если нужен ваш выбор (например, “нужно ли разрешить dependency changes”) → добавляет `needs_human` (blocking) и ставит `run.status=waiting_human`

### 3) Nick

- Отвечаете в `needs_human[].answer`
- Меняете `run.status=ready`, возможно правите `plan.yaml`
- Запускаете Codex дальше

---

## Минимальные “инструменты вокруг DSL” (не workflow engine), которые я бы добавил сразу

Чтобы DSL не стал “бумажкой”, вам нужны 2 утилиты:

1. **Validator** (`sdlc validate`)\
   Проверяет:
   - state в списке states
   - переход легальный
   - если есть blocking needs\_human → статус waiting\_human
   - ссылки на plan/report существуют

2. **Renderer** (`sdlc render`)\
   Генерит:
   - `.sdlc/diagrams/process.mmd` (FSM из process.yaml)
   - `.sdlc/diagrams/run.mmd` (по events.jsonl или plan.yaml)

Это соответствует вашему требованию Renderers как отдельного слоя (стр. 2) и шагу “Renderers как обязательный артефакт apply‑фазы” (стр. 12). fileciteturn0file0

---

## Что будет итерацией №2 (чтобы вы понимали, куда это ведёт)

После того как DSL/IR стабилен:

- добавляете **plan/run/apply как CLI** (как у вас описано на стр. 11),
- подключаете первые адаптеры:
  - `ConftestAdapter`
  - `PreCommitAdapter` (один hook: `sdlc plan && sdlc run --local`) fileciteturn0file0
- Codex становится **одним из executors** (AgentAdapter), а не “центром мира”.

А уже потом — выбор “сильного backend” (Temporal или Tekton‑стек) без смены DSL, как вы предлагаете (стр. 12). fileciteturn0file0

---

Если вы согласны с этой рамкой, то следующий практический шаг: я могу **предложить v0.1 схемы (JSON Schema)** для `process.yaml`, `state.yaml`, `plan.yaml`, `report.yaml` + список валидируемых инвариантов (10–15 правил), чтобы Codex не “ломал формат” и вы могли автоматом проверять консистентность.


#### You:
Да, подготовь всё кроме кода для первой итерации.

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Сейчас заново соберу “пакет первой итерации”: структуру `.sdlc/`, форматы файлов DSL (ProcessSpec/State/Plan/Report/Events), инварианты и правила переходов, шаблоны `AGENTS.md`, ритуал работы Nick↔Codex и критерии готовности — без реализации кода.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Готово: собрал **полный пакет Iteration 1** (DSL/IR, формальные схемы, инварианты, протокол для Codex, шаблоны файлов, примеры, gitignore) — **без реализации CLI/валидатора/раннера**.

[Скачать пакет nick-sdlc-iter1.zip](sandbox:/mnt/data/nick-sdlc-iter1.zip)

---

## Что именно вы получаете в Iteration 1

### Цель итерации

Один “контракт реальности”, чтобы **вы и Codex одинаково видели состояние** задачи и процесс SDLC:

- *где мы сейчас* (FSM state)
- *почему мы тут* (append-only event log)
- *что дальше* (next\_actions / plan)
- *нужно ли вмешательство Nick* (needs\_human)

---

## Структура (что лежит в zip)

```
nick-sdlc-iter1/
  README.md
  SPEC.md
  AGENTS.md
  gitignore.sdlc.txt
  .sdlc/
    process.yaml
    checks.yaml
    state.yaml
    plan.yaml
    report.yaml
    events.jsonl
    events.sample.jsonl
    state.example.yaml
    plan.example.yaml
    report.example.yaml
    diagrams/
      process.mmd
      run.mmd
      process.example.mmd
      run.example.mmd
    schemas/
      process.schema.json
      checks.schema.json
      state.schema.json
      plan.schema.json
      report.schema.json
      event.schema.json
```

---

## Роли файлов (ваш IR-контракт)

### 1) `.sdlc/process.yaml` — **ProcessSpec (FSM)**

- список `states`
- список `transitions` (`from -> to`)
- `invariants` (правила консистентности)

**Обычно коммитится и считается read-only для агента.**

---

### 2) `.sdlc/checks.yaml` — **CheckSpecSet**

Определяет проверки “tool-agnostic”:

- `engine: command | conftest | ai_check | manual`
- `severity: info | warn | error`
- `tags` (к каким состояниям SDLC относится)

**Обычно коммитится и считается read-only для агента.**

---

### 3) `.sdlc/state.yaml` — **StateSnapshot (каноническое состояние задачи)**

Это ваш главный “экран правды”:

- `task` (id/title/repo/workspace/branch/base\_commit/AC)
- `policy` (network/deps/loop budget)
- `run.state` (FSM state), `run.status` (операционный статус)
- `actions` (backlog)
- `needs_human` (структурированные вопросы/аппрувы)
- `artifacts` (commits/PR/logs/summary)
- `checks` (опциональная денормализация последних статусов)

**Это mutable, обычно gitignored.**

---

### 4) `.sdlc/plan.yaml` — **ExecutionPlan**

План ближайшего “прогона”:

- ссылки на `process/checks/state`
- `steps`: `agent | check | human_gate | tool`
- `depends_on` (может быть DAG, даже если сейчас линейно)
- `expected` (ожидаемое состояние до/после)

---

### 5) `.sdlc/report.yaml` — **RunReport (CheckResult + итоги)**

Результаты “run”-фазы:

- `step_results`
- `check_results` (status/evidence/metrics/suggested\_fix)
- `summary`

---

### 6) `.sdlc/events.jsonl` — **ProcessEvent log (append-only)**

Каждая строка — JSON-объект события:

- `seq`, `ts`, `actor`, `type`, `message`, `data`
- типы: `state_change`, `plan_written`, `check_result`, `needs_human_created`, …

Это ваш “decision history”: **почему** были переходы/решения.

---

## Инварианты (главные правила консистентности Iteration 1)

Они описаны в `SPEC.md`, но самые критичные:

1. **FSM-валидность**

- `run.state` должен быть одним из `process.states`
- переход состояния **только** по `process.transitions`

2. **Human blocking**
   Если есть `needs_human` с:

- `blocking: true`
- `status: open`

то:

- `run.status` **обязан** быть `waiting_human`
- агент **обязан остановиться**

3. **Append-only events**

- `events.jsonl` только дописывается
- `seq` монотонно растёт

4. **Бюджет циклов implement↔verify**

- если превышен `policy.max_fix_verify_loops` и проверки всё ещё падают → создать blocking `needs_human` и стоп.

---

## Протокол для Codex (что он обязан делать)

В `AGENTS.md` лежит готовый текст, но суть:

- Перед любым действием: прочитать `.sdlc/state.yaml` и кратко резюмировать `run.state/run.status/next_actions/needs_human`
- Если `waiting_human` или есть blocking вопрос — **стоп**
- Не трогать `process.yaml` и `checks.yaml` без явной команды от Nick
- После каждого значимого шага:
  - обновить `state.yaml`
  - дописать событие в `events.jsonl`
  - если гонял проверки — обновить `report.yaml` и (опционально) `state.checks`

Дополнительно я добавил простую “ручную блокировку” через `run.lock` (held\_by/held\_at), чтобы Nick и Codex не перетирали правки.

---

## Как использовать это прямо сейчас (ручной режим, как вы и хотите)

### 1) Встраивание в ваш workspace/repo

- Скопируйте `.sdlc/` и `AGENTS.md` в корень workspace (лучше в корень репозитория, чтобы агент всегда видел рядом).
- Добавьте из `gitignore.sdlc.txt` правила в `.gitignore`.

Рекомендация:

- **Коммитить**: `process.yaml`, `checks.yaml`, `schemas/*`, `AGENTS.md`
- **Не коммитить**: `state.yaml`, `plan.yaml`, `report.yaml`, `events.jsonl`, `.sdlc/diagrams/*`, логи

### 2) Старт новой задачи

- Скопируйте `.sdlc/state.example.yaml` → `.sdlc/state.yaml`
- Заполните `task.*` и `policy.*`
- Заполните `actions` и `run.next_actions`

### 3) Запуск Codex

Дайте Codex инструкцию уровня:

> “Следуй AGENTS.md. Истина состояния — .sdlc/state.yaml. Выполняй run.next\_actions. После каждого шага обновляй state и дописывай событие в events.jsonl. Если нужно решение — создай needs\_human (blocking) и остановись.”

### 4) Ваше вмешательство

Только когда появится `needs_human`:

- вы заполняете `answer`
- ставите `run.status: ready`
- (опционально) правите `next_actions`/`plan`

---

## Что можно расширять, не ломая контракт (уже в Iteration 1)

- добавлять новые `checks` с новым `engine` (это “адаптерная точка”)
- добавлять новые `states`/`transitions`
- ужесточать инварианты в `process.yaml` (пока просто декларативно)
- добавлять `metrics` в `report.yaml` и затем использовать их для guards во 2-й итерации

---

Если хотите, следующим шагом (Iteration 1.1, всё ещё **без workflow engine**) я могу подготовить:

- **набор “канонических event types”** (строже: какие поля у каких событий обязательны),
- **конвенции для `data`** (например: `transition`, `checkout_sha`, `policy_decisions`, `artifact_refs`),
- и **минимальный “чек-лист reviewer packet”**, который Codex обязан заполнять перед `waiting_human` (чтобы ваш 4h/day бюджет тратился максимально эффективно).


#### You:
я нашел такой проект. исследуй его и скажи, есть ли тут что-то напрямую связанное с тем, что я пытаюсь сделать

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Я посмотрел **тот проект, который вы загрузили в XML** — по содержимому это снапшот репозитория **`paip-python`**: “Python implementations of classic AI programs from Peter Norvig’s *PAIP*” (ELIZA, GPS, rule engine и т. п.).

### Короткий вердикт

**Прямо “в лоб” под вашу задачу (DSL для SDLC + общий state для вас и Codex)** там **ничего готового нет**:

- нет DSL процесса (states/transitions) в смысле SDLC,
- нет state store/ledger,
- нет event log “почему мы перешли состояние”,
- нет интеграций с Git/CI/PR как с доменными событиями (кроме общих инструкций “запусти тесты, сделай PR”).

Но… **есть 2–3 модуля, которые очень близко пересекаются с вашими примитивами** (как идеи/референсы), если вы хотите, чтобы часть “plan/policy” была **детерминированной**, а не полностью LLM‑магией.

---

## Что реально перекликается с тем, что вы строите

### 1) `paip/gps.py` — “General Problem Solver” (планирование через state transitions)

Это самый “в тему” кусок.

Что он делает: принимает

- **initial states**
- **goal states**
- **operators**, где у каждого оператора:
  - `action`
  - `preconds`
  - `add`
  - `delete`

и строит **последовательность действий**, чтобы добраться до цели (means‑ends analysis).

Почему это близко к вам:

- это практически **ExecutionPlan generator**, только в терминах “фактов” и операторов.
- модель `preconds/add/delete` — это простейшая декларативная “DSL” для переходов.
- в коде даже есть хак “как получить trace”: он добавляет состояния вида `"Executing <action>"` в `add-list`, чтобы потом по финальным состояниям восстановить последовательность действий.

Как это можно маппить на ваш SDLC‑IR:

- `StateSnapshot` → множество фактов:\
  `in_state(plan)`, `branch_created`, `tests_pass`, `lint_pass`, `pr_open`, `needs_human_approval`, …
- `CheckSpec/CheckResult` → факты `tests_pass/tests_fail`, `lint_pass/lint_fail`
- `ExecutionPlan` → найденная последовательность `operators` (шагов)

**Практический вывод:** если вы хотите, чтобы `plan.yaml` формировался не “как LLM решил”, а более формально (пусть и примитивно) — GPS‑идея вам подходит как референс.

⚠️ Но: GPS — учебный планировщик. В реальном SDLC “операторы” имеют побочные эффекты, недетерминизм, ретраи, таймауты — это всё придётся добавлять самим (или держать как внешний контур).

---

### 2) `paip/emycin.py` — expert system shell (правила + “объяснения”)

Это второй сильный кусок пересечения.

Что он даёт:

- rule‑based reasoning (backward chaining),
- механизм “уверенности” (certainty factors),
- **интроспекция** (“почему система так решила”).

Почему это близко к вам:

- вы хотите **guards/policies** и **decision history** (“почему мы перешли в waiting\_human”, “почему запретили deps”, “почему это risky”) — Emycin по духу про то же.
- интроспекция = очень удобный источник для вашего `events.jsonl` (“because …”).

**Практический вывод:** Emycin можно рассматривать как прототип **policy engine**, который:

- принимает факты (`diff_too_large`, `touches_security_code`, `deps_changed`, `network_requested`, …),
- выдаёт решения/рекомендации,
- умеет “объяснить”.

⚠️ Но: опять же, это учебный движок и на Python 2‑стиле. В реальном проекте вам проще и стандартнее будет OPA/Rego/Conftest или свой простой rule‑движок под ваши поля (но как “идея объяснимых правил” — очень в тему).

---

### 3) `paip/search.py` / `paip/logic.py` / `prolog.py` — полезно, но уже не “напрямую”

- Search‑алгоритмы могут пригодиться, если вы захотите выбирать “лучший план/путь” в пространстве состояний.
- Logic/Prolog — если вы вдруг захотите писать guards как логические предикаты и делать запросы типа “найди все невыполненные требования”.

Это **скорее академические кирпичики**, а не то, что ускорит вашу Iteration 1.

---

## Что в проекте НЕ совпадает с вашей задачей

Если сравнивать с тем, что вы строите (DSL/IR + state/events + совместимость с агентом):

- **нет “единого файла состояния”**, который агент обязан обновлять
- **нет event log’а** в доменном смысле (“decision history”)
- **нет разделения FSM vs plan (DAG)** — это ровно та грань, которую вы правильно проводите у себя
- **нет SDLC-интеграций**: GitHub events, PR checks, merge gating, pre-commit hooks и т. п.

То есть это не “готовая основа”, а **источник идей для двух подсистем**: (а) планирование шагов, (б) объяснимые правила/политики.

---

## Итог: есть ли “что-то напрямую связанное”?

Если под “напрямую” вы имеете в виду:\
**“можно взять и использовать как фундамент моего SDLC DSL + Codex loop”** → **нет**.

Если же “напрямую” как:\
**“тут есть готовые концептуальные примитивы для моих plan/policy частей”** → **да**:

- `gps.py` — референс для **формального планирования по операторам** (preconds/add/delete)
- `emycin.py` — референс для **policy/guards + explainability** (“почему так решили”)

---

P.S. Системная заметка: у меня есть доступ к вашему загруженному XML, но некоторые **более ранние** файлы, которые вы загружали в этот чат, могли “истечь” и стать недоступными. Если вам нужно будет снова анализировать какие-то из них — просто перезагрузите.


#### You:
опиши DSL для general problem solver

#### ChatGPT:
Ниже — **DSL для General Problem Solver (GPS)** в классическом “PAIP/Norvig” смысле: *задача = начальные факты + целевые факты + набор операторов, которые переводят мир из состояния в состояние*.

Это по сути **STRIPS‑подобная** декларативная модель: оператор задаёт “если (preconds), то после действия будет (add), а перестанет быть (delete)”.

---

## 1) Модель мира GPS

### Факт (fact)

Атомарное утверждение, которое либо **истинно**, либо **ложно**.\
В DSL это строка.

- Пример: `son_at_home`, `car_works`, `have_money`
- В классическом GPS **нет типов/чисел/структур**, только “факт присутствует в состоянии или нет”.

### Состояние (state)

Множество фактов, которые **истинны сейчас**.

- Всё, чего нет в списке фактов, считается ложным (**closed world assumption**).

### Цель (goal)

Множество фактов, которые должны стать истинными.

---

## 2) Оператор (operator) — основной элемент DSL

Оператор задаёт **переход состояния**.

Минимальные поля:

- `action` — имя действия (строка; используется для вывода плана/трейса)
- `preconds` — список фактов, которые должны быть истинны *до* применения
- `add` — факты, которые станут истинны *после* применения
- `delete` — факты, которые станут ложными *после* применения (будут удалены из состояния)

**Семантика применения:**

Пусть текущее состояние `S` — множество фактов.

Оператор применим, если:

- `preconds ⊆ S`

Тогда новое состояние:

- `S' = (S − delete) ∪ add`

---

## 3) DSL уровня “Problem”: что нужно описать, чтобы GPS мог планировать

Самый простой DSL (в духе того проекта, который вы нашли) выглядит так:

### GPS Problem DSL v0.1 (JSON/YAML-эквивалент)

- `start`: список фактов (начальное состояние)
- `finish`: список фактов (цели)
- `ops`: список операторов

**Псевдограмматика:**

- `Problem := { start: Fact[], finish: Fact[], ops: Operator[] }`
- `Operator := { action: string, preconds: Fact[], add: Fact[], delete: Fact[] }`
- `Fact := string`

---

## 4) Рекомендованные правила (инварианты DSL)

Чтобы планирование было предсказуемым, обычно вводят “правила корректности домена”:

1. `add` и `delete` **не должны пересекаться** у одного оператора\
   (иначе “и добавили, и удалили” один и тот же факт).

2. Внутри каждого списка (`preconds/add/delete`) не должно быть дублей.

3. Желательно, чтобы `add` был не пустой (иначе оператор ничего не меняет и может создавать бессмысленные циклы).

4. Для каждого факта из `finish` должен существовать хотя бы один оператор, который может его добавить (`fact ∈ op.add`) — иначе задача нерешаема.

5. Факты лучше нормализовать (например, `snake_case`) и избегать свободного текста — GPS сравнивает факты по **строковому равенству**.

---

## 5) Как GPS строит план (кратко, чтобы понимать смысл DSL)

Классический GPS делает *means‑ends analysis*:

- Берёт цель `g`
- Ищет оператор(ы), которые могут сделать `g` истинной (т.е. где `g ∈ add`)
- Пробует добиться **всех preconds** выбранного оператора как подцелей
- Применяет оператор → обновляет state
- Повторяет для остальных целей

Почти всегда есть защита от зацикливания: “не пытайся снова достичь цель, которая уже в стеке целей” (goal stack).

---

## 6) Пример DSL (канонический “school”)

Вот как это выглядит в YAML (то же самое можно в JSON):

```yaml
start:
  - son_at_home
  - have_money
  - have_phone_book
  - car_needs_battery

finish:
  - son_at_school

ops:
  - action: drive_son_to_school
    preconds: [son_at_home, car_works]
    add: [son_at_school]
    delete: [son_at_home]

  - action: shop_installs_battery
    preconds: [car_needs_battery, shop_knows_problem, shop_has_money]
    add: [car_works]
    delete: [car_needs_battery]

  - action: tell_shop_problem
    preconds: [in_communication_with_shop]
    add: [shop_knows_problem]
    delete: []

  - action: telephone_shop
    preconds: [know_phone_number]
    add: [in_communication_with_shop]
    delete: []

  - action: look_up_number
    preconds: [have_phone_book]
    add: [know_phone_number]
    delete: []

  - action: give_shop_money
    preconds: [have_money]
    add: [shop_has_money]
    delete: [have_money]
```

---

## 7) “Трейс действий” в GPS DSL

В том Python‑проекте трюк такой: чтобы вернуть план, они **добавляют в add‑list** каждого оператора специальный факт вида:

- `Executing <action>`

И потом, когда цель достигнута, фильтруют финальные состояния по префиксу `"Executing "` и получают список выполненных действий.

Если вы хотите “чище” на уровне DSL, можно формально договориться:

- либо GPS‑раннер сам добавляет эти “Executing …” факты (как имплементационный хак),
- либо вы расширяете DSL оператора полем `emit` (необязательно для базового GPS), например:
  - `emit: ["action:drive_son_to_school"]`

Но “классика GPS” довольствуется хаком с add‑list.

---

## 8) Как расширять DSL, не ломая GPS-ядро (если захотите)

Если вам нужен более практичный GPS под SDLC‑автоматизацию, самые полезные расширения:

1. **`id`** у оператора (стабильный идентификатор), а `action` оставить человекочитаемым
2. **`cost`** (для выбора “лучшего” плана, если добавите поиск)
3. **negative preconditions** (например `forbids: [...]`)\
   потому что “отсутствие факта” в closed-world иногда недостаточно удобно фиксировать.
4. **resources/locks** — если появится параллелизм и конкуренция за ресурсы

Но это уже GPS++.

---

## Как это напрямую ложится на вашу задачу (в 2 фразы)

GPS DSL — это идеальный формат для “plan.yaml” уровня **декларативного планирования**: состояние = факты из вашего `.sdlc/state.yaml`, а операторы = допустимые “шаги SDLC” (создать ветку, прогнать тесты, открыть PR, запросить ревью…).\
Дальше Codex может быть “исполнителем операторов”, но сам план будет получаться **детерминированно из DSL**, а не только “как LLM придумал”.

---

### Небольшая ремарка про файлы

Часть ранее загруженных в этот чат файлов у меня уже недоступна (истёк срок доступа). Если вам нужно, чтобы я ссылался/сопоставлял что-то ещё с теми файлами — просто загрузите их повторно.
