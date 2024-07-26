import pygame
from pygame.math import *


class Behavior:
    def __init__(self, game, enemy):
        self.orders = []
        self.enemy = enemy
        self.game = game
        self.process_time = 0.5
        self.clock = 0

    def tick(self):
        self.clock += self.game.dt
