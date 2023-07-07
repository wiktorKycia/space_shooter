import pygame
from pygame import mixer
from pygame.math import Vector2
import os
from code import *
from code.other import *
from code.cannons import *

mixer.init()

class Ship(object):
    def __init__(self, game, x, y, image_path, scale=1.0):
        self.game = game
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def tick(self):
        pass

    def draw(self):
        self.game.screen.blit(self.image, (self.x - self.width/2, self.y - self.height/2))

class PlayableShip(object):
    def __init__(self, game, image_path, slip, max_speed, mass, force):
        self.game = game
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        self.hitbox = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # self.mask.set_at()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.slip = slip
        self.mass = mass

        size = self.game.screen.get_size()
        self.pos = Vector2(size[0] / 2, size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.force = force
        self.bullets = []
        self.clock = 0

        self.max_speed = max_speed


    def add_force(self, force):
        self.acc += force / self.mass

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

        # Physics
        self.vel *= self.slip
        self.vel -= Vector2(0, 0)

        self.vel += self.acc

        # Limiting speed
        if self.vel.x > self.max_speed: # right
            self.vel = Vector2(self.max_speed, self.vel.y)
        elif self.vel.x < -self.max_speed: # left
            self.vel = Vector2(-self.max_speed, self.vel.y)
        if self.vel.y > self.max_speed: # up
            self.vel = Vector2(self.vel.x, self.max_speed)
        elif self.vel.y < -self.max_speed:  # down
            self.vel = Vector2(self.vel.x, -self.max_speed)

        self.pos += self.vel * self.game.dt
        self.acc *= 0

        self.hitbox.center = (self.pos.x, self.pos.y)

        self.clock += self.game.dt

        for bullet in self.bullets:
            if bullet.pos.y <= -bullet.height:
                self.bullets.remove(bullet)
            else:
                bullet.tick()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y <= 0 - bullet.height:
                self.bullets.remove(bullet)
        self.game.screen.blit(self.image, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))

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
        self.cannon = Kinetic60Gun(self.game, self, Vector2(0, -20), self.force, 0.1)

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
        super().__init__(game, self.path, 0.98, 150, 1500, 15000)
        self.cannon = LaserCannon(self.game, self, Vector2(-60, -30), self.force, 0.7)
        self.cannon2 = LaserCannon(self.game, self, Vector2(60, -30), self.force, 0.7)
        self.cannon3 = LaserCannon(self.game, self, Vector2(-100, -30), self.force, 0.7)
        self.cannon4 = LaserCannon(self.game, self, Vector2(100, -30), self.force, 0.7)

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

