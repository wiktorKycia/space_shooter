from mycode.enemies import *
from copy import deepcopy
from pygame.math import Vector2


def create_enemy(enemy_type: str, x: float, y: float):
    builder = BaseEnemyBuilder()
    director = BaseEnemyBuilderDirector(builder, enemy_type)
    enemy = director.build(x, y)
    return enemy


def add_single(enemies: list[BaseEnemy], x: float, y: float, enemy_type: str):
    e = create_enemy(enemy_type, x, y)
    enemies.append(e)
    return e


def pair(enemies: list[BaseEnemy], x: float, y: float, enemy_type: str):
    enemy1 = create_enemy(enemy_type, x, y)
    enemy2 = create_enemy(enemy_type, x, y)
    enemy1.physics.pos.xy = Vector2(x - 50, y)
    enemy2.physics.pos.xy = Vector2(x + 50, y)
    enemies.extend([enemy1, enemy2])
    return [enemy1, enemy2]


def line(enemies: list[BaseEnemy], x: float, y: float, length_: int, enemy_type: str, spacing: int = 100):
    created_number: int = 0
    created: list[BaseEnemy] = []

    if length_ % 2 == 0:
        enemy1 = create_enemy(enemy_type, x, y)
        enemy2 = create_enemy(enemy_type, x, y)
        
        enemy1.physics.pos.xy = Vector2(x - (spacing / 2), y)
        enemy2.physics.pos.xy = Vector2(x + (spacing / 2), y)
        
        enemies.extend([enemy1, enemy2])
        created.extend([enemy1, enemy2])
        created_number = 2
    else:
        enemy1 = create_enemy(enemy_type, x, y)
        enemies.append(enemy1)
        created.append(enemy1)
        created_number = 1
    
    for i in range(0, int((length_ - created_number) / 2)):
        enemy1 = create_enemy(enemy_type, x, y)
        enemy2 = create_enemy(enemy_type, x, y)
        
        if created_number == 2:
            enemy1.physics.pos.xy = Vector2(x - (i + 1) * spacing, y)
            enemy2.physics.pos.xy = Vector2(x + (i + 1) * spacing, y)
        else:
            enemy1.physics.pos.xy = Vector2(x - 50 - (i + 1) * spacing, y)
            enemy2.physics.pos.xy = Vector2(x + 50 + (i + 1) * spacing, y)
        
        enemies.extend([enemy1, enemy2])
        created.extend([enemy1, enemy2])

    return created

# def triangle1(self, x: float, y: float):
#     enemy1 = Enemy1(self.game, x - 50, y - 50)
#     enemy2 = Enemy1(self.game, x + 50, y - 50)
#     enemy3 = Enemy1(self.game, x, y + 20)
#     self.enemies.extend([enemy1, enemy2, enemy3])
#
#
# def triangle2(self, x: float, y: float):
#     enemy1 = Enemy1(self.game, x - 50, y - 50)
#     enemy2 = Enemy1(self.game, x + 50, y - 50)
#     enemy3 = Enemy2(self.game, x, y + 20)
#     self.enemies.extend([enemy1, enemy2, enemy3])
#
#
# def triangle3(self, x: float, y: float):
#     enemy1 = Enemy1(self.game, x - 85, y - 50)
#     enemy2 = Enemy1(self.game, x - 50, y + 10)
#     enemy3 = Enemy1(self.game, x, y + 50)
#     enemy4 = Enemy1(self.game, x + 50, y + 10)
#     enemy5 = Enemy1(self.game, x + 85, y - 50)
#     enemy6 = Enemy2(self.game, x, y - 20)
#     self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])
#
#
# def triangle4(self, x: float, y: float):
#     enemy1 = Enemy1(self.game, x - 85, y - 50)
#     enemy2 = Enemy1(self.game, x - 50, y + 10)
#     enemy3 = Enemy1(self.game, x, y + 50)
#     enemy4 = Enemy1(self.game, x + 50, y + 10)
#     enemy5 = Enemy1(self.game, x + 85, y - 50)
#     enemy6 = Enemy3(self.game, x, y - 30)
#     self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6])
#
#
# def triangle5(self, x: float, y: float):
#     enemy1 = Enemy1(self.game, x - 40, y + 40)
#     enemy2 = Enemy1(self.game, x + 40, y + 40)
#     enemy3 = Enemy2(self.game, x - 80, y - 20)
#     enemy4 = Enemy2(self.game, x + 80, y - 20)
#     enemy5 = Enemy3(self.game, x, y)
#     self.enemies.extend([enemy1, enemy2, enemy3, enemy4, enemy5])
