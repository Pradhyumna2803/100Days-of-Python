class MoneyMachine:
    Currency = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_recieved = 0

    def report(self):
        print(f"Money : {self.profit}")

    def process_coins(self):
        """Returns the total calculated coins from the coins inserted"""
        print("Please insert coints")
        for coin in self.COIN_VALUES:
            self.money_recieved += int(input(f"How many {coin}? : ")) * self.COIN_VALUES[coin]
        return self.money_recieved

    def make_payment(self,cost):
        """Returns true when payment is accpeted, or false if insufficient"""
        self.process_coins()
        if(self.money_recieved >= cost):
            change = round(self.money_recieved - cost , 2)
            print(f"Here is {self.Currency}{change} in change. ")
            self.profit += cost
            self.money_recieved = 0
            return True
        else:
            print("Sorry, money is not sufficient. Money refunded.")
            self.money_recieved = 0
            return False