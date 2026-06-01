from app import CampaignReport, Tag, TagCatalog, TaggedText, add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_tag_label_lowercases_category_and_name():
    tag = Tag(name="Python", category="Language")

    assert tag.label() == "language:python"


def test_tag_matches_name_case_insensitively():
    tag = Tag(name="Python", category="Language")

    assert tag.matches("I write PYTHON every day")
    assert tag.matches("cpython runtime")
    assert not tag.matches("I write Ruby every day")


def test_tag_catalog_lists_labels_and_filters_by_category():
    catalog = TagCatalog.from_iterable(
        [
            Tag(name="Python", category="Language"),
            Tag(name="Pytest", category="Tool"),
            Tag(name="Ruby", category="Language"),
        ]
    )

    assert catalog.labels() == ["language:python", "tool:pytest", "language:ruby"]
    assert [tag.name for tag in catalog.in_category("language")] == [
        "Python",
        "Ruby",
    ]


def test_tagged_text_counts_words_and_matched_labels():
    catalog = TagCatalog.from_iterable(
        [
            Tag(name="Python", category="Language"),
            Tag(name="Pytest", category="Tool"),
            Tag(name="Ruby", category="Language"),
        ]
    )
    entry = TaggedText(
        title="Build notes",
        body="Python tests run with pytest",
        catalog=catalog,
    )

    assert entry.word_count() == 5
    assert entry.matched_labels() == ["language:python", "tool:pytest"]


def test_campaign_report_summarizes_entries_and_tag_counts():
    catalog = TagCatalog.from_iterable(
        [
            Tag(name="Python", category="Language"),
            Tag(name="Pytest", category="Tool"),
            Tag(name="Ruby", category="Language"),
        ]
    )
    report = CampaignReport.from_iterable(
        "Test Campaign",
        [
            TaggedText(
                title="One",
                body="Python and pytest are useful",
                catalog=catalog,
            ),
            TaggedText(title="Two", body="Ruby is also useful", catalog=catalog),
        ],
    )

    assert report.total_word_count() == 9
    assert report.tag_counts() == {
        "language:python": 1,
        "tool:pytest": 1,
        "language:ruby": 1,
    }
    assert report.summary() == "Test Campaign: 2 entries, 9 words"
