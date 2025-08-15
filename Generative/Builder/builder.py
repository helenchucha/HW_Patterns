'''
Будівельник — це патерн проектування, що дозволяє створювати складні об'єкти покроково.
Будівельник дає можливість використовувати той самий код будівництва для отримання
різних уявлень об'єктів.

Приклад: Створюємо будівельник для автівки, який додає різні елементи до автівок
різного призначення при створенні.
'''

from abc import ABC, abstractmethod

# Продукт - Авто
class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ', '.join(self.parts)

# Абстрактний Builder
class CarBuilder(ABC):
    def __init__(self):
        self.car = Car()

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    def build_trailer(self):
        pass

    def build_trunk(self):
        pass

    def build_climate_control(self):
        pass


    def build_child_seat(self):
        pass

    def get_result(self):
        return self.car

# Конкретні Builder-и для різних авто
class StandardAutoBuilder(CarBuilder):
    def build_body(self):
        self.car.add("Стандартний кузов")
    def build_engine(self):
        self.car.add("Бензиновий двигун")
    def build_trailer(self):
        # Немає причепу
        pass
    def build_trunk(self):
        self.car.add("Багажник")
    def build_climate_control(self):
        # Не передбачено
        pass
    def build_child_seat(self):
        # Не передбачено
        pass

class EcoAutoBuilder(CarBuilder):
    def build_body(self):
        self.car.add("Стандартний кузов")
    def build_engine(self):
        self.car.add("Електричний двигун")
    def build_trailer(self):
        pass
    def build_trunk(self):
        # Не обов'язково
        pass
    def build_climate_control(self):
        # Не обов'язково
        pass
    def build_child_seat(self):
        # Не обов'язково
        pass

class FamilyAutoBuilder(CarBuilder):
    def build_body(self):
        self.car.add("Стандартний кузов")
    def build_engine(self):
        self.car.add("Бензиновий двигун")
    def build_trailer(self):
        # Не обов'язково
        pass
    def build_trunk(self):
        self.car.add("Багажник")
    def build_climate_control(self):
        # Не обов'язково
        pass
    def build_child_seat(self):
        self.car.add("Дитяче крісло")

class TravelAutoBuilder(CarBuilder):
    def build_body(self):
        self.car.add("Посилений кузов")
    def build_engine(self):
        self.car.add("Гібридний двигун")
    def build_trailer(self):
        self.car.add("Причіп")
    def build_trunk(self):
        self.car.add("Багажник")
    def build_climate_control(self):
        self.car.add("Клімат-контроль")
    def build_child_seat(self):
        # Не передбачено
        pass

# "Керівник" процесу — "Конструктор" (можна назвати інакше)
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_body()
        self.builder.build_engine()
        self.builder.build_trailer()
        self.builder.build_trunk()
        self.builder.build_climate_control()
        self.builder.build_child_seat()

# Демонстрація
# Створимо різні авто
auto_options = [
    ("Стандартне авто", StandardAutoBuilder()),
    ("Екологічне авто", EcoAutoBuilder()),
    ("Сімейне авто", FamilyAutoBuilder()),
    ("Авто для подорожей", TravelAutoBuilder()),
]

for name, builder in auto_options:
    director = CarDirector(builder)
    director.construct()
    print(f"{name}: {builder.get_result().list_parts()}")