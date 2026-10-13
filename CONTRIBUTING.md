# Contributing

Contributions should improve an observable writing decision rather than add a
generic rule.

## Good contributions

- a failure case with a clear repair principle;
- a Methods pattern that changes argument order or evidence placement;
- a citation, equation, table, or response rule with a realistic example;
- a narrow auditor check with low false-positive risk;
- a behavior case that distinguishes a useful decision from surface fluency.

## Before opening a pull request

1. State the writing failure and why existing guidance does not catch it.
2. Place shared guidance in `SKILL.md` only when most tasks need it. Put
   conditional guidance in the appropriate reference.
3. Add or update a behavior case for a user-facing change.
4. Add deterministic tests for script changes.
5. Run `make check`.
6. Keep English and Chinese README claims consistent.

Do not add rules that force one punctuation style, paragraph count, or rhetorical
template across disciplines. Do not use private manuscripts as fixtures.

## Pull request description

Include:

- the user request or failure mode;
- the changed decision rule;
- the example or behavior case;
- test output;
- any compatibility effect.
