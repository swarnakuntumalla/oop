class Pokemon:
    master = 'No Master'
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
        if self.electric_magnitude_of_the_attack > 0:
            self.electric_attacking = self._level * self.electric_magnitude_of_the_attack
        if self.air_magnitude_of_the_attack > 0:
            self.air_attacking = self._level * self.air_magnitude_of_the_attack
        self._level += 1
        
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

class FlyingPokemon(Pokemon):
    flying = ' '
    @classmethod
    def fly(cls):
        print(cls.flying)
    
    def attack(self):
        super().attack()
        print(f'Air attack with {self.air_attacking} damage')
 
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
    
class Swanna(FlyingPokemon, WaterPokemon):
    speak = 'Swanna...Swanna'
    flying = 'Swanna flying...'
    swimming = 'Swanna swimming...'
    water_magnitude_of_the_attack = 9
    water_attacking = 9
    air_magnitude_of_the_attack = 5
    air_attacking = 5
    
class Zapdos(FlyingPokemon, Electricpokemon):
    speak = 'Zap...Zap'
    flying = 'Zapdos flying...'
    electric_magnitude_of_the_attack = 10
    electric_attacking = 10
    air_magnitude_of_the_attack = 5
    air_attacking = 5

class Island:
    islands_list = []
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list = []
    
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def add_pokemon(self, pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self.pokemon_list.append(pokemon)
            self._pokemon_left_to_catch += 1
            answer = f'{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
            self.islands_list.append(answer)
            
        else:
            print('Island at its max pokemon capacity')
    
    def __str__(self):
        return f'{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
    
    @classmethod
    def get_all_islands(cls):
        print(cls.islands_list)
            
class Trainer:
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._food_in_bag = 0
        self.current_island = 'You are not on any island'
        self._max_food_in_bag = self._experience * 10
        self.caught_list = []
    
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def food_in_bag(self):
        return self._food_in_bag
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    def __str__(self):
        return self._name
    
    def move_to_island(self, island):
        self.current_island = island
        
    def collect_food(self):
        if self.current_island == 'You are not on any island':
            print('Move to an island to collect food')
        else:
            if self._food_in_bag + self._max_food_in_bag <= self.max_food_in_bag:
                self._food_in_bag += self._max_food_in_bag
        
    def catch(self, pokemon):
        if self._experience >= 100 * pokemon.level:
            print(f'You caught {pokemon.name}')
            self._experience += pokemon.level * 20
            self.caught_list.append(pokemon)
            pokemon.master = self
        else:
            print(f'You need more experience to catch {pokemon.name}')
            
    def get_my_pokemon(self):
        li =[]
        for i in self.caught_list:
            li.append(i)
            
        print(li)
        
t = Trainer('bot')
i1 = Island('Island1', 5, 10000)
p = Pikachu('swarna',1)
k = Pidgey('yduff', 1)
i2 = Island('Island2',10,2423)
i1.add_pokemon(p)
i1.add_pokemon(k)
i2.add_pokemon(p)
i2.add_pokemon(k)
#Island.get_all_islands()
t.move_to_island(i1)
# #print(t.food_in_bag)
t.collect_food()
# #print(t.food_in_bag)
print(i1.total_food_available_in_kgs)
# print(p.master)
# t.catch(p)
# print(p.master == t)
t.catch(p)
print(t.food_in_bag)