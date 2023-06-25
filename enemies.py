import pygame.time
from ships import *
from bullets import *
import os
class BaseEnemy(object):
    def __init__(self, game, imagepath, x, y, slip, mov_force, mass, shot_force, barrel_lenght, health):
        self.game = game
        self.x = x
        self.y = y

        self.image = pygame.image.load(os.path.join(imagepath)).convert_alpha()
        self.hitbox = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.slip = slip
        self.movforce = mov_force
        self.mass = mass
        self.shotforce = shot_force
        self.barrel = barrel_lenght

        self.acc = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(x, y)

        self.clock = 0
        self.bullets = []

        self.health = health

    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        self.clock += self.game.dt
        self.hitbox.center = (self.pos.x, self.pos.y)

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x - self.width/2, self.pos.y - self.height/2))
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.hitbox, 1)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)
        bullet.sound.play(0, 800)
        acc = -bullet.acc  # getting initial bullet velocity
        vel = (bullet.mass * acc) / self.mass
        # getting initial velocity from zasada zachowania pędu
        vel.x *= vel.x
        vel.y *= vel.y
        energy = (self.mass * vel) / 2  # calculating kinetic energy
        force = energy / self.barrel  # calculating kickback force
        self.add_force(Vector2(force.x, force.y))


class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.image = "./enemies/Enemy1.png"
        super().__init__(self.game, self.image, x, y , 0.99, 100, 50, 800, 5, 1000000)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 2.0:
            self.clock = 0
            bullet = KineticBullet(self.game, self.pos.x, self.pos.y, -self.shotforce)
            self.add_bullet(bullet)

        for bullet in self.bullets:
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)
            else:
                bullet.tick()

    def draw(self):
        super().draw()
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)

    def add_bullet(self, bullet):
        super().add_bullet(bullet)


class Enemy2(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.image = "./enemies/Enemy2.png"
        super().__init__(self.game, self.image, x, y , 0.99, 150, 100, 1200, 5, 10)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 1.5:
            self.clock = 0
            bullet = Kinetic9Bullet(self.game, self.pos.x, self.pos.y, -self.shotforce)
            self.add_bullet(bullet)

        for bullet in self.bullets:
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)
            else:
                bullet.tick()

    def draw(self):
        super().draw()
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)

    def add_bullet(self, bullet):
        super().add_bullet(bullet)


class Enemy3(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        self.image = "./enemies/Enemy3.png"
        super().__init__(self.game, self.image, x, y , 0.98, 540, 350, 2500, 6, 10)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 1.0:
            self.clock = 0
            bullet = EnergyGunBullet(self.game, self.pos.x-22, self.pos.y, -self.shotforce)
            bullet1 = EnergyGunBullet(self.game, self.pos.x+22, self.pos.y, -self.shotforce)
            self.add_bullet(bullet)
            self.add_bullet(bullet1)

        for bullet in self.bullets:
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)
            else:
                bullet.tick()

    def draw(self):
        super().draw()
        for bullet in self.bullets:
            bullet.draw()
            if bullet.pos.y >= self.game.height:
                self.bullets.remove(bullet)

    def add_bullet(self, bullet):
        super().add_bullet(bullet)