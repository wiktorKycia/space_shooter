import pygame.time
from code.enemies import *

class MiniLevel:
    def __init__(self, game):
        self.game = game

    def add_single(self, enemy):
        self.game.enemies.append(enemy)

    def pair(self, x:int, y:int, type:int=1):
        match type:
            case 1:
                enemy1 = Enemy1(self.game, x-50, y)
                enemy2 = Enemy1(self.game, x+50, y)
            case 2:
                enemy1 = Enemy2(self.game, x - 50, y)
                enemy2 = Enemy2(self.game, x + 50, y)
            case 3:
                enemy1 = Enemy3(self.game, x - 50, y)
                enemy2 = Enemy3(self.game, x + 50, y)
            case _:
                enemy1 = Enemy1(self.game, x - 50, y)
                enemy2 = Enemy1(self.game, x + 50, y)
        self.game.enemies.extend([enemy1, enemy2])

    def line(self, x:int, y:int, lenght:int, type:int=1):
        match type:
            case 1:
                if lenght % 2 == 0:
                    enemy1 = Enemy1(self.game, x - 50, y)
                    enemy2 = Enemy1(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght-2)/2)):
                        enemy1 = Enemy1(self.game, x - 50 - (i+1) * 100, y)
                        enemy2 = Enemy1(self.game, x + 50 + (i+1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy1(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght-1)/2)):
                        enemy2 = Enemy1(self.game, x - (i+1) * 100, y)
                        enemy3 = Enemy1(self.game, x + (i+1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case 2:
                if lenght % 2 == 0:
                    enemy1 = Enemy2(self.game, x - 50, y)
                    enemy2 = Enemy2(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght - 2) / 2)):
                        enemy1 = Enemy2(self.game, x - 50 - (i + 1) * 100, y)
                        enemy2 = Enemy2(self.game, x + 50 + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy2(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght - 1) / 2)):
                        enemy2 = Enemy2(self.game, x - (i + 1) * 100, y)
                        enemy3 = Enemy2(self.game, x + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case 3:
                if lenght % 2 == 0:
                    enemy1 = Enemy3(self.game, x - 50, y)
                    enemy2 = Enemy3(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght - 2) / 2)):
                        enemy1 = Enemy3(self.game, x - 50 - (i + 1) * 100, y)
                        enemy2 = Enemy3(self.game, x + 50 + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy3(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght - 1) / 2)):
                        enemy2 = Enemy3(self.game, x - (i + 1) * 100, y)
                        enemy3 = Enemy3(self.game, x + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case _:
                pass

    def triangle1(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 50, y - 50)
        enemy2 = Enemy1(self.game, x + 50, y - 50)
        enemy3 = Enemy1(self.game, x, y + 20)
        self.game.enemies.extend([enemy1, enemy2, enemy3])

    def triangle2(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 50, y - 50)
        enemy2 = Enemy1(self.game, x + 50, y - 50)
        enemy3 = Enemy2(self.game, x, y + 20)
        self.game.enemies.extend([enemy1, enemy2, enemy3])

    def triangle3(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 85, y - 50)
        enemy2 = Enemy1(self.game, x - 50, y + 10)
        enemy3 = Enemy1(self.game, x, y + 50)
        enemy4 = Enemy1(self.game, x + 50, y + 10)
        enemy5 = Enemy1(self.game, x + 85, y - 50)
        enemy6 = Enemy2(self.game, x, y - 20)
        self.game.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])

    def triangle4(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 85, y - 50)
        enemy2 = Enemy1(self.game, x - 50, y + 10)
        enemy3 = Enemy1(self.game, x, y + 50)
        enemy4 = Enemy1(self.game, x + 50, y + 10)
        enemy5 = Enemy1(self.game, x + 85, y - 50)
        enemy6 = Enemy3(self.game, x, y - 30)
        self.game.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])

    def triangle5(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 40, y + 40)
        enemy2 = Enemy1(self.game, x + 40, y + 40)
        enemy3 = Enemy2(self.game, x - 80, y - 20)
        enemy4 = Enemy2(self.game, x + 80, y - 20)
        enemy5 = Enemy3(self.game, x, y)
        self.game.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5])

class Level:
    def __init__(self, game):
        self.game = game
        self.block = MiniLevel(game)

    def check_if_all_died(self):
        if len(self.game.enemies) == 0:
            return True
        else: return False


