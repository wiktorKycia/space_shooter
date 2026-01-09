from __future__ import annotations

import pygame
from pygame.math import Vector2
from typing import Callable, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from mycode.weapons import Weapon

class Slot:
    def __init__(self, translation: Vector2, trigger: Callable, weapon: Weapon | None = None):
        """
        Represents a weapon slot of a Ship,
        it can contain only one weapon
        :param translation: pygame.Vector2
        :param trigger: a function returning bool
        :param weapon: any end child class inheriting from Weapon
        """
        self.translation: Vector2 = translation
        self.trigger: Callable = trigger
        self.weapon: Weapon = weapon

    def replace_weapon(self, weapon: Weapon) -> Optional[Weapon]:
        """
        mounts a new weapon onto itself, returns the old one
        """
        if self.weapon:
            wpn = self.weapon
            self.weapon = weapon
            return wpn
        else:
            return None
    
    def tick(self, dt: float, x: float, y: float):
        if self.weapon:
            self.weapon.tick(dt)
            if self.trigger():
                self.weapon.shoot(x, y)
    
    def draw(self, screen: pygame.Surface):
        if self.weapon:
            self.weapon.draw(screen)
