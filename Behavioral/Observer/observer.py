# Цей код реалізує імітацію розсилки новин.
# Вона дозволяє багатьом користувачам отримувати повідомлення, коли з'являється новина.


# Базовий клас "Спостерігач"
class User:
    def update(self, news):
        pass

# Конкретний користувач
class Subscriber(User):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} отримав новину: {news}")

# Клас "Новинна стрічка" або "Розсилка" (Subject)
class NewsFeed:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def unsubscribe(self, user):
        self.subscribers.remove(user)

    def publish_news(self, news):
        print(f"\nНова новина: {news}")
        for user in self.subscribers:
            user.update(news)

# Використання
if __name__ == "__main__":
    # Створюємо новинну стрічку
    news_feed = NewsFeed()

    # Створюємо користувачів
    user1 = Subscriber("Користувач А")
    user2 = Subscriber("Користувач Б")
    user3 = Subscriber("Користувач В")

    # Підписуємо користувачів на стрічку
    news_feed.subscribe(user1)
    news_feed.subscribe(user2)
    news_feed.subscribe(user3)

    # Публікуємо новину
    news_feed.publish_news("Новий смартфон вже доступний!")

    # Відписуємо одного користувача
    news_feed.unsubscribe(user2)

    # Ще одна новина
    news_feed.publish_news("Знижки до кінця місяця!")