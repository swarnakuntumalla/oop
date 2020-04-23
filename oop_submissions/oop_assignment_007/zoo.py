class Animal:
    sound = 'None'
    breathing = 'Breathe in air'
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
        
class WaterAnimal(Animal):
    breathing = 'Breathe oxygen from water'
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
   
class Hunt:
    kill = ' '
    @classmethod
    def hunt(cls, zoo):
        count = 0
        for instance_animal in zoo.animals_list:
            if type(instance_animal) == cls.kill:
                zoo.remove_animal(instance_animal)
                count = 1
        else:
            if cls.kill == GoldFish and count == 0:
                print('No GoldFish to hunt')
            elif count == 0:
                print('No deers to hunt')
     
class Deer(Animal):
    sound = 'Buck Buck'
    required_food = 2
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
    
        
class Lion(Animal, Hunt):
    kill = Deer
    sound = 'Roar Roar'
    required_food = 4
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class GoldFish(WaterAnimal):    
    sound = 'Hum Hum'
    required_food = 0.2
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Shark(WaterAnimal, Hunt):
    kill = GoldFish
    sound = 'Shark Sound'
    required_food = 8
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Snake(Animal, Hunt):
    kill = Deer
    sound = 'Hiss Hiss'
    required_food = 0.5
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        
class Zoo:
    obj_list =[]
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
        self.obj_list.append(animal)
        
    def remove_animal(self, animal):
        self.animals_list.remove(animal)
        self.obj_list.remove(animal)
        
    def count_animals(self):
        return len(self.animals_list)
        
    def feed(self, animal_name):
        if self._reserved_food_in_kgs >= animal_name.required_food_in_kgs:
            self._reserved_food_in_kgs -= animal_name.required_food_in_kgs
            animal_name.grow()
          
    @classmethod
    def count_animals_in_all_zoos(cls):
        count = 0
        for instance_animal in cls.obj_list:
           count += 1
        return count
        
    @staticmethod
    def count_animals_in_given_zoos(animal):
        count = 0
        for instance_animal in animal:
            for i in instance_animal.animals_list:
                count += 1
        return count
        
        
'''nehru_zoological_park = Zoo()
zoo = Zoo()

lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
zoo.add_animal(lion)
shark = Shark
shark = Shark(age_in_months=1, breed="ELK", required_food_in_kgs=10)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
#nehru_zoological_park.add_animal(deer)
zoo.add_animal(shark)
zoo.add_animal(deer)
print(zoo.count_animals())
print(Zoo.count_animals_in_given_zoos([zoo]))
#lion.hunt(nehru_zoological_park)'''