import pygame, sys, math
from pygame import mixer
from src.Utility.constants import *

from src.GameObjects.Card.CardDrawer import CardDrawer
from src.GameObjects.Board.Board import Board
from src.GameObjects.Hand.Hand import Hand
from src.GameObjects.Quest.QuestPool import QuestPool
from src.GameState.StateMachine import StateMachine
from src.GameState.StartState import StartState


pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

music_channel = mixer.Channel(0)
music_channel.set_volume(0.2)


class MainGame:
    def __init__(self):
        self.max_frame_rate = 60
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.bg_image = pygame.image.load("./graphics/background.png")

        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))

        self.num_dup_images = math.ceil(WIDTH / self.bg_image.get_width()) + 1
        # print(self.bg_image.get_size(), self.num_dup_images)
        self.scroll = 0
        self.scroll_bg = False

        self.g_state_manager = StateMachine(self.screen)
        # Import the game state here
        states = {
            "start": StartState(self.g_state_manager),
        }
        self.g_state_manager.SetStates(states)

    def RenderBackground(self):
        if self.scroll_bg:
            i = 0
            while i < self.num_dup_images:
                main.screen.blit(
                    self.bg_image, (self.bg_image.get_width() * i + self.scroll, 0)
                )  # appending same images to the back
                i += 1
            self.scroll -= 6
            if abs(self.scroll) > self.bg_image.get_width():
                self.scroll = 0
        else:
            main.screen.blit(self.bg_image, (0, 0))

    def PlayGame(self):
        # self.bg_music.play(-1)
        clock = pygame.time.Clock()
        self.g_state_manager.Change(
            "start",
            {},
        )

        scroll = 0

        while True:
            pygame.display.set_caption(
                "breakout game running with {:d} FPS".format(int(clock.get_fps()))
            )
            dt = clock.tick(self.max_frame_rate) / 1000.0

            # input
            events = pygame.event.get()

            # update
            self.g_state_manager.update(dt, events)

            # bg render
            self.RenderBackground()
            # render
            self.g_state_manager.render()

            # screen update
            pygame.display.update()


if __name__ == "__main__":
    main = MainGame()

    main.PlayGame()


# print(QuestPool().random_quest())

# card_drawer = CardDrawer()
# board = Board()
# hand = Hand()

# for i in range(5):
#     hand.add_card_to_hand(card_drawer.draw())


# while True:
#     print("Board:")
#     for card in board.show_board():
#         print(card.view_card())
#     print()

#     print("Hand:")
#     for card in hand.view_hand():
#         print(card.view_card())
#     print()

#     inp = input("Action? <card Index, Left/Right>: ")

#     inp = inp.split(" ")

#     inp[0] = int(inp[0])

#     card_trans = hand.remove_card_from_hand(hand.view_hand()[inp[0]])

#     if inp[1].upper() == "LEFT":
#         if not board.add_left(card_trans):
#             print("Invalid Position, Try Again")
#             hand.add_card_to_hand(card_trans)

#     elif inp[1].upper() == "RIGHT":
#         if not board.add_right(card_trans):
#             print("Invalid Position, Try Again")
#             hand.add_card_to_hand(card_trans)
#     else:
#         print("WTF ARE YOU DOING??")
#         hand.add_card_to_hand(card_trans)

#     if len(hand.view_hand()) == 0:
#         exit(0)
