import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.humanoids.HumanoidCreator import HumanoidCreator


class TestHumanoidCreator(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._humanoid_creator = HumanoidCreator('Yakuns')
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        GlobalTest.test_function_n_times(self._humanoid_creator.create, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_creator._set_default_properties, self._count_of_tests)
        GlobalTest.test_function_n_times(self._humanoid_creator._set_weapons, self._count_of_tests)
