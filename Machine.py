import Beverage
from Inventory import Inventory
import copy


class Machine(object):
    def __init__(self, outlet: int, inventory: Inventory, beverage: Beverage):
        self.outlet = outlet
        self.inventory = inventory
        self.beverage = beverage

    def order(self, orders):
        if len(orders) > self.outlet:
            print("Orders more than outlets processing top orders on first come first serve basis.")

        for order in orders[:self.outlet]:
            if order not in self.beverage.keys():
                print(str(order) + " is not available!!!")
            else:
                order_processed, result, raw_ingredient_quantity = self.process_order(order)
                if order_processed:
                    print(str(result) + " is prepared!!")
                else:
                    if raw_ingredient_quantity != 0:
                        print(str(order) + " cannot be prepared because " + str(result) + \
                              " is not sufficient!!!")
                    else:
                        print(str(order) + " cannot be prepared because " + str(result) + \
                              " is not available!!!")

    def process_order(self, order):
        order_ingredient = self.beverage.get(order)
        temp = copy.deepcopy(self.inventory)
        order_processed = True
        for ingredient, quantity in order_ingredient.items():
            if ingredient not in temp.keys():
                order_processed = False
                return order_processed, ingredient, 0
            if temp[ingredient] < quantity:
                order_processed = False
                return order_processed, ingredient, temp[ingredient]
            temp[ingredient] -= quantity

        if order_processed:
            self.inventory = temp
        return order_processed, order, "dummy"
