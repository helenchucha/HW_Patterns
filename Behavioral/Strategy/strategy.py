# Цей код дозволяє сортувати список даних різними способами
# - за зростанням
# - за спаданням
# - за довжиною елементів

from abc import ABC, abstractmethod

# Абстрактна стратегія сортування
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Сортування за зростанням
class AscendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data)

# Сортування за спаданням
class DescendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)

# Сортування за довжиною (для списків рядків)
class LengthSort(SortStrategy):
    def sort(self, data):
        return sorted(data, key=len)

# Контекст — список для сортування з обраною стратегією
class SortedList:
    def __init__(self, data, strategy: SortStrategy):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def get_sorted(self):
        return self.strategy.sort(self.data)

# Використання
if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5]
    words = ["яблуко", "банан", "ківі", "авокадо"]
    print(numbers)
    print(words)

    # Стратегія зростання
    sort_strategy = AscendingSort()
    sorted_numbers = SortedList(numbers, sort_strategy)
    print("За зростанням:", sorted_numbers.get_sorted())

    # Стратегія спадання
    sorted_numbers.set_strategy(DescendingSort())
    print("За спаданням:", sorted_numbers.get_sorted())

    # Стратегія за довжиною
    sorted_words = SortedList(words, LengthSort())
    print("За довжиною слова за зростанням:", sorted_words.get_sorted())