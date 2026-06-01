from app import Rectangle, add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_rectangle_area_and_perimeter():
    rectangle = Rectangle(4, 5)

    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18


def test_rectangle_scale_returns_new_rectangle_without_mutating_original():
    rectangle = Rectangle(4, 5)

    scaled = rectangle.scale(3)

    assert isinstance(scaled, Rectangle)
    assert scaled is not rectangle
    assert scaled.width == 12
    assert scaled.height == 15
    assert rectangle.width == 4
    assert rectangle.height == 5
