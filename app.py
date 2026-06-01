"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass
from collections import Counter
import re


@dataclass
class Matrix2x2:
    a: float
    b: float
    c: float
    d: float

    def determinant(self) -> float:
        return self.a * self.d - self.b * self.c

    def multiply_vector(self, x: float, y: float) -> tuple[float, float]:
        return (self.a * x + self.b * y, self.c * x + self.d * y)


class RangeBucket:
    def __init__(self, upper_bounds: list[float]):
        self.upper_bounds = upper_bounds

    def label(self, value: float) -> str:
        for index, bound in enumerate(self.upper_bounds):
            if value <= bound:
                return f"bucket_{index}"
        return "bucket_overflow"


@dataclass
class Tag:
    name: str
    category: str

    def label(self) -> str:
        return f"{self.category}:{self.name}".lower()

    def matches(self, text: str) -> bool:
        return self.name.lower() in text.lower()


class WordHistogram:
    def top_counts(self, text: str) -> dict[str, int]:
        words = re.findall(r"[a-z]+", text.lower())
        return dict(Counter(words))


class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9


class TitleCaseFormatter:
    def format_name(self, text: str) -> str:
        return " ".join(text.split()).title()


class BracketValidator:
    def is_balanced(self, text: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        opening = set(pairs.values())
        stack: list[str] = []

        for character in text:
            if character in opening:
                stack.append(character)
            elif character in pairs:
                if not stack or stack.pop() != pairs[character]:
                    return False

        return not stack


def add(a: int, b: int) -> int:
    return a + b


def add9(n: int) -> int:
    return n + 9


def septuple(n: int) -> int:
    return 7 * n


def heptax(n: int) -> int:
    return n * 7


def nove(n: int) -> int:
    return n * 9


def ninex(n: int) -> int:
    return n * 9


def triplex(n: int) -> int:
    return n * 3


def pentax(n: int) -> int:
    return n * 5


def vala(n: int) -> int:
    return n * 4


def valb(n: int) -> int:
    return n * 6


def vald(n: int) -> int:
    return n * 11


def dozenx(n: int) -> int:
    return n * 12


def factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
