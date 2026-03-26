import random


def recommend_snack(mood, crunch_level):
    '''
    Recomends a snack based on mood and crunch
    
    Enter as params 
    crunch int 1-10 crunch level 10 is most crunchy
    mood string : happy sad stressed sleepy bored
              
    returns a snack recomendation as a string       

    '''
    if not isinstance(mood, str):
        raise TypeError("mood must be a string")

    if not isinstance(crunch_level, int):
        raise TypeError("crunch_level must be an integer")

    if not 1 <= crunch_level <= 10:
        raise ValueError("crunch_level must be between 1 and 10")

    mood = mood.strip().lower()
     
    snack_map = {
        "happy": {
            "low": ["mini muffins", "banana bread bites", "soft pretzels"],
            "medium": ["goldfish crackers", "cheese puffs", "butter cookies"],
            "high": ["potato chips", "pretzel sticks", "caramel popcorn"],
                },
        "sad": {
            "low": ["warm brownie", "pudding cup", "soft cookies"],
            "medium": ["graham crackers", "animal crackers", "waffle crisps"],
            "high": ["kettle chips", "crispy chocolate wafers", "nacho chips"],
                },
        "stressed": {
            "low": ["yogurt", "mochi", "soft granola bar"],
            "medium": ["trail mix", "crackers", "rice cakes"],
            "high": ["almonds", "pretzels", "wasabi peas"],
                     },
        "sleepy": {
            "low": ["banana slices", "toast bites", "mini pancakes"],
            "medium": ["granola clusters", "cheddar crackers", "popcorn"],
            "high": ["corn nuts", "kettle popcorn", "crispy pita chips"],
                     },
        "bored": {
            "low": ["gummy bears", "marshmallows", "donuts"],
            "medium": ["cookies", "trail mix", "crackers"],
            "high": ["takis", "lays chips", "pretzels"],
                    },
    }
    if mood not in snack_map:
        valid_moods = ", ".join(snack_map.keys())
        raise ValueError(f"Invalid mood. Choose from: {valid_moods}")

    if crunch_level <= 3:
        crunch_category = "low"
    elif crunch_level <= 7:
        crunch_category = "medium"
    else:
        crunch_category = "high"

    snack = random.choice(snack_map[mood][crunch_category])
    return f"The Snack Oracle senses your {mood} energy... you should eat {snack}."

def snack_prophecy(day, hunger_level):
    """
    Gives a mystical snack prophecy based on the day and hunger level 

    Takes in 
    day string: Day of the week.
    hunger_level int: Hunger level from 1 to 10.

    Returns a string A snack prophecy.
    """
    if not isinstance(day, str):
        raise TypeError("day must be a string")

    if not isinstance(hunger_level, int):
        raise TypeError("hunger_level must be an integer")

    if not 1 <= hunger_level <= 10:
        raise ValueError("hunger_level must be between 1 and 10")

    day = day.strip().lower()

    valid_days = {
        "monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"
    }
    if day not in valid_days:
        raise ValueError("day must be a valid day of the week")

    if hunger_level <= 3:
        hunger_message = "A light nibble shall satisfy your spirit."
    elif hunger_level <= 7:
        hunger_message = "A worthy snack is in your near future."
    else:
        hunger_message = "The oracle foresees a feast-level craving approaching fast."

    day_prophecies = {
        "monday": "Beware the bland pantry. Seek flavor boldly.",
        "tuesday": "Crunch and destiny walk together today.",
        "wednesday": "Midweek wisdom points toward something cheesy.",
        "thursday": "A salty blessing is on the horizon.",
        "friday": "Joy arrives in the form of an elite snack.",
        "saturday": "Today is ruled by indulgence and extra portions.",
        "sunday": "Comfort food energy surrounds you.",
    }
    return f"{day.capitalize()} prophecy: {day_prophecies[day]} {hunger_message}"



def snack_vibe(weather, mood):
    if not isinstance(weather, str) or not isinstance(mood, str):
        raise TypeError("Inputs must be strings")

    weather = weather.strip().lower()
    mood = mood.strip().lower()

    weather_map = {
        "rainy": ["hot chocolate + cookies"],
        "sunny": ["ice cream"],
        "cloudy": ["coffee + muffin"],
        "cold": ["hot cocoa"],
    }

    mood_map = {
        "happy": ["celebratory snacks"],
        "sad": ["comfort food"],
        "stressed": ["light snacks"],
        "bored": ["random snacks"],
    }

    if weather not in weather_map:
        raise ValueError("Invalid weather")

    if mood not in mood_map:
        raise ValueError("Invalid mood")

    return f"Vibe: {mood_map[mood][0]} with {weather_map[weather][0]}"


def calorie_denial(snack, quantity):
    if not isinstance(snack, str):
        raise TypeError("snack must be a string")
    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")

    if quantity <= 0:
        raise ValueError("quantity must be positive")

    if quantity <= 2:
        level = "barely counts 😌"
    elif quantity <= 5:
        level = "we're still okay 😅"
    else:
        level = "no regrets 🔥"

    return f"{quantity} {snack}(s): {level}"


def snack_compatibility(snack1, snack2):
    if not isinstance(snack1, str) or not isinstance(snack2, str):
        raise TypeError("Inputs must be strings")

    snack1 = snack1.lower().strip()
    snack2 = snack2.lower().strip()

    pairings = {
        "chips": ["salsa", "dip"],
        "cookies": ["milk", "coffee"],
        "pizza": ["soda", "beer"],
    }

    if snack1 == snack2:
        return "Perfect match 💯"

    if snack1 in pairings and snack2 in pairings[snack1]:
        return "Great pairing 🔥"

    if snack2 in pairings and snack1 in pairings[snack2]:
        return "Great pairing 🔥"

    return "Unusual combo 🤔"