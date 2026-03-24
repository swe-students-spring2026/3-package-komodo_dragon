import pytest
from snackoracle import recommend_snack
from snackoracle import snack_prophecy
'''
 Testing for Recommend Snack Tests Bellow
'''
def test_recommend_snack_returns_string():
    result = recommend_snack("happy", 5)
    assert isinstance(result, str)
    assert "Snack Oracle" in result

def test_recommend_snack_low_crunch():
    result = recommend_snack("sad", 2)
    assert isinstance(result, str)
    
def test_recommend_snack_high_crunch():
    result = recommend_snack("bored", 9)
    assert isinstance(result, str)

def test_recommend_snack_invalid_mood():
    with pytest.raises(ValueError):
        recommend_snack("angry", 5)

def test_recommend_snack_invalid_crunch_low():
    with pytest.raises(ValueError):
        recommend_snack("happy", 0)

def test_recommend_snack_invalid_crunch_high():
    with pytest.raises(ValueError):
        recommend_snack("happy", 11)

def test_recommend_snack_wrong_crunch_type():
    with pytest.raises(TypeError):
        recommend_snack("happy", "high")

def test_recommend_snack_wrong_mood_type():
    with pytest.raises(TypeError):
        recommend_snack(5, 3)
"""
    Testing for snack prophecy 
"""
def test_snack_prophecy_returns_string():
    result = snack_prophecy("friday", 6)
    assert isinstance(result, str)
    assert "Friday prophecy" in result


def test_snack_prophecy_low_hunger():
    result = snack_prophecy("monday", 2)
    assert "light nibble" in result.lower()


def test_snack_prophecy_medium_hunger():
    result = snack_prophecy("wednesday", 5)
    assert "worthy snack" in result.lower()


def test_snack_prophecy_high_hunger():
    result = snack_prophecy("sunday", 10)
    assert "feast-level craving" in result.lower()


def test_snack_prophecy_invalid_day():
    with pytest.raises(ValueError):
        snack_prophecy("funday", 5)


def test_snack_prophecy_invalid_hunger_low():
    with pytest.raises(ValueError):
        snack_prophecy("monday", 0)


def test_snack_prophecy_invalid_hunger_high():
    with pytest.raises(ValueError):
        snack_prophecy("monday", 15)


def test_snack_prophecy_wrong_day_type():
    with pytest.raises(TypeError):
        snack_prophecy(123, 5)


def test_snack_prophecy_wrong_hunger_type():
    with pytest.raises(TypeError):
        snack_prophecy("monday", "high")