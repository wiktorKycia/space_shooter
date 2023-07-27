import pygame
from pygame import mixer
from pygame.math import Vector2
import os
from code import *
from code.other import *
from code.cannons import *
from code.maneuvering_cannons import *
from code import ShootingUp

mixer.init()


class PlayableShip(ShootingUp):
    def __init__(self, game, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, slip=0.98):
        size = self.game.screen.get_size()
        super().__init__(game, size[0]/2, size[1]/2, path, mass, max_speed, force, hp_amount, hp_width, hp_height, hp_x, hp_y, False, slip)

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

        super().tick()

    def draw(self):
        super().draw()

class Ship0(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship0.png"
        self.hp = DeluxeHP(self.game, 500000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 120, 40, 250)
        self.cannon = KineticGun(self.game, self, Vector2(0, -10), self.force, 0.6)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
    def draw(self):
        super().draw()

class Ship1(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship1.png"
        self.hp = DeluxeHP(self.game, 1000000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 150, 100, 1000)
        # self.cannon = Blaster(self.game, self, Vector2(0, -20), self.force, 0.3)
        # self.cannon = Kinetic60Gun(self.game, self, Vector2(0, -20), self.force, 0.1)
        self.cannon = ManeuveringBulletsLauncher(
            game=self.game,
            ship=self,
            translation=Vector2(0, -30),
            force=self.force,
            interval=0.7,
            key=pygame.K_SPACE
        )
    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
    def draw(self):
        super().draw()

class Ship2(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship2.png"
        self.hp = DeluxeHP(self.game, 900000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 170, 75, 1250)
        self.cannon = Blaster(self.game, self, Vector2(27, -20), self.force, 0.35)
        self.cannon2 = Blaster(self.game, self, Vector2(-27, -20), self.force, 0.35)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
        self.cannon2.tick()
    def draw(self):
        super().draw()

class Ship3(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship3.png"
        self.hp = DeluxeHP(self.game, 2000000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 200, 200, 5000)
        self.cannon = Blaster(self.game, self, Vector2(-23, -30), self.force, 0.4)
        self.cannon2 = Blaster(self.game, self, Vector2(23, -30), self.force, 0.4)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
        self.cannon2.tick()
    def draw(self):
        super().draw()

class Ship4(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship4.png"
        self.hp = DeluxeHP(self.game, 3500000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 100, 500, 5000)
        self.cannon = Blaster(self.game, self, Vector2(-25, -35), self.force, 0.4)
        self.cannon2 = Blaster(self.game, self, Vector2(25, -35), self.force, 0.4)
        self.cannon3 = Blaster(self.game, self, Vector2(-47, -30), self.force, 0.4)
        self.cannon4 = Blaster(self.game, self, Vector2(47, -30), self.force, 0.4)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
        self.cannon2.tick()
        self.cannon3.tick()
        self.cannon4.tick()
    def draw(self):
        super().draw()

class Ship5(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship5.png"
        self.hp = DeluxeHP(self.game, 6000000, 200, 700, 350, 30)
        super().__init__(game, self.path, 0.98, 250, 40, 600)
        # self.cannon = LaserCannon(self.game, self, Vector2(-60, -30), self.force, 0.7)
        # self.cannon2 = LaserCannon(self.game, self, Vector2(60, -30), self.force, 0.7)
        # self.cannon3 = LaserCannon(self.game, self, Vector2(-100, -30), self.force, 0.7)
        # self.cannon4 = LaserCannon(self.game, self, Vector2(100, -30), self.force, 0.7)
        self.cannon = ShotGun1(self.game, self, Vector2(0, 0), self.force, 0.5)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()
        # self.cannon.tick()
        # self.cannon2.tick()
        # self.cannon3.tick()
        # self.cannon4.tick()
    def draw(self):
        super().draw()

