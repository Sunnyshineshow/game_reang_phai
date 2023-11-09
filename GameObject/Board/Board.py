class Board:
    def __init__(self):
        self.board = []

    def addLeft(self, card):
        self.board.insert(0, card)

    def addRight(self, card):
        self.board.append(card)
