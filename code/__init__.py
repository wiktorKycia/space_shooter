import pygame
from code.bullets import *
from code.bullets2 import *
from code.cannons import *
from code.enemies import *
from code.levels import *
from code.maneuvering_cannons import *
from code.other import *
from code.player import *
from code.ships import *
from code.two_players import *
from code.UI import *

from abc import ABC, abstractmethod

class MainObject(object, ABC):
    def __init__(self):
        pass
    @abstractmethod
    def tick(self):
        pass
    @abstractmethod
    def draw(self):
        pass

class StaticObject(MainObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y

