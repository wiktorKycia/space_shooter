import pygame
from pygame.locals import *
from mycode.bullets import *
from mycode.cannons import *
from mycode.enemies import *
from mycode.levels import *
from mycode.other import *
from mycode.player import *
from mycode.ships import *
from mycode.UI import *
from tests.test11_line import width, height


class Game(object):
    """
    The main class in the program.
    It is used to connect things into one game.
    """

    def __init__(self,
                 levelManager: LevelManager,
                 screen: pygame.Surface,
                 max_tps: float = 100.0,
                 caption: str = "Planet defender"
                 ):
        self.tps_max = max_tps

        #initialization
        pygame.init()
        self.screen: pygame.Surface = screen
        self.tps_clock = pygame.time.Clock()
        self.dt = 0.0
        pygame.display.set_caption(caption)

        #running
        self.isrun = True

        #loading objects
        self.player = Player(self)
        self.mouse = Mouse(self)

        self.levelManager = levelManager

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
    width, height = (750, 750)
    screen = pygame.display.set_mode((width, height))

    enemySpawner: EnemySpawner = EnemySpawner(self)
    waveManager: WaveManager = WaveManager(self, "./gameData/levels.json", enemySpawner)
    levelManager: LevelManager = LevelManager(waveManager)

    game: Game = Game(levelManager, screen, 100.0)
