# I00-F0005-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0005-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md)

## Source

- chat_id: `I00-F0005-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил структурировать идею Natural Language интерфейса для агентов без добавления новых сущностей: NL-запросы, формализация в схемы/JSON/код, версионируемый контекст-пакет, валидация в рамках контекста и пользовательская читаемость логов (`raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:4`).
2. Пользователь попросил оценить идею по шкале 1-100 с обоснованием (`raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:107`).
3. Пользователь запросил поиск максимально идентичного open-source решения и поручил самостоятельно определить приоритеты поиска (`raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:137`, `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:158`).

## AI Response Summary

1. Агент оформил концепцию как dual-representation pipeline: human-readable logs + formal executable form под versioned context package (`C01`, `C02`, `C03`, `C04`).
2. Идея оценена высоко (85/100) с явными рисками реализации (детерминизм NL-компиляции, стоимость сопровождения контекста, двусмысленность авто-логов) (`C06`).
3. Дана подборка OSS-архетипов, покрывающих части идеи: dialog/NLU platforms, schema-first agent SDKs, NL-to-code executors, explicit context standard (`C07`, `C08`, `C09`, `C10`).

## Extracted Concepts

### C01. Agent query must have two synchronized representations: human NL and formal executable form

- Concept: Один и тот же запрос должен существовать как читаемый человеком лог и как формальная структура для исполнения системой.
- Why it matters: Одновременно решает наблюдаемость для пользователей и машинную управляемость исполнения.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:18`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:26`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:32`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:102`

### C02. Context package acts as versioned transformation contract

- Concept: Контекст описывается программно, поставляется как пакет и задаёт детерминированное преобразование query->actions по версии схемы.
- Why it matters: Управляет совместимостью поведения агентов при обновлениях.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:36`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:40`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:41`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:45`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:46`

### C03. Shared context interpretation between bots and operators is a core design requirement

- Concept: И боты, и человек-оператор используют один и тот же контекст для расшифровки и генерации корректных запросов.
- Why it matters: Убирает разрыв интерпретации и повышает качество контроля.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:50`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:56`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:60`

### C04. Context-bounded validation is required to prevent out-of-scope agent actions

- Concept: Запросы должны валидироваться на принадлежность доступному контексту до исполнения.
- Why it matters: Ограничивает галлюцинации и неконтролируемые команды агентов.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:64`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:66`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:68`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:69`

### C05. Ontology plus executable tooling is viewed as extensible knowledge substrate

- Concept: Формализация понимается как комбинация онтологии и кода (например Python), которая позволяет строить дополнительные производные представления (knowledge map).
- Why it matters: Делает контекст-пакет не только parser contract, но и reusable knowledge asset.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:89`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:92`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:95`

### C06. Viability is high, but determinism and maintenance cost are principal risk factors

- Concept: Идея оценена высоко, но критические риски - канонизация NL в детерминированные действия, стоимость эволюции контекста, точность авто-сгенерированных логов.
- Why it matters: Определяет реальный engineering complexity beyond concept clarity.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:111`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:125`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:126`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:127`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:130`

### C07. NLU/dialog frameworks approximate the intent-to-action contract pattern

- Concept: Платформы типа Rasa/DeepPavlov показывают связку NL input -> structured intents/entities -> policy-driven action under domain contract.
- Why it matters: Дают зрелые референсы для части pipeline “interpretation and dialog state”.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:171`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:175`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:178`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:182`

### C08. Schema-first agent SDKs align with formal calls, guardrails, and typed validation

- Concept: OpenAI Agents SDK, Pydantic AI, Semantic Kernel реализуют tool-call schemas, guardrails, typed contracts и трассировку шагов.
- Why it matters: Это наиболее близкий путь к контролируемому NL->formal action execution.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:190`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:193`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:194`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:198`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:205`

### C09. NL-to-code execution frameworks demonstrate practical transparency pattern

- Concept: Подход “NL command -> generated executable code with user confirmation” показывает применимый механизм прозрачности и контроля на runtime.
- Why it matters: Закрывает operational side идеи, где formal action действительно исполняется.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:208`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:210`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:212`

### C10. Explicit context standards can externalize and version agent state/contracts

- Concept: Стандартный context JSON слой позволяет сделать контекст переносимым, версионируемым и пригодным для валидации/аудита.
- Why it matters: Даёт vendor-neutral способ управления контекстом как отдельным артефактом.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:214`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:216`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0005-CHATGPT.md:217`

## Unresolved Ambiguities

1. Не определён канонический formal target языка запроса (JSON DSL, function call schema, generated code, или гибрид).
2. Не зафиксирована политика обратной совместимости при смене версии context package.
3. Не решено, какой OSS-путь выбран как основной (dialog framework vs agent SDK vs custom compiler layer).
