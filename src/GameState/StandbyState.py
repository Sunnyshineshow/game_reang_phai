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


class StandbyState(BaseState):
    def __init__(self, state_manager):
        super(StandbyState, self).__init__(state_manager)

        self.small_font = pygame.font.Font("./fonts/font.ttf", 24)
        self.medium_font = pygame.font.Font("./fonts/font.ttf", 48)
        self.large_font = pygame.font.Font("./fonts/font.ttf", 96)
        self.option = 0

    def Enter(self, params):
        self.card_drawer = params["card_drawer"]
        self.board = params["board"]
        self.hand = params["hand"]
        self.pool = params["pool"]
        self.quest_board = params["quest_board"]
        self.quest_pool = params["quest_pool"]
        self.reshuffle = params["reshuffle"]
        self.option = 0
        self.log = params["log"]
        self.hand.hand_selecting(self.option)

    def Exit(self):
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.option <= 0:
                        self.option = 0
                    else:
                        self.option -= 1
                    self.hand.hand_selecting(self.option)

                if event.key == pygame.K_RIGHT:
                    if self.option >= self.hand.count_hand() - 1:
                        self.option = self.hand.count_hand() - 1
                    else:
                        self.option += 1
                    self.hand.hand_selecting(self.option)

                if event.key == pygame.K_a:
                    self.board.shift_right()

                if event.key == pygame.K_d:
                    self.board.shift_left()

                # Reshuffle
                if event.key == pygame.K_LCTRL:
                    if self.reshuffle.get_level() <= 0:
                        self.log = "You can no longer reshuffle"

                    else:
                        self.reshuffle.change_level(self.reshuffle.get_level() - 1)
                        reshuffle_num = self.hand.count_hand()
                        self.hand.clear_hand()
                        for i in range(reshuffle_num):
                            self.hand.add_card_to_hand(self.card_drawer.draw())

                        self.log = "Reshuffle Remaining: " + str(
                            self.reshuffle.get_level()
                        )

                if event.key == pygame.K_q:
                    self.state_machine.Change("gameover", {})

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.state_machine.Change(
                        "direction",
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

    def render(self, screen):
        screen.fill(SCREEN_COLOR)
        self.board.render(screen)
        self.hand.render(screen)
        self.quest_board.render(screen)
        self.reshuffle.render(screen, 0, 0)
        t_log = self.small_font.render(self.log, False, (255, 0, 0))
        rect_log = t_log.get_rect(center=(WIDTH / 2, HEIGHT / 4))

        screen.blit(t_log, rect_log)
