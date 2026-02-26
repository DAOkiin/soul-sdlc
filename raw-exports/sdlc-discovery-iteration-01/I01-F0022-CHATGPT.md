# Альтернативы Microsoft Agent Framework

<user>
Какая сейчас есть реальная альтарнатива Microsoft Agent Framework? Кажется что это беспроигрышный выбор. Например, если я хочу построить систему автоматизации разработки, я обязан создать управление рабочими процессами через FSM. И FSM должна быть написана при участии DSL по моему SDLC.

</user>
<agent>
Понял: я кратко сравню реальные альтернативы Agent Framework (по экосистемам и сценариям), и затем предложу архитектуру для “автоматизации разработки” с FSM + DSL, включая какие инструменты лучше подходят и почему.


</agent>
<agent>
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


</agent>
<user>
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

</user>
<agent>
Понял: я предложу практичную схему “workflow engine в центре” именно для вашего кейса (Codex‑агент, macOS, 4 часа внимания в день): разложу ответственности по слоям, дам порядок внедрения (MVP → production), и покажу как организовать циклы SDLC с точками вашего вмешательства.


</agent>
<agent>
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


</agent>
<user>
Идея верная, но текущий вектор чуть другой. На текущем этапе я буду сам создавать workspaces и запускать агентов codex. Мне нужно чтобы у меня появился DSL, который поможет агенту и мне видеть состояние одинаково. Это то, что должно появиться в первой итерации.

</user>
<agent>
Понял: в первой итерации делаем не движок, а **минимальный DSL “общего состояния”** для вас и Codex: единый формат задачи, текущего шага SDLC, артефактов, гейтов и следующих действий. Дам практичный YAML/JSON‑спек, примеры, правила переходов и шаблон AGENTS.md/промпта, чтобы Codex обновлял состояние.


</agent>
<agent>
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


</agent>
<user>
Спланируй заново, я подготовил исследование по ландшафту решений.

</user>
<agent>
Ок — сейчас перечитаю ваш PDF и перепланирую “итерацию №1” вокруг DSL/IR так, чтобы он был future‑proof (plan/run/apply), но работал уже при ручных workspaces и ручном запуске Codex.


<PARSED TEXT FOR PAGE: 1 / 16>
OSS экосистема для SDLC‑оркестрации в
репозитории и агентного development workflow
Резюме
На рынке почти нет одного open‑source инструмента, который «из коробки» полностью закрывает
вашу целевую архитектуру целиком: Process DSL (states/transitions) + Policy/Checks + Triggers/
Runners + Executors + State store/history + Renderers. На практике «закрывается» это либо
оркестратором выполнения (workflow engine) с долговременной историей, либо CI/merge‑gating
платформой, а всё остальное добирается адаптерами и договорённостями по формату
спецификаций (ваш будущий DSL/IR). 
Если цель — plan/run/apply с воспроизводимостью и полноценной историей событий как у
инфраструктурного GitOps/plan‑apply, то «самый близкий к идеалу» фундамент дают: - Temporal как
«currency» для долговременных workflow с event history, запросами/сигналами, UI и плагинностью.
- Либо Kubernetes‑стек Tekton Pipelines + Triggers + Results как «DSL+triggers+execution+long‑term
history» в k8s‑нативной форме. 
Если цель — минимум самописного кода и быстрый «боевой» запуск с привычной CI‑моделью, то
наиболее прагматичный фундамент: - Jenkins (Pipeline as Code) + OPA/Conftest + pre-commit, где
ваш DSL сначала может быть «компилятором» в Jenkinsfile/шаги пайплайна, а state/history жить в
артефактах/БД/логах плюс CI‑UI. 
Для «agent‑driven» слоя (Codex/LLM‑агент как исполнитель) наиболее близкие OSS‑кандидаты
сегодня: OpenHands (SDK + GitHub Action + event‑log подход) и Continue (source‑controlled AI checks в
репозитории). Но у обоих заметная доля value завязана на «control plane / hosted интеграции»,
поэтому их разумнее проектировать как плагины‑исполнители/интеграции поверх вашего DSL, а
не как единственный фундамент. 
Требования к системе и целевая архитектура
Ваша целевая система (в терминах слоёв) хорошо раскладывается на 6 компонент:
Process DSL: граф состояний и переходов (states/transitions), guards, инварианты.
Checks/Policies (policy‑as‑code): спецификация проверок (tool‑agnostic), единый формат
результата, возможность «объяснить» и «починить/предложить diff».
Triggers/Runners: локально (git hooks, pre-commit ) и удалённо (CI, webhooks, issue/PR
commands, cron).
Executors: task runner/command runner/agent runner (в идеале — детерминированные шаги +
опционально агентные).
1
2
3
4
5
• 
• 
• 
• 
1
<PARSED TEXT FOR PAGE: 2 / 16>
State store/history: журнал событий и история решений (почему был сделан переход), а также
актуальное состояние.
Renderers: диаграммы, документация, отчёты, «граф процесса» и «граф выполнения». 
С практической точки зрения, «plan/run/apply» обычно означает: - plan: вычислить, какие проверки/
действия нужны, в каком порядке, какие переходы допустимы, и сформировать артефакт плана (в
идеале — воспроизводимый). - run: исполнить план (локально/в CI), собрать CheckResult/артефакты. -
apply: зафиксировать состояние/историю (и, опционально, применить изменения: merge, label, PR
comment, обновление docs). Паттерн «plan/apply по событиям PR» очень хорошо иллюстрирует
Atlantis (пусть он и Terraform‑специфичен). 
Ниже — архитектурный «скелет» (ваш DSL как source of truth; разные backends подключаются
адаптерами):
flowchart TB
 subgraph Repo["Git репозиторий"]
 DSL["Process DSL: states/transitions"]
 PolicyIR["CheckSpec/Policy IR"]
 Docs["Docs/diagrams sources"]
 end
 CLI["Orchestrator CLI: plan/run/apply"]
 PreCommit["Local runner: pre-commit"]
 CI["CI runner (any)"]
 Conftest["Policy engine: conftest (OPA/Rego)"]
 AgentExec["Agent executor (Codex/OpenHands/etc)"]
 CmdExec["Command/task executor (Dagger/Jenkins steps/etc)"]
 State["State store + event history"]
 Render["Renderers: Mermaid/TechDocs/UI"]
 DSL --> CLI
 PolicyIR --> CLI
 PreCommit --> CLI
 CI --> CLI
 CLI --> Conftest
 CLI --> CmdExec
 CLI --> AgentExec
 CLI --> State
 CLI --> Render
 Docs --> Render
