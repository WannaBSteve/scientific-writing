# Reviewer responses

Use this reference for rebuttals, revision letters, response documents, and
change summaries.

## Treat the comment as the response contract

Preserve the reviewer's wording. Extract every requested item and answer in the
same order. A response fails when it provides substantial new material but
leaves one requested item implicit.

## Response progression

Use the shortest progression that fully answers the comment:

1. Thank the reviewer and acknowledge the underlying need.
2. Give the direct answer.
3. Explain the design choice when the answer depends on it.
4. State what changed.
5. Report the evidence and result.
6. Point to the manuscript location.

Do not repeat gratitude before every paragraph. Do not delay the answer with a
project history or engineering narrative.

## Explain before defending

When a reviewer appears to have missed an existing mechanism, first ask why the
paper made it hard to see. Clarify the mechanism in ordinary language and show
the relevant evidence. Avoid wording that implies the reviewer failed to read
carefully.

## Match evidence to requested questions

Keep evidence surfaces separate:

- method prose answers how the mechanism works;
- a resource table answers what the mechanism costs;
- a scaling study answers how optimization grows;
- a lifecycle figure answers what happens over time;
- an ablation answers which component causes a result.

Do not combine unrelated metrics into a single dense table merely to reduce the
number of response objects.

## Avoid defensive writing

Retain a negative or limiting sentence only when it:

- answers a reviewer statement;
- defines the measured scope;
- prevents a specific technical misreading;
- reports a real limitation or negative result.

Remove preemptive denials, descriptions of what the work is not, and detailed
engineering history that does not answer the comment.

## Report changes precisely

Use future tense only for work not yet completed. For completed revisions,
state what was added or changed and provide the section, figure, table, or
equation label.

Do not say "we clarified" when the actual change is an experiment, algorithm,
or new definition. Name the change.

## Response audit

Before delivery, verify:

- every requested item has a direct answer;
- the response order follows the comment;
- gratitude is respectful and brief;
- design rationale connects the problem to the mechanism;
- evidence appears next to the claim it supports;
- all results have workload, metric, and baseline scope;
- figure and table references resolve;
- promised manuscript changes are written or clearly marked as pending;
- no internal run names or debug details remain;
- no unraised objection interrupts the main explanation.
