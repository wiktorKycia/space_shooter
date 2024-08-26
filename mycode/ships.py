import math

import pygame
from pygame import mixer
from pygame.math import Vector2
import os
from mycode import *
from mycode.other import *
from mycode.cannons import *
from mycode import Shooting
from main import Game
mixer.init()


class PlayableShip(Shooting):
    def __init__(self, game, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, slip=0.98, scale=1.0):
        size = game.screen.get_size()
        super().__init__(game, size[0]/2, size[1]/2, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, False, slip, scale)
        # self.guns = []
        self.level = 1

    def getClosestEnemy(self):
        e = None
        d = math.inf
        for enemy in self.game.menuHandler.currentMenu.enemies:
            distance = math.sqrt(
                math.pow(abs(enemy.pos.x - self.pos.x), 2) + math.pow(abs(self.pos.y - enemy.pos.y), 2))
            if e is None or distance < d:
                d = distance
                e = enemy
        try:
            return e.pos.x, e.pos.y
        except AttributeError:
            return None

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        force = Vector2(0, 0)
        if pressed[pygame.K_w]:
            force.y = -self.force
            # self.add_force(Vector2(0, -self.force))
        if pressed[pygame.K_s]:
            # self.add_force(Vector2(0, self.force))
            force.y = self.force
        if pressed[pygame.K_d]:
            force.x = self.force
            # self.add_force(Vector2(self.force, 0))
        if pressed[pygame.K_a]:
            force.x = -self.force
            # self.add_force(Vector2(-self.force, 0))
        if pressed[pygame.K_LSHIFT]:
            self.current_slip = 0.8
        else:
            self.current_slip = self.slip

        if force != [0, 0]:
            self.add_force(force.clamp_magnitude(self.force))
        else:
            self.add_force(force)

        for gun in self.guns:
            gun.tick()
            for bullet in gun.bullets:
                if bullet.pos.y < 0:
                    gun.bullets.remove(bullet)
                    continue
                for enemy in self.game.menuHandler.currentMenu.enemies:
                    if bullet.check_collision(enemy):
                        enemy.hp.get_damage(bullet.damage)
                        if type(gun) != Laser1:
                            gun.bullets.remove(bullet)
                        # energy = (bullet.mass * bullet.vel * bullet.vel) / 2
                        if enemy.hp.hp <= 0:
                            for gunE in enemy.guns:
                                self.game.menuHandler.currentMenu.other_bullets.extend(gunE.bullets)
                            self.game.menuHandler.currentMenu.enemies.remove(enemy)
                            break
                        break


        super().tick()

    def draw(self):
        super().draw()
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox, 1)
        for gun in self.guns:
            for bullet in gun.bullets:
                bullet.draw()


class Slot:
    def __init__(self, game: Game, ship: PlayableShip, translation: Vector2, key: int):
        self.game = game
        self.ship = ship
        self.translation = translation
        self.key = key


class Ship1(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_1.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                KineticLight(game, self, Vector2(20, -20), key=pygame.K_KP_1),
                KineticLight(game, self, Vector2(-20, -20), key=pygame.K_KP_1)
            ]
        )

class Ship2(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_2.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                KineticMedium(game, self, Vector2(0, -20), key=pygame.K_KP_1)
            ]
        )

class Ship3(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_3.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                # KineticLight(game, self, Vector2(0, -20), key=pygame.K_KP_1)
                # ShotGun1(game, self, Vector2(0, -20), key=pygame.K_KP_1)
                Flamethrower1(game, self, Vector2(-10, -20), key=pygame.K_KP_0),
                Flamethrower1(game, self, Vector2(10, -20), key=pygame.K_KP_0)
            ]
        )

class Ship4(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_4.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                # KineticLight(game, self, Vector2(0, -20), key=pygame.K_KP_1)
                Laser1(game, self, Vector2(3, -25), key=pygame.K_KP_0),
                Laser1(game, self, Vector2(-5, -25), key=pygame.K_KP_0),
                Laser1(game, self, Vector2(25, 15), key=pygame.K_KP_0),
                Laser1(game, self, Vector2(-28, 15), key=pygame.K_KP_0)
            ]
        )

class Ship5(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_5.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                KineticLight(game, self, Vector2(0, -20), key=pygame.K_KP_1)
            ]
        )