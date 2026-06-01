"""factory-codegen-sandbox — a disposable target for autonomous codegen.

The factory's Phase 11 vertical adds/edits functions here; pytest is the gate.
"""

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass
class Tag:
    name: str
    category: str

    def label(self) -> str:
        return f"{self.category}:{self.name}".lower()

    def matches(self, text: str) -> bool:
        return self.name.lower() in text.lower()


@dataclass(frozen=True)
class TagCatalog:
    tags: Tuple[Tag, ...]

    @classmethod
    def from_iterable(cls, tags: Iterable[Tag]) -> "TagCatalog":
        return cls(tuple(tags))

    def labels(self) -> List[str]:
        return [tag.label() for tag in self.tags]

    def in_category(self, category: str) -> List[Tag]:
        return [
            tag
            for tag in self.tags
            if tag.category.lower() == category.lower()
        ]

    def matching(self, text: str) -> List[Tag]:
        return [tag for tag in self.tags if tag.matches(text)]


@dataclass(frozen=True)
class TaggedText:
    title: str
    body: str
    catalog: TagCatalog

    def word_count(self) -> int:
        return len(self.body.split())

    def matched_tags(self) -> List[Tag]:
        return self.catalog.matching(self.body)

    def matched_labels(self) -> List[str]:
        return [tag.label() for tag in self.matched_tags()]


@dataclass(frozen=True)
class CampaignReport:
    name: str
    entries: Tuple[TaggedText, ...]

    @classmethod
    def from_iterable(
        cls, name: str, entries: Iterable[TaggedText]
    ) -> "CampaignReport":
        return cls(name=name, entries=tuple(entries))

    def total_word_count(self) -> int:
        return sum(entry.word_count() for entry in self.entries)

    def tag_counts(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for entry in self.entries:
            for label in entry.matched_labels():
                counts[label] = counts.get(label, 0) + 1
        return counts

    def summary(self) -> str:
        return (
            f"{self.name}: {len(self.entries)} entries, "
            f"{self.total_word_count()} words"
        )


def add(a: int, b: int) -> int:
    return a + b
