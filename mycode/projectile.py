from __future__ import annotations

from mycode.physics import PygamePhysics
from pygame.math import Vector2

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mycode.spacecraft import Spacecraft
    from mycode.displayable import Displayer


class Projectile:
    def __init__(self):
        self.physics: PygamePhysics | None = None
        self.displayer: Displayer | None = None
        self.damage: int = 0
        self.initial_rotation: float = 0.0
    
    def check_collision(self, ship: Spacecraft) -> bool:
        pass
    
    def tick(self, dt: float):
        pass
    
    def draw(self, dt: float):
        pass
