import pygame
from pygame.math import *

class ManeuveringBullet:
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
