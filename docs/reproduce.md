# Reproduce the workflow

## Requirements

- Switch Console with a running local Switch server and a Mattermost connection.
- Claude Code installed and signed in on that computer, with enough provider usage available for four agent sessions.
- Python 3 for the optional case-preparation and result-checking helpers. Neither helper needs third-party packages.

The recorded run used macOS, Switch Console 0.40.1, Switch Core 0.31.0, and four local Claude Code agents. [Switch's getting-started guide](https://docs.switchagents.ai/switch-rooms/getting-started) covers installation and messaging setup.

## Create the team

1. Download or clone this repository.
2. In Switch Console, open **Templates** and import `audityard.template.yaml`.
3. Use the template. Choose an unused team prefix and select your Mattermost connection. The default prefix is `audityard`; its room is `audityard-audit`.
4. Check that the room contains you and all four agents, and that each agent uses local Claude Code. Keep all four on the same computer so the case paths are shared.

The template does not automatically start an audit. The next step supplies the input location and scope.

## Prepare and start a case

From the repository root, run the following command. If you chose a different team prefix, replace `audityard` with that prefix.

```sh
python3 scripts/prepare_case.py --team audityard
```

The helper creates a fresh temporary case directory with `agent-pack/` and `output/`. It copies exactly four input files, then prints a kickoff message with absolute paths and the right manager mention. Paste that message into the new Mattermost room.

For manual preparation, copy only `agent-pack/` to a separate case folder, create an empty output directory, and fill in [demo/kickoff.md](../demo/kickoff.md). Do not give the team the repository root as its audit input. It contains assessment notes and saved outputs.

A separate directory does not prevent an agent running under your account from reading other accessible files. For a truly isolated evaluation, restrict the account or environment to the inputs and writable outputs. Do not use a prompt as a substitute for that restriction.

## What completion looks like

The manager assigns extraction, investigation, and review through the room. Specialists return artifact paths and results. The manager resolves review feedback, then posts a final summary with these files in the supplied output directory.

```text
output/
  final_report.md
  disposition_register.csv
  reconciliation.json
  case/
    evidence/
    investigation/
    review/
```

The register should cover every source work order. Read the independent review and any unresolved issues before acting on the final report. Save the outputs to a permanent location before the temporary folder is cleaned up.

## If a run stops

Check whether the manager's assignment was actually posted, whether its recipient is in the room, and whether that agent can open the supplied paths. Check the agent's error in Switch Console and its provider sign-in or usage status. A join message or tool count does not demonstrate task completion. Resume the specific blocked handoff rather than repeatedly posting the whole kickoff.

## Template provenance and verification

The template packages the four-role design and shared coordination rules from the recorded run. It replaces machine-specific paths with kickoff paths, adds a configurable prefix, focuses the investigator on supplier payments, and makes completion, acceptance, filing, and follow-up checks explicit. The manager is instructed to wait for the investigator's output before requesting the comparison review.

These are post-evaluation changes. The 91/100 score belongs to the original run; it is not a score for the released template. Verification results for the release are recorded in [verification.md](verification.md).

The workflow and submission materials were developed with AI assistance. The synthetic packet and evaluator materials were supplied for this exercise. Switch, Claude Code, and Mattermost are existing tools used by the workflow.
