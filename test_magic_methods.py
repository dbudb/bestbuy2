import pytest

from products import LimitedProduct, Product
from store import Store


def test_price_property_rejects_negative_values():
    product = Product("MacBook Air M2", 1450, 100)

    with pytest.raises(ValueError):
        product.price = -100

    assert product.price == 1450


def test_product_string_representation():
    product = Product("MacBook Air M2", 1450, 100)

    assert str(product) == "MacBook Air M2, Price: $1450 Quantity:100"


def test_products_can_be_compared_by_price():
    mac = Product("MacBook Air M2", 1450, 100)
    bose = Product("Bose QuietComfort Earbuds", 250, 500)

    assert mac > bose
    assert bose < mac


def test_store_membership():
    mac = Product("MacBook Air M2", 1450, 100)
    bose = Product("Bose QuietComfort Earbuds", 250, 500)
    pixel = LimitedProduct("Google Pixel 7", 500, 250, maximum=1)
    best_buy = Store([mac, bose])

    assert mac in best_buy
    assert pixel not in best_buy


def test_stores_can_be_combined():
    mac = Product("MacBook Air M2", 1450, 100)
    bose = Product("Bose QuietComfort Earbuds", 250, 500)
    first_store = Store([mac])
    second_store = Store([bose])

    combined_store = first_store + second_store

    assert isinstance(combined_store, Store)
    assert combined_store.products == [mac, bose]
    assert first_store.products == [mac]
    assert second_store.products == [bose]
