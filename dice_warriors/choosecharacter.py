import json
import os
from builder import builder_characters
from character import Warrior, Mage, Thief, Character
from dice import Dice
from get_info import get_infos

def print_all_char(info: {}):
    for item in info:
        print(f"{item} : type {info[item]['type']} / max_health {info[item]['max_health']} / attack {info[item]['attack']} / defense {info[item]['defense']} / current_health {info[item]['current_health']}/ attack_speed {info[item]['attack_speed']} / dice_faces {info[item]['dice_faces']}")

def choose_character():
    info = get_infos()
    print("Choose your character:")
    print("0. Build your character")
    for i, (name, stats) in enumerate(info.items(), 1): print(f"{i}. {name} - {stats['type']}")

    while True:
        try:
            choice = int(input("Insert number of chosen character : "))
            if choice == 0: return builder_characters()
            elif 1 <= choice <= len(info):
                chosen_character = list(info.keys())[choice - 1]
                if info[chosen_character]['type'] == "Warrior": return Warrior(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Mage": return Mage(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Thief": return Thief(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                else: return Character(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
            else: print("Incorrect number. Please insert a correct number.")
        except ValueError: print("Please insert a number.")




if __name__ == "__main__":
    print_all_char(get_infos())