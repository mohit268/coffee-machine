import unittest

from Inventory import Inventory


class TestInventory(unittest.TestCase):

    def test_add_raw_material(self):
        test_input = {
            "total_items_quantity": {
                "hot_water": 500,
                "hot_milk": 500,
                "ginger_syrup": 100,
                "sugar_syrup": 100,
                "tea_leaves_syrup": 100
            }
        }

        inventory = Inventory().add_raw_material(test_input['total_items_quantity'])
        expected_output = {
            "hot_water": 500,
            "hot_milk": 500,
            "ginger_syrup": 100,
            "sugar_syrup": 100,
            "tea_leaves_syrup": 100

        }
        self.assertEqual(expected_output, inventory)

    def test_refill_inventory(self):
        inventory_input = {
            "total_items_quantity": {
                "hot_water": 0,
                "hot_milk": 500,
                "ginger_syrup": 100,
                "sugar_syrup": 100,
                "tea_leaves_syrup": 100
            }
        }
        inventory = Inventory()
        inventory.add_raw_material(inventory_input['total_items_quantity'])
        updated_inventory = inventory.refill_inventory("hot_water", 20)
        updated_expected_output = {
            "hot_water": 20,
            "hot_milk": 500,
            "ginger_syrup": 100,
            "sugar_syrup": 100,
            "tea_leaves_syrup": 100

        }
        self.assertEqual(updated_expected_output, updated_inventory)
