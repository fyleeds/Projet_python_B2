from __future__ import annotations
from character import Warrior, Mage, Thief, Character
from dice import Dice
from verif import verify

def builder_characters():
    username = input(str("Hello my friend ! What's your name ? : "))
    if verify(username) : 
        print(f"Welcome {username} ! Now you can choose your character !")
        print("1. Warrior 🪓")
        print("2. Mage 🧙")
        print("3. Thief 🗡️")
        print("4. Exit 🚪")
        classe = int(input("What's your choice ? : "))
        if classe == 1:
            print(f"Ok {username}, you are now a Warrior !")
            return Warrior(username, 20, 8, 3, 1, Dice(6))
        elif classe == 2:
            print(f"Ok {username}, you are now a Mage !")
            return Mage(username, 20, 8, 3, 2, Dice(6))
        elif classe == 3:
            print(f"Ok {username}, you are now a Thief !")
            return Thief(username, 20, 8, 3, 3, Dice(6))
        elif classe == 4:
            print("Goodbye !")
            exit()
        else:
            print("Please choose a number between 1 and 4")
            builder_characters()
    elif not verify(username):
        print("This name is already taken !")
        builder_characters()

    

if __name__ == "__main__":
    char1 = builder_characters()
    print(char1)
    char1.json_save()

