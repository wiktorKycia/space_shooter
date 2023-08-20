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
        size = game.screen.get_size()
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
        super().__init__(game, self.path, 40, 150, 200, 500000, 300, 25, 165, 710)
        self.cannon = KineticGun(self.game, self, Vector2(0, -10), self.force, 0.6)

    def tick(self):
        super().tick()
        self.cannon.tick()

class Ship1(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship1.png"
        super().__init__(
            game=game,
            path=self.path,
            mass=100,
            max_speed=150,
            force=4000,
            hp_amount=1000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = ManeuveringBulletsLauncher(
            game=self.game,
            ship=self,
            translation=Vector2(0, -30),
            force=self.force,
            interval=0.7,
            key=pygame.K_SPACE
        )

    def tick(self):
        super().tick()
        self.cannon.tick()

class Ship2(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship2.png"
        super().__init__(
            game, self.path,
            mass=70,
            max_speed=170,
            force=1250,
            hp_amount=900000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.gun = KineticGun(game, self, Vector2(-27, 20), self.force, key=pygame.K_SPACE)
        self.gun2 = KineticGun(game, self, Vector2(-27, -20), self.force, key=pygame.K_SPACE, bar_y=670)
        # self.cannon = Blaster(self.game, self, Vector2(27, -20), self.force, 0.35)
        # self.cannon2 = Blaster(self.game, self, Vector2(-27, -20), self.force, 0.35)

    def tick(self):
        super().tick()
        self.gun.tick()
        self.gun2.tick()
        # self.cannon.tick()
        # self.cannon2.tick()

    def draw(self):
        super().draw()
        # self.gun.clip.draw()
        # self.gun2.clip.draw()

class Ship3(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship3.png"
        super().__init__(
            game, self.path,
            mass=200,
            max_speed=200,
            force=5000,
            hp_amount=2000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = Blaster(self.game, self, Vector2(-23, -30), self.force, 0.4)
        self.cannon2 = Blaster(self.game, self, Vector2(23, -30), self.force, 0.4)

    def tick(self):
        super().tick()
        self.cannon.tick()
        self.cannon2.tick()

class Ship4(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship4.png"
        super().__init__(
            game, self.path,
            mass=500,
            max_speed=100,
            force=5000,
            hp_amount=3500000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = Blaster(self.game, self, Vector2(-25, -35), self.force, 0.4)
        self.cannon2 = Blaster(self.game, self, Vector2(25, -35), self.force, 0.4)
        self.cannon3 = Blaster(self.game, self, Vector2(-47, -30), self.force, 0.4)
        self.cannon4 = Blaster(self.game, self, Vector2(47, -30), self.force, 0.4)

    def tick(self):
        super().tick()
        self.cannon.tick()
        self.cannon2.tick()
        self.cannon3.tick()
        self.cannon4.tick()

class Ship5(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/ship5.png"
        super().__init__(
            game, self.path,
            mass=40,
            max_speed=250,
            force=600,
            hp_amount=1500000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = ShotGun1(self.game, self, Vector2(0, 0), self.force, 0.5)

    def tick(self):
        super().tick()
        self.cannon.tick()

class Ship6(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./images/ships/excalibur.png"
        super().__init__(
            game, self.path,
            mass=400,
            max_speed=200,
            force=4500,
            hp_amount=5000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = LaserHeavyGun(game, self, Vector2(0, 0), self.force, 0.1)

    def tick(self):
        super().tick()
        self.cannon.tick()

class Ship7(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/ships/ship7.png",
            mass=260,
            max_speed=300,
            force=2500,
            hp_amount=4800000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon = Blaster(game, self, Vector2(0,0), self.force, 0.25)

    def tick(self):
        super().tick()
        self.cannon.tick()

class Ship8(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/ships/ship8.png",
            mass=800,
            max_speed=250,
            force=2000,
            hp_amount=6000000,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710
        )
        self.cannon1 = Kinetic60Gun(self.game, self, Vector2(-40, 0), self.force, 0.03)
        self.cannon2 = Kinetic60Gun(self.game, self, Vector2(-20, -20), self.force, 0.03)
        self.cannon3 = Kinetic60Gun(self.game, self, Vector2(0, -40), self.force, 0.03)
        self.cannon4 = Kinetic60Gun(self.game, self, Vector2(20, -20), self.force, 0.03)
        self.cannon5 = Kinetic60Gun(self.game, self, Vector2(40, 0), self.force, 0.03)

    def tick(self):
        super().tick()
        self.cannon1.tick()
        self.cannon2.tick()
        self.cannon3.tick()
        self.cannon4.tick()
        self.cannon5.tick()
