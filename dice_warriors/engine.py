from character import Warrior, Mage, Thief, Character
from dice import Dice

import random

def main():
    warrior = Warrior("James", 20, 8, 3, Dice(6))
    mage = Mage("Elisa", 20, 8, 3, Dice(6))
    thief = Thief("Bastien", 20, 8, 3, Dice(6))

    cars : list[Character] = [warrior, mage, thief]
    stats = {}

    char1 = random.choice(cars)
    cars.remove(char1)

    char2 = random.choice(cars)
    cars.remove(char2)

    print(char1)
    print(char2)

    stats[char1.get_name()] = 0
    stats[char2.get_name()] = 0

    for i in range(100):
        while char1.is_alive() and char2.is_alive():
            print("--------------------------------")
            print(f"Round {i}")
            char1.attack(char2)
            char2.attack(char1)
        if char1.is_alive():
            stats[char1.get_name()] += 1
        else:
            stats[char2.get_name()] += 1

if __name__ == "__main__":
    main()