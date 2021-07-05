import unittest
import io
import unittest.mock
from Beverage import Beverages
from Inventory import Inventory
from Machine import Machine


class TestMachine(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_successful_order(self, mock_stdout):
        test_input = {
            "machine": {
                "outlets": {
                    "count_n": 4
                },
                "total_items_quantity": {
                    "hot_water": 500,
                    "hot_milk": 500,
                    "ginger_syrup": 100,
                    "sugar_syrup": 100,
                    "tea_leaves_syrup": 100
                },
                "beverages": {
                    "hot_tea": {
                        "hot_water": 200,
                        "hot_milk": 100,
                        "ginger_syrup": 10,
                        "sugar_syrup": 10,
                        "tea_leaves_syrup": 30
                    },
                    "hot_coffee": {
                        "hot_water": 100,
                        "ginger_syrup": 30,
                        "hot_milk": 400,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    },
                    "black_tea": {
                        "hot_water": 300,
                        "ginger_syrup": 30,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    },
                    "green_tea": {
                        "hot_water": 100,
                        "green_mixture": 30,
                        "ginger_syrup": 30,
                        "sugar_syrup": 50,

                    }
                }
            }
        }

        inventory = Inventory().add_raw_material(test_input['machine']['total_items_quantity'])
        beverage = Beverages().add_beverages(test_input['machine']['beverages'])

        machine = Machine(test_input['machine']['outlets']['count_n'], inventory, beverage)
        machine.order(['hot_tea', 'hot_coffee'])
        expected_output = "hot_tea is prepared!!\n" + \
                          "hot_coffee is prepared!!\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_processing_more_orders_than_outlet(self, mock_stdout):
        test_input = {
            "machine": {
                "outlets": {
                    "count_n": 4
                },
                "total_items_quantity": {
                    "hot_water": 500,
                    "hot_milk": 500,
                    "ginger_syrup": 100,
                    "sugar_syrup": 100,
                    "tea_leaves_syrup": 100
                },
                "beverages": {
                    "hot_tea": {
                        "hot_water": 200,
                        "hot_milk": 100,
                        "ginger_syrup": 10,
                        "sugar_syrup": 10,
                        "tea_leaves_syrup": 30
                    },
                    "hot_coffee": {
                        "hot_water": 100,
                        "ginger_syrup": 30,
                        "hot_milk": 400,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    },
                    "black_tea": {
                        "hot_water": 300,
                        "ginger_syrup": 30,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    },
                    "green_tea": {
                        "hot_water": 100,
                        "green_mixture": 30,
                        "ginger_syrup": 30,
                        "sugar_syrup": 50,

                    }
                }
            }
        }

        inventory = Inventory().add_raw_material(test_input['machine']['total_items_quantity'])
        beverage = Beverages().add_beverages(test_input['machine']['beverages'])

        machine = Machine(test_input['machine']['outlets']['count_n'], inventory, beverage)
        machine.order(['hot_tea', 'hot_coffee', 'green_tea', 'black_tea', 'hot_tea'])
        expected_output = "Orders more than outlets processing top orders on first come first " \
                          "serve basis.\n" + \
                          "hot_tea is prepared!!\n" + \
                          "hot_coffee is prepared!!\n" + \
                          "green_tea cannot be prepared because green_mixture is not available!!!\n" + \
                          "black_tea cannot be prepared because hot_water is not sufficient!!!\n"

        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_beverage_not_available(self, mock_stdout):
        test_input = {
            "machine": {
                "outlets": {
                    "count_n": 4
                },
                "total_items_quantity": {
                    "hot_water": 500,
                    "hot_milk": 500,
                    "ginger_syrup": 100,
                    "sugar_syrup": 100,
                    "tea_leaves_syrup": 100
                },
                "beverages": {
                    "hot_tea": {
                        "hot_water": 200,
                        "hot_milk": 100,
                        "ginger_syrup": 10,
                        "sugar_syrup": 10,
                        "tea_leaves_syrup": 30
                    },
                    "hot_coffee": {
                        "hot_water": 100,
                        "ginger_syrup": 30,
                        "hot_milk": 400,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    }
                }
            }
        }

        inventory = Inventory().add_raw_material(test_input['machine']['total_items_quantity'])
        beverage = Beverages().add_beverages(test_input['machine']['beverages'])
        machine = Machine(test_input['machine']['outlets']['count_n'], inventory, beverage)
        machine.order(['hot_tea', 'cold_coffee'])
        expected_output = "hot_tea is prepared!!\n" + \
                          "cold_coffee is not available!!!\n"

        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ingredient_not_available(self, mock_stdout):
        test_input = {
            "machine": {
                "outlets": {
                    "count_n": 4
                },
                "total_items_quantity": {
                    "hot_water": 500,
                    "hot_milk": 500,
                    "ginger_syrup": 100,
                    "sugar_syrup": 100,
                    "tea_leaves_syrup": 100
                },
                "beverages": {
                    "hot_tea": {
                        "hot_water": 200,
                        "hot_milk": 100,
                        "ginger_syrup": 10,
                        "sugar_syrup": 10,
                        "tea_leaves_syrup": 30
                    },
                    "green_tea": {
                        "hot_water": 100,
                        "green_mixture": 30,
                        "ginger_syrup": 30,
                        "sugar_syrup": 50,

                    }
                }
            }
        }

        inventory = Inventory().add_raw_material(test_input['machine']['total_items_quantity'])
        beverage = Beverages().add_beverages(test_input['machine']['beverages'])
        machine = Machine(test_input['machine']['outlets']['count_n'], inventory, beverage)
        machine.order(['hot_tea', 'green_tea'])
        expected_output = "hot_tea is prepared!!\n" + \
                          "green_tea cannot be prepared because green_mixture is not available!!!\n"

        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ingredient_not_sufficient(self, mock_stdout):
        test_input = {
            "machine": {
                "outlets": {
                    "count_n": 4
                },
                "total_items_quantity": {
                    "hot_water": 500,
                    "hot_milk": 500,
                    "ginger_syrup": 100,
                    "sugar_syrup": 100,
                    "tea_leaves_syrup": 40
                },
                "beverages": {
                    "hot_tea": {
                        "hot_water": 200,
                        "hot_milk": 100,
                        "ginger_syrup": 10,
                        "sugar_syrup": 10,
                        "tea_leaves_syrup": 30
                    },
                    "hot_coffee": {
                        "hot_water": 100,
                        "ginger_syrup": 30,
                        "hot_milk": 400,
                        "sugar_syrup": 50,
                        "tea_leaves_syrup": 30
                    }
                }
            }
        }

        inventory = Inventory().add_raw_material(test_input['machine']['total_items_quantity'])
        beverage = Beverages().add_beverages(test_input['machine']['beverages'])
        machine = Machine(test_input['machine']['outlets']['count_n'], inventory, beverage)
        machine.order(['hot_tea', 'hot_coffee'])
        expected_output = "hot_tea is prepared!!\n" + \
                          "hot_coffee cannot be prepared because tea_leaves_syrup is not " \
                          "sufficient!!!\n"

        self.assertEqual(expected_output, mock_stdout.getvalue())
