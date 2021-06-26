from collections import Counter

# TODO: implement multi-item bundles
# TODO: implement promotions

pricing_rules = {
    'A': {1: 50, 3: 130},  # 3 for 130
    'B': {1: 30, 2: 45, 5: 95},  # 30,  # 2 for 45
    'C': {1: 20},
    'D': {1: 15},
}


class CheckOut:
    def __init__(self, pricing=None):
        self.items = Counter()
        self.bundled = Counter()
        self.total = 0

        if pricing is None:
            self.pricing = pricing_rules
        else:
            self.pricing = pricing
        for item_name, rules in self.pricing.items():
            if 1 not in rules.keys():
                raise Warning(f'No price for single item {item_name}')

        self.bundles = {name: Counter() for name in self.pricing.keys()}


    def scan(self, items):
        for item_name in items:
            self.items[item_name] += 1
            # TODO: What is there are bundles of 1, 3, 5? We’d miss the 5
            count_all_items = self.items[item_name]
            count_free_items = self.items[item_name] - self.bundles[item_name]
            count_bundled_items = self.bundled[item_name]

            unbundled = self.items[item_name] # - self.bundled[item_name]
            while unbundled > 0:
                pack_sizes = self.pricing[item_name].keys()
                pack = max(pack for pack in pack_sizes if pack < unbundled)
                self.bundles[item_name][pack] += 1
                self.bundled[item_name] += pack
                self.total += self.pricing[item_name][pack]



            self.bundles[item_name]
            # TODO: What is there are bundles of different types of items
            if count_bundled_items == 0:

            if count_all_items in self.pricing[item_name].keys():
                if count_bundled_items == 0:
                    # Repeat
                    self.total += self.pricing[item_name][count_free_items]
                    if count_free_items > 1:
                        self.bundles[item_name] += count_free_items
                        self.total -= self.pricing[item_name][1] * (
                                    count_free_items - 1)
                    # End repeat
                else:
                    …
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
    co.scan('BBBBB')
    print(co.total)
