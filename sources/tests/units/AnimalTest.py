import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.animals.Animal import Animal
from implementations.units.animals.AnimalsBreed import AnimalsBreed


class TestAnimal(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._animals_breed = AnimalsBreed(1)
        self._animal = Animal(self._animals_breed)
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        self.assertEqual(self._animal.health, self._animals_breed.health)
        self.assertEqual(self._animal.defense, self._animals_breed.defense)
        self.assertEqual(self._animal.attack, self._animals_breed.attack)