class LevelGame:
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.levels = [
            Level1, Level2, Level3,
            Level4, Level5, Level6,
            Level7, Level8, Level9,
            Level10, Level11
        ]
        self.level_pointer = 0
        self.click_P_counter = 0

        self.other_bullets = []

    def tick(self):
        """
        Method tick contains instructions to run during every tick (frame).
        First, it calls every enemies' tick method,
        then calls every bullets' tick method, that doesn't have any superior object, for example a ship,
        then calls player's and level's tick method,
        lastly, checks for clicking p key in order to show pause menu.
        """
        for enemy in self.enemies:
            enemy.tick()
            # for bullet in enemy.bullets:
            #     if self.player.current_ship.mask.overlap(bullet.mask, (bullet.pos.x - self.player.current_ship.hitbox.x, bullet.pos.y - self.player.current_ship.hitbox.y)):
            #         energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
            #         self.player.current_ship.hp.get_damage(energy)
            #         enemy.bullets.remove(bullet)
            #         continue

            # for bullet in self.player.current_ship.bullets:
            #     if enemy.mask.overlap(bullet.mask, (bullet.pos.x - bullet.width/2 - enemy.hitbox.x, bullet.pos.y - bullet.height/2 - enemy.hitbox.y)):
            #         self.player.current_ship.bullets.remove(bullet)
            #         energy = (bullet.mass * bullet.vel * bullet.vel) / 2
            #         enemy.hp.get_damage(energy)
            #         if enemy.hp.hp <= 0:
            #             self.other_bullets.extend(enemy.bullets)
            #             self.enemies.remove(enemy)
            #             break
            #         continue

        for bullet in self.other_bullets:
            bullet.tick()
            bullet.draw()
            if self.game.player.current_ship.mask.overlap(bullet.mask, (
                    bullet.pos.x - self.game.player.current_ship.hitbox.x,
                    bullet.pos.y - self.game.player.current_ship.hitbox.y)):
                energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                self.game.player.current_ship.hp.get_damage(energy)
                self.other_bullets.remove(bullet)
                continue

        self.game.player.current_ship.tick()
        self.levels[self.level_pointer].tick()

        if pygame.key.get_pressed()[pygame.K_p] == 1 and self.click_P_counter == 0:
            self.click_P_counter += 1
            # self.showing = "pausemenu"
        elif pygame.key.get_pressed()[pygame.K_p] == 0:
            self.click_P_counter = 0
        else:
            self.click_P_counter += 1

    def draw(self):
        """
        Method draw usually is called after tick method, it displays object on the screen.
        First, it draws the enemies,
        then player and player's hp.
        """
        for enemy in self.enemies:
            enemy.draw()

        self.game.player.current_ship.draw()
        self.game.player.current_ship.hp.tick()

