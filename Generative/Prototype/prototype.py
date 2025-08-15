'''
Прототип — це патерн проектування, що дозволяє копіювати об'єкти,
не вдаючись у подробиці їх реалізації.

Приклад: Друк різної кількості фото в фотокабіні.
'''

import copy

# Базовий клас фотозображення
class Photo:
    def __init__(self, color=True, size=(4, 6), quantity=1):
        self.color = color  # Колірність фото
        self.size = size          # Розмір фото (ширина, висота) у дюймах
        self.quantity = quantity  # Кількість копій

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        color_mode = "Color" if self.color else "Black & White"
        return (f"{self.quantity}x, {color_mode} photo, "
                f"Size: {self.size[0]}x{self.size[1]} inches")

# Приклад роботи фотокабіни
if __name__ == "__main__":
    # Створюємо оригінальне фото
    original_photo = Photo(color=True, size=(4, 6), quantity=1)
    print("Оригінальне фото:", original_photo)

    # Створюємо копії з різними налаштуваннями
    # Чорно-біле, розмір 5х7, копій 10
    bw_photo = original_photo.clone()
    bw_photo.color = False
    bw_photo.size = (5, 7)
    bw_photo.quantity = 10

    # Колірне фото, розмір 3х5, копій 5
    color_photo = original_photo.clone()
    color_photo.size = (3, 5)
    color_photo.quantity = 2

    # Вивід інформації про копії
    print("Чорно-білі копії:", bw_photo)
    print("Колірні копії:", color_photo)