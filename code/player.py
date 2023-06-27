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