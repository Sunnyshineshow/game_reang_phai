from src.Utility.constants import *
import pygame
from src.Utility.Dependency import tray_image


class Hand:
    def __init__(self):
        self.hand_field = []
        self.width = 128
        self.height = 128
        self.x = 0
        self.y = 500
        self.dx = 0
        self.dy = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hand_selection = 0

    def update(self, dt):
        pass

    def add_card_to_hand(self, card):
        self.hand_field.append(card)

    def remove_card_from_hand(self, card):
        self.hand_field.remove(card)
        return card

    def view_hand(self):
        return self.hand_field

    def clear_hand(self):
        self.hand_field = []

    def hand_selecting(self, index):
        self.hand_selection = index

    def count_hand(self):
        return len(self.hand_field)

    def render(self, screen):
        screen.blit(tray_image, (0, HEIGHT / 6))
        for i in range(len(self.hand_field)):
            if i == self.hand_selection:
                self.hand_field[i].render(screen, 50 + i * 128, 500)
            else:
                self.hand_field[i].render(screen, 50 + i * 128, 550)
