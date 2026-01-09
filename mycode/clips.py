from abc import abstractmethod, ABC


class BaseClip(ABC):
    @abstractmethod
    def maximise_ammo(self):
        pass
    
    @abstractmethod
    def can_i_shoot(self):
        pass
    
    @abstractmethod
    def tick(self, dt: float):
        pass


class Clip(BaseClip):
    def __init__(self, max_ammo: int, reload_time: float, active_reload: bool = False):
        self.max_ammo = max_ammo
        self.current_ammo = max_ammo
        self.reload_time = reload_time
        self.active = active_reload
        self.reloading = False
        
        self.clock = 0
    
    def maximise_ammo(self):
        self.current_ammo = self.max_ammo
    
    def shot(self):
        self.current_ammo -= 1
    
    def can_i_shoot(self):
        if self.current_ammo > 0:
            return True
        # If ammo is equal or below 0, then undeniably returns False
        return False
    
    def tick(self, dt: float):
        # there is no ammo, passive reloading
        if not self.active:
            # it is not reloading
            if not self.reloading:
                if self.current_ammo <= 0:
                    self.reloading = True
            # it is reloading
            if self.reloading:
                self.clock += dt
                if self.clock > self.reload_time:
                    self.clock = 0
                    self.reloading = False
                    self.maximise_ammo()
        # active reloading
        else:
            self.clock += dt
            if self.clock > self.reload_time and self.current_ammo < self.max_ammo:
                self.current_ammo += 100
                self.clock = 0


class LaserClip(BaseClip):
    def __init__(self, shooting_time, reload_time):
        self.clock = 0
        self.shooting_time = shooting_time
        self.reload_time = reload_time
        self._active = True
    
    def can_i_shoot(self):
        return self._active
    
    def maximise_ammo(self):
        self.clock = 0
        self._active = True
    
    def tick(self, dt: float):
        self.clock += dt
        if self._active:
            if self.clock > self.shooting_time:
                self.clock = 0
                self._active = False
        else:
            if self.clock > self.reload_time:
                self.clock = 0
                self._active = True
