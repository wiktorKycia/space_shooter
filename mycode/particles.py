from mycode.projectile import Projectile


class Particle(Projectile):
    def __init__(self, game, flamethrower, radius, mass, force, angle, damage=1):
        self.game = game
        self.flamethrower = flamethrower
        self.radius = radius
        
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        self.mass = mass
        self.force = force
        
        self.alpha = 100
        self.green = 0
        super().__init__(game, self.flamethrower.slot.pos.x, self.flamethrower.slot.pos.y, self.surf, mass)
        self.add_force(Vector2(0, -force).rotate(angle))
        
        self.base_damage = damage
        self.damage = self.base_damage
    
    def check_collision(self, ship):
        return self.hitbox.colliderect(ship.hitbox)
    
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
            self.damage = self.alpha / 100 * self.base_damage
        super().tick()
        # if self.alpha < 10 or self.pos.y < 0:
        #     print("self delete")
        #     del self
    
    def draw(self):
        color = (255, self.green, 0, self.alpha)
        pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), self.radius)
        self.game.screen.blit(self.surf, self.surf.get_rect(center=(self.pos.x, self.pos.y)))
