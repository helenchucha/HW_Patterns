# Це програма, яка імітує процес покупки товару.

# - Покупець — робить замовлення на смартфон.
# - Продавець отримує замовлення і передає його постачальнику.
# - Постачальник обробляє замовлення і доставляє його покупцю.
#
# Уся ця послідовність реалізована через команду "PlaceOrder", яка автоматично виконує всі кроки.
#
# Програма показує, як дані рухаються між цими учасниками і як замовлення проходить через усі етапи.

from abc import ABC, abstractmethod

# Абстрактна команда
class Order(ABC):
    @abstractmethod
    def process(self):
        pass

# Покупець — ініціатор
class Customer:
    def __init__(self):
        self.order_details = ""

    def make_order(self, item):
        self.order_details = item
        print(f"Покупець зробив замовлення на: {self.order_details}")

    def place_order(self, seller):
        seller.receive_order(self.order_details)

# Продавець — виконавець
class Seller:
    def __init__(self):
        self.order_received = ""

    def receive_order(self, order_details):
        self.order_received = order_details
        print(f"Продавець отримав замовлення: {self.order_received}")
        self.forward_to_supplier()

    def forward_to_supplier(self):
        supplier = Supplier()
        supplier.fulfill_order(self.order_received)

# Постачальник — отримувач
class Supplier:
    def fulfill_order(self, order_details):
        print(f"Постачальник обробляє замовлення: {order_details}")
        print(f"Замовлення '{order_details}' доставлено покупцю!")

# Конкретна команда — оформлення замовлення
class PlaceOrder(Order):
    def __init__(self, customer, seller, item):
        self.customer = customer
        self.seller = seller
        self.item = item

    def process(self):
        self.customer.make_order(self.item)
        self.customer.place_order(self.seller)

# Демонстрація роботи
if __name__ == "__main__":
    customer = Customer()
    seller = Seller()

    order = PlaceOrder(customer, seller, "смартфон")
    order.process()