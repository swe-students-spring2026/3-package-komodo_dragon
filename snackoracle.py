import random


def recommend_snack(mood, crunch_level):
    '''
    Recomends a snack based on mood and crunch
    
    Enter as params 
    crunch (int) 1-10 crunch level 10 is most crunchy
    mood (str) : happy sad stressed sleepy bored
              
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
