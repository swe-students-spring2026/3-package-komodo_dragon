import pytest

from guiltmeter import guilt_meter


def test_guilt_meter_low_guilt_result():
    result = guilt_meter("popcorn", 1)

    assert isinstance(result, str)
    assert "popcorn" in result.lower()
    assert "virtually saintly" in result.lower()
    assert "savory energy" in result.lower()


def test_guilt_meter_alias_and_sweet_result():
    result = guilt_meter("cookie", 2)

    assert "cookies" in result.lower()
    assert "a tiny indulgence" in result.lower()
    assert "sweet energy" in result.lower()


def test_guilt_meter_high_guilt_result():
    result = guilt_meter("donuts", 6)

    assert "donuts" in result.lower()
    assert "full snack confession required" in result.lower()
    assert "sweet energy" in result.lower()


def test_guilt_meter_midrange_result():
    result = guilt_meter("nachos", 4)

    assert "nachos" in result.lower()
    assert "the guilt meter is blinking" in result.lower()
    assert "savory energy" in result.lower()


def test_guilt_meter_invalid_inputs():
    with pytest.raises(ValueError):
        guilt_meter("", 1)

    with pytest.raises(ValueError):
        guilt_meter("broccoli", 1)

    with pytest.raises(TypeError):
        guilt_meter("chips", "two")
