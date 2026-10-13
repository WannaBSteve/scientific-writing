# Argument compilation

Use this reference when correct facts still read as disconnected, repetitive,
or hard to follow.

## The unit of revision

Do not begin with sentence polish. First recover the passage's argument:

| Element | Question |
|---|---|
| Reader question | What is the reader trying to understand here? |
| Claim | What answer does the passage support? |
| Reason | Why should the reader accept that answer? |
| Mechanism | What process connects cause, input, or decision to the result? |
| Evidence | Which source, equation, measurement, figure, or example supports it? |
| Scope | Under which conditions does the answer hold? |

A paragraph may omit elements already established nearby. It may not rely on a
missing link that the reader must invent.

## Build a reader path

For each paragraph, write a private four-line record:

```text
Given: what the reader already knows
Question: what this paragraph answers
New: what the reader learns
Next: why the next paragraph follows
```

If `New` contains several unrelated conclusions, split the paragraph. If
`Given` depends on material introduced later, reorder the passage. If `Next`
has no logical connection, add the missing reasoning or change the order. Do
not add a transition phrase to conceal a missing relationship.

## Common structural failures

### Fact stacking

Symptoms:

- each sentence is locally correct;
- sentences share a topic but not a progression;
- transitions could be permuted without changing meaning.

Repair by choosing a real organizing relation:

- temporal order;
- causal order;
- decision order;
- abstraction from problem to mechanism;
- evidence from observation to conclusion;
- comparison by a stable dimension.

### Premature notation

Symptoms:

- a paragraph opens with several symbols;
- the reader cannot say what decision the formula supports;
- prose after the formula merely repeats symbol definitions.

Repair by stating the scientific or operational question first. Introduce only
the notation needed for that question.

### Citation-shaped reasoning

Symptoms:

- a broad statement ends with several citations;
- the text does not state what was borrowed;
- the citations replace rather than support the rationale.

Repair by assigning each citation a concrete job. See
[citations-and-related-work.md](citations-and-related-work.md).

### Defensive detours

Symptoms:

- the passage denies a claim nobody made;
- a caveat appears before the main mechanism is understood;
- repeated "not" statements dominate the explanation.

Keep a sentence only when it defines the claim's scope, answers a raised
question, or prevents a likely technical misreading at that exact point.
Otherwise remove it or move it to the relevant response.

### Terminology churn

Symptoms:

- the same object receives several names;
- a local implementation term replaces a reader-facing concept;
- a new noun is introduced to summarize one sentence and never reused.

Choose one stable term. Prefer an established disciplinary term when it has the
right meaning. Define a new term only when it supports repeated reasoning.

## Paragraph contract

A strong technical paragraph usually has this shape:

1. State the question or conclusion.
2. Give the reason or mechanism.
3. Attach the relevant evidence or operational detail.
4. End when the paragraph's job is complete.

This is a diagnostic shape, not a fixed template. Do not force every paragraph
to contain four sentences or the same rhythm.

## Recompilation procedure

1. Extract all factual claims without editing them.
2. Mark the support for each claim.
3. Identify the one question the passage should answer.
4. Order the claims by a real reasoning relation.
5. Locate missing links. Add one only when supported.
6. Draft paragraphs around reader questions.
7. Restore equations, citations, labels, and scope conditions at the step they
   support.
8. Compare the revision against the extracted facts.

When the source is ambiguous, preserve the ambiguity as a question for the
author. Fluency is not permission to decide an unresolved scientific issue.
