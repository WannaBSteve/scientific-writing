# Methods and systems writing

Use this reference for Methods sections, system designs, algorithms,
protocols, implementations, and technical mechanism explanations.

## Start from the method trace

Represent the method before drafting:

```text
problem
  -> available inputs and state
  -> ordered operations
  -> decision or branch
  -> resulting output or state
  -> validation
```

For a stateful system, add when state becomes visible and which later operation
consumes it. For an experimental protocol, add sampling, controls, and the
measurement that determines the result.

Do not expose this representation unless the user asks for a plan or it helps
explain a structural revision.

## Explain a design choice

A design choice is persuasive when the reader can answer:

1. What concrete problem rules out the simpler choice?
2. What mechanism did the authors choose?
3. Why does that mechanism address the problem?
4. What evidence or precedent supports the choice?
5. What cost or scope condition matters for interpreting it?

Do not start with "we design" or "we introduce" when the reader does not yet
know the problem. Do not list a trade-off merely to sound balanced. Include it
when it changes use, interpretation, or evaluation.

## Describe stages in their real order

Use numbered steps when operations occur in a true sequence. Each step should
state:

- the actor or component;
- the input it reads;
- the work it performs;
- the output or state change;
- the condition that advances or stops the process.

Example pattern:

```text
The controller processes a candidate in four steps. (1) It estimates ...
(2) It selects ... (3) It realizes ... (4) It publishes ...
```

After the overview, expand each step in the same order. Do not rename stages
between the overview, algorithm, figure, and evaluation.

## Separate proposal, decision, and execution

Many systems combine a heuristic, model, or agent with deterministic system
logic. Keep their responsibilities distinct:

| Role | Reader question |
|---|---|
| Proposal | Where do candidates come from? |
| Decision | Which candidates are accepted, and by what rule? |
| Execution | How is the chosen action realized? |
| Validation | What prevents an incorrect or harmful state? |

Do not attribute numerical estimates to a language model when the database,
optimizer, simulator, or measurement system supplies them. Conversely, do not
hide a semantic decision inside generic "system logic" when a model makes it.

## Stateful and concurrent methods

For stateful or asynchronous systems, identify:

- the current visible state;
- the private or candidate state;
- the work that can proceed without changing visibility;
- the operation that changes visibility;
- the failure outcome;
- the state seen by subsequent requests.

Use a short table or timeline when prose would force the reader to remember
more than two states across several steps.

## Algorithms and pseudocode

Pseudocode should expose the decision structure, not mirror implementation
line by line. Before adding an algorithm, check that it contributes at least
one of:

- ordering that prose cannot show compactly;
- a nontrivial branch or loop;
- an invariant;
- a termination or acceptance condition;
- a relationship used by later analysis.

Use the same names in prose and pseudocode. Explain inputs and outputs before
walking through internal steps. State whether the algorithm is exact,
heuristic, bounded, or locally refining when that affects the claim.

## Implementation detail filter

Keep an implementation detail in the paper when it explains:

- correctness;
- performance;
- reproducibility;
- a design trade-off;
- a reviewer-requested mechanism.

Move or remove it when it is only a run directory, trial name, debug protocol,
internal variable, or incidental engineering history.

## Methods audit

Before delivery, verify:

- the problem appears before the mechanism that solves it;
- stages use one stable vocabulary;
- inputs and outputs are explicit;
- branch conditions are stated where the branch occurs;
- the visibility or state transition is clear;
- equations control a named decision;
- validation follows the operation it validates;
- evidence supports the design rationale rather than merely decorating it;
- evaluation metrics correspond to the stated costs and benefits.
