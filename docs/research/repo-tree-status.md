# Repo Tree Status (Light Audit)

Date: 2026-02-25

## Why this file exists
This is a lightweight baseline for the upcoming deduplication pass. It captures current structure, duplicate pressure, and source quality markers.

## Scope snapshot

| Area | Count | Notes |
|---|---:|---|
| `raw-exports/**/*.md` | 45 | Exported chats and readmes |
| `raw-exports/sdlc-discovery-iteration-00/*.md` | 12 | ChatGPT iteration 00 |
| `raw-exports/sdlc-discovery-iteration-01/*.md` | 5 | Gemini iteration 01 |
| `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/*.md` | 28 | 27 chats + 1 README |
| `docs/**/*.md` | 13 | Curated docs/syntheses/research |
| `docs/research/artifacts/**/*` | 11 files | Canonical research artifacts (truth source) |

## Canonical truth zone
Current project rule: files under `docs/research/artifacts` are treated as truth source for standards/viewpoints.

Present files:
- `docs/research/artifacts/standards/CAN CSA ISO IEC IEEE 12207-18.pdf`
- `docs/research/artifacts/standards/AMS_Software_Lifecycle_GetLab.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/A3-2_IEEE-EIA-12207_Unit2_JamesWMoore.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/An_Overview_of_IEEE_Software_Engineering_Standards_Croll.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/BSI_ISO-IEC-IEEE_12207_2017_Preview_ANSI.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/GOST_R_ISO-IEC_12207_Meganorm_6430.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/IEEE 12207 Software Life Cycle - David F. Rico.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/IEEE-EIA_12207.2-1997_Implementation_Considerations.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/IEEE_Std_12207_ETS_MTL_Laporte.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/incose_rwg_gtwr_v4_summary_sheet.pdf`
- `docs/research/artifacts/ieee12207-viewpoints/international-standard-iso-iec-12207-software-life-cycle-2vke9fu8gz.pdf`

## Registry coverage
Active manual registry: `CHAT_REGISTRY.md`

- Included scopes:
  - `raw-exports/sdlc-discovery-iteration-01/*.md`
  - `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-*.md`
- Current rows: 32
  - `GEMINI`: 5
  - `CHATGPT`: 27
  - `deep_research` rows: 3

## Duplicate pressure (current)

### In selected registry scope (`iteration-01` + `all-chatgpt-work`)
10 rows are flagged as duplicate candidates (same normalized topic family):

- `ChatGPT-AI_агенты_и_управление_состоянием` family: 3
- `ChatGPT-Оценка_идеи_state_machine` family: 2
- `ChatGPT-Исследование_подходов_управления_состоянием` family: 3
- `ChatGPT-Альтернативы_Microsoft_Agent_Framework` family: 2

### Across all `raw-exports` folders
Highest-frequency normalized topics:

- `ChatGPT-Исследование_подходов_управления_состоянием`: 3
- `ChatGPT-AI_агенты_и_управление_состоянием`: 3
- `ChatGPT-Оценка_идеи_state_machine`: 2
- `ChatGPT-Альтернативы_Microsoft_Agent_Framework`: 2
- `README`: 2

## Source quality markers (`all-chatgpt-work`)
Top files by `[Unsupported Content]` markers:

| File | Unsupported | Plugin blocks |
|---|---:|---:|
| `ChatGPT-Branch_·_Исследование_подходов_управления_состоянием.md` | 90 | 1 |
| `ChatGPT-Исследование_подходов_управления_состоянием.md` | 68 | 1 |
| `ChatGPT-Альтернативы_Microsoft_Agent_Framework.md` | 56 | 1 |
| `ChatGPT-Branch_·_Альтернативы_Microsoft_Agent_Framework.md` | 44 | 0 |
| `ChatGPT-Многочасовые_сессии_Codex.md` | 8 | 0 |
| `ChatGPT-Исследование_гит-флоу_с_ИИ.md` | 5 | 0 |

Implication: dedup should preserve best-completeness variant and track loss risk where source quality is poor.

## Immediate dedup readiness notes

1. Normalize by topic family before merging:
   - strip suffix `(1)`
   - strip `Branch_·_`
   - strip `-deep-research-report[-xx]`
2. Keep one canonical row per topic family in future synthesis docs, but preserve all raw files for auditability.
3. Treat deep research files as supplementary evidence, not direct replacement for dialogue transcripts.
4. Keep `CHAT_REGISTRY.md` order stable; do not renumber existing IDs during dedup.
