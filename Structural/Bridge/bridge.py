'''
Міст – це структурний патерн проектування, який поділяє один чи кілька класів на дві окремі ієрархії
– абстракцію та реалізацію, дозволяючи змінювати їх незалежно один від одного.

Приклад: Створюємо морозива з різними смаками та кольорами.
'''

from abc import ABC, abstractmethod


# Реалізатор (Color)
class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass


class RedColor(Color):
    def fill_color(self):
        return "червоний"


class YellowColor(Color):
    def fill_color(self):
        return "жовтий"


class BrownColor(Color):
    def fill_color(self):
        return "коричневий"


# Реалізатор (Flavor)
class Flavor(ABC):
    @abstractmethod
    def fill_flavor(self):
        pass


class VanillaFlavor(Flavor):
    def fill_flavor(self):
        return "ванільного смаку"


class ChocolateFlavor(Flavor):
    def fill_flavor(self):
        return "шоколадного смаку"


class StrawberryFlavor(Flavor):
    def fill_flavor(self):
        return "полуничного смаку"


# Абстракція (IceCream)
class IceCream(ABC):
    def __init__(self, color: Color, flavor: Flavor):
        self.color = color
        self.flavor = flavor

    @abstractmethod
    def get_description(self):
        pass


# Конкретна реалізація смаків морозива
class RealIceCream(IceCream):
    def get_description(self):
        return f"Морозиво {self.flavor.fill_flavor()} з {self.color.fill_color()} кольором"


# Використання
def main():
    # Створюємо різні комбінації смаків та кольорів
    vanilla_red = RealIceCream(RedColor(), VanillaFlavor())
    vanilla_yellow = RealIceCream(YellowColor(), VanillaFlavor())
    chocolate_brown = RealIceCream(BrownColor(), ChocolateFlavor())
    strawberry_red = RealIceCream(RedColor(), StrawberryFlavor())

    # Вивід описів
    print(vanilla_red.get_description())
    print(vanilla_yellow.get_description())
    print(chocolate_brown.get_description())
    print(strawberry_red.get_description())


if __name__ == "__main__":
    main()
