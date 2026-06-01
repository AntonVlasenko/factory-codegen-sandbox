from app import add, square


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_square():
    assert square(3) == 9
    assert square(-4) == 16
    assert square(0) == 0