• 
• 6
7
8
2
<PARSED TEXT FOR PAGE: 3 / 16>
Ключевая «future‑proof» идея здесь: вы вводите стабильный промежуточный контракт (IR) —
ProcessSpec , CheckSpec , CheckResult , Event , StateSnapshot — и делаете набор
адаптеров под execution backends и policy engines. Тогда появление «новых инструментов/подходов»
сводится к добавлению нового адаптера, без переизобретения процесса. 
Приоритетный список OSS решений и оценка по слоям
Данные по stars/последним коммитам — по состоянию на 20 февраля 2026 (UTC+7). 
Проект Коротко
Слои (DSL /
Policy / Triggers /
Exec / State /
Render)
Зрелость и
активность
Язык/
рантайм
Интеграции (pre￾commit /
conftest / CI /
агенты)
Расширяемость
Ограничения
относительно вашей
DSL‑цели
Temporal
Durable workflow
engine с полной
event history,
message passing
(signals/queries/
updates) и Web UI. 
DSL: частично
(кодовые
workflow как
«граф»); Policy:
частично; 
Triggers:
частично; Exec:
да; State: да; 
Render: да (UI). 
~18.4k★;
коммиты 20
Feb 2026. 
Go
(server);
SDK в
разных
языках
(workers/
clients). 
pre-commit
вызывает ваш 
plan ; Activities
запускают
conftest/
команды; CI/
webhooks шлют
signals/updates. 
Плагины/интерсепторы/
плагин‑гайд. 
Вам нужно самим
определить «repo‑state»
модель и bridges к git/PR;
policy‑as‑code не
нативный. 
Tekton
Kubernetes‑нативный
CI/CD: Tasks/
Pipelines/PipelineRuns
+ Triggers
(EventListener/
Trigger/Binding/
Template). 
DSL: да (CRDs); 
Policy: частично;
Triggers: да; 
Exec: да; State:
частично (CRDs)
+ долго через
Results; Render:
частично
(dashboard/
внешние UI). 
pipeline
~8.9k★;
коммиты 16
Feb 2026. 
Go, k8s
Отлично ложится
как CI backend;
conftest можно
запускать как
Task; pre￾commit остаётся
локальным. 
Расширение через новые
Tasks/Resolvers/
Interceptors, композиция
YAML. 
Kubernetes‑зависимость
и «DAG/Steps» вместо
«FSM‑состояний»;
state‑machine придётся
моделировать поверх
PipelineRun/Results. 
Tekton
Results
Долговременное
хранение истории
запусков и логов
отдельно от etcd: API
server + controller +
retention agent. 
State/History: 
да (для Tekton
workload). 
~86★;
обновлялся 
20 Feb 2026. 
Go
Используется как
«event store» для
CI‑выполнений. 
API/метаданные/
retention. 
Это история запусков, не
ваша доменная
FSM‑история — её нужно
сквозным correlation id
связывать с Result. 
9
10
11
12
13
14
15
16
17
18
19
20
3
21
22
23
24
25
26
26
27 26
26
26
3
<IMAGE FOR PAGE: 3 / 16>
![image](sediment://e86782b527223a0#file_00000000324c71fa9b29944d19ee6ce4#p_2.jpg)
<PARSED TEXT FOR PAGE: 4 / 16>
Проект Коротко
Слои (DSL /
Policy / Triggers /
Exec / State /
Render)
Зрелость и
активность
Язык/
рантайм
Интеграции (pre￾commit /
conftest / CI /
агенты)
Расширяемость
Ограничения
относительно вашей
DSL‑цели
Argo
Workflows
Workflow engine для
k8s, поддерживает
DAG и step‑based
workflows; UI
показывает
артефакты. 
DSL: да (YAML); 
Policy: частично;
Triggers:
частично
(обычно с Argo
Events); Exec: да; 
State: частично
(CRDs); Render:
да (UI + artifact
viz). 
~16.5k★;
коммиты 20
Feb 2026. 
Go + k8s
Хороший
backend для
run‑фазы;
conftest как шаг/
контейнер;
локально —
через pre￾commit . 
Простая расширяемость
через templates/steps/
DAG и артефакты. 
Как и Tekton: нет
встроенной «FSM
доменной модели»;
придётся строить state
store поверх. 
Jenkins
Automation server с
Pipeline as Code
(Jenkinsfile),
огромный
плагинный мир,
визуализация
пайплайнов (Blue
Ocean). 
DSL: да (pipeline
script); Policy:
частично; 
Triggers: да; 
Exec: да; State:
частично (build
history); Render:
да (UI). 
~25k★;
коммиты 15
Feb 2026. 
Java
Отлично как CI
backend;
webhooks/SCM
triggers;
локально
остаётся pre￾commit . 
Extension points и
плагины. 
DSL вам придётся
компилировать в
Jenkinsfile/Steps;
«история
решений» (почему
сменили состояние) не
нативна — нужна своя
БД/лог. 
Prow
k8s‑based CI/CD для
GitHub: webhooks +
плагины + jobs +
crier; Tide управляет
merge pool и
автослиянием. 
DSL: частично
(job config); 
Policy: частично;
Triggers: да; 
Exec: да; State:
частично
(ProwJobs CRD/
статусы); 
Render:
частично (Deck). 
repo 
kubernetes￾sigs/prow
~261★;
коммиты 20
Feb 2026; код
исторически
мигрировал
из 
kubernetes/
test-infra . 
Go + k8s
Очень силён для
PR‑гейтинга и
автоматизации
вокруг GitHub;
ваши checks
можно запускать
как presubmit
jobs. 
Плагины на Go (hook
plugins). 
Сложность эксплуатации
(k8s‑кластер), и
«процесс» чаще
выражается
job‑критериями/
лейблами, а не строгой
FSM. 
28
29
30
31
32
33
34
35
36 37
38
39
40
41
42
43
44
45
46
47
48
4
<IMAGE FOR PAGE: 4 / 16>
![image](sediment://2ada1c94d2a8ea2#file_00000000324c71fa9b29944d19ee6ce4#p_3.jpg)
<PARSED TEXT FOR PAGE: 5 / 16>
Проект Коротко
Слои (DSL /
Policy / Triggers /
Exec / State /
Render)
Зрелость и
активность
Язык/
рантайм
Интеграции (pre￾commit /
conftest / CI /
агенты)
Расширяемость
Ограничения
относительно вашей
DSL‑цели
Dagger
Programmable
delivery engine:
одинаково локально
и в CI; модули для
переиспользования;
OpenTelemetry traces
(TUI/web). 
DSL: частично
(модули/
функции); Policy:
частично; 
Triggers:
частично (через
CI); Exec: да; 
State: частично
(кэш/
артефакты); 
Render: да
(traces). 
~15.4k★;
коммиты 18
Feb 2026. 
Go engine
+ SDK (Go/
TS/Python
и др.) 
Отличен как
executor для
run‑фазы; есть
GitHub Action
интеграция;
conftest можно
вызывать как
шаг. 
Модульность и
переиспользование
через Dagger modules. 
Не даёт «доменной»
state/history — это нужно
строить поверх (хотя
трассировка помогает). 
Backstage
Developer Portal:
Software Templates
(scaffolder) +
TechDocs
(docs‑as‑code) +
плагины. В TechDocs
у Spotify заявлены
5000+ док‑сайтов. 
DSL: частично
(template YAML
steps/actions); 
Policy: нет/
частично; 
Triggers:
частично; Exec:
частично
(scaffolder
actions); State:
частично
(каталог/
задачи); Render:
да (портал,
TechDocs). 
~32.6k★;
коммиты 20
Feb 2026. 
Node/TS +
плагины 
Сильная
интеграция с
docs/
диаграммами;
можно показать
ваш процесс/
состояния в
портале; CI/
проверки
остаются
внешними. 
Плагинная архитектура
(frontend plugins). 
Не заменяет оркестратор
исполнения; скорее
«Renderer/Portal слой» +
шаблоны. 
Continue
Source‑controlled AI
checks: checks в
репозитории как
markdown в
.continue/
checks/ ,
репортятся как
GitHub status checks;
есть CLI ( cn ) как
модульный agent
loop. 
DSL: частично
(check DSL в
md+frontmatter);
Policy: частично
(LLM‑policy); 
Triggers: да (PR/
cron/issues —
часть через
control plane); 
Exec: да (агент); 
State: частично; 
Render:
частично (через
PR checks). 
~31.5k★;
коммиты 20
Feb 2026. 
TypeScript/
Node
Может стать
«AI‑check runner»
в вашей системе;
но офиц. «Run
checks in CI»
подразумевает
Continue account
+ наблюдение
репозитория. 
Плагинообразно через
CLI инструменты/
конфиги; checks как
files‑as‑code. 
Часть триггеров/
оркестрации уходит в их
Mission Control; для
чистого OSS вам
придётся воспроизвести
control plane или
запускать CLI самим. 
49
50
51
52
53
54
55
56
57
58
59
60 61
62
63
64
65
66
67
68
69
70
71
5
<IMAGE FOR PAGE: 5 / 16>
![image](sediment://a30d64c690b671d#file_00000000324c71fa9b29944d19ee6ce4#p_4.jpg)
<PARSED TEXT FOR PAGE: 6 / 16>
Проект Коротко
Слои (DSL /
Policy / Triggers /
Exec / State /
Render)
Зрелость и
активность
Язык/
рантайм
Интеграции (pre￾commit /
conftest / CI /
агенты)
Расширяемость
Ограничения
относительно вашей
DSL‑цели
OpenHands
Платформа coding
agents: SDK (tools:
bash/files/web/MCP),
CLI/GUI; есть GitHub
Action: триггер по
label fix-me или
комменту 
@openhands￾agent . В статье/
пейпере описан
event‑log как
представление state/
memory. 
DSL: нет/
частично (agent
workflows); 
Policy: частично;
Triggers: да
(GitHub Action); 
Exec: да (агент); 
State: частично
(event log/
траектории); 
Render:
частично (UI/
логи). 
~68k★;
коммиты 20
Feb 2026. 
Python +
web UI
Хороший «agent
executor» слой;
легко
оборачивается в
вашу run‑фазу;
но policy/guards
должны
оставаться у вас. 
SDK + возможность
определять tools/
поведение. 
Агентная
недетерминированность;
требует жёстких «safety
rails» и контрактов
CheckSpec/TaskSpec. 
LangGraph
Graph‑based
orchestrator для
агентных workflow;
есть встроенная
persistence через
checkpointers,
checkpoints «на
каждом super‑step»,
поддержка time
travel/HiTL. 
DSL: да (graph
API); Policy:
частично; 
Triggers: нет/
частично; Exec:
да; State: да
(checkpointers); 
Render:
частично
(mermaid‑вывод/
инструменты
экосистемы). 
~24.9k★;
активные
релизы
(например, 19
Feb 2026). 
Python/JS
Может стать
«движком» для
вашей FSM/
агентных веток и
state store;
conftest/
pre‑commit
подключаются
как tools/steps. 
Checkpointer‑плагины
(Postgres и др.). 
Это agent workflow
engine, не
SDLC‑оркестратор
repo‑событий; триггеры/
CI интеграции придётся
писать. 
Atlantis
PR‑оркестратор для
Terraform: слушает
PR events по
webhooks, запускает 
plan/apply и
комментирует в PR.
Очень «похоже» на
вашу plan/run/apply
архитектуру. 
DSL: частично; 
Policy: частично;
Triggers: да; 
Exec: да; State:
частично (locks/
история PR); 
Render:
частично (PR
comments). 
~8.8k★. Go
Как шаблон/
референс‑модель
«plan/apply через
PR»; сам по себе
узко‑доменный. 
Конфиг‑ориентированное
расширение под
Terraform workflow. 
Не универсален для
SDLC; но даёт
проверенный паттерн
«коммент‑как‑триггер»,
«план‑как‑артефакт». 
72
73 74
75
76
77
78
79
80
81
82
83
84
80
85
7 86
87
86
86
86
6
<IMAGE FOR PAGE: 6 / 16>
![image](sediment://e5d24ec841d2640#file_00000000324c71fa9b29944d19ee6ce4#p_5.jpg)
<PARSED TEXT FOR PAGE: 7 / 16>
Проект Коротко
Слои (DSL /
Policy / Triggers /
Exec / State /
Render)
Зрелость и
активность
Язык/
рантайм
Интеграции (pre￾commit /
conftest / CI /
агенты)
Расширяемость
Ограничения
относительно вашей
DSL‑цели
bors-ng
Merge queue /
continuous testing
workflow для PR;
объясняет, почему
простые required
checks не
гарантируют
«вечнозелёную
main». Но проект
архивирован. 
Process/Queue:
да (merge
gating); 
остальное:
частично. 
~1.5k★;
архивирован
4 Apr 2024,
коммиты до
Jan 2024. 
Elixir/
Phoenix
Полезен как
«исторический
референс»
merge‑queue
подсистемы. 
—
Не future‑proof (архив),
лучше использовать как
источник идей, не как
основу. 
Дополнительно (как «базовые кирпичи» для ваших слоёв Checks/Triggers): - pre-commit —
стандартный каркас для локальных git hooks; мотивация — ловить проблемы до code review. 
- Open Policy Agent + Conftest — policy‑as‑code через Rego и тестирование структурированных
конфигов в CI/CD. 
Топ кандидатов и расхождение с вашими DSL‑целями
Ниже — «топ‑5» кандидатов как ядро (или как ключевой слой) и то, насколько они закрывают ваши
компоненты полностью/частично/нет (F/P/N). Далее — какой glue code обычно нужен, чтобы
уложить их в ваш plan/run/apply и tool‑agnostic CheckSpec.
Кандидат
Process
DSL
(states/
transitions)
Checks/
Policies
Triggers/
Runners
Executors
State
store/
history
Renderers
Что обычно
придётся дописать
под ваши цели
Temporal P P P F F F
Компиляция DSL →
workflow/activities;
адаптеры git/PR
events → signals/
updates; общий
CheckSpec/
CheckResult;
экспортер
диаграмм вашего
процесса. 
88
89
89 90 89
90
91
92
93 94
95
96
7
<PARSED TEXT FOR PAGE: 8 / 16>
Кандидат
Process
DSL
(states/
transitions)
Checks/
Policies
Triggers/
Runners
Executors
State
store/
history
Renderers
Что обычно
придётся дописать
под ваши цели
Tekton
(+Triggers+Results) P P F F
P→F
(через
Results)
P
Компиляция DSL →
Pipeline/
PipelineRun; связка
«доменный state»
↔ «PipelineRun/
Result»; единый
формат
план‑артефакта
(ConfigMap/
Artifact). 
Jenkins P P F F P F
Компиляция DSL →
Jenkinsfile/stages;
state/history
(почему переход)
— в отдельную БД/
артефакты;
стандартизировать
contracts шагов
(CheckSpec). 
Prow (+Tide) P P F F P P
Выразить процесс
через критерии
Tide/плагины;
хранить доменную
FSM отдельно;
написать
job‑генератор из
DSL; интеграция
локального pre￾commit с
серверными
presubmit. 
3
97
98
8
<PARSED TEXT FOR PAGE: 9 / 16>
Кандидат
Process
DSL
(states/
transitions)
Checks/
Policies
Triggers/
Runners
Executors
State
store/
history
Renderers
Что обычно
придётся дописать
под ваши цели
Continue P
P→F (AI
checks)
P→F (через
GitHub
integration /
Mission
Control)
F (агент) P P
Если хотите
«чистый OSS»:
воспроизвести/
обойти control
plane; встроить в
ваш plan/run/apply
как executor чеков;
нормализовать
CheckResult и
историю. 
Три «жёстких» расхождения с вашей DSL‑целью, которые повторяются почти у всех кандидатов:
1) FSM ≠ DAG pipeline. Большинство CI/Workflow систем нативно DAG/steps‑ориентированы (Argo,
Tekton, Jenkins stages). Ваш доменный процесс (states/transitions + guards) надо либо (а)
компилировать в DAG «на конкретный plan», либо (б) хранить как FSM отдельно и использовать
pipeline только как executor для run‑фазы. 
2) Tool‑agnostic checks — обычно ваша ответственность. OPA/Conftest решает policy‑as‑code, но
«единый CheckSpec» + «поддержка разных движков» (conftest, линтеры, тесты, AI‑чеки) обычно
делается вашим слоем-адаптером. 
3) Event history есть, но “decision history” нет. Temporal хранит богатую event history workflow
execution. В CI‑системах история — это логи/статусы джобов. Но «почему приняли решение о
переходе состояния» и «какие guards сработали» чаще всего нужно явно логировать/хранить как
доменные events. 
Проверенные людьми SDLC‑процессы и шаблоны
Ниже — проекты/документы, которые можно считать «проверенными людьми» (battle‑tested) и
полезными как процессные шаблоны для вашей системы:
Merge gating / merge queue паттерн: Prow Tide («merge pool», ретест и автомерж при
соблюдении критериев) — это практический шаблон того, как формализовать «готовность к
merge» как набор условий + автоматическое исполнение. 
Исторически похожий паттерн описан bors‑подходом (очередь мержа, staging,
batch‑тестирование), даже если bors‑ng сейчас архивирован — как модель процесса он
полезен. 
99
100
101
102
• 
103
90
9
<PARSED TEXT FOR PAGE: 10 / 16>
plan/apply через PR events: Atlantis прямо документирует модель «слушаем PR webhooks →
делаем plan/apply → комментируем результат в PR», что практически тот же «plan/run/apply»
контур, только на Terraform‑домены. 
Docs‑as‑code на масштабе: Backstage TechDocs описан как docs‑as‑code внутри портала; в
документации утверждается использование в Spotify на уровне тысяч doc‑сайтов и
ежедневных просмотров. Это хороший шаблон того, как рендерить и хостить «процессную
документацию» и диаграммы как часть SDLC. 
Code review как формализованный gate:
Документация Google Engineering Practices подробно описывает, что проверять в code review
(design, tests, readability и т.д.). 
Microsoft Engineering Fundamentals Playbook фиксирует практики code review/PR. 
Эти документы полезно «перевести» в ваши CheckSpec (часть — как conftest/линтеры, часть —
как AI‑чеки/чеклисты).
Branching и интеграционная дисциплина:
GitHub Flow как простой PR‑центричный процесс. 
Trunk‑Based Development как модель «не ломать trunk», короткоживущие ветки и практики,
уменьшающие merge hell. 
Локальный “shift‑left” gate: pre-commit прямо объясняет мотивацию — ловить тривиальные
проблемы до code review, освобождая ревьюерам время на архитектуру. Это практически
«локальный trigger/runner» слой вашего процесса. 
Рекомендуемые стеки и план интеграции с вашим DSL
Ниже — две «лучшие комбинации» (стека) под вашу цель: минимум самописного кода, но при этом
future‑proof (легко подключать новые инструменты и подходы).
Стек A: Temporal как ядро + Dagger как executor + OPA/Conftest + pre-commit +
мермаид‑рендер
Почему это минимизирует кастомный код: Temporal уже даёт durable execution + event history +
message passing + Web UI и поддерживает расширение worker setup через плагины/интерсепторы.
Dagger закрывает «выполняй одинаково локально и в CI», плюс трассировка через OpenTelemetry
помогает дебажить сложные планы. 
Conftest/OPA дают реальный policy‑as‑code движок, а pre-commit — стандартный локальный триггер.
Tradeoffs: нужен Temporal cluster (или dev‑режим для старта), а также придётся определить ваше
отображение DSL → workflow/activities и каналы событий (webhooks → signals/updates). 
• 
7
• 
104
• 
• 
105
• 106
• 
• 107
• 
108
• 
109
110
111
112
10
<PARSED TEXT FOR PAGE: 11 / 16>
Стек B: Tekton (Pipelines+Triggers) + Tekton Results + OPA/Conftest + pre-commit +
Backstage TechDocs
Почему это минимизирует кастомный код: Tekton закрывает CI‑орchestrator, Triggers закрывают
событийный вход (webhooks), а Results добавляет долговременную историю и хранение логов
отдельно от etcd. 
Backstage TechDocs закрывает «портализацию» процесса/диаграмм (включая docs‑as‑code подход), а
conftest — policy‑as‑code. 
Tradeoffs: Kubernetes‑инфраструктура и типичная сложность «k8s‑native CI». Доменные
FSM‑состояния всё равно придётся хранить как отдельный слой (или как аннотации/CRDs +
корреляция с PipelineRun/Results). 
Пошаговая стратегия миграции и адаптации под ваш DSL
Шаги ниже построены так, чтобы вы могли начать с pre-commit + conftest (как вы и планируете), а
затем «подложить» более мощный backend без ломки архитектуры.
1) Зафиксировать промежуточный контракт (IR) вместо привязки к конкретным тулзам
Определите в коде (и в схеме) стабильные типы: - ProcessSpec : states, transitions, guards, invariants.
- CheckSpec : id, inputs (files/refs), engine ( conftest , command , ai_check , …), severity, tags. -
ExecutionPlan : упорядоченный список шагов + зависимости + expected transitions. -
CheckResult : status, evidence (logs/artifacts), suggested_fix (diff/patch), metrics. - ProcessEvent :
timestamp, actor, trigger, transition, checkout SHA, policy decisions.
Так вы получаете «место», куда в будущем встроятся новые инструменты (например, новый агентный
runtime или новый policy engine), как просто новый engine / adapter .
2) Реализовать plan/run/apply как чистые функции вокруг IR
- plan(context) -> ExecutionPlan : вычисляет, какие проверки нужны и какие переходы
допустимы (без исполнения).
- run(plan) -> RunReport : исполняет (локально/в CI), собирает CheckResult .
- apply(report) -> NewState + EventLogAppend : принимает решение о переходах, фиксирует
историю, генерирует рендеры (диаграммы/доки), опционально комментирует PR.
Паттерн Atlantis («plan/apply по PR webhooks и комментариям») полезно взять как референс UX для
apply‑фазы. 
3) Адаптеры для conftest и pre-commit как первые “бэкенды” - ConftestAdapter: запускает
conftest, парсит deny‑сообщения, маппит в CheckResult (включая payload с указанием файла/
правила). Conftest позиционируется как инструмент тестирования структурированных конфигов и
работает поверх OPA/Rego. 
- PreCommitAdapter: предоставляет один «hook entry» (например, orchestrator plan && 
orchestrator run --local ) и превращает провалы CheckResult в понятный вывод, чтобы
остановить commit. Мотивация pre-commit — именно в том, чтобы ловить проблемы раньше code
review. 
Если нужно — можно использовать готовые хуки для форматирования Rego, например pre￾commit‑opa. 
113
114
24
86
115
109
116
11
<PARSED TEXT FOR PAGE: 12 / 16>
4) Добавить “State store/history” минимальными средствами
До появления «большого» движка можно хранить: - state.yaml в репозитории (как у вас уже есть
паттерн state‑yaml в метаданных) + append‑only events.jsonl .
Но если вы выбираете Temporal, то event history и «durable log» уже существуют, и вашу доменную
историю можно либо (а) хранить как workflow events/markers, либо (б) синхронизировать в отдельное
хранилище. Temporal прямо описывает, что сервис хранит полную event history lifecycle workflow
execution. 
5) Подключить один “сильный backend” (Temporal или Tekton) без смены DSL
- Для Temporal: компилируете ExecutionPlan в workflow: каждый шаг → Activity; переходы и guards
→ workflow state + message handlers; triggers → signals/updates. Тем более, Temporal прямо описывает
Workflows как stateful сервисы, которые принимают signals/queries/updates. 
- Для Tekton: компилируете ExecutionPlan в PipelineRun; Triggers связываете с GitHub/GitLab
webhooks; историю запусков и логи отдаёте в Tekton Results. 
6) Добавить Renderers как обязательный артефакт apply‑фазы - Минимум: генерировать
Mermaid‑диаграмму процесса и диаграмму фактического Run (DAG/последовательность) как *.md
артефакт.
- Если используете Backstage: публиковать это в TechDocs (docs‑as‑code), что уже описано как
центральная модель «md рядом с кодом → doc site в портале». 
- Если используете Dagger как executor: можно прикладывать OpenTelemetry traces как
диагностический слой исполнения. 
7) Опционально: добавить agent‑executor как “плагин”, не как ядро - OpenHands удобен как agent
runtime: SDK заявляет готовые tools (bash, files, web, MCP) и GitHub Action триггеры по label/
комментам. 
- Continue удобен как «AI checks как files‑as‑code» (markdown checks) и как CLI agent loop. 
В обоих случаях будущая устойчивость достигается тем, что агент — это просто один из executors, а
guards/policies/история решений остаются у вашего DSL.
Ниже — как это выглядит на уровне адаптеров (важно: ваш DSL/IR остаётся одним, меняются только
бэкенды):
flowchart LR
 IR["ProcessSpec + CheckSpec IR"] --> Planner["Planner (plan)"]
 Planner --> Plan["ExecutionPlan artifact"]
 Plan --> Runner["Runner (run)"]
 Runner -->|policy| ConftestAdapter["ConftestAdapter"]
 Runner -->|commands| CmdAdapter["Command/Dagger/Jenkins adapter"]
 Runner -->|agent| AgentAdapter["Agent adapter (OpenHands/Continue/Codex)"]
 Runner --> Report["RunReport: CheckResults + artifacts"]
 Report --> Applier["Applier (apply)"]
