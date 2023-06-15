from bullets import *
class BaseEnemy(object):
    def __init__(self, x, y, isshooting, movforce, mass, shotforce):
        self.x = x
        self.y = y
        self.isshooting = isshooting
        self.movforce = movforce
        self.mass = mass
        self.shotforce = shotforce