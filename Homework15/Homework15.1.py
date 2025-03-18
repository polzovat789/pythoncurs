from enum import Enum

# Enum для статусов заказа
class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"

# Класс заказа
class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
        else:
            print("Ошибка: неверный статус")

    def display_status(self):
        print(f"Статус заказа {self.order_id}: {self.status.value}")

# Пример использования
order = Order(order_id=123)
order.display_status()  # Выведет статус "Заказ ожидает обработки"

order.update_status(OrderStatus.IN_PROGRESS)
order.display_status()  # Выведет статус "Заказ готовится"

order.update_status(OrderStatus.COMPLETED)
order.display_status()  # Выведет статус "Заказ выдан"
