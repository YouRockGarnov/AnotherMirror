import json


class WeaponType:
    def __init__(self, weapon_id):
        fields = self._read_weapon(weapon_id)
        self._damage = fields['damage']
        self._num_weapons = -1 # TODO default num is -1 = none. but i don't know what is it

    @property
    def num_weapons(self):
        if self._num_weapons == -1:
            json_file = open('implementations/units/humanoids/WeaponsStats.json')
            self._num_weapons = len(json.load(json_file).keys())
            json_file.close()
        return self._num_weapons

    @staticmethod
    def _read_weapon(weapon_id: int):
        json_file = open('implementations/units/humanoids/WeaponsStats.json')
        return json.load(json_file)[weapon_id]

    @property
    def damage(self):
        return self._damage
