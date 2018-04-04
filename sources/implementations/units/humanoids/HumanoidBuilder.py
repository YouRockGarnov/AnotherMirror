from implementations.units.humanoids.Humanoid import Humanoid
from implementations.units.humanoids.HumanoidRace import HumanoidRace
from implementations.units.humanoids.WeaponType import WeaponType
import random


class HumanoidBuilder:
    def __init__(self, name_of_race: str):
        self._race = HumanoidRace(name_of_race)
        self._product = Humanoid(self._race)

    def get_humanoid(self):
        return self._product

    def create_product(self):
        self._product = Humanoid(self._race)

    def set_health(self):
        self._product._health = self._race.health

    def set_defense(self):
        self._product._defense = self._race.defense

    def set_attack(self):
        self._product._attack = self._race.attack

    def add_weapon(self, weapon_id):
        weapon = WeaponType(weapon_id)
        self._product._weapons.append(weapon)

    def add_random_weapon(self):
        weapon_id = random.randint(1, WeaponType('1').num_weapons)
        self.add_weapon(str(weapon_id))
