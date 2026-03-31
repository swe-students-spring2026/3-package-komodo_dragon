import hashlib
import random
import argparse
import sys


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

"""
Estimate a late-night "snack risk" score based on how long you've been awake
and how strong your self-control is.
"""

# hours_awake (int): Number of hours the user has been awake (0-24).
# self_control (int): Self-control level (1-10). Higher means more control.

def midnight_snack_risk(hours_awake, self_control):

    if not isinstance(hours_awake, int):
        raise TypeError("hours_awake must be an integer")
    if not isinstance(self_control, int):
        raise TypeError("self_control must be an integer")

    if hours_awake < 0 or hours_awake > 24:
        raise ValueError("hours_awake must be between 0 and 24")
    if self_control < 1 or self_control > 10:
        raise ValueError("self_control must be between 1 and 10")

    # Higher self-control reduces the risk and more awake hours increases it.
    score = hours_awake * (11 - self_control)

    if score <= 15:
        risk_label = "Low"
        advice = "You are running on willpower and vibes."
    elif score <= 35:
        risk_label = "Moderate"
        advice = "Proceed carefully; keep water nearby."
    elif score <= 60:
        risk_label = "High"
        advice = "Your cravings have momentum. Choose wisely."
    else:
        risk_label = "Critical"
        advice = "Midnight snack emergency. Set a snack plan now."

    return (f"Midnight Snack Risk: {risk_label}. ")

"""
Reads user's aura based on their current emotion and favorite flavor
and returns a snack energy message.
"""
# current_emotion (str): happy, sad, stressed, sleepy, bored.
# favorite_flavor (str): The snack flavor the user loves.

def snack_aura_reading(current_emotion, favorite_flavor):

    if not isinstance(current_emotion, str):
        raise TypeError("current_emotion must be a string")
    if not isinstance(favorite_flavor, str):
        raise TypeError("favorite_flavor must be a string")

    emotion = current_emotion.strip().lower()
    flavor = favorite_flavor.strip()
    if not emotion:
        raise ValueError("current_emotion must not be empty")
    if not flavor:
        raise ValueError("favorite_flavor must not be empty")

    emotion_map = {
        "happy": {"descriptor": "radiant", "aura_word": "sunbeam yellow"},
        "sad": {"descriptor": "tender", "aura_word": "deep indigo"},
        "stressed": {"descriptor": "chaotic", "aura_word": "neon orange"},
        "sleepy": {"descriptor": "foggy", "aura_word": "lilac mist"},
        "bored": {"descriptor": "mischievous", "aura_word": "sparkly teal"},
    }
    if emotion not in emotion_map:
        valid = ", ".join(emotion_map.keys())
        raise ValueError(f"Invalid current_emotion. Choose from: {valid}")

    #Get an index from the flavor text.
    digest = hashlib.md5(flavor.lower().encode("utf-8")).hexdigest()
    idx = int(digest[:8], 16)

    energy_options = [
        "focus fizz",
        "comfort current",
        "confidence crunch",
        "calm constellation",
        "joy spark",
        "spice ignition",
    ]
    energy = energy_options[idx % len(energy_options)]

    aura_descriptor = emotion_map[emotion]["descriptor"]
    aura_word = emotion_map[emotion]["aura_word"]

    return (
        f"Your aura is {aura_descriptor} {aura_word} today. "
        f"You must consume {flavor}"
        f"Snack energy assigned: {energy}."
    )


def build_cli_parser():
    parser = argparse.ArgumentParser(
        prog="snackoracle",
        description="Snack Oracle: run snack predictions from the command line.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_recommend = sub.add_parser("recommend", help="Recommend a snack.")
    p_recommend.add_argument("--mood", required=True, help="happy|sad|stressed|sleepy|bored")
    p_recommend.add_argument("--crunch-level", required=True, type=int, help="1-10")

    p_prophecy = sub.add_parser("prophecy", help="Get a snack prophecy.")
    p_prophecy.add_argument("--day", required=True, help="monday...sunday")
    p_prophecy.add_argument("--hunger-level", required=True, type=int, help="1-10")

    p_vibe = sub.add_parser("vibe", help="Get a snack vibe.")
    p_vibe.add_argument("--weather", required=True, help="rainy|sunny|cloudy|cold")
    p_vibe.add_argument("--mood", required=True, help="happy|sad|stressed|bored")

    p_denial = sub.add_parser("denial", help="Calculate calorie denial level.")
    p_denial.add_argument("--snack", required=True, help="Snack name")
    p_denial.add_argument("--quantity", required=True, type=int, help="Positive integer")

    p_compat = sub.add_parser("compat", help="Check snack compatibility.")
    p_compat.add_argument("--snack1", required=True, help="First snack")
    p_compat.add_argument("--snack2", required=True, help="Second snack")

    p_risk = sub.add_parser("risk", help="Estimate midnight snack risk.")
    p_risk.add_argument("--hours-awake", required=True, type=int, help="0-24")
    p_risk.add_argument("--self-control", required=True, type=int, help="1-10")

    p_aura = sub.add_parser("aura", help="Read snack aura.")
    p_aura.add_argument("--current-emotion", required=True, help="happy|sad|stressed|sleepy|bored")
    p_aura.add_argument("--favorite-flavor", required=True, help="Your favorite snack flavor")

    return parser


def main(argv=None):
    """
    Command-line interface entrypoint

    ex. python -m snackoracle risk --hours-awake 12 --self-control 3
    """
    parser = build_cli_parser()
    args = parser.parse_args(argv)

    if args.command == "recommend":
        out = recommend_snack(args.mood, args.crunch_level)
    elif args.command == "prophecy":
        out = snack_prophecy(args.day, args.hunger_level)
    elif args.command == "vibe":
        out = snack_vibe(args.weather, args.mood)
    elif args.command == "denial":
        out = calorie_denial(args.snack, args.quantity)
    elif args.command == "compat":
        out = snack_compatibility(args.snack1, args.snack2)
    elif args.command == "risk":
        out = midnight_snack_risk(args.hours_awake, args.self_control)
    elif args.command == "aura":
        out = snack_aura_reading(args.current_emotion, args.favorite_flavor)
    else:
        parser.error("Unknown command")
        return 2

    print(out)
    return 0 #success


if __name__ == "__main__":
    main()