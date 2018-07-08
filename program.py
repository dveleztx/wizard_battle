# Program    : Wizard Battle
# Author     : David Velez
# Date       : 07/08/2018
# Description: Wizard Battle App from Python Training Vids from Michael Kennedy


# Imports
import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


# Main Function
def main():
    print_header()
    game_loop()


# Print the Header
def print_header():
    print("------------------------")
    print("    WIZARD GAME APP")
    print("------------------------")
    print()


# Game Logic
def game_loop():

    # Create Creature Objects
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 75, True),
        Wizard("Evil Wizard", 1000),
    ]

    # Create Hero Object
    hero = Wizard("Certneilius", 75)

    # Play the Game
    while True:

        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from a dark and foggy forest..."
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print("The wizard has become unsure of his power and flees!!!")
        elif cmd == 'l':
            print("The wizard {} takes in the surroundings and sees: ".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")

        print()


# Main
if __name__ == '__main__':
    main()
