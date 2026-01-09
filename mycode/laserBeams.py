from mycode.spacecraft import Spacecraft
import pygame


class LaserBeam:
    def __init__(self, damage: int = 10):
        self.line: tuple[tuple[float, float], tuple[float, float]] | None = None
        self.damage = damage
    
    def check_collision(self, ship: Spacecraft):
        return ship.displayer.hitbox.clipline(self.line)
    
    def set_aim(self, ship_coords: tuple[float, float], enemy_coords: tuple[float, float], trigger: bool):
        if trigger:
            self.line = (ship_coords, enemy_coords)
    
    def deal_damage(self, damage, enemies: list[Spacecraft]):
        for enemy in enemies:
            if self.check_collision(enemy):
                enemy.hp.damage(damage)
    
    def tick(self, dt, enemies: list[Spacecraft]):
        if self.line is not None:
            self.deal_damage(self.damage * dt, enemies)
        else:
            self.line = None
    
    def draw(self, screen: pygame.Surface):
        if self.line is not None:
            pygame.draw.line(screen, (255, 255, 255), self.line[0], self.line[1], 2)
