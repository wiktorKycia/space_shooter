from __future__ import annotations

from abc import ABC, abstractmethod
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mycode.physics import PygamePhysics
    from mycode.displayable import Displayer
    from mycode.other import RefillableBar
    from mycode.slot import Slot


class Spacecraft(ABC):
    def __init__(self):
        self.displayer: Displayer
        self.physics: PygamePhysics
        self.hp: RefillableBar
        self.slots: list[Slot]
    
    @abstractmethod
    def tick(self, dt: float):
        pass
    
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass
