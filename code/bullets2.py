import pygame
from pygame import mixer
from pygame.math import *
mixer.init()

class ManeuveringBullet:
    def __init__(self, game, x, y, width, height, force, mass, color=(255, 255, 255), sound=None):
        self.game = game

        self.x = x
        self.y = y
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.force = force
        self.mass = mass
        acc = int(force / mass)
        self.acc = Vector2(0, -acc)

        self.width = width
        self.height = height
        self.image = pygame.image.load("./images/bullet.png").convert_alpha()
        self.hitbox = pygame.Surface((self.width, self.height))
        self.hitbox.fill(color)
        self.mask = pygame.mask.from_surface(self.image)

        self.color = color
        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)

        self.maneuvering = False
        if len(self.game.enemies) != 0:
            enemies_distances = []
            for enemy in self.game.enemies:
                vector = Vector2(enemy.pos.x - self.pos.x, enemy.pos.y - self.pos.y)
                distance = vector.magnitude()
                enemies_distances.append(distance)

            enemy_index = enemies_distances.index(min(enemies_distances))
            self.enemy = self.game.enemies[enemy_index]
            self.maneuvering = True

    def tick(self):
        self.vel *= 0.9995
        self.vel += self.acc
        self.pos += self.vel * self.game.dt
        self.acc *= 0
        if self.maneuvering:
            if self.enemy in self.game.enemies:
                vector = Vector2(self.enemy.pos.x - self.pos.x, self.enemy.pos.y - self.pos.y)
                angle = self.vel.angle_to(vector)
                if angle > 180:
                    angle = -angle
                if angle < -180:
                    angle = -angle
                self.vel.rotate_ip(angle/10)

            else: self.maneuvering = False

    def draw(self):
        image2 = pygame.transform.rotate(self.image, self.vel.angle_to(Vector2(0, -1)))
        self.game.screen.blit(image2, (self.pos.x - self.width / 2, self.pos.y - self.height / 2))