from code.bullets import *

class Kinetic60Gun:
    def __init__(self, game, ship, x, y, force, interval, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = Vector2(x, y)
        self.x = x
        self.y = y
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0

    def shot(self):
        pass

    def tick(self):
        self.clock += self.game.dt

