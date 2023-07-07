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
        pygame.display.set_caption("Planet defender")

        #running
        self.isrun = True
        self.showing = "mainmenu"

        #loading objects
        self.player = Player(self)
        self.mouse = Mouse(self)

        # lists
        self.enemies = []
        self.levels = [
            Level1(self), Level2(self), Level3(self),
            Level4(self), Level5(self), Level6(self),
            Level7(self), Level8(self), Level9(self),
            Level10(self)
        ]
        self.level_pointer = 0

        self.other_bullets = []

        # menus/interfaces
        self.mainmenu = MainMenu(self)
        self.gamemenu = GameMenu(self)
        self.levelsmenu = LevelsMenu(self)
        self.hangar = HangarMenu(self)

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
                    enemy.hp.get_damage(energy)
                    if enemy.hp.hp <= 0:
                        self.other_bullets.extend(enemy.bullets)
                        self.enemies.remove(enemy)
                        break
                    continue

        for bullet in self.other_bullets:
            bullet.tick()
            bullet.draw()
            if self.player.current_ship.mask.overlap(bullet.mask, (
            bullet.pos.x - self.player.current_ship.hitbox.x, bullet.pos.y - self.player.current_ship.hitbox.y)):
                energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                self.player.current_ship.hp.get_damage(energy)
                self.other_bullets.remove(bullet)
                continue

        self.player.current_ship.tick()
        self.levels[self.level_pointer].tick()

    def draw(self):

        for enemy in self.enemies:
            enemy.draw()

        self.player.current_ship.draw()
        self.player.current_ship.hp.tick()


if __name__ == "__main__":
    Game()