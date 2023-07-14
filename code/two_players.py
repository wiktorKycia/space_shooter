import pygame
from code.ships import PlayableShip
from code.other import DeluxeHP
from code.cannons import *


class Player1(PlayableShip):
    def __init__(self, game):
        self.hp = DeluxeHP(self.game, 1000000, 120, 700, 200, 20)
        super().__init__(game, "./images/SpaceShips2/spaceship_small_blue.png", 0.98, 200, 100, 2000)
        self.cannon = KineticGun(game, self, Vector2(0, 20), self.force, 0.5, pygame.K_LSHIFT)

    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()

    def draw(self):
        super().draw()

class Player2(PlayableShip):
    def __init__(self, game):
        self.hp = DeluxeHP(self.game, 1000000, 120, 30, 200, 20)
        super().__init__(game, "./images/SpaceShips2/spaceship_small_red.png", 0.98, 200, 100, 2000)
        self.cannon = KineticGun(game, self, Vector2(0, 20), self.force, 0.5, pygame.K_RSHIFT)

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.add_force(Vector2(0, -self.force))
        if pressed[pygame.K_DOWN]:
            self.add_force(Vector2(0, self.force))
        if pressed[pygame.K_RIGHT]:
            self.add_force(Vector2(self.force, 0))
        if pressed[pygame.K_LEFT]:
            self.add_force(Vector2(-self.force, 0))

        # Physics
        self.vel *= self.slip
        self.vel -= Vector2(0, 0)

        self.vel += self.acc

        # Limiting speed
        if self.vel.x > self.max_speed:  # right
            self.vel = Vector2(self.max_speed, self.vel.y)
        elif self.vel.x < -self.max_speed:  # left
            self.vel = Vector2(-self.max_speed, self.vel.y)
        if self.vel.y > self.max_speed:  # up
            self.vel = Vector2(self.vel.x, self.max_speed)
        elif self.vel.y < -self.max_speed:  # down
            self.vel = Vector2(self.vel.x, -self.max_speed)

        self.pos += self.vel * self.game.dt
        self.acc *= 0

        self.hitbox.center = (self.pos.x, self.pos.y)

        self.clock += self.game.dt

        for bullet in self.bullets:
            if bullet.pos.y <= -bullet.height:
                self.bullets.remove(bullet)
            else:
                bullet.tick()

class TwoPlayersGame:
    def __init__(self, game):
        pass