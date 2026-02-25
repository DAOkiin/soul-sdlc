# CHAT_DEDUP_REGISTRY.md

Registry of exact-duplicate removals in `raw-exports`.

- Rule: remove only exact SHA256 duplicates.
- Purpose: keep full provenance after physical deletion.

| dedup_id | sha256 | removed_original_path | removed_target_path | canonical_original_path | canonical_target_path | rule | notes |
|---|---|---|---|---|---|---|---|
| DEDUP-0001 | 6a7382bd5ec95432efcc6ac158ddf172be6235ca3fb98d60afaacd2928a727b3 | raw-exports/sdlc-discovery-iteration-00/ChatGPT-agents-state-management.md | raw-exports/sdlc-discovery-iteration-00/CHAT-CHATGPT-I00-0011.md | raw-exports/sdlc-discovery-iteration-all-chatgpt-work/ChatGPT-AI_агенты_и_управление_состоянием-deep-research-report-ru.md | raw-exports/sdlc-discovery-iteration-01/CHAT-CHATGPT-DR-0013.md | sha256-exact-match | canonical file kept because it already had stable `chat_id` in `CHAT_REGISTRY.md` |
