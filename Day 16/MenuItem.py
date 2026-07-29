class MenuItem:
        def __init__(self,name, water, milk, coffee, cost):
                self.name = name
                self.cost = cost
                self.ingredients = {
                        "water" : water,
                        "milk" : milk,
                        "coffee": coffee
                }


class Menu:
        def __init__(self):
                self.menu = [
                    MenuItem("Latte", 200, 150, 24, 2.5),
                    MenuItem("Espresso", 50, 0, 18, 1.5),
                    MenuItem("Cappuccino", 250, 50, 24, 3.0)
                ]

        def getItems(self):
            """Returns names of all the available menu items"""
            options = ""
            for item in self.menu:
                   options += f"{self.menu}"
            return options

        def findDrink(self, orderName):
            """Searches the menu for that item"""
            for item in self.menu:
                   if item.name == orderName:
                          return item
            print("Sorry Item not available!")