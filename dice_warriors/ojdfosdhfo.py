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
                if 'type' in data: types.append(data['type'])

    for item in names:
        char_data[item] = {}
        char_data[item]['max_health'] = max_healths[names.index(item)]
        char_data[item]['attack'] = attacks[names.index(item)]
        char_data[item]['defense'] = defenses[names.index(item)]
        char_data[item]['current_health'] = current_healths[names.index(item)]
        char_data[item]['dice_faces'] = dice_faces[names.index(item)]
        char_data[item]['type'] = types[names.index(item)]

    return char_data

def print_all_char(info: {}):
    for item in info:
        print(f"{item} : type {info[item]['type']} / max_health {info[item]['max_health']} / attack {info[item]['attack']} / defense {info[item]['defense']} / current_health {info[item]['current_health']} / dice_faces {info[item]['dice_faces']}")

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
                if info[chosen_character]['type'] == "Warrior": return Warrior(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Mage": return Mage(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], Dice(info[chosen_character]['dice_faces']))
                if info[chosen_character]['type'] == "Thief": return Thief(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], Dice(info[chosen_character]['dice_faces']))
                else: return Character(chosen_character, info[chosen_character]['max_health'], info[chosen_character]['attack'], info[chosen_character]['defense'], Dice(info[chosen_character]['dice_faces']))
            else: print("Numéro invalide. Veuillez entrer un numéro valide.")
        except ValueError: print("Veuillez entrer un numéro.")