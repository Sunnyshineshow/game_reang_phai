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
        self.disc_image = None

        if self.type == CardType.FOOD:
            self.image = food_image_list[self.attribute.value]
            self.disc_image = discs_image_list[0]
        elif self.type == CardType.SWEET:
            self.image = sweet_image_list[self.attribute.value]
            self.disc_image = discs_image_list[1]
        elif self.type == CardType.DRINK:
            self.image = drink_image_list[self.attribute.value]
            self.disc_image = discs_image_list[2]
        elif self.type == CardType.FRUIT:
            self.image = fruit_image_list[self.attribute.value]
            self.disc_image = discs_image_list[3]
        elif self.type == CardType.NONE:
            self.image = none_image_list[0]
            self.disc_image = discs_image_list[4]

    def render(self, screen, x, y):
        if self.disc_image:
            screen.blit(self.disc_image, (int(x), int(y)))
        if self.type == CardType.FOOD:
            screen.blit(self.image, (int(x), int(y + 10)))
        else:
            screen.blit(self.image, (int(x), int(y)))

    def view_card(self):
        return "Card Type:", self.type, ", Card Attribute:", self.attribute
