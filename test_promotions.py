import pytest

from products import NonStockedProduct, Product
from promotions import (
    PercentDiscount,
    Promotion,
    SecondHalfPrice,
    ThirdOneFree,
)


def test_promotion_is_abstract():
    with pytest.raises(TypeError):
        Promotion("General promotion")


def test_percent_discount():
    product = Product("Laptop", 100, 10)
    product.promotion = PercentDiscount("30% off", 30)

    assert product.buy(2) == pytest.approx(140)
    assert product.quantity == 8


def test_second_item_at_half_price():
    product = Product("Laptop", 100, 10)
    product.promotion = SecondHalfPrice("Second half price")

    assert product.buy(3) == pytest.approx(250)
    assert product.quantity == 7


def test_third_item_free():
    product = Product("Earbuds", 100, 10)
    product.promotion = ThirdOneFree("Third one free")

    assert product.buy(7) == pytest.approx(500)
    assert product.quantity == 3


def test_promotion_can_be_removed():
    product = Product("Laptop", 100, 10)
    product.promotion = PercentDiscount("30% off", 30)

    product.promotion = None

    assert product.promotion is None
    assert product.buy(2) == pytest.approx(200)


def test_same_promotion_can_be_shared_by_products():
    promotion = PercentDiscount("30% off", 30)
    first_product = Product("Laptop", 100, 10)
    second_product = Product("Phone", 200, 10)

    first_product.promotion = promotion
    second_product.promotion = promotion

    assert first_product.promotion is promotion
    assert second_product.promotion is promotion
    assert first_product.buy(1) == pytest.approx(70)
    assert second_product.buy(1) == pytest.approx(140)


def test_non_stocked_product_supports_promotions():
    product = NonStockedProduct("Windows License", 125)
    product.promotion = PercentDiscount("30% off", 30)

    assert product.buy(2) == pytest.approx(175)
    assert product.quantity == 0


def test_show_displays_current_promotion(capsys):
    product = Product("Laptop", 100, 10)
    product.promotion = SecondHalfPrice("Second half price")

    print(product)

    assert "Promotion: Second half price" in capsys.readouterr().out
