# Програма створює список зупинок для велосипедного маршруту по місту.
# У кожної зупинки є назва, опис і рейтинг популярності.

# Stop — клас для опису однієї зупинки (назва, опис, рейтинг популярності).
# CityBikeRoute — клас для збереження всіх зупинок і створення ітераторів для проходження.


class Stop:
    def __init__(self, name, description, popularity):
        self.name = name
        self.description = description
        self.popularity = popularity  # рейтинг популярності

    def __repr__(self):
        return f"{self.name} ({self.popularity}⭐): {self.description}"

class CityBikeRoute:
    def __init__(self):
        self.stops = [
            Stop("Майдан Незалежності", "Центральна площа міста", 5),
            Stop("Парк Шевченка", "Зелена зона для відпочинку", 4),
            Stop("Музей мистецтв", "Відомий художній музей", 3),
            Stop("Річковий порт", "Вид на річку та прогулянковий катер", 4),
            Stop("Старе місто", "Історичний центр з вузькими вуличками", 5),
        ]

    def get_sequential(self):
        # Ітератор у прямому порядку
        return iter(self.stops)

    def get_reverse(self):
        # Ітератор у зворотному порядку
        return iter(reversed(self.stops))

    def get_popular(self):
        # Ітератор за популярністю (від найбільш популярних)
        sorted_stops = sorted(self.stops, key=lambda s: s.popularity, reverse=True)
        return iter(sorted_stops)

# Використання
if __name__ == "__main__":
    route = CityBikeRoute()

    print("Маршрут у прямому порядку:")
    for stop in route.get_sequential():
        print(f" - {stop}")

    print("\nЗворотній маршрут:")
    for stop in route.get_reverse():
        print(f" - {stop}")

    print("\nПопулярні зупинки:")
    for stop in route.get_popular():
        print(f" - {stop}")