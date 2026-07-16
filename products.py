class Products:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError('name can not be empty')
        else: self.name = name

        if price > 0:
            self.price = float(price)
        else:
            raise ValueError('price can not be negative')
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('quantity must be > 0')
        self.active = True

    def get_quantity(self) -> int:
            return self.quantity


    def set_quantity(self, quantity: int):
        if quantity > 0 and isinstance(quantity, int):
            self.quantity = quantity
            return True
        else:
            raise ValueError('quantity must be > 0')
    # missing auto deactivate

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