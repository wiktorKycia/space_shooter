import pygame
import os
from main import *
from code import *

class Player(object):
    def __init__(self, game, coins=1500):
        self.game = game
        self.coins = coins
        self.ships = []

    def add_coins(self, amount:int):
        self.coins += amount

    def add_new_ship(self, ship):
        for sh in self.ships:
            if sh.type() == ship.type():
                print("You cannot add the ship to the list, you have this model!")

        self.ships.append(ship)