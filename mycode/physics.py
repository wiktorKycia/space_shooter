import pygame
from pygame.math import Vector2
from abc import ABC


@ABC
class Physics:
    pass


class PygamePhysics(Physics):
    def __init__(self, x: int, y: int, mass: int, power: int, slip: float = 0.98):
        self.pos: Vector2 = Vector2(x, y)
        self.vel: Vector2 = Vector2(0, 0)
        self.acc: Vector2 = Vector2(0, 0)
        
        self.clock: float = 0
        
        self.mass: int = mass
        self.force: int = power
        
        self.slip: float = slip
        self.current_slip: float = slip
    
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
