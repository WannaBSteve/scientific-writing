# Figures and tables

Use this reference to plan, revise, caption, or integrate scientific evidence
objects.

## Give each object one primary question

Write the question before choosing the format. Examples:

- How does latency change with scale?
- Which stage dominates adaptation cost?
- When is each object published and retired?
- How many model calls and tokens does each workload use?

If columns or panels answer unrelated questions, split the object. Related
panels may remain together when their joint reading supports one conclusion.

## Choose the format by evidence relation

| Relation | Useful format |
|---|---|
| exact values across a few systems | table |
| trend over order, scale, or time | line plot |
| decomposition of one total | stacked bar |
| event and state sequence | timeline |
| object lifetime | Gantt or interval plot |
| repeated field comparison | aligned table or small multiples |

Do not add a visual when a sentence gives the relationship more clearly.

## Separate accounting domains

Do not combine metrics merely because they share a workload name. For example,
model tokens, end-to-end latency, solver time, and storage answer different
questions. Keep them in separate tables or clearly separated panels unless the
figure's purpose is to show their accounting relationship.

When two ledgers are not additive, state that relationship once in the caption
or text. Do not use visual alignment that implies addition.

## Captions and body text

A caption should identify:

- what is measured;
- the comparison or scope;
- the encoding needed to read the object;
- the statistic or aggregation when it is not obvious.

The body should state:

- the result the reader should notice;
- the explanation supported by the method or evidence;
- the claim this object supports.

Do not repeat every cell or panel in prose.

## Labels and references

Every numbered object needs a stable label. Refer to it by label rather than
"the figure below" or "the following table." Check that:

- every reference resolves;
- every label is referenced in the manuscript or response;
- numbering is generated rather than typed by hand when the format allows;
- a caption remains bound to its object;
- panel letters used in prose exist in the figure.

## Table design

- Use one metric per column.
- Include units in headers.
- Align numbers by value or decimal position.
- Avoid vertical rules unless the target style requires them.
- Separate input and output tokens rather than compressing them into one
  ambiguous field.
- Keep derived metrics only when they add interpretation.
- Use `--` for not applicable or not measured only when the caption defines it.
  Do not turn missing data into zero.

## Figure and table audit

Check:

- one primary question;
- correct format for the relationship;
- labels and references;
- caption scope and aggregation;
- metric names and units;
- visual grouping that matches accounting;
- no duplicated evidence without a distinct purpose;
- claims in prose match the plotted or tabulated values.
