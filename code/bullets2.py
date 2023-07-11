import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBullet:
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
        self.game = game

        self.x = x
        self.y = y
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.width = width
        self.height = height

        self.force = force
        self.mass = mass
        acc = int(force / mass)
        self.acc = Vector2(0, -acc)

        self.color = color
        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)
