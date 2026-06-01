from app import add, add3


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add3():
    assert add3(2) == 5
    assert add3(-1) == 2
