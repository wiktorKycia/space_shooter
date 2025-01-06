import pygame.time
from mycode.enemies import *
from mycode.UI import *
import random
import json
from copy import deepcopy


def add_single(enemies: list, enemy: BaseEnemy):
    enemies.append(enemy)


def pair(self, x: int, y: int, enemy: BaseEnemy):
    enemy1 = deepcopy(enemy)
    enemy2 = deepcopy(enemy)
    enemy1.pos.xy = (x - 50, y)
    enemy2.pos.xy = (x + 50, y)
    enemies.extend([enemy1, enemy2])


def line(self, x: int, y: int, lenght_: int, enemy: BaseEnemy):
    match type_:
        case 1:
            if lenght_ % 2 == 0:
                enemy1 = Enemy1(self.game, x - 50, y)
                enemy2 = Enemy1(self.game, x + 50, y)
                self.enemies.extend([enemy1, enemy2])
                
                for i in range(0, int((lenght_ - 2) / 2)):
                    enemy1 = Enemy1(self.game, x - 50 - (i + 1) * 100, y)
                    enemy2 = Enemy1(self.game, x + 50 + (i + 1) * 100, y)
                    self.enemies.extend([enemy1, enemy2])
            else:
                enemy1 = Enemy1(self.game, x, y)
                self.enemies.append(enemy1)
                
                for i in range(0, int((lenght_ - 1) / 2)):
                    enemy2 = Enemy1(self.game, x - (i + 1) * 100, y)
                    enemy3 = Enemy1(self.game, x + (i + 1) * 100, y)
                    self.enemies.extend([enemy2, enemy3])
        case 2:
            if lenght_ % 2 == 0:
                enemy1 = Enemy2(self.game, x - 50, y)
                enemy2 = Enemy2(self.game, x + 50, y)
                self.enemies.extend([enemy1, enemy2])
                
                for i in range(0, int((lenght_ - 2) / 2)):
                    enemy1 = Enemy2(self.game, x - 50 - (i + 1) * 100, y)
                    enemy2 = Enemy2(self.game, x + 50 + (i + 1) * 100, y)
                    self.enemies.extend([enemy1, enemy2])
            else:
                enemy1 = Enemy2(self.game, x, y)
                self.enemies.append(enemy1)
                
                for i in range(0, int((lenght_ - 1) / 2)):
                    enemy2 = Enemy2(self.game, x - (i + 1) * 100, y)
                    enemy3 = Enemy2(self.game, x + (i + 1) * 100, y)
                    self.enemies.extend([enemy2, enemy3])
        case 3:
            if lenght_ % 2 == 0:
                enemy1 = Enemy3(self.game, x - 50, y)
                enemy2 = Enemy3(self.game, x + 50, y)
                self.enemies.extend([enemy1, enemy2])
                
                for i in range(0, int((lenght_ - 2) / 2)):
                    enemy1 = Enemy3(self.game, x - 50 - (i + 1) * 100, y)
                    enemy2 = Enemy3(self.game, x + 50 + (i + 1) * 100, y)
                    self.enemies.extend([enemy1, enemy2])
            else:
                enemy1 = Enemy3(self.game, x, y)
                self.enemies.append(enemy1)
                
                for i in range(0, int((lenght_ - 1) / 2)):
                    enemy2 = Enemy3(self.game, x - (i + 1) * 100, y)
                    enemy3 = Enemy3(self.game, x + (i + 1) * 100, y)
                    self.enemies.extend([enemy2, enemy3])
        case _:
            pass


def triangle1(self, x: int, y: int):
    enemy1 = Enemy1(self.game, x - 50, y - 50)
    enemy2 = Enemy1(self.game, x + 50, y - 50)
    enemy3 = Enemy1(self.game, x, y + 20)
    self.enemies.extend([enemy1, enemy2, enemy3])


def triangle2(self, x: int, y: int):
    enemy1 = Enemy1(self.game, x - 50, y - 50)
    enemy2 = Enemy1(self.game, x + 50, y - 50)
    enemy3 = Enemy2(self.game, x, y + 20)
    self.enemies.extend([enemy1, enemy2, enemy3])


def triangle3(self, x: int, y: int):
    enemy1 = Enemy1(self.game, x - 85, y - 50)
    enemy2 = Enemy1(self.game, x - 50, y + 10)
    enemy3 = Enemy1(self.game, x, y + 50)
    enemy4 = Enemy1(self.game, x + 50, y + 10)
    enemy5 = Enemy1(self.game, x + 85, y - 50)
    enemy6 = Enemy2(self.game, x, y - 20)
    self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])


def triangle4(self, x: int, y: int):
    enemy1 = Enemy1(self.game, x - 85, y - 50)
    enemy2 = Enemy1(self.game, x - 50, y + 10)
    enemy3 = Enemy1(self.game, x, y + 50)
    enemy4 = Enemy1(self.game, x + 50, y + 10)
    enemy5 = Enemy1(self.game, x + 85, y - 50)
    enemy6 = Enemy3(self.game, x, y - 30)
    self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])


def triangle5(self, x: int, y: int):
    enemy1 = Enemy1(self.game, x - 40, y + 40)
    enemy2 = Enemy1(self.game, x + 40, y + 40)
    enemy3 = Enemy2(self.game, x - 80, y - 20)
    enemy4 = Enemy2(self.game, x + 80, y - 20)
    enemy5 = Enemy3(self.game, x, y)
    self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5])
