from src.Utility.Dependency import *
from src.GameObjects.Card.CardDrawer import CardDrawer
from src.GameObjects.Board.Board import Board
from src.GameObjects.Hand.Hand import Hand
from src.GameObjects.Quest.QuestPool import QuestPool
from src.GameObjects.Quest.QuestBoard import QuestBoard
from src.GameState.StateMachine import StateMachine
from src.Utility.CheckDirectionFrom import CheckDirectionFrom
from src.GameState.StateMachine import StateMachine
from src.GameState.BaseState import BaseState
from src.Utility.constants import *
import pygame, sys


class DirectionSelectState(BaseState):
    def __init__(self, state_manager):
        super(DirectionSelectState, self).__init__(state_manager)

        self.medium_font = pygame.font.Font("./fonts/font.ttf", 48)
        self.large_font = pygame.font.Font("./fonts/font.ttf", 96)
        self.direction = 0

    def Enter(self, params):
        self.card_drawer = params["card_drawer"]
        self.board = params["board"]
        self.hand = params["hand"]
        self.pool = params["pool"]
        self.quest_board = params["quest_board"]
        self.quest_pool = params["quest_pool"]
        self.reshuffle = params["reshuffle"]
        self.direction = 0
        self.log = params["log"]

    def Exit(self):
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = 1

                if event.key == pygame.K_RIGHT:
                    self.direction = 2

                if event.key == pygame.K_a:
                    self.board.shift_right()

                if event.key == pygame.K_d:
                    self.board.shift_left()

                if event.key == pygame.K_ESCAPE:
                    self.state_machine.Change(
                        "standby",
                        {
                            "card_drawer": self.card_drawer,
                            "board": self.board,
                            "hand": self.hand,
                            "pool": self.pool,
                            "quest_board": self.quest_board,
                            "quest_pool": self.quest_pool,
                            "reshuffle": self.reshuffle,
                            "log": "",
                        },
                    )

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if self.direction != 0:
                        card_trans = self.hand.remove_card_from_hand(
                            self.hand.view_hand()[self.hand.hand_selection]
                        )

                        if self.direction == 1:
                            if not self.board.add_left(card_trans):
                                print("Invalid Position, Try Again")
                                self.hand.add_card_to_hand(card_trans)
                                self.state_machine.Change(
                                    "standby",
                                    {
                                        "card_drawer": self.card_drawer,
                                        "board": self.board,
                                        "hand": self.hand,
                                        "pool": self.pool,
                                        "quest_board": self.quest_board,
                                        "quest_pool": self.quest_pool,
                                        "reshuffle": self.reshuffle,
                                        "log": "Invalid Position, Try Again",
                                    },
                                )
                            else:
                                self.state_machine.Change(
                                    "process",
                                    {
                                        "card_drawer": self.card_drawer,
                                        "board": self.board,
                                        "hand": self.hand,
                                        "pool": self.pool,
                                        "quest_board": self.quest_board,
                                        "quest_pool": self.quest_pool,
                                        "reshuffle": self.reshuffle,
                                        "log": self.log,
                                    },
                                )

                        if self.direction == 2:
                            if not self.board.add_right(card_trans):
                                print("Invalid Position, Try Again")
                                self.hand.add_card_to_hand(card_trans)
                                self.state_machine.Change(
                                    "standby",
                                    {
                                        "card_drawer": self.card_drawer,
                                        "board": self.board,
                                        "hand": self.hand,
                                        "pool": self.pool,
                                        "quest_board": self.quest_board,
                                        "quest_pool": self.quest_pool,
                                        "reshuffle": self.reshuffle,
                                        "log": "Invalid Position, Try Again",
                                    },
                                )
                            else:
                                self.state_machine.Change(
                                    "process",
                                    {
                                        "card_drawer": self.card_drawer,
                                        "board": self.board,
                                        "hand": self.hand,
                                        "pool": self.pool,
                                        "quest_board": self.quest_board,
                                        "quest_pool": self.quest_pool,
                                        "reshuffle": self.reshuffle,
                                        "log": self.log,
                                    },
                                )

    def render(self, screen):
        screen.fill(SCREEN_COLOR)
        self.board.render(screen)
        self.hand.render(screen)
        self.reshuffle.render(screen, 0, 0)

        left_arrow = arrows_image_list[0]
        right_arrow = arrows_image_list[2]

        if self.direction == 1:
            left_arrow = arrows_image_list[1]
            right_arrow = arrows_image_list[2]
        elif self.direction == 2:
            left_arrow = arrows_image_list[0]
            right_arrow = arrows_image_list[3]

        screen.blit(left_arrow, left_arrow.get_rect(center=(WIDTH / 4, HEIGHT / 2)))
        screen.blit(
            right_arrow, right_arrow.get_rect(center=(WIDTH / 4 * 3, HEIGHT / 2))
        )
