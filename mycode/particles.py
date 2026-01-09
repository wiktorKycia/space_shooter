# from mycode.projectile import Projectile
# from mycode.physics import PygamePhysics
# from mycode.spacecraft import Spacecraft
# from mycode.displayable import Displayer
# import pygame
#
# class Particle(Projectile):
#     def __init__(self, physics: PygamePhysics, radius, rotation, damage=1):
#         super().__init__(physics, damage, rotation)
#         self.radius = radius
#
#         self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
#
#         self.displayer = Displayer(self.surf)
#
#         self.alpha = 100
#         self.green = 0
#
#         self.current_damage = damage
#
#     def check_collision(self, ship: Spacecraft):
#         return self.displayer.hitbox.colliderect(ship.displayer.hitbox)
#
#     def tick(self, dt):
#         if self.physics.clock > 0.05:
#             self.physics.clock -= 0.05
#             if self.alpha > 5:
#                 self.alpha -= 1 * dt
#             if self.green < 230:
#                 self.green += 200 * dt
#                 if self.green > 230:
#                     self.green = 230
#             self.radius += 30 * dt
#             self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
#             self.displayer.hitbox = self.surf.get_rect()
#             self.current_damage = self.alpha / 100 * self.damage
#
#         self.physics.tick(dt)
#         self.displayer.tick(self.physics.pos.x, self.physics.pos.y)
#
#     def draw(self, screen: pygame.Surface):
#         color = (255, self.green, 0, self.alpha)
#         pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), self.radius)
#         screen.blit(self.surf, self.surf.get_rect(center=(self.physics.pos.x, self.physics.pos.y)))
# TODO: create a builder and builder director for this class
# ! DO NOT DELETE
