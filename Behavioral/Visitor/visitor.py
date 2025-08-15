from abc import ABC, abstractmethod

# Абстрактний клас - Поліс
class InsurancePolicy(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Конкретні класи полісів
class AutoInsurance(InsurancePolicy):
    def __init__(self, policy_number, driver_age, premium):
        self.policy_number = policy_number
        self.driver_age = driver_age
        self.premium = premium

    def accept(self, visitor):
        visitor.visit_auto_insurance(self)

class HomeInsurance(InsurancePolicy):
    def __init__(self, policy_number, property_value, premium):
        self.policy_number = policy_number
        self.property_value = property_value
        self.premium = premium

    def accept(self, visitor):
        visitor.visit_home_insurance(self)

class HealthInsurance(InsurancePolicy):
    def __init__(self, policy_number, age, premium):
        self.policy_number = policy_number
        self.age = age
        self.premium = premium

    def accept(self, visitor):
        visitor.visit_health_insurance(self)

# Відвідувач - базовий клас
class InsuranceVisitor(ABC):
    @abstractmethod
    def visit_auto_insurance(self, policy):
        pass

    @abstractmethod
    def visit_home_insurance(self, policy):
        pass

    @abstractmethod
    def visit_health_insurance(self, policy):
        pass

# Реалізація відвідувача для підрахунку загальної суми страхових внесків
class PremiumSumVisitor(InsuranceVisitor):
    def __init__(self):
        self.total_premium = 0

    def visit_auto_insurance(self, policy):
        self.total_premium += policy.premium

    def visit_home_insurance(self, policy):
        self.total_premium += policy.premium

    def visit_health_insurance(self, policy):
        self.total_premium += policy.premium

# Реалізація відвідувача для друку деталей
class PolicyDetailsPrinter(InsuranceVisitor):
    def visit_auto_insurance(self, policy):
        print(f"Автостраховка: №{policy.policy_number}, Водій віком {policy.driver_age}, Внесок {policy.premium} грн.")

    def visit_home_insurance(self, policy):
        print(f"Житловий поліс: №{policy.policy_number}, Вартість майна {policy.property_value} грн, Внесок {policy.premium} грн.")

    def visit_health_insurance(self, policy):
        print(f"Медичне страхування: №{policy.policy_number}, Вік {policy.age}, Внесок {policy.premium} грн.")

# Використання
if __name__ == "__main__":
    policies = [
        AutoInsurance("A123", 30, 5000),
        HomeInsurance("H456", 250000, 3000),
        HealthInsurance("H789", 45, 2000),
        AutoInsurance("A456", 22, 4800),
    ]

    # Підрахунок суми внесків
    sum_visitor = PremiumSumVisitor()
    for policy in policies:
        policy.accept(sum_visitor)
    print(f"Загальна сума страхових внесків: {sum_visitor.total_premium} грн.\n")

    # Друк деталей
    printer = PolicyDetailsPrinter()
    for policy in policies:
        policy.accept(printer)