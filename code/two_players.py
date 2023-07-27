import pygame
from code import ShootingDown
import code.UI
from code.ships import PlayableShip
from code.other import DeluxeHP
from code.cannons import *


class Player1(PlayableShip):
    def __init__(self, game):
        self.hp = DeluxeHP(game, 1000000, 120, 700, 200, 20)
        super().__init__(game, "./images/SpaceShips2/spaceship_small_blue.png", 0.98, 200, 100, 1000)
        self.cannon = KineticGun(game, self, Vector2(0, 20), self.force, 0.5, pygame.K_LSHIFT)

    def tick(self):
        self.hp.tick()
        super().tick()
        self.cannon.tick()

    def draw(self):
        super().draw()

class Player2(ShootingDown):
    def __init__(self, game):
        super().__init__(game, 350, 150, "./images/SpaceShips2/spaceship_small_red_reversed.png",
                         150, 200, 2000, 2000000, 200, 20, 10, 10)
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
        self.cannon.tick()

class TwoPlayersGame:
    def __init__(self, game):
        self.game = game
        self.player1 = Player1(self.game)
        self.player2 = Player2(self.game)

        self.click_P_counter = 0

        self.pausemenu = code.UI.PauseMenu(game, "twoplayers", "gamemenu")

    def tick(self):
        self.player1.tick()
        self.player2.tick()

        for bullet in self.player1.bullets:
            bullet.tick()
            bullet.draw()
            if self.player2.mask.overlap(bullet.mask, (
            bullet.pos.x - self.player2.hitbox.x, bullet.pos.y - self.player2.hitbox.y)):
                energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                self.player2.hp.get_damage(energy)
                continue

        for bullet in self.player2.bullets:
            bullet.tick()
            bullet.draw()
            if self.player1.mask.overlap(bullet.mask, (
            bullet.pos.x - self.player1.hitbox.x, bullet.pos.y - self.player1.hitbox.y)):
                energy = int((bullet.mass * bullet.vel * bullet.vel) / 2)
                self.player1.hp.get_damage(energy)
                continue

        if pygame.key.get_pressed()[pygame.K_p] == 1 and self.click_P_counter == 0:
            self.click_P_counter += 1
            self.game.showing = "twoplayers_pausemenu"
        elif pygame.key.get_pressed()[pygame.K_p] == 0:
            self.click_P_counter = 0
        else:
            self.click_P_counter += 1

    def draw(self):
        self.player1.draw()
        self.player2.draw()
        self.player1.hp.tick()
        self.player2.hp.tick()
