import random

class Dice:

    def __init__(self, nbr_faces : int = 6) :
        self._nbr_faces = nbr_faces

    def roll(self):
        return random.randint(1, self._nbr_faces)

    def __str__(self):
        return f"I'm a {self._nbr_faces} face dice"
    

class RiggedDice(Dice):
    
    def roll(self, boolean : bool = False):
        if boolean : return self._nbr_faces
        else : return super().roll()

if __name__ == "__main__":
    a_dice = Dice()
    print(a_dice)
    print(a_dice.roll())

    a_rigged_dice = RiggedDice(12)
    print(a_rigged_dice)
    print(a_rigged_dice.roll(True))
item_dice = Dice(100)