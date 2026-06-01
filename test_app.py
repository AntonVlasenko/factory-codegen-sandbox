from app import add, dectuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_dectuple():
    assert dectuple(2) == 20
    assert dectuple(-3) == -30
