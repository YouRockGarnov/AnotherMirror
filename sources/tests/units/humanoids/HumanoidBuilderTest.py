import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.humanoids.HumanoidBuilder import HumanoidBuilder


# can i do all of functions of object when i don't know about them?


class TestHumanoidBuilder(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._humanoid_builder = HumanoidBuilder('Yakuns')
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        GlobalTest.test_function_n_times(self._humanoid_builder.create_product, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_builder.set_attack, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_builder.set_defense, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_builder.set_health, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_builder.add_weapon, self._count_of_tests, '1')
        GlobalTest.test_function_n_times(self._humanoid_builder.get_humanoid, self._count_of_tests)