117
118
113
104
56
76
66
12
<PARSED TEXT FOR PAGE: 13 / 16>
 Applier --> StateStore["State store + Event log"]
 Applier --> Renderers["Renderers (Mermaid/TechDocs/UI)"]
https://github.com/temporalio/temporal
https://github.com/temporalio/temporal
https://docs.temporal.io/workflow-execution/event
https://docs.temporal.io/workflow-execution/event
https://tekton.dev/docs/pipelines/pipelineruns/
https://tekton.dev/docs/pipelines/pipelineruns/
https://www.jenkins.io/doc/book/pipeline/pipeline-as-code/
https://www.jenkins.io/doc/book/pipeline/pipeline-as-code/
https://docs.openhands.dev/sdk
https://docs.openhands.dev/sdk
https://docs.temporal.io/encyclopedia/event-history
https://docs.temporal.io/encyclopedia/event-history
https://github.com/runatlantis/atlantis
https://github.com/runatlantis/atlantis
https://pre-commit.com/
https://pre-commit.com/
https://docs.temporal.io/develop/plugins-guide
https://docs.temporal.io/develop/plugins-guide
https://github.com/temporalio/temporal/commits
https://github.com/temporalio/temporal/commits
https://github.com/open-policy-agent/conftest
https://github.com/open-policy-agent/conftest
https://docs.temporal.io/sending-messages
https://docs.temporal.io/sending-messages
https://tekton.dev/docs/pipelines/tasks/
https://tekton.dev/docs/pipelines/tasks/
https://github.com/tektoncd/pipeline
https://github.com/tektoncd/pipeline
https://docs.prow.k8s.io/docs/components/plugins/
https://docs.prow.k8s.io/docs/components/plugins/
https://github.com/tektoncd/results
https://github.com/tektoncd/results
https://github.com/orgs/tektoncd/repositories
https://github.com/orgs/tektoncd/repositories
119
1 12 14 15 57 112
2 13 117
3 24
4 36 37 41 65 97
5 76 77
6 102 110
7 86 87
8 92 109
9 17 18
10 85
11 101 115 119
16
19 20 22 23 91
21 79
25 43 47
26 49
27
13
<PARSED TEXT FOR PAGE: 14 / 16>
https://backstage.io/docs/features/techdocs/
https://backstage.io/docs/features/techdocs/
https://argoproj.github.io/workflows/
https://argoproj.github.io/workflows/
https://argo-workflows.readthedocs.io/en/latest/walk-through/dag/
https://argo-workflows.readthedocs.io/en/latest/walk-through/dag/
https://github.com/argoproj/argo-workflows
https://github.com/argoproj/argo-workflows
https://argo-workflows.readthedocs.io/en/latest/fields/
https://argo-workflows.readthedocs.io/en/latest/fields/
https://github.com/bors-ng/bors-ng
https://github.com/bors-ng/bors-ng
https://github.com/jenkinsci/jenkins
https://github.com/jenkinsci/jenkins
https://plugins.jenkins.io/github/
https://plugins.jenkins.io/github/
https://www.jenkins.io/doc/developer/architecture/extensions/
https://www.jenkins.io/doc/developer/architecture/extensions/
https://docs.prow.k8s.io/docs/jobs/
https://docs.prow.k8s.io/docs/jobs/
https://github.com/kubernetes-sigs/prow/commits
https://github.com/kubernetes-sigs/prow/commits
https://docs.prow.k8s.io/docs/overview/architecture/
https://docs.prow.k8s.io/docs/overview/architecture/
https://github.com/dagger/dagger
https://github.com/dagger/dagger
https://docs.dagger.io/getting-started/api/sdk
https://docs.dagger.io/getting-started/api/sdk
https://docs.dagger.io/getting-started/ci-integrations/github-actions/
https://docs.dagger.io/getting-started/ci-integrations/github-actions/
https://docs.dagger.io/features/reusability/
https://docs.dagger.io/features/reusability/
https://docs.dagger.io/features/observability
https://docs.dagger.io/features/observability
https://backstage.io/docs/features/software-templates/
https://backstage.io/docs/features/software-templates/
https://backstage.io/docs/features/software-templates/writing-templates/
https://backstage.io/docs/features/software-templates/writing-templates/
28 62 64 72 104 114
29
30 32 100
31 42
33 34
35 89 90
38
39
40
44 46
45 94
48
50 51 52
53
54
55 88
56
58
59
14
<PARSED TEXT FOR PAGE: 15 / 16>
https://github.com/backstage/backstage/commits
https://github.com/backstage/backstage/commits
https://backstage.io/docs/frontend-system/building-plugins/index/
https://backstage.io/docs/frontend-system/building-plugins/index/
https://docs.continue.dev/
https://docs.continue.dev/
https://docs.continue.dev/checks/running-in-ci
https://docs.continue.dev/checks/running-in-ci
https://github.com/continuedev/continue
https://github.com/continuedev/continue
https://docs.continue.dev/checks/reference
https://docs.continue.dev/checks/reference
https://docs.continue.dev/agents/overview
https://docs.continue.dev/agents/overview
https://github.com/OpenHands/OpenHands
https://github.com/OpenHands/OpenHands
https://docs.openhands.dev/openhands/usage/run-openhands/github-action
https://docs.openhands.dev/openhands/usage/run-openhands/github-action
https://arxiv.org/html/2511.03690v1
https://arxiv.org/html/2511.03690v1
https://docs.langchain.com/oss/python/langgraph/graph-api
https://docs.langchain.com/oss/python/langgraph/graph-api
https://docs.langchain.com/oss/python/langgraph/persistence
https://docs.langchain.com/oss/python/langgraph/persistence
https://github.com/langchain-ai/langgraph/commits
https://github.com/langchain-ai/langgraph/commits
https://reference.langchain.com/python/langgraph/checkpoints/
https://reference.langchain.com/python/langgraph/checkpoints/
https://google.github.io/eng-practices/review/reviewer/looking-for.html
https://google.github.io/eng-practices/review/reviewer/looking-for.html
https://openpolicyagent.org/docs
https://openpolicyagent.org/docs
https://docs.temporal.io/encyclopedia/workflow-message-passing
https://docs.temporal.io/encyclopedia/workflow-message-passing
https://docs.prow.k8s.io/docs/components/core/tide/
https://docs.prow.k8s.io/docs/components/core/tide/
https://microsoft.github.io/code-with-engineering-playbook/code-reviews/
https://microsoft.github.io/code-with-engineering-playbook/code-reviews/
60
61 63
66
67 69 99
68
70
71
73 75
74
78
80
81 83
82
84
93 105
95 111
96 118
98 103
106
15
<PARSED TEXT FOR PAGE: 16 / 16>
https://docs.github.com/en/get-started/using-github/github-flow
https://docs.github.com/en/get-started/using-github/github-flow
https://trunkbaseddevelopment.com/
https://trunkbaseddevelopment.com/
https://tekton.dev/docs/triggers/triggers/
https://tekton.dev/docs/triggers/triggers/
https://github.com/anderseknert/pre-commit-opa
https://github.com/anderseknert/pre-commit-opa
107
108
113
116
16

