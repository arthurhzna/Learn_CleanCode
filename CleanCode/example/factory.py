from abc import ABC, abstractmethod


# ======================
# 1. Abstract Base Class
# ======================
class Food(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass


# ======================
# 2. Concrete Classes
# ======================
class Burger(Food):
    def eat(self) -> str:
        return "🍔 Makan Burger"


class Pizza(Food):
    def eat(self) -> str:
        return "🍕 Makan Pizza"


class KrabbyPatty(Food):
    def eat(self) -> str:
        return "🦀 Makan Krabby Patty"


# ======================
# 3. Factory (Registry Pattern)
# ======================
class FoodFactory:
    def __init__(self):
        self._creators = {}

    def register(self, name: str, creator):
        self._creators[name] = creator

    def make_food(self, name: str) -> Food:
        creator = self._creators.get(name)
        if not creator:
            raise ValueError(f"Menu '{name}' tidak tersedia")
        return creator()


# ======================
# 4. Setup (Wiring)
# ======================
factory = FoodFactory()

factory.register("burger", Burger)
factory.register("pizza", Pizza)
factory.register("krabby", KrabbyPatty)


# ======================
# 5. Usage
# ======================
def main():
    # food1 = factory.make_food("burger")
    # food2 = factory.make_food("pizza")
    # food3 = factory.make_food("krabby")

    # print(food1.eat())
    # print(food2.eat())
    # print(food3.eat())

menu = ["burger", "pizza", "krabby"]

foods = []
for name in menu:
    foods.append(factory.make_food(name))

for food in foods:
    print(food.eat())


if __name__ == "__main__":
    main()
