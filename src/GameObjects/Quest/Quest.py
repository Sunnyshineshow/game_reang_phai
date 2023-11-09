import json, random
from src.GameObjects.Card.Card import Card
from src.GameObjects.Card.CardType import CardType
from src.GameObjects.Card.CardAttribute.DrinkAttribute import DrinkAttribute
from src.GameObjects.Card.CardAttribute.FoodAttribute import FoodAttribute
from src.GameObjects.Card.CardAttribute.SweetAttribute import SweetAttribute
from src.GameObjects.Card.CardAttribute.FruitAttribute import FruitAttribute

"""
Summary:

Quest Structure
Name: Name of the Quest
QuestCode: Code of the quest and its attribute number as follows

Fo - Food
Dr - Drink
Sw - Sweet
Fr - Fruit

Attribute number see CardAttribute in GameObject Section

Range: 
adjacent - near cards, bidirection
overall - all card in the field
"""


class Quest:
    def __init__(self, raw_quest):
        self.name = quest["name"]
        self.range = quest["range"].upper()

        # Render Area
        quest_code_overall = quest["questcode"].split(";")

        for q in quest_code_overall:
            card_type = ""
            card_attrib = ""
            if q[0:2] == "Fo":
                card_type = CardType.FOOD
            elif q[0:2] == "Dr":
                card_type = CardType.DRINK
            elif q[0:2] == "Fr":
                card_type = CardType.FRUIT
            elif q[0:2] == "Sw":
                card_type = CardType.SWEET
            else:
                print("Cannot render quest")
