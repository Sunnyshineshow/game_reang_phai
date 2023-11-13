from src.Utility.Dependency import *
from src.GameObjects.Card.CardType import CardType

import random


class Card:
    def __init__(self, food_type, attribute):
        # food_type = Type of food
        self.type = food_type
        self.attribute = attribute

        # Is combo calculated for the card?
        self.is_in_combo = False

        self.image = None

        if self.type == CardType.FOOD:
            self.image = food_image_list[self.attribute.value]
        elif self.type == CardType.SWEET:
            self.image = sweet_image_list[self.attribute.value]
        elif self.type == CardType.DRINK:
            self.image = drink_image_list[self.attribute.value]
        elif self.type == CardType.FRUIT:
            self.image = fruit_image_list[self.attribute.value]
        elif self.type == CardType.NONE:
            self.image = none_image_list[0]

    def render(self, screen, x, y):
        screen.bilt(self.image, x, y)

    def view_card(self):
        return "Card Type:", self.type, ", Card Attribute:", self.attribute
