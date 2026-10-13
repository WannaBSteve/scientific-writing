# Candidate selection

The selector compares the measured cost of the current configuration with the
estimated cost of each candidate. It chooses a candidate only when the expected
saving covers construction and validation.

The database optimizer supplies the candidate cost when it can represent the
proposed structure. Otherwise, the system measures a short probe. Repeated
requests retain their observed counts in both cases.
