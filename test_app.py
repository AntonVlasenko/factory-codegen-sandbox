from app import add, is_even


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_even_zero():
    assert is_even(0) is True


def test_is_even_positive_odd():
    assert is_even(3) is False


def test_is_even_negative_even():
    assert is_even(-4) is True
