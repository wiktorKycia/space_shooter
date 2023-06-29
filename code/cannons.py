import pygame
import math
from code.bullets import *

class Kinetic60Gun:
    def __init__(self, game, ship, translation:Vector2, force:int, barrel_length:int, interval:float, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0
        self.barrel = barrel_length
        # self.rect = pygame.Rect(self.pos.x - 5, self.pos.y - 10, 10, 20)

    def shot(self):
        bullet = Kinetic60Bullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)

    def calculate_kickback_force(self, bullet):
        acc = -bullet.acc  # getting initial bullet velocity
        tim = math.sqrt(2 * self.barrel / acc)  # time that bullet spent in the barrel
        vel1 = acc * tim        # getting vel of the bullet after escaping from barrel
        vel = (bullet.mass * vel1) / self.ship.mass
        # getting initial velocity from zasada zachowania pędu
        vel.x *= vel.x
        vel.y *= vel.y
        energy = (self.ship.mass * vel) / 2  # calculating kinetic energy
        force = energy / self.barrel  # calculating kickback force
        return force
    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        # self.rect.center = self.pos
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval:
            self.clock = 0
            self.shot()


    def draw(self):
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.rect)
        pass
