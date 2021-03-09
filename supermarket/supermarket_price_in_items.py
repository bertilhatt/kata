from collections import Counter

pricing_rules = {
    'A': 50,  # 3 for 130
    'B': 30,  # 2 for 45
    'C': 20,
    'D': 15,
}

special_prices = {
    'A': {3: 130},
    'B': {2: 45},
    'C': {},
    'D': {},
}


class Item:
    def __init__(self, name, price=None, special_price=None):
        self.name = name
        if price is None:
            self.price = pricing_rules[name]
        elif type(price) in (float, int):
            self.price = price
        if price is None:
            self.special_price = special_prices[name]
        elif type(price) == dict:
            self.special_price = special_price
        self.part_of_a_bundle = False


class CheckOut:
    def __init__(self):
        self.items = Counter()
        self.bundles = Counter()
        self.total = 0
        pass

    def scan(self, items):
        for name in items:
            item = Item(name)
            self.items[name] += 1
            item_unbundled_count = self.items[name] - self.bundles[name]

            if item_unbundled_count in item.special_price.keys():
                bundle_count = item_unbundled_count
                self.bundles[name] += bundle_count
                self.total += item.special_price[bundle_count]
                self.total -= item.price * (bundle_count-1)
            else:
                self.total += item.price


if __name__ == '__main__':
    co = CheckOut()
    co.scan('A')
    co.scan('BB')
    print(co.total)
