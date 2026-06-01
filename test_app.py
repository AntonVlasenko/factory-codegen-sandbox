from app import (
    Tag,
    add,
    add9,
    dozenx,
    factorial,
    heptax,
    ninex,
    nove,
    pentax,
    septuple,
    triplex,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add9():
    assert add9(0) == 9
    assert add9(3) == 12
    assert add9(-10) == -1


def test_septuple():
    assert septuple(0) == 0
    assert septuple(3) == 21
    assert septuple(-2) == -14


def test_heptax():
    assert heptax(0) == 0
    assert heptax(3) == 21
    assert heptax(-2) == -14


def test_nove():
    assert nove(0) == 0
    assert nove(3) == 27
    assert nove(-2) == -18


def test_ninex():
    assert ninex(0) == 0
    assert ninex(3) == 27
    assert ninex(-2) == -18


def test_triplex():
    assert triplex(0) == 0
    assert triplex(3) == 9
    assert triplex(-2) == -6


def test_pentax():
    assert pentax(0) == 0
    assert pentax(3) == 15
    assert pentax(-2) == -10


def test_dozenx():
    assert dozenx(0) == 0
    assert dozenx(3) == 36
    assert dozenx(-2) == -24


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_tag_label_lowercases_category_and_name():
    tag = Tag(name="Python", category="Language")

    assert tag.label() == "language:python"


def test_tag_matches_name_case_insensitively():
    tag = Tag(name="Python", category="Language")

    assert tag.matches("I write PYTHON every day")
    assert tag.matches("cpython runtime")
    assert not tag.matches("I write Ruby every day")
