from app import add, cube


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0
