from src.Utility.CheckDirectionFrom import CheckDirectionFrom
from src.GameObjects.Card.CardType import CardType


def check_individual_quest(quest, board, direction_from):
    board_field = board.board_field
    quest_field = quest.condition

    if quest.range == "ADJACENT":
        if direction_from == CheckDirectionFrom.RIGHT:
            board_field = board_field[::-1]

        return len(board_field) >= len(quest_field) and all(
            board_field[i].type == quest_field[i].type for i in range(len(quest_field))
        )

    elif quest.range == "ALL":
        quest_types = {q.type for q in quest_field}
        count = sum(
            1 for b in board_field if b.type in quest_types and not b.is_in_combo
        )

        if len(quest_types) == count:
            return True

    print("Invalid Quest Range")
    return False


# Comes from...
# def check_individual_quest(quest, board, direction_from):
#     board_field = board.board_field
#     quest_field = quest.condition

#     if quest.range == "ADJACENT":
#         if direction == CheckDirectionFrom.RIGHT:
#             board_field = board_field[::-1]

#         if len(board_field) < len(quest_field):
#             return False

#         for i in range(len(quest_field)):
#             if board_field[i].type != quest_field[i].type:
#                 return False
#         return True

#     elif quest.range == "ALL":
#         count = 0
#         for i in range(len(board_field)):
#             for j in range(len(quest_field)):
#                 if board_field[i].type == quest_field[j].type:
#                     board_field[i].is_in_combo = True
#                     count += 1
#                     break

#         if len(quest_field) == count:
#             return True
#         else:
#             return False

#     else:
#         print("Invalid Quest Range")
#         return False
