import pygame
from code import ShootingDown
import code.UI
from code.ships import PlayableShip
from code.other import DeluxeHP
from code.cannons import *


class Player1(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game=game,
            path="./images/SpaceShips2/spaceship_small_blue.png",
            mass=150,
            max_speed=200,
            force=2000,
            hp_amount=2000000,
            hp_width=200, hp_height=20,
            hp_x=110, hp_y=730
        )
        self.cannon = KineticGun(game, self, Vector2(0, 20), self.force, 0.5, pygame.K_LSHIFT)
        self.pos = Vector2(350, 600)

    def tick(self):
        super().tick()
        self.cannon.tick()

    def draw(self):
        super().draw()

class Player2(ShootingDown):
    def __init__(self, game):
        super().__init__(game=game,
                         x=350,
                         y=150,
                         path="./images/SpaceShips2/spaceship_small_red_reversed.png",
                         mass=150,
                         max_speed=200,
                         force=2000,
                         hp_amount=2000000,
                         hp_width=200, hp_height=20,
                         hp_x=110, hp_y=20)
        self.cannon = KineticGun(game, self, Vector2(0, 20), self.force, 0.5, pygame.K_RSHIFT)

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.add_force(Vector2(0, self.force))
        if pressed[pygame.K_DOWN]:
            self.add_force(Vector2(0, -self.force))
        if pressed[pygame.K_RIGHT]:
            self.add_force(Vector2(-self.force, 0))
        if pressed[pygame.K_LEFT]:
            self.add_force(Vector2(self.force, 0))

        super().tick()
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
