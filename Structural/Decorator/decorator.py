'''
Декоратор - це структурний патерн проектування,
який дозволяє динамічно додавати об'єктам нову функціональність,
обертаючи їх у корисні обгортки.
'''

# Базовий клас напою
class Drink:
    def get_description(self):
        return "Сам напій"

    def get_cost(self):
        return 0

# Конкретний напій
class Coffee(Drink):
    def get_description(self):
        return "Кава"

    def get_cost(self):
        return 20  # ціна за каву

# Декоратор - базовий клас для добавок
class AdditiveDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

    def get_description(self):
        return self.drink.get_description()

    def get_cost(self):
        return self.drink.get_cost()

# Конкретні добавки
class Milk(AdditiveDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Молоко"

    def get_cost(self):
        return self.drink.get_cost() + 5

class Sugar(AdditiveDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Цукор"

    def get_cost(self):
        return self.drink.get_cost() + 2

class Cinnamon(AdditiveDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Кориця"

    def get_cost(self):
        return self.drink.get_cost() + 3

# Використання
def main():
    # Створюємо базовий напій
    my_coffee = Coffee()

    # Додаємо молоко і цукор
    my_coffee_with_milk = Milk(my_coffee)
    my_coffee_with_milk_and_sugar = Sugar(my_coffee_with_milk)

    print("Опис:", my_coffee_with_milk_and_sugar.get_description())
    print("Ціна:", my_coffee_with_milk_and_sugar.get_cost(), "грн")

    # Додаємо тільки корицю
    сinnamon_coffee = Cinnamon(Coffee())
    print("Опис:",  сinnamon_coffee.get_description())
    print("Ціна:",  сinnamon_coffee.get_cost(), "грн")

if __name__ == "__main__":
    main()