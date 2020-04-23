import math
from car import Car
class RaceCar(Car):
    horn="Peep Peep\nBeep Beep"
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro = 0
    
    @property
    def nitro(self):
        return self._nitro
    
    def apply_brakes(self):
        if self._current_speed >= self.max_speed//2:
                self._nitro += 10
        super().apply_brakes()
        
    def accelerate(self):
        if self.nitro != 0:
            self._current_speed += math.ceil(self._acceleration*0.3)
            self._nitro -= 10
        super().accelerate()