from src.GameObjects.Card.CardAttribute.NoneAttribute import NoneAttribute
from src.GameObjects.Card.CardType import CardType
from src.GameObjects.Card.Card import Card
from src.GameObjects.Board.CardChecker import check_order
from src.Utility.CheckDirectionFrom import CheckDirectionFrom


class Board:
    def __init__(self):
        self.board_field = [Card(CardType.NONE, NoneAttribute.NONE)]

    def add_left(self, card):
        if check_order(self.board_field[0], card):
            self.board_field.insert(0, card)
            return True
        return False

    def add_right(self, card):
        if check_order(self.board_field[-1], card):
            self.board_field.append(card)
            return True
        return False

    def show_board(self):
        return self.board_field

    def check_individual_quest(self, quest, direction_from):
        quest_field = quest.condition

        if quest.range == "ADJACENT":
            if len(self.board_field) < len(quest_field):
                return False
            if direction_from == CheckDirectionFrom.LEFT:
                for i in range(len(quest_field)):
                    if self.board_field[i] != quest_field[i]:
                        return False
                    if self.board_field[i].is_in_combo:
                        return False

                for i in range(len(quest_field)):
                    self.board_field[i].is_in_combo = True
            else:
                for i in range(len(quest_field)):
                    if (
                        self.board_field[len(self.board_field) - i - 1]
                        != quest_field[i]
                    ):
                        return False

                for i in range(len(quest_field)):
                    self.board_field[len(self.board_field) - i - 1].is_in_combo = True
            return True

        elif quest.range == "ALL":
            counted_arr = []
            for i in range(len(quest_field)):
                for j in range(len(self.board_field)):
                    if self.board_field[j].type == quest_field[i].type:
                        if self.board_field[j].is_in_combo:
                            continue
                        elif j in counted_arr:
                            continue
                        else:
                            counted_arr.append(j)
                            break

            if len(quest_field) == len(counted_arr):
                for i in counted_arr:
                    self.board_field[i].is_in_combo = True
                return True
            else:
                return False

        else:
            print("Invalid Quest Range")
            return False
