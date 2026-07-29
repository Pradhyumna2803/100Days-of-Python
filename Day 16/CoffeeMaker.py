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

    