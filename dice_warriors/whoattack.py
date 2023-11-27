from character import Character

def Who_attack_first(char1: Character, char2: Character) -> int | str :
    if char1._attack_speed > char2._attack_speed: return 1, f"{char1.get_name()} attack first attack first because he has {char1._attack_speed} attack speed and {char2.get_name()} has {char2._attack_speed} attack speed"
    elif char1._attack_speed < char2._attack_speed: return 2, f"{char2.get_name()} attack first attack first because he has {char2._attack_speed} attack speed and {char1.get_name()} has {char1._attack_speed} attack speed"
    else: 
        rool_char1 = char1._dice.roll()
        rool_char2 = char2._dice.roll()
        if rool_char1 > rool_char2: return 1, f"{char1.get_name()} attack first because he has {rool_char1} dice rool and {char2.get_name()} has {rool_char2}"
        elif rool_char1 < rool_char2: return 2, f"{char2.get_name()} attack first because he has {rool_char2} dice rool and {char1.get_name()} has {rool_char1}"
        else: return Who_attack_first(char1, char2)
