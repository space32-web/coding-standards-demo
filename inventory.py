"""Учёт товаров на складе."""
from dataclasses import dataclass

LOW_STOCK_LIMIT = 5


@dataclass
class Product:
    """Товар на складе."""

    name: str
    price: float
    quantity: int

    @property
    def total_value(self):
        """Стоимость всех единиц товара."""
        return self.price * self.quantity


def low_stock(products, limit=LOW_STOCK_LIMIT):
    """Возвращает товары, которых осталось меньше limit штук."""
    return [item for item in products if item.quantity < limit]


def inventory_value(products):
    """Общая стоимость склада."""
    return sum(item.total_value for item in products)


if __name__ == "__main__":
    stock = [
        Product("Ручка", 25.0, 120),
        Product("Тетрадь", 60.0, 3),
        Product("Маркер", 90.0, 4),
    ]
    print(f"Стоимость склада: {inventory_value(stock):.2f}")
    for item in low_stock(stock):
        print(f"Заканчивается: {item.name} ({item.quantity} шт.)")
