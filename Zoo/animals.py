# Class definition for Animal class
class Animal:
    # class constructor
    def __init__(self, name, species, sound, special):
        # attributes
        self.name = name
        self.species = species
        self.sound = sound
        self.speciality = special

    # class method
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    # The __str__() method returns a reader-friendly string representation of class object when we print() it
    def __str__(self):
        return f"\n{'*' * 20}\nAnimal\nName: {self.name}\nSpecies: {self.species}\nSound: {self.sound}\n{'*' * 20}"
