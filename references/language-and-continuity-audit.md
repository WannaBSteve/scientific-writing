# Language and continuity audit

Use this reference after the scientific argument is correct. Surface polish
cannot repair a missing rationale, unsupported link, or wrong evidence order.

## Paragraph continuity

For each adjacent pair of paragraphs, ask:

- Does the second paragraph answer a question created by the first?
- If the subject changes, is the reason for the change clear?
- Does a transition name a real logical relation?
- Could the paragraphs be swapped without changing meaning? If so, the
  organizing relation may be missing.

## Sentence continuity

Prefer sentences with an explicit actor and action when that clarifies the
mechanism. Keep passive voice when the actor is irrelevant or the object is the
stable topic.

Break a sentence when it performs several independent reasoning steps. Join
short sentences when separating them hides a direct causal or computational
relation.

## Abstract noun load

Several technical nouns in a row can hide the action:

```text
candidate configuration transition benefit estimation
```

Restore the actor and operation:

```text
LogicDB estimates how much time the candidate saves and how much the transition
costs.
```

Keep established technical terms. Replace only noun chains that force the
reader to reconstruct the relation.

## Staging and defensive patterns

Review phrases that often delay the point:

- "It is important to note that"
- "It should be emphasized that"
- "This is not merely"
- "Rather than"
- "While it may appear"
- "To be clear"
- "It introduces no"

Some are valid. Keep them only when the contrast or boundary has already
become relevant.

## Punctuation and rhythm

Match the author's deliberate style. In the absence of a sample:

- prefer periods and commas for technical prose;
- use semicolons when they clarify two closely related independent clauses;
- use dashes sparingly;
- do not turn every aside into parentheses;
- avoid repeated sentence shapes and forced groups of three.

No punctuation mark is universally forbidden. Density is a prompt to inspect
the reasoning, not an automatic error.

## Terminology

- Use one name per concept.
- Define a term when first needed.
- Avoid local engineering names in reader-facing prose.
- Do not replace a precise term only to avoid repetition.
- Use capitalization consistently for named system operations.

## AI-sounding prose

Remove language that performs importance instead of adding information:

- inflated significance;
- generic claims of robustness or comprehensiveness;
- decorative triads;
- repeated "not X but Y" frames;
- chatbot greetings and closers;
- headings followed by a sentence that repeats the heading;
- citations used as borrowed authority without explanation.

Do not optimize for an AI detector. Preserve the author's voice and the
scientific meaning.

## Final integrity pass

Compare the revision with the source and evidence. Check:

- all numbers and units;
- baselines and comparison direction;
- conditions and qualifiers;
- notation and labels;
- causal language;
- citation placement;
- negative results;
- requested scope;
- unresolved evidence needs.
