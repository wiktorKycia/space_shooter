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
    def __init__(self, game, image_path, slip, max_speed, mass, force, barrel_length):
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
        self.barrel = barrel_length
        self.bullets = []
        self.clock = 0

        self.max_speed = max_speed

        self.hp = DeluxeHP(self.game, 1000000, 200, 700, 350, 30)

        self.cannon = Kinetic60Gun(self.game, self, Vector2(20, -20), self.force, self.barrel, 0.25)
        self.cannon2 = Kinetic60Gun(self.game, self, Vector2(-20, -20), self.force, self.barrel, 0.01)

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
        self.hp.tick()
        self.cannon.tick()
        self.cannon2.tick()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y <= 0 - bullet.height:
                self.bullets.remove(bullet)
        self.game.screen.blit(self.image, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))
        self.cannon.draw()
        self.cannon2.draw()
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox, 1)
        # self.hp.draw()

class Ship1(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/ship1.png"
        super().__init__(game, self.path, 0.98, 150, 100, 400, 10)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.clock >= 0.25:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x, self.pos.y, 5, 50, self.force, 0.5, (0, 200, 230), './shot_sounds/blaster.mp3')
            # bullet = Kinetic60Bullet(self.game, self.pos.x, self.pos.y, self.shot_force)
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            acc = -bullet.acc # getting initial bullet velocity
            vel = (bullet.mass * acc) / self.mass
                # getting initial velocity from zasada zachowania pędu
            vel.x *= vel.x
            vel.y *= vel.y
            energy = (self.mass * vel) / 2 # calculating kinetic energy
            force = energy / self.barrel # calculating kickback force
            self.add_force(Vector2(force.x, force.y))
    def draw(self):
        super().draw()

class Ship2(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/ship2.png"
        super().__init__(game, self.path, 0.98, 170, 38, 500, 10)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.clock >= 0.30:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x-27, self.pos.y-15, 5, 50, self.force, 0.5, (0, 200, 230), './shot_sounds/blaster.mp3')
            bullet1 = Bullet(self.game, self.pos.x+27, self.pos.y-15, 5, 50, self.force, 0.5, (0, 200, 230), './shot_sounds/blaster.mp3')
            self.bullets.append(bullet)
            self.bullets.append(bullet1)
            bullet.sound.play(0, 650)
            bullet1.sound.play(0, 650)
            acc = -bullet.acc # getting initial bullet velocity
            vel = (bullet.mass * acc) / self.mass
                # getting initial velocity from zasada zachowania pędu
            vel.x *= vel.x
            vel.y *= vel.y
            energy = (self.mass * vel) / 2 # calculating kinetic energy
            force = energy / self.barrel # calculating kickback force
            self.add_force(Vector2(force.x, force.y))
            self.add_force(Vector2(force.x, force.y))
    def draw(self):
        super().draw()

