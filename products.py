class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Getter function for quantity.
           Returns the quantity (float)."""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """Getter function for active.
            Returns True if the product is active, otherwise False."""
        if not self.active:
            return False

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        self.active = False

    def show(self):
        """Returns a string that represents the product, for example:
            "MacBook Air M2, Price: 1450, Quantity: 100"""
        print(self.name, "Price:", self.price, "Quantity:", self.quantity)

    def buy(self, quantity):
        """Buys a given quantity of the product.Returns the total price (float) of the purchase.
            Updates the quantity of the product.In case of a problem (when? think about it),
            raises an Exception.
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

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()