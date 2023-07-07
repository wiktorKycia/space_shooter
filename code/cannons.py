import pygame
import math
from code.bullets import *

class BaseCannon:
    def __init__(self, game, ship, translation: Vector2, force: int, interval: float, barrel_length, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0
        self.barrel = barrel_length

    def shot(self):
        pass

    def calculate_kickback_force(self, bullet):
        acc = -bullet.acc  # getting initial bullet velocity
        try: # time that bullet spent in the barrel
            tim = Vector2(math.sqrt(2 * self.barrel / acc.x), math.sqrt(2 * self.barrel / acc.y))
        except ZeroDivisionError:
            if acc.x == 0:
                tim = Vector2(0, math.sqrt(2 * self.barrel / acc.y))
            elif acc.y == 0:
                tim = Vector2(math.sqrt(2 * self.barrel / acc.x), 0)
        vel1 = Vector2(acc.x * tim.x, acc.y * tim.y)        # getting vel of the bullet after escaping from barrel
        vel = (bullet.mass * vel1) / self.ship.mass # getting initial velocity from zasada zachowania pędu
        vel.x *= vel.x
        vel.y *= vel.y
        energy = (self.ship.mass * vel) / 2  # calculating kinetic energy
        force = energy / self.barrel  # calculating kickback force
        return force

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        # self.rect.center = self.pos
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval:
            self.clock = 0
            self.shot()

class BaseShotGun:
    def __init__(self):
        pass

class Kinetic60Gun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

        # self.rect = pygame.Rect(self.pos.x - 5, self.pos.y - 10, 10, 20)

    def shot(self):
        bullet = Kinetic60Bullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 120)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

    def calculate_kickback_force(self, bullet):
        return super().calculate_kickback_force(bullet)
    def tick(self):
        super().tick()

    def draw(self):
        # pygame.draw.rect(self.game.screen, (255, 255, 255), self.rect)
        pass

class Kinetic9Gun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 50
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = Kinetic9Bullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class KineticGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 60
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = KineticBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class Blaster(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = BlasterBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class EnergyGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 80
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = EnergyGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserCannon(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 200
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserCannonBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLightCannon(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 150
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLightCannonBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLightGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 30
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLightGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserMediumGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 60
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserMediumGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserHeavyGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 90
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserHeavyGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLongGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLongGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        self.ship.add_force(self.calculate_kickback_force(bullet))