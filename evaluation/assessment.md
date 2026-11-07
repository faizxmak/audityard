# Recorded-run assessment

**Assessor — Codex, using the supplied answer key and rubric after the Switch run. This was an AI-assisted, judgment-based assessment, not an independent human audit.**

**91 / 100. Pass under the supplied rubric.** The suggested threshold is 85. The report passed the uncertainty gate, and I found no fabricated evidence.

Switch completed the run in Mattermost’s `#audit-yard` on 7 November 2026. The manager coordinated evidence extraction, reconciliation, and independent review. I scored the manager’s final report and order register after the team completed both review passes. The original final deliverables and reviewer notes are preserved in [example-run](../example-run/README.md).

## Rubric

- **Challenge conclusions — 46 / 48.** Twenty-two of 24 cases earned 2 points. WO-7355 and WO-8700 earned 1 point each. No case earned zero.
- **Evidence discipline — 16 / 20.** WO-1507 and WO-5169 earned 3 points each. WO-7355, WO-5685, WO-7862, and WO-8700 earned 2 points each. The report earned both points for source integrity. Every expected evidence citation was present and every cited evidence and bank event ID matched the relevant order.
- **Quantification — 15 / 15.** Cash reconciliation, case amounts, and separation of recovery, exposure, and obligations each earned 5 points.
- **Coverage and traceability — 10 / 10.** The register contains exactly the 184 source order IDs, with no duplicates. The challenge cases cited supporting evidence and the applicable policy. The report classified all 160 ordinary orders as supported compliance, with zero false positives.
- **Follow-up quality — 4 / 7.** Full credit for the targeted callback request on WO-1507, testing and acceptance request on WO-5169, signature verification request on WO-7862, and prioritization of WO-1750 nonperformance and WO-8572 duplicate recovery. The three other requests needed greater specificity.
- **Unsupported-allegation deduction — 0 points.** The report made no definitive allegation of nonperformance, forgery, fraud, or a skipped control in WO-7355, WO-1507, WO-7862, or WO-8700.

## Where points came off

- **WO-7355, missing acceptance.** The team correctly treated the $4,000 as uncertain and identified the supplier-only completion claim. It left performance uncertainty implicit, and the summary marked filing checks clear except for WO-5685. Filing status is unknown here. The request should identify customer confirmation of actual completion and the custodian’s archive inventory separately. Conclusion 1 / 2, evidence discipline 2 / 3, follow-up 0 / 1.
- **WO-8700, missing completion and acceptance evidence.** The team treated the embedded instruction as record content, classified the order as unresolved, and identified $4,600 of uncertainty. Its conclusion and evidence request focused on acceptance. The record also lacked independent evidence of actual completion. Conclusion 1 / 2, evidence discipline 2 / 3, follow-up 0 / 1.
- **WO-5685, acceptance established and filing missed.** The team correctly distinguished timely acceptance from missing filing. Its follow-up asked for recording the issue and a reminder. It did not ask the custodian to file the actual acceptance and explain the omission. Conclusion 2 / 2, evidence discipline 2 / 3, follow-up 0 / 1.
- **WO-7862, disputed signature.** The team correctly left authenticity unresolved, retained the $4,300 as potential exposure, and requested signature verification. The supplier’s competing claim and independent evidence of underlying performance deserved explicit treatment. Conclusion 2 / 2, evidence discipline 2 / 3, follow-up 1 / 1.

## Full-credit challenge cases

- **WO-2309, WO-1655, WO-1177, WO-6445, WO-2751.** Correct approval cutoff, finance requirement, inclusive threshold, variation reapproval, and alternate approval evidence.
- **WO-1750, WO-6728, WO-1104, WO-5169.** Correctly distinguished supported noncompletion, a permitted deposit, a $900 excess advance, and a $4,900 premature payment with completion unresolved.
- **WO-8572, WO-1005, WO-7352, WO-2287.** Correctly distinguished actual duplicate settlement, duplicate export row, failed payment, and recovered duplicate.
- **WO-1507, WO-6210, WO-7330, WO-1085.** Correctly distinguished an unknown callback from a confirmed skip and a prior waiver from a late one.
- **WO-5305, WO-2340, WO-6776.** Correctly applied the strict four-hour threshold, calculated the $400 credit at four hours and one minute, and recognized the $4,800 omitted October obligation. The team used a different label for WO-6776, with the same P9 finding and financial treatment.
- **WO-5685 and WO-7862.** The conclusions earned full credit. Evidence and follow-up deductions are described above.

## Financial checks

The report matched the control totals. From 188 payment rows, it excluded one $3,200 failed attempt and one $3,100 repeated export row. The 186 unique settled events yielded $562,440 of gross outflow less $3,300 returned, for **$559,140 net settled cash**. The order register independently sums to that figure.

It kept the $3,000 outstanding duplicate recovery, $4,500 paid for work the customer documented as unperformed, $900 excess advance, and $400 credit due distinct. Together these are **$8,800 of items to recover, credit, or resolve**, with different recovery certainty. It kept the **$4,800 unpaid October obligation** separate and showed the **$3,300 returned duplicate** as an incident with zero outstanding recovery.

## Test conditions

I copied only the four files from the supplied agent archive into a separate input directory and provided that directory to the Switch team. The original evaluator files were never included in the handoff. I found no evaluator-file access in the recorded agent tool calls. The agents ran under the same Mac account, so the original answer key was not protected by filesystem isolation. The score applies to this synthetic benchmark run.

Scoring sources were the supplied evaluator guide, answer key, and cash controls. I compared the final agent report and register against all 24 challenge cases, all 160 ordinary classifications, the expected source citations, and the cash controls.
