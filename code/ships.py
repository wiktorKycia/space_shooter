import pygame
from pygame import mixer
from pygame.math import Vector2
import os
from code import *
from code.other import *
from code.cannons import *
from code import ShootingUp

mixer.init()


class PlayableShip(ShootingUp):
    def __init__(self, game, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, slip=0.98, scale=1.0):
        size = game.screen.get_size()
        super().__init__(game, size[0]/2, size[1]/2, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, False, slip, scale)
        self.guns = []
        self.level = 1

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.force))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.force))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.force, 0))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.force, 0))
        if pressed[pygame.K_LSHIFT]:
            self.current_slip = 0.8
        else:
            self.current_slip = self.slip

        for gun in self.guns:
            gun.tick()
            for bullet in gun.bullets:
                for enemy in self.game.enemies:
                    if bullet.check_collision(enemy):
                        gun.bullets.remove(bullet)
                        energy = (bullet.mass * bullet.vel * bullet.vel) / 2
                        enemy.hp.get_damage(energy)
                        if enemy.hp.hp <= 0:
                            for gunE in enemy.guns:
                                self.game.other_bullets.extend(gunE.bullets)
                            self.game.enemies.remove(enemy)
                            break


        super().tick()

    def draw(self):
        super().draw()
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox, 1)
        for gun in self.guns:
            for bullet in gun.bullets:
                bullet.draw()



class Ship1(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_1.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=4000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, -20), self.force, key=pygame.K_KP_1)
            ]
        )

class Ship2(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_2.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=4000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, -20), self.force, key=pygame.K_KP_1)
            ]
        )

class Ship3(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_3.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=4000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, -20), self.force, key=pygame.K_KP_1)
            ]
        )

class Ship4(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_4.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=4000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, -20), self.force, key=pygame.K_KP_1)
            ]
        )

class Ship5(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_5.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=4000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.guns.extend(
            [
                LaserLight(game, self, Vector2(0, -20), self.force, key=pygame.K_KP_1)
            ]
        )