# Behavior evaluations

These synthetic cases test the decisions that distinguish this skill from a
surface copy editor. They do not prove general writing quality or predict
publication outcomes.

Run each case in a fresh agent session. Give the agent only `SKILL.md`, the
references it selects, and one case file. Do not expose `manifest.json` before
the response is complete.

Suggested instruction:

```text
Use $scientific-writing to complete the task in evals/cases/method-trace.md.
Return only the requested deliverable.
```

Grade the completed response against every criterion for that case. Equivalent
wording is acceptable. Invented facts, changed measurements, unsupported causal
links, or a false claim of source verification are automatic failures.

Validate the case assets with:

```bash
python3 scripts/check_eval_assets.py
```

This command checks the package, not model behavior. Store actual isolated run
records under `evals/results/` only after running them.
