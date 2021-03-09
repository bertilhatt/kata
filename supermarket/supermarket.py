
class Item:
    def __init__(self, name):  #, price, special_price):
        self.name = name
        # self.price = price
        # self.special_price = special_price


class CheckOut:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = []
        self.total = 0
        pass

    def scan(self, items):
        for item in items:
            self.items.extend([item])

    def total(self):
        total = 0
        for item in self.items:
            total += self.pricing_rules[item]
        return total


pricing_rules = {
    'A': 50,  # 3 for 130
    'B': 30,  # 2 for 45
    'C': 20,
    'D': 15,
}


if __name__ == '__main__':
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('BB')
    print(co.total())
