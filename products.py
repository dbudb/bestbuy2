class Products:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError('name can not be empty')
        else: self.name = name

        if price > 0 and isinstance(price, float):
            self.price = float(price)
        else:
            raise ValueError('price can not be negative')
        if quantity > 0 and isinstance(quantity, int):
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


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:

        actual_q = get_quantity()
        new_q = actual_q - quantity
        if new_q > 0:
            set_quantity(new_q)

        return quantity * self.price