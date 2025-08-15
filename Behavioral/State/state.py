# Цей код моделює роботу кавової машини.
# Машина може бути у різних станах:
# - очікує
# - обробляє замовлення
# - готова до видачі напою
#
# В залежності від стану, вона реагує по-різному на дії користувача.

from abc import ABC, abstractmethod

# Абстрактний клас стану
class CoffeeMachineState(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def press_button(self, context):
        pass

    @abstractmethod
    def dispense(self, context):
        pass

# Конкретний стан - Очікує
class WaitingState(CoffeeMachineState):
    def insert_coin(self, context):
        print("Монета вставлена. Тепер натисніть кнопку для початку приготування.")
        context.state = ProcessingState()

    def press_button(self, context):
        print("Спершу вставте монету.")

    def dispense(self, context):
        print("Немає напою для видачі.")

# Конкретний стан - Обробляє
class ProcessingState(CoffeeMachineState):
    def insert_coin(self, context):
        print("Вже обробляє. Зачекайте.")

    def press_button(self, context):
        print("Ви натиснули кнопку, напій готується.")

    def dispense(self, context):
        print("Напій готовий! Видаємо його.")
        context.state = ReadyState()

# Конкретний стан - Готово
class ReadyState(CoffeeMachineState):
    def insert_coin(self, context):
        print("Будь ласка, дочекайтеся, поки попередній напій буде виданий.")

    def press_button(self, context):
        print("Вам вже видано напій.")

    def dispense(self, context):
        print("Ви отримали свій напій. Готово до нового замовлення.")
        context.state = WaitingState()

# Контекст - кавова машина
class CoffeeMachine:
    def __init__(self):
        self.state = WaitingState()

    def insert_coin(self):
        self.state.insert_coin(self)

    def press_button(self):
        self.state.press_button(self)

    def dispense(self):
        self.state.dispense(self)

# Демонстрація роботи
if __name__ == "__main__":
    machine = CoffeeMachine()

    machine.insert_coin()      # вставляємо монету, переходимо до Обробляє
    machine.press_button()     # натискаємо кнопку, готуємо напій
    machine.dispense()         # видаємо напій, повертаємось до Очікує
    print("---")
    machine.press_button()     # спроба натиснути без монети
    machine.insert_coin()      # вставляємо монету
    machine.dispense()         # намагаємося отримати напій без обробки
    machine.press_button()     # натискаємо кнопку
    machine.dispense()         # отримуємо напій