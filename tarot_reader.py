import random

# Tarot card list
TAROT_CARDS = [
    "The Fool", "The Magician", "The High Priestess", "The Empress",
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
    "Strength", "The Hermit", "Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

def draw_three_cards():
    """Randomly select 3 tarot cards."""
    return random.sample(TAROT_CARDS, 3)

def make_prompt(card_name):
    """Create a DALL·E 3 style prompt for the tarot card."""
    return (
        f"Tarot card illustration of '{card_name}'. "
        "Highly detailed, mystical, magical atmosphere, fantasy themed, ornate border, dramatic lighting."
    )
