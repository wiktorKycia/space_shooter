import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBullet:
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
        self.game = game

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.force = force
        self.mass = mass

        self.color = color
        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)
