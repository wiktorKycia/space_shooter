from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mycode.ships import PlayableShip
    from mycode.weapons import Weapon

class Player:
    def __init__(self, coins:int = 1500):
        self.coins: int = coins

        self.ships: list[PlayableShip] = []
        self.__current_ship: PlayableShip | None = None

        self.weapons: list[Weapon] = []

    def add_coins(self, amount:int):
        self.coins += amount

    def subtract_coins(self, amount:int):
        self.coins -= amount

    @property
    def current_ship(self):
        return self.__current_ship

    def add_new_ship(self, ship: PlayableShip):
        self.ships.append(ship)

        if len(self.ships) == 1:
            self.set_current_ship(ship)

    def set_current_ship(self, ship: PlayableShip):
        if ship not in self.ships:
            raise Exception("No such ship in list")
        else:
            self.__current_ship = self.ships[self.ships.index(ship)]
