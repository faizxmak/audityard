# Start an audit

The easiest route is `python3 scripts/prepare_case.py`, which prints this message with real paths. For manual setup, replace both path placeholders below. If you changed the template's team prefix, change the manager mention too.

```text
@audityard-manager Run case MERIDIAN-OCT2026. Audit October 2026 as of 7 November 2026 using only the four input files in <ABSOLUTE_AGENT_PACK_PATH>. Read START_HERE.md for the company policies, scope, and required outputs. Pass the same input and output paths to your team. Coordinate extraction, investigation, and independent review through this room. Do not read evaluation files, example outputs, or previous benchmark answers. Save final_report.md, disposition_register.csv, reconciliation.json, and the separate specialist artifacts under <ABSOLUTE_OUTPUT_PATH>. Complete the review before final delivery. Report any access or messaging blocker. Post a concise final summary with the exact output paths.
```
