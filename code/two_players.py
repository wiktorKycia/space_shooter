import pygame
from code.ships import PlayableShip


class Player1(PlayableShip):
    def __init__(self, game):
        super().__init__(game, "./images/SpaceShips2/spaceship_small_blue.png", 0.98, 200, 100, 2000)

    def tick(self):
        super().tick()

    def draw(self):
        super().draw()

class Player2(PlayableShip):
    def __init__(self, game):
        super().__init__(game, "./images/SpaceShips2/spaceship_small_red.png", 0.98, 200, 100, 2000)

class TwoPlayersGame:
    def __init__(self, game):
        pass