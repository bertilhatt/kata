from collections import Counter

# TODO: implement multi-item bundles
# TODO: implement promotions

pricing_rules = {
    'A': {1: 50, 3: 130},  # 3 for 130
    'B': {1: 30, 2: 45},  # 30,  # 2 for 45
    'C': {1: 20},
    'D': {1: 15},
}


class CheckOut:
    def __init__(self, pricing=None):
        self.items = Counter()
        self.bundles = Counter()
        self.total = 0

        if pricing is None:
            self.pricing = pricing_rules
        else:
            self.pricing = pricing
        for item_name, rules in self.pricing.items():
            if 1 not in rules.keys():
                raise Warning(f'No price for single item {item_name}')

    def scan(self, items):
        for item_name in items:
            self.items[item_name] += 1
            # TODO: What is there are bundles of 1, 3, 5? We’d miss the 5
            count_free_items = self.items[item_name] - self.bundles[item_name]
            # TODO: What is there are bundles of different types of items
            if count_free_items in self.pricing[item_name].keys():
                self.total += self.pricing[item_name][count_free_items]
                if count_free_items > 1:
                    self.bundles[item_name] += count_free_items
                    self.total -= self.pricing[item_name][1] * (count_free_items-1)
            else:
                self.total += self.pricing[item_name][1]

    # TODO: implement an item retraction


if __name__ == '__main__':
    co = CheckOut(pricing_rules)
    co.scan('A')
    co.scan('BB')
    print(co.total)
