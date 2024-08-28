from pygame.math import Vector2
class Slot:
    def __init__(self, game, ship, translation: Vector2, key: int, weaponType):
        """
        Represents a weapon slot of a Ship,
        it can contain only one weapon
        :param game: Game
        :param ship: any type inheriting from PlayableShip or BaseEnemy
        :param translation: pygame.Vector2
        :param key: int
        :param weaponType: any end child class inheriting from Weapon
        """
        self.game = game
        self.ship = ship
        self.translation = translation
        self.key = key
        self.pos = self.ship.pos + self.translation
        self.weapon = weaponType(game, self, key)

    def tick(self):
        self.pos = self.ship.pos + self.translation
        self.weapon.tick()

    def draw(self):
        self.weapon.draw()
