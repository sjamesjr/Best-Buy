from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        print(f"Applying SecondHalfPrice promotion: {product.name}, Quantity: {quantity}")
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total_price = full_price_items * product.price + half_price_items * (product.price / 2)
        print(f"Total price after promotion: {total_price}")
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        print(f"Applying ThirdOneFree promotion: {product.name}, Quantity: {quantity}")
        paid_items = quantity - (quantity // 3)
        total_price = paid_items * product.price
        print(f"Total price after promotion: {total_price}")
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent: int):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        print(f"Applying PercentDiscount promotion: {product.name}, Quantity: {quantity}, Percent: {self.percent}%")
        total_price = product.price * quantity * (1 - self.percent / 100)
        print(f"Total price after promotion: {total_price}")
        return total_price
