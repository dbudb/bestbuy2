import pytest

from products import Product


def test_create_normal_product():
    product = Product("Laptop", 999.99, 10)

    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.quantity == 10
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", 100, 10)

    with pytest.raises(ValueError):
        Product("Laptop", -1, 10)


def test_product_becomes_inactive_at_zero_quantity():
    product = Product("Laptop", 999.99, 10)

    product.quantity = 0

    assert product.quantity == 0
    assert not product.is_active()


def test_buy_modifies_quantity_and_returns_total():
    product = Product("Laptop", 100, 10)

    total = product.buy(3)

    assert total == 300
    assert product.quantity == 7


def test_buy_more_than_available_raises_exception():
    product = Product("Laptop", 100, 2)

    with pytest.raises(ValueError):
        product.buy(3)

    assert product.quantity == 2
