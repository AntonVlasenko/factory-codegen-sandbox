from app import add, dec


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_dec():
    assert dec(3) == 2
    assert dec(0) == -1