</agent>
<agent>
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


</agent>
<user>
Да, подготовь всё кроме кода для первой итерации.

</user>
<agent>
Сейчас заново соберу “пакет первой итерации”: структуру `.sdlc/`, форматы файлов DSL (ProcessSpec/State/Plan/Report/Events), инварианты и правила переходов, шаблоны `AGENTS.md`, ритуал работы Nick↔Codex и критерии готовности — без реализации кода.


</agent>
<agent>
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


</agent>
<user>
да, подготовь.

</user>
<agent>
Сделаю “Iteration 1.1” поверх уже подготовленного DSL: зафиксирую канонические типы событий и их схемы, конвенции для `data`, и шаблон reviewer‑packet, который Codex обязан формировать перед `waiting_human`.


</agent>
<agent>
Готово — подготовил “Iteration 1.1” пакет **без кода**, который добавляет:

1. **канонические типы событий** (decision/execution history)
2. **конвенции для `data`/refs/ID/status**
3. **минимальный Human/Reviewer Packet**, который Codex обязан заполнять перед `waiting_human`

[Скачать nick-sdlc-iter1.1.zip](sandbox:/mnt/data/nick-sdlc-iter1.1.zip)

---

## Что добавлено (по вашему запросу)

### 1) Канонические event types + обязательные поля

