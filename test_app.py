from app import add, half


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_half():
    assert half(4) == 2
    assert half(5) == 2.5
