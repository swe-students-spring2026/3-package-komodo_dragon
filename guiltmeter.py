"""Snack guilt meter readings."""


def guilt_meter(snack, quantity):
    """
    Rate the snack guilt level based on snack type and quantity.

    Args:
        snack (str): The snack being judged.
        quantity (int): How many servings were eaten.

    Returns:
        str: A playful guilt meter reading.
    """
    if not isinstance(snack, str):
        raise TypeError("snack must be a string")

    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")

    snack = snack.strip().lower()

    if not snack:
        raise ValueError("snack must not be empty")

    if quantity <= 0:
        raise ValueError("quantity must be positive")

    snack_aliases = {
        "chip": "chips",
        "cookie": "cookies",
        "cracker": "crackers",
        "donut": "donuts",
    }
    snack = snack_aliases.get(snack, snack)

    guilt_weights = {
        "chips": 2,
        "cookies": 3,
        "popcorn": 1,
        "pretzels": 1,
        "brownie": 4,
        "crackers": 1,
        "donuts": 4,
        "nachos": 3,
        "muffins": 2,
        "pizza": 3,
    }

    if snack not in guilt_weights:
        valid_snacks = ", ".join(sorted(guilt_weights.keys()))
        raise ValueError(f"Unsupported snack. Choose from: {valid_snacks}")

    score = quantity + guilt_weights[snack]

    if score <= 2:
        verdict = "virtually saintly"
    elif score <= 5:
        verdict = "a tiny indulgence"
    elif score <= 8:
        verdict = "the guilt meter is blinking"
    else:
        verdict = "full snack confession required"

    snack_style = "sweet" if snack in {"cookies", "brownie", "donuts", "muffins"} else "savory"
    return (
        f"The Snack Oracle rates {quantity} serving(s) of {snack} as {verdict}. "
        f"It carries strong {snack_style} energy."
    )
