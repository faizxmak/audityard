# Evaluation of the recorded run

The completed Switch run scored **91/100** under the supplied [rubric](rubric.md). Codex performed the assessment after the team finished, comparing the final report and register with the privately retained answer key and [control totals](control_totals.json). It combined file and arithmetic checks with judgment about conclusions and follow-up quality. It was not a third-party or human professional validation.

| Category | Awarded | Available |
|---|---|---|
| Challenge-case conclusions | 46 | 48 |
| Evidence discipline | 16 | 20 |
| Quantification | 15 | 15 |
| Coverage and traceability | 10 | 10 |
| Follow-up quality | 4 | 7 |
| Unsupported-allegation deduction | 0 | Up to −20 |
| **Total** | **91** | **100** |

The uncertainty gate passed. Twenty-two of 24 challenge cases earned full conclusion credit. WO-7355 and WO-8700 earned partial credit because uncertainty about actual completion needed to be stated more clearly. Follow-up requests for WO-5685 and treatment of conflicting evidence for WO-7862 also lost points. The [full assessment](assessment.md) explains each deduction.

## How to inspect the result

Read the public rubric summary and assessment alongside the saved report and register. The answer key and hidden evaluator notes are excluded from this repository, so a complete answer-key rescore requires access to the original evaluator packet. Equivalent wording is allowed, so the conclusion and follow-up scores involve judgment. The two helper scripts do not calculate that score.

Run `python3 scripts/verify_example.py` from the repository root to independently recompute cash controls and check register coverage and reference ownership. That check does not establish that a cited source supports a particular conclusion.

## Test boundaries

- The benchmark was supplied with the project materials. Its organizations, people, policies, and records are fictional.
- It contains 24 challenge cases and 160 ordinary orders with similar evidence patterns.
- The tested agents received only the four input files in a separate case directory. No evaluator-file access was found in the recorded tool calls.
- The evaluator files remained accessible under the same Mac account. This did not satisfy the rubric's filesystem-isolation requirement. The score is descriptive, not a claim of an isolated test.
- The reviewer inside Switch was a separate AI agent. The post-run assessment here was also AI-assisted.
- The source packet contains compact text extracts. It does not measure OCR, document authentication, or performance on real audits.
- There was one scored run. No repeated-run reliability, single-agent comparison, cost saving, or time-saving claim has been measured.

For another evaluation, give the audit team only `agent-pack/` and use a separate restricted account or environment that cannot read this directory or `example-run/`. The preparation script separates files but does not enforce access restrictions. Use a fresh, independently authored packet to test whether the workflow generalizes.
