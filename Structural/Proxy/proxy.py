# Програма демонструє, як через проксі можна контролювати доступ до важливих дій залежно від прав користувача.

# В програмі створюється документ, який можна переглядати і редагувати.
# Є два користувачі: один — звичайний гість, інший — адміністратор.
# Для кожного користувача створюється спеціальний "захисний" посередник — проксі.
# Цей проксі контролює, що користувач може робити:
# - Гість може тільки дивитись документ.
# - Адміністратор може і дивитись, і редагувати документ.
# Коли користувач намагається щось зробити, проксі перевіряє його роль і вирішує, дозволити або заборонити цю дію.

# SecurityProxy контролює доступ до RealDocument залежно від ролі користувача.

# Гість (guest) може переглядати документ, але не має права редагувати.

# Адміністратор (admin) може і переглядати, і редагувати.


from abc import ABC, abstractmethod

# Інтерфейс документу
class Document(ABC):
    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def edit(self):
        pass

# Реальний документ
class RealDocument(Document):
    def view(self):
        print("Перегляд документа...")

    def edit(self):
        print("Редагування документа...")

# Структура користувача з роллю
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # Наприклад, 'admin' або 'guest'

# Проксі, що регулює доступ
class SecurityProxy(Document):
    def __init__(self, real_document, user):
        self._real_document = real_document
        self._user = user

    def view(self):
        # будь-хто може переглядати
        self._real_document.view()

    def edit(self):
        # тільки адміністратор може редагувати
        if self._user.role == 'admin':
            self._real_document.edit()
        else:
            print(f"Доступ заборонено! {self._user.name} не має прав редагування.")

# Демонстрація
if __name__ == "__main__":
    user1 = User("Олексій", "guest")
    user2 = User("Олена", "admin")

    document = RealDocument()

    proxy_for_guest = SecurityProxy(document, user1)
    proxy_for_admin = SecurityProxy(document, user2)

    print("Гість спробує переглянути і редагувати:")
    proxy_for_guest.view()
    proxy_for_guest.edit()

    print("\nАдміністратор спробує переглянути і редагувати:")
    proxy_for_admin.view()
    proxy_for_admin.edit()