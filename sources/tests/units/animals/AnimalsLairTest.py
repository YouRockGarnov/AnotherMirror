import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.animals.AnimalsLair import AnimalsLair
from implementations.units.animals.AnimalsBreed import AnimalsBreed


class TestAnimalsLair(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._animals_lair = AnimalsLair(AnimalsBreed(1))
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        GlobalTest.test_function_n_times(self._animals_lair.create_animal, self._count_of_tests,
                                         AnimalsLair.STRENGTH.BABY_STRENGTH)
        GlobalTest.test_function_n_times(self._animals_lair.create_animal, self._count_of_tests,
                                         AnimalsLair.STRENGTH.ADULT_STRENGTH)
        GlobalTest.test_function_n_times(self._animals_lair.create_animal, self._count_of_tests,
                                         AnimalsLair.STRENGTH.LEADER_STRENGTH)
