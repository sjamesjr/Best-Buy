class Product:
    """
    A class to represent a product in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        active (bool): Whether the product is active (available for purchase).

    Methods:
        get_quantity(): Returns the current quantity of the product.
        set_quantity(quantity): Updates the quantity and deactivates the product if quantity reaches zero.
        is_active(): Checks if the product is active.
        activate(): Activates the product.
        deactivate(): Deactivates the product.
        show(): Displays product details as a formatted string.
        buy(quantity): Purchases a specified quantity of the product, updating stock and returning total price.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial stock quantity of the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Products are active by default

    def get_quantity(self):
        """
        Getter for the quantity attribute.

        Returns:
            int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Setter for the quantity attribute. Updates the product quantity.
        If the quantity reaches zero, the product is deactivated.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False

    def show(self):
        """
        Displays product details as a formatted string.

        Returns:
            str: A string representation of the product.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int):
        """
        Buys a specified quantity of the product. Updates stock and calculates the total price.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            Exception: If the product is inactive or if there is insufficient stock.
        """
        # Check if the product is active
        if not self.active:
            raise Exception("Cannot buy inactive product.")

        # Check if there's enough quantity to fulfill the order
        if quantity > self.quantity:
            raise Exception("Insufficient quantity available.")

        # Calculate the total price
        total_price = self.price * quantity

        # Update the quantity after purchase
        self.quantity -= quantity

        # If quantity reaches 0, deactivate the product
        if self.quantity == 0:
            self.active = False

        return total_price



