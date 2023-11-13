from src.GameObjects.Card.CardDrawer import CardDrawer
from src.GameObjects.Board.Board import Board
from src.GameObjects.Hand.Hand import Hand
from src.GameObjects.Quest.QuestPool import QuestPool
from src.GameObjects.Quest.QuestBoard import QuestBoard
from src.GameState.StateMachine import StateMachine
from src.Utility.CheckDirectionFrom import CheckDirectionFrom

# DEFINE
RESHUFFLE_LIFE = 3

# INITIALIZE
card_drawer = CardDrawer()
board = Board()
hand = Hand()
pool = QuestPool()
quest_board = QuestBoard()
arr = pool.get_pool()

# GAME STARTING
quest_board.add_quest_to_board(arr[0])
quest_board.add_quest_to_board(arr[1])


for i in range(5):
    hand.add_card_to_hand(card_drawer.draw())

# MAIN STATE
while True:
    # Show stuff
    print("Board:")
    for card in board.show_board():
        print(card.view_card())
    print()

    print("Hand:")
    for card in hand.view_hand():
        print(card.view_card())
    print()

    print("Quest:")
    for quest in quest_board.view_quest_board():
        print(quest)
    print()

    # Decide
    inp = input("Action? <card Index, Left/Right> or Reshuffle: ")

    inp = inp.split(" ")

    if inp[0].isalpha() and inp[0].upper() == "RESHUFFLE":
        if RESHUFFLE_LIFE <= 0:
            print("You can no longer reshuffle")
            continue

        RESHUFFLE_LIFE -= 1
        reshuffle_num = len(hand.view_hand())
        hand.clear_hand()
        for i in range(reshuffle_num):
            hand.add_card_to_hand(card_drawer.draw())

        print("Reshuffle Remaining:", RESHUFFLE_LIFE)
        continue

    if inp[0].isalpha() and inp[0].upper() == "END":
        break

    inp[0] = int(inp[0])

    card_trans = hand.remove_card_from_hand(hand.view_hand()[inp[0]])

    if inp[1].upper() == "LEFT":
        if not board.add_left(card_trans):
            print("Invalid Position, Try Again")
            hand.add_card_to_hand(card_trans)

    elif inp[1].upper() == "RIGHT":
        if not board.add_right(card_trans):
            print("Invalid Position, Try Again")
            hand.add_card_to_hand(card_trans)
    else:
        print("WTF ARE YOU DOING??")
        hand.add_card_to_hand(card_trans)

    quest_counter = 0
    for quest in quest_board.get_board():
        if board.check_individual_quest(quest, CheckDirectionFrom.LEFT):
            print("Quest Completed")
            quest_board.remove_quest_from_board(quest)
            quest_counter += 1
            for i in range(quest.reward):
                hand.add_card_to_hand(card_drawer.draw())
        elif board.check_individual_quest(quest, CheckDirectionFrom.RIGHT):
            print("Quest Completed")
            quest_board.remove_quest_from_board(quest)
            quest_counter += 1
            for i in range(quest.reward):
                hand.add_card_to_hand(card_drawer.draw())

    for i in range(quest_counter):
        quest_board.add_new_quest_to_board()

    if len(hand.view_hand()) == 0:
        print("Board:")
        for card in board.show_board():
            print(card.view_card())
        print()
        exit(0)
