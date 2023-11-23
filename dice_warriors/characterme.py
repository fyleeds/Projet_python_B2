from dice import Dice

class Character:
    
    def __init__(self, name : str, max_health : int, attack : int, defense : int, dice) -> None:
        self._name = name
        self._max_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._health = self._max_health
        self._dice = dice

    def __str__(self) -> str:
        return f"I'm {self._name} the Character with : {self._attack_value} attack / {self._defense_value} defense"
    
    def is_alive(self):
        return self._health > 0

    def show_health_bar(self):
        print(f"[{'🥰' * self._health}{'🖤' * (self._max_health - self._health)}] {self._health}/{self._max_health}")

    # def take_damage(self, damage : int):
    #     self._health -= damage
    #     if self._health < 0 : self._health = 0
    #     self.show_health_bar()

    def attack(self) -> int:
        if not self.is_alive() : return
        damage = self._attack_value + self._dice.roll()
        print(f'{damage} damage in your face ! (attack : {self._attack_value} + dice : {damage - self._attack_value})')
        return damage
    
    def defense(self, damages : int):
        roll = self._dice.roll()
        wounds = damages - self._defense_value - roll
        print(f"{wounds} wounds in my face ! (damages : {damages} - defense : {self._defense_value} - dice : {roll})")

    def json_save(self):
        char_data = {
            'name' : self._name,
            'max_health' : self._max_health,
            'attack' : self._attack_value,
            'defense' : self._defense_value,
            'dice' : self._dice
            
        }

if __name__ == "__main__":
    a_dice = Dice()
   
    character1 = Character("Gerard", 20, 8, 3, Dice())
    print(character1)

    damage = character1.attack()
    character1.defense(damage)
    print(character1.show_health_bar())
    