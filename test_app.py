import pytest

from app import (
    BankAccount,
    BracketValidator,
    Matrix2x2,
    RangeBucket,
    Tag,
    TemperatureConverter,
    TextAnalyzer,
    TimeRange,
    TitleCaseFormatter,
    WordHistogram,
    add,
    add9,
    clampx,
    dozenx,
    factorial,
    heptax,
    iz1,
    iz2,
    lerpx,
    ninex,
    nove,
    pentax,
    septuple,
    signx,
    triplex,
    vala,
    valb,
    vald,
    wala,
    walb,
    walc,
    wald,
)


def test_matrix2x2_calculates_determinant_and_multiplies_vector():
    matrix = Matrix2x2(1, 2, 3, 4)

    assert matrix.determinant() == -2
    assert matrix.multiply_vector(5, 6) == (17, 39)


def test_range_bucket_labels_first_matching_bound_and_overflow():
    bucket = RangeBucket([10, 20, 30])

    assert bucket.label(10) == "bucket_0"
    assert bucket.label(11) == "bucket_1"
    assert bucket.label(30) == "bucket_2"
    assert bucket.label(31) == "bucket_overflow"


def test_time_range_calculates_duration_minutes():
    time_range = TimeRange(60, 150)

    assert time_range.duration_minutes() == 90


def test_time_range_contains_start_and_excludes_end():
    time_range = TimeRange(60, 150)

    assert time_range.contains(60)
    assert time_range.contains(149)
    assert not time_range.contains(59)
    assert not time_range.contains(150)


def test_time_range_detects_overlaps_and_adjacent_ranges():
    time_range = TimeRange(60, 150)

    assert time_range.overlaps(TimeRange(0, 61))
    assert time_range.overlaps(TimeRange(149, 240))
    assert not time_range.overlaps(TimeRange(0, 60))
    assert not time_range.overlaps(TimeRange(150, 240))


def test_time_range_accepts_full_day_bounds():
    time_range = TimeRange(0, 1440)

    assert time_range.duration_minutes() == 1440
    assert time_range.contains(0)
    assert time_range.contains(1439)
    assert not time_range.contains(1440)


def test_time_range_rejects_invalid_bounds():
    invalid_bounds = [
        (-1, 60),
        (60, 60),
        (120, 60),
        (60, 1441),
    ]

    for start, end in invalid_bounds:
        with pytest.raises(ValueError):
            TimeRange(start, end)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_lerpx_interpolates_between_endpoints():
    assert lerpx(10, 20, 0) == 10
    assert lerpx(10, 20, 1) == 20
    assert lerpx(10, 20, 0.25) == 12.5
    assert lerpx(20, 10, 0.5) == 15


def test_add9():
    assert add9(0) == 9
    assert add9(3) == 12
    assert add9(-10) == -1


def test_septuple():
    assert septuple(0) == 0
    assert septuple(3) == 21
    assert septuple(-2) == -14


def test_heptax():
    assert heptax(0) == 0
    assert heptax(3) == 21
    assert heptax(-2) == -14


def test_nove():
    assert nove(0) == 0
    assert nove(3) == 27
    assert nove(-2) == -18


def test_ninex():
    assert ninex(0) == 0
    assert ninex(3) == 27
    assert ninex(-2) == -18


def test_triplex():
    assert triplex(0) == 0
    assert triplex(3) == 9
    assert triplex(-2) == -6


def test_iz1():
    assert iz1(0) == 0
    assert iz1(3) == 9
    assert iz1(-2) == -6


def test_iz2():
    assert iz2(0) == 0
    assert iz2(3) == 15
    assert iz2(-2) == -10


def test_pentax():
    assert pentax(0) == 0
    assert pentax(3) == 15
    assert pentax(-2) == -10


def test_vala():
    assert vala(0) == 0
    assert vala(3) == 12
    assert vala(-2) == -8


def test_wala():
    assert wala(0) == 0
    assert wala(3) == 12
    assert wala(-2) == -8


def test_valb():
    assert valb(0) == 0
    assert valb(3) == 18
    assert valb(-2) == -12


def test_walb():
    assert walb(0) == 0
    assert walb(3) == 18
    assert walb(-2) == -12


def test_walc():
    assert walc(0) == 0
    assert walc(3) == 24
    assert walc(-2) == -16


def test_vald():
    assert vald(0) == 0
    assert vald(3) == 33
    assert vald(-2) == -22


def test_wald():
    assert wald(0) == 0
    assert wald(3) == 33
    assert wald(-2) == -22