Файл: `EVENTS.md`

- Описывает envelope события (`seq/ts/actor/type/message/data`)
- Для каждого `type` задаёт **что именно должно быть в `data`**
- Вводит обязательное событие:
  - `human_packet_written` — **обязательно перед остановкой на человека**

Также обновлено:

- `.sdlc/schemas/event.schema.json` → **v0.1.1**\
  (включает `human_packet_written` и минимальные требования к `data` для ключевых типов)

---

### 2) Конвенции для `data` и ссылок (единый стиль)

Файл: `CONVENTIONS.md`

- ID-паттерны: `A###`, `H###`, `S###`, `check_id`
- `data.refs` — единый формат ссылок на `state/plan/report/packet/logs`
- Стандарты для логов/“evidence” (`.sdlc/logs/<subject>-<ts>.txt`)
- Единые enum’ы статусов (run/actions/steps/checks)
- Минимальная шкала рисков

---

### 3) Минимальный Reviewer/Human Packet

Файл: `HUMAN_PACKET.md`

- Чётко фиксирует: **когда обязателен пакет** (перед `waiting_human` / при создании blocking `needs_human`)
- Определяет `kind: decision|review`
- Даёт чек‑лист обязательных секций (заголовок → запрос к Nick → что сделано → evidence → risk → rollback → next step)
- Запрещает секреты/простыни кода

Шаблоны/примеры (внутри `.sdlc/`):

