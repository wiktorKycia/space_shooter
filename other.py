import pygame

class HP:
    def __init__(self, game, amount, width, height, x, y, color=(250, 250, 250)):
        self.game = game
        self.full = amount
        self.amount = amount

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
        self.bgcolor = (color[0] - 50, color[1] - 50, color[2] - 50)

    def draw(self):

