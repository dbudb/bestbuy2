from promotions import Promotion


class Product:
    """Represents a product with name, price and quantity."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError("name can not be empty")
        self.name = name.strip()
        try:
            price = float(price)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Price must be a number.")
        if price >= 0:
            self.price = price
        else:
            raise ValueError("price can not be negative")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a whole number")
        self.promotion = None
        self.activate()
        self.set_quantity(quantity)

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError("quantity must be a whole number (integer).")

        else:
            quantity = int(quantity)

            if quantity < 0:
                raise ValueError("quantity must be >= 0")
            elif quantity == 0:
                self.quantity = 0
                self.deactivate()
            else:
                self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_promotion(self) -> Promotion | None:
        return self.promotion

    def set_promotion(self, promotion: Promotion | None) -> None:
        if promotion is not None and not isinstance(promotion, Promotion):
            raise TypeError("Promotion must be a Promotion instance or None")

        self.promotion = promotion

    def _promotion_description(self) -> str:
        if self.promotion is None:
            return ""

        return f", Promotion: {self.promotion.name}"

    def show(self):
        print(
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
            f"{self._promotion_description()}"
        )

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

        if quantity > self.get_quantity():
            raise ValueError("Not enough stock")

        total_price = self._calculate_price(quantity)
        self.set_quantity(self.get_quantity() - quantity)

        return total_price


class NonStockedProduct(Product):
    """Represents a product whose stock quantity is not tracked."""

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int) -> None:
        """Keep the quantity at zero because this product is not stocked."""
        self.quantity = 0

    def show(self) -> None:
        print(
            f"{self.name}, Price: {self.price}, Quantity: Unlimited"
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

    def show(self) -> None:
        print(
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
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
