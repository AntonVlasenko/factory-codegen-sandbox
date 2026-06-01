"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def double(n: int) -> int:
    return 2 * n


def negate(n: int) -> int:
    return -n


def is_even(n: int) -> bool:
    return n % 2 == 0


def clamp(x: int, lo: int, hi: int) -> int:
    return min(max(x, lo), hi)
