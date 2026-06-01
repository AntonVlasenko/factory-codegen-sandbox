"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""


def add(a: int, b: int) -> int:
    return a + b


class Counter:
    def __init__(self, start=0):
        self._value = start

    @property
    def value(self):
        return self._value

    def increment(self, amount=1):
        self._value += amount
        return self._value

    def decrement(self, amount=1):
        self._value -= amount
        return self._value
