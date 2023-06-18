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
                    enemy1 = Enemy1(self.game, x - 50, y)
                    enemy2 = Enemy1(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght-2)/2)):
                        enemy1 = Enemy1(self.game, x - 50 - (i+1) * 100, y)
                        enemy2 = Enemy1(self.game, x + 50 + (i+1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy1(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght-1)/2)):
                        enemy2 = Enemy1(self.game, x - (i+1) * 100, y)
                        enemy3 = Enemy1(self.game, x + (i+1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case 2:
                if lenght % 2 == 0:
                    enemy1 = Enemy2(self.game, x - 50, y)
                    enemy2 = Enemy2(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght - 2) / 2)):
                        enemy1 = Enemy2(self.game, x - 50 - (i + 1) * 100, y)
                        enemy2 = Enemy2(self.game, x + 50 + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy2(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght - 1) / 2)):
                        enemy2 = Enemy2(self.game, x - (i + 1) * 100, y)
                        enemy3 = Enemy2(self.game, x + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case 3:
                if lenght % 2 == 0:
                    enemy1 = Enemy3(self.game, x - 50, y)
                    enemy2 = Enemy3(self.game, x + 50, y)
                    self.game.enemies.extend([enemy1, enemy2])

                    for i in range(0, int((lenght - 2) / 2)):
                        enemy1 = Enemy3(self.game, x - 50 - (i + 1) * 100, y)
                        enemy2 = Enemy3(self.game, x + 50 + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy1, enemy2])
                else:
                    enemy1 = Enemy3(self.game, x, y)
                    self.game.enemies.append(enemy1)

                    for i in range(0, int((lenght - 1) / 2)):
                        enemy2 = Enemy3(self.game, x - (i + 1) * 100, y)
                        enemy3 = Enemy3(self.game, x + (i + 1) * 100, y)
                        self.game.enemies.extend([enemy2, enemy3])
            case _:
                pass

    def triangle1(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 50, y - 50)
        enemy2 = Enemy1(self.game, x + 50, y - 50)
        enemy3 = Enemy1(self.game, x, y + 50)
        self.game.enemies.extend([enemy1, enemy2, enemy3])

    def triangle2(self, x:int, y:int):
        enemy1 = Enemy1(self.game, x - 50, y - 50)
        enemy2 = Enemy1(self.game, x + 50, y - 50)
        enemy3 = Enemy2(self.game, x, y + 50)
        self.game.enemies.extend([enemy1, enemy2, enemy3])