import pygame
from pygame.math import Vector2
import os
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
    def __init__(self, game, image_path, speed, slip):
        self.game = game
        self.image = pygame.image.load(os.path.join(image_path))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = speed
        self.slip = slip

        size = self.game.screen.get_size()
        self.pos = Vector2(size[0] / 2, size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))

        # Physics
        self.vel *= self.slip
        self.vel -= Vector2(0, 0)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))

class Scout(PlayableShip):
    def __init__(self, game):
        self.game = game
        self.path = "./ships/statek1.png"
        super().__init__(self.game, self.path, 0.001, 0.999)
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

class Bullet(object):
    def __init__(self, x, y, width, height, color):
        pass
    def tick(self):
        pass
    def draw(self):
        pass