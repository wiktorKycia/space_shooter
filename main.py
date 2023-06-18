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
        self.player = Ship1(self)

        # lists
        self.enemies = []
        self.block = Minilevel(self)
        # self.block.triangle4(int(750/2), 100)
        # self.block.triangle4(int(750/2 + 150), 100)
        # self.block.line(375, 50, 8, 2)
        self.block.pair(375, 50)
        # self.block.add_single(Enemy2(self, 400, 50))
        # self.block.add_single(Enemy1(self, 300, 50))
        # self.block.add_single(Enemy3(self, 500, 50))
        pygame.mouse.set_visible(True)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        # mouse
        self.mouse = pygame.Surface((10, 10))
        self.mouse.fill(self.red)
        self.mouse_mask = pygame.mask.from_surface(self.mouse)


        while self.isrun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrun = False
                    pygame.quit()
                    quit()
            self.dt = self.tps_clock.get_time() / 1000
            self.tps_clock.tick(self.tps_max)
            self.tick()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.update()


    def tick(self):

        for enemy in self.enemies:
            enemy.tick()
            for bullet in enemy.bullets:
                if self.player.mask.overlap(bullet.mask, (bullet.pos.x - self.player.pos.x, bullet.pos.y - self.player.pos.y)):
                    print("Trafiony")
                    enemy.bullets.remove(bullet)
                    continue
                else:
                    pass

        # get the mouse position
        pos = pygame.mouse.get_pos()

        # check mask overlap
        if self.player.mask.overlap(self.mouse_mask, (pos[0] - self.player.pos.x, pos[1] - self.player.pos.y)):
            self.mouse.fill(self.green)
        else:
            self.mouse.fill(self.red)
        self.screen.blit(self.mouse, pos)
        self.player.tick()

    def draw(self):
        # self.ob.draw()

        for enemy in self.enemies:
            enemy.draw()

        self.player.draw()


if __name__ == "__main__":
    Game()