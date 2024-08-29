import pygame
from pygame import mixer
from pygame.math import Vector2
from mycode import NoShooting
mixer.init()

class ImageBullet(NoShooting):
    def __init__(self, game, gun, x, y, path, mass, force, angle, damage, sound: str = "", scale=1.0):
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        super().__init__(game, x, y, self.image, mass, scale)
        self.add_force(Vector2(0, -force).rotate(angle))

        self.gun = gun
        self.damage = damage

        if sound != "":
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)

        self.line = None

        self.steered_by_menu = False

    def check_collision(self, ship):
        if self.line is not None:
            if (ship.mask.overlap(self.mask, (
                    (self.pos.x - self.width / 2) - ship.hitbox.x, (self.pos.y - self.height / 2) - ship.hitbox.y))
                    or ship.hitbox.clipline(self.line)):
                return True
            return False
        elif ship.mask.overlap(self.mask, (
                (self.pos.x - self.width / 2) - ship.hitbox.x, (self.pos.y - self.height / 2) - ship.hitbox.y)):
            return True
        return False

    def tick(self):
        # Checking if the target of a bullet is in between of last bullet position and new bullet position
        # making it too far jump per one frame

        # drawing a line
        # if self.vel.y * self.game.dt > self.height or self.vel.x * self.game.dt > self.width:
        new_pos: Vector2 = self.pos + (((self.vel * self.current_slip) + self.acc) * self.game.dt)
        self.line = ((self.pos.x, self.pos.y), (new_pos.x, new_pos.y))

        if self.pos.y < 0:
            self.gun.bullets.remove(self)

        if self.gun.is_player:
            for enemy in self.game.menuHandler.currentMenu.enemies:
                if self.check_collision(enemy):
                    enemy.hp.get_damage(self.damage)
                    try:
                        self.gun.bullets.remove(self)
                    except ValueError:
                        pass
        else:
            if self.check_collision(self.game.player.current_ship):
                self.game.player.current_ship.hp.get_damage(self.damage)
                try:
                    if not self.steered_by_menu:
                        self.gun.bullets.remove(self)
                    else:
                        self.game.menuHandler.currentMenu.other_bullets.remove(self)
                except ValueError:
                    pass

        super().tick()

    def draw(self):
        # self.game.screen.blit(self.surf, (self.pos.x - self.width/2, self.pos.y - self.height/2))
        super().draw()
        # pygame.draw.rect(self.game.screen, (255,0,0), self.hitbox, 1)

class BulletSmallBlue(ImageBullet):
    def __init__(self, game, gun, x, y, force, angle=0):
        super().__init__(
            game, gun, x, y,
            path="./images/Laser Sprites/01.png",
            mass=2,
            force=force,
            angle=angle,
            damage=5,
            sound="./sounds/shot_sounds/laser-light-gun.wav",
            scale=0.5
        )


class BulletMediumBlue(ImageBullet):
    def __init__(self, game, gun, x, y, force, angle=0):
        super().__init__(
            game, gun, x, y,
            path="./images/Laser Sprites/11.png",
            mass=2,
            force=force,
            angle=angle,
            damage=5,
            sound="./sounds/shot_sounds/laser-light-gun.wav",
            scale=0.5
        )
        self.damage = 10


class ShotgunBulletFire(ImageBullet):
    def __init__(self, game, gun, x, y, force, angle=0):
        super().__init__(
            game, gun, x, y,
            path="./images/shotgun_bullet.png",
            mass=1,
            force=force,
            angle=angle,
            damage=1,
            sound="./sounds/shot_sounds/laser-light-gun.wav",
            scale=0.1
        )


class Particle(NoShooting):
    def __init__(self, game, x, y, radius, mass, force, angle, damage=1):
        self.game = game
        self.radius = radius

        self.surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)

        self.mass = mass
        self.force = force

        self.alpha = 100
        self.green = 0
        super().__init__(game, x, y, self.surf, mass)
        self.add_force(Vector2(0, -force).rotate(angle))

        self.base_damage = damage
        self.damage = self.base_damage

    def check_collision(self, ship):
        return self.hitbox.colliderect(ship.hitbox)

    def tick(self):
        if self.clock > 0.05:
            self.clock -= 0.05
            if self.alpha > 5:
                self.alpha -= 1 * self.game.dt
            if self.green < 230:
                self.green += 200 * self.game.dt
                if self.green > 230: self.green = 230
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


class LaserL(NoShooting):
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
