import pygame
from ships import *
from enemies import *
from levels import *

class Game(object):
    def __init__(self):
        self.tps_max = 100.0

        #initialization
        pygame.init()
        self.width = 750
        self.height = 750
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.dt = 0.0
        #running
        self.isrun = True

        #loading objects
        # self.ob = Object(50, 50, 50, 50, self)
        self.player = Ship2(self)

        # lists
        self.enemies = []
        self.block = Minilevel(self)
        self.block.add_single(Enemy1(self, 0, 0))
        while self.isrun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrun = False
                    pygame.quit()
                    quit()
            self.dt = self.tps_clock.tick(self.tps_max) / 100
            self.tick()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.update()


    def tick(self):
        self.player.tick()
        for enemy in self.enemies:
            enemy.tick()

    def draw(self):
        # self.ob.draw()
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()


if __name__ == "__main__":
    Game()