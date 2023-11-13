class Hand:
    def __init__(self):
        self.hand_field = []

    def add_card_to_hand(self, card):
        self.hand_field.append(card)

    def remove_card_from_hand(self, card):
        self.hand_field.remove(card)
        return card

    def view_hand(self):
        return self.hand_field

    def clear_hand(self):
        self.hand_field = []
