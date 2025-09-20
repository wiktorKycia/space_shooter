import pygame
from pygame.math import Vector2


class PygamePhysics:
    def __init__(self, x: float, y: float, mass: int, force: int, is_player: bool = True, slip: float = 0.98):
        self.pos: Vector2 = Vector2(x, y)
        self.vel: Vector2 = Vector2(0, 0)
        self.acc: Vector2 = Vector2(0, 0)
        
        self.clock: float = 0
        
        self.mass: int = mass
        self.force: int = force if is_player else -force
        
        self.slip: float = slip
        self.current_slip: float = slip
    
    @property
    def x(self) -> float:
        return self.pos.x
    
    @property
    def y(self) -> float:
        return self.pos.y
    
    def add_force(self, force: pygame.Vector2):
        """
        a method that adds force to the object,
        you can't specify the mass as it uses the mass object to calculate acceleration.
        then adds it to acc vector of the object
        :param force: must be the pygame 2-dimensional Vector
        :return:
        """
        self.acc += force / self.mass
    
    def tick(self, dt: float):
        """
        Updates the clock,
        multiplies the vel by slip and adds acc to vel,
        then, limits the vel if it is above max_speed,
        lastly, updates the position by vel and resets acc to 0
        :return:
        """
        self.clock += dt
        
        self.vel *= self.current_slip
        self.vel += self.acc
        
        # Limiting speed
        # if self.vel.x > self.max_speed:  # right
        #     self.vel = Vector2(self.max_speed, self.vel.y)
        # elif self.vel.x < -self.max_speed:  # left
        #     self.vel = Vector2(-self.max_speed, self.vel.y)
        # if self.vel.y > self.max_speed:  # up
        #     self.vel = Vector2(self.vel.x, self.max_speed)
        # elif self.vel.y < -self.max_speed:  # down
        #     self.vel = Vector2(self.vel.x, -self.max_speed)
        
        self.pos += self.vel * dt
        self.acc *= 0
