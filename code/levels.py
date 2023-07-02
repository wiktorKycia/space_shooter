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
                    self.game.showing = "gamemenu"
                    self.game.gamemenu.__init__(self.game)
