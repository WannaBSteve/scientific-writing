# Task

Revise the passage around the equation. Preserve the notation. Do not add a new
parameter.

# Draft

For classes $c$ and counts $n_c$:

\[
V(S)=\sum_c n_c[\hat l_c(S_0)-\hat l_c(S)]-\hat C(S_0\rightarrow S).
\]

Here, $S$ is a state. This is standard. We choose the maximum.

# Supplied facts

- The classes group equivalent completed requests.
- The counts are observed occurrences in the recent window.
- Latency comes from a prior measurement, a database estimate, or a short
  probe.
- Transition cost covers construction and validation.
- A positive value makes the candidate eligible for private construction.
