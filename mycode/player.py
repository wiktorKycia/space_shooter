import pygame
import os
from mycode import *
from mycode.ships import *

class Player(object):
    def __init__(self, coins=1500):
        self.coins = coins
        self.ships = [Ship1(), Ship2(), Ship3(), Ship4(), Ship5()]
        self.current_ship = self.ships[0]

    def add_coins(self, amount:int):
        self.coins += amount

    def subtract_coins(self, amount:int):
        self.coins -= amount

    def add_new_ship(self, ship):
        if any(isinstance(ship, type(sh)) for sh in self.ships):
            print("You cannot add the ship to the list, you have this model!")

        self.ships.append(ship)