def test_dozenx():
    assert dozenx(0) == 0
    assert dozenx(3) == 36
    assert dozenx(-2) == -24


def test_signx_returns_negative_zero_or_positive_sign():
    assert signx(-10) == -1
    assert signx(0) == 0
    assert signx(7) == 1


def test_clampx_returns_bounds_or_value_within_inclusive_range():
    assert clampx(-1, 0, 10) == 0
    assert clampx(0, 0, 10) == 0
    assert clampx(5, 0, 10) == 5
    assert clampx(10, 0, 10) == 10
    assert clampx(11, 0, 10) == 10


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


def test_word_histogram_counts_lowercase_alphabetic_words_only():
    histogram = WordHistogram()

    assert histogram.top_counts("Hello, hello! HELLO... world? 123 world.") == {
        "hello": 3,
        "world": 2,
    }


def test_text_analyzer_counts_words_case_insensitively_and_strips_punctuation():
    analyzer = TextAnalyzer("Hello, hello! HELLO... world? 'world'")

    assert analyzer.word_count() == 5
    assert analyzer.unique_words() == ["hello", "world"]
    assert analyzer.most_common_word() == "hello"


def test_text_analyzer_unique_words_are_sorted():
    analyzer = TextAnalyzer("banana apple, Cherry! apple")

    assert analyzer.unique_words() == ["apple", "banana", "cherry"]


def test_text_analyzer_returns_none_when_text_has_no_words():
    analyzer = TextAnalyzer("... !!! ---")

    assert analyzer.word_count() == 0
    assert analyzer.unique_words() == []
    assert analyzer.most_common_word() is None


def test_temperature_converter_celsius_to_fahrenheit_freezing_and_boiling():
    converter = TemperatureConverter()

    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(100) == 212


def test_temperature_converter_fahrenheit_to_celsius_freezing_and_boiling():
    converter = TemperatureConverter()

    assert converter.fahrenheit_to_celsius(32) == 0
    assert converter.fahrenheit_to_celsius(212) == 100


def test_bank_account_deposits_amount_and_returns_new_balance():
    account = BankAccount(owner="Ada", balance=100)

    assert account.deposit(25) == 125
    assert account.balance == 125


def test_bank_account_withdraws_amount_and_returns_new_balance():
    account = BankAccount(owner="Ada", balance=100)

    assert account.withdraw(30) == 70
    assert account.balance == 70


def test_bank_account_applies_interest_and_returns_new_balance():
    account = BankAccount(owner="Ada", balance=100)

    assert account.apply_interest(0.05) == 105
    assert account.balance == 105


def test_bank_account_rejects_negative_deposit():
    account = BankAccount(owner="Ada", balance=100)

    with pytest.raises(ValueError):
        account.deposit(-1)


def test_bank_account_rejects_negative_withdrawal():
    account = BankAccount(owner="Ada", balance=100)

    with pytest.raises(ValueError):
        account.withdraw(-1)


def test_bank_account_rejects_withdrawal_exceeding_balance():
    account = BankAccount(owner="Ada", balance=100)

    with pytest.raises(ValueError):
        account.withdraw(101)


def test_title_case_formatter_trims_and_title_cases_name():
    formatter = TitleCaseFormatter()

    assert formatter.format_name("  jANE doe  ") == "Jane Doe"


def test_title_case_formatter_collapses_internal_whitespace():
    formatter = TitleCaseFormatter()

    assert formatter.format_name("john\t  quincy\nadams") == "John Quincy Adams"


def test_bracket_validator_accepts_empty_text_and_text_without_brackets():
    validator = BracketValidator()

    assert validator.is_balanced("")
    assert validator.is_balanced("plain text with 123 punctuation!")


def test_bracket_validator_accepts_balanced_nested_brackets():
    validator = BracketValidator()

    assert validator.is_balanced("({[]})")
    assert validator.is_balanced("function(arg[0], {key: (value)})")


def test_bracket_validator_rejects_mismatched_or_crossed_brackets():
    validator = BracketValidator()

    assert not validator.is_balanced("(]")
    assert not validator.is_balanced("([)]")


def test_bracket_validator_rejects_unmatched_closing_bracket():
    validator = BracketValidator()

    assert not validator.is_balanced("]")
    assert not validator.is_balanced("text ) after")


def test_bracket_validator_rejects_unclosed_opening_brackets():
    validator = BracketValidator()

    assert not validator.is_balanced("(")
    assert not validator.is_balanced("{[nested]")
