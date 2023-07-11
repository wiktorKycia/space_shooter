import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBulletsLauncher:
    def __init__(self, game, ship, translation: Vector2, force: int, interval: float, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key
