from __future__ import annotations

class Item :
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return f"{self._name}"


class Potion(Item):

    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal

    def use(self, user):
        user.increase_health(self.heal)
        print(f"🧪 {user.get_name()} use {self._name} and restore {self.heal} hp !")
        user.show_healthbar()

    def __str__(self):
        return f"{self._name} et restore {self.heal} hp !"


little_potion = Potion("Little Potion", 1)
medium_potion = Potion("Medium Potion", 2)
big_potion = Potion("Big Potion", 5)