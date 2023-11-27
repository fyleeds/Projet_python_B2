import os
import json


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

if __name__ == "__main__":
    print(get_infos())