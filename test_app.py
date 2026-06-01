from app import add, quad


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_quad():
    assert quad(2) == 8
    assert quad(-1) == -4
