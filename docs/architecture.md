# Architecture

The repository is one Agent Skill with progressive references. The entrypoint
contains the shared evidence and argument workflow. It routes to a focused
reference only when the current task needs that material.

```text
user request
  -> operation: plan | draft | revise | audit | respond
  -> writing contract
  -> argument compilation
  -> task reference
  -> evidence-preserving output
  -> integrity check
```

The prose auditor is independent of the generative workflow. It reports
mechanical signals and can run in CI or an editor. Its warnings do not override
author intent or disciplinary conventions.

Behavior cases evaluate model decisions. Unit tests evaluate deterministic
code and repository consistency. The project does not describe asset validation
as a model benchmark.
