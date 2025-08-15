'''
Фабричний метод — це спосіб створювати різні об'єкти, не вказуючи прямо,
який саме об'єкт створюється. Замість того, щоб писати код, який створює
конкретний об'єкт, ми залишаємо цю задачу спеціальному методу — фабриці.
Це дуже зручно, коли у тебе багато схожих об'єктів або потрібно додавати
нові без змін у коді, який вже існує.

Приклад: Ферма з різними тваринами. Створюємо базовий клас Animal, на
основі якого додаємо до ферми нових тварин.
'''

from abc import ABC, abstractmethod

# Базовий клас Тварина
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def produce(self):
        pass

# Конкретні тварини
class Cow(Animal):
    def eat(self):
        print("Корова їсть сіно.")

    def produce(self):
        print("Корова дає молоко.")

class Pig(Animal):
    def eat(self):
        print("Свиня їсть висівки.")

    def produce(self):
        print("Свиня дає м'ясо.")

class Sheep(Animal):
    def eat(self):
        print("Вівця їсть траву.")

    def produce(self):
        print("Вівця дає вовну.")

# Абстрактна ферма
class Farm(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    def care_for_animal(self):
        animal = self.create_animal()
        animal.eat()
        animal.produce()

# Конкретні ферми
class CowFarm(Farm):
    def create_animal(self):
        return Cow()

class PigFarm(Farm):
    def create_animal(self):
        return Pig()

class SheepFarm(Farm):
    def create_animal(self):
        return Sheep()

# Використання
if __name__ == "__main__":
    farms = [CowFarm(), PigFarm(), SheepFarm()]

    for farm in farms:
        farm.care_for_animal()
        print("---")