from app import (
    BracketValidator,
    Matrix2x2,
    RangeBucket,
    Tag,
    TemperatureConverter,
    TitleCaseFormatter,
    WordHistogram,
    add,
    add9,
    dozenx,
    factorial,
    heptax,
    ninex,
    nove,
    pentax,
    septuple,
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


def test_temperature_converter_celsius_to_fahrenheit_freezing_and_boiling():
    converter = TemperatureConverter()

    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(100) == 212


def test_temperature_converter_fahrenheit_to_celsius_freezing_and_boiling():
    converter = TemperatureConverter()

    assert converter.fahrenheit_to_celsius(32) == 0
    assert converter.fahrenheit_to_celsius(212) == 100


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
