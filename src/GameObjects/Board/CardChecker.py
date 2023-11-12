from src.GameObjects.Card.Card import Card


def check_order(previous_card, next_card):
    if previous_card.type.value == 0:
        return True

    if next_card.type.value == 0:
        return True

    if previous_card.type.value == 4 and next_card.type.value == 1:
        return True

    return previous_card.type.value <= next_card.type.value
