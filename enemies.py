import pygame.time
from bullets import *
import os
class BaseEnemy(object):
    def __init__(self, game, imagepath, x, y, slip, mov_force, mass, shot_force, barrel_lenght):
        self.game = game
        self.x = x
        self.y = y

        self.image = imagepath
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

    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        self.clock += self.game.dt

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x - self.width/2, self.pos.y - self.height/2))

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
        self.image = pygame.image.load(os.path.join("./enemies/Enemy1.png"))
        super().__init__(self.game, self.image, x, y , 0.99, 1000, 500, 2200, 50)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 1.0:
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
        self.image = pygame.image.load(os.path.join("./enemies/Enemy2.png"))
        super().__init__(self.game, self.image, x, y , 0.99, 1500, 1000, 2500, 50)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 0.75:
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
        self.image = pygame.image.load(os.path.join("./enemies/Enemy3.png"))
        super().__init__(self.game, self.image, x, y , 0.98, 5400, 3500, 6000, 60)

    def add_force(self, force):
        super().add_force(force)

    def tick(self):
        super().tick()
        if self.clock >= 0.5:
            self.clock = 0
            bullet = BlasterBullet(self.game, self.pos.x-20, self.pos.y, -self.shotforce)
            bullet1 = BlasterBullet(self.game, self.pos.x+20, self.pos.y, -self.shotforce)
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