from products import Product


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
        Processes a shopping list and returns the total cost of the order.

        Args:
            shopping_list (list): A list of tuples where each tuple contains:
                                  - Product (Product): The product to purchase.
                                  - quantity (int): The quantity to purchase.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If the quantity needed exceeds the available stock of a product.
        """
        total_cost = 0.0
        for product, quantity_needed in shopping_list:
            # Check if the product is in the store and has sufficient quantity
            if product in self.product_list and product.quantity >= quantity_needed:
                # Reduce the quantity of the product
                product.quantity -= quantity_needed
                # Add the cost of the product to the total cost
                total_cost += product.price * quantity_needed
            else:
                # Raise an exception if there's insufficient quantity
                raise ValueError(f"Insufficient quantity for product: {product.name}")
        return total_cost
