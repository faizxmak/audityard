"""Check the saved example's coverage, cash totals, and reference ownership.

This does not grade policy interpretation or reproduce the 91/100 rubric score.
Uses only the Python standard library. Run from any working directory.
"""

import csv
from collections import Counter, defaultdict
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    root = Path(__file__).resolve().parents[1]

    def records(name):
        return [json.loads(line) for line in (root / "agent-pack" / name).read_text().splitlines() if line.strip()]

    orders = records("work_orders.jsonl")
    evidence = records("evidence.jsonl")
    payments = records("payments.jsonl")
    with (root / "example-run/disposition_register.csv").open(newline="") as handle:
        register = list(csv.DictReader(handle))
    reported = json.loads((root / "example-run/reconciliation.json").read_text())
    controls = json.loads((root / "evaluation/control_totals.json").read_text())

    order_ids = {row["work_order_id"] for row in orders}
    require(len(order_ids) == len(orders), "Source work-order IDs are duplicated")
    require(len(register) == len(orders), "Register size differs from the input")
    require({row["work_order_id"] for row in register} == order_ids, "Register has missing or extra orders")
    evidence_by_id = {row["evidence_id"]: row for row in evidence}
    require(len(evidence_by_id) == len(evidence), "Evidence IDs are duplicated")

    unique_events = {}
    settled = {}
    failed = []
    repeated = []
    for row in payments:
        require(row["work_order_id"] in order_ids, "Payment references an unknown work order")
        key = row["event_id"]
        if key in unique_events:
            require(row == unique_events[key], f"Conflicting repeated bank event {key}")
            repeated.append(row)
            continue
        unique_events[key] = row
        if row["status"] == "settled":
            settled[key] = row
        elif row["status"] == "failed":
            failed.append(row)
        else:
            raise ValueError(f"Unrecognized bank event status {row['status']}")

    net_by_order = defaultdict(int)
    for row in settled.values():
        net_by_order[row["work_order_id"]] += row["amount_usd"]
    for row in register:
        order = row["work_order_id"]
        require(int(row["net_settled_usd"]) == net_by_order[order], f"Cash mismatch for {order}")
        for key in filter(None, row["evidence_ids"].split(";")):
            require(key in evidence_by_id and evidence_by_id[key]["work_order_id"] == order,
                    f"Evidence reference mismatch for {order}: {key}")
        for key in filter(None, row["payment_event_ids"].split(";")):
            require(key in unique_events and unique_events[key]["work_order_id"] == order,
                    f"Payment reference mismatch for {order}: {key}")

    gross = sum(row["amount_usd"] for row in settled.values() if row["amount_usd"] > 0)
    returns = -sum(row["amount_usd"] for row in settled.values() if row["amount_usd"] < 0)
    computed = {
        "work_orders": len(orders), "evidence_records": len(evidence),
        "raw_payment_rows": len(payments),
        "raw_signed_amount_sum": sum(row["amount_usd"] for row in payments),
        "failed_attempts_excluded": sum(row["amount_usd"] for row in failed),
        "duplicate_export_amount_excluded": sum(row["amount_usd"] for row in repeated),
        "unique_settled_events": len(settled), "gross_settled_outflows": gross,
        "settled_returns": returns, "net_settled_cash": gross - returns,
        "contract_fees": sum(row["fee_usd"] for row in orders),
    }
    require(computed == controls, "Recomputed controls differ from the supplied evaluator totals")
    expected_report = {
        "rows": len(payments), "failed_rows": len(failed),
        "failed_amt": computed["failed_attempts_excluded"], "dup_rows": len(repeated),
        "dup_amt": computed["duplicate_export_amount_excluded"], "settled_rows": len(settled),
        "gross_settled": gross, "returns": -returns, "net_settled": gross - returns,
        "total_fees": computed["contract_fees"],
        "classes": dict(Counter(row["classification"] for row in register)),
    }
    require(reported == expected_report, "Published reconciliation differs from recomputed results")
    print(f"PASS: {len(register)} orders, no missing or duplicate register entries")
    print("PASS: cited evidence and bank event IDs belong to their stated orders")
    print(f"PASS: {len(settled)} unique settled events; ${gross - returns:,} net cash")
    print("PASS: all supplied control totals and the published reconciliation match")
    print("Not assessed: source authenticity, policy conclusions, or the manual rubric score")


if __name__ == "__main__":
    main()
