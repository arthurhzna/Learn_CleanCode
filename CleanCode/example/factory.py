from abc import ABC, abstractmethod

class Food(ABC):
    factory = None

    @classmethod
    def create(cls, name):
        return cls.factory.make_food(name) // <---------- 

    @abstractmethod
    def eat(self):
        pass
        
class Burger(Food):
    def eat(self):
        return "Makan Burger 🍔"


class Pizza(Food):
    def eat(self):
        return "Makan Pizza 🍕"
        
        
class FoodFactory:
    def make_food(self, name):
        if name == "burger":
            return Burger()
        elif name == "pizza":
            return Pizza()
        else:
            raise ValueError("Menu tidak ada")
Food.factory = FoodFactory()
food1 = Food.create("burger")
food2 = Food.create("pizza")

print(food1.eat())
print(food2.eat())
