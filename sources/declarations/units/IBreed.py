import abc
import json

class IBreed:
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass

    def read_breed(self, breed_id: int):
        json_file = open('implementations/units/animals/AnimalsStats.json')
        return json.load(json_file)[breed_id]