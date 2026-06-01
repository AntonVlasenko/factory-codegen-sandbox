from app import add, septuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_septuple():
    assert septuple(3) == 21
    assert septuple(-2) == -14
