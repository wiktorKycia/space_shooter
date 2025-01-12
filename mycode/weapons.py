import pygame
import math
from mycode.bullets import *
from typing import Callable
from abc import ABC, abstractmethod
import random
from clips import *

class Weapon:
    def __init__(self, trigger: Callable):
        self.trigger = trigger
        self.clock = 0
    
    def tick(self, dt):
        self.clock += dt
    
    def draw(self, screen: pygame.Surface):
        pass


class Gun(Weapon):
    def __init__(self, trigger: Callable, bullet_name: str, force: int, interval: float, spread: int, clip: Clip):
        super().__init__(trigger)
        self.interval: float = interval
        self.bullet_name: str = bullet_name
        self.bullets: list[Bullet] = []
        self.clip: Clip = clip
        self.spread: int = spread
        self.force: int = force
    
    @staticmethod
    def _create_bullet(bullet_name: str, x: float, y: float, initial_force: int, rotation: float) -> Bullet:
        builder = BulletBuilder()
        director = BulletBuilderDirector(builder, bullet_name)
        bullet: Bullet = director.build(x, y, initial_force, rotation)
        return bullet
    
    def shot(self, x: float, y: float, ):
        bullet = self._create_bullet(
            self.bullet_name, x, y, self.force,
            random.uniform(-self.spread / 2, self.spread / 2) if self.spread > 0 else 0
        )
        if not self.is_player: bullet.image = pygame.transform.flip(bullet.image, False, True)
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)
        self.clip.shot()
    
    def _shootCheck(self):
        if self.trigger() and self.clock > self.interval and self.clip.can_i_shoot():
            self.clock = 0
            self.shot()

    def tick(self):
        super().tick()
        self.clip.tick()
        pressed = pygame.key.get_pressed()

        if self.is_player:
            self._shootCheck((pressed[pygame.K_KP_0] or pressed[self.key]))
        else:
            self.key = self.slot.ship.is_shooting
            self._shootCheck(self.key)

        for bullet in self.bullets:
            bullet.tick()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()


class KineticLight(Gun):
    def __init__(self, game, slot, key=pygame.K_KP_0):
        super().__init__(
            game, slot, key,
            bullet=BulletSmallBlue,
            force=3500,
            interval=0.1,
            max_ammo=50,
            reload_time=3.0,
            active_reload=False
        )
class KineticMedium(Gun):
    def __init__(self, game, slot, key=pygame.K_KP_0):
        super().__init__(
            game, slot, key,
            bullet=BulletMediumBlue,
            force=3500,
            interval=0.15,
            max_ammo=50,
            reload_time=2.0,
            active_reload=False
        )


class ShotGun(Weapon):
    def __init__(self, game, slot, key, bullet, spread, intensity, force, interval, max_ammo: int, reload_time: float,
                 active_reload: bool):
        super().__init__(game, slot, key)
        self.bullets = []
        self.bul = bullet
        self.spread = [-spread / 2, spread / 2]
        self.bullets_at_once = intensity
        self.interval = interval
        self.clip = Clip(game, max_ammo, reload_time, active_reload)

        if self.is_player:
            self.force = force
        else:
            self.force = -force

    def shot(self):
        for _ in range(self.bullets_at_once):
            bullet = self.bul(self.game, self.slot.weapon, self.slot.pos.x, self.slot.pos.y, self.force,
                              random.uniform(self.spread[0], self.spread[1]))
            self.bullets.append(bullet)
            bullet.sound.play(0, 800)
            self.clip.shot()

    def _shootCheck(self, condition):
        if condition and self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()

    def tick(self):
        super().tick()
        self.clip.tick()
        pressed = pygame.key.get_pressed()

        if self.is_player:
            self._shootCheck((pressed[pygame.K_KP_0] or pressed[self.key]))
        else:
            self.key = self.slot.ship.is_shooting
            self._shootCheck(self.key)

        for bullet in self.bullets:
            bullet.tick()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

class ShotGun1(ShotGun):
    def __init__(self, game, slot, key=pygame.K_KP_0):
        super().__init__(
            game, slot, key,
            bullet=ShotgunBulletFire,
            force=5000,
            interval=0.2,
            spread=10,
            intensity=10,
            max_ammo=1000,
            reload_time=0.01,
            active_reload=True
        )


class Flamethrower(Weapon):
    def __init__(self, game, slot, key, particle, spread, intensity, force, interval, max_ammo: int,
                 reload_time: float, active_reload: bool):
        super().__init__(game, slot, key)
        self.particles = []
        self.particle = particle
        self.spread = [-spread / 2, spread / 2]
        self.intensity = intensity
        self.interval = interval
        self.clip = Clip(game, max_ammo, reload_time, active_reload)

        if self.is_player:
            self.force = force
        else:
            self.force = -force

    def shot(self):
        for _ in range(self.intensity):
            par = self.particle(self.game, self.slot.weapon, 2, 1, self.force,
                                random.uniform(self.spread[0], self.spread[1]))
            self.particles.append(par)
            self.clip.shot()

    def _shootCheck(self, condition):
        if condition and self.clock > self.interval:
            if self.clip.can_i_shoot():
                self.clock = 0
                self.shot()

    def tick(self):
        super().tick()
        self.clip.tick()
        pressed = pygame.key.get_pressed()

        if self.is_player:
            self._shootCheck((pressed[pygame.K_KP_0] or pressed[self.key]))
        else:
            self.key = self.slot.ship.is_shooting
            self._shootCheck(self.key)

        for particle in self.particles:
            particle.tick()

    def draw(self):
        for particle in self.particles:
            particle.draw()


class Flamethrower1(Flamethrower):
    def __init__(self, game, slot, key=pygame.K_KP_0):
        super().__init__(
            game, slot, key,
            particle=Particle,
            force=100,
            interval=0.05,
            spread=5,
            intensity=1,
            max_ammo=100,
            reload_time=2.0,
            active_reload=False
        )


class Laser(Weapon):
    def __init__(self, game, slot, key, laserType, shooting_time, reload_time):
        super().__init__(game, slot, key)
        self.laser = laserType(game, self, self.slot.pos.x, self.slot.pos.y)
        self.clip = LaserClip(game, shooting_time, reload_time)
        self.active = False

    def shot(self):
        self.active = True

    def _shootCheck(self, condition):
        if condition and self.clip.can_i_shoot():
            self.shot()
        elif not self.clip.can_i_shoot() or not condition:
            self.active = False

    def tick(self):
        super().tick()
        self.clip.tick()
        self.laser.tick()
        pressed = pygame.key.get_pressed()

        if self.is_player:
            self._shootCheck((pressed[pygame.K_KP_0] or pressed[self.key]))
        else:
            self.key = self.slot.ship.is_shooting
            self._shootCheck(self.key)

    def draw(self):
        self.laser.draw()


class Laser1(Laser):
    def __init__(self, game, slot, key=pygame.K_KP_0):
        super().__init__(
            game, slot, key,
            laserType=LaserL,
            shooting_time=10.0,
            reload_time=5.0
        )
