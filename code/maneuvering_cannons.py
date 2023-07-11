import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBulletsLauncher:
    def __init__(self, game, ship, translation: Vector2, force: int, interval: float, barrel_length, key=pygame.K_SPACE):