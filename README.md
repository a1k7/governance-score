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
