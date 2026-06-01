from app import add, octuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_octuple():
    assert octuple(3) == 24
    assert octuple(-2) == -16
    assert octuple(0) == 0
