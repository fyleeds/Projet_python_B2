import ojdfosdhfo
from ojdfosdhfo import Who_attack_first
import random
from character import Character, Warrior, Mage, Thief
from dice import Dice

def main():
    nbr_round = 1
    char = ojdfosdhfo.choose_character()
    char.json_save()
    print(char)
    drop = random.randint(1, 3)
    if drop == 1 : adv = Warrior("Gerard le guerrier", 20, 8, 3, 1, Dice(6))
    elif drop == 2 : adv = Mage("Gerard le mage", 20, 8, 3, 2, Dice(6))
    elif drop == 3 : adv = Thief("Gerard le voleur", 20, 8, 3, 3, Dice(6)) 
    while True:
        print(f"\n ------ Round {nbr_round} ------ \n")
        char.drop_item()
        adv.drop_item()
        print("battle phase :")
        who, msg = Who_attack_first(char, adv)
        if who == 1 :
            print(msg)
            char.attack(adv)
            if adv.is_alive(): adv.attack(char)
            elif not adv.is_alive() : break
            if not char.is_alive() : break
        elif who == 2 :
            print(msg) 
            adv.attack(char)
            if char.is_alive(): char.attack(adv)
            elif not char.is_alive() : break
            if not adv.is_alive() : break
        print("\nheal phase :")
        char.use_item(char.items)
        adv.use_item(adv.items)
        nbr_round += 1
        print("\n")
    if char.is_alive() : print(f"\n{char.get_name()} win !")
    elif adv.is_alive() : print(f"\n{adv.get_name()} win !")


if __name__ == "__main__":
    main()