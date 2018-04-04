import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.humanoids.WeaponType import WeaponType


class TestWeaponType(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._weapon_type = WeaponType('1')
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        GlobalTest.test_function_n_times(self._weapon_type._read_weapon, self._count_of_tests, '1')
        # GlobalTest.test_function_n_times(self._weapon_type.damage, self._count_of_tests)
