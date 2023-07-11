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
        self.hitbox = pygame.Surface((self.width, self.height))
        self.hitbox.fill(color)
        self.mask = pygame.mask.from_surface(self.hitbox)

        self.color = color
        if sound is not None:
            self.sound = mixer.Sound(sound)
            self.sound.set_volume(0.1)

        self.maneuvering = False
        enemies_distances = []
        for enemy in self.game.enemies:
            vector = Vector2(enemy.pos.x - self.pos.x, enemy.pos.y - self.pos.y)
            distance = vector.magnitude()
            enemies_distances.append(distance)

        enemy_index = enemies_distances.index(min(enemies_distances))
        self.enemy = self.game.enemies[enemy_index]

    def tick(self):
        if self.maneuvering:
            pass
        else:
            self.vel *= 0.9995
            self.vel += self.acc
            self.pos += self.vel * self.game.dt
            self.acc *= 0

    def draw(self):
        self.game.screen.blit(self.hitbox, (self.pos.x - self.width/2, self.pos.y - self.height/2))
