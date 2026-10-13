# Supplied evidence

- The three advisors propose Layout, Index, and Reusable actions.
- The solver checks dependencies, conflicts, storage, and expected net value.
- Net value is estimated workload saving minus one-time transition cost.
- Current request latency is measured.
- Candidate latency uses, in order, a compatible prior measurement, a database
  optimizer estimate, or a short probe.
- Repeated equivalent requests preserve their observed counts.
- Only selected changes are built in a private state.
- Affected requests are replayed against the candidate.
- An operation may be removed when it fails correctness or measured payoff.
- Requests continue to use the current state until Publication.
- Publication atomically changes the visible descriptor.
- Unreachable old objects are reclaimed afterward.
- References [1, 2] describe physical-design advisors that compare candidate
  structures by their estimated representative-workload cost.
- The source text of references [1, 2] is not available in this example.
