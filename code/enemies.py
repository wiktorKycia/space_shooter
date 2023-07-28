import pygame.time
import pygame.math
import code
from code import *
from code.other import *
from code.bullets import *
import os

class BaseEnemy(ShootingDownNoMove):
    def __init__(self, game,  x, y, path, force, hp_amount, hp_width=50, hp_height=5):
        super().__init__(game, x, y, path, force, hp_amount, hp_width, hp_height)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)

class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy1.png"
        super().__init__(
            game, x, y, self.path, force=500, hp_amount=100000
        )

    def tick(self):
        super().tick()
        if self.clock >= 2.0:
            self.clock = 0
            bullet = KineticBullet(self.game, self.pos.x, self.pos.y, self.force)
            self.add_bullet(bullet)

class Enemy2(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy2.png"
        super().__init__(
            game, x, y, self.path, force=350, hp_amount=250000
        )

    def tick(self):
        super().tick()
        if self.clock >= 1.5:
            self.clock = 0
            bullet = Kinetic9Bullet(self.game, self.pos.x, self.pos.y, self.force)
            self.add_bullet(bullet)

class Enemy3(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy3.png"
        super().__init__(self.game, self.image, x, y , 0.98, 540, 350, 1200, 6, 4500000)

    def tick(self):
        super().tick()
        if self.clock >= 1.0:
            self.clock = 0
            bullet = EnergyGunBullet(self.game, self.pos.x-22, self.pos.y, self.force)
            bullet1 = EnergyGunBullet(self.game, self.pos.x+22, self.pos.y, self.force)
            self.add_bullet(bullet)
            self.add_bullet(bullet1)
