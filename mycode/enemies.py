import pygame.time
import pygame.math
import mycode
from mycode import *
from mycode.other import *
from mycode.bullets import *
from mycode.cannons import *
from mycode.Behaviors import *
from mycode.slot import Slot
import os
import random


class BaseEnemy(Shooting):
    def __init__(self, game, x, y, path, mass, max_speed, force, hp_amount, hp_width=50, hp_height=10, hp_relative=True,
                 slip=0.98, scale=1.0):
        super().__init__(game, x, y, path, mass, max_speed, -force, hp_amount, hp_width=hp_width, hp_height=hp_height,
                         hp_relative=hp_relative, slip=slip, scale=scale)
        self.move_clock = 0
        self.slots = []
        self.is_shooting = True

    def tick(self):
        super().tick()

        for slot in self.slots:
            slot.tick()

        if self.hp.hp <= 0:
            for slot in self.slots:
                self.game.menuHandler.currentMenu.other_bullets.extend(slot.weapon.bullets)
            self.game.menuHandler.currentMenu.enemies.remove(self)

    def draw(self):
        super().draw()
        for slot in self.slots:
            slot.draw()


class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy1.png",
            mass=50,
            max_speed=50,
            force=500,
            hp_amount=20
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )

class Enemy2(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy2.png",
            mass=75,
            max_speed=120,
            force=350,
            hp_amount=45
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )

class Enemy3(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy3.png",
            mass=250,
            max_speed=100,
            force=1000,
            hp_amount=100
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(-22, 10), self.is_shooting, KineticMedium),
                Slot(game, self, Vector2(22, 10), self.is_shooting, KineticMedium)
            ]
        )


class Bouncer1(BaseEnemy):
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
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 0), self.is_shooting, KineticLight)
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


class Bouncer2(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(
            game, x, y,
            "./enemies/bouncer2.png",
            mass=6,
            max_speed=200,
            force=2500,
            hp_amount=35,
            scale=3.0
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )
        self.destination_x = random.randint(0, 750)
        self.destination_y = random.randint(0, 350)
        self.dest_clock = 0

        self.behavior = Behavior(self.game, self)

    def reset_destination_points(self):
        self.destination_x = random.randint(0, 750)
        self.destination_y = random.randint(0, 350)

    def do_move(self, x, y):
        angle = 0
        if self.pos.x < x and self.pos.y < y:  # top left
            angle = random.randint(91, 180)
        if self.pos.x > x and self.pos.y < y:  # top right
            angle = random.randint(180, 270)
        if self.pos.x < x and self.pos.y > y:  # bottom left
            angle = random.randint(1, 90)
        if self.pos.x > x and self.pos.y > y:  # bottom right
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
        # self.dest_clock += self.game.dt
        # if self.dest_clock > 5.0:
        #     self.reset_destination_points()
        self.behavior.tick()

        if self.move_clock > 0.5:
            self.move_clock = 0
            self.do_move(self.destination_x, self.destination_y)
        super().tick()
