import pytest

from app import add, percent_change


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_percent_change_positive():
    assert percent_change(100, 125) == 25


def test_percent_change_negative():
    assert percent_change(80, 60) == -25


def test_percent_change_zero_baseline():
    with pytest.raises(ValueError):
        percent_change(0, 10)
