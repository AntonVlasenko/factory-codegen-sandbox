"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass
from collections import Counter
import re
import string


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


@dataclass
class TimeRange:
    start: int
    end: int

    def __post_init__(self) -> None:
        if not 0 <= self.start < self.end <= 1440:
            raise ValueError("TimeRange requires 0 <= start < end <= 1440")

    def duration_minutes(self) -> int:
        return self.end - self.start

    def contains(self, minute: int) -> bool:
        return self.start <= minute < self.end

    def overlaps(self, other: "TimeRange") -> bool:
        return self.start < other.end and other.start < self.end


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


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def _words(self) -> list[str]:
        return [
            word
            for word in (
                raw_word.strip(string.punctuation).lower()
                for raw_word in self.text.split()
            )
            if word
        ]

    def word_count(self) -> int:
        return len(self._words())

    def unique_words(self) -> list[str]:
        return sorted(set(self._words()))

    def most_common_word(self) -> str | None:
        words = self._words()
        if not words:
            return None

        return Counter(words).most_common(1)[0][0]


class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9


@dataclass
class BankAccount:
    owner: str
    balance: float

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("deposit amount cannot be negative")

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("insufficient funds")

        self.balance -= amount
        return self.balance

    def apply_interest(self, rate: float) -> float:
        self.balance += self.balance * rate
        return self.balance


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


def lerpx(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


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


def iz1(n: int) -> int:
    return n * 3


def pentax(n: int) -> int:
    return n * 5


def vala(n: int) -> int:
    return n * 4


def wala(n: int) -> int:
    return n * 4


def valb(n: int) -> int:
    return n * 6


def walb(n: int) -> int:
    return n * 6


def walc(n: int) -> int:
    return n * 8


def vald(n: int) -> int:
    return n * 11


def wald(n: int) -> int:
    return n * 11


def dozenx(n: int) -> int:
    return n * 12


def signx(n: int | float) -> int:
    return (n > 0) - (n < 0)


def clampx(x: int | float, lo: int | float, hi: int | float) -> int | float:
    return max(lo, min(x, hi))


def factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
