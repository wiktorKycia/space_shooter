import pygame
import math
from code.bullets import *
from code.other import AmmoBar

class ClipE:
    def __init__(self, game, max_ammo:int, reload_time:float, active_reload:bool=False):
        self.game = game
        self.max_ammo = max_ammo
        self.current_ammo = max_ammo
        self.reload_time = reload_time
        self.active = active_reload
        self.reloading = False

        self.clock = 0

    def maximise_ammo(self):
        self.current_ammo = self.max_ammo

    def shot(self):
        self.current_ammo -= 1

    def can_i_shoot(self):
        if self.current_ammo > 0:
            return True
        return False

    def tick(self):
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

class GunE:
    def __init__(self, game, ship, translation, force, interval, max_ammo:int, reload_time:float, active_reload:bool,):
        self.game = game
        self.ship = ship
        self.pos = ship.pos
        self.translation = translation
        self.force = force
        self.interval = interval
        self.bullets = []

        self.clock = 0
        self.clip = ClipE(game, max_ammo, reload_time, active_reload)

    def shot(self):
        pass

    def tick(self):
        self.clock += self.game.dt
        self.pos = self.ship.pos + self.translation
        self.clip.tick()

        if self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()

        for bullet in self.bullets:
            bullet.tick()

class GunPrototypeE(GunE):
    def __init__(self, game, ship, translation, force, interval, bul, clip_size, reload_time, active_reload:bool=False,):
        super().__init__(game, ship, translation, force, interval, clip_size, reload_time, active_reload)
        self.bul = bul

    def shot(self):
        bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force)
        bullet.image = pygame.transform.flip(bullet.image, True, False)
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)
        self.clip.shot()

class KineticGunE(GunPrototypeE):
    def __init__(self, game, ship, translation, force):
        super().__init__(
            game, ship, translation, force,
            interval=0.5,
            bul=BulletSmallBlue,
            clip_size=10,
            reload_time=2.5,
            )

class ShotGunE(GunE):
    def __init__(self, game, ship, translation, force, interval, bul, angles, clip_size, reload, active_reload:bool=False,):
        super().__init__(game, ship, translation, force, interval, clip_size, reload, active_reload)
        self.bul = bul
        self.angles = angles

    def shot(self):
        for angle in self.angles:
            bullet = self.bul(self.game, self.pos.x, self.pos.y, self.force, angle)
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            self.clip.shot()