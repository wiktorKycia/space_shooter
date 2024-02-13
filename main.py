import pygame
from pygame.locals import *
from mycode.bullets import *
from mycode.cannons import *
from mycode.enemies import *
from mycode.levels import *
from mycode.other import *
from mycode.player import *
from mycode.ships import *
from mycode.two_players import *
from mycode.UI import *

class Game(object):
    """
    The main class in the program.
    It is used to connect things into one game.
    """
    def __init__(self):
        self.tps_max = 100.0

        #initialization
        pygame.init()
        self.width = 750
        self.height = 750
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.dt = 0.0
        pygame.display.set_caption("Planet defender")

        #running
        self.isrun = True

        #loading objects
        self.player = Player(self)
        self.mouse = Mouse(self)

        # lists
        self.levels = [
            Level1, Level2, Level3,
            Level4, Level5, Level6,
            Level7, Level8, Level9,
            Level10, Level11
        ]
        self.menuHandler = MenuHandler(self, MainMenu)

        while self.isrun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrun = False
            self.dt = self.tps_clock.get_time() / 1000
            self.tps_clock.tick(self.tps_max)
            self.screen.fill((0, 0, 0))

            self.tick()
            self.draw()
            pygame.display.update()
        pygame.quit()
        quit()

    def tick(self):
        self.menuHandler.tick()

    def draw(self):
        self.menuHandler.draw()

if __name__ == "__main__":
    Game()