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

    def pair(self, x:int, y:int, type:int=1):
        match type:
            case 1:
                enemy1 = Enemy1(self.game, x-50, y)
                enemy2 = Enemy1(self.game, x+50, y)
            case 2:
                enemy1 = Enemy2(self.game, x - 50, y)
                enemy2 = Enemy2(self.game, x + 50, y)
            case 3:
                enemy1 = Enemy3(self.game, x - 50, y)
                enemy2 = Enemy3(self.game, x + 50, y)
            case _:
                enemy1 = Enemy1(self.game, x - 50, y)
                enemy2 = Enemy1(self.game, x + 50, y)
        self.game.enemies.extend([enemy1, enemy2])

    def line(self, x:int, y:int, lenght:int, type:int=1):
        match type:
            case 1:
                if lenght % 2 == 0:
                    for i in range(0, lenght):
                        enemy1 = Enemy1(self.game, x - i*50, y)
                        enemy2 = Enemy1(self.game, x + i*50, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    pass
            case 2:
                pass
            case 3:
                pass
            case _:
                pass