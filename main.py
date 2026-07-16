def start(store_obj):

    def list_products():
        print("------")
        for index, product in enumerate(store_obj.get_all_products(), start=1):
            print(f"{index}. ", end="")
            product.show()
        print("------")

    def show_total():
        print(f"Total of {store_obj.get_total_quantity()} items in store")

    def make_order():
        shopping_list = []

        while True:
            list_products()

            print("When you want to finish order, enter empty text.")

            product_choice = input("Which product # do you want? ")

            if product_choice == "":
                break

            quantity = input("What amount do you want? ")

            if quantity == "":
                break

            try:
                product = store_obj.get_all_products()[int(product_choice) - 1]
                quantity = int(quantity)

                shopping_list.append((product, quantity))
                print("Product added to list!")

            except (ValueError, IndexError):
                print("Invalid input")

        if shopping_list:
            try:
                total = store_obj.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total}")
            except ValueError as e:
                print(e)

    actions = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
    }

    while True:
        print(
            "\n   Store Menu\n"
            "   ----------\n"
            "1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit"
        )

        choice = input("Please choose a number: ")

        if choice == "4":
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice")
