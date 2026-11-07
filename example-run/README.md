# Original run artifacts

The four-agent team completed this Meridian Works audit in Mattermost's `#audit-yard` on 7 November 2026. These files preserve the original output contents, including the weaknesses described in the separate evaluation.

| File | Original artifact |
|---|---|
| [final_report.md](final_report.md) | Manager's final reviewed report |
| [disposition_register.csv](disposition_register.csv) | One disposition for each of the 184 work orders |
| [reconciliation.json](reconciliation.json) | Cash reconciliation and classification counts |
| [review/initial-review.md](review/initial-review.md) | Review T3, including corrections C1–C6 |
| [review/final-comparison.md](review/final-comparison.md) | Review T3b, including comparison with the investigation |

The reviewer files retain their original internal filenames and relative paths in the text. This is a curated snapshot, so some referenced intermediate extraction files and scripts are not included. The original manager scripts contained case-specific conclusions and machine-specific paths; they are not presented here as a reusable audit engine.

Review T3 initially checked the manager's draft while the investigator output was still pending. T3b subsequently compared the investigator, manager, and reviewer results. The final report applies presentation changes from both passes. A separate post-run assessment still identified shortcomings, detailed in [evaluation/assessment.md](../evaluation/assessment.md).

The run used `audit-manager`, `evidence-controller`, `reconciliation-investigator`, and `audit-reviewer`. The published template uses a configurable prefix, with `audityard-manager`, `audityard-evidence`, `audityard-investigator`, and `audityard-reviewer` as its defaults.
