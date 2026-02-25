# AGENTS.md

Instructions for agents working in this repository to verify, order, and process the SDLC knowledge corpus.

## Mission

Primary objective: keep repository knowledge legible, traceable, and dedup-ready while preserving raw evidence.

## Mandatory read order

1. `AGENTS.md` (this file)
2. `CHAT_REGISTRY.md` (manual ordering + processing state)
3. `docs/research/repo-tree-status.md` (latest tree audit snapshot)
4. `Harring.md` (selected harness engineering quotes)
5. `docs/README.md` and `docs/research/README.md`
6. Target chat file(s) referenced by `CHAT_REGISTRY.md`

## Source-of-truth hierarchy

1. `docs/research/artifacts/**/*` is treated as canonical truth for standards and viewpoints.
2. Curated docs in `docs/` are structured synthesis layers.
3. `raw-exports/` files are immutable evidence transcripts.
4. `CHAT_REGISTRY.md` is the canonical processing order for scoped chat exports.

## Hard constraints

- Do not rewrite semantic content inside `raw-exports/` to "clean" it.
- Do not delete source files during analysis/dedup planning.
- Do not renumber existing `chat_id` values in `CHAT_REGISTRY.md`.
- Any normalization happens in derived docs, not in raw exports.

## ID policy

### Chat IDs
- Standard: `CHAT-<PROVIDER>-XXXX`
- Deep research variant: `CHAT-<PROVIDER>-DR-XXXX`
- Current providers: `CHATGPT`, `GEMINI`

### Requirement IDs
- Canonical format in synthesis docs: `US-XXXX`, `UC-XXXX`, `NFR-XXXX`, `AT-XXXX`, `ADR-XXXX`
- If source transcript uses `US-###` style, keep source untouched and map it via aliases in derived artifacts.

## CHAT_REGISTRY contract

Table columns:
- `order`: manual canonical order.
- `chat_id`: stable identifier.
- `provider`: chat source provider.
- `kind`: `chat` or `deep_research`.
- `title`: source title from filename.
- `source_path`: relative path to file.
- `source_mtime`: recorded import timestamp.
- `status`: processing state.
- `linked_us`: linked requirement IDs when extracted.
- `notes`: anomalies, dedup hints, quality flags.

### Status values
- `raw`: not processed yet.
- `indexed`: indexed and classified.
- `parsed`: key entities extracted.
- `synthesized`: merged into structured docs.
- `verified`: links and evidence validated.

Allowed transition direction: `raw -> indexed -> parsed -> synthesized -> verified`.

## Processing workflow

1. Pick the earliest row by `order` with non-final status.
2. Read target source file from `source_path`.
3. Extract and record in derived docs:
   - core claims
   - referenced standards/artifacts
   - IDs (`US/UC/NFR/AT/ADR`) and missing-ID findings
   - quality notes (`Unsupported Content`, plugin insertions, corruption)
4. Update row `status`, `linked_us`, and `notes`.
5. If duplicates are detected, mark both rows with matching `duplicate-candidate: <topic-family>`.

## Scope currently tracked by CHAT_REGISTRY

- `raw-exports/sdlc-discovery-iteration-01/*.md`
- `raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-*.md`

## Quick checks before finalizing changes

Run from repository root:

- `rg -n "^\| [0-9]{4} \|" CHAT_REGISTRY.md | wc -l`
- `rg -n "CHAT-[A-Z0-9]+(-DR)?-[0-9]{4}" CHAT_REGISTRY.md`
- `rg -n "duplicate-candidate:" CHAT_REGISTRY.md`
- `rg -n "\[Unsupported Content\]" raw-exports/sdlc-discovery-iteration-all-chatgpt-work/*.md`

## Dedup preparation rule

Dedup decisions must be evidence-based:

- prefer best-completeness variant as canonical synthesis input;
- keep alternative variants as references in notes;
- never lose provenance to raw source path and `chat_id`.

## Expected deliverables for each substantial pass

- updated `CHAT_REGISTRY.md` rows;
- updated `docs/research/repo-tree-status.md` snapshot if tree reality changed;
- derived synthesis/traceability updates in `docs/`;
- explicit list of unresolved ambiguities.
