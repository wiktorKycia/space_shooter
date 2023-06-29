import pygame

from code.bullets import *

class Kinetic60Gun:
    def __init__(self, game, ship, translation:Vector2, force:int , interval:float, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0

        # self.rect = pygame.Rect(self.pos.x - 5, self.pos.y - 10, 10, 20)

    def shot(self):
        bullet = Kinetic60Bullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        self.ship.bullets.append(bullet)

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        # self.rect.center = self.pos
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval:
            self.clock = 0
            print("E")


    def draw(self):
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.rect)
        pass
