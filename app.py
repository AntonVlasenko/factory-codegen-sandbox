"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass


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
        slug = []
        previous_was_separator = False

        for character in text.lower():
            if character.isalnum():
                slug.append(character)
                previous_was_separator = False
            elif not previous_was_separator:
                slug.append("-")
                previous_was_separator = True

        return "".join(slug).strip("-")


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
