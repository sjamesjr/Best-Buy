from products import Product, NonStockedProduct, LimitedProduct


class Store:
    """
    A class to represent a store containing a list of products.

    Attributes:
        product_list (list): A list of Product objects representing the inventory of the store.

    Methods:
        add_product(product): Adds a product to the store's inventory.
        remove_product(product): Removes a product from the store's inventory.
        get_total_quantity(): Returns the total quantity of all items in the store.
        get_all_products(): Returns all active products in the store.
        order(shopping_list): Processes a shopping list and returns the total cost of the order.
    """

    def __init__(self, product_list):
        """
        Initializes the Store with a list of products.

        Args:
            product_list (list): A list of Product objects to populate the store's inventory.
        """
        self.product_list = []
        for product in product_list:
            self.product_list.append(product)

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add to the store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        Args:
            product (Product): The product to remove from the store.
        """
        self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Calculates the total quantity of all items in the store.

        Returns:
            int: The total quantity of all items in the store.
        """
        return sum(product.quantity for product in self.product_list)

    def get_all_products(self):
        """
        Retrieves all active products in the store.

        Returns:
            list: A list of Product objects that are active.
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        """
        Processes a shopping list and returns the total cost of the order,
        with options to retry or adjust the order in case of errors.

        Args:
            shopping_list (list): A list of tuples where each tuple contains:
                                  - Product (Product): The product to purchase.
                                  - quantity (int): The quantity to purchase.

        Returns:
            float: The total cost of the order.
        """
        total_cost = 0.0
        idx = 0  # Index to track current product in shopping list

        while idx < len(shopping_list):
            product, quantity_needed = shopping_list[idx]

            try:
                # Process NonStockedProduct
                if isinstance(product, NonStockedProduct):
                    total_cost += product.price * quantity_needed
                    idx += 1  # Move to next product
                    continue

                # Process LimitedProduct
                elif isinstance(product, LimitedProduct):
                    if quantity_needed > product.maximum:
                        raise Exception(f"{product.name} is limited to {product.maximum} per order.")
                    if quantity_needed > product.quantity:
                        raise Exception(f"Insufficient stock for {product.name}. Available: {product.quantity}")
                    total_cost += product.buy(quantity_needed)
                    idx += 1  # Move to next product
                    continue

                # Process regular Product
                elif isinstance(product, Product):
                    if quantity_needed > product.quantity:
                        raise Exception(f"Insufficient stock for {product.name}. Available: {product.quantity}")
                    total_cost += product.buy(quantity_needed)
                    idx += 1  # Move to next product
                    continue

                else:
                    raise Exception(f"Unknown product type: {product.__class__.__name__}")

            except Exception as e:
                print(f"Error processing product {product.name}: {e}")

                # Provide retry or skip options
                print("Options:")
                print("1. Retry with a different quantity")
                print("2. Skip this product")
                user_choice = input("Choose an option (1/2): ")

                if user_choice == "1":
                    try:
                        # Get new quantity from user
                        new_quantity = input(f"Enter a new quantity for {product.name}: ").strip()
                        if not new_quantity.isdigit() or int(new_quantity) <= 0:
                            print("Invalid quantity. Skipping product.")
                            idx += 1  # Move to next product
                            continue

                        # Update shopping list and retry
                        shopping_list[idx] = (product, int(new_quantity))
                        continue  # Retry with updated quantity

                    except ValueError:
                        print("Invalid input. Skipping product.")
                        idx += 1  # Move to next product
                        continue

                elif user_choice == "2":
                    print(f"Skipping {product.name}.")
                    idx += 1  # Move to next product
                    continue

                else:
                    print("Invalid choice. Skipping product.")
                    idx += 1  # Move to next product
                    continue

        return total_cost
