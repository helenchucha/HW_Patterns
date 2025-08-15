# Це програма, яка імітує систему підтримки користувачів.
# Вона має кілька рівнів обробки запитів:

# - Технічна підтримка — вирішує проблеми з технікою, наприклад, з інтернетом.
# - Обробка питань з рахунками — допомагає з оплатою або рахунками.
# - Менеджер — розглядає будь-які інші запити, які не були вирішені на попередніх рівнях.

# Запит проходить по ланцюгу, поки хтось його не вирішить або не дійде до кінця.


from abc import ABC, abstractmethod

# Абстрактний клас обробника
class SupportHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, issue):
        pass

# Обробник для технічних питань
class TechnicalSupport(SupportHandler):
    def handle(self, issue):
        if issue['category'] == 'technical':
            print(f"Технічна підтримка вирішує проблему: {issue['description']}")
        elif self.successor:
            self.successor.handle(issue)
        else:
            print("Проблему не вдалося обробити.")

# Обробник для питань, пов'язаних з рахунками
class BillingSupport(SupportHandler):
    def handle(self, issue):
        if issue['category'] == 'billing':
            print(f"Відділ обліку вирішує проблему: {issue['description']}")
        elif self.successor:
            self.successor.handle(issue)
        else:
            print("Проблему не вдалося обробити.")

# Обробник для загальних питань або для ескалації
class ManagerSupport(SupportHandler):
    def handle(self, issue):
        print(f"Менеджер розглядає проблему: {issue['description']}")

# Створюємо ланцюг обробників
tech_support = TechnicalSupport()
billing_support = BillingSupport()
manager = ManagerSupport()

tech_support.successor = billing_support
billing_support.successor = manager

# Демонстрація роботи
issues = [
    {'category': 'technical', 'description': 'Не працює інтернет'},
    {'category': 'billing', 'description': 'Проблема з оплатою рахунка'},
    {'category': 'general', 'description': 'Запит щодо оновлення підписки'}
]

for issue in issues:
    print(f"\nОбробка запиту: {issue}")
    tech_support.handle(issue)