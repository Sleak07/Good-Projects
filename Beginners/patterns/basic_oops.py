# TODO: To revise the basic of oops


class Animal:
    def __init__(self, name, breed, color):
        self.name = name
        self._breed = breed
        self.color = color

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if "#" in new_breed:
            self._breed = new_breed

    def food(self):
        eat = f"{self.name}loves to eat food"
        return eat

    @staticmethod
    def animal_kingdom():
        return "All animals belong to the animal kingdom"


if __name__ == "__main__":
    dog = Animal("Bruno", "Pomerian", "Brown")
    print(dog.food())
    print(f"Breed: {dog.breed}")

dog.breed = "#German Sepherd"
print(f"New Breed: {dog.breed}")
print(Animal.animal_kingdom())
