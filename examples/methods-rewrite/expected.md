# Reference revision

The optimizer processes each proposed database change in four stages. (1) The
Layout, Index, and Reusable advisors propose candidate operations. The selector
then checks their dependencies, conflicts, storage use, and expected net value.
It computes net value as the query time expected to be saved over the recent
workload minus the one-time transition cost. Current latency comes from completed
requests. Candidate latency comes from the first available source: a compatible
prior measurement, a database optimizer estimate, or a short probe. Equivalent
requests may be evaluated together, but their observed counts are preserved.
(2) The system builds only the selected changes in a private state. Requests
continue to use the current state during construction. (3) The system replays
the affected requests against the candidate. It removes any operation that
fails correctness or measured payoff. (4) Publication atomically changes the
visible descriptor after the remaining candidate passes validation. Later
requests use the published state, and unreachable objects are reclaimed.

This cost comparison follows a concrete physical-design precedent. References
[1, 2] describe advisors that compare candidate structures by their estimated
effect on a representative workload. The present optimizer uses the same
workload-level comparison across three interacting action types and adds private
measurement before Publication.

## Why the revision works

The revision first builds the method trace:

```text
propose -> select -> construct -> measure/refine -> publish -> reclaim
```

It then places cost estimation inside the selection stage, where the result is
used. The citations have a stated job. They support the workload-level design
precedent rather than decorating a generic claim.

This is an illustrative reference output. The example does not claim that the
cited source text was checked.
