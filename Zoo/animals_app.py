# Class imports
from Zoo.animals import Animal
from Zoo.birds import Bird
from Zoo.zoo import Zoo

# Instantiating Animal and Bird Classes
# Bird class has been derived from Animal Class
lion = Animal("Leo", "Lion", "Roar", "has mane")
elephant = Animal("Appu", "Elephant", "Pa-woo", "has trunk")
giraffe = Animal("Gerald", "Giraffe","shh", "long neck")
penguin = Bird("Captain", "Penguin","Honk", False)
parrot = Bird("Mitthu", "Parrot","Whistle", True)

# Instantiating Zoo class
zoo = Zoo()

# calling method of Zoo class to add animal
zoo.add_animal(lion)
# calling method of Animal class on animal instance
lion.make_sound()
# printing object
print(lion)

zoo.add_animal(elephant)
elephant.make_sound()

zoo.add_animal(giraffe)
giraffe.make_sound()
# method of Zoo class to list animals
zoo.list_animals()

zoo.add_animal(penguin)
# calling method of Animal (Base) class on Bird (derived class) instance
penguin.make_sound()
# calling method of Bird class on bird instance
penguin.fly()
# printing object
print(penguin)


zoo.add_animal(parrot)
# calling method of Animal (Base) class on Bird (derived class) instance
parrot.make_sound()
# calling method of Bird class on bird instance
parrot.fly()

zoo.list_animals()

zoo.transfer_animal(elephant)
zoo.list_animals()

# Method of Zoo class to remove animal from Zoo
zoo.transfer_animal(penguin)

# instantiating Bird class
penguin2 = Bird("Nimrod", "Penguin","Honk",False)
zoo.add_animal(penguin2)
# Listing animals on the modified list
zoo.list_animals()
