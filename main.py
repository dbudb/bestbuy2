"""Command-line interface for the Best Buy store."""

import products
import promotions
import store


def list_products(store_obj):
    """Display all active products in the store."""
    print("------")

    for index, product in enumerate(
        store_obj.get_all_products(),
        start=1,
    ):
        print(f"{index}. ", end="")
        product.show()

    print("------")


def show_total(store_obj):
    """Display the total number of items in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_order(store_obj):
    """Ask the user for products and submit an order."""
    shopping_list = []

    while True:
        list_products(store_obj)
        print("When you want to finish the order, enter empty text.")

        product_choice = input("Which product # do you want? ")

        if not product_choice:
            break

        quantity_input = input("What amount do you want? ")

        if not quantity_input:
            break

        try:
            product_number = int(product_choice)
            quantity = int(quantity_input)

            if product_number < 1:
                raise ValueError

            available_products = store_obj.get_all_products()
            product = available_products[product_number - 1]

            shopping_list.append((product, quantity))
            print("Product added to list!")

        except (ValueError, IndexError):
            print("Invalid input")

    if not shopping_list:
        return

    try:
        total = store_obj.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total}")
    except ValueError as error:
        print(error)


def start(store_obj):
    """Run the interactive store menu."""
    actions = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
    }

    while True:
        print(
            "\nStore Menu\n"
            "----------\n"
            "1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit"
        )

        choice = input("Please choose a number: ")

        if choice == "4":
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice")
        else:
            action(store_obj)


def main():
    """Create the default store and start the interface."""
    product_list = [
        products.Product("MacBook Air M2", 1450, 100),
        products.Product(
            "Bose QuietComfort Earbuds",
            250,
            500,
        ),
        products.Product("Google Pixel 7", 500, 250),
        products.NonStockedProduct("Windows License", 125),
        products.LimitedProduct("Shipping", 10, 250, 1),
    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
