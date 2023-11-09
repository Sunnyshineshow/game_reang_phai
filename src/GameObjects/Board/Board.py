from src.GameObjects.Card.CardAttribute.NoneAttribute import NoneAttribute
from src.GameObjects.Card.CardType import CardType
from src.GameObjects.Card.Card import Card


class Board:
    def __init__(self):
        self.board_field = [Card(CardType.NONE, NoneAttribute.NONE)]

    def add_left(self, card):
        self.board_field.insert(0, card)

    def add_right(self, card):
        self.board_field.append(card)

    def show_board(self):
        return self.board_field
