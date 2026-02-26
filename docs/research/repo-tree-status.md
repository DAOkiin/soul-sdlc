# Repo Tree Status (Post-Reset)

Date: 2026-02-26

## Why this file exists

Current snapshot after full distillation reset and transition to incremental micro-pass mode.

## Iteration progression

- Completed: `ITER-00`, `ITER-01`, `ITER-02`
- Current: `ITER-03` (micro-pass mode)
- Canonical ledger: `docs/research/distillation/ITERATION_LEDGER.md`

## Scope snapshot

| Area                                           | Count | Notes                              |
|------------------------------------------------|------:|------------------------------------|
| `raw-exports/**/*.md`                          |    44 | Canonical evidence zone            |
| `raw-exports/sdlc-discovery-iteration-00/*.md` |    11 | 10 legacy chats (`I00`) + 1 README |
| `raw-exports/sdlc-discovery-iteration-01/*.md` |    22 | IDs up to `I01-F0022-CHATGPT`      |
| `raw-exports/sdlc-discovery-iteration-02/*.md` |    10 | IDs from `I02-F0001-CHATGPT`       |
| `raw-exports/sdlc-discovery-iteration-03/*.md` |     1 | `I03-F0001-GEMINI-DR`              |
| `docs/**/*.md`                                 |    58 | Curated docs                       |
| `docs/research/distillation/*.md`              |    45 | Minimal contract + 42 pass artifacts |
| `docs/research/artifacts/**/*`                 |    11 | Canonical research artifacts       |

## Reset outcome

- Deleted previous distillation artifacts (`concept/slice/redistill/request-history/primary-notes/workbench`).
- Removed derived file `Harring.md`.
- Recreated minimal distillation baseline:
   - `docs/research/distillation/ITERATION_LEDGER.md`
   - `docs/research/distillation/PRIMARY_PASS_REGISTRY.md`
   - `docs/research/distillation/WORKING_PROTOCOL.md`

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
