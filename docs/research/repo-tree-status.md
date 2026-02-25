# Repo Tree Status (Post-Migration)

Date: 2026-02-25

## Why this file exists
Current lightweight snapshot after raw-export normalization, iteration split update, and exact dedup pass.

## Iteration progression

- Completed: `ITER-00`, `ITER-01`, `ITER-02`
- Current: `ITER-03` primary distillation (`docs/research/distillation/*`)
- Canonical ledger: `docs/research/distillation/ITERATION_LEDGER.md`

## Scope snapshot

| Area | Count | Notes |
|---|---:|---|
| `raw-exports/**/*.md` | 43 | Exported chats and readmes after migration |
| `raw-exports/sdlc-discovery-iteration-00/*.md` | 11 | 10 legacy chats (`I00`) + 1 README |
| `raw-exports/sdlc-discovery-iteration-01/*.md` | 22 | IDs up to `CHAT-CHATGPT-0022` |
| `raw-exports/sdlc-discovery-iteration-02/*.md` | 10 | IDs from `CHAT-CHATGPT-0023` |
| `docs/**/*.md` | 19 | Curated docs/syntheses/research (includes distillation workspace) |
| `docs/research/artifacts/**/*` | 11 files | Canonical research artifacts (truth source) |

## Canonical truth zone
Files under `docs/research/artifacts` remain the truth source for standards/viewpoints.

## Registry coverage

- Main SDLC registry: `CHAT_REGISTRY.md`
  - Scope: `iteration-01` + `iteration-02`
  - Rows: 32
  - Providers: `GEMINI` 5, `CHATGPT` 27
  - Deep research rows: 3
- Legacy prehistory registry: `CHAT_REGISTRY_ITERATION_00.md`
  - Scope: `iteration-00`
  - Rows: 10
  - ID family: `CHAT-CHATGPT-I00-XXXX`
- Dedup registry: `CHAT_DEDUP_REGISTRY.md`
  - Exact removals recorded: 1

## Iteration boundary rule

- `CHAT-CHATGPT-0022` belongs to `iteration-01`.
- `CHAT-CHATGPT-0023` is the first file of `iteration-02`.

## Dedup status

- Removed exact duplicate:
  - `raw-exports/sdlc-discovery-iteration-00/ChatGPT-agents-state-management.md`
- Kept canonical:
  - `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-DR-0013.md`
- Current exact hash duplicates in `raw-exports`: none.

## Source quality markers
Top files by `[Unsupported Content]` markers (after migration):

| File | Unsupported |
|---|---:|
| `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-0018.md` | 90 |
| `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-0019.md` | 68 |
| `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-0022.md` | 56 |
| `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-0021.md` | 44 |
| `raw-exports/sdlc-discovery-iteration-02/CHAT-CHATGPT-0023.md` | 8 |
| `raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-0007.md` | 5 |

## Migration evidence

- Pre-migration inventory: `docs/research/raw-exports-migration-input.tsv`
- Deprecated aggregate folder removed.
