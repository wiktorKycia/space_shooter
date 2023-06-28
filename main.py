import pygame
from code import *

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
        self.showing = "mainmenu"

        #loading objects
        self.player = Player(self)

        #levels
        self.level1 = Level1(self)
        self.level2 = Level2(self)
        self.level3 = Level3(self)

        # lists
        self.enemies = []
        self.levels = [self.level1, self.level2, self.level3]
        self.level_pointer = 0

        # menus/interfaces
        self.mainmenu = MainMenu(self)
        self.gamemenu = GameMenu(self)
        self.levelsmenu = LevelsMenu(self)

        while self.isrun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrun = False
            self.dt = self.tps_clock.get_time() / 1000
            self.tps_clock.tick(self.tps_max)
            self.screen.fill((0, 0, 0))

            match self.showing:
                case "mainmenu":
                    self.mainmenu.tick_menu()
                    self.mainmenu.draw_menu()
                case "gamemenu":
                    self.gamemenu.tick_menu()
                    self.gamemenu.draw_menu()
                case "levelsmenu":
                    self.levelsmenu.tick_menu()
                    self.levelsmenu.draw_menu()
                case "game":
                    self.tick()
                    self.draw()
                case _: pass
            pygame.display.update()
        pygame.quit()
        quit()

    def tick(self):

        for enemy in self.enemies:
            enemy.tick()
            for bullet in enemy.bullets:
                if self.player.current_ship.mask.overlap(bullet.mask, (bullet.pos.x - self.player.current_ship.hitbox.x, bullet.pos.y - self.player.current_ship.hitbox.y)):
                    energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                    self.player.current_ship.hp.get_damage(energy)
                    enemy.bullets.remove(bullet)
                    continue

            for bullet in self.player.current_ship.bullets:
                if enemy.mask.overlap(bullet.mask, (bullet.pos.x - bullet.width/2 - enemy.hitbox.x, bullet.pos.y - bullet.height/2 - enemy.hitbox.y)):
                    self.player.current_ship.bullets.remove(bullet)
                    energy = (bullet.mass * bullet.vel * bullet.vel) / 2
                    enemy.health -= energy
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                    continue

        self.player.current_ship.tick()
        self.levels[self.level_pointer].tick()

    def draw(self):

        for enemy in self.enemies:
            enemy.draw()

        self.player.current_ship.draw()


if __name__ == "__main__":
    Game()