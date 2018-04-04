import json


class AnimalsBreed:
    def __init__(self, breed_id: int):
        fields = self.read_race(breed_id)

        self._health = fields['health']
        self._defense = fields['defense']
        self._attack = fields['attack']
        self._strength = 1

    @property
    def health(self):
        return self._health * self._strength

    @property
    def defense(self):
        return self._defense * self._strength

    @property
    def attack(self):
        return self._attack * self._strength

    def _set_strength(self, strength: int):
        self._strength = strength

    # TODO recode to another level of abstraction without dependencies on JSON
    @staticmethod
    def read_race(breed_id: int):
        json_file = open('implementations/units/animals/AnimalsStats.json')
        return json.load(json_file)[str(breed_id)]
