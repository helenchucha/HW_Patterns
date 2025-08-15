# Цей код показує, як за допомогою шаблонного методу можна створювати різні напої (каву і чай),
# дотримуючись одного загального плану приготування.

from abc import ABC, abstractmethod

# Абстрактний клас з шаблонним методом
class Beverage(ABC):

    # Шаблонний метод
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Кип'ятимо воду.")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Переливаємо у чашку.")

    @abstractmethod
    def add_condiments(self):
        pass

# Конкретний клас - кава
class Coffee(Beverage):
    def brew(self):
        print("Заварюємо каву.")

    def add_condiments(self):
        print("Додаємо цукор і молоко.")

# Конкретний клас - чай
class Tea(Beverage):
    def brew(self):
        print("Заварюємо чай.")

    def add_condiments(self):
        print("Додаємо лимон.")

# Демонстрація
if __name__ == "__main__":
    print("Готуємо каву:")
    coffee = Coffee()
    coffee.prepare()

    print("\nГотуємо чай:")
    tea = Tea()
    tea.prepare()