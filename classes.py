import pygame
from pygame import mixer
from pygame.math import Vector2
import os
mixer.init()
class Object(object):
    def __init__(self, x, y, width, height, game):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        pass
    def draw(self):
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox)
class MovingObject(Object):
    pass

class PlayableShip(object):
    def __init__(self, game, image_path, slip, force, mass, barrel_lenght):
        self.game = game
        self.image = pygame.image.load(os.path.join(image_path))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.slip = slip

        self.barrel = barrel_lenght

        self.force = force
        self.mass = mass

        size = self.game.screen.get_size()
        self.pos = Vector2(size[0] / 2, size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.bullets = []
        self.clock = 0

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
        self.pos += self.vel * self.game.dt
        self.acc *= 0

        self.clock += pygame.time.Clock().tick(self.game.tps_max) / 1000
        if pressed[pygame.K_SPACE] and self.clock >= 0.1:
            self.clock = 0
            bullet = Bullet(self.game, self.pos.x, self.pos.y, 2, 10, self.force, 20, (255, 0, 0), './shot_sounds/laser-medium-gun.mp3')
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

        for bullet in self.bullets:
            bullet.tick()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y <= 0 - bullet.height:
                self.bullets.remove(bullet)
        self.game.screen.blit(self.image, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))

class Scout(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/statek1.png"
        super().__init__(self.game, self.path, 0.99, 1000, 2000, 10)
        # # self.points = [Vector2(0, -26), Vector2(20, 12), Vector2(0, 24), Vector2(-20, 12)]
    def add_force(self, force):
        super().add_force(force)
    def tick(self):
        super().tick()
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

class Ship2(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/ship1.png"
        super().__init__(game, self.path, 0.98, 3500, 4000, 50)

class Bullet(object):
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.mass = mass
        acc = int(force / mass)
        self.acc = Vector2(0, -acc)

        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.pos.x - width / 2, self.pos.y - height / 2, width, height)

        self.game = game
        self.color = color

        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)
    def tick(self):
        # Physics
        self.vel *= 0.999

        self.vel += self.acc
        self.pos += self.vel * self.game.dt
        self.acc *= 0
    def draw(self):
        self.hitbox = pygame.Rect(self.pos.x - self.width / 2, self.pos.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, self.hitbox)