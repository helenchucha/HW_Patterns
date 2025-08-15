# Ця програма імітує роботу таксі-диспетчера.
# Пасажир просить таксі, а диспетчер (посередник) вирішує, який водій його підвезе.
# Коли водій закінчує поїздку, він повідомляє диспетчера, що він знову готовий приймати нові замовлення.

# Dispatcher (Посередник) — головний об'єкт, який керує всією взаємодією між пасажиром і водіями.
# TaxiDispatcher (Конкретний диспетчер) — реалізація посередника. Він тримає список водіїв і знає, коли і кому призначити поїздку.
# Driver (Водій) — колега, який отримує замовлення і виконує їх. Він повідомляє диспетчера, коли закінчує поїздку.
# Passenger (Пасажир) — клієнт, який просить таксі. Він посилає запит через диспетчера.

from abc import ABC, abstractmethod

# Інтерфейс посередника
class Dispatcher(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Конкретний диспетчер таксі
class TaxiDispatcher(Dispatcher):
    def __init__(self):
        self.drivers = [
            Driver(self, "Водій 1"),
            Driver(self, "Водій 2"),
            Driver(self, "Водій 3")
        ]
        self.passenger = Passenger(self)

    def notify(self, sender, event):
        if event == "pickup_request":
            print(f"Диспетчер отримав запит на підбір від {sender.name}.")
            # Вибираємо першого доступного водія
            available_driver = next((d for d in self.drivers if d.is_available), None)
            if available_driver:
                available_driver.assign_ride()
            else:
                print("Всі водії зайняті. Спробуйте пізніше.")
        elif event == "ride_completed":
            print(f"Диспетчер отримав повідомлення, що поїздка завершена {sender.name}.")

# Колега - Водій
class Driver:
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
        self.is_available = True

    def assign_ride(self):
        if self.is_available:
            print(f"{self.name} отримав новий виклик і починає їхати.")
            self.is_available = False
            # Імітуємо завершення поїздки
            self.complete_ride()

    def complete_ride(self):
        print(f"{self.name} завершив поїздку.")
        self.is_available = True
        self.mediator.notify(self, "ride_completed")

# Колега - Пасажир
class Passenger:
    def __init__(self, mediator):
        self.mediator = mediator
        self.name = "Пасажир"

    def request_pickup(self):
        print(f"{self.name} просить підбір таксі.")
        self.mediator.notify(self, "pickup_request")


# Використання
if __name__ == "__main__":
    dispatcher = TaxiDispatcher()
    # Пасажир робить запит
    dispatcher.passenger.request_pickup()
    # Новий запит
    print("\n--- Наступний запит ---\n")
    dispatcher.passenger.request_pickup()