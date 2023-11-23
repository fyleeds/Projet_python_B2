import json
import os
from builder import builder_characters
from character import Warrior, Mage, Thief, Character
from dice import Dice

def get_infos():
    names = []
    max_healths = []
    attacks = []
    defenses = []
    current_healths = []
    dice_faces = []
    attacks_speeds = []
    types = []
    char_data = {}
    
    for filename in os.listdir("db_char"):
        if filename.endswith(".json"):
            file_path = os.path.join("db_char", filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if 'name' in data: names.append(data['name'])
                if 'max_health' in data: max_healths.append(data['max_health'])
                if 'attack' in data: attacks.append(data['attack'])
                if 'defense' in data: defenses.append(data['defense'])
                if 'current_health' in data: current_healths.append(data['current_health'])
                if 'dice_faces' in data: dice_faces.append(data['dice_faces'])
                if 'attack_speed' in data: attacks_speeds.append(data['attack_speed'])
                if 'type' in data: types.append(data['type'])

    for item in names:
        char_data[item] = {}
        char_data[item]['max_health'] = max_healths[names.index(item)]
        char_data[item]['attack'] = attacks[names.index(item)]
        char_data[item]['defense'] = defenses[names.index(item)]
        char_data[item]['current_health'] = current_healths[names.index(item)]
        char_data[item]['dice_faces'] = dice_faces[names.index(item)]
        char_data[item]['attack_speed'] = attacks_speeds[names.index(item)]
        char_data[item]['type'] = types[names.index(item)]

    return char_data

def print_all_char(info: {}):
    for item in info:
        print(f"{item} : type {info[item]['type']} / max_health {info[item]['max_health']} / attack {info[item]['attack']} / defense {info[item]['defense']} / current_health {info[item]['current_health']}/ attack_speed {info[item]['attack_speed']} / dice_faces {info[item]['dice_faces']}")

def choose_character():
    info = get_infos()
    print("Choisissez un personnage:")
    print("0. Construire un personnage de zéro")
    for i, (name, stats) in enumerate(info.items(), 1): print(f"{i}. {name} - {stats['type']}")

    while True:
        try:
            choice = int(input("Entrez le numéro du personnage choisi : "))
            if choice == 0: return builder_characters()
            elif 1 <= choice <= len(info):
                chosen_character = list(info.keys())[choice - 1]
                if info[chosen_character]['type'] == "Warrior": return Warrior(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Mage": return Mage(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Thief": return Thief(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
                else: return Character(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], info[chosen_character]['attack_speed'], Dice(info[chosen_character]['dice_faces']))
            else: print("Numéro invalide. Veuillez entrer un numéro valide.")
        except ValueError: print("Veuillez entrer un numéro.")

def Who_attack_first(char1: Character, char2: Character) -> int | str :
    if char1._attack_speed > char2._attack_speed: return 1, f"{char1.get_name()} attack first attack first because he has {char1._attack_speed} attack speed and {char2.get_name()} has {char2._attack_speed} attack speed"
    elif char1._attack_speed < char2._attack_speed: return 2, f"{char2.get_name()} attack first attack first because he has {char2._attack_speed} attack speed and {char1.get_name()} has {char1._attack_speed} attack speed"
    else: 
        rool_char1 = char1._dice.roll()
        rool_char2 = char2._dice.roll()
        if rool_char1 > rool_char2: return 1, f"{char1.get_name()} attack first because he has {rool_char1} dice rool and {char2.get_name()} has {rool_char2}"
        elif rool_char1 < rool_char2: return 2, f"{char2.get_name()} attack first because he has {rool_char2} dice rool and {char1.get_name()} has {rool_char1}"
        else: return Who_attack_first(char1, char2)


if __name__ == "__main__":
    print_all_char(get_infos())