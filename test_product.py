import pytest
from products import Product


# Test that creating a normal product works.

def test_creating_prod():
    name = "PS5"
    price = 599.00
    quantity = 50

    product = Product(name, price, quantity)

    assert product.name == name, "The product name was not set correctly"
    assert product.price == price, "The product price was not set correctly"
    assert product.quantity == quantity, "The product quantity was not set correctly"


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_creating_prod_invalid_details():
    name = ""
    price = -599.00
    quantity = 50

    product = Product(name, price, quantity)

    assert product.name == name, "The product name was not set correctly"
    assert product.price == price, "The product price was not set correctly"
    assert product.quantity == quantity, "The product quantity was not set correctly"


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_creating_prod_becomes_inactive():
    pass


# Test that product purchase modifies the quantity and returns the right output.
def test_buy_modifies_quantity():
    pass


# Test that buying a larger quantity than exists invokes exception.
def test_buy_too_much():
    pass
