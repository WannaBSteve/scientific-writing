# Methods rewrite example

This synthetic example shows the skill's central operation. It reconstructs the
method trace before editing sentences.

- [`draft.md`](draft.md) contains correct but disconnected facts.
- [`evidence.md`](evidence.md) fixes the allowed facts and terminology.
- [`expected.md`](expected.md) is a reference revision and rationale. It is not
  a recorded agent run or a benchmark result.

Try it with:

```text
Use $scientific-writing in revise mode. Revise
examples/methods-rewrite/draft.md using examples/methods-rewrite/evidence.md.
Preserve every fact and return a copy-ready Methods passage.
```
