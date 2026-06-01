from app import add, triple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_triple():
    assert triple(2) == 6
    assert triple(-4) == -12
    assert triple(0) == 0
