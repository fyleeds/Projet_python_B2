from character import Character, Warrior, Mage, Thief
from dice import Dice
import random

def adversaire():
    drop = random.randint(1, 3)
    if drop == 1 : return Warrior("Gerard le guerrier", 25, 6, 5, 1, Dice(6))
    elif drop == 2 : return Mage("Gerard le mage", 16, 7, 3, 2, Dice(6))
    elif drop == 3 : return Thief("Gerard le voleur", 20, 7, 3, 3, Dice(6)) 
