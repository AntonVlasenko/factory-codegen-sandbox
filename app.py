"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""


def add(a: int, b: int) -> int:
    return a + b


def dectuple(n: int) -> int:
    return 10 * n
