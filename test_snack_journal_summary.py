import pytest

from snackoracle import snack_journal_summary


def test_snack_journal_summary_happy_path():
    entries = [
        {"snack": "Chips", "quantity": 2, "mood": "Happy"},
        {"snack": "cookies", "quantity": 1, "mood": "happy"},
        {"snack": "chips", "quantity": 3, "mood": "stressed"},
    ]

    result = snack_journal_summary(entries)

    assert isinstance(result, str)
    assert "entries=3" in result
    assert "total_servings=6" in result
    assert "Top snack: chips" in result
    assert "Moods: happy=2, stressed=1" in result
    assert "Snack energy: medium" in result


def test_snack_journal_summary_empty_list():
    result = snack_journal_summary([])
    assert result == "Snack Journal: 0 entries. No snacks logged yet."


def test_snack_journal_summary_requires_list():
    with pytest.raises(TypeError):
        snack_journal_summary("chips")


def test_snack_journal_summary_entry_must_be_dict():
    with pytest.raises(TypeError):
        snack_journal_summary([{"snack": "chips", "quantity": 1, "mood": "happy"}, 2])


def test_snack_journal_summary_missing_keys():
    with pytest.raises(ValueError):
        snack_journal_summary([{"snack": "chips", "quantity": 1}])


def test_snack_journal_summary_type_validation():
    with pytest.raises(TypeError):
        snack_journal_summary([{"snack": 5, "quantity": 1, "mood": "happy"}])

    with pytest.raises(TypeError):
        snack_journal_summary([{"snack": "chips", "quantity": "2", "mood": "happy"}])

    with pytest.raises(TypeError):
        snack_journal_summary([{"snack": "chips", "quantity": 2, "mood": 7}])


def test_snack_journal_summary_value_validation():
    with pytest.raises(ValueError):
        snack_journal_summary([{"snack": "   ", "quantity": 1, "mood": "happy"}])

    with pytest.raises(ValueError):
        snack_journal_summary([{"snack": "chips", "quantity": 0, "mood": "happy"}])

    with pytest.raises(ValueError):
        snack_journal_summary([{"snack": "chips", "quantity": 1, "mood": "   "}])


def test_snack_journal_summary_top_snack_tie_break():
    entries = [
        {"snack": "pretzels", "quantity": 1, "mood": "happy"},
        {"snack": "chips", "quantity": 1, "mood": "happy"},
    ]

    result = snack_journal_summary(entries)

    assert "Top snack: chips" in result
    assert "Snack energy: low" in result
