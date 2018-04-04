import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.animals.AnimalsBreed import AnimalsBreed


class TestAnimalsBreed(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._animals_breed = AnimalsBreed(1)
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        # GlobalTest.test_function_n_times(self._animals_breed.health, self._count_of_tests)
        # GlobalTest.test_function_n_times(self._animals_breed.defense, self._count_of_tests)
        # GlobalTest.test_function_n_times(self._animals_breed.attack, self._count_of_tests)
        GlobalTest.test_function_n_times(self._animals_breed.read_race, self._count_of_tests, '1')
