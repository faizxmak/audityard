# Audityard demo script

Read the paragraphs below. Allow about 2 minutes 15 seconds, with short pauses while changing screens. The [recording sequence](recording-sequence.md) gives the matching shots.

---

Hi, I'm Faizan. This is Audityard, a supplier-payment audit workflow I configured using Switch.

Imagine a company has paid suppliers for a month of work. Someone needs to check what was approved, whether the work was accepted, and whether the payments match. The useful output is a finding you can trace back to its evidence.

For this demo, I used a fictional company called Meridian Works. The packet contains 184 work orders, supporting records, and payment transactions. The team checks them against nine company policies.

Here is the completed run in Mattermost. I gave the audit manager the scope and the input folder. Through Switch, it assigned work to three specialists. One organized the evidence, one checked the policies and payments, and one reviewed the sources and calculations separately.

You can see the assignments and replies in the room. The reviewer also asked for clearer financial categories, and the final register includes that change.

Here is one example of the reasoning. Two orders involved changed bank details. Company policy required a phone check before payment. For one order, Treasury confirmed the check was skipped. For the other, the record was missing. The report called the first a confirmed breach and left the second unresolved. That distinction matters when someone will act on the findings.

The team delivered a report and a register covering all 184 orders. A separate AI-assisted assessment scored this run 91 out of 100 against the supplied answer key. The deductions and limitations are published in the repository.

This is a prototype tested on synthetic data. A person still reviews the findings and decides what action to take.

The repository includes the Switch template, sample inputs, and completed outputs, so you can try the workflow yourself.
