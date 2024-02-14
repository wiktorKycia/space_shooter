import pygame.time
import pygame.math
import mycode
from mycode import *
from mycode.other import *
from mycode.bullets import *
from mycode.cannons import *
import os

class BaseEnemy(ShootingDownNoMove):
    def __init__(self, game, x, y, path, force, hp_amount, hp_width=50, hp_height=10):
        super().__init__(game, x, y, path, force, hp_amount, hp_width, hp_height)
        self.guns = []
        self.is_shooting = True

    def tick(self):
        super().tick()
        for gun in self.guns:
            gun.tick()
            for bullet in gun.bullets:
                if bullet.check_collision(self.game.player.current_ship):
                    # energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                    self.game.player.current_ship.hp.get_damage(bullet.damage)
                    gun.bullets.remove(bullet)
                    del bullet

    def draw(self):
        super().draw()
        for gun in self.guns:
            for bullet in gun.bullets:
                bullet.draw()

class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy1.png"
        super().__init__(
            game, x, y, self.path, force=500, hp_amount=20
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, 10), self.force, key=self.is_shooting)
            ]
        )

    def tick(self):
        super().tick()

class Enemy2(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy2.png"
        super().__init__(
            game, x, y, self.path, force=350, hp_amount=45
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, 10), self.force, key=self.is_shooting)
            ]
        )

    def tick(self):
        super().tick()
        # if self.clock >= 1.5:
        #     self.clock = 0
        #     bullet = Kinetic9Bullet(self.game, self.pos.x, self.pos.y, self.force)
        #     self.add_bullet(bullet)

class Enemy3(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.path = "./enemies/Enemy3.png"
        super().__init__(self.game, x, y, self.path, force=1000, hp_amount=100)
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(-22, 10), self.force, key=self.is_shooting),
                LaserLight(game, self, Vector2(22, 10), self.force, key=self.is_shooting)
            ]
        )

    def tick(self):
        super().tick()
        # if self.clock >= 1.0:
        #     self.clock = 0
        #     bullet = EnergyGunBullet(self.game, self.pos.x-22, self.pos.y, self.force)
        #     bullet1 = EnergyGunBullet(self.game, self.pos.x+22, self.pos.y, self.force)
        #     self.add_bullet(bullet)
        #     self.add_bullet(bullet1)

import random

class MovingEnemy(ShootingDown):
    def __init__(self, game, x, y, path, mass, max_speed, force, hp_amount, hp_width=50, hp_height=10, scale=1.0):
        super().__init__(game, x, y, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_relative=True, slip=0.99, scale=scale)
        self.move_clock = 0
        self.guns = []
        self.bullets = []
        self.is_shooting = True

    def add_bullet(self, bullet):
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)

    def tick(self):
        super().tick()
        for gun in self.guns:
            gun.tick()
            for bullet in gun.bullets:
                if bullet.check_collision(self.game.player.current_ship):
                    # energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                    self.game.player.current_ship.hp.get_damage(bullet.damage)
                    gun.bullets.remove(bullet)
                    del bullet

    def draw(self):
        super().draw()
        for gun in self.guns:
            for bullet in gun.bullets:
                bullet.draw()


class Bouncer1(MovingEnemy):
    def __init__(self, game, x, y):
        super().__init__(
            game, x, y,
            "./enemies/bouncer1.png",
            mass=2,
            max_speed=200,
            force=1500,
            hp_amount=15,
            scale=3.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, 0), self.force, key=self.is_shooting)
            ]
        )

    def do_move(self):
        angle = 0
        if self.pos.x < 350 and self.pos.y < 150: # top left
            angle = random.randint(91, 180)
        if self.pos.x > 350 and self.pos.y < 150: # top right
            angle = random.randint(180, 270)
        if self.pos.x < 350 and self.pos.y > 150: # bottom left
            angle = random.randint(1, 90)
        if self.pos.x > 350 and self.pos.y > 150: # bottom right
            angle = random.randint(270, 360)
        if angle > 180:
            angle = -angle
        if angle < -180:
            angle = -angle
        self.add_force(Vector2(0, self.force))
        self.acc.rotate_ip(angle)

    def tick(self):
        self.hp.x = self.pos.x
        self.hp.y = self.pos.y - 50
        self.move_clock += self.game.dt
        if self.move_clock > 0.5:
            self.move_clock = 0
            self.do_move()
        super().tick()
        # if self.clock > 1.5:
        #     self.clock = 0
        #     bullet = KineticBullet(self.game, self.pos.x, self.pos.y, self.force)
        #     self.add_bullet(bullet)