import pytest
from products import Product, LimitedProduct, NonStockedProduct


# Test that creating a normal product works.
def test_creating_prod():
    name = "PS5"
    price = 599.00
    quantity = 50

    product = Product(name, price, quantity)

    assert product.name == name, "The product name was not set correctly"
    assert product.price == price, "The product price was not set correctly"
    assert product.quantity == quantity, "The product quantity was not set correctly"
    assert product.is_active(), "The product should be active by default"


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_creating_prod_invalid_details():
    name = ""
    price = -599.00
    quantity = 50

    with pytest.raises(ValueError, match="Invalid product details"):
        Product(name, price, quantity)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_creating_prod_becomes_inactive():
    name = "PS5"
    price = 599.00
    quantity = 1

    product = Product(name, price, quantity)
    product.buy(1)  # Assuming there's a method buy to reduce quantity

    assert product.get_quantity() == 0, "The product quantity was not updated to 0"
    assert not product.is_active(), "The product should become inactive when quantity reaches 0"


# Test that product purchase modifies the quantity and returns the right output.
def test_buy_modifies_quantity():
    name = "PS5"
    price = 599.00
    quantity = 50

    product = Product(name, price, quantity)
    total_price = product.buy(10)

    assert product.get_quantity() == 40, "The product quantity was not updated correctly after purchase"
    assert total_price == 599.00 * 10, "The total price calculation is incorrect"


# Test that buying a larger quantity than exists invokes exception.
def test_buy_too_much():
    name = "PS5"
    price = 599.00
    quantity = 10

    product = Product(name, price, quantity)

    with pytest.raises(Exception, match="Insufficient quantity available"):
        product.buy(15)
