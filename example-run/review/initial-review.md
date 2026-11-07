# Independent Review T3 — Case MERIDIAN-OCT2026 (rev 1, evidence v1)

Reviewer: audit-reviewer. Cutoff 7 Nov 2026. Closed-world: only `agent-pack/` (START_HERE.md, work_orders.jsonl, evidence.jsonl, payments.jsonl) was used as audit material; the manager draft was read for comparison only.
Reviewed: `output/disposition_register.csv/.json`, `reconciliation.json`, `scripts/build_manager_register.py`, `final_report.md` (draft). Not reviewed: `output/case/investigation/` (empty at review time) — comparison **not performed**, see Section 6.
Re-derivation: `review/scripts/reviewer_rederive.py` → `reviewer_reconciliation.json`, `reviewer_standard_160.csv`. Original files not modified.

## 1. Overall result

All 24 special-order conclusions and the 160 standard-order conclusions are **supported** on the evidence. Reconciliation figures are reproduced exactly. No finding is rejected. There are **no conclusion-changing corrections**; there are 6 wording/presentation corrections (Section 5) and 3 qualifications on confidence/classification.

## 2. Reconciliation (independently recomputed)

- 188 rows: 1 failed excluded (BANK-WO-7352-0, 3,200, 14 Oct); 1 repeated export row excluded (second BANK-REPEAT-091, 3,100) → **186 settled events**.
- Gross settled **562,440**; returns **-3,300** (BANK-WO-2287-2, 3 Nov); net **559,140**. Fees **572,640**. Gap **13,500** ✔ (matches manager).
- Gap by order (net − fee): WO-1104 −5,400; WO-6728 −6,300; WO-6776 −4,800; WO-8572 +3,000 → −13,500 ✔. Every other order nets exactly to its fee (incl. WO-2287: 3,300+3,300−3,300; WO-1005 after de-dup; WO-7352 after excluding failed).
- BANK-REPEAT-091 rows are byte-identical (same order, amount, date); EV-306850 says bank shows one settlement. Treating as one is supported by START_HERE ("repeated event IDs represent repeated export rows").
- No double counting: each exposure is attributed to a single order and a single bucket (checked, Section 4). Caveat: the `amount_flagged_usd` column mixes buckets (sums to 34,700, which is not a meaningful figure) — see correction C4.

## 3. Standard orders (160) — SUPPORTED

For every one of the 160 (list in `reviewer_standard_160.csv`): start 20 Oct, fee ≤ 5,000 (so within the 15-Oct-onward manager limit; baseline approval 19 Oct), evidence = signed acceptance archived 23 Oct with fee confirmed equal to the register fee, exactly one settled payment equal to the fee dated on or after the 23 Oct acceptance (checked per order in the script), deadline 31 Oct. No P1/P2/P3/P8 exception. Baseline assumptions (P4 timely filing, P5 unchanged account, P6 separate people, no deposit/SLA) apply and are not contradicted by any record. Limit of this conclusion: baseline records are assumed per START_HERE, not independently seen; the 160 acceptance items are text records, not authenticated documents.

## 4. Special orders (24) — verdicts

