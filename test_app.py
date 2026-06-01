from app import Tag, add, add7, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add7():
    assert add7(0) == 7
    assert add7(5) == 12
    assert add7(-10) == -3


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
