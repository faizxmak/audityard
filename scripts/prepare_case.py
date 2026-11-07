"""Copy the four audit inputs into a new case directory and print its kickoff."""

import argparse
from pathlib import Path
import re
import shutil
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team", default="audityard", help="Template team prefix")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9-]*", args.team):
        parser.error("team must start with a lowercase letter and use letters, digits, or hyphens")

    root = Path(__file__).resolve().parents[1]
    names = ("START_HERE.md", "work_orders.jsonl", "evidence.jsonl", "payments.jsonl")
    for name in names:
        if not (root / "agent-pack" / name).is_file():
            parser.error(f"Missing input file: {name}")

    case = Path(tempfile.mkdtemp(prefix="audityard-")).resolve()
    inputs = case / "agent-pack"
    inputs.mkdir()
    output = case / "output"
    output.mkdir()
    for name in names:
        shutil.copy2(root / "agent-pack" / name, inputs / name)

    print(f"Case directory: {case}")
    print("This is a temporary folder. Copy finished outputs somewhere permanent.")
    print("Only the four input files were copied. This does not restrict the agents' filesystem access.")
    print("\nPaste this message in the new audit room:\n")
    print(
        f"@{args.team}-manager Run case MERIDIAN-OCT2026. Audit October 2026 "
        f"as of 7 November 2026 using only the four input files in {inputs}. "
        "Read START_HERE.md for the company policies, scope, and required outputs. "
        "Pass the same input and output paths to your team. Coordinate extraction, "
        "investigation, and independent review through this room. Do not read "
        "evaluation files, example outputs, or previous benchmark answers. "
        f"Save final_report.md, disposition_register.csv, reconciliation.json, and "
        f"the separate specialist artifacts under {output}. "
        "Complete the review before final delivery. Report any access or messaging "
        "blocker. Post a concise final summary with the exact output paths."
    )


if __name__ == "__main__":
    main()
