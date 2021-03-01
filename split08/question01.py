import unittest


class Product:
    def __init__(self, name, price, count):
        if price < 0 or count < 0:
            raise AttributeError

        self.name = name
        self.price = price
        self.count = count

    def discount_price(self):
        if self.count in range(5, 7):
            return self.price * 0.95
        elif self.count in range(7, 10):
            return self.price * 0.9
        elif self.count in range(10, 20):
            return self.price * 0.8
        elif self.count == 20:
            return self.price * 0.7
        elif self.count > 20:
            return self.price * 0.5
        else:
            return self.price


class Cart:
    def __init__(self, products: list) -> None:
        self.products = products

    def get_total_price(self):
        return sum([x.discount_price() * x.count for x in self.products])


class CartTest(unittest.TestCase):
    def test_total_price_1(self):
        product1 = Product('1', 100, 5)
        product2 = Product('2', 100, 20)
        product3 = Product('3', 100, 10)
        cart = Cart([product1, product2, product3])
        self.assertEqual(cart.get_total_price(),
                        product1.discount_price() * product1.count +\
                        product2.discount_price() * product2.count +\
                        product3.discount_price() * product3.count)