from app import add, clamp, double, is_even, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-4, 5) == -20
    assert multiply(0, 9) == 0


def test_double():
    assert double(3) == 6
    assert double(-4) == -8
    assert double(0) == 0


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_clamp():
    assert clamp(5, 1, 10) == 5
    assert clamp(-1, 1, 10) == 1
    assert clamp(12, 1, 10) == 10
