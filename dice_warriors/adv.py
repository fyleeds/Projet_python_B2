from character import Character, Warrior, Mage, Thief
from dice import Dice
import random

def adversaire():
    drop = random.randint(1, 3)
    if drop == 1 : return Warrior("Gerard le guerrier", 20, 8, 3, 1, Dice(6))
    elif drop == 2 : return Mage("Gerard le mage", 20, 8, 3, 2, Dice(6))
    elif drop == 3 : return Thief("Gerard le voleur", 20, 8, 3, 3, Dice(6)) 