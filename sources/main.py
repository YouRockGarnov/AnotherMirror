from tests.units.humanoids.HumanoidBuilderTest import TestHumanoidBuilder
from tests.units.humanoids.HumanoidCreatorTest import TestHumanoidCreator
from tests.units.humanoids.HumanoidTest import TestHumanoid
from tests.units.humanoids.HumanoidRaceTest import TestHumanoidRace
from tests.units.humanoids.WeaponTypeTest import TestWeaponType
from tests.units.animals.AnimalsBreedTest import TestAnimalsBreed
from tests.units.animals.AnimalsLairTest import TestAnimalsLair


def main():
    test_humanoid_builder = TestHumanoidBuilder()
    test_humanoid_builder.test_all_functions_n_times()

    test_humanoid_creator = TestHumanoidCreator()
    test_humanoid_creator.test_all_functions_n_times()

    test_humanoid = TestHumanoid()
    test_humanoid.test_all_functions_n_times()

    test_humanoid_race = TestHumanoidRace()
    test_humanoid_race.test_all_functions_n_times()

    test_weapon_type = TestWeaponType()
    test_weapon_type.test_all_functions_n_times()

    test_animals_breed = TestAnimalsBreed()
    test_animals_breed.test_all_functions_n_times()

    test_animals_lair = TestAnimalsLair()
    test_animals_lair.test_all_functions_n_times()


if __name__ == '__main__':
    main()
