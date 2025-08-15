'''
Адаптер – це структурний патерн проектування, що дозволяє об'єктам
з несумісними інтерфейсами працювати разом.

Приклад: Старий зарядний пристрій для мобільного телефону з роз'ємом Micro USB,
а новий телефон має роз'єм USB-C. Щоб підключити новий телефон до старого зарядного
пристрою, потрібен адаптер.
'''

# Старий зарядний пристрій з Micro USB
class OldCharger:
    def charge(self):
        return "Зарядка через Micro USB. Зарядка через USB-C не виконується!"

# Новий телефон з USB-C
class NewPhone:
    def __init__(self):
        self.port = "USB-C"

    def connect(self):
        return "Новий телефон з'єднано через USB-C"

# Адаптер, що робить новий телефон сумісним з старим зарядним пристроєм
class ChargerAdapter:
    def __init__(self, new_phone):
        self.new_phone = new_phone

    def charge(self):
        # Використовуємо метод нового телефону для зарядки
        return f"Адаптер: {self.new_phone.connect()} та зарядка через Micro USB"

# Використання
old_charger = OldCharger()
new_phone = NewPhone()

# Без адаптера — не сумісно
print(old_charger.charge())

# З адаптером
adapter = ChargerAdapter(new_phone)
print(adapter.charge())
