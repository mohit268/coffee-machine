from collections import defaultdict


class Inventory(object):
    def __init__(self):
        self.materials = defaultdict(int)

    def add_raw_material(self, materials: dict):
        for material, quantity in materials.items():
            self.materials[material] = quantity

        return self.materials

    def refill_inventory(self, item, quantity):
        self.materials[item] = quantity
        return self.materials

    def show_inventory(self):
        print(self.materials)
