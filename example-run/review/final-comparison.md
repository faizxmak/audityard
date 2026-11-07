# Independent Review T3b — Case MERIDIAN-OCT2026 (rev 2, evidence v1)

Reviewer: audit-reviewer. Cutoff 7 Nov 2026 unchanged. `review_T3.md` (rev 1) is preserved unchanged; this file covers only what changed: manager rev 2 (C1–C6 applied) and the investigator comparison.
Inputs compared: `output/disposition_register.csv` (rev 2, with `exposure_bucket`), `final_report.md` (rev 2), `case/investigation/dispositions.json`, `calculation_results.json`, `findings.md` (read for bucket definitions). Facts re-checked against `agent-pack/` (no new evidence; evidence v1).

## 1. Result

**Supported.** Manager register, investigator dispositions and my own re-derivation agree on all 184 orders (class, evidence IDs, net settled cash, evidence references); the only class-label difference is WO-6776. Three differences are in how exposure is bucketed, not in what happened. Two small wording issues remain (Section 4); neither changes an amount or a conclusion.

## 2. Order-by-order comparison (184)

Programmatic comparison on work_order_id, class, net_settled_usd, evidence_ids:
- 183 of 184 identical. 169 supported compliance, 9 confirmed breach + WO-6776, 1 documentation defect (WO-5685), 1 conflicting (WO-7862), 3 unresolved (WO-1507, WO-7355, WO-8700) in both sets.
- Only difference: **WO-6776** — investigator "confirmed breach", manager "unrecorded October obligation". Amount (4,800 unpaid) identical in both.
- Cash: both sets give 186 settled events, gross 562,440, returns −3,300, net 559,140, fees 572,640, gap 13,500 (same four orders). Equals my T3 recomputation. Investigator's partition of net cash (513,640 supported + 25,700 control/at-risk + 3,400 recoverable + 16,400 unknown = 559,140) adds up and matches its own order lists; I re-added it.
- SLA, deposit and P1 limit figures in `calculation_results.json` (WO-5305 4.0h no credit; WO-2340 4.0167h, 400; WO-1104 excess 900; WO-6728 0; WO-1655 needs finance) match mine.

## 3. Manager's three reconciliation notes (report §8)

1. **WO-6776 an unrecorded October obligation, not a breach — SUPPORTED.** P9 makes accepted October work an October obligation regardless of invoice date; the complete October obligation register omits it (EV-899321) and the export (complete through cutoff) has no payment. No P2 payment-before-acceptance, delivery or approval rule is violated, so "confirmed breach" overstates. Presentation caution: START_HERE asks for five outcome classes (confirmed breach, supported compliance, unresolved, documentation defect, conflicting evidence). The manager's sixth label is accurate but non-standard; in the register's class column keep the descriptive label only if the report explains it maps to a P9 finding with $4,800 unpaid obligation. Either label leaves the amount unchanged.
2. **Control-breach payments not counted as at-risk — SUPPORTED for WO-1655 and WO-1085; NEEDS ADJUSTMENT for WO-6210.**
   - WO-1655 (P1, 8,000): work accepted 18 Oct (EV-616301), paid exactly the fee 19 Oct; the failure is missing finance approval (EV-203758). WO-1085 (P6, 3,800): accepted 13 Oct, paid the fee; waiver post-dates release (EV-320554). In both the cash went for accepted work; showing them as "paid under control breach, loss not shown" is a defensible exposure treatment, provided the 15,400 stays disclosed (it does, §2 table).
   - WO-6210 (P5, 3,600): the purpose of the callback control is to ensure funds reach the real vendor. A deliberate skip (EV-102596) means the 3,600 may have gone to an unverified account — a *potential* misdirection exposure that does not depend on the work being accepted. It is inconsistent to put the otherwise-comparable WO-1507 (3,500, callback unverifiable) in unknown exposure while WO-6210 sits in a bucket labelled "no loss shown". Recommend WO-6210 appear in "at risk (potential misdirected payment)" or have a note that vendor receipt is unconfirmed and the 3,600 is potentially exposed; the amount must still appear in exactly one bucket.
   - No double counting either way: each order sits in one bucket in both datasets.
3. **WO-7862 at risk — SUPPORTED (judgment call).** Customer's authenticated denial plus supplier insistence (EV-151122) means valid acceptance is neither established nor refuted; 4,300 was paid 23 Oct before the denial. Investigator's "unknown exposure" is equally defensible (it gives low confidence). The 4,300 is counted once in each set; both agree class = conflicting evidence. Keep Medium confidence and the stated limit: forgery is not concluded. The difference is definitional (positive contrary evidence ⇒ at risk; pure absence ⇒ unknown), and the manager's rule is applied consistently: WO-5169/WO-7862 at risk, WO-7355/WO-8700/WO-1507 unknown.

## 4. Further observations (non-blocking)

- **N1.** Investigator treats WO-1104's 900 and WO-1750's 4,500 as "at risk"; manager treats them as outstanding overpayment (900) and recoverable-on-customer-statements (4,500). Wording only. Note the 900 is an *advance payment above the permitted 30% deposit* (P3), within the total fee, so it is "excess advance, offset against the 5,400 balance" rather than an overpayment above fee under P8. Suggest relabelling in §2 ("excess advance payment" rather than "overpayment"). WO-2340's 400 is a credit due. WO-8572's 3,000 is a true P8 overpayment.
- **N2.** Report title line carries the whole status string "(FINAL (…reviewer comparison … pending confirmation))" and §8 still says comparison is pending. After this review, update to "comparison complete (review_T3b)". Only the manager should change its own file.
- **N3.** Investigator's `dispositions.json` has confidence "low" for WO-7862, WO-1507, WO-7355, WO-8700 where manager shows Medium/High (manager rates WO-7355 and WO-8700 confidence High). That is confidence in the *finding* (evidence gap exists) vs confidence in the *underlying fact*; recommend the register state which one it means, or use Medium for the gap items.
- Preserved from T3: no investigator/reviewer disagreement changes a disposition class except the WO-6776 label.

## 5. Coverage and unperformed checks

- Compared all 184 dispositions programmatically; read the 24 special-order explanations manually in both sets.
- Not performed: any source outside `agent-pack/`; authentication of documents; independent confirmation of release dates for P6 (bank settlement date used as proxy, stated in report per C5).
- No new evidence arrived; evidence v1 and the 7 Nov cutoff preserved. Historical rev 1 findings remain as filed in `review_T3.md`.

## 6. Status

**T3b: SUPPORTED** (reconciliation notes 1 and 3 supported; note 2 supported for WO-1655/WO-1085 with a WO-6210 adjustment recommended; WO-1104 wording and status-line cleanup suggested). No order rejected.
