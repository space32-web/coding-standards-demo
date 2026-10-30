"""Тесты модуля inventory."""
from inventory import Product, inventory_value, low_stock


def test_inventory_value():
    stock = [Product("A", 10.0, 2), Product("B", 5.0, 4)]
    assert inventory_value(stock) == 40.0


def test_low_stock():
    stock = [Product("A", 10.0, 2), Product("B", 5.0, 40)]
    assert [item.name for item in low_stock(stock)] == ["A"]
