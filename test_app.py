from app import add, clamp


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_clamp_below_range():
    assert clamp(-1, 0, 10) == 0


def test_clamp_in_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_above_range():
    assert clamp(11, 0, 10) == 10
