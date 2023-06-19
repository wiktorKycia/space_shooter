import pygame

class HP:
    def __init__(self, game, amount, width, height, x, y, color=(250, 250, 250)):
        self.game = game
        self.amount = amount

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
        self.bgcolor = (color[0] - 100, color[1] - 100, color[2] - 100)

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(self.bgcolor)

        self.unit = self.width / self.amount

        self.block = pygame.Rect(0, 0, self.unit * self.amount, self.height)

    def tick(self):
        self.block = pygame.Rect(0, 0, self.unit * self.amount, self.height)

    def draw(self):
        self.game.screen.blit(self.surf, (self.x - self.width/2, self.y - self.height/2))
        pygame.draw.rect(self.surf, self.color, self.block)
