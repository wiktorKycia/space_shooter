import pygame
import os
from main import *
from code import *

class Player(object):
    def __init__(self, game, coins=1500):
        self.game = game
        self.coins = coins

    def add_coins(self, amount:int):
        self.coins += amount