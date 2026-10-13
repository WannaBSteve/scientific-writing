# Equations and cost models

Use this reference for objectives, estimators, constraints, optimization
problems, scoring functions, and measured acceptance rules.

## The equation bridge

Surround each important equation with four links:

1. **Purpose:** What question does this equation answer?
2. **Provenance:** Where does each term come from?
3. **Decision:** What changes because of the result?
4. **Validation:** How is the estimate checked or measured?

The purpose comes before the equation. Provenance and decision normally follow
it in the order the quantity is computed.

## A practical order

For a cost model, use this progression:

```text
decision question
    -> compact objective
    -> benefit computation
    -> cost computation
    -> feasibility constraints
    -> estimator sources
    -> measured correction or validation
```

Do not begin with a sum over classes, weights, or latent variables before the
reader knows the decision the sum supports.

## Term provenance

For every term, identify whether it is:

- directly measured;
- estimated by an established backend;
- predicted by a learned model;
- supplied as a configured constant;
- counted from observed data;
- derived from other terms.

If several sources are used in priority order, state that order as a real
sequence. Explain why later sources are needed.

## Keep units coherent

Terms added or subtracted in one objective need compatible units. Do not
silently convert storage, model tokens, latency, and money into one score with
arbitrary weights.

Use constraints or separate reporting when a quantity answers a different
question:

| Quantity | Typical treatment |
|---|---|
| latency saved | objective benefit |
| one-time construction time | transition cost |
| storage capacity | hard constraint |
| dependency or conflict | feasibility constraint |
| model tokens | resource accounting |
| solver wall time | optimizer overhead and configuration |

This table is guidance, not a universal rule. Follow the actual system and
state any justified conversion.

## Explain aggregation

When a workload term is aggregated, state:

- the unit being aggregated;
- the source of its weight or count;
- the observation window or population;
- how equivalent units are grouped;
- how interactions avoid double counting.

Grouping repeated observations is a computational optimization. It should not
silently change their total contribution.

## Objectives and constraints have different jobs

Explain the objective in plain language before listing constraints. For each
constraint family, state the invalid outcome it prevents.

Example pattern:

```text
The objective selects the configuration with the largest estimated net value.
Prerequisite constraints prevent an action from being selected without its
provider. Conflict constraints prevent incompatible alternatives. Capacity
constraints keep resource use within the configured budget.
```

Use formulas after those purposes are clear. A list of inequalities alone does
not explain the design.

## Estimated and measured decisions

When the system estimates before acting and measures afterward, state the two
decisions separately:

1. the estimate decides whether a candidate is worth realizing;
2. the measurement decides whether the realized candidate is accepted.

Clarify whether the measured value replaces or supplements the estimate. Do
not make a cost appear to be charged twice. If construction is sunk before the
second decision, state whether the acceptance rule considers total cost,
remaining cost, or both. The rule must match the implementation and claim.

## Citation support for cost models

A citation should identify the borrowed modeling principle. Compare:

Weak:

```text
This follows workload-based design practice [1, 2].
```

Useful:

```text
Prior physical-design advisors estimate how candidate structures change the
cost of a representative workload and choose a configuration under storage
constraints [1, 2]. We use the same workload-level comparison for ...
```

The second version gives the reader a concrete analogy and explains the design
choice.

## Equation audit

For each displayed equation, verify:

- a reader can say what question it answers;
- every symbol is defined before or immediately after first use;
- term sources are stated;
- units are compatible;
- weights or counts have an observable meaning;
- the equation controls a named decision;
- constraints are tied to invalid outcomes;
- later measurement uses consistent terms;
- the evaluation reports the quantities the method claims to optimize.
