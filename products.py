from promotions import Promotion


class Product:
    """Represents a product with name, price and quantity."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError("name can not be empty")
        self.name = name.strip()

        self.price = price
        self.promotion = None
        self.activate()
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number")

        if price < 0:
            raise ValueError("price can not be negative")

        self._price = price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("quantity must be a whole number (integer)")
        if quantity < 0:
            raise ValueError("quantity must be >= 0")

        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    @property
    def promotion(self) -> Promotion | None:
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion | None) -> None:
        if promotion is not None and not isinstance(promotion, Promotion):
            raise TypeError("Promotion must be a Promotion instance or None")

        self._promotion = promotion

    def _promotion_description(self) -> str:
        if self.promotion is None:
            return ""

        return f", Promotion: {self.promotion.name}"

    def __str__(self) -> str:
        return (
            f"{self.name}, Price: ${self.price:g} Quantity:{self.quantity}"
            f"{self._promotion_description()}"
        )

    def __lt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.price < other.price

    def __gt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.price > other.price

    def _validate_purchase_quantity(self, quantity: int) -> None:
        """Validate a requested purchase quantity."""
        if not self.is_active():
            raise ValueError("Product is not active")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a whole number")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

    def _calculate_price(self, quantity: int) -> float:
        """Return the regular or promotional total for a quantity."""
        if self.promotion is None:
            return quantity * self.price

        return self.promotion.apply_promotion(self, quantity)

    def buy(self, quantity: int) -> float:
        """Buy a quantity of this product and return total price."""
        self._validate_purchase_quantity(quantity)

        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        total_price = self._calculate_price(quantity)
        self.quantity -= quantity

        return total_price


class NonStockedProduct(Product):
    """Represents a product whose stock quantity is not tracked."""

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, 0)

    @Product.quantity.setter
    def quantity(self, quantity: int) -> None:
        """Keep the quantity at zero because this product is not stocked."""
        self._quantity = 0

    def __str__(self) -> str:
        return (
            f"{self.name}, Price: ${self.price:g} Quantity:Unlimited"
            f"{self._promotion_description()}"
        )

    def buy(self, quantity: int) -> float:
        """Buy this product without changing its quantity."""
        self._validate_purchase_quantity(quantity)
        return self._calculate_price(quantity)


class LimitedProduct(Product):
    """Represents a product with a per-order purchase limit."""

    def __init__(
            self,
            name: str,
            price: float,
            quantity: int,
            maximum: int,
    ) -> None:
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum must be a positive whole number")

        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self) -> str:
        return (
            f"{self.name}, Price: ${self.price:g} Quantity:{self.quantity}, "
            f"Limited to {self.maximum} per order"
            f"{self._promotion_description()}"
        )

    def buy(self, quantity: int) -> float:
        """Buy no more than the allowed quantity per order."""
        self._validate_purchase_quantity(quantity)

        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} per order"
            )

        return super().buy(quantity)
