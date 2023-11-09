from src.CardDrawer import CardDrawer
from src.GameObjects.Board.Board import Board
from src.GameObjects.Hand.Hand import Hand

card_drawer = CardDrawer()
board = Board()
hand = Hand()

for i in range(5):
    hand.add_card_to_hand(card_drawer.draw())


while True:
    print("Board:")
    for card in board.show_board():
        print(card.view_card())
    print()

    print("Hand:")
    for card in hand.view_hand():
        print(card.view_card())
    print()

    inp = input("Action? <card Index, Left/Right>: ")

    inp = inp.split(" ")

    inp[0] = int(inp[0])

    card_trans = hand.remove_card_from_hand(hand.view_hand()[inp[0]])

    if inp[1].upper() == "LEFT":
        board.add_left(card_trans)
    elif inp[1].upper() == "RIGHT":
        board.add_right(card_trans)
    else:
        print("WTF ARE YOU DOING??")
        hand.add_card_to_hand(card_trans)

    if len(hand.view_hand()) == 0:
        exit(0)
