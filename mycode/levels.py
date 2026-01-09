import pygame.time
from mycode.enemies import *
import json
from mycode import spawners

class WaveManager:
    def __init__(self, config_file: str):
        with open(config_file, "r") as f:
            self.config = json.load(f)
    
    def spawn_wave(self, level_number: int, wave_number: int, enemies: list[BaseEnemy]):
        wave = self.config['levels'][level_number - 1]['waves'][wave_number]
        if not wave:
            return

        wave_type = wave["type"]
        x, y = wave["x"], wave["y"]
        enemy_type = wave["enemy_type"]

        if wave_type == "single":
            spawners.add_single(enemies, x, y, enemy_type)
        elif wave_type == "pair":
            spawners.pair(enemies, x, y, enemy_type)
        elif wave_type == "line":
            enemy_count = wave.get("enemy_count", 1)
            spawners.line(enemies, x, y, enemy_count, enemy_type)


class LevelManager:
    def __init__(self, waveManager: WaveManager):
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.point_time = 0
        self.wave_number = 0
        self.flag = True
        self.waveManager = waveManager
    
    @staticmethod
    def check_if_all_died(enemies: list[BaseEnemy]):
        if len(enemies) == 0:
            return True
        else:
            return False
    
    def tick(self, level_number: int, enemies: list[BaseEnemy]):
        self.current_time = pygame.time.get_ticks()
        
        if self.check_if_all_died(enemies) and self.flag:
            self.flag = False
            self.point_time = pygame.time.get_ticks()
            self.wave_number += 1
        elif self.check_if_all_died(enemies) and not self.flag and self.current_time - self.point_time >= 1500:
            self.flag = True
            self.waveManager.spawn_wave(level_number, self.wave_number, enemies)

