from __future__ import annotations
from dice import Dice
import item
import json
import random

class MessageManager:
    pass

class Character:
    
    def __init__(self, name: str, max_health: int, attack: int, defense: int,attack_speed: int, dice) -> None:
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._attack_speed = attack
        self._attack_speed = attack_speed
        self._dice = dice
        self.items = []
        
    def __str__(self):
        return f"I'm {self._name} the {self.__class__.__name__} with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def get_name(self):
        return self._name
        
    def get_defense_value(self):
        return self._defense_value
    
    def is_alive(self):
        return self._current_health > 0
        
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0:
            amount = self._current_health
        self._current_health -= amount
        self.show_healthbar()
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"{self._name} : [{"🥰" * self._current_health}{"🖤" * missing_hp}] {self._current_health}/{self._max_health}hp"
        print(healthbar)

    def compute_damages(self, roll, target):
        return self._attack_value + roll

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages in your face ! (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)
    
    def compute_wounds(self, damages, roll, attacker):
        wounds = damages - self._defense_value - roll
        if wounds < 0:
            wounds = 0
        return wounds
    
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        wounds = self.compute_wounds(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

    def json_save(self):
        char_data = {
            'name' : self._name,
            'max_health' : self._max_health,
            'attack' : self._attack_value,
            'defense' : self._defense_value,
            'current_health' : self._current_health,
            'dice_faces' : self._dice._nbr_faces,
            'attack_speed' : self._attack_speed,
            'type' :  self.__class__.__name__,
        }
        filename = f"db_char\\{self._name}_character.json"
        with open(filename, 'w') as f:
            json.dump(char_data, f, indent=4)
        print(f"Character saved in {filename}")
    
    def drop_item(self):
        drop = random.randint(1, 3)
        if drop == 3: self.items.append(item.big_potion)
        elif drop == 2: self.items.append(item.medium_potion)
        elif drop == 1: self.items.append(item.little_potion)
    
    def show_item(self):
        for item in self.items:
            print(item)

    def use_item(self, items):
        items[0].use(self)
        items.pop(0)

    def increase_health(self, amount):
        if (self._current_health + amount) > self._max_health:
            amount = self._max_health - self._current_health
        self._current_health += amount


class Warrior(Character):

    def compute_damages(self, roll, target):
        print("🪓 Bonus: Axe in your face (+3 attack)")
        return super().compute_damages(roll, target) + 3

class Mage(Character):

    def compute_wounds(self, damages, roll, attacker):
        print("🧙 Bonus: Magic armor (-3 wounds)")
        return super().compute_wounds(damages, roll, attacker) - 3

class Thief(Character):

    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneacky attack (ignore defense: + {target.get_defense_value()} bonus)")
        return super().compute_damages(roll, target) + target.get_defense_value()

if __name__ == "__main__":
    char1 = Character("Gerard", 20, 8, 3, Dice(6))
    char1.attack(char1)
    char1.drop_item()
    char1.show_item()
    char1.use_item(char1.items)
