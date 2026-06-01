from app import add, nonuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_nonuple():
    assert nonuple(2) == 18
    assert nonuple(-1) == -9
