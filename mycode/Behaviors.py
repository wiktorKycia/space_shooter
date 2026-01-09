import pygame
from pygame.math import *
import random

class Behavior:
    def __init__(self, game, enemy):
        self.orders = []
        self.enemy = enemy
        self.game = game
        self.process_time = 0.5
        self.clock = 0

    def tick(self):
        self.clock += self.game.dt
        # self.enemy.tick()
        if self.clock > self.process_time:
            self.clock = 0
            if self.enemy.hp.hp / self.enemy.hp.max_hp > 1 / 2 and not self.enemy.slots[0].weapon.clip.reloading:
                self.enemy.is_shooting = True
                self.enemy.destination_x = self.game.player.current_ship.pos.x
                self.enemy.destination_y = 100
            else:
                self.enemy.is_shooting = False
                if abs(self.game.player.current_ship.pos.x - self.enemy.pos.x) < 30:
                    if self.game.player.current_ship.pos.x > 350:
                        self.enemy.destination_x = random.randint(0, 200)
                    else:
                        self.enemy.destination_x = random.randint(550, 750)
