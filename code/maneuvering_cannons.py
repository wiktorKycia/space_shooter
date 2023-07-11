import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBulletsLauncher:
    def __init__(self, game, ship, translation: Vector2, force: int, interval: float, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key
        self.clock = 0

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval:
            self.clock = 0
