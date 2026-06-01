"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Tag:
    name: str
    category: str

    def label(self) -> str:
        return f"{self.category}:{self.name}".lower()

    def matches(self, text: str) -> bool:
        return self.name.lower() in text.lower()


class ScoreTracker:
    def __init__(self, scores: Iterable[int] | None = None) -> None:
        self._scores = list(scores) if scores is not None else []

    def add(self, score: int) -> None:
        self._scores.append(score)

    def highest(self) -> int:
        return max(self._scores)

    def average(self) -> float:
        return sum(self._scores) / len(self._scores)

    def passed(self, minimum: int) -> list[int]:
        return [score for score in self._scores if score >= minimum]


def add(a: int, b: int) -> int:
    return a + b


def add9(n: int) -> int:
    return n + 9


def septuple(n: int) -> int:
    return 7 * n


def nove(n: int) -> int:
    return n * 9


def dozenx(n: int) -> int:
    return n * 12


def factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
