'''
Це патерн проектування, який дозволяє створювати сімейства об'єктів
без вказання конкретних класів цих об'єктів. Іншими словами, він
допомагає створювати групи взаємопов’язаних або взаємозалежних
об’єктів, залишаючи процес створення гнучким і розширюваним.

Приклад: Фабрика жіночих та чоловічих комплектів речей.
Створюємо абстрактну фабрику, яка створює окремі блузки та штани.
На її основі створюємо окремі фабрики для чоловічих та жіночих речей.
'''

from abc import ABC, abstractmethod

# Абстрактні товари
class Shirt(ABC):
    @abstractmethod
    def wear(self):
        pass

class Pants(ABC):
    @abstractmethod
    def wear(self):
        pass

# Конкретні товари для чоловіків
class MenShirt(Shirt):
    def wear(self):
        return "Чоловіча сорочка"

class MenPants(Pants):
    def wear(self):
        return "Чоловічі штани"

# Конкретні товари для жінок
class WomenShirt(Shirt):
    def wear(self):
        return "Жіноча сорочка"

class WomenPants(Pants):
    def wear(self):
        return "Жіночі штани"

# Абстрактна фабрика
class ClothingFactory(ABC):
    @abstractmethod
    def create_shirt(self) -> Shirt:
        pass

    @abstractmethod
    def create_pants(self) -> Pants:
        pass

# Конкретна фабрика для чоловічого одягу
class MenClothingFactory(ClothingFactory):
    def create_shirt(self) -> Shirt:
        return MenShirt()

    def create_pants(self) -> Pants:
        return MenPants()

# Конкретна фабрика для жіночого одягу
class WomenClothingFactory(ClothingFactory):
    def create_shirt(self) -> Shirt:
        return WomenShirt()

    def create_pants(self) -> Pants:
        return WomenPants()

# Створення та виведення набору одягу для різних клієнтів (чоловіків, жінок)
def dress_up(factory: ClothingFactory):
    shirt = factory.create_shirt()
    pants = factory.create_pants()

    print(f"Обрано: {shirt.wear()}")
    print(f"Обрано: {pants.wear()}")

# Демонстрація наборів одягу для клієнтів
print("Одяг для чоловіка:")
men_factory = MenClothingFactory()
dress_up(men_factory)

print("\nОдяг для жінки:")
women_factory = WomenClothingFactory()
dress_up(women_factory)