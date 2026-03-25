"""Drink pairing recommendations for snacks."""


def drink_pairing(snack, temperature):
    """
    Recommend a drink to pair with a snack.

    Args:
        snack (str): The snack to pair with a drink.
        temperature (str): The preferred drink temperature.

    Returns:
        str: A Snack Oracle drink recommendation.
    """
    if not isinstance(snack, str):
        raise TypeError("snack must be a string")

    if not isinstance(temperature, str):
        raise TypeError("temperature must be a string")

    snack = snack.strip().lower()
    temperature = temperature.strip().lower()

    if not snack:
        raise ValueError("snack must not be empty")

    temperature_aliases = {
        "hot": "hot",
        "warm": "hot",
        "cold": "cold",
        "cool": "cold",
        "iced": "cold",
    }

    if temperature not in temperature_aliases:
        valid_temperatures = ", ".join(sorted(temperature_aliases.keys()))
        raise ValueError(
            f"temperature must be one of: {valid_temperatures}"
        )

    pairings = {
        "chips": {"hot": "tomato soup", "cold": "iced tea"},
        "cookies": {"hot": "hot cocoa", "cold": "cold milk"},
        "popcorn": {"hot": "chai latte", "cold": "sparkling lemonade"},
        "pretzels": {"hot": "spiced cider", "cold": "lemonade"},
        "brownie": {"hot": "coffee", "cold": "vanilla milkshake"},
        "crackers": {"hot": "herbal tea", "cold": "sparkling water"},
        "pizza": {"hot": "black tea", "cold": "soda"},
    }

    if snack not in pairings:
        valid_snacks = ", ".join(sorted(pairings.keys()))
        raise ValueError(f"Unsupported snack. Choose from: {valid_snacks}")

    normalized_temperature = temperature_aliases[temperature]
    drink = pairings[snack][normalized_temperature]
    return (
        f"The Snack Oracle pairs {snack} with {drink} "
        f"when the drink should be {normalized_temperature}."
    )
