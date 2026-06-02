# AI Agent Governance Score

**A free, open‑source tool to measure how governable your AI agent was at runtime.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why?

Enterprises today have no objective way to compare AI agent governance. Every vendor claims “we have governance” – but there’s no standard metric.

The **Governance Score** fills that gap. It gives you a single number (0–100) based on:

- **Continuity** – Did the agent’s identity and policy frame remain intact?
- **Evidence Freshness** – Were approvals, tokens, and context still valid at commit?
- **Rollback Viability** – Could every action be reversed? Was hidden commitment detected?

## How it works

1. Capture an execution trace of your agent in our **open JSON format** (canonical hashes, step‑by‑step).
2. Run the CLI tool:
   ```bash
   python governance_score.py trace.json
3.Get an instant score and interpretation.
No API. No cloud. No vendor lock‑in. Runs entirely on your own machine.

Installation

bash
git clone https://github.com/a1k7/governance-score.git
cd governance-score
No dependencies – uses only Python standard library (3.9+).

Usage

bash
python governance_score.py examples/aws_trace_failure.json
Example output:

text
📊 AI Agent Governance Score Report
===================================
Continuity Score:         16.67 / 100
Evidence Freshness Score: 83.33 / 100
Rollback Viability Score: 66.67 / 100

🎯 Governance Score:       51.67 / 100
📌 Interpretation:        Warning – risk of silent failure
For verbose step‑by‑step details, add --verbose or -v.
For machine‑readable JSON output (e.g., for automation), add --json.

Input Format

The tool expects a JSON array of step objects. Each step object MUST contain at least:

Field	Type	Description
continuity_valid	boolean	True if the agent’s identity and policy frame unchanged since last valid state.
evidence_fresh	boolean	True if all required time‑bound evidence (tokens, approvals) was within validity window.
rollback_viable	boolean	True if the action could still be reversed at commit time.
hidden_commitment	boolean	True if a retry or continuation was attempted without re‑authorisation.
Optional fields (e.g., step_name, timestamp) may be present for human readability.

#Scoring Formula

Let N = number of steps.

Continuity Score = (steps with continuity_valid = true) / N × 100
Evidence Freshness Score = (steps with evidence_fresh = true) / N × 100
Rollback Viability Score = (steps with rollback_viable = true AND hidden_commitment = false) / N × 100
Governance Score = 0.4 × Continuity Score + 0.3 × Evidence Freshness Score + 0.3 × Rollback Viability Score

Interpretation

**Score Range	Interpretation
90–100	Excellent – highly governable
70–89	Good – acceptable governance
50–69	Warning – risk of silent failure
<50	Critical – high risk of undetected drift
Examples

#The examples/ folder contains real execution traces from a live AWS run:

aws_trace_failure.json – trace where continuity collapsed and rollback failed (Warning score)
aws_trace_success.json – fully admissible trace (Excellent score)
survivability_trace.json – degradation from FULL to DENIED
Contributing

#License

MIT – free for any use, commercial or otherwise. See LICENSE for details.

Author

Akhilesh Warik – Founder, DecisionAssure
LinkedIn : www.linkedin.com/in/decisionassure

Star this repo if you find it useful. Spread the word. Let’s make agent governance measurable.
