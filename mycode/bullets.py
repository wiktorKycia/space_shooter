import pygame
from pygame import mixer
from pygame.math import Vector2
from mycode import NoShooting
mixer.init()

class ImageBullet(NoShooting):
    def __init__(self, game, x, y, path, mass, force, sound:str="", scale=1.0):
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        super().__init__(game, x, y, self.image, mass, scale)
        self.add_force(Vector2(0, -force))

        # reinitialize hitbox
        # self.surf = self.mask.to_surface().convert_alpha()
        #
        # self.width = self.surf.get_width()
        # self.height = self.surf.get_height()
        #
        # self.hitbox = self.surf.get_rect()

        if sound != "":
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)

    def check_collision(self, ship):
        if ship.mask.overlap(self.mask, ((self.pos.x - self.width/2) - ship.hitbox.x, (self.pos.y - self.height/2) - ship.hitbox.y)):
            return True
        return False

    def tick(self):
        super().tick()

    def draw(self):
        # self.game.screen.blit(self.surf, (self.pos.x - self.width/2, self.pos.y - self.height/2))
        super().draw()
        # pygame.draw.rect(self.game.screen, (255,0,0), self.hitbox, 1)

class BulletSmallBlue(ImageBullet):
    def __init__(self, game, x, y, force):
        super().__init__(
            game, x, y,
            path="./images/Laser Sprites/01.png",
            mass=2,
            force=force,
            sound="./sounds/shot_sounds/laser-light-gun.wav",
            scale=0.5)



class Particle:
    def __init__(self, game, x, y, radius, mass, force):
        self.game = game
        self.x = x
        self.y = y
        self.radius = radius

        self.surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)

        self.mass = mass
        self.force = force

        self.alpha = 100
        self.clock = 0
        self.green = 0

    def tick(self):
        self.clock += self.game.dt
        if self.clock > 0.15:
            self.clock -= 0.15
            if self.alpha > 5:
                self.alpha -= 1
            if self.green >= 150:
                self.green += 1
            self.radius += 1
            if self.alpha == 5:
                del self

    def draw(self):
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        color = (255, self.green, 0, self.alpha)
        pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), self.radius)
        self.game.screen.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))



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
    def __init__(self, game, x, y, width, height, force, mass, angle,color=(255, 255, 255), sound=None):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.mass = mass
        acc = int(force / mass)
        self.acc = Vector2(0, -acc).rotate(angle)

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
        self.game.screen.blit(self.hitbox, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))

class ShotGunBullet1(ShotGunBullet):
    def __init__(self, game, x, y, force, angle):
        self.width = 3
        self.height = 6
        self.force = force
        self.mass = 1.3
        self.color = (90, 90, 100)
        self.sound = "./sounds/shot_sounds/gunshot.wav"
        super().__init__(game, x, y, self.width, self.height, self.force, self.mass, angle, self.color, self.sound)
    def tick(self):
        super().tick()
    def draw(self):
        super().draw()

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

