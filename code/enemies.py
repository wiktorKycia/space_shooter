import pygame.time
import pygame.math
import code
from code import *
from code.other import *
from code.bullets import *
import os

class BaseEnemy(ShootingDownNoMove):
    def __init__(self, game, x, y, path, force, hp_amount, hp_width=50, hp_height=10):
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
        super().__init__(self.game, x, y, self.path, force=1000, hp_amount=500000)

    def tick(self):
        super().tick()
        if self.clock >= 1.0:
            self.clock = 0
            bullet = EnergyGunBullet(self.game, self.pos.x-22, self.pos.y, self.force)
            bullet1 = EnergyGunBullet(self.game, self.pos.x+22, self.pos.y, self.force)
            self.add_bullet(bullet)
            self.add_bullet(bullet1)

import random

class MovingEnemy(ShootingDown):
    def __init__(self, game, x, y, path, mass, max_speed, force, hp_amount, hp_width=50, hp_height=10):
        super().__init__(game, x, y, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_relative=True, slip=0.99)
        self.move_clock = 0


class Bouncer1(MovingEnemy):
    def __init__(self, game, x, y):
        super().__init__(
            game, x, y,
            "./enemies/bouncer1.png",
            mass=60,
            max_speed=200,
            force=1500,
            hp_amount=2000000
        )

    def do_move(self):
        angle = 0
        if self.pos.x < 350 and self.pos.y < 150: #top left
            angle = random.randint(1, 89)
        if self.pos.x > 350 and self.pos.y < 150: #top right
            angle = random.randint(1, 89)
        if self.pos.x < 350 and self.pos.y > 150: # bottom left
            angle = random.randint(1, 89)
        if self.pos.x > 350 and self.pos.y > 150: # bottom right
            angle = random.randint(1, 89)

        if angle > 180:
            angle = -angle
        if angle < -180:
            angle = -angle

        self.vel.rotate_ip(angle)
        self.add_force(Vector2(0, self.force))

    def tick(self):
        self.hp.x = self.pos.x
        self.hp.y = self.pos.y - 50
        self.move_clock += self.game.dt
        if self.move_clock > 0.5:
            self.move_clock = 0
            self.do_move()
        super().tick()