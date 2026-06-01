"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass
import re


@dataclass
class Tag:
    name: str
    category: str

    def label(self) -> str:
        return f"{self.category}:{self.name}".lower()

    def matches(self, text: str) -> bool:
        return self.name.lower() in text.lower()


class Slugifier:
    def build(self, text: str) -> str:
        slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
        return slug.strip("-")


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
