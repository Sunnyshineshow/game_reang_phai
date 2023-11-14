import pygame
from src.Utility.Dependency import heart_image_list


class HeartRenderer:
    def __init__(self, level):
        self.image_list = heart_image_list
        self.level = level

    def change_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def render(self, screen, x, y):
        for i in range(3):
            if i < self.level:
                screen.blit(self.image_list[1], (int(x + i * 64), int(y)))
            else:
                screen.blit(self.image_list[0], (int(x + i * 64), int(y)))
