from enemies import *
# klasa minilevel
# jako argument przyjmuje listę wszystkich przeciwników
# poszczególnymi metodami generuje zestawy przeciwników, lub pojedyńczo
#
# klasa level
# zawiera wywołania poszczególnych metod z minilevel'a
#
# lista przeciwników w mainie
class Minilevel():
    def __init__(self, game):
        self.game = game

    def add_single(self, enemy):
        self.game.enemies.append(enemy)

    def pair(self, x, y):
        enemy1 = Enemy1(self.game, x-50, y)
        enemy2 = Enemy1(self.game, x+50, y)
        self.game.enemies.extend([enemy1, enemy2])