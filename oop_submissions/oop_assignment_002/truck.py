from car import Car
class Truck(Car):
    horn = 'Honk Honk'
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self._cargo = 0
    
    @property
    def cargo(self):
        return self._cargo
        
    def load(self,cargo_weight):
        if self.current_speed > 0:
            print('Cannot load cargo during motion')
        else:
            if cargo_weight < 0:
                raise ValueError('Invalid value for cargo_weight')
            elif cargo_weight+self._cargo > self.max_cargo_weight:
                print(f'Cannot load cargo more than max limit: {self.max_cargo_weight}')
            else:
                self._cargo +=cargo_weight
                
    def unload(self,cargo_weight):
        if self.current_speed > 0:
            print('Cannot unload cargo during motion')
        else:
            if cargo_weight < 0:
                raise ValueError('Invalid value for cargo_weight')
            else:
                self._cargo -=cargo_weight