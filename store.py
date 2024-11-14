from products import Product


class Store:

    def __init__(self, product_list):
        self.product_list = []
        for product in product_list:
            self.product_list.append(product)

    def add_product(self, product):
        """Adds product to store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        return sum(product.quantity for product in self.product_list)

    def get_all_products(self):
        """Returns all products in the store that are active"""
        return self.product_list

    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
            Product (Product class) and quantity (int).
            Buys the products and returns the total price of the order."""
        total_cost = 0.0
        for item in shopping_list:
            product, quantity_needed = item
            if product in self.product_list and product.quantity >= quantity_needed:
                product.quantity -= quantity_needed
                total_cost += product.price * quantity_needed
            else:
                raise ValueError(f"Insufficient quantity for product: {product.name}")
        return total_cost
