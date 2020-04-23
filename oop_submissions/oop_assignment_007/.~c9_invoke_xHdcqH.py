class Animal:
    sound = 'None'
    breathing = 'None'
    required_food = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        elif required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
            
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.breathing)

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs += self.required_food
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
   
class Hunt:
    def hunt(self, zoo):
        for killing_animal in zoo:
            if type(zoo.kill) == killing_animal:
                zoo.remove_animal(killing_animal)
     
class Deer(Animal):
    sound = 'Buck Buck'
    breathing = 'Breathe in air'
    required_food = 2
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
    
        
class Lion(Animal,Hunt):
    kill = Deer
    sound = 'Roar Roar'
    breathing = 'Breathe in air'
    required_food = 4
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class GoldFish(Animal):    
    sound = 'Hum Hum'
    breathing = 'Breathe oxygen from water'
    required_food = 0.2
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Shark(Animal,Hunt):
    kill = GoldFish
    sound = 'Shark Sound'
    breathing = 'Breathe oxygen from water'
    required_food = 8
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Snake(Animal,Hunt):
    kill = Deer
    sound = 'Hiss Hiss'
    breathing = 'Breathe in air'
    required_food = 0.5
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Zoo:
    obj_list = []
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animals_list = []
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self, food_quantity):
        self._reserved_food_in_kgs += food_quantity
    
    def add_animal(self, animal):
        self.animals_list.append(animal)
        
    def remove_animal(self, animal):
        self.animals_list.remove(animal)
        
    def count_animals(self):
        return len(self.animals_list)
        
    def feed(self, animal_name):
        if self._reserved_food_in_kgs >= animal_name.required_food_in_kgs:
            self._reserved_food_in_kgs -= animal_name.required_food_in_kgs
            animal_name.grow()
          
    @classmethod
    def count_animals_in_all_zoos(cls):
        
    @staticmethod
    def count_animals_in_given_zoos()
        
nehru_zoological_park = Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
print(nehru_zoological_park)
print(nehru_zoological_park.count_animals())
#lion.hunt(nehru_zoological_park)