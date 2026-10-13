# Scientific Writing skill design

## Goal

Build an open Agent Skill that improves scientific writing by reconstructing
the argument before editing sentences. The first release must be useful for a
single paragraph, a Methods section, a system paper, or a reviewer response.
Methods and technical design are the deepest path, not a thin section-specific
checklist.

The skill preserves supplied facts, measurements, citations, notation, and
author decisions. It does not invent evidence, silently broaden claims, or
replace disciplinary judgment with surface style rules.

## Positioning

Existing tools usually specialize in one of three layers:

1. prose cleanup and removal of AI-sounding patterns;
2. broad manuscript checklists;
3. large collections of independent research skills.

This project focuses on the layer between technical content and prose. It
turns claims, mechanisms, equations, citations, and evidence into a continuous
reader path. The repository calls this **argument compilation**.

Argument compilation is not a new scientific method. It is an internal writing
workflow that makes the following relationships explicit before drafting:

```text
reader question
    -> claim or design decision
    -> reason
    -> mechanism or ordered process
    -> evidence
    -> scope
```

## Distinctive mechanisms

### Reader-state continuity

For each paragraph, determine:

- what the reader already knows;
- the question the paragraph must answer;
- the new conclusion the reader can draw at the end;
- why the next paragraph follows.

This check detects fact stacking, abrupt terminology, repeated setup, and
paragraphs that are individually correct but collectively hard to follow.

### Method trace

Technical methods are first represented as an ordered trace:

```text
problem -> inputs -> operations -> decision -> state/output -> validation
```

The trace may branch when the method branches. The prose follows the actual
order of reasoning or execution unless another order clearly serves the target
reader better.

### Equation bridge

An equation is complete only when the surrounding prose establishes:

1. the question the equation answers;
2. the meaning and source of each term;
3. the decision or inference it controls;
4. how the quantity is measured, estimated, or validated.

The skill must not add notation before the corresponding idea is needed.

### Citation job

Every citation used to justify a design choice receives a concrete job. The
text states what the cited work contributes, such as a definition, precedent,
mechanism, measurement method, or contrast. A citation attached only to a
generic phrase such as "follows prior work" fails this check.

### Evidence routing

Each table and figure answers one primary question. The surrounding prose
states that question, references the object by label, and explains the result
without repeating the caption. Measurements that answer different questions
remain separate.

### Objection relevance

Scope conditions and limitations stay when they are needed to interpret a
claim. Sentences that answer an objection the reader has not encountered are
removed or moved to the response that raised it. This distinguishes useful
precision from defensive writing.

## Modes

The entry skill routes among five modes:

1. **Plan** builds the argument and evidence map without drafting prose.
2. **Draft** writes new prose from supplied content and the argument map.
3. **Revise** changes existing prose while preserving technical meaning.
4. **Audit** returns prioritized, located findings without rewriting unless
   requested.
5. **Respond** connects a reviewer request to reasoning, completed changes,
   evidence, and manuscript locations.

The user may request a narrow operation. The skill does not expand a paragraph
edit into a full manuscript audit.

## Repository architecture

```text
scientific-writing/
|-- SKILL.md
|-- agents/openai.yaml
|-- references/
|   |-- argument-compilation.md
|   |-- methods-and-systems.md
|   |-- equations-and-cost-models.md
|   |-- citations-and-related-work.md
|   |-- figures-and-tables.md
|   |-- reviewer-responses.md
|   `-- language-and-continuity-audit.md
|-- scripts/audit_prose.py
|-- tests/
|-- evals/
|-- examples/
|-- docs/
|-- .github/workflows/ci.yml
|-- README.md
|-- README.zh-CN.md
|-- CONTRIBUTING.md
|-- CITATION.cff
|-- LICENSE
`-- VERSION
```

`SKILL.md` contains the shared workflow and routes to only the references
needed for the current task. References contain decisions and examples rather
than repeated generic advice.

## Audit helper

`scripts/audit_prose.py` reports deterministic surface signals in Markdown,
plain text, and LaTeX. It does not rewrite text and does not claim to detect AI
authorship. Initial checks cover:

- dash and semicolon density;
- unusually long sentences;
- repeated paragraph openings;
- common staged or defensive phrases;
- figure and table references without matching labels;
- labels that are never referenced;
- generic citation lead-ins such as "follows prior work";
- equations with no nearby purpose or interpretation prose.

Warnings are review prompts. They are not proof of bad writing.

## Behavioral evaluations

The repository ships synthetic cases with rubrics. At minimum, cases cover:

- a disconnected Methods paragraph that must become an ordered process;
- a cost equation that lacks term provenance and operational meaning;
- a decorative citation that must explain the borrowed design principle;
- a response letter that contains unraised objections;
- a mixed-purpose table that must be split by evidence question;
- a concise paragraph that should remain unchanged.

Each case separates input, evidence, expected properties, and grading rubric.
The expected output is never presented as a recorded model benchmark unless a
real isolated run has been performed.

## Open-source quality

The first release includes:

- English and Chinese READMEs;
- install instructions for Codex, Claude Code, and generic Agent Skills hosts;
- a clear quick-start example and a full Methods example;
- MIT license and citation metadata;
- contribution guidelines and issue templates;
- CI for package validation, unit tests, links between references, and eval
  asset consistency;
- semantic version `0.1.0`;
- no copied prose or code from comparison repositories.

## Acceptance criteria

The release is complete when:

1. the skill passes the bundled Agent Skill validator;
2. all deterministic tests and repository checks pass;
3. every reference linked by `SKILL.md` exists and has a defined trigger;
4. examples preserve all supplied facts and demonstrate the distinctive
   mechanisms above;
5. the audit helper produces useful warnings and no warnings on its clean
   control fixture;
6. a fresh reader can install and invoke the skill from the README;
7. the repository has a clean Git history and is pushed to
   `WannaBSteve/scientific-writing` when remote creation credentials are
   available.

## Boundaries

The project does not provide plagiarism detection, AI-authorship detection,
automatic citation verification, venue acceptance prediction, or a substitute
for domain expertise. It does not upload private manuscripts. Network lookup
occurs only when the user requests source research and the active environment
provides an authorized tool.
