'''
Фасад — це структурний шаблон проектування,
який надає простий інтерфейс до складної системи класів,
бібліотеки чи фреймворка.

Приклад: Система управления домашним кинотеатром
'''

class Television:
    def turn_on(self):
        print("Телевізор увімкнено.")
    def turn_off(self):
        print("Телевізор вимкнено.")

class AudioSystem:
    def turn_on(self):
        print("Аудіосистема увімкнена.")
    def turn_off(self):
        print("Аудіосистема вимкнена.")
    def set_volume(self, level):
        print(f"Гучність встановлено на {level}.")

class Light:
    def turn_on(self):
        print("Світло увімкнено.")
    def turn_off(self):
        print("Світло вимкнено.")

# Фасад, що спрощує керування всіма пристроями
class HomeTheaterFacade:
    def __init__(self, tv, audio, ac):
        self.tv = tv
        self.audio = audio
        self.lt = lt

    def start_movie_night(self):
        print("Починаємо вечір кіно...")
        self.tv.turn_on()
        self.audio.turn_on()
        self.audio.set_volume(20)
        self.lt.turn_off()

    def end_movie_night(self):
        print("Завершуємо вечір кіно...")
        self.tv.turn_off()
        self.audio.turn_off()
        self.lt.turn_on()

# Використання
tv = Television()
audio = AudioSystem()
lt = Light()

home_theater = HomeTheaterFacade(tv, audio, lt)

# Запуск сценарію
home_theater.start_movie_night()
print("---")
home_theater.end_movie_night()