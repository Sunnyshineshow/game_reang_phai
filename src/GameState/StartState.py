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
import pygame


class StartState(BaseState):
    def __init__(self, state_manager):
        super(StartState, self).__init__(state_manager)

        self.medium_font = pygame.font.Font("./fonts/font.ttf", 48)
        self.large_font = pygame.font.Font("./fonts/font.ttf", 96)

    def Enter(self, params):
        self.card_drawer = CardDrawer()
        self.board = Board()
        self.hand = Hand()
        self.pool = QuestPool()
        self.quest_board = QuestBoard()
        self.quest_pool = self.pool.get_pool()
        self.reshuffle_live = 3
        self.log = ""

        # GAME STARTING
        self.quest_board.add_quest_to_board(self.quest_pool[0])
        self.quest_board.add_quest_to_board(self.quest_pool[1])

        for i in range(5):
            self.hand.add_card_to_hand(self.card_drawer.draw())

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
                "log": self.log,
            },
        )

    def Exit(self):
        pass

    def update(self, dt, events):
        pass

    def render(self, screen):
        t_title = self.large_font.render("Loading", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        screen.fill(SCREEN_COLOR)
        screen.blit(t_title, rect)
