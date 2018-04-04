import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.humanoids.HumanoidRace import HumanoidRace


class TestHumanoidRace(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._humanoid_race = HumanoidRace('Yakuns')
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        #GlobalTest.test_function_n_times(self._humanoid_race.health, self._count_of_tests)
        #GlobalTest.test_function_n_times(self._humanoid_race.defense, self._count_of_tests)
        #GlobalTest.test_function_n_times(self._humanoid_race.attack, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_race.read_race, self._count_of_tests, 'Yakuns')
