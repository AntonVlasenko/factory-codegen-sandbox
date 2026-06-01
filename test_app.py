from app import add, eleventuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_eleventuple():
    assert eleventuple(2) == 22
    assert eleventuple(-1) == -11
