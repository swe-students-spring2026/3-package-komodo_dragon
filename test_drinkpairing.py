import pytest

from drinkpairing import drink_pairing


def test_drink_pairing_hot_pairing():
    result = drink_pairing("cookies", "hot")

    assert isinstance(result, str)
    assert "cookies" in result.lower()
    assert "hot cocoa" in result.lower()


def test_drink_pairing_cold_alias_and_normalization():
    result = drink_pairing("  CHIPS  ", " iced ")

    assert "chips" in result.lower()
    assert "iced tea" in result.lower()
    assert "cold" in result.lower()


def test_drink_pairing_alternate_supported_snack():
    result = drink_pairing("pretzels", "warm")

    assert isinstance(result, str)
    assert "pretzels" in result.lower()
    assert "spiced cider" in result.lower()


def test_drink_pairing_invalid_snack():
    with pytest.raises(ValueError):
        drink_pairing("broccoli", "cold")


def test_drink_pairing_invalid_temperature():
    with pytest.raises(ValueError):
        drink_pairing("cookies", "lukewarm")


def test_drink_pairing_empty_snack():
    with pytest.raises(ValueError):
        drink_pairing("   ", "cold")


def test_drink_pairing_invalid_snack_type():
    with pytest.raises(TypeError):
        drink_pairing(42, "cold")


def test_drink_pairing_invalid_temperature_type():
    with pytest.raises(TypeError):
        drink_pairing("cookies", 42)


def test_drink_pairing_accepts_snack_alias():
    result = drink_pairing("cookie", "cool")

    assert "cookies" in result.lower()
    assert "cold milk" in result.lower()
    assert "sweet match" in result.lower()


def test_drink_pairing_supports_donuts():
    result = drink_pairing("donuts", "hot")

    assert "donuts" in result.lower()
    assert "spiced latte" in result.lower()
    assert "sweet match" in result.lower()


def test_drink_pairing_supports_nachos():
    result = drink_pairing("nachos", "cold")

    assert "nachos" in result.lower()
    assert "lime soda" in result.lower()
    assert "savory match" in result.lower()
