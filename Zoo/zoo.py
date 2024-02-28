# Definition for class Zoo
class Zoo:
    # class constructor
    def __init__(self):
        # attribute to store list of animals
        self.animals = []

    # class methods

    # Adds animal to the Zoo
    def add_animal(self, animal):
        print(f"\nWelcome new member of the zoo: {animal.name} ({animal.species})")
        self.animals.append(animal)

    # Method removes transferred animal from zoo list
    def transfer_animal(self, animal):
        print(f"\n{animal.species} ({animal.name}) has been transferred to another facility!")
        index = self.animals.index(animal)
        self.animals.pop(index)

    # method lists all animals currently in the Zoo
    def list_animals(self):
        print(f"\n{'*' * 20}\nAnimals presently at the zoo:")
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal.name} - {animal.species}")
        print('*' * 20)
