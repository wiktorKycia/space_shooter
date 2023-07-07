import pygame
from pygame import mixer
from pygame.math import Vector2
mixer.init()

class Bullet(object):
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.mass = mass
        acc = int(force / mass)
        self.acc = Vector2(0, -acc)

        self.width = width
        self.height = height
        # self.hitbox = pygame.Rect(self.pos.x - width / 2, self.pos.y - height / 2, width, height)
        self.hitbox = pygame.Surface((self.width, self.height))
        self.hitbox.fill(color)
        # self.hitbox.topleft = (self.pos.x, self.pos.y)

        self.mask = pygame.mask.from_surface(self.hitbox)

        self.game = game
        self.color = color

        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)
    def tick(self):
        # Physics
        self.vel *= 0.9995

        self.vel += self.acc
        self.pos += self.vel * self.game.dt
        self.acc *= 0
    def draw(self):
        # self.hitbox = pygame.Rect(self.pos.x - self.width / 2, self.pos.y - self.height / 2, self.width, self.height)
        # pygame.draw.rect(self.game.screen, self.color, self.hitbox)
        # self.hitbox.topleft = (self.pos.x, self.pos.y)
        self.game.screen.blit(self.hitbox, (self.pos.x - self.width/2, self.pos.y - self.height/2))

class ShotGunBullet:
    def __init__(self):
        pass

class Kinetic60Bullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 2
        self.height = 2
        self.force = force
        self.mass = 1.0
        self.color = (200, 210, 55)
        self.sound = "./sounds/shot_sounds/M60-single.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class Kinetic9Bullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 3
        self.height = 6
        self.force = force
        self.mass = 1.3
        self.color = (90, 90, 100)
        self.sound = "./sounds/shot_sounds/gunshot.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class KineticBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 2
        self.height = 4
        self.force = force
        self.mass = 2.0
        self.color = (130, 130, 120)
        self.sound = "./sounds/shot_sounds/kinetic-gun.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()


class BlasterBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 5
        self.height = 30
        self.force = force
        self.mass = 5.0
        self.color = (120, 230, 180)
        self.sound = "./sounds/shot_sounds/blaster.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class EnergyGunBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 5
        self.height = 15
        self.force = force
        self.mass = 7.0
        self.color = (230, 150, 150)
        self.sound = "./sounds/shot_sounds/energy-gun.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()


class LaserCannonBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 4
        self.height = 50
        self.force = force
        self.mass = 50.0
        self.color = (140, 220, 220)
        self.sound = "./sounds/shot_sounds/laser-cannon.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class LaserLightCannonBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 4
        self.height = 40
        self.force = force
        self.mass = 8.0
        self.color = (120, 230, 210)
        self.sound = "./sounds/shot_sounds/laser-cannon-light.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()


class LaserLightGunBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 3
        self.height = 8
        self.force = force
        self.mass = 3.0
        self.color = (150, 210, 150)
        self.sound = "./sounds/shot_sounds/laser-light-gun.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class LaserMediumGunBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 4
        self.height = 10
        self.force = force
        self.mass = 6.0
        self.color = (150, 210, 150)
        self.sound = "./sounds/shot_sounds/laser-medium-gun.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class LaserHeavyGunBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 4
        self.height = 12
        self.force = force
        self.mass = 10.0
        self.color = (150, 210, 150)
        self.sound = "./sounds/shot_sounds/laser-heavy-gun.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

class LaserLongGunBullet(Bullet):
    def __init__(self, game, x, y, force):
        self.width = 4
        self.height = 40
        self.force = force
        self.mass = 9.0
        self.color = (150, 210, 150)
        self.sound = "./sounds/shot_sounds/laser-long-gun.mp3"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()