# class Level:
#     def __init__(self, game):
#         self.game = game
#         self.block = MiniLevel(game)
#
#         # reset player's ship's stats
#         self.game.player.current_ship.hp.maximise_hp()
#         for slot in self.game.player.current_ship.slots:
#             try:
#                 slot.weapon.clip.maximise_ammo()
#             except AttributeError:
#                 pass
#
#     def check_if_all_died(self):
#         if len(self.game.menuHandler.currentMenu.enemies) == 0:
#             return True
#         else: return False
#
# class Level1(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.add_single(Enemy1(self.game, self.game.width/2, 100))
#                 case 2:
#                     self.block.pair(self.game.width / 2, 100, 1)
#                 case 3:
#                     self.block.line(self.game.width/2, 100, 3, 1)
#                 case _:
#                     self.game.player.add_coins(500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level2(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.pair(self.game.width / 2, 100, 1)
#                 case 2:
#                     self.block.triangle1(self.game.width/2, 100)
#                 case 3:
#                     self.block.line(self.game.width/2, 100, 4, 1)
#                 case _:
#                     self.game.player.add_coins(750)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level3(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.add_single(Enemy2(self.game, self.game.width/2, 100))
#                 case 2:
#                     self.block.line(self.game.width/2, 100, 3)
#                 case 3:
#                     self.block.triangle2(self.game.width/2, 100)
#                 case 4:
#                     self.block.pair(self.game.width/2, 150)
#                 case _:
#                     self.game.player.add_coins(1000)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level4(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.line(self.game.width / 2, 100, 3)
#                 case 2:
#                     self.block.triangle1(self.game.width/4, 100)
#                     self.block.triangle1(self.game.width*3/4, 100)
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 6)
#                 case 4:
#                     self.block.pair(self.game.width/2, 100, 2)
#                 case 5:
#                     self.block.line(self.game.width / 2, 100, 3)
#                     self.block.triangle1(self.game.width / 2, 200)
#                 case _:
#                     self.game.player.add_coins(1500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level5(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1500:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.line(self.game.width / 2, 100, 3, 2)
#                 case 2:
#                     self.block.triangle3(self.game.width/2, 100)
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 8)
#                 case 4:
#                     self.block.pair(self.game.width/2, 150, 2)
#                 case 5:
#                     self.block.line(self.game.width / 2, 100, 3, 2)
#                 case _:
#                     self.game.player.add_coins(2000)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level6(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.triangle3(self.game.width*4/5, 100)
#                     self.block.triangle3(self.game.width/5, 100)
#                 case 2:
#                     self.block.triangle2(self.game.width/2, 100)
#                     self.block.triangle2(self.game.width/5, 100)
#                     self.block.triangle2(self.game.width*4/5, 100)
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 3)
#                     self.block.line(self.game.width / 2, 200, 3)
#                 case 4:
#                     self.block.line(self.game.width / 2, 100, 3, 5)
#                 case _:
#                     self.game.player.add_coins(2500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level7(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.triangle2(self.game.width / 5, 100)
#                     self.block.line(self.game.width / 2, 100, 3)
#                     self.block.triangle2(self.game.width * 4 / 5, 100)
#                 case 2:
#                     self.block.line(self.game.width / 2, 100, 6, 2)
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 5)
#                     self.block.line(self.game.width / 2, 200, 5)
#                 case 4:
#                     self.block.triangle3(self.game.width / 2, 150)
#                 case 5:
#                     self.block.pair(self.game.width*3/4, 100, 2)
#                     self.block.pair(self.game.width/4, 100, 2)
#                 case _:
#                     self.game.player.add_coins(3500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level8(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.add_single(Enemy3(self.game, self.game.width/2, 150))
#                 case 2:
#                     self.block.add_single(Enemy3(self.game, self.game.width / 2, 150))
#                     self.block.add_single(Enemy1(self.game, self.game.width / 4, 100))
#                     self.block.add_single(Enemy1(self.game, self.game.width * 3 / 4, 100))
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 3, 2)
#                     self.block.line(self.game.width / 2, 200, 3, 2)
#                 case 4:
#                     self.block.triangle2(self.game.width / 4, 150)
#                     self.block.triangle2(self.game.width * 3 / 4, 150)
#                 case _:
#                     self.game.player.add_coins(4500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
#
# class Level9(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.triangle4(self.game.width/2, 150)
#                 case 2:
#                     self.block.add_single(Enemy3(self.game, self.game.width / 2, 150))
#                     self.block.add_single(Enemy2(self.game, self.game.width / 4, 100))
#                     self.block.add_single(Enemy2(self.game, self.game.width * 3 / 4, 100))
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 7)
#                     self.block.line(self.game.width / 2, 200, 7)
#                 case 4:
#                     self.block.triangle3(self.game.width / 4, 150)
#                     self.block.triangle3(self.game.width * 3 / 4, 150)
#                 case 5:
#                     self.block.triangle5(self.game.width/2, 150)
#                 case _:
#                     self.game.player.add_coins(6000)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
#
# class Level10(Level):
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.line(self.game.width / 2, 50, 6)
#                     self.block.line(self.game.width / 2, 150, 6)
#                     self.block.line(self.game.width / 2, 250, 6)
#                 case 2:
#                     self.block.pair(self.game.width/2, 150, 3)
#                 case 3:
#                     self.block.line(self.game.width / 2, 100, 8, 2)
#                 case 4:
#                     self.block.triangle5(self.game.width/5, 150)
#                     self.block.triangle5(self.game.width*4/5, 150)
#                 case _:
#                     self.game.player.add_coins(7500)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
# class Level11(Level):
#
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0: pass
#                 case 1:
#                     self.block.add_single(Bouncer1(self.game, 300, 200))
#                 case _:
#                     self.game.player.add_coins(10000)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
#
# class Level12(Level):
#
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0:
#                     pass
#                 case 1:
#                     self.block.add_single(Bouncer2(self.game, 300, 200))
#                 case 2:
#                     self.block.add_single(Bouncer1(self.game, 300, 200))
#                     self.block.add_single(Bouncer1(self.game, 200, 300))
#                 case _:
#                     self.game.player.add_coins(10000)
#                     self.game.menuHandler.changeMenu(GameMenu)
#
#
# class Level13(Level):
#
#     def __init__(self, game):
#         super().__init__(game)
#         self.clock = pygame.time.Clock()
#         self.current_time = 0
#         self.point_time = 0
#         self.wave_number = 0
#         self.flag = True
#
#     def tick(self):
#         self.current_time = pygame.time.get_ticks()
#
#         if self.check_if_all_died() and self.flag:
#             self.flag = False
#             self.point_time = pygame.time.get_ticks()
#             self.wave_number += 1
#         elif self.check_if_all_died() and not self.flag and self.current_time - self.point_time >= 1400:
#             self.flag = True
#             match self.wave_number:
#                 case 0:
#                     pass
#                 case 1:
#                     self.block.add_single(Bouncer2(self.game, random.randint(0, 300), random.randint(0, 300)))
#                     self.block.add_single(Bouncer2(self.game, random.randint(400, 750), random.randint(0, 300)))
#                 case 2:
#                     self.block.add_single(Bouncer1(self.game, 100, 100))
#                     self.block.add_single(Bouncer2(self.game, random.randint(0, 750), random.randint(0, 350)))
#                     self.block.add_single(Bouncer1(self.game, 650, 100))
#                 case 3:
#                     self.block.add_single(Bouncer1(self.game, random.randint(0, 750), random.randint(0, 350)))
#                     self.block.add_single(Bouncer1(self.game, random.randint(0, 750), random.randint(0, 350)))
#                     self.block.add_single(Bouncer1(self.game, random.randint(0, 750), random.randint(0, 350)))
#                     self.block.add_single(Bouncer1(self.game, random.randint(0, 750), random.randint(0, 350)))
#                 case _:
#                     self.game.player.add_coins(10000)
#                     self.game.menuHandler.changeMenu(GameMenu)
