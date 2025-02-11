# Imports
import random


# Creature Class
class Creature:
    # Constructor
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name,
            self.level
        )

    # Defensive Roll Method
    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


# Wizard SubClass of Creature
class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    # Attack Method
    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        # Determine victor of the battle
        if my_roll >= creature_roll:
            print("The wizard has handily defeated {}.".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


# Small Animal SubClass of Creature
class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


# Dragon SubClass of Creature
class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.breathes_fire = breathes_fire
        self.scaliness = scaliness

    # Override of defensive roll method
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()

        # if self.breathes_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
