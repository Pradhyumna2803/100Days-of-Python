class CoffeeMaker:
    def __init__(self):
        self.resources ={
            "water" : 300,
            "coffee" : 250,
            "milk" : 450,
        }

    def report(self):
        """Prints the resources left in the coffee machine"""
        print(f"There is {self.resources["water"]}ml of water left")
        print(f"There is {self.resources["milk"]}ml of milk left")
        print(f"There is {self.resources["coffee"]}g of water left")

    def is_resource_sufficient(self,drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f'Here is your {order.name}. Enjoy!')