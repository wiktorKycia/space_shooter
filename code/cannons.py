import pygame
import math
from code.bullets import *
from code.other import HP

class Clip:
    def __init__(self, game, max_ammo:int, reload_time:float, active_reload:bool=False):
        self.game = game
        self.max_ammo = max_ammo
        self.current_ammo = max_ammo
        self.reload_time = reload_time
        self.active = active_reload
        self.reloading = False

        self.clock = 0

        self.ammo_bar = HP(game, self.max_ammo, 250, 25, 200, 700, (0, 0, 255))

    def can_i_shoot(self):
        if self.current_ammo > 0 or not self.reloading:
            return True
        return False

    def tick(self):
        self.clock += self.game.dt

        if not self.reloading: # there is ammo, no reload needed
            pass
        elif not self.active: # there is no ammo, passive reloading
            self.reloading = True
        else: # active reloading
            if self.clock > self.reload_time and self.current_ammo < self.max_ammo:
                self.current_ammo += 1
                self.clock = 0

        if self.reloading:
            if self.clock > self.reload_time:
                self.reloading = False
                self.current_ammo = self.max_ammo

    def draw(self):
        pass

class Gun:
    def __init__(self, game, ship, translation, force, interval, direction, key, max_ammo:int, reload_time:float, active_reload:bool):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key
        self.direction = direction

        self.clock = 0
        self.clip = Clip(game, max_ammo, reload_time, active_reload)

    def shot(self):
        pass

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()


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
    def __init__(self, game, ship, translation: Vector2, force: int, interval: float, barrel_length, magazine_size, magazine_reload_time, key=pygame.K_SPACE):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0
        self.barrel = barrel_length

        self.magazine_size = magazine_size
        self.magazine = magazine_size
        self.reload_time = magazine_reload_time
        self.reload_clock = 0

    def shot(self):
        pass

    # def calculate_kickback_force(self, bullet, angle):
    #     acc = bullet.acc  # getting initial bullet velocity
    #     try:  # time that bullet spent in the barrel
    #         print(2 * self.barrel / acc.x)
    #         print(2 * self.barrel / acc.y)
    #
    #         tim = Vector2(math.sqrt(2 * self.barrel / acc.x), math.sqrt(2 * self.barrel / acc.y))
    #     except ZeroDivisionError:
    #         if acc.x == 0:
    #             tim = Vector2(0, math.sqrt(2 * self.barrel / acc.y))
    #         elif acc.y == 0:
    #             tim = Vector2(math.sqrt(2 * self.barrel / acc.x), 0)
    #     vel1 = Vector2(acc.x * tim.x, acc.y * tim.y)  # getting vel of the bullet after escaping from barrel
    #     vel = (bullet.mass * vel1) / self.ship.mass  # getting initial velocity from zasada zachowania pędu
    #     vel.x *= vel.x
    #     vel.y *= vel.y
    #     energy = (self.ship.mass * vel) / 2  # calculating kinetic energy
    #     force = energy / self.barrel  # calculating kickback force
    #     # returning final_acc
    #     final_acc = Vector2(force.x, force.y)
    #     final_acc.rotate(angle)
    #
    #     return final_acc

    def tick(self):
        self.clock += self.game.dt
        self.reload_clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        # self.rect.center = self.pos
        pressed = pygame.key.get_pressed()
        if pressed[self.key] and self.clock > self.interval and self.magazine > 0:
            self.magazine -= 1
            self.clock = 0
            self.shot()
        if self.reload_clock > self.reload_time and self.magazine < self.magazine_size:
            self.magazine += 1
            self.reload_clock = 0

class ShotGun1(BaseShotGun):
    def __init__(self, game, ship, translation, force, interval, key=pygame.K_SPACE):
        self.barrel = 50
        super().__init__(game, ship, translation, force, interval, self.barrel, 5, 1.5, key)

    def shot(self):
        # force1 = self.ship.force.rotate(20)
        # force2 = self.ship.force.rotate(-20)
        bullet1 = ShotGunBullet1(self.game, self.pos.x, self.pos.y, self.ship.force, 10)
        bullet2 = ShotGunBullet1(self.game, self.pos.x, self.pos.y, self.ship.force, -10)
        bullet3 = ShotGunBullet1(self.game, self.pos.x, self.pos.y, self.ship.force, 5)
        bullet4 = ShotGunBullet1(self.game, self.pos.x, self.pos.y, self.ship.force, -5)
        bullet5 = ShotGunBullet1(self.game, self.pos.x, self.pos.y, self.ship.force, 0)
        # bullet1.acc.rotate(20)
        # bullet2.acc.rotate(-20)
        self.ship.bullets.append(bullet1)
        # self.ship.add_force(self.calculate_kickback_force(bullet1))
        self.ship.bullets.append(bullet2)
        self.ship.bullets.append(bullet3)
        self.ship.bullets.append(bullet4)
        self.ship.bullets.append(bullet5)
        # self.ship.acc += self.calculate_kickback_force(bullet1, bullet1.acc.angle_to((0, -1)))
        bullet1.sound.play(0, 800)
        bullet2.sound.play(0, 800)
        bullet3.sound.play(0, 800)
        bullet4.sound.play(0, 800)
        bullet5.sound.play(0, 800)
        # self.ship.add_force(self.calculate_kickback_force(bullet2))


class Kinetic60Gun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

        # self.rect = pygame.Rect(self.pos.x - 5, self.pos.y - 10, 10, 20)

    def shot(self):
        bullet = Kinetic60Bullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 120)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

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
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class KineticGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 60
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = KineticBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class Blaster(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = BlasterBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class EnergyGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 80
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = EnergyGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserCannon(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 200
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserCannonBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLightCannon(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 150
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLightCannonBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLightGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 30
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLightGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserMediumGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 60
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserMediumGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserHeavyGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 90
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserHeavyGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))

class LaserLongGun(BaseCannon):
    def __init__(self, game, ship, translation:Vector2, force:int, interval:float, key=pygame.K_SPACE):
        self.barrel = 100
        super().__init__(game, ship, translation, force, interval, self.barrel, key)

    def shot(self):
        bullet = LaserLongGunBullet(self.game, self.pos.x, self.pos.y, self.ship.force)
        bullet.sound.play(0, 800)
        self.ship.bullets.append(bullet)
        # self.ship.add_force(self.calculate_kickback_force(bullet))