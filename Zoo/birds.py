# Import base class
from animals import Animal
# Class definition for Bird class that inherits from Animal class
class Bird(Animal):
    # class constructor
    def __init__(self, name, species, sound, can_fly):
        # calling base class constructor
        super().__init__(name, species, sound, special=can_fly)
        # setting value of can_fly attribute of Bird class
        self.can_fly = can_fly

    # class method checks class attribute can_fly and behaves based on its value
    def fly(self):
        if self.can_fly:
            print(f"\n~~~~~{self.name} is flying.~~~~~")
        else:
            print(f"\n~~~~~{self.name} cannot fly.~~~~~")

    # The __str__() method returns a reader-friendly string representation of class object when we print() it
    def __str__(self):
        return (f"\n{'*' * 20}\nBird\nName: {self.name}\nSpecies: "
                f"{self.species}\nSound: {self.sound}\n{'*' * 20}")