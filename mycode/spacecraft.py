from abc import ABC, abstractmethod
import pygame
from mycode.physics import PygamePhysics
from mycode.displayable import Displayer
from mycode.other import RefillableBar
from mycode.slot import Slot


class Spacecraft(ABC):
    def __init__(self, physics: PygamePhysics, healthBar: RefillableBar, image: pygame.Surface, scale: float = 1.0):
        self.displayer = Displayer(image, scale)
        self.physics: PygamePhysics = physics
        self.hp = healthBar
        
        self.slots: list[Slot] = []
    
    @abstractmethod
    def tick(self, dt: float):
        pass
    
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass
