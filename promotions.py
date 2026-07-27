from abc import ABC, abstractmethod


class Promotion(ABC):
    """Defines the interface shared by all product promotions."""

    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Promotion name cannot be empty")

        self.name = name.strip()

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Return the total price after applying this promotion."""


class PercentDiscount(Promotion):
    """Applies a percentage discount to every purchased item."""

    def __init__(self, name: str, percent: float) -> None:
        super().__init__(name)

        try:
            percent = float(percent)
        except (TypeError, ValueError):
            raise ValueError("Percent must be a number")

        if not 0 <= percent <= 100:
            raise ValueError("Percent must be between 0 and 100")

        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        discount_factor = 1 - self.percent / 100
        return product.price * quantity * discount_factor


class SecondHalfPrice(Promotion):
    """Charges half price for every second item."""

    def apply_promotion(self, product, quantity: int) -> float:
        pairs = quantity // 2
        remaining_items = quantity % 2
        return product.price * (pairs * 1.5 + remaining_items)


class ThirdOneFree(Promotion):
    """Makes every third item free."""

    def apply_promotion(self, product, quantity: int) -> float:
        payable_items = quantity - quantity // 3
        return product.price * payable_items
