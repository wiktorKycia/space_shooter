import pygame.time
from bullets import *
import os
class BaseEnemy(object):
    def __init__(self, game, imagepath, x, y, slip, mov_force, mass, shot_force, barrel_lenght):
        self.game = game
        self.x = x
        self.y = y

        self.image = imagepath
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.slip = slip
        self.movforce = mov_force
        self.mass = mass
        self.shotforce = shot_force
        self.barrel = barrel_lenght

        self.acc = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(x, y)

        self.clock = 0
        self.bullets = []

    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        self.clock += pygame.time.Clock().tick(self.game.tps_max) / 1000

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x - self.width/2, self.pos.y - self.height/2))

class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.image.load(os.path.join("./enemies/Enemy1.png"))
        super().__init__(self.game, self.image, x, y , 0.99, 1000, 500, 2200, 50)

    def tick(self):
        super().tick()
