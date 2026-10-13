---
name: scientific-writing
description: Plan, draft, revise, or audit scientific manuscripts and reviewer responses by reconstructing the argument, method trace, equation logic, citation roles, and evidence path before editing prose. Use especially for Methods, system design, algorithms, cost models, technical figures and tables, and revisions where correct facts still read as disconnected or defensive. Do not use for literature discovery alone, statistical analysis alone, or generic grammar correction with no scientific argument.
---

# Scientific Writing

Turn technical content into a continuous argument without changing what the
evidence supports. Work on the reasoning before polishing sentences.

## Choose the requested operation

- **Plan:** produce the section contract, argument map, evidence needs, and
  paragraph progression. Do not draft full prose unless requested.
- **Draft:** write new prose from supplied facts, results, and sources.
- **Revise:** restructure or rewrite supplied prose while preserving facts,
  measurements, notation, citation meaning, and scope.
- **Audit:** return prioritized, located findings. Do not silently edit the
  source.
- **Respond:** answer reviewer comments and connect each answer to a concrete
  manuscript change and evidence.

Honor a narrower request. A paragraph edit does not authorize a full paper
rewrite or new scientific claims.

## Start with the writing contract

Before drafting, recover five items from the supplied material:

1. **Reader question:** What question should this passage answer now?
2. **Section job:** What must this section accomplish that adjacent sections do
   not?
3. **Supported conclusion:** What can the reader conclude from the available
   evidence?
4. **Required path:** What reasoning, mechanism, or sequence connects the
   question to that conclusion?
5. **Evidence anchors:** Which equations, citations, figures, tables, examples,
   or measurements support each step?

For a short edit, keep this map internal. Show it when the user requests a plan
or when a structural problem must be explained.

Read [argument-compilation.md](references/argument-compilation.md) when the
passage is disconnected, repetitive, hard to follow, or structurally unclear.

## Compile the argument before editing prose

Use this internal representation:

```text
reader question
    -> claim or design decision
    -> reason
    -> mechanism or ordered process
    -> evidence
    -> scope
```

Not every passage needs all six parts. Keep only the parts that perform real
work. Preserve the author's established voice and terminology when they are
clear.

For every paragraph, check reader-state continuity:

- What does the reader know at the start?
- What single question does the paragraph answer?
- What new conclusion is available at the end?
- Why does the next paragraph follow?

Reorder facts when their current order forces the reader to infer missing
links. Do not add a causal link merely to make the prose smooth.

## Use the Methods path for technical mechanisms

For Methods, system design, algorithms, protocols, or implementation
descriptions, read [methods-and-systems.md](references/methods-and-systems.md).

Build a method trace before writing:

```text
problem -> inputs -> ordered operations -> decision -> state/output -> validation
```

When the method branches, state the decision that creates the branch and the
condition for each path. Use numbered steps only for a real order. Do not turn
unrelated facts into a decorative list.

A design choice needs three connected statements:

1. the problem that makes the choice necessary;
2. the chosen mechanism;
3. the reason this mechanism addresses the problem under the stated scope.

Add a trade-off only when it affects interpretation or is supported by the
available evidence.

## Bridge equations to the method

For equations, objectives, constraints, estimators, and cost models, read
[equations-and-cost-models.md](references/equations-and-cost-models.md).

An equation is not complete until the prose establishes:

1. the question it answers;
2. the meaning and source of its terms;
3. the decision or inference it controls;
4. how its output is measured, estimated, or validated.

Introduce the idea before its notation. After the equation, explain term
provenance in the order used to compute the quantity. Separate objectives,
constraints, and reported resources when they use different units or answer
different questions.

## Give every citation a job

For design rationale, comparisons, or related work, read
[citations-and-related-work.md](references/citations-and-related-work.md).

Do not use a citation as decoration after phrases such as "follows prior work."
State what the cited work contributes. Common citation jobs are:

- definition;
- design precedent;
- mechanism;
- measurement method;
- empirical comparison;
- contrast or limitation.

Do not claim that a source supports a statement unless the source text was
checked or the support was supplied. Preserve an unresolved citation need as a
located issue.

## Route evidence through figures and tables

For figure planning, captions, table design, or manuscript integration, read
[figures-and-tables.md](references/figures-and-tables.md).

Each evidence object should answer one primary question. Split an object when
its columns, panels, or metrics answer unrelated questions. Use stable labels
and refer to the object in prose. A caption identifies the measurement and
scope. The body explains the result and why it matters.

## Answer reviewers in the order of their request

For rebuttals, revision letters, and response packages, read
[reviewer-responses.md](references/reviewer-responses.md).

Preserve the reviewer comment. Then move through:

```text
thanks and agreement on the underlying need
    -> direct answer
    -> design rationale when needed
    -> completed change
    -> evidence and result
    -> manuscript location
```

Do not hide the answer behind process notes. Do not introduce unraised
objections into the main explanation. Necessary scope conditions remain close
to the claim they qualify.

## Protect evidence and author intent

- Preserve numbers, units, baselines, conditions, causal direction, certainty,
  and negative results.
- Do not invent measurements, citations, definitions, motivations, or links
  between facts.
- Distinguish a checked source from a citation marker that has not been
  inspected.
- State when evidence is missing. Do not repair an evidence gap with a softer
  unsupported claim.
- Keep terminology stable. Introduce a new term only when it reduces repeated
  explanation and can be defined plainly.
- Follow the user's venue, format, color, labeling, and file constraints.

## Revise in passes

Use the smallest set of passes that fits the task:

1. **Contract:** recover the reader question, section job, and supported
   conclusion.
2. **Structure:** build the argument map or method trace.
3. **Evidence:** attach equations, citations, figures, tables, and measurements
   to the claims they support.
4. **Paragraphs:** give each paragraph one main job and preserve continuity.
5. **Sentences:** make actors and actions explicit, remove empty staging, and
   match the author's voice.
6. **Integrity:** compare the revision with the source facts and requested
   scope.

Read [language-and-continuity-audit.md](references/language-and-continuity-audit.md)
for a full prose audit. The bundled `scripts/audit_prose.py` reports mechanical
signals only. Treat its warnings as prompts for review, not proof of an error or
AI authorship.

## Deliver the requested artifact

- **Plan:** section contract, ordered claims, evidence anchors, and unresolved
  needs.
- **Draft or revision:** copy-ready prose or an explicitly requested file,
  followed by a concise note on material changes when useful.
- **Audit:** prioritized findings with locations, reasons, and concrete repair
  actions.
- **Reviewer response:** copy-ready response plus matching manuscript changes
  and evidence locations.

Do not force the user to read an internal checklist. Lead with the revised
artifact or the highest-consequence finding.
