from mycode.ships import PlayableShip

class Player(object):
    def __init__(self, coins=1500):
        self.coins = coins
        self.ships: list[PlayableShip] = []
        self.__current_ship: PlayableShip | None = None
    
    def set_current_ship(self, ship: PlayableShip):
        if ship not in self.ships:
            raise Exception("No such ship in list")
        else:
            self.__current_ship = self.ships[self.ships.index(ship)]
    
    @property
    def current_ship(self):
        return self.__current_ship

    def add_coins(self, amount:int):
        self.coins += amount

    def subtract_coins(self, amount:int):
        self.coins -= amount

    def add_new_ship(self, ship):
        if any(isinstance(ship, type(sh)) for sh in self.ships):
            print("You cannot add the ship to the list, you have this model!")
        
        self.ships.append(ship)
        
        if len(self.ships) == 1:
            self.set_current_ship(ship)
