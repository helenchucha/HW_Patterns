# Ідея: Це програма, яка створює систему оповіщень для будинку.
# Ідея в тому, щоб мати один об’єкт цієї системи, який використовується
# скрізь у програмі — так званий сінглтон.

# Метаклас SingletonMeta, який зберігає всі вже створені екземпляри у словнику _instances.

# Метод __call__ контролює створення екземпляра класу. Якщо об'єкт ще не існує — створює
# і зберігає, інакше повертає вже існуючий.

# Клас CentralAlarmSystem тепер використовує цей метаклас, тому він автоматично стає сінглтоном.


# Створимо метаклас для сінглтона
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Створюємо екземпляр класу {cls.__name__}")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"Використовуємо вже існуючий екземпляр класу {cls.__name__}")
        return cls._instances[cls]

# Застосуємо метаклас до класу системи оповіщення
class CentralAlarmSystem(metaclass=SingletonMeta):
    def __init__(self):
        self.alerts = []

    def trigger_alert(self, location, alert_type):
        message = f"{location} - {alert_type}"
        self.alerts.append(message)
        print(f"[Оповіщення]: {message}")

# Функції для виклику системи з різних ситуацій
def report_fire(location):
    alarm = CentralAlarmSystem()
    alarm.trigger_alert(location, "Пожежа")

def report_intrusion(location):
    alarm = CentralAlarmSystem()
    alarm.trigger_alert(location, "Проникнення")

def report_sensor_failure(location):
    alarm = CentralAlarmSystem()
    alarm.trigger_alert(location, "Збій датчика")

# Виклики з різних частин будинку
report_fire("Кухня")
report_intrusion("Вітальня")
report_sensor_failure("Спальня")
report_fire("Гараж")
report_intrusion("Подвал")

# Перевірка, що об'єкт один
alarm1 = CentralAlarmSystem()
alarm2 = CentralAlarmSystem()

print(f"Використовуємо ту саму систему оповіщення: {alarm1 is alarm2}")
print("Всі оповіщення:", alarm1.alerts)