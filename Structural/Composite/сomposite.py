'''
Компонувальник - це структурний патерн проектування,
який дозволяє згрупувати безліч об'єктів у деревоподібну структуру,
а потім працювати з нею так, ніби це одиничний об'єкт.

Приклад: Демонструє меню кафе
'''

from abc import ABC, abstractmethod

# Базовий компонент
class MenuComponent(ABC):
    def add(self, menu_component):
        pass

    def remove(self, menu_component):
        pass

    def get_child(self, index):
        pass

    @abstractmethod
    def print(self, indent=0):
        pass

# Конкретна страва
class MenuItem(MenuComponent):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def print(self, indent=0):
        print("  " * indent + f"{self.name} - {self.price}$")
        print("  " * (indent + 1) + self.description)

# Меню та підменю
class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.menu_components = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, index):
        return self.menu_components[index]

    def print(self, indent=0):
        print("  " * indent + f"\n{self.name}")
        print("  " * indent + "-" * len(self.name))
        for component in self.menu_components:
            component.print(indent + 1)

# Використання
def main():
    # Головне меню
    main_menu = Menu("Меню ресторана")

    # Створюємо підменю напоїв
    drinks_menu = Menu("Напої")
    tea_menu = Menu("Чаї")
    coffee_menu = Menu("Кава")
    juice_menu = Menu("Соки")

    # Додаємо страви до підменю "Кава"
    coffee_menu.add(MenuItem("Кава по-турецьки", "Чорна кава з меленої кави", 3))
    coffee_menu.add(MenuItem("Капучино", "Кава з молочною пінкою", 2.5))
    coffee_menu.add(MenuItem("Американо", "Оригінальна кава", 2))

    # Додаємо страви до підменю "Чаї"
    tea_menu.add(MenuItem("Зелений чай", "Зелений чай з м'ятою", 1.8))
    tea_menu.add(MenuItem("Чорний чай", "Класичний чорний чай", 1.5))

    # Додаємо страви до підменю "Соки"
    juice_menu.add(MenuItem("Апельсиновий сік", "Свіжовичавлений апельсиновий сік", 2.5))
    juice_menu.add(MenuItem("Яблучний сік", "Свіжий яблучний сік", 2.2))

    # Створюємо головне підменю "Напої" і додаємо туди всі підкатегорії
    drinks_menu.add(tea_menu)
    drinks_menu.add(coffee_menu)
    drinks_menu.add(juice_menu)

    # Створюємо інше меню
    food_menu = Menu("Страви")
    food_menu.add(MenuItem("Піцца", "Піцца з сиром і томатами", 7))
    food_menu.add(MenuItem("Бургер", "Бургер з яловичиною", 5))

    # Додаємо підменю до головного меню
    main_menu.add(drinks_menu)
    main_menu.add(food_menu)

    # Вивід меню
    main_menu.print()

if __name__ == "__main__":
    main()