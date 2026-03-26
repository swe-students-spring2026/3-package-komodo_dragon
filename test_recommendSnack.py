import pytest
from snackoracle import recommend_snack
from snackoracle import snack_prophecy
from snackoracle import snack_vibe, calorie_denial, snack_compatibility, midnight_snack_risk, snack_aura_reading

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

"""
    Testing for snack vibe 
"""
def test_snack_vibe():
    assert "cookies" in snack_vibe("rainy", "sad")
    assert "ice cream" in snack_vibe("sunny", "happy")
    with pytest.raises(ValueError):
        snack_vibe("stormy", "happy")

"""
    Testing for calorie denial 
"""
def test_calorie_denial():
    result = calorie_denial("chips", 3)
    assert "chips" in result
    assert "we're still okay" in result

    with pytest.raises(ValueError):
        calorie_denial("chips", 0)

"""
    Testing for snack compatibility 
"""
def test_snack_compatibility():
    assert "Perfect" in snack_compatibility("chips", "chips")
    assert "Great pairing" in snack_compatibility("chips", "dip")
    assert isinstance(snack_compatibility("chips", "cookies"), str)


"""
Testing for midnight_snack_risk
"""


def test_midnight_snack_risk_low():
    result = midnight_snack_risk(hours_awake=1, self_control=10)
    assert isinstance(result, str)
    assert "Midnight Snack Risk" in result
    assert "Low" in result


def test_midnight_snack_risk_critical():
    result = midnight_snack_risk(hours_awake=20, self_control=1)
    assert isinstance(result, str)
    assert "Critical" in result
    assert "hours_awake=20" in result


def test_midnight_snack_risk_invalid_inputs():
    with pytest.raises(ValueError):
        midnight_snack_risk(hours_awake=-1, self_control=5)
    with pytest.raises(ValueError):
        midnight_snack_risk(hours_awake=25, self_control=5)
    with pytest.raises(TypeError):
        midnight_snack_risk(hours_awake="3", self_control=5)


"""
Testing for snack_aura_reading
"""


def test_snack_aura_reading_stressed_example_shape():
    result = snack_aura_reading(
        current_emotion="stressed",
        favorite_flavor="Flamin' Hot Cheetos",
    )
    assert isinstance(result, str)
    assert result.startswith("Your aura is")
    assert "You must consume" in result
    assert "Flamin' Hot Cheetos" in result


def test_snack_aura_reading_invalid_emotion():
    with pytest.raises(ValueError):
        snack_aura_reading(current_emotion="angry", favorite_flavor="chips")


def test_snack_aura_reading_type_errors():
    with pytest.raises(TypeError):
        snack_aura_reading(current_emotion=123, favorite_flavor="chips")
    with pytest.raises(TypeError):
        snack_aura_reading(current_emotion="happy", favorite_flavor=5)
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