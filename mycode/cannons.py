import pygame
import math
from mycode.bullets import *
from mycode.other import AmmoBar

class Clip:
    def __init__(self, game, max_ammo:int, reload_time:float, active_reload:bool=False,
                 bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        self.game = game
        self.max_ammo = max_ammo
        self.current_ammo = max_ammo
        self.reload_time = reload_time
        self.active = active_reload
        self.reloading = False

        self.clock = 0

        self.ammo_bar = AmmoBar(game, self.max_ammo, bar_width, bar_height, bar_x, bar_y)

    def maximise_ammo(self):
        self.current_ammo = self.max_ammo
        self.ammo_bar.fill()

    def shot(self):
        self.current_ammo -= 1
        self.ammo_bar.decrease_by(1)

    def can_i_shoot(self):
        if self.current_ammo > 0:
            return True
        # If ammo is equal or below 0, then undeniably returns False
        return False

    def tick(self):
        self.ammo_bar.tick()
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
                self.ammo_bar.increase_by(1)
        self.ammo_bar.draw()

class Gun:
    def __init__(self, game, ship, translation, force, interval, key, max_ammo:int, reload_time:float, active_reload:bool,
                 bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.key = key

        self.clock = 0
        self.bullets = []
        self.clip = Clip(game, max_ammo, reload_time, active_reload, bar_width, bar_height, bar_x, bar_y)

    def shot(self):
        pass

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        self.clip.tick()
        pressed = pygame.key.get_pressed()

        if (pressed[pygame.K_KP_0] or pressed[self.key]) and self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()

        for bullet in self.bullets:
            bullet.tick()

class GunPrototype(Gun):
    def __init__(self, game, ship, translation, force, interval, bul, clip_size, reload_time, active_reload:bool=False,
                 key=pygame.K_KP_0, bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        super().__init__(game, ship, translation, force, interval, key, clip_size, reload_time, active_reload,
                         bar_width, bar_height, bar_x, bar_y)
        self.bul = bul

    def shot(self):
        bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force)
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

class LaserLight(GunPrototype):
    def __init__(self, game, ship, translation, force, key=pygame.K_KP_0,
                 bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        super().__init__(
            game, ship, translation, force,
            interval=0.2,
            bul=BulletSmallBlue,
            clip_size=50,
            reload_time=1.0,
            key=key,
            bar_width=bar_width, bar_height=bar_height, bar_x=bar_x, bar_y=bar_y
        )

class ShotGun(Gun):
    def __init__(self, game, ship, translation, force, interval, bul, angles, clip_size, reload, active_reload:bool=False,
                 key=pygame.K_KP_0, bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        super().__init__(game, ship, translation, force, interval, key, clip_size, reload, active_reload,
                         bar_width, bar_height, bar_x, bar_y)
        self.bul = bul
        self.angles = angles

    def shot(self):
        for angle in self.angles:
            bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force, angle)
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            self.clip.shot()

class Flamethrower(Gun):
    def __init__(self, game, ship, translation, force, interval, particle, spread, clip_size, reload, active_reload:bool=False,
                 key=pygame.K_KP_0, bar_width:int=300, bar_height:int=18, bar_x:int=165, bar_y:int=685):
        super().__init__(game, ship, translation, force, interval, key, clip_size, reload, active_reload,
                         bar_width, bar_height, bar_x, bar_y)
        self.particle = particle
        self.spread_angle = spread

    def shot(self):
        par = self.particle(self.game, self.pos.x, self.pos.y, 2, 20,self.force)
        self.bullets.append(par)
        self.clip.shot()

