class Pokemon:
    speak = ' '
    electric_magnitude_of_the_attack = 0
    water_magnitude_of_the_attack = 0
    air_magnitude_of_the_attack = 0
    water_attacking, electric_attacking, air_attacking = 0, 0, 0
    def __init__(self, name = '', level = 1):
        if name == '':
            raise ValueError('name cannot be empty')
        elif level <= 0:
            raise ValueError('level should be > 0')
        self._name = name
        self._level = level
        
    def __str__(self):
        return f'{self._name} - Level {self._level}'
        
    def __mul__(self,other):
        return self*other
      
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    
    @classmethod
    def make_sound(cls):
        print(cls.speak)
        

    def attack(self):
        if self.water_magnitude_of_the_attack > 0:
            self.water_attacking = self._level * self.water_magnitude_of_the_attack
        if self.air_magnitude_of_the_attack > 0:
            self.air_attacking = self._level * self.air_magnitude_of_the_attack
        if self.electric_magnitude_of_the_attack > 0:
            self.electric_attacking = self._level * self.electric_magnitude_of_the_attack
        self._level += 1

class FlyingPokemon(Pokemon):
    flying = ' '
    @classmethod
    def fly(cls):
        print(cls.flying)
    
    def attack(self):
        super().attack()
        print(f'Air attack with {self.air_attacking} damage')
        
class Electricpokemon(Pokemon):
    running = ' '
    @classmethod
    def run(cls):
        print(cls.running)
      
    def attack(self):
        super().attack()
        print(f'Electric attack with {self.electric_attacking} damage')

class WaterPokemon(Pokemon):
    swimming = ''
    running = ' '
    @classmethod
    def run(cls):
        print(cls.running)
    @classmethod
    def swim(cls):
        print(cls.swimming)
        
    def attack(self):
        super().attack()
        print(f'Water attack with {self.water_attacking} damage')
 
class Pikachu(Electricpokemon):
    speak = 'Pika Pika'
    running = 'Pikachu running...'
    electric_magnitude_of_the_attack = 10
    electric_attacking = 10
    
class Squirtle(WaterPokemon):
    speak = 'Squirtle...Squirtle'
    running = 'Squirtle running...'
    swimming = 'Squirtle swimming...'
    water_magnitude_of_the_attack = 9
    water_attacking = 9
    
class Pidgey(FlyingPokemon):
    speak = 'Pidgey...Pidgey'
    flying = 'Pidgey flying...'
    air_magnitude_of_the_attack = 5
    air_attacking = 5
    
class Swanna(WaterPokemon, FlyingPokemon):
    speak = 'Swanna...Swanna'
    flying = 'Swanna flying...'
    swimming = 'Swanna swimming...'
    water_magnitude_of_the_attack = 9
    water_attacking = 9
    air_magnitude_of_the_attack = 5
    air_attacking = 5
    
class Zapdos(Electricpokemon, FlyingPokemon):
    speak = 'Zap...Zap'
    flying = 'Zapdos flying...'
    air_magnitude_of_the_attack = 5
    air_attacking = 5
    electric_magnitude_of_the_attack = 10
    electric_attacking = 10
    
p= Zapdos('swa',1)
p.attack()
p.attack()