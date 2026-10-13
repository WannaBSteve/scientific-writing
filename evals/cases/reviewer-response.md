# Task

Rewrite the response so it answers the reviewer directly and points to the
completed evidence change.

# Reviewer comment

Report Advisor call count, token use, and wall time separately from end-to-end
latency.

# Draft response

We thank the reviewer. To be clear, our Advisor never blocks every request and
does not replace the database optimizer. It would be misleading to compare its
wall time with all prior agent systems. We added a table containing calls,
input and output tokens, wall time, Vanilla latency, system latency, Apply time,
and speedup.

# Completed change

A new table contains workload, request count, Advisor calls, input tokens,
output tokens, and cumulative Advisor wall time. End-to-end latency remains in
the performance figure.
