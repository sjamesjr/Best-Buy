import products
from store import Store


def start(store_class):
    """
    Main function to run the store menu.

    Args:
        store_class (class): The Store class, used to manage the store's products and operations.

    This function presents a menu to the user, allowing them to:
    1. List all products in the store.
    2. Show the total amount of products in the store.
    3. Make an order by selecting products and quantities.
    4. Quit the program.
    """
    while True:
        # Display the store menu options
        print("Store Menu")
        print("__________")
        print("1. List all products in store \n"
              "2. Show total amount in store \n"
              "3. Make order \n"
              "4. Quit")

        try:
            menu_input = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        # Setup initial stock of inventory
        product_list = [
            products.Product("MacBook Air M2", 1450, 100),
            products.Product("Bose QuietComfort Earbuds", 250, 500),
            products.Product("Google Pixel 7", 500, 250)
        ]

        # Create an instance of the store with the initial products
        best_buy = store_class(product_list)

        # Handle menu options
        if menu_input == 1:
            # List all products in the store
            for product in best_buy.get_all_products():
                print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

        elif menu_input == 2:
            # Display the total quantity of all products
            print("Total quantity in store:", best_buy.get_total_quantity())

        elif menu_input == 3:
            # Handle making an order
            shopping_list = []
            print("______")
            # Display products with their details
            for idx, product in enumerate(best_buy.get_all_products(), start=1):
                print(f"{idx}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print("______\n")

            # Allow the user to create a shopping list
            while True:
                print("When you want to finish your order, press 'Enter'")
                product_input = input("Which product would you like?: ")
                if not product_input:
                    break  # Exit the loop if user presses Enter

                try:
                    product_ordered = int(product_input)
                    # Validate product number
                    if product_ordered < 1 or product_ordered > len(best_buy.get_all_products()):
                        print("Invalid product number. Please try again.")
                        continue

                    order_quantity = int(input("What amount would you like?: "))
                    # Validate order quantity
                    if order_quantity <= 0:
                        print("Quantity must be greater than zero. Please try again.")
                        continue

                    # Add the chosen product and quantity to the shopping list
                    chosen_product = best_buy.get_all_products()[product_ordered - 1]
                    shopping_list.append((chosen_product, order_quantity))
                except ValueError:
                    print("Invalid input! Please enter a valid product number and quantity.")
                    continue

            # Process the order and display the total cost
            print("Your total is: $", best_buy.order(shopping_list))

        elif menu_input == 4:
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid menu input
            print("Invalid option. Please choose a number between 1 and 4.")

        # Wait for the user to press Enter before displaying the menu again
        input("\nPress 'Enter' to continue...")


# Run the program
start(Store)
