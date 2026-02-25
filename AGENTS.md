# AGENTS.md

Instructions for agents working in this repository to verify, order, and process the SDLC knowledge corpus.

## Mission

Primary objective: keep repository knowledge legible, traceable, and dedup-ready while preserving raw evidence.

## Mandatory read order

1. `AGENTS.md` (this file)
2. `CHAT_REGISTRY.md` (manual ordering for SDLC iterations 01/02)
3. `CHAT_REGISTRY_ITERATION_00.md` (legacy prehistory registry)
4. `CHAT_DEDUP_REGISTRY.md` (exact-duplicate removals)
5. `docs/research/repo-tree-status.md` (latest tree audit snapshot)
6. `Harring.md` (selected harness engineering quotes)
7. `docs/README.md` and `docs/research/README.md`
8. Target chat file(s) referenced by the registries

## Source-of-truth hierarchy

1. `docs/research/artifacts/**/*` is treated as canonical truth for standards and viewpoints.
2. Curated docs in `docs/` are structured synthesis layers.
3. `raw-exports/` files are immutable evidence transcripts (content-level immutability).
4. `CHAT_REGISTRY.md` is the canonical processing order for SDLC discovery chats.

## Iteration model

- `raw-exports/sdlc-discovery-iteration-00`: pre-SDLC-automation history (data collection/discovery).
- `raw-exports/sdlc-discovery-iteration-01`: chats up to `CHAT-CHATGPT-0022` (inclusive).
- `raw-exports/sdlc-discovery-iteration-02`: chats from `CHAT-CHATGPT-0023` and later.

## Hard constraints

- Do not rewrite semantic content inside `raw-exports/` to "clean" it.
- File path/filename normalization inside `raw-exports/` is allowed only by ID policies below.
- Delete raw files only for exact SHA256 duplicates and only after recording the event in `CHAT_DEDUP_REGISTRY.md`.
- Do not renumber existing `chat_id` values in `CHAT_REGISTRY.md` (`0001..0032` are stable).
- Keep lineage explicit: every dedup or move must preserve provenance to prior path(s).

## ID policy

### Chat IDs
- Standard: `CHAT-<PROVIDER>-XXXX`
- Deep research variant: `CHAT-<PROVIDER>-DR-XXXX`
- Current providers: `CHATGPT`, `GEMINI`

### Legacy iteration-00 IDs
- Standard: `CHAT-CHATGPT-I00-XXXX`
- Managed in `CHAT_REGISTRY_ITERATION_00.md`

### Requirement IDs
- Canonical format in synthesis docs: `US-XXXX`, `UC-XXXX`, `NFR-XXXX`, `AT-XXXX`, `ADR-XXXX`
- If source transcript uses `US-###` style, keep source untouched and map via aliases in derived artifacts.

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
5. If duplicates are detected, mark related rows and record resolved exact dedup events in `CHAT_DEDUP_REGISTRY.md`.

## Scope currently tracked by CHAT_REGISTRY

- `raw-exports/sdlc-discovery-iteration-01/*.md`
- `raw-exports/sdlc-discovery-iteration-02/*.md`

## Quick checks before finalizing changes

Run from repository root:

- `rg -n "^\| [0-9]{4} \|" CHAT_REGISTRY.md | wc -l`
- `rg -n "CHAT-[A-Z0-9]+(-DR)?-[0-9]{4}" CHAT_REGISTRY.md`
- `rg -n "CHAT-CHATGPT-I00-[0-9]{4}" CHAT_REGISTRY_ITERATION_00.md`
- `find raw-exports/sdlc-discovery-iteration-01 raw-exports/sdlc-discovery-iteration-02 -maxdepth 1 -type f -name '*.md' | sed 's#.*/##' | rg -v '^CHAT-(CHATGPT|GEMINI)(-DR)?-[0-9]{4}\.md$'`
- `find raw-exports/sdlc-discovery-iteration-00 -maxdepth 1 -type f -name '*.md' | sed 's#.*/##' | rg -v '^(CHAT-CHATGPT-I00-[0-9]{4}\.md|README\.md)$'`

## Dedup preparation rule

Dedup decisions must be evidence-based:

- prefer best-completeness variant as canonical synthesis input;
- keep alternative variants as references in notes/registry;
- never lose provenance to raw source path and `chat_id`.

## Expected deliverables for each substantial pass

- updated `CHAT_REGISTRY.md` rows;
- updated `CHAT_REGISTRY_ITERATION_00.md` rows when legacy scope is touched;
- updated `CHAT_DEDUP_REGISTRY.md` when exact duplicates are removed;
- updated `docs/research/repo-tree-status.md` snapshot if tree reality changed;
- derived synthesis/traceability updates in `docs/`;
- explicit list of unresolved ambiguities.
