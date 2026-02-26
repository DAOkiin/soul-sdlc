# I00-F0010-CHATGPT Concepts (Draft)

[Analyzed source: I00-F0010-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md)

## Source

- chat_id: `I00-F0010-CHATGPT`
- source_path: [raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md](/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md)
- source_path_abs: `/Users/daokiin/projects/daokiin/soul/sdlc/raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md`
- processed_on: `2026-02-26`
- draft_status: `awaiting_user_alignment`

## User Prompts Summary

1. Пользователь попросил найти существующие англоязычные категоризации веб-страниц (таксономии/онтологии/иерархии) для хранения категории страницы в БД, с примерами product page, media article, tweet/post, homepage/store pages (`raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:4`).
2. Пользователь попросил продолжить исследование и найти дополнительные релевантные материалы (`raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:85`).

## AI Response Summary

1. Агент предложил практическое ядро через Schema.org page/entity typing и отделил page-type от topic taxonomies (`C01`-`C04`).
2. Агент расширил обзор академическими web-genre корпусами и register-schemes (KI-04, 7-Web, 20-Genre, CORE, FGC) с разной гранулярностью (`C05`-`C08`).
3. Агент свёл это в многослойную модель хранения (page role + content/genre + optional topic) и отметил необходимость multi-label/гибридной обработки (`C09`, `C10`).

## Extracted Concepts

### C01. Page-type classification should be separated from topic classification

- Concept: Категория “что это за страница” (functional/page role) не эквивалентна категории “о чём контент”; это отдельные классификационные оси.
- Why it matters: Предотвращает смешение сигналов и улучшает устойчивость схемы данных.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:8`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:35`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:47`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:50`

### C02. Schema.org is positioned as the primary practical ontology for page-role typing

- Concept: Schema.org `WebPage` subtypes (`ItemPage`, `CollectionPage`, `ProfilePage`, `SearchResultsPage`, `FAQPage` etc.) выступают готовым словарём для page-type.
- Why it matters: Даёт стандартную и массово распространённую основу классификации при парсинге веба.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:10`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:15`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:17`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:22`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:23`

### C03. Main-entity typing is a second core axis for page semantics

- Concept: Поверх page role отдельно фиксируется тип главной сущности страницы (`Product`, `Article`, `SocialMediaPosting`, `Organization` и т.д.).
- Why it matters: Уточняет meaning страницы и улучшает downstream use-cases (поиск, аналитика, routing).
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:25`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:29`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:31`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:73`

### C04. Topic taxonomies (IAB/IPTC) should be optional complementary layer, not replacement of page type

- Concept: IAB Content Taxonomy и IPTC Media Topics полезны как тематическая ось, но не заменяют функциональный тип страницы.
- Why it matters: Позволяет строить composable schema: page role + entity + topic.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:47`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:50`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:54`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:57`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:75`

### C05. Web-genre research provides reusable taxonomies and labeled corpora for model training

- Concept: Линия genre-based classification предлагает устойчивые схемы ярлыков и датасеты для автоматической классификации типов веб-страниц.
- Why it matters: Даёт evidence-based базу для выбора taxonomy и обучения классификатора.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:37`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:39`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:97`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:100`

### C06. KI-04 and Santinis corpora are pragmatic mid-size label sets close to real web page classes

- Concept: KI-04 (8 жанров) и 7-Web Genre Collection дают прикладные категории, близкие к operational веб-типам (shop, article, discussion, FAQ/search/list/personal pages).
- Why it matters: Удобны как стартовый label inventory для production taxonomy.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:106`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:108`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:112`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:119`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:137`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:138`

### C07. Richer taxonomies (20-Genre, CORE) improve coverage but increase complexity and may require multi-label modeling

- Concept: Более широкие жанровые схемы захватывают сложные и технические классы (включая multi-label страницы), но требуют более сложной модели классификации.
- Why it matters: Влияет на компромисс “точность/покрытие” vs “простота внедрения”.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:144`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:146`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:149`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:153`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:157`

### C08. Coarse macro-genre schemes are valid when stability and low cardinality are prioritized

- Concept: Functional Genre Classification (7 macro-genres) предлагает сжатую и стабильную схему категорий для систем, где важно ограничить число классов.
- Why it matters: Помогает проектировать low-maintenance taxonomy для БД и аналитики.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:166`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:169`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:171`

### C09. Structured metadata extraction (Schema.org/OpenGraph) can bootstrap or replace parts of ML classification

- Concept: Типы страниц и контента часто можно извлекать из встроенной разметки (`schema.org`, `og:type`) до запуска более тяжёлой ML-классификации.
- Why it matters: Повышает точность на размеченных сайтах и снижает стоимость inference.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:181`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:183`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:185`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:189`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:204`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:206`

### C10. Production-grade web page typing should be multi-layer and multi-label aware

- Concept: Практическая схема для интернет-парсинга должна учитывать гибридность страниц и поддерживать многослойное представление (page role + content/genre + optional topic), потенциально с multi-label.
- Why it matters: Делает taxonomy устойчивой к смешанным шаблонам и эволюции веба.
- Evidence:
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:225`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:227`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:231`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:234`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:240`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:242`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:245`
  - `raw-exports/sdlc-discovery-iteration-00/I00-F0010-CHATGPT.md:250`

## Unresolved Ambiguities

1. Не выбран целевой уровень гранулярности taxonomy (compact 7-15 классов vs expanded multi-label схема на 20+ классов).
2. Не определён приоритет домена (универсальный веб vs e-commerce/content/social-first), от которого зависит базовый словарь категорий.
3. Не зафиксирована стратегия слияния metadata-first и ML-classification (fallback-правила, confidence thresholds, conflict resolution).
