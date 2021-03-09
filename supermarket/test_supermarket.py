import unittest
# from supermarket_price_in_checkout import CheckOut, pricing_rules
from supermarket_price_in_items import CheckOut, pricing_rules


def price(goods):
    co = CheckOut()
    for item in goods:
        co.scan(item)
    return co.total


class TestPrice(unittest.TestCase):
    def test_incremental(self):
        co = CheckOut()
        self.assertEqual(0, co.total)
        co.scan("A")
        self.assertEqual(50, co.total)
        co.scan("B")
        self.assertEqual(80, co.total)
        co.scan("A")
        self.assertEqual(130, co.total)
        co.scan("A")
        self.assertEqual(160, co.total)
        co.scan("B")
        self.assertEqual(175, co.total)

    def test_totals(self):
        self.assertEqual(0, price(""))
        self.assertEqual(50, price("A"))
        self.assertEqual(80, price("AB"))
        self.assertEqual(115, price("CDBA"))

        self.assertEqual(100, price("AA"))
        self.assertEqual(130, price("AAA"))
        self.assertEqual(180, price("AAAA"))
        self.assertEqual(230, price("AAAAA"))
        self.assertEqual(260, price("AAAAAA"))

        self.assertEqual(160, price("AAAB"))
        self.assertEqual(175, price("AAABB"))
        self.assertEqual(190, price("AAABBD"))
        self.assertEqual(190, price("DABABA"))


if __name__ == '__main__':
    unittest.main()
