from products import Product
from store import Store


def main():
    product_list = [Product("MacBook Air M2", 1450, 100),
                    Product("Bose QuietComfort Earbuds", 250, 500),
                    Product("Google Pixel 7", 500, 250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store)
    print(store.get_total_quantity())
    print(products)
    print(type(products[0]))
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
