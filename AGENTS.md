# AGENTS.md

Instructions for agents working in this repository to verify, order, and process the SDLC knowledge corpus.

## Mission

Primary objective: keep repository knowledge legible, traceable, and dedup-ready while preserving raw evidence.

## Mandatory read order

1. `AGENTS.md` (this file)
2. `CHAT_REGISTRY.md` (manual ordering for SDLC iterations 01/02/03)
3. `CHAT_REGISTRY_ITERATION_00.md` (legacy prehistory registry)
4. `docs/research/repo-tree-status.md` (latest tree audit snapshot)
5. `docs/research/distillation/ITERATION_LEDGER.md` (iteration progression)
6. `docs/research/distillation/ITERATION-03-INTENT.md` (context anchor for current iteration intent)
7. `docs/research/distillation/ITERATION-03-PRIMARY-DISTILLATION.md` (current distillation runbook)
8. `docs/research/distillation/PRIMARY_PASS_REGISTRY.md` (primary-pass queue)
9. `Harring.md` (selected harness engineering quotes)
10. `docs/README.md` and `docs/research/README.md` (for artifact definitions and research scope)

## Source-of-truth hierarchy

1. `docs/research/artifacts/**/*` is treated as canonical truth for standards and viewpoints.
2. Curated docs in `docs/` are structured synthesis layers.
3. `raw-exports/` files are immutable evidence transcripts (content-level immutability).
4. `CHAT_REGISTRY.md` is the canonical processing order for SDLC discovery chats.

## Iteration model

- `raw-exports/sdlc-discovery-iteration-00`: pre-SDLC-automation history (data collection/discovery).
- `raw-exports/sdlc-discovery-iteration-01`: chats up to `CHAT-CHATGPT-0022` (inclusive).
- `raw-exports/sdlc-discovery-iteration-02`: chats from `CHAT-CHATGPT-0023` to `CHAT-CHATGPT-0032`.
- `raw-exports/sdlc-discovery-iteration-03`: chats from `CHAT-GEMINI-DR-0033` and later.
- `docs/research/distillation/*` (`ITER-03`): primary distillation of all sources, followed by slice-based targeted redistillation.

## Hard constraints

- Do not rewrite semantic content inside `raw-exports/` to "clean" it.
- File path/filename normalization inside `raw-exports/` is allowed only by ID policies below.
- Do not renumber existing `chat_id` values in `CHAT_REGISTRY.md` (`0001..0033` are stable).
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

## Iteration-03 distillation workflow

1. Read `docs/research/distillation/ITERATION-03-INTENT.md` as context anchor before taking tasks.
2. Take next `pending` row in `docs/research/distillation/PRIMARY_PASS_REGISTRY.md`.
3. Create/update `docs/research/distillation/primary-notes/<SOURCE_ID>.md`.
4. Extract atomic claims with explicit evidence references (`source_path:line`).
5. Propose/adjust slice placement in `docs/research/distillation/CONTEXT_SLICE_MAP.md`.
6. Add focused follow-up work into `docs/research/distillation/TARGETED_REDISTILL_BACKLOG.md`.

## Scope currently tracked by CHAT_REGISTRY

- `raw-exports/sdlc-discovery-iteration-01/*.md`
- `raw-exports/sdlc-discovery-iteration-02/*.md`
- `raw-exports/sdlc-discovery-iteration-03/*.md`

## Quick checks before finalizing changes

Run from repository root:

- `rg -n "^\| [0-9]{4} \|" CHAT_REGISTRY.md | wc -l`
- `rg -n "CHAT-[A-Z0-9]+(-DR)?-[0-9]{4}" CHAT_REGISTRY.md`
- `rg -n "CHAT-CHATGPT-I00-[0-9]{4}" CHAT_REGISTRY_ITERATION_00.md`
- `find raw-exports/sdlc-discovery-iteration-01 raw-exports/sdlc-discovery-iteration-02 -maxdepth 1 -type f -name '*.md' | sed 's#.*/##' | rg -v '^CHAT-(CHATGPT|GEMINI)(-DR)?-[0-9]{4}\.md$'`
- `find raw-exports/sdlc-discovery-iteration-03 -maxdepth 1 -type f -name '*.md' | sed 's#.*/##' | rg -v '^CHAT-(CHATGPT|GEMINI)(-DR)?-[0-9]{4}\.md$'`
- `find raw-exports/sdlc-discovery-iteration-00 -maxdepth 1 -type f -name '*.md' | sed 's#.*/##' | rg -v '^(CHAT-CHATGPT-I00-[0-9]{4}\.md|README\.md)$'`

## Dedup preparation rule

Dedup decisions must be evidence-based:

- prefer best-completeness variant as canonical synthesis input;
- keep alternative variants as references in notes/registry;
- never lose provenance to raw source path and `chat_id`.

## Expected deliverables for each substantial pass

- updated `CHAT_REGISTRY.md` rows;
- updated `CHAT_REGISTRY_ITERATION_00.md` rows when legacy scope is touched;
- updated `docs/research/repo-tree-status.md` snapshot if tree reality changed;
- derived synthesis/traceability updates in `docs/`;
- explicit list of unresolved ambiguities.
