class Board:
    def __init__(self):
        self.board_field = []

    def add_left(self, card):
        self.board_field.insert(0, card)

    def add_right(self, card):
        self.board_field.append(card)
