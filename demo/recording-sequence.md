# Recording sequence

Use [script.md](script.md) as the read-aloud text. Record the completed `#audit-yard` run. Describe it as a completed run, since the video walks through existing messages and files.

| Approximate time | Screen | What to show |
|---|---|---|
| 0:00–0:25 | Repository README | Project name and the opening explanation |
| 0:25–0:40 | `agent-pack/START_HERE.md` | Fictional company, period, and company policies |
| 0:40–1:10 | Mattermost `#audit-yard` | Human kickoff, manager assignment, specialist reply, reviewer reply, final delivery |
| 1:10–1:25 | Initial review, then register | Correction C4 asks for financial categories; the register has `exposure_bucket` |
| 1:25–1:55 | Final report | Find WO-6210, then WO-1507; leave each conclusion readable |
| 1:55–2:15 | Evaluation, then README | 91/100, deductions, and the template link |

Before recording, open these screens in order and enlarge the text. Avoid scrolling through long sections while speaking. The shot timings are a guide; clarity matters more than fitting every line into two minutes.

## Terms in the script

- **Work order** means an agreement to buy a particular piece of work from a supplier.
- **Acceptance** means the customer confirms the work was completed satisfactorily.
- **Bank callback** means calling a previously verified number to check a change in payment details.
- **Reconciliation** means matching the recorded payments and explaining differences.
- **Unresolved** means the supplied evidence cannot settle the question.
- **Register** means the table with one result for each work order.

## Answers for likely judge questions

**What did you build?** I configured the four agent roles, shared room rules, task handoffs, and review loop in Switch, using AI assistance. This repository packages that workflow and its benchmark evidence.

**Why four agents?** Evidence extraction, investigation, review, and coordination have different responsibilities. The separate review produced observable corrections in this run. I have not yet measured whether it outperforms one agent on cost, speed, or accuracy.

**What does 91 mean?** It is an AI-assisted assessment using the supplied 100-point rubric. It is one synthetic run, with 24 challenge cases. It is not a measured production accuracy rate or an external auditor's validation.

**Did the agents see the answer key?** It was excluded from the input handoff. No evaluator access was found in the recorded tool calls. Filesystem isolation was not enforced, so I do not claim a fully isolated test.

**What was the human's role?** I supplied the case and scope. The agents produced the draft findings and review. A person must assess those outputs before acting on them; the recording does not show a completed human sign-off.

**What would you improve next?** Run new, independently authored packets with enforced input isolation, measure a single-agent baseline, and test messier documents and more specific evidence requests.
