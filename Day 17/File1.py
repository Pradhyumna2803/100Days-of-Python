class BankAccount:
    def __init__(self,accountnumber ,ownername , balance):
        self.accountnumber = accountnumber
        self.owner = ownername
        self.balance = balance

    # def greet(self,fx):
    #     def mfx(*args, **kwargs):
    #         print("Greetings!")
    #         fx(*args, **kwargs)
    #         print("Thanks for using our bank's services.")
    #     return mfx

    #@greet
    def deposit_money(self, accountnumber, amount):
        print(f"Your account {self.accountnumber} is credited with {amount}")
        self.balance += amount

    #@greet
    def withdraw_money(self, accountnumber, amount):
        print(f"Amount {amount} is debited from your account {self.accountnumber}. Remaining balance is {self.balance - amount} ")

    #@greet
    def check_balance(self, accountnumber):
        print(f"Your balance is {self.balance}")


#Examples for Getters & Setters

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'The value is {self._value}')

    @property
    def x10(self):
        return self._value * 10

    @x10.setter
    def x10(self):
        return self._value / 10


# acc1 = BankAccount(123,"Ganesh",50000)
# acc1.withdraw_money(123,8910)

obj = MyClass(10)
obj.x10 = 25
print(obj.x10)
obj.show()

