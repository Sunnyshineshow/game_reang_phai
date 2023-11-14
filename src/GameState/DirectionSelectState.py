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
        self.reshuffle_live = params["reshuffle_live"]
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

                if event.key == pygame.K_SPACE:
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
                                        "reshuffle_live": self.reshuffle_live,
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
                                        "reshuffle_live": self.reshuffle_live,
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
                                        "reshuffle_live": self.reshuffle_live,
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
                                        "reshuffle_live": self.reshuffle_live,
                                        "log": self.log,
                                    },
                                )

    def render(self, screen):
        screen.fill(SCREEN_COLOR)
        self.board.render(screen)
        self.hand.render(screen)

        left_color = (255, 255, 255)
        right_color = (255, 255, 255)

        if self.direction == 1:
            left_color = (0, 255, 255)
        elif self.direction == 2:
            right_color = (0, 255, 255)

        t_left = self.large_font.render("LEFT", False, left_color)
        rect_left = t_left.get_rect(center=(WIDTH / 4, HEIGHT / 3))

        t_right = self.large_font.render("RIGHT", False, right_color)
        rect_right = t_right.get_rect(center=(WIDTH / 4 * 3, HEIGHT / 3))
        screen.blit(t_left, rect_left)
        screen.blit(t_right, rect_right)
