import pygame
import math
from mycode.bullets import *
# from mycode.other import AmmoBar

class Clip:
    def __init__(self, game, max_ammo: int, reload_time: float, active_reload: bool = False):
        self.game = game
        self.max_ammo = max_ammo
        self.current_ammo = max_ammo
        self.reload_time = reload_time
        self.active = active_reload
        self.reloading = False

        self.clock = 0

        # self.ammo_bar = AmmoBar(game, self.max_ammo, bar_width, bar_height, bar_x, bar_y)

    def maximise_ammo(self):
        self.current_ammo = self.max_ammo
        # self.ammo_bar.fill()

    def shot(self):
        self.current_ammo -= 1
        # self.ammo_bar.decrease_by(1)

    def can_i_shoot(self):
        if self.current_ammo > 0:
            return True
        # If ammo is equal or below 0, then undeniably returns False
        return False

    def tick(self):
        # self.ammo_bar.tick()
        # there is no ammo, passive reloading
        if not self.active:
            # it is not reloading
            if not self.reloading:
                if self.current_ammo <= 0:
                    self.reloading = True
            # it is reloading
            if self.reloading:
                self.clock += self.game.dt
                if self.clock > self.reload_time:
                    self.clock = 0
                    self.reloading = False
                    self.maximise_ammo()
        # active reloading
        else:
            self.clock += self.game.dt
            if self.clock > self.reload_time and self.current_ammo < self.max_ammo:
                self.current_ammo += 1
                self.clock = 0
                # self.ammo_bar.increase_by(1)
        # self.ammo_bar.draw()


class Weapon:
    def __init__(self, game, ship, weaponType: int, translation):
        self.game = game
        self.ship = ship
        self.weaponType = weaponType
        self.translation = translation


class Gun(Weapon):
    def __init__(self, game, ship, weaponType, translation, force, interval, key, max_ammo: int, reload_time: float,
                 active_reload: bool):
        super().__init__(game, ship, weaponType, translation)
        self.pos = ship.pos
        self.interval = interval
        # self.key = key

        self.clock = 0
        self.bullets = []
        self.clip = Clip(game, max_ammo, reload_time, active_reload)

        if type(key) == int:
            # if passed pygame.key value
            self.is_player = True
            self.force = force
            self.key: int = key
        else:
            # if passed other bool type variable
            self.is_player = False
            self.force = -force
            self.key: bool = key

    def shot(self):
        pass

    def _shootCheck(self, condition):
        if condition and self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        self.clip.tick()
        pressed = pygame.key.get_pressed()

        if self.is_player:
            self._shootCheck((pressed[pygame.K_KP_0] or pressed[self.key]))
        else:
            self.key = self.ship.is_shooting
            self._shootCheck(self.key)

        for bullet in self.bullets:
            bullet.tick()

class GunPrototype(Gun):
    def __init__(self, game, ship, weaponType, translation, force, interval, bul, clip_size, reload_time,
                 active_reload: bool = False, key: int = pygame.K_KP_0):
        super().__init__(game, ship, weaponType, translation, force, interval, key, clip_size, reload_time,
                         active_reload)
        self.bul = bul

    def shot(self):
        bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force)
        if not self.is_player: bullet.image = pygame.transform.flip(bullet.image, False, True)
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)
        self.clip.shot()

# class KineticGun(GunPrototype):
#     def __init__(self, game, ship, translation, force, key=pygame.K_KP_0,
#                  bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
#         super().__init__(
#             game, ship, translation, force,
#             interval=0.5,
#             bul=KineticBullet,
#             clip_size=10,
#             reload_time=2.5,
#             key=key,
#             bar_width=bar_width, bar_height=bar_height, bar_x=bar_x, bar_y=bar_y
#             )

class KineticLight(GunPrototype):
    def __init__(self, game, ship, translation, key=pygame.K_KP_0):
        self.force = 3500
        super().__init__(
            game, ship,
            weaponType=1,
            translation=translation,
            force=self.force,
            interval=0.1,
            bul=BulletSmallBlue,
            clip_size=50,
            reload_time=3.0, key=key)


class KineticMedium(GunPrototype):
    def __init__(self, game, ship, translation, key=pygame.K_KP_0):
        self.force = 3500
        super().__init__(
            game, ship,
            weaponType=2,
            translation=translation,
            force=self.force,
            interval=0.15,
            bul=BulletMediumBlue,
            clip_size=50,
            reload_time=2.0,
            key=key)

class ShotGun(Gun):
    def __init__(self, game, ship, weaponType, translation, force, interval, bul, angles, clip_size, reload,
                 active_reload: bool = False, key: int = pygame.K_KP_0):
        super().__init__(game, ship, weaponType, translation, force, interval, key, clip_size, reload, active_reload)
        self.bul = bul
        self.angles = angles

    def shot(self):
        for angle in self.angles:
            bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force, angle)
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            self.clip.shot()

class Flamethrower(Gun):
    def __init__(self, game, ship, weaponType, translation, force, interval, particle, spread, clip_size, reload,
                 active_reload: bool = False, key: int = pygame.K_KP_0):
        super().__init__(game, ship, weaponType, translation, force, interval, key, clip_size, reload, active_reload)
        self.particle = particle
        self.spread_angle = spread

    def shot(self):
        par = self.particle(self.game, self.pos.x, self.pos.y, 2, 20,self.force)
        self.bullets.append(par)
        self.clip.shot()