class Level1(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.add_single(Enemy1(self.game, self.game.width/2, 100))
                case 2:
                    self.block.pair(self.game.width / 2, 100, 1)
                case 3:
                    self.block.line(self.game.width/2, 100, 3, 1)
                case _:
                    self.game.player.add_coins(500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level2(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.pair(self.game.width / 2, 100, 1)
                case 2:
                    self.block.triangle1(self.game.width/2, 100)
                case 3:
                    self.block.line(self.game.width/2, 100, 4, 1)
                case _:
                    self.game.player.add_coins(750)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level3(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.add_single(Enemy2(self.game, self.game.width/2, 100))
                case 2:
                    self.block.line(self.game.width/2, 100, 3)
                case 3:
                    self.block.triangle2(self.game.width/2, 100)
                case 4:
                    self.block.pair(self.game.width/2, 150)
                case _:
                    self.game.player.add_coins(1000)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level4(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.line(self.game.width / 2, 100, 3)
                case 2:
                    self.block.triangle1(self.game.width/4, 100)
                    self.block.triangle1(self.game.width*3/4, 100)
                case 3:
                    self.block.line(self.game.width / 2, 100, 6)
                case 4:
                    self.block.pair(self.game.width/2, 100, 2)
                case 5:
                    self.block.line(self.game.width / 2, 100, 3)
                    self.block.triangle1(self.game.width / 2, 200)
                case _:
                    self.game.player.add_coins(1500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level5(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.line(self.game.width / 2, 100, 3, 2)
                case 2:
                    self.block.triangle3(self.game.width/2, 100)
                case 3:
                    self.block.line(self.game.width / 2, 100, 8)
                case 4:
                    self.block.pair(self.game.width/2, 150, 2)
                case 5:
                    self.block.line(self.game.width / 2, 100, 3, 2)
                case _:
                    self.game.player.add_coins(2000)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level6(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.triangle3(self.game.width*4/5, 100)
                    self.block.triangle3(self.game.width/5, 100)
                case 2:
                    self.block.triangle2(self.game.width/2, 100)
                    self.block.triangle2(self.game.width/5, 100)
                    self.block.triangle2(self.game.width*4/5, 100)
                case 3:
                    self.block.line(self.game.width / 2, 100, 3)
                    self.block.line(self.game.width / 2, 200, 3)
                case 4:
                    self.block.line(self.game.width / 2, 100, 3, 5)
                case _:
                    self.game.player.add_coins(2500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level7(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.triangle2(self.game.width / 5, 100)
                    self.block.line(self.game.width / 2, 100, 3)
                    self.block.triangle2(self.game.width * 4 / 5, 100)
                case 2:
                    self.block.line(self.game.width / 2, 100, 6, 2)
                case 3:
                    self.block.line(self.game.width / 2, 100, 5)
                    self.block.line(self.game.width / 2, 200, 5)
                case 4:
                    self.block.triangle3(self.game.width / 2, 150)
                case 5:
                    self.block.pair(self.game.width*3/4, 100, 2)
                    self.block.pair(self.game.width/4, 100, 2)
                case _:
                    self.game.player.add_coins(3500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level8(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.add_single(Enemy3(self.game, self.game.width/2, 150))
                case 2:
                    self.block.add_single(Enemy3(self.game, self.game.width / 2, 150))
                    self.block.add_single(Enemy1(self.game, self.game.width / 4, 100))
                    self.block.add_single(Enemy1(self.game, self.game.width * 3 / 4, 100))
                case 3:
                    self.block.line(self.game.width / 2, 100, 3, 2)
                    self.block.line(self.game.width / 2, 200, 3, 2)
                case 4:
                    self.block.triangle2(self.game.width / 4, 150)
                    self.block.triangle2(self.game.width * 3 / 4, 150)
                # case 5:
                #     self.block.pair(self.game.width*3/4, 100, 2)
                #     self.block.pair(self.game.width/4, 100, 2)
                case _:
                    self.game.player.add_coins(4500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)


class Level9(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.triangle4(self.game.width/2, 150)
                case 2:
                    self.block.add_single(Enemy3(self.game, self.game.width / 2, 150))
                    self.block.add_single(Enemy2(self.game, self.game.width / 4, 100))
                    self.block.add_single(Enemy2(self.game, self.game.width * 3 / 4, 100))
                case 3:
                    self.block.line(self.game.width / 2, 100, 7)
                    self.block.line(self.game.width / 2, 200, 7)
                case 4:
                    self.block.triangle3(self.game.width / 4, 150)
                    self.block.triangle3(self.game.width * 3 / 4, 150)
                case 5:
                    self.block.triangle5(self.game.width/2, 150)
                case _:
                    self.game.player.add_coins(6000)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)


class Level10(Level):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.line(self.game.width / 2, 50, 6)
                    self.block.line(self.game.width / 2, 150, 6)
                    self.block.line(self.game.width / 2, 250, 6)
                case 2:
                    self.block.pair(self.game.width/2, 150, 3)
                case 3:
                    self.block.line(self.game.width / 2, 100, 8, 2)
                case 4:
                    self.block.triangle5(self.game.width/5, 150)
                    self.block.triangle5(self.game.width*4/5, 150)
                # case 5:
                #     self.block.triangle5(self.game.width/2, 150)
                case _:
                    self.game.player.add_coins(7500)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)

class Level11(Level):

    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True

    def tick(self):
        self.current_time = pygame.time.get_ticks()

        if self.check_if_all_died() and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
            self.flag = True
            match self.wave_number:
                case 0: pass
                case 1:
                    self.block.add_single(Bouncer1(self.game, 300, 200))
                case _:
                    self.game.player.add_coins(10000)
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)