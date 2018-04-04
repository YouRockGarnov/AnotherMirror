from implementations.units.humanoids.HumanoidRace import HumanoidRace


class Humanoid:
    def __init__(self, race: HumanoidRace):
        self._race = race
        self._health = race.health
        self._defense = race.defense
        self._weapons = list()

    @property
    def health(self):
        return self._health

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._race.attack

