# Ця програма імітує простий текстовий редактор, який дозволяє писати текст і
# зберігати його стан на різних етапах.
# Потім, якщо потрібно, можна повернутися назад до попереднього стан, тобто скасувати деякі зміни.

# Текстовий редактор
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        # Створюємо мему (знімок стану)
        return Memento(self._content)

    def restore(self, memento):
        # Відновлюємо стан з мему
        self._content = memento.get_content()

# Мему (Memento)
class Memento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content

# Зберігач історії
class History:
    def __init__(self):
        self._mementos = []

    def save_state(self, memento):
        self._mementos.append(memento)

    # добавить просмотр истории состояний
    # переключение между ними

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None

# Демонстрація роботи
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    # Написати перший рядок
    editor.write("Привіт, світ!\n")
    print("Поточний текст:\n" + editor.get_content())

    # Зберегти стан
    history.save_state(editor.save())

    # Додати ще один рядок
    editor.write("Як у тебе справи?\n")
    print("Додано ще один рядок:\n" + editor.get_content())

    # Зберегти стан
    history.save_state(editor.save())

    # Додати ще один рядок
    editor.write("Все добре!\n")
    print("Ще один рядок:\n" + editor.get_content())

    # Відкотитися до попереднього стану
    print("\nВідкат до попереднього стану...")
    previous_state = history.undo()
    if previous_state:
        editor.restore(previous_state)
        print("Після відкату:\n" + editor.get_content())
    else:
        print("Немає збережених станів.")