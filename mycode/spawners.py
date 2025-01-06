import pygame.time
from mycode.enemies import *
from mycode.UI import *
import random
import json
from copy import deepcopy


def add_single(enemies: list[BaseEnemy], enemy: BaseEnemy):
    enemies.append(enemy)


def pair(enemies: list[BaseEnemy], x: int, y: int, enemy: BaseEnemy):
    enemy1 = deepcopy(enemy)
    enemy2 = deepcopy(enemy)
    enemy1.pos.xy = (x - 50, y)
    enemy2.pos.xy = (x + 50, y)
    enemies.extend([enemy1, enemy2])


def line(enemies: list[BaseEnemy], x: int, y: int, length_: int, enemy: BaseEnemy, spacing: int = 100):
    created: int = 0
    if length_ % 2 == 0:
        enemy1 = deepcopy(enemy)
        enemy2 = deepcopy(enemy)
        
        enemy1.pos.xy = (x - (spacing / 2), y)
        enemy2.pos.xy = (x + (spacing / 2), y)
        
        enemies.extend([enemy1, enemy2])
        created = 2
    else:
        enemy1 = deepcopy(enemy)
        enemies.append(enemy1)
        created = 1
    
    for i in range(0, int((length_ - created) / 2)):
        enemy1 = deepcopy(enemy)
        enemy2 = deepcopy(enemy)
        
        if created == 2:
            enemy1.pos.xy = (x - (i + 1) * spacing, y)
            enemy2.pos.xy = (x + (i + 1) * spacing, y)
        else:
            enemy1.pos.xy = (x - 50 - (i + 1) * spacing, y)
            enemy2.pos.xy = (x + 50 + (i + 1) * spacing, y)
        
        enemies.extend([enemy1, enemy2])
    
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
