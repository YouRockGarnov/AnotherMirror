import unittest
from tests.GlobalTest import GlobalTest
from implementations.units.humanoids.Humanoid import Humanoid
from implementations.units.humanoids.HumanoidRace import HumanoidRace


class TestHumanoid(unittest.TestCase, GlobalTest):
    def __init__(self):
        super().__init__()
        self._humanoid_race = HumanoidRace('Yakuns')
        self._humanoid = Humanoid(self._humanoid_race)
        self._count_of_tests = 100

    def test_all_functions_n_times(self):
        self.assertEqual(self._humanoid.health, self._humanoid_race.health)
        self.assertEqual(self._humanoid.defense, self._humanoid_race.defense)
        self.assertEqual(self._humanoid.attack, self._humanoid_race.attack)