- `.sdlc/review_packet.md` (обязательный шаблон)
- `.sdlc/review_packet.example.md` (пример заполнения)
- `.sdlc/review_packet.yaml` + `.example.yaml` (опционально, если захотите ещё и структурированный пакет)
- `.sdlc/schemas/review_packet.schema.json` (схема для YAML/JSON варианта)

---

## Что обновлено в протоколе Codex

Файл: `AGENTS.md`

Добавлено жёсткое правило:

**Перед тем как поставить `run.status: waiting_human` или создать blocking `needs_human`:**

1. записать/обновить `.sdlc/review_packet.md`
2. дописать событие `human_packet_written`
3. только потом выставлять `waiting_human` и останавливаться

---

## Ещё мелкие правки в пакет

- `SPEC.md` обновлён до **Iteration 1.1** (добавлен Human Packet как артефакт + инварианты)
- `gitignore.sdlc.txt` дополнен (игнор review\_packet + `.sdlc/logs`)
- `state.yaml` и `state.example.yaml` дополнены ссылками:
  - `artifacts.review_packet_ref`
  - `artifacts.review_packet_yaml_ref`
- `events.sample.jsonl` расширен примерами (включая `human_packet_written`)
- `run.example.mmd` обновлён (показан шаг генерации пакета)

---

## Как использовать (в вашем ручном режиме)

1. Скопируйте из zip в workspace/репо:
   - `EVENTS.md`, `CONVENTIONS.md`, `HUMAN_PACKET.md`
   - обновлённые `AGENTS.md`, `SPEC.md`
   - папку `.sdlc/` (или точечно нужные файлы)
2. Добавьте `gitignore.sdlc.txt` в `.gitignore`
3. Работайте как раньше:
   - вы создаёте workspace и запускаете Codex
   - **Codex синхронизируется только через `.sdlc/state.yaml` + `.sdlc/events.jsonl`**
   - когда нужен вы → Codex обязан заполнить `review_packet.md` и поставить `waiting_human`

---

Если хотите, следующим шагом (тоже без кода) могу подготовить **“каталог policy decisions”** (типовые `needs_human` для network/deps/scope/merge/deploy) + готовые формулировки вопросов/опций/рекомендаций, чтобы Codex не придумывал их каждый раз заново.


</agent>
<user>
а ты не начал уже перераздувать DSL? Разве он не должен формироваться под проект за счёт встреченных задач?

</user>
<agent>
Да — вы правы, и вы вовремя это поймали.

Я действительно начал **структурировать “на вырост”**, и это легко превращается в “мини‑стандарт”, который начинает жить своей жизнью. А для вашей текущей стадии (ручные workspaces + ручной запуск Codex) DSL должен быть **тонкой талией (thin waist)** и **расти от встреченных задач**, а не “сверху вниз”.

Нормальная траектория такая:

- **v0 (минимум)**: только то, без чего вы *сейчас* не можете синхронизировать состояние.
- **v0.x (эволюция)**: добавляем поля/типы **только** когда повторяется боль / появляется автоматизация, которой нужен контракт.
- Всё остальное — в **extensions/free‑form** до момента, когда это станет стабильным.

Ниже — как я бы “сдул” это обратно и как бы задавал правила роста.

---

## Минимально жизнеспособный DSL для Iteration 1

Если строго следовать вашему тезису “одинаково видеть состояние” и **YAGNI**, то ядро — всего 3 артефакта + протокол:

1. `.sdlc/process.yaml` — FSM (states + transitions)
2. `.sdlc/state.yaml` — текущий state + next actions + needs\_human
3. `.sdlc/events.jsonl` — append‑only “что произошло/почему”
4. `AGENTS.md` — правила, что Codex **обязан** читать/обновлять

Всё.\
`checks.yaml/plan.yaml/report.yaml/review_packet.*` — **не обязательны** для первой волны, если вы пока не строите раннер/валидацию.

---

## Почему “канонические event types” и “human packet” могут быть лишними сейчас

### Event types

Пока у вас нет инструментов, которые **фильтруют/агрегируют** события, строгая таксономия типов — это нагрузка на агента и вас.

Для итерации 1 достаточно:

- `type: note` (любая запись)
- `type: state_change`
- `type: needs_human`

И всё остальное — **как свободный текст или namespaced строка**, без обязательной схемы.

### Human packet

Пакет полезен, когда:

- вы часто попадаете в `waiting_human`,
- и хотите, чтобы каждая остановка была “дешёвой” по вниманию.

Но делать “пакет обязателен всегда” — это может быть рано.\
Правильнее: **шаблон есть**, но становится обязательным **после первого реального случая**, когда Nick тратит >10 минут на разбор контекста.

---

## Как дать DSL “формироваться под проект” и не распухать

### Правило 1 — Добавляем в core только по критерию повторяемости

Поле/тип/структуру переводим в “основной контракт”, только если выполняется одно из условий:

- 🔁 **встречается минимум 3 раза** в разных задачах и каждый раз вы импровизируете
- 🚦 нужно для **гейтинга/переходов FSM** (“если X, то нельзя идти дальше”)
- 🧰 нужно для **инструмента** (валидатор, рендер, отчёт) — иначе инструмент не работает
- 🧠 экономит внимание Nick (повторяющиеся вопросы/решения становятся структурированными)

Если не выполняется — это остаётся **free-form**.

---

### Правило 2 — “Свободные расширения” вместо новых полей

Чтобы DSL мог расти, но core не пух:

В `state.yaml` держите блок:

```yaml
extensions: {}
```

И туда складывайте всё “пока непонятно, станет ли стандартом”:

```yaml
extensions:
  github:
    pr_url: "..."
  ci:
    last_run: "..."
  security:
    touched_auth: true
```

Когда устоится — переносите в core.

---

### Правило 3 — События: минимальный “зарезервированный набор” + namespacing

Не надо заранее перечислять 25 типов событий.

Сделайте так:

- Зарезервированные:
  - `note`
  - `state_change`
  - `needs_human`

- Всё остальное — строка с namespace:
  - `ci.run.finished`
  - `git.commit.created`
  - `deps.change.requested`

Пока нет инструмента, который “понимает” эти события — они просто строки.

---

### Правило 4 — Схемы не должны душить эволюцию

JSON Schema в ранних итерациях должна:

- гарантировать **форму ядра** (state/process),
- и допускать `additionalProperties: true` в `data/extensions`, чтобы не блокировать рост.

Иначе вы будете менять схемы быстрее, чем делать SDLC.

---

## Что делать с тем, что я уже “нарастил” в Iteration 1.1

Считайте Iter 1.1 не “обязательным DSL”, а **каталогом опциональных модулей**, который вы подключаете по мере необходимости:

- `CONVENTIONS.md` — полезно почти сразу (единый стиль, меньше хаоса)
- `EVENTS.md` — подключаете, когда начнёте делать поиск/аналитику/валидацию событий
- `review_packet.md` — подключаете, когда `waiting_human` станет частым и дорогим

То есть это **не часть core DSL**, а “надстройки”.

---

## Практичный процесс эволюции (чтобы DSL реально рос от задач)

После каждой задачи делайте 10‑минутный “ретро‑коммит” в DSL:

1. Что было непонятно при чтении state?
2. Какие вопросы Nick задавал дважды?
3. Какие решения повторились? (например, “разрешить deps”, “включить сеть”, “скоп большой”)
4. Что агент делал “по‑разному” два раза?

Из этого:

- либо добавляете **одно поле** в core,
- либо добавляете **один шаблон needs\_human.kind**,
- либо оставляете как есть.

**Лимит: максимум 1–2 изменения DSL на задачу**, иначе начнётся “перепроектирование вместо разработки”.

---

## Если хотите — я предложу “сдутое” ядро прямо в терминах ваших файлов

Скажите, и я дам “Iteration 1 core” в виде:

- минимального `process.yaml`
- минимального `state.yaml` (с `extensions` и без лишнего)
- минимального формата `events.jsonl` (3 типа)
- обновлённого `AGENTS.md`, где Codex обязан только: читать state → делать next action → обновлять state → писать событие

Без review packet, без plan/report/checks — пока вы сами не почувствуете, что оно нужно.

Главное: вы абсолютно правильно мыслите — **DSL должен “отливаться” по факту реальных кейсов**, а не быть заранее идеальным.


</agent>
<user>
перед этим просмотри документ по схожей теме и подумай не надо ли что-то позаимствовать. заимствование необязательно, мне нужна простота и надёжность.

