from src.GameObjects.Card.CardType import CardType
from src.GameObjects.Card.CardAttribute.FoodAttribute import FoodAttribute
from src.GameObjects.Card.CardAttribute.DrinkAttribute import DrinkAttribute
from src.GameObjects.Card.CardAttribute.SweetAttribute import SweetAttribute
from src.GameObjects.Card.CardAttribute.FruitAttribute import FruitAttribute
from src.GameObjects.Card.Card import Card

import random


class CardDrawer:
    def __init__(self):
        self.card_types = []
        for card_type in CardType:
            if card_type == CardType.NONE or card_type == CardType.ANY:
                continue
            self.card_types.append(card_type)

    def available_types(self):
        return self.card_types

    def available_attribute(self, card_type):
        card_attribute = []
        if card_type == CardType.FOOD:
            for attribute in FoodAttribute:
                card_attribute.append(attribute)
        elif card_type == CardType.DRINK:
            for attribute in DrinkAttribute:
                card_attribute.append(attribute)
        elif card_type == CardType.SWEET:
            for attribute in SweetAttribute:
                card_attribute.append(attribute)
        elif card_type == CardType.FRUIT:
            for attribute in FruitAttribute:
                card_attribute.append(attribute)
        else:
            return 0

        return card_attribute

    def draw(self):
        card_type = random.choice(self.card_types)

        print(card_type)

        card_available_attributes = self.available_attribute(card_type)

        if card_available_attributes == 0:
            raise TypeError("Invalid Card Draw")

        card_attribute = random.choice(card_available_attributes)

        return Card(card_type, card_attribute)
