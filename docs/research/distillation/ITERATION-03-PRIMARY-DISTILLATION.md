# ITERATION-03 Primary Distillation

## Goal
Produce a first-pass distilled knowledge layer from all raw chat sources so the full context can be sliced and re-distilled pointwise.

## Input Set
- `CHAT_REGISTRY.md` (iteration 01/02 chat corpus)
- `CHAT_REGISTRY_ITERATION_00.md` (legacy prehistory corpus)
- `Harring.md` (harness engineering quote extraction)
- curated syntheses in `docs/syntheses/*`

## Core Outputs
- `PRIMARY_PASS_REGISTRY.md`: processing tracker for first-pass distillation by source ID.
- `primary-notes/<SOURCE_ID>.md`: first-pass distillation note per source.
- `CONTEXT_SLICE_MAP.md`: mapping from distilled claims to reusable context slices.
- `TARGETED_REDISTILL_BACKLOG.md`: queue for second-pass pointwise distillation.

## ID Rules
- Source IDs are reused as-is (`CHAT-*` and `CHAT-CHATGPT-I00-*`).
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
1. Process sources in `PRIMARY_PASS_REGISTRY.md` order.
2. Create/update `primary-notes/<SOURCE_ID>.md` using the template.
3. Mark source status (`pending -> primary_done`).
4. Aggregate repeated claims into `CONTEXT_SLICE_MAP.md`.
5. Create focused second-pass entries in `TARGETED_REDISTILL_BACKLOG.md`.

## Definition of Done for Iteration-03
- Every source row in `PRIMARY_PASS_REGISTRY.md` is at least `primary_done`.
- Every stable claim belongs to at least one explicit `SLICE-XXXX`.
- `TARGETED_REDISTILL_BACKLOG.md` contains actionable, bounded tasks (source subset + expected artifact).