</user>
<agent>
Посмотрел документ. Он описывает классический GPS/STRIPS‑подход: **состояние = множество булевых фактов**, а “шаг/оператор” задаётся как `preconds` → применимость, и эффект как `add/delete` над множеством фактов (closed‑world: чего нет в списке — считается ложным). Плюс там же даны простые инварианты (например, `add` не пересекается с `delete`, без дублей, нормализовать имена фактов) и замечание про “трейс действий” как отдельную сущность. fileciteturn1file0

### Что стоит позаимствовать, чтобы было **проще и надёжнее**

Я бы **взял ровно одну сильную идею** и оставил остальное опциональным:

1. **`facts[]` как “тонкая талия” расширяемости**\
   Вместо того чтобы добавлять новые поля в DSL под каждую новую ситуацию, вы добавляете **новый факт‑строку**. Это как раз отвечает вашему требованию “DSL формируется под проект за счёт встреченных задач”. fileciteturn1file0

2. **(Опционально) семантика шага в стиле STRIPS (`preconds/add/delete`) — но только когда понадобится**\
   Не для “планировщика сейчас”, а чтобы:
   - избегать случайных нелегальных переходов,
   - иметь возможность позже добавить авто‑валидацию/полу‑детерминированное планирование,
   - и при этом не распухать схемой. fileciteturn1file0

### Что **не** стоит заимствовать на этом этапе

- **Полный “Problem DSL” со `start/finish/ops` как основа всей системы** — это уже про автоматическое планирование, а вы сейчас решаете задачу синхронизации состояния.
- “Хак” с `Executing ...` как факт для трейсинга — вам проще и надёжнее держать **append‑only events.jsonl** (у вас уже есть канал для истории, значит трейс — отдельным логом, не фактом). В документе сам трейс выделен как отдельная тема, и это правильно. fileciteturn1file0

---

## Итог: “сдутое” ядро Iteration 1 (Core)

**Обязательные файлы всего 3 + протокол:**

- `.sdlc/process.yaml` — *coarse* FSM стадий SDLC (intake/plan/implement/verify/…)
- `.sdlc/state.yaml` — **canonical state snapshot**:
  - `run.stage`, `run.status`
  - `facts[]` (булевы факты, растут от задач)
  - `next_actions[]`, `needs_human[]`, `artifacts{…}`
  - `extensions{}` (всё нестабильное/экспериментальное)
- `.sdlc/events.jsonl` — append‑only “что изменилось и почему”
- `AGENTS.md` — правила Codex: читать state → делать next action → обновлять state → писать event → спрашивать Nick и стоп, если blocking

**Ключевой момент из документа:** факты сравниваются по **строковому равенству**, поэтому для надёжности нужны простые правила именования и отсутствие “свободного текста” в фактах. fileciteturn1file0\
(Я предлагаю `dot.namespace` или `snake_case`: `ci.tests_pass`, `pr.open`, `git.branch_created`.)

---

## Я подготовил для вас “Iteration 1 Core” пакет (без кода)

Он отражает именно этот “тонкий” подход: минимальные файлы, `facts[]` как главный механизм роста, и только лёгкие инварианты.

[Скачать nick-sdlc-iter1-core.zip](sandbox:/mnt/data/nick-sdlc-iter1-core.zip)

### Что внутри

- `SPEC.md` — минимальная спецификация + инварианты + правила эволюции
- `AGENTS.md` — протокол для Codex (без “обязательных пакетов”, без жёсткой таксономии событий)
- `.sdlc/process.yaml` — FSM
- `.sdlc/state.yaml` — snapshot с `facts[]` и `extensions{}`
- `.sdlc/events.jsonl` (пустой) + `events.sample.jsonl`
- `FACTS.md` (опциональный реестр фактов — чтобы не ловить опечатки и дрейф)

---

## Как DSL будет “формироваться от задач” (практическое правило)

Чтобы DSL не раздувался:

- Новая потребность → **сначала** добавляете факт в `facts[]` или запись в `extensions{}`.
- Поле становится “core” только если:
  - повторилось **3+ раза**, или
  - нужно для гейта/перехода, или
  - нужно для инструмента, который вы реально строите *прямо сейчас*.

Так вы получаете и простоту, и надёжность, и естественную эволюцию.

Если хотите, следующим шагом я могу “обратно сократить” ваш текущий Iter 1.1 (с event types / packet) до **модульных “плагинов”**, чтобы core оставался тонким, а всё строгое включалось только когда реально заболит.


</agent>
<user>
я не понял как должны работать facts. в документации для агента это достаточно понятно объяснено? я ещё не читал

</user>
<agent>
`facts` — это **не “ещё один слой статусов”**, а максимально простой механизм: **множество булевых утверждений** (строк), которые “истинны сейчас”.

Идея из того документа ровно такая:

- **Fact** = атомарное утверждение (строка) типа `son_at_home`, `car_works`.
- **State** = множество фактов, которые истинны.
- Всё, чего **нет** в списке, считается ложным (closed‑world).
- Оператор меняет состояние через `add/delete` над множеством фактов. fileciteturn1file0

В нашем SDLC‑контексте мы **берём только часть про state=facts** (без планировщика GPS на первой итерации): `facts` — это “тонкая талия”, чтобы DSL **не распухал полями**, а рос через новые факты по мере реальных задач.

---

## Как `facts` должны работать у вас

### 1) Семантика (простая)

- `facts` — **set строк** (без дублей).
- Факт **истинен**, если он **присутствует** в списке.
- Отсутствие факта = “не истинно” (в строгом GPS это “ложно”). fileciteturn1file0\
  Для надёжности в вашей системе лучше интерпретировать так: **“не утверждено как true”** — и **не строить критичных решений на отсутствии**, пока вы не автоматизировали вывод фактов.

### 2) Зачем они нужны, если есть `run.stage`

`run.stage` — грубая стадия SDLC (“plan/implement/verify”).\
`facts` — мелкие булевы “флажки” вокруг этого:

- что уже реально сделано (`git.branch_created`)
- какие условия выполнены (`checks.tests_pass`)
- какие риски/ограничения включились (`policy.network_needed`)
- что блокирует работу (`human.blocking_question_open` — можно сделать derived)

Это позволяет **не добавлять** каждый раз новое поле в DSL.

### 3) Когда их добавлять/удалять

Правило для Codex и для вас:

- **после каждого meaningful шага** (создал ветку, внёс изменения, прогнал тесты, открыл PR)\
  → обновить `facts` (добавить/удалить то, что изменилось)\
  → и **обязательно** дописать событие в `events.jsonl` (“почему факты изменились”).

---

## Мини‑пример “до/после”

### До: ветка создана, тесты не гонялись

```yaml
run:
  stage: implement
facts:
  - workspace.created
  - git.repo_cloned
  - git.branch_created
```

### После прогона тестов, упали

```yaml
facts:
  - workspace.created
  - git.repo_cloned
  - git.branch_created
  - checks.tests_fail
```

### После фикса и зелёных тестов

```yaml
facts:
  - workspace.created
  - git.repo_cloned
  - git.branch_created
  - checks.tests_pass
```

(обратите внимание: `checks.tests_fail` удалили)

---

## Правила, чтобы было **просто и надёжно**

1. **Факты — только булевы.**\
   Никаких значений.
   - ✅ `pr.open`
   - ❌ `pr.url=https://...`\
     URL кладём в `artifacts.pr_url`, а фактом отмечаем состояние (`pr.open`).

2. **Нормализация имен:** `dot.namespace` или `snake_case`.\
   GPS сравнивает факты по **строковому равенству**, поэтому опечатки = разные факты. fileciteturn1file0\
   Пример: `git.branch_created`, `ci.tests_pass`.

3. **Эксклюзивные пары/группы держим взаимоисключающими.**\
   Для простоты итерации 1 достаточно пары:
   - `checks.tests_pass` XOR `checks.tests_fail`
   - `checks.lint_pass` XOR `checks.lint_fail`

4. **Если не уверен — не утверждай факт.**\
   Лучше оставить факт отсутствующим и написать `needs_human` или `event note`. Это повышает надёжность.

5. **Факт должен иметь “обоснование” в истории.**\
   Если выставили `checks.tests_pass`, пусть в `events.jsonl` будет событие “ran tests” (и желательно ссылка на лог в `artifacts.logs[]`).

