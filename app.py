"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""


def add(a: int, b: int) -> int:
    return a + b


def percent_change(old: float, new: float) -> float:
    if old == 0:
        raise ValueError("old must not be 0")

    return ((new - old) / old) * 100
