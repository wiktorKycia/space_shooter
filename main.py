import pygame
from code.ships import *
from code.enemies import *
from code.levels import *

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
        self.player = Ship2(self)

        # lists
        self.enemies = []
        # self.block = Minilevel(self)
        # self.block.triangle4(int(750/2), 100)
        # self.block.triangle4(int(750/2 + 150), 100)
        # self.block.line(375, 50, 8, 2)
        # self.block.pair(375, 50)
        # self.block.add_single(Enemy2(self, 400, 50))
        # self.block.add_single(Enemy1(self, 300, 50))
        # self.block.add_single(Enemy3(self, 500, 50))
        self.level1 = Level1(self)

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

        for enemy in self.enemies:
            enemy.tick()
            for bullet in enemy.bullets:
                if self.player.mask.overlap(bullet.mask, (bullet.pos.x - self.player.hitbox.x, bullet.pos.y - self.player.hitbox.y)):
                    energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                    self.player.hp.get_damage(energy)
                    enemy.bullets.remove(bullet)
                    continue

            for bullet in self.player.bullets:
                if enemy.mask.overlap(bullet.mask, (bullet.pos.x - enemy.hitbox.x, bullet.pos.y - enemy.hitbox.y)):
                    self.player.bullets.remove(bullet)
                    energy = (bullet.mass * bullet.vel * bullet.vel) / 2
                    enemy.health -= energy
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                    continue

        self.player.tick()
        self.level1.tick()

    def draw(self):

        for enemy in self.enemies:
            enemy.draw()

        self.player.draw()


if __name__ == "__main__":
    Game()