import pytest

from app import ScoreTracker, Tag, add, add9, dozenx, factorial, nove, septuple


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add9():
    assert add9(0) == 9
    assert add9(3) == 12
    assert add9(-10) == -1


def test_septuple():
    assert septuple(0) == 0
    assert septuple(3) == 21
    assert septuple(-2) == -14


def test_nove():
    assert nove(0) == 0
    assert nove(3) == 27
    assert nove(-2) == -18


def test_dozenx():
    assert dozenx(0) == 0
    assert dozenx(3) == 36
    assert dozenx(-2) == -24


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_tag_label_lowercases_category_and_name():
    tag = Tag(name="Python", category="Language")

    assert tag.label() == "language:python"


def test_tag_matches_name_case_insensitively():
    tag = Tag(name="Python", category="Language")

    assert tag.matches("I write PYTHON every day")
    assert tag.matches("cpython runtime")
    assert not tag.matches("I write Ruby every day")


def test_score_tracker_accepts_starting_scores_and_tracks_highest_average():
    tracker = ScoreTracker([72, 95, 88])

    assert tracker.highest() == 95
    assert tracker.average() == pytest.approx(85.0)


def test_score_tracker_add_appends_scores():
    tracker = ScoreTracker()

    tracker.add(80)
    tracker.add(92)

    assert tracker.highest() == 92
    assert tracker.average() == pytest.approx(86.0)


def test_score_tracker_passed_returns_scores_in_original_order():
    tracker = ScoreTracker(score for score in [60, 85, 70, 92, 85])

    assert tracker.passed(85) == [85, 92, 85]


def test_score_tracker_empty_highest_and_average_raise_value_error():
    tracker = ScoreTracker()

    with pytest.raises(ValueError):
        tracker.highest()
    with pytest.raises(ValueError):
        tracker.average()
