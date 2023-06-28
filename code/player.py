import pygame
import os
from code import *

class Player(object):
    def __init__(self, game, coins=1500):
        self.game = game
        self.coins = coins
        self.ships = []
        self.add_new_ship(Ship1(self.game))
        self.current_ship = self.ships[0]

    def add_coins(self, amount:int):
        self.coins += amount

    def subtract_coins(self, amount:int):
        self.coins -= amount

    def add_new_ship(self, ship):
        for sh in self.ships:
            if type(sh) == type(ship):
                print("You cannot add the ship to the list, you have this model!")

        self.ships.append(ship)