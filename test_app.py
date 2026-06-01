import pytest

from app import add, divide, is_even, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(-3, -7) == 4


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(-2, 5) == -10
    assert multiply(9, 0) == 0


def test_divide():
    assert divide(9, 3) == 3.0
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
