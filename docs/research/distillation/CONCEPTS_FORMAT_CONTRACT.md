# CONCEPTS_FORMAT_CONTRACT.md

Canonical contract for `docs/research/distillation/*-concepts.md`.

## Status

- Version: `v2.2`
- Effective date: `2026-02-26`
- Scope: all current and future `*-concepts.md` files
- Migration note: existing legacy files can remain in prior format until dedicated migration pass

## Purpose

- Keep concept artifacts human-readable and machine-parseable.
- Preserve evidence traceability to raw exports.
- Separate concise summaries from evidence anchors.
- Standardize inputs for future aggregation (`Markdown+XML`) and parser code.

## Canonical section order

1. `# <CHAT_ID> Concepts (Draft)`
2. `## Source`
3. `## User Prompts Summary`
4. `## AI Response Summary`
5. `## Summary Evidence Map`
6. `## Extracted Concepts`
7. `## Unresolved Ambiguities`

## Prohibited top block

- Do not include the standalone top link block:
- `[Analyzed source: ...](...)`
- Source links must live only inside `## Source`.

## `## Source` schema (required keys)

- `chat_id`
- `source_path`
- `source_path_abs`
- `processed_on` (`YYYY-MM-DD`)
- `draft_status`

Rules:
- `chat_id` uses `Ixx-Fxxxx-PROVIDER` or `Ixx-Fxxxx-PROVIDER-DR`.
- `source_path` points to a raw export markdown file under `raw-exports/`.
- `source_path_abs` is an absolute filesystem path to the same source.
- All keys are mandatory and must appear in the order listed above.

## `## User Prompts Summary` schema

- Number of items: `1..7`.
- Each item must use typed and tagged format: `N. [type] [Uxx] text`.
- Allowed `type` values:
- `goal`
- `constraint`
- `request`
- `proposal`
- `decision`
- `risk`
- `next_step`

Item creation rule:
- Add a new item only when there is a semantic delta (for example: objective change, new constraint/preference, new explicit request/output format, proposal/decision change, new risk, or new next step).

ID rules:
- `Uxx` values are unique within the section.
- Recommended sequence is `U01..U0N`.

Rules:
- Do not include source anchors (`source_path:line`) in this section.
- Do not include Markdown links in this section.
- Keep each item concise and descriptive.

## `## AI Response Summary` schema

- Number of items: `1..7`.
- Each item must use typed and tagged format: `N. [type] [Axx] text`.
- Allowed `type` values:
- `goal`
- `constraint`
- `request`
- `proposal`
- `decision`
- `risk`
- `next_step`

Item creation rule:
- Add a new item only when there is a semantic delta (for example: response direction shift, proposal/structure change, explicit decision, newly surfaced risk, or next action update).

ID rules:
- `Axx` values are unique within the section.
- Recommended sequence is `A01..A0N`.

Rules:
- Do not include source anchors (`source_path:line`) in this section.
- Do not include Markdown links in this section.
- Keep each item concise and descriptive.

## `## Summary Evidence Map` schema

Purpose:
- Store source anchors for summary items without placing anchors inside summary text.

Line format:
- `- <item_id>: <anchor_1>, <anchor_2>, ...`

ID format:
- `Uxx` for `User Prompts Summary` items.
- `Axx` for `AI Response Summary` items.

Anchor format:
- ``raw-exports/.../<file>.md:<line>``

Rules:
- Every summary item ID must be present in `Summary Evidence Map`.
- IDs in map must refer to existing summary items.
- Each map entry must contain one or more anchors.

## `## Extracted Concepts` schema

For each concept block:
- Heading format: `### CNN. <Title>`
- Required fields:
- `Concept`
- `Why it matters`
- `Evidence`

Rules:
- `CNN` is zero-padded and sequential: `C01`, `C02`, ..., `CNN`.
- `Evidence` is a list of one or more anchors.
- Each evidence anchor format: ``raw-exports/.../<file>.md:<line>``.
- Evidence stays mandatory in concept files for traceability.

## `## Unresolved Ambiguities` schema

- Numbered list.
- Section must exist in every file.
- If there are no ambiguities, use a single item: `1. None identified.`

## Normalized parser-facing record (target interface)

```yaml
chat_id: string
iteration: string
source_path: string
processed_on: date
draft_status: string
user_summary:
  - id: string
    type: string
    text: string
ai_summary:
  - id: string
    type: string
    text: string
summary_evidence_map:
  Uxx:
    - string
  Axx:
    - string
concepts:
  - id: string
    title: string
    concept: string
    why_it_matters: string
    evidence:
      - string
unresolved_ambiguities:
  - string
```

Derivation rules:
- `iteration` is derived from `chat_id` prefix (example: `I02` from `I02-F0010-CHATGPT`).
- `concepts[].id` maps to `CNN`.
- `user_summary` and `ai_summary` lengths must be `1..7`.
- `user_summary[].type` and `ai_summary[].type` must be in the allowed enum.
- `summary_evidence_map` must be complete and consistent with summary IDs.

## Aggregated export policy (`Markdown+XML`, next iteration)

The aggregated output should include:
- document metadata
- summary items (without anchors in text)
- concepts with `concept` and `why_it_matters`
- unresolved ambiguities

The aggregated output may include:
- summary-level anchors via `summary_evidence_map` when requested by consumer

The aggregated output should exclude by default:
- concept-level `Evidence` payload (while evidence remains mandatory in source concept files)

## Allowed deviations

- `draft_status` value is free text.
- Summary text can use `N/A` when source dialog does not provide enough information.
- No other structural deviations are allowed.

## Acceptance criteria for this contract

- File exists at `docs/research/distillation/CONCEPTS_FORMAT_CONTRACT.md`.
- Contract includes formal structure (required sections, required fields, allowed deviations).
- Contract explicitly states:
- `Evidence` is required in concept files.
- Summary anchors are kept in `Summary Evidence Map`, not inside summary text.
- Concept `Evidence` may be omitted from default aggregated output.
