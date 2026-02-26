# Repo Tree Status (Post-Migration)

Date: 2026-02-26

## Why this file exists

Current lightweight snapshot after raw-export normalization, iteration split update, and full-pass distillation sync.

## Iteration progression

- Completed: `ITER-00`, `ITER-01`, `ITER-02`
- Current: `ITER-03` intent-context + primary distillation (`docs/research/distillation/*`)
- Canonical ledger: `docs/research/distillation/ITERATION_LEDGER.md`

## Scope snapshot

| Area                                           |    Count | Notes                                                                       |
|------------------------------------------------|---------:|-----------------------------------------------------------------------------|
| `raw-exports/**/*.md`                          |       44 | Canonical exported chats/readmes (evidence zone)                            |
| `raw-exports/sdlc-discovery-iteration-00/*.md` |       11 | 10 legacy chats (`I00`) + 1 README                                          |
| `raw-exports/sdlc-discovery-iteration-01/*.md` |       22 | IDs up to `I01-F0022-CHATGPT`                                               |
| `raw-exports/sdlc-discovery-iteration-02/*.md` |       10 | IDs from `I02-F0001-CHATGPT`                                                |
| `raw-exports/sdlc-discovery-iteration-03/*.md` |        1 | Canonical intake export: `I03-F0001-GEMINI-DR`                              |
| `docs/**/*.md`                                 |       74 | Curated docs/syntheses/research (includes generated distillation artifacts) |
| `docs/research/artifacts/**/*`                 | 11 files | Canonical research artifacts (truth source)                                 |

## Canonical truth zone

Files under `docs/research/artifacts` remain the truth source for standards/viewpoints.

## Registry coverage

- Main SDLC registry: `CHAT_REGISTRY.md`
   - Scope: `iteration-01` + `iteration-02` + `iteration-03`
   - Rows: 33
   - Providers: `GEMINI` 6, `CHATGPT` 27
   - Deep research rows: 4
- Legacy prehistory registry: `CHAT_REGISTRY_ITERATION_00.md`
   - Scope: `iteration-00`
   - Rows: 10
   - ID family: `I00-Fxxxx-CHATGPT`

## Iteration boundary rule

- `I01-F0022-CHATGPT` belongs to `iteration-01`.
- `I02-F0001-CHATGPT` is the first file of `iteration-02`.
- `I03-F0001-GEMINI-DR` is currently the first file of `iteration-03`.

## Derived working artifacts

- Mutable working brief moved from raw zone to `docs/research/distillation/workbench/iteration-03-codex-working-brief.md`.
- Canonical source linkage is documented in `docs/research/distillation/SOURCE_DERIVATION_MAP.md`.

## Dedup status

- Removed exact duplicate:
   - `raw-exports/sdlc-discovery-iteration-00/ChatGPT-agents-state-management.md`
- Kept canonical:
   - `raw-exports/sdlc-discovery-iteration-01/I01-F0013-CHATGPT-DR.md`
- Current exact hash duplicates in `raw-exports`: none.

## Source quality markers

Top files by `[Unsupported Content]` markers (after migration):

| File                                                               | Unsupported |
|--------------------------------------------------------------------|------------:|
| `raw-exports/sdlc-discovery-iteration-01/I01-F0018-CHATGPT.md`     |          90 |
| `raw-exports/sdlc-discovery-iteration-01/I01-F0019-CHATGPT.md`     |          68 |
| `raw-exports/sdlc-discovery-iteration-01/I01-F0022-CHATGPT.md`     |          56 |
| `raw-exports/sdlc-discovery-iteration-01/I01-F0021-CHATGPT.md`     |          44 |
| `raw-exports/sdlc-discovery-iteration-00/I00-F0009-CHATGPT.md` |          13 |
| `raw-exports/sdlc-discovery-iteration-02/I02-F0001-CHATGPT.md`     |           8 |

## Migration evidence

- Pre-migration inventory: `docs/research/raw-exports-migration-input.tsv`
- Deprecated aggregate folder removed.
