from implementations.units.humanoids.HumanoidBuilder import HumanoidBuilder
import random


class HumanoidCreator:
    def __init__(self, name_of_race: str):
        self._builder = HumanoidBuilder(name_of_race)

    def create(self):
        self._builder.create_product()
        self._set_default_properties()
        self._set_weapons()

    def _set_default_properties(self):
        self._builder.set_attack()
        self._builder.set_defense()
        self._builder.set_health()

    def _set_weapons(self):
        BASE_CHANCE_OF_ADDING_WEAPON = 8
        REDUCING_CHANCE = 2
        chance_of_adding_weapon = BASE_CHANCE_OF_ADDING_WEAPON

        while random.randint(1, 10) <= chance_of_adding_weapon:
            self._builder.add_random_weapon()
            chance_of_adding_weapon /= REDUCING_CHANCE

