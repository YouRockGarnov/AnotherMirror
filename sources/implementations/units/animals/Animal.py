from implementations.units.animals.AnimalsBreed import AnimalsBreed


class Animal:
    def __init__(self, breed: AnimalsBreed):
        self._breed = breed
        self._health = breed.health
        self._defense = breed.defense

    @property
    def health(self):
        return self._health

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._breed.attack
