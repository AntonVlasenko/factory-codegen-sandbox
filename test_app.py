from app import add, inc


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_inc():
    assert inc(1) == 2
    assert inc(-1) == 0
