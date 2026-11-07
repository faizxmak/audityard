# Release verification

Checked on 7 November 2026 using Switch Console 0.40.1 and Switch Core 0.31.0 on macOS.

## Template checks

- Switch Core's installed template linter returned no errors or warnings.
- The four agent slots and room membership resolved correctly with both the default `audityard` prefix and an alternate prefix.
- The resolved room document parsed with its shared instructions and no machine-specific case paths.
- The running server accepted the template through its validation and import endpoints. Reading it back returned identical content.
- Switch Console displayed the four-agent preview and successfully created all four local Claude Code agents and the `audityard-audit` Mattermost room.

## Live handoff check

The new manager was asked to coordinate three small tasks against a fresh copy of the four inputs. It used addressed Switch messages, received specialist results, wrote `release-check.md`, and posted `TEMPLATE-CHECK-PASS`. The [original manager check result](template-smoke-test.md) is included.

| Specialist | Task | Reported result |
|---|---|---|
| `audityard-evidence` | Read and count work-order rows | 184 |
| `audityard-investigator` | Read and count raw payment rows | 188 |
| `audityard-reviewer` | Read the period and cutoff from START_HERE | October 2026, as of 7 November 2026 |

This verifies team creation, input access, and the three handoffs in this local setup. It is a smoke test, not a new audit or a guarantee of future completion.

## Submission checks

- The saved register covers all 184 source order IDs exactly once.
- Cited evidence and payment IDs belong to their stated orders.
- Recomputed cash controls match the supplied controls and the published reconciliation, including $559,140 net settled cash.
- Published input files, the three final deliverables, and both reviewer artifacts match their original contents.
- The preparation helper copies only the four inputs and creates an empty output directory.
- Local Markdown links resolve, both Python helpers parse, and the submission files pass a scan for common credential patterns and personal machine paths.

Run `python3 scripts/verify_example.py` to repeat the saved-example arithmetic and reference checks. It does not grade audit conclusions.

## Remaining limits

The revised template has not completed a newly scored full audit. The 91/100 score is attached only to the preserved original run. No benchmark with enforced filesystem isolation, repeated runs, or a single-agent baseline has been completed.
