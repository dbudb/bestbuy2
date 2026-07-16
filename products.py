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

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy a quantity of this product and return total price."""
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a whole number")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.get_quantity():
            raise ValueError("Not enough stock")

        self.set_quantity(self.get_quantity() - quantity)

        return quantity * self.price
