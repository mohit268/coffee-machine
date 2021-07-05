from collections import defaultdict


class Beverages(object):
    def __init__(self):
        self.beverages = defaultdict(dict)

    def add_beverages(self, beverages: dict):
        for product, ingredients in beverages.items():
            self.beverages[product] = ingredients

        return self.beverages
