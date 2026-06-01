from app import Counter, add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_counter_initialization():
    assert Counter().value == 0
    assert Counter(start=5).value == 5


def test_counter_increment():
    counter = Counter(start=2)

    assert counter.increment() == 3
    assert counter.value == 3
    assert counter.increment(4) == 7
    assert counter.value == 7


def test_counter_decrement():
    counter = Counter(start=5)

    assert counter.decrement() == 4
    assert counter.value == 4
    assert counter.decrement(3) == 1
    assert counter.value == 1
