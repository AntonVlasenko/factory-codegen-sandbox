from app import add, sub3


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub3():
    assert sub3(5) == 2
    assert sub3(0) == -3