6. **Факты — про “что истинно сейчас”, события — про “что произошло”.**\
   Не пытайтесь хранить историю в facts.

---

## В “документации для агента” это объяснено достаточно понятно?

Сейчас в **AGENTS.md** (из core‑пакета) `facts` упомянуты как:

> “`facts` (add/remove booleans that changed)”

То есть **агенту сказано “обновляй facts”**, но **семантика (что это и как именно вести) больше раскрыта в SPEC.md**: там прямо написано “facts-as-state”, closed-world, правила именования, “facts is a set”. fileciteturn1file0

Если ваша цель — чтобы Codex **не интерпретировал это по‑своему**, то я бы добавил в AGENTS.md маленький блок “Facts 101”. Вот готовый текст (можно вставить без изменений):

```md
## Facts (boolean truth set)
- `facts` is a SET of strings. A fact is true iff it is present in `facts:`.
- Keep facts boolean. Do NOT encode values in facts (URLs/SHAs/paths go to `artifacts.*` or `extensions.*`).
- Prefer `dot.namespace` names (e.g. `git.branch_created`, `checks.tests_pass`).
- For multi-valued statuses keep them mutually exclusive (e.g. remove `checks.tests_fail` when adding `checks.tests_pass`).
- After any step that changes facts: update `.sdlc/state.yaml` AND append an event to `.sdlc/events.jsonl` explaining why.
- If unsure, do not assert a fact; ask Nick via `needs_human` or add a `note` event.
```

---

## Чтобы facts “формировались от задач”, а не распухали

Оставьте `FACTS.md` **пустым** и пополняйте его только когда:

- один и тот же факт появился 2–3 раза,
- или вы ловили опечатки/дрейф.

Это будет поддерживать простоту.

---

Если хотите, я предложу **стартовый минимальный набор фактов (10–15 штук)** именно под ваш ручной режим “workspaces + Codex”, чтобы не изобретать каждый раз, но без раздувания “словаря”.


</agent>
<user>
получается что нужно поддерживать набор фактов и переходы между ними? ну это звучит вроде бы надёжно, осталось найти то, какие факты могут быть и их переходы.

и это тоже звучит как fsm.

</user>
<agent>
Да — **в математическом смысле** “множество фактов + правила, которые их добавляют/удаляют” действительно описывает **систему переходов состояний**, то есть *по сути FSM*. Разница в том, **что вы не храните FSM “явно”** (узлы/рёбра), а задаёте её **компактно** через *факторизованное состояние* (набор булевых признаков) и *операторы* `preconds/add/delete`. Именно так это и описано в вашем документе про GPS/STRIPS: состояние = множество фактов, оператор применим если `preconds ⊆ S`, а новое состояние `S’ = (S − delete) ∪ add`. fileciteturn1file0

Но из этого **не следует**, что вам теперь нужно “поддерживать переходы между фактами” как граф. Вам **не нужно** перечислять переходы между *всеми комбинациями* фактов — это было бы 2^N состояний. Надёжность как раз достигается тем, что вы **не моделируете всё явно**, а держите:

- **крошечный явный FSM** по стадиям SDLC (`run.stage`)
- **набор фактов** (`facts[]`) как булевы наблюдаемые условия
- *(опционально)* **операторы** (шаблоны действий) как “правила обновления фактов” — только когда это реально начинает приносить пользу

Ниже — как это мыслить и что делать на практике.

---

## 1) Нужны ли “переходы между фактами” прямо сейчас?

### В Iteration 1 — нет

В итерации, где вы **вручную** создаёте workspace и **вручную** запускаете Codex, `facts` могут работать как **просто “truth tags”**:

- после действия вы/агент обновляете `facts[]` (“что стало истинно”)
- добавляете событие в `events.jsonl` (“почему так считаем”)

Никаких `preconds/add/delete` пока не обязательно.

### Когда операторы становятся полезны

Операторы (в стиле документа) нужны, когда вы хотите **хотя бы одно** из трёх:

1. **Валидация**: “ты не мог открыть PR, если не было `git.branch_created`”
2. **Авто-подсказка next\_actions**: “если нет `checks.tests_pass`, следующий шаг — run tests/fix tests”
3. **Детерминированная сборка plan.yaml** (позже)

И даже тогда вы не строите “граф переходов”, вы добавляете *несколько правил-операторов*. Это компактнее и надёжнее. fileciteturn1file0

---

## 2) Да, это похоже на FSM — но “другого типа”

Есть два уровня:

### Уровень A: Stage FSM (маленький, стабильный)

Это ваш `run.stage`: `intake → plan → implement → verify → deliver → waiting_human → done`.

Он нужен, чтобы **не спорить о прогрессе** и чтобы “не утонуть” в деталях.

### Уровень B: Fact state (большой, растущий)

`facts[]` — это “микро-состояние”: булевы утверждения “что истинно сейчас”.

Итого полный state системы можно понимать как пару:

**FullState = (stage, facts\_set)**

Это действительно FSM, но **факторизованный**: состояние не перечисляется, а собирается из признаков.

---

## 3) Как выбирать факты, чтобы было просто и надёжно

Главное правило: **факт должен быть проверяемым** (observable), а не “намерением”.

Хорошие факты (проверяемые):

- `git.repo_cloned`
- `git.branch_created`
- `checks.tests_pass`
- `checks.tests_fail`
- `pr.open`
- `human.blocking_open`

Плохие факты (слишком субъективно/размыто):

- `code_is_good`
- `plan_is_clear`
- `tests_are_enough`

Ещё правило из документа: факты сравниваются по строковому равенству, поэтому нужны нормализованные имена и без свободного текста. fileciteturn1file0

---

## 4) Нужны ли “переходы” для фактов и как их задавать правильно

Если вы всё-таки хотите “надёжность через правила”, то делайте не “переходы факт→факт”, а **операторы** как в GPS:

- `preconds`: какие факты должны быть true
- `add`: какие факты станут true
- `delete`: какие факты станут false

Это ровно STRIPS-семантика из документа. fileciteturn1file0

### Важный момент: проверки/тесты недетерминированы

Например “run tests” может привести к `pass` или `fail`.

Надёжный способ:

- оператор “run\_tests” **не выбирает исход**, а фиксирует факт вида `checks.tests_ran`
- затем вы/агент по результату добавляете **один** из `checks.tests_pass` / `checks.tests_fail`

И держите пару взаимно исключающей (XOR). В документе тоже есть инварианты уровня “не пересекать add/delete” и “убирать дубли”, это про предсказуемость домена. fileciteturn1file0

---

## 5) Практический минимум: стартовый набор фактов (без раздувания)

Чтобы не “искать все факты мира”, начните с 12–15, закрывающих 80% SDLC‑ритуалов:

**workspace / git**

- `workspace.created`
- `git.repo_cloned`
- `git.branch_created`
- `git.commit_created`

**checks**

- `checks.lint_pass` / `checks.lint_fail`
- `checks.tests_pass` / `checks.tests_fail`

**PR / delivery**

- `pr.open`
- `pr.ready_for_review`

**human**

- `human.blocking_open`

**policy**

- `policy.network_needed` (если упёрлись)
- `policy.deps_change_needed` (если упёрлись)

И всё.\
Любой новый факт добавляете **только когда реальная задача потребовала**.

---

## 6) Как это ответить на ваш вопрос “нужно найти факты и их переходы”

Переформулирую так, чтобы стало легче:

- **Найти “все возможные факты” не нужно.** Они появятся по задачам.
- **Переходы между фактами как граф не нужны.**
- Если хотите формальность — описываете **несколько операторов**, которые покрывают повторяемые действия.

И это будет “надёжно” ровно потому, что вы описываете не огромную машину состояний, а маленький набор правил применимости и эффектов. fileciteturn1file0

---

## 7) Рекомендация по вашей простоте (как я бы сделал)

Чтобы сохранить простоту и не “пере-FSM-ить” всё:

1. **Оставьте явный SDLC FSM по стадиям** (7 состояний)
2. `facts[]` используйте как “тонкую талию расширений”
3. Операторы (`preconds/add/delete`) **не вводите**, пока не появится реальная потребность в:
   - авто-валидации, или
   - авто-подсказке next\_actions

Если вы захотите — я могу предложить **минимальный файл `operators.yaml` всего из 6–8 операторов** (clone repo, create branch, commit, run lint, run tests, open PR, ask human) — но только если вы скажете “да, пора”, чтобы не раздувать DSL раньше времени.
</agent>
