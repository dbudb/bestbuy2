class Products:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError("name can not be empty")
        else:
            self.name = name.strip()

        try:
            price = float(price)
            if price > 0:
                self.price = price
            else:
                raise ValueError("price can not be negative")
        except Exception as e:
            raise ValueError(f"Price must be a number.")
        try:
            quantity = int(quantity)
            if quantity > 0:
                self.quantity = quantity
            else:
                raise ValueError("quantity must be > 0")
        except ValueError as e:
            raise ValueError("Quantity must be a number!")
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError("quantity must be a whole number (integer).")

        else:
            quantity = int(quantity)

            if quantity < 0:
                raise ValueError("quantity must be > 0")
            elif quantity == 0:
                self.deactivate()
                return False
            else:
                self.quantity = quantity
                return True

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        # missing the thing.. like can we buy more than in stock etc.
        actual_q = self.get_quantity()
        new_q = actual_q - quantity
        if new_q > 0:
            self.set_quantity(new_q)

        return quantity * self.price
