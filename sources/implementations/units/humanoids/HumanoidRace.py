import json


class HumanoidRace:
    def __init__(self, name_of_race: str):
        fields = self.read_race(name_of_race)

        self._health = fields['health']
        self._defense = fields['defense']
        self._attack = fields['attack']

    @property
    def health(self):
        return self._health

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._attack

    # TODO recode to another level of abstraction without dependencies on JSON
    @staticmethod
    def read_race(name_of_race: str):
        json_file = open('implementations/units/humanoids/HumanoidStats.json')
        return json.load(json_file)[name_of_race]

