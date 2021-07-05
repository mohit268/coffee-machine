import unittest

from Beverage import Beverages


class TestBeverages(unittest.TestCase):

    def test_add_beverages(self):
        test_input = {
            "beverages": {
                "hot_tea": {
                    "hot_water": 200,
                    "hot_milk": 100,
                    "ginger_syrup": 10,
                    "sugar_syrup": 10,
                    "tea_leaves_syrup": 30
                }
            }
        }
        beverage = Beverages().add_beverages(test_input['beverages'])
        expected_output = {
            "hot_tea": {
                "hot_water": 200,
                "hot_milk": 100,
                "ginger_syrup": 10,
                "sugar_syrup": 10,
                "tea_leaves_syrup": 30
            }
        }
        self.assertEqual(expected_output, beverage)
