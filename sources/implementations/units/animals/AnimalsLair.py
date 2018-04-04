from implementations.units.animals.AnimalsBreed import AnimalsBreed
from implementations.units.animals.Animal import Animal
from enum import Enum


class AnimalsLair:  # factory
    class STRENGTH(Enum):
        BABY_STRENGTH = 0.8
        ADULT_STRENGTH = 1
        LEADER_STRENGTH = 1.2

    def __init__(self, breed: AnimalsBreed):
        self._breed = breed

    def create_animal(self, strength: STRENGTH):
        self._breed._set_strength(strength.value)
        return Animal(self._breed)
