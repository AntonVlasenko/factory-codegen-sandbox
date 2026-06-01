from app import add, clamp, is_even, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_clamp():
    assert clamp(5, 1, 10) == 5
    assert clamp(-1, 1, 10) == 1
    assert clamp(12, 1, 10) == 10
