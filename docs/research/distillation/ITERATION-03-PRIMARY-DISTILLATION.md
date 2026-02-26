# ITERATION-03 Primary Distillation

## Goal

Produce a first-pass distilled knowledge layer from all raw chat sources so the full context can be sliced and re-distilled pointwise.

## Input Set

- `CHAT_REGISTRY.md` (iteration 01/02 chat corpus)
- `CHAT_REGISTRY_ITERATION_00.md` (legacy prehistory corpus)
- `Harring.md` (harness engineering quote extraction)
- `CONCEPT_REGISTRY.md` (operational concept memory for Iteration-03)
- `FILE_CONCEPT_MAP.md` (persistent file↔concept index for Iteration-03)
- curated syntheses in `docs/syntheses/*`

## Core Outputs

- `PRIMARY_PASS_REGISTRY.md`: processing tracker for first-pass distillation by source ID.
- `primary-notes/<SOURCE_ID>.md`: first-pass distillation note per source.
- `CONCEPT_REGISTRY.md`: canonical concept registry with `concept_id` and first-seen evidence.
- `FILE_CONCEPT_MAP.md`: canonical file-level concept coverage index with context/evidence.
- `CONTEXT_SLICE_MAP.md`: mapping from distilled claims to reusable context slices.
- `TARGETED_REDISTILL_BACKLOG.md`: queue for second-pass pointwise distillation.

## ID Rules

- Source IDs are reused as-is (`Ixx-Fxxxx-PROVIDER` and `Ixx-Fxxxx-PROVIDER-DR`).
- Slice IDs use `SLICE-XXXX`.
- Distill tasks use `REDIST-XXXX`.

## Primary Distillation Template (per source)

1. `intent`: what problem/question this source is trying to solve.
2. `atomic_claims`: 5-20 concise claims with evidence line/path references.
3. `stable_knowledge`: claims likely to be re-used across iterations.
4. `volatile_knowledge`: claims that need periodic verification.
5. `artifacts_and_ids`: mentioned `US/UC/NFR/AT/ADR`, standards, files.
6. `quality_risks`: unsupported content, corruption, ambiguities.
7. `slice_candidates`: proposed `SLICE-XXXX` candidates.

## Workflow

1. Load `CONCEPT_REGISTRY.md` and `FILE_CONCEPT_MAP.md` before source processing.
2. Process sources in `PRIMARY_PASS_REGISTRY.md` order.
3. Create/update `primary-notes/<SOURCE_ID>.md` using the template.
4. Mark source status (`pending -> primary_done`).
5. Register new or updated concepts in `CONCEPT_REGISTRY.md` (with `first_seen` as `source_path:line` and lifecycle status).
6. Update file-level mapping in `FILE_CONCEPT_MAP.md` (concept IDs, context type, evidence refs, decision/proposal).
7. Aggregate repeated claims into `CONTEXT_SLICE_MAP.md`.
8. Create focused second-pass entries in `TARGETED_REDISTILL_BACKLOG.md`.

## Definition of Done for Iteration-03

- Every source row in `PRIMARY_PASS_REGISTRY.md` is at least `primary_done`.
- Every stable claim belongs to at least one explicit `SLICE-XXXX`.
- Every concept in `CONCEPT_REGISTRY.md` has at least one valid evidence anchor (`first_seen`).
- `FILE_CONCEPT_MAP.md` covers `docs/research/**/*` and `raw-exports/**/*`, excluding only explicit binary artifacts.
- `TARGETED_REDISTILL_BACKLOG.md` contains actionable, bounded tasks (source subset + expected artifact).
