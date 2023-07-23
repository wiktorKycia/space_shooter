import pygame
from code.bullets import *
from code.bullets2 import *
from code.cannons import *
from code.enemies import *
from code.levels import *
from code.maneuvering_cannons import *
from code.other import *
from code.player import *
from code.ships import *
from code.two_players import *
from code.UI import *


class MainObject(object):
    def __init__(self):
        pass

    def tick(self):
        pass

    def draw(self):
        pass

class StaticObject(MainObject):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.x = x
        self.y = y

class UnClickable(StaticObject):
    def __init__(self, game, x, y, surf):
        super().__init__(game, x, y)
        self.surf = surf

    def draw(self):
        self.game.screen.blit(self.surf, (self.x, self.y))

class TextObject(UnClickable):
    def __init__(self, game, x, y, text, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        self.text = self.write(text, font_size, color, font_style, is_centered)
        super().__init__(game, x, y, self.text)

    def write(self, text, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        font = pygame.font.SysFont(font_style, font_size)
        rend = font.render(text, True, color)
        if is_centered is True:
            self.x = (self.game.width - rend.get_rect().width) / 2
            self.y = (self.game.height - rend.get_rect().height) / 2
        return rend