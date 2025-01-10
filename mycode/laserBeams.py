from mycode.projectile import Projectile


class LaserBeam(Projectile):
    def __init__(self, game, laser, x, y, damage=10):
        self.laser = laser
        super().__init__(game, x, y, pygame.Surface((0, 0)), 0)
        self.line = ((0, 0), (0, 0))
        self.base_damage = damage
        self.damage = self.base_damage
    
    def check_collision(self, ship):
        return ship.hitbox.clipline(self.line)
    
    def tick(self):
        coords = self.laser.slot.ship.getClosestEnemy()
        if coords is not None and self.laser.active:
            self.line = (
                (self.laser.slot.pos.x + self.laser.slot.translation.x,
                 self.laser.slot.pos.y + self.laser.slot.translation.y),
                coords
                # if coords is not None else (
                #     self.laser.slot.pos.x + self.laser.slot.translation.x,
                #     self.laser.slot.pos.y + self.laser.slot.translation.y)
            )
            self.damage = self.base_damage * self.game.dt
            if self.laser.is_player:
                for enemy in self.game.menuHandler.currentMenu.enemies:
                    if self.check_collision(enemy):
                        enemy.hp.get_damage(self.damage)
            else:
                if self.check_collision(self.game.player.current_ship):
                    self.game.player.current_ship.hp.get_damage(self.damage)
        else:
            self.line = None
        del coords
    
    def draw(self):
        if self.line is not None:
            pygame.draw.line(self.game.screen, (255, 255, 255), self.line[0], self.line[1], 2)
