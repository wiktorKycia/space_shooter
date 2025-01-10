from mycode.projectile import Projectile
from mycode.physics import PygamePhysics
from mycode.spacecraft import Spacecraft
import pygame

class Particle(Projectile):
    def __init__(self, physics: PygamePhysics, radius, rotation, damage=1):
        super().__init__(physics, damage, rotation)
        self.radius = radius
        
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        self.alpha = 100
        self.green = 0
        
        self.current_damage = damage
    
    def check_collision(self, ship: Spacecraft):
        return self.hitbox.colliderect(ship.displayer.hitbox)
    
    def tick(self):  # TODO: naprawić: zrobić tak, żeby zadawało damage
        if self.clock > 0.05:
            self.clock -= 0.05
            if self.alpha > 5:
                self.alpha -= 1 * self.game.dt
            if self.green < 230:
                self.green += 200 * self.game.dt
                if self.green > 230:
                    self.green = 230
            self.radius += 30 * self.game.dt
            self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            self.hitbox = self.surf.get_rect()
            self.current_damage = self.alpha / 100 * self.damage
        super().tick()
        # if self.alpha < 10 or self.pos.y < 0:
        #     print("self delete")
        #     del self
    
    def draw(self):
        color = (255, self.green, 0, self.alpha)
        pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), self.radius)
        self.game.screen.blit(self.surf, self.surf.get_rect(center=(self.pos.x, self.pos.y)))
