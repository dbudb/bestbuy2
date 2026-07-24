from typing import List
from products import Product


class Store:
    """Represents a store that manages products."""

    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product):
        """Adds a product to store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total = 0

        for product, quantity in shopping_list:
            total += product.buy(quantity)

        return total
