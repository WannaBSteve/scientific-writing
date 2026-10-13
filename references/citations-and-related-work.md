# Citations and related work

Use this reference when citations support a definition, design choice,
measurement, comparison, or novelty claim.

## Assign a citation job

Every citation in an explanatory passage should have a visible job:

| Job | What the sentence must say |
|---|---|
| Definition | Which term or formalism is adopted |
| Precedent | Which design pattern is reused |
| Mechanism | Which causal or operational account is supported |
| Measurement | Which metric, protocol, or estimator is adopted |
| Comparison | Which result or capability is contrasted |
| Limitation | Which known boundary motivates the present choice |

The same source may perform several jobs, but the prose should not leave all of
them implicit.

## Explain the analogy

For a design precedent, use three moves:

1. state what the cited system or method does;
2. identify the shared problem structure;
3. state how the current work adapts or extends that design.

Example shape:

```text
Prior systems choose physical structures by estimating their effect on a
representative workload. Our problem has the same configuration-selection
structure, but it also includes ...
```

This is stronger than a citation list after "follows prior work" because it
helps the reader understand the choice.

## Verify support at the right level

Use explicit support states when auditing sources:

- `not checked`: only a citation marker or bibliographic record is available;
- `identity checked`: title and source match, but supporting text was not read;
- `text checked`: the relevant passage was inspected;
- `supports`: the passage supports the claim at the stated scope;
- `partly supports`: only part or a narrower version is supported;
- `contradicts`: the source conflicts with the claim.

Do not convert `not checked` into `supports` because a title sounds relevant.

## Avoid citation bundles that hide differences

When several sources support different parts of a sentence, separate the
claims or name each contribution. A long citation bundle is appropriate only
when the sources genuinely support the same proposition.

## Related work as a decision map

Organize related work around the dimensions that matter to the paper's design,
not one paragraph per paper. A useful comparison states:

- the problem addressed;
- the unit of optimization or analysis;
- the decision authority;
- the state or data affected;
- the validation mechanism;
- the measured scope.

Use a table only when the dimensions are stable and evidence exists for each
cell. Do not use checkmarks to hide meaningful partial support.

## Citation audit

Check that:

- every citation has a discernible job;
- design citations explain the borrowed principle;
- novelty claims name the actual comparison set;
- source support was not inferred from metadata alone;
- citation scope matches claim scope;
- the current work's difference follows the analogy rather than appearing as a
  detached novelty statement.
