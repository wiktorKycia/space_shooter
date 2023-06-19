import pygame
from pygame import mixer
from pygame.math import Vector2
from other import *
import os

from bullets import *
mixer.init()

class PlayableShip(object):
    def __init__(self, game, image_path, slip, mov_force, mass, shot_force,barrel_lenght):
        self.game = game
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        self.hitbox = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # self.mask.set_at()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.slip = slip
        self.mov_force = mov_force
        self.mass = mass

        size = self.game.screen.get_size()
        self.pos = Vector2(size[0] / 2, size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.shot_force = shot_force
        self.barrel = barrel_lenght
        self.bullets = []
        self.clock = 0

        self.hp = HP(self.game, 100, 200, 50, 700, 700)

    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.mov_force))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.mov_force))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.mov_force, 0))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.mov_force, 0))

        # Physics
        self.vel *= self.slip
        self.vel -= Vector2(0, 0)

        self.vel += self.acc
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
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox, 1)

class Scout(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/statek1.png"
        super().__init__(self.game, self.path, 0.99, 1000, 2000, 1500, 10)
        # # self.points = [Vector2(0, -26), Vector2(20, 12), Vector2(0, 24), Vector2(-20, 12)]
    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.clock >= 0.15:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x, self.pos.y, 2, 10, self.shot_force, 20, (230, 0, 0),
                            './shot_sounds/blaster.mp3')
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            acc = -bullet.acc  # getting initial bullet velocity
            vel = (bullet.mass * acc) / self.mass
            # getting initial velocity from zasada zachowania pędu
            vel.x *= vel.x
            vel.y *= vel.y
            energy = (self.mass * vel) / 2  # calculating kinetic energy
            force = energy / self.barrel  # calculating kickback force
            self.add_force(Vector2(force.x, force.y))
    def draw(self):
        super().draw()
        # #Base polygon
        # self.points = [Vector2(0, -26), Vector2(20, 12), Vector2(0, 24), Vector2(-20, 12)]
        #
        # #Rotate polygon
        # angle = self.vel.angle_to(Vector2(0, 1)) # kąt między wektorem prędkości, a linią poziomą
        # self.points = [p.rotate(angle) for p in self.points]
        #
        # # Fix y axis
        # self.points = [Vector2(p.x, p.y * -1) for p in self.points]
        #
        # #Add current position
        # self.points = [self.pos + p for p in self.points]
        #
        # #draw polygon
        # pygame.draw.polygon(self.game.screen, (255, 255, 255), self.points)

class Ship1(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/ship1.png"
        super().__init__(game, self.path, 0.98, 18600, 4000, 40000, 100)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.clock >= 0.25:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x, self.pos.y, 5, 50, self.shot_force, 50, (0, 200, 230), './shot_sounds/blaster.mp3')
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
        super().__init__(game, self.path, 0.98, 25000, 3800, 50000, 100)

    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.clock >= 0.30:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x-27, self.pos.y-15, 5, 50, self.shot_force, 50, (0, 200, 230), './shot_sounds/blaster.mp3')
            bullet1 = Bullet(self.game, self.pos.x+27, self.pos.y-15, 5, 50, self.shot_force, 50, (0, 200, 230), './shot_sounds/blaster.mp3')
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

