from mycode.physics import PygamePhysics
from pygame.math import Vector2

class Projectile:
    def __init__(self, physics: PygamePhysics, damage: int, rotation: float = 0):
        self.physics = physics
        self.physics.add_force(Vector2(0, -self.physics.force).rotate(rotation))
        
        self.damage = damage
