from src.GameState.BaseState import BaseState
import pygame, sys
from src.Utility.constants import *
from src.Utility.Dependency import *


class GameOverState(BaseState):
    def __init__(self, state_manager):
        super(GameOverState, self).__init__(state_manager)
        # start = 1,       ranking = 2
        self.option = 1

        self.menu_change_sound = pygame.mixer.Sound("sounds/paddle_hit.wav")
        self.confirm_sound = pygame.mixer.Sound("sounds/confirm.wav")
        self.medium_font = pygame.font.Font("./fonts/font.ttf", 48)
        self.large_font = pygame.font.Font("./fonts/font.ttf", 96)

    def Exit(self):
        pass

    def Enter(self, params):
        # self.high_scores = params["high_scores"]
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if self.option == 1:
                        self.option = 2
                    else:
                        self.option = 1
                    self.menu_change_sound.play()
                if event.key == pygame.K_RETURN:
                    self.confirm_sound.play()

                    if self.option == 1:
                        self.state_machine.Change("start", {})
                    else:
                        self.state_machine.Change("menu", {})

    def render(self, screen):
        # title
        screen.fill((0, 0, 0))
        screen.blit(gameover_bg, (0, 0))
        screen.blit(
            gameover_logo, gameover_logo.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        )

        retry_sprite = retry_image_list[0]
        main_menu_sprite = main_menu_image_list[0]

        if self.option == 1:
            retry_sprite = retry_image_list[1]
            main_menu_sprite = main_menu_image_list[0]

        if self.option == 2:
            retry_sprite = retry_image_list[0]
            main_menu_sprite = main_menu_image_list[1]

        screen.blit(
            retry_sprite,
            retry_sprite.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 90)),
        )
        screen.blit(
            main_menu_sprite,
            main_menu_sprite.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 230)),
        )
