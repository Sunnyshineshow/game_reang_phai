class Card:
    def __init__(self, food_type, attribute):
        # food_type = Type of food
        self.type = food_type
        self.attribute = attribute

        # Is combo calculated for the card?
        self.is_in_combo = False

    def view_card(self):
        return "Card Type:", self.type, ", Card Attribute:", self.attribute
