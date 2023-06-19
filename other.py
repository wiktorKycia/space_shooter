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
        self.bgcolor = (255, 0, 0)#(color[0] - 100, color[1] - 100, color[2] - 100)

        self.back = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)

        self.unit = self.width / self.amount

        self.block = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.unit * self.amount, self.height)

    def decrease_by(self, amount):
        self.amount -= amount
        self.tick()
        self.draw()

    def tick(self):
        self.block = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.unit * self.amount, self.height)

    def draw(self):
        # self.game.screen.blit(self.surf, (self.x - self.width/2, self.y - self.height/2))
        print(self.block.width, self.amount, self.unit)
        pygame.draw.rect(self.game.screen, self.bgcolor, self.back)
        pygame.draw.rect(self.game.screen, self.color, self.block)
