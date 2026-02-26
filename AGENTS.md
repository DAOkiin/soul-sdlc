# AGENTS.md

Instructions for agents working in this repository to verify, order, and process the SDLC knowledge corpus.

## Mission

Primary objective: keep repository knowledge legible and traceable while preserving raw evidence.

## Mandatory read order

1. `AGENTS.md` (this file)
2. `CHAT_REGISTRY.md` (manual order for SDLC iterations 01/02/03)
3. `CHAT_REGISTRY_ITERATION_00.md` (legacy prehistory registry)
4. `docs/research/repo-tree-status.md` (current tree snapshot)
5. `docs/research/distillation/ITERATION_LEDGER.md` (iteration progression)
6. `docs/research/distillation/PRIMARY_PASS_REGISTRY.md` (micro-pass queue)
7. `docs/research/distillation/WORKING_PROTOCOL.md` (operational micro rules)
8. `docs/research/distillation/CONCEPTS_FORMAT_CONTRACT.md` (canonical format for `*-concepts.md`)
9. `docs/README.md` and `docs/research/README.md` (artifact definitions and research scope)

## Source-of-truth hierarchy

1. `docs/research/artifacts/**/*` is treated as canonical truth for standards and viewpoints.
2. Curated docs in `docs/` are structured synthesis layers.
3. `raw-exports/` files are immutable evidence transcripts (content-level immutability).
4. `CHAT_REGISTRY.md` is the canonical processing order for SDLC discovery chats.

## Iteration model

- `raw-exports/sdlc-discovery-iteration-00`: pre-SDLC-automation history.
- `raw-exports/sdlc-discovery-iteration-01`: chats up to `I01-F0022-CHATGPT` (inclusive).
- `raw-exports/sdlc-discovery-iteration-02`: chats from `I02-F0001-CHATGPT` to `I02-F0010-CHATGPT`.
- `raw-exports/sdlc-discovery-iteration-03`: chats from `I03-F0001-GEMINI-DR` and later.
- `docs/research/distillation/*` (`ITER-03`): in micro-pass mode.

## Hard constraints

- Do not rewrite semantic content inside `raw-exports/`.
- File path/filename normalization inside `raw-exports/` is allowed only by ID policies below.
- Do not renumber existing `order` values in `CHAT_REGISTRY.md` (`0001..0033` are stable).
- Keep lineage explicit: every dedup or move must preserve provenance to prior path(s).

## ID policy

### Chat IDs

- Standard: `Ixx-Fxxxx-PROVIDER`
- Deep research variant: `Ixx-Fxxxx-PROVIDER-DR`
- Current providers: `CHATGPT`, `GEMINI`

### Legacy iteration-00 IDs

- Standard: `I00-Fxxxx-CHATGPT`
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
- `notes`: anomalies and quality flags.

### Status values

- `raw`: not processed yet.
- `indexed`: source reviewed and minimally classified.
- `parsed`: atomic claims extracted with evidence anchors.
- `synthesized`: merged into higher-level docs.
- `verified`: links and evidence validated.

Allowed transition direction: `raw -> indexed -> parsed -> synthesized -> verified`.

## Processing workflow (micro-pass)

1. Pick one source per step (`one source_id = one step`).
2. Use canonical row order from the relevant registry.
3. Read target source file from `source_path`.
4. Extract all important(don't extract all known concepts) atomic claims related to Software Development with explicit evidence refs (`source_path:line`).
5. Update only one row in `docs/research/distillation/PRIMARY_PASS_REGISTRY.md`.
6. Update source row status and keep notes concise.

## Scope currently tracked by CHAT_REGISTRY

- `raw-exports/sdlc-discovery-iteration-01/*.md`
- `raw-exports/sdlc-discovery-iteration-02/*.md`
- `raw-exports/sdlc-discovery-iteration-03/*.md`

## Quick checks before finalizing changes

Run from repository root:

- `find docs/research/distillation -type f | sort`
- `rg -n "^\| [0-9]{4} \|" CHAT_REGISTRY.md | wc -l`
- `rg -n "\| raw \|" CHAT_REGISTRY.md | wc -l`
- `rg -n "^\| [0-9]{4} \|" CHAT_REGISTRY_ITERATION_00.md | wc -l`
- `rg -n "\| raw \|" CHAT_REGISTRY_ITERATION_00.md | wc -l`
- `find raw-exports -type f -name '*.md' | wc -l`
- `python check_concepts_contract.py --root docs/research/distillation --mode strict`

## Expected deliverables for each substantial pass

- updated `CHAT_REGISTRY.md` rows;
- updated `CHAT_REGISTRY_ITERATION_00.md` rows when legacy scope is touched;
- one incremental update in `docs/research/distillation/PRIMARY_PASS_REGISTRY.md`;
- updated `docs/research/repo-tree-status.md` when tree reality changes;
- explicit list of unresolved ambiguities.