Verdict key: S = supported, R = rejected, N = needs-more-evidence (about the manager's conclusion, not about the underlying activity).

| WO | Manager class | Verdict | Basis (source) |
|---|---|---|---|
| WO-1177 | Supported compliance P1 | **S** | Fee 5,000, start 20 Oct → limit 5,000 "up to and including"; baseline manager approval suffices. Accepted 22 Oct (EV-224326); paid 5,000 on 23 Oct. |
| WO-1655 | Confirmed breach P1 | **S** | Start 16 Oct ≥ 15 Oct → 5,000 limit; fee 8,000 needs finance. EV-203758 (complete register + archive, finance confirms none). Acceptance 18 Oct (EV-616301) precedes payment 19 Oct. Breach is approval-only. |
| WO-6445 | Supported P1 | **S** | Start 20 Oct; original 4,500 ≤ 5,000; variation to 7,000 signed 21 Oct with finance authenticated email before added work began (EV-799581) — satisfies "reapproved if fee increases above limit". Accepted 24 Oct, paid 7,000 on 25 Oct. |
| WO-5305 | Supported P7 | **S** | Opened 20 Oct 20:00 UTC. Restored 21 Oct 05:30 Colombo = 21 Oct 00:00 UTC. Duration exactly 4h00 → not "strictly exceeds 4 hours" → no credit (EV-932288). |
| WO-2340 | Confirmed breach P7 | **S** | Restored 05:31 Colombo = 00:01 UTC → 4h01 > 4h → 10% × 4,000 = **400** credit. Complete credit register has none (EV-280659); 4,000 paid in full 23 Oct. Reported as an unapplied credit (not an overpayment above fee) — acceptable. |
| WO-1104 | Confirmed breach P3 | **S** | 30% × 9,000 = 2,700 permitted; paid 3,600 on 11 Oct → excess **900** (EV-551396). Start 10 Oct, 9,000 ≤ 10,000 limit. Balance 5,400 not due until 20 Nov. |
| WO-6728 | Supported P3 | **S** | Paid 2,700 = 30% exactly (EV-311661); no excess; balance 6,300 not yet due, no acceptance yet required. |
| WO-5685 | Documentation defect P4 | **S** | Authenticated customer email 14 Oct is valid acceptance (P2; EV-561541). Complete archive inventory through cutoff has no upload; email first given to audit 6 Nov (EV-484022) → P4 missing/late filing (> 5 days after 14 Oct). Payment 16 Oct after acceptance. Defect only; no payment exposure. |
| WO-2751 | Supported P1/P4 | **S** | Portal blank is a migration artefact; archived authenticated manager email 19 Oct approves 4,400, before 20 Oct start; uploaded 19 Oct (EV-157830) → within 5 days. Fee ≤ 5,000. Accepted 23 Oct, paid 24 Oct. Reasonable to log portal gap as an observation only. |
| WO-5169 | Confirmed breach P2 | **S** | Customer confirms acceptance pending/testing unfinished at cutoff (EV-875864) = positive evidence acceptance did not occur; payment 2 Nov. P9 correctly **not** concluded: deadline passed, but noncompletion not established (supplier says complete). |
| WO-7862 | Conflicting evidence | **S** | Signed PDF vs customer authenticated denial and no verification (EV-151122). Neither forgery nor valid acceptance established; payment 23 Oct preceded denial. Medium confidence appropriate. |
| WO-1750 | Confirmed breach P2/P9 | **S, with qualification** | Supplier completion report (EV-292990) is an assertion only; customer inspection 15 Oct and 7 Nov reconfirmation say work unstarted (EV-259901). No acceptance on file and positive evidence of failure → P2 breach (payment 16 Oct). Deadline 31 Oct passed → P9 delivery breach supported by customer statements. But this is a customer assertion vs supplier assertion with no independent site record; see C2. |
| WO-8572 | Confirmed breach P8 | **S** | Two distinct settled transfers (3,000 on 14 and 15 Oct), no return (EV-629643). Settled 6,000 vs fee 3,000 → recovery outstanding **3,000**. |
| WO-2287 | Confirmed breach P8 | **S** | 3,300 ×2 (14, 15 Oct) − 3,300 returned 3 Nov (EV-882881). Incident stands; outstanding recovery 0 (P8: return reduces recovery, does not erase incident). |
| WO-1005 | Supported P8 | **S** | Repeated export row only; one settlement (EV-306850). |
| WO-7352 | Supported P8 | **S** | Failed attempt (no debit) excluded; one settled 3,200 on 15 Oct (EV-589328). |
| WO-7330 | Supported P6 | **S** | Same person E17, but finance waiver dated 10 Oct for this exact order precedes release (bank date 14 Oct) (EV-827885). |
| WO-1085 | Confirmed breach P6 | **S** | Waiver dated 16 Oct is after release (bank date 14 Oct; release cannot be later than settlement), and finance says it is the first waiver (EV-320554). Exception not authorized. Release date is inferred from bank settlement date — see C5. |
| WO-6210 | Confirmed breach P5 | **S** | Account changed 12 Oct; signed interview admits callback deliberately skipped (EV-102596); first/only payment 14 Oct to new account. Loss not established — treatment correct. |
| WO-1507 | Unresolved P5 | **S** | Callback field blank, retention expired, notebook not supplied (EV-726868). Blank ≠ proof not done. Correctly unresolved; exposure unknown (3,500 paid 14 Oct). |
| WO-2309 | Supported P1/P2 | **S** | Start 10 Oct → 10,000 limit; fee 8,000 within manager authority. Acceptance 12 Oct (EV-967526); paid 13 Oct. |
| WO-7355 | Unresolved P2 | **S** | Supplier-only completion; acceptance absent from selective export; customer has not replied (EV-460277). Evidence gap, not a breach. |
| WO-8700 | Unresolved P2 | **S** | Supplier completion assertion only; acceptance not in selective collection (EV-536214). The supplier's note asking for a compliant report carries no evidential weight and was not followed; the order stays unresolved. |
| WO-6776 | Confirmed breach P9 | **S, relabel** | Accepted 31 Oct; invoice 4 Nov; complete October obligation register excludes it (EV-899321); no payment row (export complete) → 4,800 unrecorded October obligation. P9 applies; this is a recognition/cutoff finding, not a delivery breach — see C3. |

Rejected: none. Needs-more-evidence on the manager's conclusion: none (open questions below are evidence requests on the underlying facts, which the manager already lists).

## 5. Corrections / qualifications to return to audit-manager

- **C1 (wording, report §1/§2).** "Confirmed recoverable, outstanding: $8,800" includes WO-1750's 4,500, whose basis is customer statements only (Medium-High in the register). Suggest "Recoverable, outstanding: 8,800 (of which 4,300 established by bank/contract records — WO-8572 3,000, WO-1104 900, WO-2340 400 as unapplied credit — and 4,500 dependent on customer statements, WO-1750)". Note WO-2340's 400 is a credit due, not cash overpaid.
- **C2 (WO-1750 classification).** Support "Confirmed breach" for P2; state P9 as supported by customer statements with the supplier's completion report as the conflicting assertion, keep Medium-High, and make the independent site record the top evidence request. Do not describe the 4,500 as a loss.
- **C3 (WO-6776 label).** Change "Confirmed breach" to "Confirmed finding — unrecorded October obligation (P9)". The 4,800 is an unpaid obligation, not at-risk cash.
- **C4 (register structure).** `amount_flagged_usd` combines recoverable, at-risk and unpaid amounts and the incident-only WO-2287 3,300. Add a typed bucket column (recoverable / at-risk / unpaid / unknown / incident-no-balance / control-breach-paid) so no consumer can sum the column. The report's §2 table already separates them correctly (no double counting there).
- **C5 (WO-1085/WO-7330).** State that "release date" is taken from bank settlement date (14 Oct) because no release record exists; the conclusion holds for any release date on or before settlement. No supplier release log was provided.
- **C6 (bucket consistency).** WO-7355 and WO-8700 (no acceptance evidence in a selective collection) are reported as "at risk" together with WO-5169 and WO-7862, where there is positive evidence against acceptance or a dispute. Consider presenting 5169+7862 (9,200) as "at risk — contrary or disputed evidence" and 7355+8700 (8,600) as "unknown exposure — evidence gap", keeping total 17,800 and the explicit statement that missing evidence does not show non-acceptance. Not wrong as drafted; it is a clarity issue given START_HERE asks for "unknown exposure" to be separated.
- WO-1655 (8,000), WO-1085 (3,800), WO-6210 (3,600) are correctly shown as paid-under-control-breach, not as loss (total 15,400 ✔). WO-1507's 3,500 is correctly unknown exposure.

## 6. Coverage, limits, and unperformed checks

- **Investigator comparison not done**: `output/case/investigation/` was empty. Re-review when it lands; compare per-order class, SLA/deposit figures, bucket totals.
- **P4 for approvals/acceptances of the 160 and for the WO-6445 variation approval**: filing timeliness rests on the START_HERE baseline assumption and absence of a contrary record; no filing dates exist in the pack to test.
- **Authentication of documents**: none of the evidence was independently authenticated; conclusions rely on the stated qualities in START_HERE ("supplied approvals authenticated", etc.).
- **Release date for P6** (C5) and **timezone of date-only fields**: register and evidence dates are date-only; no conclusion here depends on a boundary of < 1 day except the two SLA items, which are explicitly timestamped.
- **Selective collection**: for WO-7355, WO-8700, WO-1507, WO-5169, WO-7862 the evidence cannot establish whether acceptance/callback/completion occurred; the manager's wording is consistent with that.
- Not performed: any test outside the supplied files (bank statements, vendor confirmations, contracts), as required by the closed-world instruction.

## 7. Status

Review complete for manager draft rev 1 / evidence v1. Result: **SUPPORTED with 6 non-substantive corrections (C1–C6)**. Open: comparison with investigator output (pending).
