# Scientific Writing implementation plan

## Release target

Publish version 0.1.0 as one portable Agent Skill with a strong Methods path,
progressive references, deterministic audits, behavior cases, and an
open-source repository suitable for external contributors.

## Build order

1. Create the skill entrypoint and UI metadata.
2. Implement the argument-compilation and Methods references.
3. Add equation, citation, figure/table, response, and language references.
4. Add a report-only prose auditor and unit tests.
5. Add synthetic behavior cases and asset validation.
6. Add examples that demonstrate the distinctive workflows.
7. Add English and Chinese documentation, contribution files, metadata, and
   CI.
8. Run skill validation, tests, example audits, and repository consistency
   checks.
9. Install a local copy for discovery testing.
10. Create the GitHub repository under WannaBSteve and push the tagged release.

## Quality gates

- `quick_validate.py` passes.
- `python3 -m unittest discover -s tests -v` passes.
- `python3 scripts/check_eval_assets.py` passes.
- `python3 scripts/audit_prose.py examples/clean-control.md` reports no
  findings at the default threshold.
- Every `SKILL.md` reference exists and is routed by task.
- No placeholder, private manuscript detail, or copied third-party prose ships.
- README install instructions work from a clean temporary directory.
- The Git working tree is clean before publication.
