# WORKING_PROTOCOL.md

Operational protocol for reset-mode distillation.

1. One step equals one `source_id`.
2. Record only quotable facts with explicit anchors: `source_path:line`.
3. Extract only 3-7 atomic claims per step.
4. After each step, update exactly one row in `PRIMARY_PASS_REGISTRY.md`.
5. Do not create global taxonomies (concept maps, slice maps, ontologies) before 5-10 processed sources.
6. Keep raw sources immutable: never rewrite semantic content in `raw-exports/`.
