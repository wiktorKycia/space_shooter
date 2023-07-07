import pygame
import os
from code import *
from code.ships import *

class Player(object):
    def __init__(self, game, coins=1500):
        self.game = game
        self.coins = coins
        self.ships = [Ship0(self.game), Ship1(self.game), Ship2(self.game), Ship3(self.game), Ship4(self.game), Ship5(self.game)]
        # self.add_new_ship(Ship2(self.game))
        self.current_ship = self.ships[2]

    def add_coins(self, amount:int):
        self.coins += amount

    def subtract_coins(self, amount:int):
        self.coins -= amount

    def add_new_ship(self, ship):
        for sh in self.ships:
            if type(sh) == type(ship):
                print("You cannot add the ship to the list, you have this model!")

        self.ships.append(ship)