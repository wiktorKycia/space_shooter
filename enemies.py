from bullets import *
class BaseEnemy(object):
    def __init__(self, game, x, y, isshooting, movforce, mass, shotforce, imagepath):
        self.game = game
        self.x = x
        self.y = y
        self.isshooting = isshooting
        self.movforce = movforce
        self.mass = mass
        self.shotforce = shotforce

        self.acc = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(x, y)

        self.image = imagepath
    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        self.draw()

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x, self.pos.y))

class Enemy1(BaseEnemy):
    def __init__(self, game, path, x, y):
        self.game = game
        self.image = path
        super().__init__(self.game, x, y , True, 1000, 500, 2200, self.image)
